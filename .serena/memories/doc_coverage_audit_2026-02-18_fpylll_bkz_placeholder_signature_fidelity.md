# Doc Coverage Audit Handoff (2026-02-18): fpylll BKZ placeholder-signature fidelity

## Scope and goals handled
- Assignment type: documentation-only (`docs/documentation_coverage_audit_playbook.md`).
- FIRST GOAL (maintenance check): re-ran cursory in-scope package-surface check while doing this pass; no new in-scope bilinear-form lattice package checklist gap identified.
- SECOND GOAL (contract fidelity): removed residual BKZ `...` placeholders on active fpylll surfaces and replaced with explicit source-backed signatures/contract wording.

## Changes made
- `docs/fpylll_methods_checklist.md`
  - Replaced `BKZ.reduction(B, BKZ.Param(...), ...)` with `BKZ.reduction(B, param, U=None, float_type=None, precision=0)`.
  - Replaced ellipsis BKZ.Param row with full source-backed defaults signature.
  - Added contract note that `param` is a `BKZ.Param` object.
- `docs/fpylll/lattice/fpylll_lattice_reference.md`
  - Replaced BKZ reduction placeholder signature with explicit `param` form and typed contract note.
  - Replaced `BKZ.Param(...)` row with the full defaulted signature.
- `docs/fpylll/upstream/fpylll_online_provenance_2026-02-18.md`
  - Added pass addendum documenting this signature-cleanup action and the unchanged Goal 1 maintenance result.
- `docs/TODO.md`
  - Added checked Goal 1 maintenance entry for this pass.
  - Added checked Goal 2 fidelity entry for fpylll BKZ placeholder cleanup.

## Commit
- `cee7d7d` (`docs: tighten fpylll BKZ signature contracts`)

## Validation
- Targeted grep/diff validation only (no runtime tests needed for this docs-only change).

## Remaining notable gaps
- Open TODO work remains concentrated in scope-archive migration/cross-reference reconciliation items (polyhedral/LP package moves, umbrella sweeps, link/path validation).
- Additional in-scope contract-fidelity opportunities still exist in active surfaces that retain intentional `...` placeholders where upstream docs do not expose typed dispatch signatures (notably parts of Julia/GAP helper families).