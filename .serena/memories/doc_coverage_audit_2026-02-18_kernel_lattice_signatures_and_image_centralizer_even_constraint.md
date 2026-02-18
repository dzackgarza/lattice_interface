# Doc Coverage Audit Handoff (2026-02-18): kernel_lattice typed signatures and image_centralizer_in_Oq even-lattice precondition

## Objectives covered
- FIRST GOAL (cursory package-surface maintenance): previous pass confirmed no new in-scope bilinear-form lattice packages; this pass focused entirely on Goal 2.
- SECOND GOAL (active phase focus): two targeted contract-fidelity improvements derived from reading the local snapshot `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom.md`:
  1. Replaced bare `kernel_lattice(Lf, p)` and `kernel_lattice(Lf, l)` placeholder entries with typed dispatch signatures and explicit primitivity caveats.
  2. Added the missing even-lattice precondition to `image_centralizer_in_Oq` and a differentiation caveat for `image_in_Oq`.

## Completed edits

### 1. `docs/julia_methods_checklist.md` (§2.14 Kernel sublattices)
- Replaced `kernel_lattice(Lf, p)` with `kernel_lattice(Lf::ZZLatWithIsom, p::Union{ZZPolyRingElem, QQPolyRingElem})` plus primitivity caveat.
- Replaced `kernel_lattice(Lf, l)` with `kernel_lattice(Lf::ZZLatWithIsom, l::Integer)` plus primitivity caveat.

### 2. `docs/julia_methods_checklist.md` (§2.14 Discriminant groups)
- Added even-lattice caveat to `image_centralizer_in_Oq` entry.
- Added differentiation caveat to `image_in_Oq` entry (distinct from `image_centralizer_in_Oq`; works for definite and indefinite).

### 3. `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (§2.14 Kernel sublattices)
- Updated `kernel_lattice` rows to typed dispatch signatures with primitivity descriptions.

### 4. `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (§2.14 Discriminant groups)
- Updated `image_centralizer_in_Oq` row to include: even-lattice restriction for Miranda-Morrison general case, with explicit bypass conditions (definite, ±identity, Euler-totient-rank).
- Updated `image_in_Oq` row to note it is the general π-image computation and distinct from `image_centralizer_in_Oq`.

### 5. `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md` (§2.11)
- Split `kernel_lattice(Lf, ...)` row into two typed overloads with primitivity notes.
- Expanded `discriminant_group(Lf)` row to include `image_centralizer_in_Oq` even-lattice restriction.

### 6. `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- Added Pass-25 addendum documenting source (local snapshot) and alignment actions for `kernel_lattice` and `image_centralizer_in_Oq`.

### 7. `docs/TODO.md`
- Checked off two new Goal 2 contract-fidelity items.

## Upstream evidence used in this pass
- Local snapshot: `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom.md`
  - Typed dispatch: `kernel_lattice(::ZZLatWithIsom, ::Union{ZZPolyRingElem, QQPolyRingElem})` and `kernel_lattice(::ZZLatWithIsom, ::Integer)`.
  - Even-lattice restriction text: "Important note: hermitian Miranda-Morrison is only available for even lattices."

## Remaining high-impact gaps
1. §2.4 Intrinsic data: all entries unchecked (`gram_matrix(L)`, `basis_matrix(L)`, `rank(L)`, `degree(L)`, etc.) — no method-tagged tests yet.
2. §2.3 Construction: `integer_lattice(; gram=G)`, `integer_lattice(B; gram=G)`, `lattice(V, B)`, `root_lattice`, `hyperbolic_plane_lattice`, `rescale` — unchecked.
3. §2.8 Automorphism: `automorphism_group_generators`, `automorphism_group_order`, `is_isometric`, `is_isometric_with_isometry`, `is_rationally_isometric`, `hasse_invariant`, `witt_invariant` — all unchecked.
4. §2.14 Construction/accessor/attribute/operations blocks: almost entirely unchecked.
5. Missing local doc copies for flint, gap, ntl, fpylll, forms, g6k, hypercells, crystallographic_stack, flatter, pari_gp.

## Commits
- `a2b2386` — docs: tighten kernel_lattice typed signatures and add image_centralizer_in_Oq even-lattice precondition
- `1f47209` — docs: add typed signatures and tuple return shapes for TorQuadModuleWithIsom submodule/aut-group methods

## Additional Pass-26 work (TorQuadModuleWithIsom return types)
Upstream fetch of OSCAR stable `torquadmodwithisom` confirmed tuple return shapes previously absent:
- `sub` / `primary_part` / `orthogonal_submodule` all return `(TorQuadModuleWithIsom, TorQuadModuleMap)`
- `automorphism_group_with_inclusion` returns `(AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism)`
- `automorphism_group` typed as `TorQuadModuleWithMap` (known typesetting inconsistency)
- `is_isomorphic_with_map` / `is_anti_isomorphic_with_map` argument types confirmed
Applied to checklist (§2.18), Julia umbrella reference (§2.18), Hecke mirror reference (§2.13), provenance note.

## Additional Pass-27 work (ZZLatWithIsom return types and vector-enumeration fixes)
Upstream fetch of OSCAR stable `latwithisom` and `integer_lattices` pages confirmed:
- `discriminant_group(Lf)` returns `(TorQuadModule, AutomorphismGroupElem)` — not just a module
- `discriminant_group(::Type{TorQuadModuleWithIsom}, Lf; ...)` — type argument form is `::Type{...}`
- `image_centralizer_in_Oq` returns `(AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism)`
- `invariant_coinvariant_pair(Lf)` returns `(ZZLatWithIsom, ZZLatWithIsom)`
- `rational_span(Lf)` returns `QuadSpaceWithIsom` (not plain `QuadSpace`)
- `discriminant_representation` has `full::Bool=true` and `check::Bool=true` kwargs (undocumented before)
- `lll(L::ZZLat)` has `redo::Bool=false` and `ctx::LLLContext` kwargs (undocumented before)
- `close_vectors` check defaults to `false` (was incorrectly shown as `true`)
- `rational_spinor_norm(Lf; b::Int=-1)` — b=-1 is the default
- `signatures(Lf)` constrained to hermitian-type with irreducible cyclotomic minimal polynomial
Applied to checklist (§2.5, §2.14), Julia umbrella reference (§2.5, §2.14), Hecke mirror (§2.5, §2.11), provenance note.
Commit: `647f48f`

## Validation
- Documentation-only pass; no runtime tests executed.
- All edits sourced from local snapshots or upstream page fetches; no speculative assertions.
