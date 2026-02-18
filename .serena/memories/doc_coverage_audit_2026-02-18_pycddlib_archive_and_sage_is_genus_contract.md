# Doc Coverage Audit Handoff (2026-02-18): pycddlib archive move + Sage `is_genus` contract wording

## Objective coverage
- FIRST GOAL (cursory missing-package check): brief maintenance check over current package checklist inventory + prior handoff memories found no clear missing in-scope bilinear-form lattice package surface requiring a new checklist in this pass.
- SECOND GOAL (contract fidelity): tightened an in-scope Sage method caveat to be source-exact about odd-lattice support status for `TorsionQuadraticModule.is_genus(..., even=True)`.
- TODO queue execution: completed and checked off `Move pycddlib docs (explicit example scope violation)`.

## Changes made
1. Archived pycddlib scope-violation surface
- Moved:
  - `docs/pycddlib_methods_checklist.md` -> `docs/archive/scope_violations/pycddlib_methods_checklist.md`
  - `docs/pycddlib/lattice/pycddlib_lattice_reference.md` -> `docs/archive/scope_violations/pycddlib/lattice/pycddlib_lattice_reference.md`
  - `docs/pycddlib/upstream/pycddlib_online_provenance_2026-02-17.md` -> `docs/archive/scope_violations/pycddlib/upstream/pycddlib_online_provenance_2026-02-17.md`
- Updated archived checklist/reference headers and internal path references to the new archive locations.

2. Updated TODO queue
- `docs/TODO.md`:
  - marked pycddlib move item as completed (`[x]`),
  - recorded old -> archive paths in-place.

3. In-scope contract wording refinement (Sage)
- `docs/sage_methods_checklist.md`:
  - replaced raw TODO quote with explicit caveat: upstream docs include odd-lattice TODO; `even=False` is not fully documented/complete.
- `docs/sage/torsion_quadratic_module/sage_torsion_quadratic_module_reference.md`:
  - aligned `T.is_genus(signature_pair, even=True)` description with upstream status (odd-lattice path not documented complete).

## Source evidence used
- Local upstream snapshot:
  - `docs/sage/torsion_quadratic_module/upstream/torsion_quadratic_module.html`
  - `TorsionQuadraticModule.is_genus` section contains explicit TODO text: "implement the same for odd lattices".

## Commit
- `e472aef` — docs: archive pycddlib surface and tighten Sage genus caveat

## Repository hygiene notes
- Preserved unrelated pre-existing dirty/untracked state and did not stage/revert it:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - `.serena/`, `scripts/__pycache__/`

## Remaining high-impact queue items
1. Continue scope archive migration for cdd-family/polyhedral stacks still listed in `docs/TODO.md` (`cddlib`, `CddInterface`, and broader polyhedral LP stacks).
2. Reconcile cross-links after further archive moves (playbook references, GAP umbrella references/checklists).
3. Continue Goal-2 fidelity passes on in-scope surfaces where caveats/assumptions can be made more source-exact.