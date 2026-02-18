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

- [x] Fix `IntegralLattice.orthogonal_group` definiteness constraint: tag was `[PD]` (positive definite only) but upstream docs confirm negative definite lattices also work; only indefinite lattices raise `NotImplementedError` — corrected to `[DEFINITE]` across `sage_integral_lattice_reference.md` (method table + definiteness summary) and `sagemath_lattice_reference.md` (method table + two pitfalls entries). Sourced from local upstream snapshot `free_quadratic_module_integer_symmetric.html`.

- [x] Fix `automorphism_group_generators` and `automorphism_group_order` definiteness constraint: tags were `[PD]` (positive definite only) but upstream OSCAR/Hecke docs explicitly state "Given a definite lattice `L`" — negative definite lattices are also supported; only indefinite lattices are excluded; corrected to `[DEFINITE]` across `julia_lattice_methods_reference.md`, `nemo_hecke_lattice_reference.md`, and `julia_methods_checklist.md`; also added `ambient_representation::Bool=true` kwarg to `automorphism_group_generators` signature. Sourced from `https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/integer_lattices/`.

## Goal 2 contract-fidelity verification (2026-02-18 follow-up)

- [x] Verified `torquadmodwithisom.md` local snapshot already has `submodules(::TorQuadModuleWithIsom; quotype::Vector{Int}=Int[])` keyword contract — Julia references and checklist are consistent with local snapshot.

## Missing Local Doc Copies

These packages have partial or need complete local copies of upstream docs:

- [ ] flint (has .rst files under upstream/, needs integration check)
- [ ] gap (core GAP docs)
- [x] Replace `NormalFormIntMat(...)` and `Decomposition(...)` placeholder signatures in GAP core reference and checklist with source-backed typed signatures — `NormalFormIntMat(mat, options)` with full bitmask contract and record-return shape; `Decomposition(A, B, depth)` with cyclotomic-matrix rank constraint and `"nonnegative"` depth variant — sourced from local upstream `docs/gap/upstream/matint.gd` §NormalFormIntMat and `docs/gap/upstream/chap25.html` §25.4-1.

- [ ] ntl (has .txt/.cpp.html files under upstream/, needs integration check)
- [ ] fpylll (partial docs)
- [ ] forms (partial docs)
- [ ] g6k (partial docs)
- [ ] crystallographic_stack (partial docs)
- [ ] pari_gp (partial docs)

Already addressed:
- [x] hypercells (has full chapter snapshots under upstream/)
- [x] flatter (has README and example profiles under upstream/)
