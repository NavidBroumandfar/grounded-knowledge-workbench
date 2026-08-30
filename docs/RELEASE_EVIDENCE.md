# Release evidence

## Public foundation

**Maturity:** `contract_ready`

The public foundation contains a synthetic Markdown corpus, a validated
manifest, fail-closed path handling, deterministic role filtering, a command
line evidence surface, and focused unit tests.

## Reproducible checks

Run from the repository root:

```bash
uv sync --locked
uv run python -m unittest discover -s tests -v
uv run gkw status --json
uv run gkw access --role reader --json
uv build
```

Continuous integration is configured to run the locked test, build, and
installed-wheel smoke path on supported Python versions. The workflow uses
read-only repository permissions and commit-pinned GitHub Actions.

## Public-safety gate

Before publication, tracked files and Git history are checked for:

- private or credential-bearing files;
- employer, client, call, email, transcript, and private-specification material;
- common secret and private-key patterns;
- generated environments, build outputs, and caches.

All committed demonstration content is synthetic.

## Current limitations

- There is no retrieval or model adapter yet.
- No cited-answer, report-generation, graph-export, or agent workflow exists.
- The notebook and knowledge-transfer package are placeholders only.
- Role filtering is a deterministic portfolio demonstration, not a production
  authorization system.
- Evaluation currently covers the manifest and access boundary only.

These limitations are intentional and remain visible until each capability has
implementation and verification evidence.
