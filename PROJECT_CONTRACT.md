# Product Contract: Grounded Knowledge Workbench

**State:** `contract_ready`

## User and problem

The initial user is an applied-AI engineer preparing for governed enterprise
knowledge-work environments. They need one reproducible project that demonstrates
local document ingestion, grounded retrieval, agent workflows, access control,
human review, evaluation, and knowledge transfer without using confidential
material.

## Measurable outcome

The portfolio release must, on a clean supported environment:

1. ingest a synthetic technical corpus across supported formats;
2. answer a fixed evaluation set with source citations;
3. prevent every defined cross-role retrieval leak;
4. generate one structured, reviewable technical report;
5. pause at a human approval checkpoint before finalization;
6. export a local, inspectable knowledge graph;
7. reproduce the workflow from an executable notebook and documented command;
8. publish an evaluation report containing limitations and failure cases.

Initial release targets will be frozen with the evaluation dataset. Proposed
targets are at least 90% citation coverage, zero known role-policy leaks, and a
fully passing deterministic test suite.

## Input and output

### Inputs

- Synthetic technical documents in explicitly supported test formats.
- A document manifest containing provenance and role metadata.
- A fixed set of questions and expected evidence.
- Human approval or correction at defined gates.

### Outputs

- Cited answers and retrieval traces.
- A portable Markdown knowledge bundle.
- An inspectable local graph export.
- A reviewed technical report.
- Deterministic and model-based evaluation results.
- An executable demonstration notebook and training material.

## Deterministic versus model-owned behavior

Deterministic code owns path safety, manifest validation, role filtering,
provenance, workflow states, approval gates, exact checks, and evidence
serialization. Models may own synthesis, drafting, critique, classification,
and semantic judging, but their outputs never override deterministic policy.

## Data and privacy boundary

Only synthetic or explicitly public inputs are permitted in Git. Private data,
credentials, raw personal traces, employer documents, client requirements, and
copied private specifications are prohibited. Cloud-model adapters, if added, must be
optional and disabled for private data by default.

## Non-goals

- Production authorization or identity management.
- Certification for classified or defense environments.
- Recreating a specific company's internal architecture or dataset.
- Supporting every document format in the first vertical slice.
- Autonomous publication, deployment, or consequential external actions.
- Claiming enterprise readiness before production-grade evidence exists.

## Acceptance scenarios

1. A `reader` can retrieve public operational guidance but cannot retrieve
   engineering-only or reviewer-only content.
2. An `engineer` can retrieve public and engineering content but not the review
   register.
3. A `reviewer` can retrieve all three synthetic document classes.
4. Invalid, missing, absolute, or traversal document paths fail closed.
5. A grounded answer contains resolvable citations to allowed sources.
6. A report cannot reach `approved` without a recorded human decision.
7. The evaluation command produces repeatable machine-readable results.

## Deployment and rollback

The first release is local-only. All generated model artifacts remain outside
Git until sanitized. A later preview must be isolated, use synthetic data, and
have a documented disable/rollback path. Git history is the code rollback
mechanism; corpus and index rebuilds must be deterministic.

## Moat and post-model-vendor value

The durable value is the governed workflow: portable knowledge representation,
explicit evidence, deterministic access boundaries, human approval, evaluation
datasets, and reproducible local execution. The project must remain useful when
individual models or chat interfaces become interchangeable.
