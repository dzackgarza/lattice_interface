# Documentation Gaps - Bilinear-Form Lattice Methods

This file tracks missing prerequisites for building the per-package method checklists correctly.
The checklists themselves track per-method completion; this file tracks what must exist *before* checklist entries can be filled out with source-backed accuracy (primarily: local copies of upstream docs).

Real work needed.

## Goal 1 maintenance checks (2026-02-18 pass)

- [x] Cursory in-scope package-gap scan: no clear new bilinear-form lattice package surface requiring a new checklist was identified in this pass.

## Goal 2 contract-fidelity items (2026-02-18 pass)

- [x] Tighten `TorQuadModule.submodules` and `TorQuadModule.stable_submodules` signatures in Julia umbrella reference, Hecke mirror reference, and checklist — replaced `...` placeholders with source-backed typed signatures from upstream Hecke `TorQuadModule` discriminant-group docs.
- [x] Reconcile `torsion_quadratic_module_with_isometry` constructor type union in Julia umbrella reference, Hecke mirror reference, and checklist — added `AutomorphismGroupElem{TorQuadModule}` to the documented type union `U` for the `f` parameter, per OSCAR stable upstream docs.
- [x] Add optional-parameter fidelity (`[f]` notation) to both `torsion_quadratic_module_with_isometry` constructor rows across all three surfaces.
- [x] Tighten `kernel_lattice(::ZZLatWithIsom, ...)` typed dispatch signatures (polynomial and integer overloads) and add primitivity caveats across checklist, Julia umbrella reference, and Hecke mirror reference — sourced from local snapshot `latwithisom.md`.
- [x] Add missing even-lattice precondition to `image_centralizer_in_Oq` (hermitian Miranda-Morrison only available for even lattices) and differentiation caveat for `image_in_Oq` — sourced from local snapshot `latwithisom.md`.
- [x] Add typed signatures and tuple return shapes for `TorQuadModuleWithIsom` submodule/aut-group methods (`sub`, `primary_part`, `orthogonal_submodule` return `(TorQuadModuleWithIsom, TorQuadModuleMap)`; `automorphism_group_with_inclusion` returns `(AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism)`) — sourced from OSCAR stable upstream `torquadmodwithisom` page (2026-02-18).
- [x] Fix `discriminant_group(Lf)` return type to `(TorQuadModule, AutomorphismGroupElem)` and `::Type{TorQuadModuleWithIsom}` type-argument form; add `discriminant_representation` keyword args (`full`, `check`); add `invariant_coinvariant_pair(Lf)` tuple return `(ZZLatWithIsom, ZZLatWithIsom)`; add `signatures(Lf)` cyclotomic/irreducible constraint and `rational_spinor_norm` `b=-1` default; fix `close_vectors` `check` default to `false`; add `lll` `redo` and `ctx` kwargs; fix `rational_span(Lf)` return type to `QuadSpaceWithIsom` — all sourced from OSCAR stable upstream `latwithisom` and `integer_lattices` pages (2026-02-18).

## Missing Local Doc Copies

These packages need local copies of actual upstream docs (like the `.html` snapshots under `docs/sage/*/upstream/`):

- [ ] flint
- [ ] gap
- [ ] ntl
- [ ] fpylll
- [ ] forms
- [ ] g6k
- [ ] hypercells
- [ ] crystallographic_stack
- [ ] flatter
- [ ] pari_gp
