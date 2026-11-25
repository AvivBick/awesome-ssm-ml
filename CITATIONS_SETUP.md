# Citation counts in the GitHub README

The counts are ordinary Markdown links inside `README.md`. GitHub renders them without JavaScript, a website, or a browser cache. OpenAlex is the source; counts can differ from Google Scholar and other indexes.

## Local files

Copy these files into the existing repository, preserving their paths:

- `README.md`
- `data/citations.json`
- `scripts/update_citations.py`
- `tests/test_update_citations.py`
- `.github/workflows/update-citations.yml` (the `.github` folder is hidden in some file browsers)

`preview.html` previews the same static README counts; it makes no API requests. `README.diff` compares the updated reading list with the original repository README. The ZIP includes the repository files and this guide.

Everything has been prepared locally. The workflow is not installed or running on GitHub yet.

## Activate later on GitHub

When you choose to commit and push the files to the repository's default branch, the workflow can run daily at 07:23 UTC. To refresh immediately, select **Actions → Update citation counts → Run workflow**. GitHub schedules may be delayed; public repositories can have schedules disabled after 60 days without activity.

The workflow requests `contents: write` to commit only `README.md` and `data/citations.json` after refreshing counts. Repository or organization policy must allow Actions and that write permission. If branch protection prevents the bot from pushing, the job will fail visibly rather than bypass the rule.

No OpenAlex key is required for basic API use. Optionally add a repository secret named `OPENALEX_API_KEY` for a larger independent quota. The updater reads the secret from its environment; it does not write the key into the README or citation data.

## Run locally

Python 3.10 or newer is sufficient; there are no third-party dependencies.

```sh
python scripts/update_citations.py
python -m unittest discover -s tests -p 'test_update_citations.py' -v
```

Render only the existing snapshot without accessing the internet:

```sh
python scripts/update_citations.py --offline
```

## Matching and failures

Existing mappings use verified OpenAlex work IDs. New papers with supported scholarly URLs are discovered from the README, then matched by exact normalized title; alternate titles can be added to their `aliases` in `data/citations.json`. Custom paper URLs can be registered there with a title, URL, aliases, and an optional OpenAlex work ID.

Unmatched papers show **Citations: unavailable**, not zero. The updater retries transient errors and rate limits, retains previous counts and their original timestamps when a record is missing or invalid, and fails without changing either file if no valid counts could be refreshed. Partial refreshes retain older per-paper timestamps; the header reports the latest successful check, not a guarantee that every paper was updated.

Edit paper titles, links, and venue labels normally. Citation text between `<!-- citations:start -->` and `<!-- citations:end -->`, and the citation summary block, are generated. Daily updates touch those generated portions and the citation snapshot.
