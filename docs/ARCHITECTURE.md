# Architecture

## Design objective

Provide one local-first workflow that turns an allowed synthetic corpus into
grounded answers, a reviewable knowledge graph, and approved documentation with
measurable evidence.

## Target flow

```text
synthetic documents
        |
        v
manifest + parsers ----> deterministic role/provenance policy
        |                              |
        v                              v
portable knowledge bundle ----> allowed retrieval context
        |                              |
        v                              v
local model adapter -----------> cited draft
                                       |
                          researcher -> writer -> reviewer
                                       |
                              human approval gate
                                       |
                     report + graph + evaluation evidence
```

## Component boundaries

1. **Corpus and manifest** — source identity, format, provenance, roles, and
   public-safety classification.
2. **Policy core** — deterministic path validation, role filtering, workflow
   states, and approval records.
3. **Knowledge compiler** — parsed chunks, portable Markdown pages,
   indexes, links, and graph export.
4. **Retrieval** — role-filtered search that returns evidence identifiers before
   any model sees context.
5. **Model adapters** — optional pluggable local or remote inference interface;
   no policy ownership.
6. **Agent workflow** — bounded researcher, writer, and reviewer roles with
   explicit stopping conditions.
7. **Artifact generation** — cited answer, technical report, notebook, and
   training material.
8. **Evaluation** — deterministic correctness and access tests plus separately
   reported semantic judging, latency, and resource use.

## First vertical slice

The first functional slice will ingest a small synthetic text corpus,
filter retrieval by role, answer a fixed question with resolvable citations,
and serialize an evaluation record. Additional formats, model runtimes, and
user interfaces follow only after this slice passes.

## Failure policy

- Unknown roles are rejected.
- Unsafe or missing document paths stop manifest loading.
- Missing provenance prevents ingestion.
- An empty allowed evidence set produces an explicit refusal, not a model call.
- Model output without resolvable evidence cannot be approved.
- No report reaches an approved state without a human decision record.

## Revisit points

- Choose the local inference runtime after checking available development
  hardware.
- Select one primary knowledge compiler only after a thin comparative spike.
- Add container isolation only when a concrete reproduction requirement calls
  for it.
- Freeze evaluation targets after the synthetic corpus and questions exist.
