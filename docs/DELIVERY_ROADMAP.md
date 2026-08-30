# Delivery roadmap

The roadmap is organized by evidence gates rather than calendar promises. A
stage is complete only when its implementation, deterministic checks, and
limitations are visible in the repository.

## Stage 1 — Deterministic foundation

- Reproducible Python environment and dependency lock.
- Packaged synthetic corpus and validated manifest.
- Fail-closed path and role policy.
- Command-line evidence surface.

**Gate:** a clean environment passes the policy tests and returns only sources
allowed for the requested role.

## Stage 2 — Grounded knowledge layer

- Parsing for the first supported document formats.
- Provenance-aware retrieval.
- Portable Markdown knowledge bundle.
- Inspectable local graph export.

**Gate:** fixed questions return the expected allowed evidence with resolvable
citations.

## Stage 3 — Reviewed document workflow

- Bounded research, drafting, and review roles.
- Human approval checkpoint.
- Structured technical-report generation.
- Explicit stopping and refusal conditions.

**Gate:** the workflow pauses for review, records the human decision, and
rejects model output without valid evidence.

## Stage 4 — Evaluation and operator transfer

- Fixed evaluation set and access-leak tests.
- Quality, citation, latency, and limitation reporting.
- Executable notebook.
- Reproducible operator walkthrough.

**Gate:** a fresh operator can reproduce the demonstration and distinguish
implemented, experimental, and planned capabilities.
