# Release evidence

## Public foundation

**Maturity:** `contract_ready`

The public foundation contains a synthetic Markdown corpus, a validated
manifest, fail-closed path handling, deterministic role filtering, a command
line evidence surface, and focused unit tests.

## Release verification

The public baseline commit `fb000e7` passed the first GitHub Actions run on
Python 3.11 and 3.13. The workflow now covers every advertised minor from 3.11
through 3.13 on each push and pull request.

Reproduce the local gate from the repository root:

```bash
uv sync --locked
git diff --check
uv run python -m unittest discover -s tests -v
uv run gkw status --json
uv run gkw access --role reader --json
uv build
gitleaks git . --no-banner
```

Continuous integration is configured to run the locked test, build, and
installed-wheel smoke path on supported Python versions. The workflow uses
read-only repository permissions and commit-pinned GitHub Actions.

## Publication gate

Every public change is checked for:

- private or credential-bearing files;
- employer, client, call, email, transcript, and private-specification material;
- common secret and private-key patterns;
- generated environments, build outputs, and caches.

All committed demonstration content remains synthetic. The authoritative CI
results are available from the repository's
[Actions history](https://github.com/NavidBroumandfar/grounded-knowledge-workbench/actions/workflows/ci.yml).

## Current limitations

- There is no retrieval or model adapter yet.
- No cited-answer, report-generation, graph-export, or agent workflow exists.
- The notebook and knowledge-transfer package are placeholders only.
- Role filtering is a deterministic portfolio demonstration, not a production
  authorization system.
- Evaluation currently covers the manifest and access boundary only.

These limitations are intentional and remain visible until each capability has
implementation and verification evidence.
