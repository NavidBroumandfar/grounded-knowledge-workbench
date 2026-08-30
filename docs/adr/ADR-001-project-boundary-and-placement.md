# ADR-001: Place Grounded Knowledge Workbench in the agent-products portfolio lane

**Status:** Accepted
**Date:** 2026-08-30
**Decider:** Navid

## Context

The project demonstrates governed enterprise knowledge-work capabilities using
an independently specified synthetic scenario. Its primary purpose is portfolio
evidence, not a shared runtime, client workspace, academic thesis, or production
product. It must remain independently versioned and public-safe.

## Decision

Create an independent Git repository in the portfolio's `agent-products` lane.
Use **Grounded Knowledge Workbench** as the product name and
`grounded-knowledge-workbench` as the repository slug. Keep the repository
local until a separate private-GitHub or public-release decision.

**Release amendment (2026-08-30):** after the clean-room boundary and initial
deterministic slice were verified, Navid authorized creation of a public GitHub
repository under the selected slug. This changes visibility, not the project's
data or evidence boundaries.

## Options considered

### Applied AI Portfolio / Agent Products

| Dimension | Assessment |
|---|---|
| Primary purpose | Exact match: portfolio evidence for an agent product |
| Isolation | Independent repository and history |
| Public safety | Governed by the portfolio contract |
| Discoverability | Clear lane and descriptive slug |

**Pros:** Matches the existing taxonomy, preserves an independent release
boundary, and makes the GitHub purpose immediately understandable.

**Cons:** The project is not treated as reusable AI infrastructure until it
earns that role through actual adoption.

### AI Systems

**Pros:** Fits some runtime and local-inference components.

**Cons:** Misstates the primary purpose; this is initially a bounded portfolio
demonstration rather than shared infrastructure.

### Applied AI Portfolio / Challenge Builds

**Pros:** Fits short, bounded implementation exercises.

**Cons:** Frames the work as disposable practice when the intended outcome is
a durable agent product and public portfolio repository.

## Naming trade-off

`ScribeLoop` was rejected because the name is already used by public GitHub
repositories and does not communicate the project function. A
pattern-specific alternative was rejected because it coupled the product
identity to one implementation approach. `Grounded Knowledge Workbench`
emphasizes evidence and remains useful if the underlying model, interface, or
knowledge format changes.

## Consequences

- The public story must focus on grounded, governed knowledge workflows.
- Private source material remains outside the repository.
- The first implementation must prove deterministic boundaries before adding
  local models or agent frameworks.

## Action items

1. Complete the deterministic manifest and role-policy foundation.
2. Implement one end-to-end cited retrieval vertical slice.
3. Add model and UI adapters only after the deterministic gate passes.
4. Preserve the public-safety and evidence review as a release gate for every
   future public change.
