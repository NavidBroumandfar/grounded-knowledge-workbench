# Contributing

Grounded Knowledge Workbench is currently an early portfolio project. Focused
issues and pull requests are welcome when they preserve its evidence and data
boundaries.

## Before opening a change

1. Use only synthetic or explicitly public source material.
2. Do not add employer, client, defense, mailbox, transcript, credential, or
   private-project content, including in fixtures and examples.
3. Keep deterministic policy, validation, provenance, and evaluation separate
   from model-generated behavior.
4. Describe implemented behavior as implemented and roadmap behavior as
   planned.
5. Add or update focused tests for policy and boundary changes.

## Local verification

```bash
uv sync --locked
uv run python -m unittest discover -s tests -v
uv run gkw status --json
uv build
```

Use a descriptive branch and keep commits narrowly scoped. For a security or
sensitive-data concern, follow [SECURITY.md](SECURITY.md) instead of opening a
public issue.
