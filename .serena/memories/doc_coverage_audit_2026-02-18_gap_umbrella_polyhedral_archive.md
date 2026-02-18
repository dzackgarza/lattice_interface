# Doc Coverage Audit Handoff (2026-02-18): GAP umbrella polyhedral scope archive

## Completed work
- Performed a cursory Goal-1 package-surface maintenance check during this pass; no clear new in-scope bilinear-form lattice package checklist gap identified.
- Archived out-of-scope GAP umbrella sections from active scope while preserving content in dedicated archive files:
  - New: `docs/archive/scope_violations/gap_methods_checklist_polyhedral_sections_2026-02-18.md`
  - New: `docs/archive/scope_violations/gap/lattice/gap_lattice_methods_reference_polyhedral_sections_2026-02-18.md`
- Updated active GAP umbrella checklist/reference to remove in-scope-surface exposure for:
  - `NormalizInterface`,
  - `toric`,
  - `NConvex`,
  - polyhedral `CddInterface` families.
- Left `4ti2Interface` active in GAP umbrella surfaces for now (separate broader scope-migration queue still open).
- Updated `docs/TODO.md`:
  - added checked Goal-1 cursory-maintenance line for this pass,
  - checked off the mixed-file archive item for GAP umbrella sections.

## Files changed
- `docs/gap_methods_checklist.md`
- `docs/gap/lattice/gap_lattice_methods_reference.md`
- `docs/archive/scope_violations/gap_methods_checklist_polyhedral_sections_2026-02-18.md` (new)
- `docs/archive/scope_violations/gap/lattice/gap_lattice_methods_reference_polyhedral_sections_2026-02-18.md` (new)
- `docs/TODO.md`

## Commit
- `88a02bb` — docs: archive out-of-scope GAP umbrella polyhedral sections

## Remaining high-impact follow-ups
1. Continue `Move polyhedral/LP-centered package docs identified as out of scope` in `docs/TODO.md` (includes `docs/4ti2_methods_checklist.md`, `docs/normaliz_methods_checklist.md`, `docs/toric_methods_checklist.md`, `docs/nconvex_methods_checklist.md`, etc.).
2. Archive toric/polyhedral sections from Sage umbrella docs (`docs/sage_methods_checklist.md`, `docs/sage/lattice/sagemath_lattice_reference.md`).
3. Complete cross-reference reconciliation in playbook/index surfaces so archive links are consistently used.