# Repository Working Agreement

## Objective

Build a public-safe, local-first knowledge engineering workbench that turns a
synthetic technical corpus into grounded answers and reviewable documentation.
The project is an independently specified portfolio demonstration, not a copy
of any private or third-party specification.

## Authority order

1. The user's current request.
2. `PROJECT_CONTRACT.md`.
3. `docs/ARCHITECTURE.md` and accepted ADRs.
4. The nearest implementation tests.

## Hard boundaries

- Never add employer, client, defense, mailbox, transcript, contract, or
  internal-project material to this repository.
- Use only synthetic or explicitly public source data.
- Do not copy distinctive wording, exact version matrices, or acceptance
  criteria from private or third-party specifications.
- Keep model-backed behavior separate from deterministic policy, validation,
  provenance, and evaluation logic.
- Do not claim a feature is implemented because it appears in a roadmap.
- Do not change the repository's remote or GitHub visibility without Navid's
  explicit approval.

## Engineering loop

`contract -> smallest vertical slice -> deterministic checks -> model adapter -> evaluation -> repair -> evidence`

## Current verification

```bash
uv run python -m unittest discover -s tests -v
uv run gkw status --json
uv run gkw access --role reader --json
```

## Implementation conventions

- Python 3.11 or newer.
- Prefer the standard library until an external dependency has a concrete job.
- Pin runtime dependencies with `uv` when they are introduced.
- Fail closed on invalid paths, unknown roles, missing provenance, and access
  policy ambiguity.
- Every model-owned result must retain evidence links and evaluation metadata.
