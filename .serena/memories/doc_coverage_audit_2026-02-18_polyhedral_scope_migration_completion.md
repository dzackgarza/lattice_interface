# Doc Coverage Audit Handoff (2026-02-18): polyhedral scope-migration completion pass

## Completed work
- Performed mandatory Goal-1 cursory in-scope package-surface maintenance check while running this migration pass.
- Result: no clear new in-scope (bilinear-form lattice) package checklist gap identified.
- Archived remaining out-of-scope package surfaces by preserving full historical content under `docs/archive/scope_violations/` and converting active-path files into redirect stubs for:
  - `4ti2`
  - `latte_integrale`
  - `normaliz`
  - `lrslib`
  - `polymake`
  - `topcom`
  - `palp`
  - `toric`
  - `nconvex`
- Updated GAP umbrella active docs to remove residual active `4ti2Interface` method exposure and point all polyhedral/toric package families to archive content:
  - `docs/gap_methods_checklist.md`
  - `docs/gap/lattice/gap_lattice_methods_reference.md`
- Extended existing GAP archive files to include `4ti2Interface` sections and corrected archived NConvex cross-links to archive paths:
  - `docs/archive/scope_violations/gap_methods_checklist_polyhedral_sections_2026-02-18.md`
  - `docs/archive/scope_violations/gap/lattice/gap_lattice_methods_reference_polyhedral_sections_2026-02-18.md`
- Updated `docs/TODO.md` checkboxes for completed scope-migration steps in this run.

## Validation performed
- Stub-target existence check across all moved package surfaces: OK.
- Archive self-link normalization check (`docs/<pkg>/...` -> `docs/archive/scope_violations/<pkg>/...`) for moved package docs: OK.
- Active GAP umbrella docs no longer contain active 4ti2 method inventory; only archive pointers remain.

## Intentional non-edits
- Did not modify pre-existing dirty files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/` and `scripts/__pycache__/`

## Remaining gaps
1. `docs/documentation_coverage_audit_playbook.md` still references some out-of-scope checklist paths in active references/upstream map sections; this item remains open in `docs/TODO.md` (`Replace active-scope links with archive links...`).
2. `docs/TODO.md` validation item `Confirm cron prompt/playbook package targeting no longer includes out-of-scope stacks` remains open; scheduler/prompt contain no explicit package loop, but playbook references still need reconciliation.

## Commit
- `bb7d959` — docs: archive remaining out-of-scope package surfaces