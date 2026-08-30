# Grounded Knowledge Workbench

[![CI](https://github.com/NavidBroumandfar/grounded-knowledge-workbench/actions/workflows/ci.yml/badge.svg)](https://github.com/NavidBroumandfar/grounded-knowledge-workbench/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-2ea44f.svg)](LICENSE)

A public-safe, local-first foundation for governed knowledge workflows.

## Current state

`contract_ready` — the clean-room contract, architecture, simulated delivery
plan, repository boundary, and first deterministic access-control slice exist.
Retrieval, model-backed synthesis, graph, multi-agent, document-generation, and
notebook features are planned but are **not yet implemented**.

## Capability status

| Capability | Status |
|---|---|
| Python 3.11 environment managed with `uv` | Validated |
| Synthetic corpus manifest and required provenance metadata | Validated |
| Fail-closed path validation and role filtering | Validated |
| Grounded retrieval and cited answers | Planned |
| Local model adapter and bounded agent workflow | Planned |
| Knowledge bundle, graph export, and report generation | Planned |
| Evaluation suite, executable notebook, and training package | Planned |

## Validated foundation

The initial slice validates a synthetic corpus manifest and demonstrates
fail-closed role filtering without any model dependency. From a clean clone:

```bash
uv sync --locked
uv run python -m unittest discover -s tests -v
uv run gkw status --json
uv run gkw access --role engineer --json
```

The access command returns only the synthetic documents authorized for the
requested role. Unknown roles and unsafe document paths fail closed.

## Delivery model

The repository follows a gated delivery roadmap that keeps deterministic
boundaries ahead of model-backed features. See [the delivery roadmap](docs/DELIVERY_ROADMAP.md).

## Clean-room boundary

This repository is independently specified. It contains no employer, client,
defense, internal-project, call, email, transcript, or controlled-distribution
material. All demonstrations use synthetic data.

## Repository layout

```text
docs/adr/                        architecture decisions
docs/training/                   future knowledge-transfer material
notebooks/                       future executable walkthrough
src/grounded_knowledge_workbench deterministic core, packaged synthetic corpus, and future adapters
tests/                           contract and policy tests
```

## Project documentation

- [Product contract](PROJECT_CONTRACT.md) — boundaries, outcomes, and acceptance scenarios.
- [Architecture](docs/ARCHITECTURE.md) — target flow, components, and failure policy.
- [Delivery roadmap](docs/DELIVERY_ROADMAP.md) — implementation stages and evidence gates.
- [Release evidence](docs/RELEASE_EVIDENCE.md) — verified commands, public-safety checks, and current limitations.

Contributions must preserve the clean-room data boundary described in
[CONTRIBUTING.md](CONTRIBUTING.md). Security and sensitive-data concerns should
be reported through the process in [SECURITY.md](SECURITY.md).
