# Documentation Gaps - Bilinear-Form Lattice Methods

Real work needed.

## Goal 1 maintenance checks (2026-02-18 pass)

- [x] Cursory in-scope package-gap scan: no clear new bilinear-form lattice package surface requiring a new checklist was identified in this pass.

## Goal 2 contract-fidelity items (2026-02-18 pass)

- [x] Tighten `TorQuadModule.submodules` and `TorQuadModule.stable_submodules` signatures in Julia umbrella reference, Hecke mirror reference, and checklist — replaced `...` placeholders with source-backed typed signatures from upstream Hecke `TorQuadModule` discriminant-group docs.
- [x] Reconcile `torsion_quadratic_module_with_isometry` constructor type union in Julia umbrella reference, Hecke mirror reference, and checklist — added `AutomorphismGroupElem{TorQuadModule}` to the documented type union `U` for the `f` parameter, per OSCAR stable upstream docs.
- [x] Add optional-parameter fidelity (`[f]` notation) to both `torsion_quadratic_module_with_isometry` constructor rows across all three surfaces.

## Missing Local Doc Copies

These packages need local copies of actual upstream docs:

- [ ] flint - add local doc copies
- [ ] fplll - add local doc copies
- [ ] gap - add local doc copies
- [ ] ntl - add local doc copies
