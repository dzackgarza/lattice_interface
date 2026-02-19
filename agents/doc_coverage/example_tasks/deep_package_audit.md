# Example Task: Deep Package Audit

## Goal

Pick one in-scope package at random. Read ALL upstream documentation for that package, then verify the reference doc and checklist.

## Workflow

1. **Select a package** — e.g., `flint`
2. **Read all upstream sources** — e.g., for FLINT:
   - `docs/flint/upstream/fmpz_lll.rst` — full LLL API
   - `docs/flint/upstream/fmpz_mat.rst` — full HNF/SNF API
3. **Compare against reference doc** — `docs/flint/lattice/flint_lattice_reference.md`:
   - Does every upstream method appear with full signature?
   - Are argument types and constraints documented?
   - Are domain caveats (e.g., "positive-definite only") captured?
4. **Compare against checklist** — `docs/flint_methods_checklist.md`:
   - Does every documented method have a checklist entry?
   - Are there checklist entries with no reference doc coverage?
5. **Fix gaps found** — add missing signatures, types, caveats, or checklist entries

## Critical Points

- This is the standard task pattern
- Do not skip reading upstream sources
- Do not assume reference docs are complete
- Every method must have full typed signature and constraints
- Every checklist entry must correspond to a documented method
