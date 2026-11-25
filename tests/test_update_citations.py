import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('update_citations', ROOT / 'scripts/update_citations.py')
updater = importlib.util.module_from_spec(spec)
spec.loader.exec_module(updater)
NOW = '2026-11-22T20:00:00+00:00'
OLD = '2026-11-21T20:00:00+00:00'

def data():
    return {'version':1,'provider':'OpenAlex','papers':{
        'p':{'title':'Paper A','url':'https://arxiv.org/abs/2401.00001','aliases':['Paper A'],
             'openalex_id':'W1','citation_count':7,'updated_at':OLD},
        'q':{'title':'Paper B','url':'https://arxiv.org/abs/2401.00002','aliases':['Paper B','Alternate title'],
             'openalex_id':None,'citation_count':None,'updated_at':None}}}

README = '# Resources\n\n## Table of Contents\n\n## Foundation\n1. [Paper A](https://arxiv.org/abs/2401.00001) (ICML 2024) [[code]](https://example.org/code)\n2. [Paper B](https://arxiv.org/abs/2401.00002) (preprint)\n'

class FakeClient:
    def __init__(self, results): self.results = iter(results); self.calls = []
    def get(self, **params):
        self.calls.append(params)
        result = next(self.results)
        if isinstance(result, Exception): raise result
        return result

class UpdaterTests(unittest.TestCase):
    def test_valid_zero_and_exact_alias_match(self):
        d = data()
        c = FakeClient([[{'id':'https://openalex.org/W1','title':'Paper A','cited_by_count':0}],
                        [{'id':'https://openalex.org/W2','title':'Alternate TITLE!','cited_by_count':13}]])
        refreshed, errors = updater.refresh(d, ['p','q'], c, NOW)
        self.assertEqual(refreshed, {'p','q'}); self.assertFalse(errors)
        self.assertEqual(d['papers']['p']['citation_count'], 0)
        self.assertEqual(d['papers']['q']['openalex_id'], 'W2')
        self.assertIn('[Citations: 0]', updater.render(README, d, ['p','q']))

    def test_missing_record_retains_its_count_and_timestamp(self):
        d = data(); original = copy.deepcopy(d['papers']['p'])
        d['papers']['q']['openalex_id']='W2'
        updater.refresh(d,['p','q'],FakeClient([[{'id':'https://openalex.org/W2','cited_by_count':1}]]),NOW)
        self.assertEqual(d['papers']['p'], original)

    def test_malformed_counts_do_not_become_zero(self):
        for value in (None, -1, True, '3', 1.5):
            with self.subTest(value=value):
                d=data(); before=copy.deepcopy(d)
                with self.assertRaises(RuntimeError):
                    updater.refresh(d,['p'],FakeClient([[{'id':'https://openalex.org/W1','cited_by_count':value}]]),NOW)
                self.assertEqual(d,before)

    def test_malformed_ids_are_ignored(self):
        d=data()
        with self.assertRaises(RuntimeError):
            updater.refresh(d,['p'],FakeClient([[{'id':None,'cited_by_count':42},None]]),NOW)
        self.assertEqual(d['papers']['p']['citation_count'],7)

    def test_unrelated_search_result_not_used(self):
        d=data()
        with self.assertRaises(RuntimeError):
            updater.refresh(d,['q'],FakeClient([[{'id':'https://openalex.org/W9','title':'Unrelated paper','cited_by_count':9999}]]),NOW)
        self.assertIsNone(d['papers']['q']['citation_count'])

    def test_partial_request_failure_retains_cached_values(self):
        d=data()
        done, errors=updater.refresh(d,['p','q'],FakeClient([
            [{'id':'https://openalex.org/W1','cited_by_count':8}],RuntimeError('rate limit')]),NOW)
        self.assertEqual(done,{'p'});self.assertEqual(errors,['rate limit'])
        self.assertIsNone(d['papers']['q']['citation_count'])

    def test_render_is_idempotent_and_preserves_prose_and_venues(self):
        d=data(); first=updater.render(README,d,['p','q'])
        self.assertEqual(first,updater.render(first,d,['p','q']))
        self.assertEqual(first.count('<!-- citations:start -->'),2)
        self.assertEqual(first.count('<!-- citation-summary:start -->'),1)
        self.assertIn('(ICML 2024) [[code]](https://example.org/code)',first)
        self.assertIn('*Citations: unavailable*',first)
        self.assertNotIn('<script',first)
        self.assertIn(OLD,first)

    def test_auto_discovers_new_arxiv_paper_but_not_tutorial(self):
        d=data()
        text=README+'3. [New paper](https://arxiv.org/abs/2401.00003)\n## Tutorials\n1. [Tutorial](https://arxiv.org/abs/2401.00004)\n'
        keys=updater.discover(text,d)
        self.assertIn('2401.00003',keys)
        self.assertNotIn('2401.00004',keys)

    def test_total_network_failure_leaves_both_files_unchanged(self):
        with tempfile.TemporaryDirectory() as folder:
            readme=Path(folder)/'README.md'; snapshot=Path(folder)/'citations.json'
            readme.write_text(README);snapshot.write_text(json.dumps(data()))
            before=(readme.read_bytes(),snapshot.read_bytes())
            with patch.object(updater,'Client',return_value=FakeClient([RuntimeError('offline'),RuntimeError('offline')])):
                with self.assertRaises(RuntimeError):updater.main(['--readme',str(readme),'--data',str(snapshot)])
            self.assertEqual(before,(readme.read_bytes(),snapshot.read_bytes()))

    def test_offline_mode_requires_no_api_and_is_repeatable(self):
        with tempfile.TemporaryDirectory() as folder:
            readme=Path(folder)/'README.md'; snapshot=Path(folder)/'citations.json'
            readme.write_text(README);snapshot.write_text(json.dumps(data()))
            args=['--offline','--readme',str(readme),'--data',str(snapshot)]
            with patch.object(updater,'Client',side_effect=AssertionError('offline mode must not call the API')):
                updater.main(args);first=(readme.read_bytes(),snapshot.read_bytes());updater.main(args)
            self.assertEqual(first,(readme.read_bytes(),snapshot.read_bytes()))

    def test_all_repository_papers_render_as_markdown(self):
        d=json.loads((ROOT/'data/citations.json').read_text())
        readme=(ROOT/'README.md').read_text()
        keys=updater.discover(readme,d)
        self.assertTrue(keys)
        result=updater.render(readme,d,keys)
        available=sum(updater.valid_count(d['papers'][key].get('citation_count')) for key in keys)
        self.assertEqual(result.count('<!-- citations:start -->'),len(keys))
        self.assertEqual(result.count('[Citations:'),available)
        self.assertEqual(result.count('*Citations: unavailable*'),len(keys)-available)
        self.assertEqual(result,updater.render(result,d,keys))

if __name__ == '__main__': unittest.main()
