# Doc Coverage Audit Handoff (2026-02-18): TorQuadModule submodule signatures and TorQuadModuleWithIsom constructor type union

## Objectives covered
- FIRST GOAL (cursory package-surface maintenance): brief in-scope package-gap scan found no clear new bilinear-form lattice package surface requiring a new checklist.
- SECOND GOAL (active phase focus): two targeted contract-fidelity improvements:
  1. Replaced `submodules(T; ...)` and `stable_submodules(T, act; ...)` `...` placeholders with source-backed typed signatures from upstream Hecke `TorQuadModule` discriminant-group docs.
  2. Reconciled `torsion_quadratic_module_with_isometry` constructor type union to include `AutomorphismGroupElem{TorQuadModule}` per OSCAR stable upstream docs; added optional-parameter fidelity (`[f]` notation) to both constructor overloads.
- TODO queue integration: added and checked off Goal 1 and Goal 2 items in `docs/TODO.md`.

## Completed edits

### 1. `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
- §2.11 (TorQuadModule): replaced `submodules(T; ...)` and `stable_submodules(T, act; ...)` with typed signatures:
  - `submodules(T::TorQuadModule; order::Int, index::Int, subtype::Vector{Int}, quotype::Vector{Int})`
  - `stable_submodules(T::TorQuadModule, act::Vector{TorQuadModuleMap}; quotype::Vector{Int})`
- §2.18 (TorQuadModuleWithIsom):
  - Replaced `torsion_quadratic_module_with_isometry(T, f; check=true)` with `torsion_quadratic_module_with_isometry(T::TorQuadModule, [f::U]; check::Bool=true)` documenting `U` as `AutomorphismGroupElem{TorQuadModule}`, `TorQuadModuleMap`, `FinGenAbGroupHom`, `ZZMatrix`, or `MatGroupElem{QQFieldElem, QQMatrix}`.
  - Replaced `torsion_quadratic_module_with_isometry(q::QQMatrix, f::ZZMatrix; check=true)` with optional-parameter form.
- Updated source note to reference Pass-24 addendum.

### 2. `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md`
- §2.10 (TorQuadModule): added typed `submodules` and `stable_submodules` rows.
- §2.13 (TorQuadModuleWithIsom): updated both constructor rows with type union and optional-parameter fidelity.
- Updated source note to reference Pass-24 addendum.

### 3. `docs/julia_methods_checklist.md`
- §2.11: updated `submodules(T; ...)` and `stable_submodules(T, act; ...)` lines with typed signatures and caveats.
- §2.18: updated both `torsion_quadratic_module_with_isometry` constructor lines with type union (including `AutomorphismGroupElem`) and optional-parameter notation.

### 4. `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- Added Pass-24 addendum documenting upstream evidence URLs and local alignment actions.

### 5. `docs/TODO.md`
- Added and checked off Goal 1 maintenance re-run entry.
- Added and checked off Goal 2 contract-fidelity entries for `submodules`/`stable_submodules` and constructor type union.

## Upstream evidence used in this pass
- `https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/discriminant_group/` — `TorQuadModule` submodule/stable_submodules typed signatures.
- `https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/torquadmodwithisom/` — `torsion_quadratic_module_with_isometry` constructor type union with `AutomorphismGroupElem`.

## Commit
- `6274e07` — docs: tighten TorQuadModule submodule signatures and constructor type union

## Validation
- Documentation-only pass; no runtime tests executed in this environment.
- Targeted grep/diff checks confirmed replacements on all three touched surfaces before commit.

## Intentional non-edits
- Left unrelated pre-existing dirty files untouched:
  - `README.md`
  - untracked `.serena/`, `agents/`, `tmp/`

## Remaining high-impact gaps
1. Continue Goal 2 contract-fidelity: many Julia checklist rows in §2.3–§2.9 remain unchecked (`[ ]`) for basic ZZLat construction, intrinsic data, and reduction methods. These lack method-tagged test coverage.
2. The `stable_submodules` checklist test link in §2.11 points to `test_31_stable_submodules` which covers the `TorQuadModule` (non-isometry) surface; consider whether the isometry-equipped surface (`TorQuadModuleWithIsom.submodules`) also needs a distinct tagged test.
3. Outstanding TODO items for local doc copies of `flint`, `fplll`, `gap`, `ntl` packages.
4. Scope-migration archive backlog for out-of-scope polyhedral/toric surfaces (low priority after in-scope contract-fidelity work).
