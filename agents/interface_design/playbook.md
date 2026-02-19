# Interface Design Playbook

## Scope

Applies when assignment work defines or changes interface contracts, type surfaces, and behavioral guarantees.

## Core Rule (Non-Negotiable)

- Never prioritize backward compatibility during interface-definition work.
- If interface is still being defined, backward compatibility is not a valid constraint.
- Prioritize mathematical correctness, coherent type ontology, and clear contracts first.
- Remove or rename incorrect interface types immediately rather than preserving legacy names.

## Design Expectations

- Contracts are explicit, mathematically correct, and testable.
- Types and method signatures are coherent and non-contradictory.
- Assumptions/constraints are explicit (domain, definiteness, ring assumptions, etc.).
- Interface docs and tests remain aligned with real behavior.

## Handoff

- Record design decisions and remaining contract gaps in Serena continuity memories.
- Commit assignment-owned interface changes.
