#!/usr/bin/env python3
"""Refresh OpenAlex counts and write ordinary Markdown into README.md (stdlib only)."""
import argparse
import copy
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ENTRY = re.compile(r'^\d+\. \[(.*?)\]\((https?://[^)]+)\)')
BADGE = re.compile(r'\s*<!-- citations:start -->.*?<!-- citations:end -->')
SUMMARY = re.compile(r'<!-- citation-summary:start -->.*?<!-- citation-summary:end -->\n*', re.S)
PAPER_HOSTS = {'arxiv.org', 'doi.org', 'openreview.net', 'proceedings.mlr.press',
               'proceedings.neurips.cc', 'papers.nips.cc', 'papers.nips.org',
               'ieeexplore.ieee.org', 'aclanthology.org', 'openaccess.thecvf.com'}

def normalize(title):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', title).lower())

def valid_count(value):
    return type(value) is int and value >= 0

def work_id(work):
    value = work.get('id')
    value = value.removeprefix('https://openalex.org/') if isinstance(value, str) else ''
    return value if re.fullmatch(r'W\d+', value) else None

class Client:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def get(self, **params):
        params.update(select='id,title,cited_by_count', per_page=100)
        request = Request('https://api.openalex.org/works?' + urlencode(params),
                          headers={'User-Agent': 'awesome-ssm-ml-citations/1.0'})
        if self.api_key:
            request.add_header('Authorization', 'Bearer ' + self.api_key)
        for attempt in range(3):
            try:
                with urlopen(request, timeout=30) as response:
                    result = json.load(response)
                if not isinstance(result, dict) or not isinstance(result.get('results'), list):
                    raise ValueError('OpenAlex returned an invalid results list')
                return result['results']
            except HTTPError as error:
                if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                    raise RuntimeError(f'OpenAlex HTTP {error.code}') from None
                retry = error.headers.get('Retry-After', '')
                delay = min(float(retry), 30) if retry.isdigit() else 2 ** attempt
                time.sleep(delay)
            except (URLError, TimeoutError):
                if attempt == 2:
                    raise RuntimeError('OpenAlex is unreachable') from None
                time.sleep(2 ** attempt)
        raise RuntimeError('OpenAlex request failed')

def discover(readme, data):
    """Track added papers by their first link; ignore books, tutorials, and software."""
    by_url = {p['url']: key for key, p in data['papers'].items()}
    active = []
    section = ''
    for line in readme.splitlines():
        if line.startswith('## '):
            section = line
        match = ENTRY.match(line)
        if not match:
            continue
        title, url = match.groups()
        if url not in by_url:
            if section.startswith(('## Tutorials', '## Books', '## Libraries', '## Contributions')):
                continue
            if urlsplit(url).hostname not in PAPER_HOSTS:
                continue
            arxiv = re.search(r'arxiv.org/(?:abs|pdf)/(\d+\.\d+)', url)
            key = arxiv.group(1) if arxiv else url
            data['papers'][key] = {'title': title, 'url': url, 'aliases': [title],
                                  'openalex_id': None, 'citation_count': None, 'updated_at': None}
            by_url[url] = key
        key = by_url[url]
        paper = data['papers'][key]
        if title not in paper['aliases']:
            paper['aliases'].append(title)
        active.append(key)
    return list(dict.fromkeys(active))

def refresh(data, keys, client, now):
    """Never replace a saved count or timestamp with missing/invalid API data."""
    known = [key for key in keys if data['papers'][key].get('openalex_id')]
    refreshed = set()
    errors = []

    def accept(key, work):
        if not work_id(work) or not valid_count(work.get('cited_by_count')):
            return False
        paper = data['papers'][key]
        paper.update(openalex_id=work_id(work), citation_count=work['cited_by_count'], updated_at=now)
        refreshed.add(key)
        return True

    for start in range(0, len(known), 100):
        group = known[start:start + 100]
        ids = list(dict.fromkeys(data['papers'][key]['openalex_id'] for key in group))
        try:
            works = client.get(filter='openalex:' + '|'.join(ids))
            returned = {work_id(work): work for work in works if isinstance(work, dict)}
            for key in group:
                work = returned.get(data['papers'][key]['openalex_id'])
                if work:
                    accept(key, work)
        except (RuntimeError, ValueError) as error:
            errors.append(str(error))

    for key in keys:
        paper = data['papers'][key]
        if paper.get('openalex_id'):
            continue
        try:
            works = client.get(filter='title.search:' + max(paper['aliases'], key=len))
            titles = {normalize(title) for title in paper['aliases']}
            matches = [w for w in works if isinstance(w, dict) and isinstance(w.get('title'), str)
                       and normalize(w['title']) in titles and valid_count(w.get('cited_by_count'))
                       and work_id(w)]
            if matches:
                # Duplicate records are not added together, which would double-count citations.
                accept(key, max(matches, key=lambda w: w['cited_by_count']))
        except (RuntimeError, ValueError) as error:
            errors.append(str(error))
    if not refreshed:
        raise RuntimeError('No valid citation counts refreshed; saved files were not changed. '
                           + (errors[0] if errors else 'OpenAlex returned no usable records.'))
    return refreshed, errors

def render(readme, data, keys):
    by_url = {data['papers'][key]['url']: data['papers'][key] for key in keys}
    lines = []
    for line in SUMMARY.sub('', readme).splitlines():
        match = ENTRY.match(line)
        if match and match.group(2) in by_url:
            paper = by_url[match.group(2)]
            line = BADGE.sub('', line)
            if valid_count(paper.get('citation_count')) and paper.get('openalex_id'):
                checked = paper.get('updated_at') or 'unknown'
                badge = f'[Citations: {paper["citation_count"]:,}](https://openalex.org/{paper["openalex_id"]} "OpenAlex; checked {checked}")'
            else:
                badge = '*Citations: unavailable*'
            line += ' <!-- citations:start --> ' + badge + ' <!-- citations:end -->'
        lines.append(line)
    readme = '\n'.join(lines) + '\n'
    dates = [data['papers'][key].get('updated_at') for key in keys if valid_count(data['papers'][key].get('citation_count'))]
    latest = max((date for date in dates if date), default='not yet checked')
    summary = ('<!-- citation-summary:start -->\n'
               '> Citation counts: [OpenAlex](https://openalex.org/), refreshed daily by GitHub Actions. '
               f'Latest successful check: {latest}. Hover over a count for its individual check time; '
               'unmatched papers show "unavailable".\n'
               '<!-- citation-summary:end -->\n\n')
    if '## Table of Contents\n' in readme:
        return readme.replace('## Table of Contents\n', summary + '## Table of Contents\n', 1)
    return readme.split('\n', 1)[0] + '\n\n' + summary + readme.split('\n', 1)[1].lstrip('\n')

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--readme', type=Path, default=ROOT / 'README.md')
    parser.add_argument('--data', type=Path, default=ROOT / 'data/citations.json')
    parser.add_argument('--offline', action='store_true', help='Render the stored snapshot without network requests')
    args = parser.parse_args(argv)
    readme = args.readme.read_text(encoding='utf-8')
    data = json.loads(args.data.read_text(encoding='utf-8'))
    if data.get('version') != 1 or data.get('provider') != 'OpenAlex':
        raise ValueError('Unsupported citation data schema')
    data = copy.deepcopy(data)
    keys = discover(readme, data)
    if not keys:
        raise ValueError('No papers found in README; refusing to overwrite it')
    if not args.offline:
        now = datetime.now(timezone.utc).isoformat(timespec='seconds')
        refreshed, errors = refresh(data, keys, Client(os.environ.get('OPENALEX_API_KEY')), now)
        print(f'Refreshed {len(refreshed)}/{len(keys)} papers.')
        if errors:
            print(f'Warning: {len(errors)} requests failed; previous counts and timestamps retained.', file=sys.stderr)
    result = render(readme, data, keys)
    # Both are fully prepared before either existing file is replaced.
    data_text = json.dumps(data, indent=2, ensure_ascii=False) + '\n'
    for path, text in [(args.data, data_text), (args.readme, result)]:
        temp = path.with_suffix(path.suffix + '.tmp')
        temp.write_text(text, encoding='utf-8')
        temp.replace(path)
    available = sum(valid_count(data['papers'][key].get('citation_count')) for key in keys)
    print(f'README: {available} citation counts; {len(keys)-available} unavailable. No JavaScript required.')

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, RuntimeError) as error:
        print(f'Citation update failed: {error}', file=sys.stderr)
        sys.exit(1)
