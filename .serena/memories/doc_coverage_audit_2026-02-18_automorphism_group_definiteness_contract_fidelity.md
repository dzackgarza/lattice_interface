# Doc Coverage Audit Handoff (2026-02-18): `automorphism_group_generators` / `automorphism_group_order` definiteness constraint

## Objectives covered
- FIRST GOAL (cursory package-surface maintenance): no new in-scope bilinear-form lattice package surface gap identified.
- SECOND GOAL (active phase focus): corrected a source-backed contract-fidelity error in the OSCAR/Hecke `automorphism_group_generators` and `automorphism_group_order` definiteness constraints.

## The error
- Previous documentation tagged both `automorphism_group_generators(L)` and `automorphism_group_order(L)` as `[PD]` (positive definite only) in three separate locations.
- Upstream OSCAR/Hecke stable docs (`https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/integer_lattices/`) explicitly state "Given a **definite** lattice `L`" for both functions.
- "Definite" encompasses both positive definite AND negative definite lattices; only indefinite lattices are excluded.
- Therefore the correct constraint is `[DEFINITE]` (positive or negative definite), not `[PD]`.

## Additional improvement
- Added the previously undocumented `ambient_representation::Bool=true` keyword argument to `automorphism_group_generators`, per the upstream typed signature: `automorphism_group_generators(L::AbstractLat; ambient_representation::Bool=true, depth::Int=-1, bacher_depth::Int=0)`.
- Also added typed signatures with `depth::Int=-1` and `bacher_depth::Int=0` kwargs to `automorphism_group_order`.

## Completed edits
1. `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (§2.8)
   - Method table: `[PD, GAP]` → `[DEFINITE, GAP]` for `automorphism_group_generators`; full typed signature added.
   - Method table: `[PD]` → `[DEFINITE]` for `automorphism_group_order`; full typed signature added.
   - Bullet note updated: "PD: finite groups..." → "DEFINITE (PD or ND): both positive and negative definite lattices supported..."

2. `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md` (§2.7)
   - Method table: `[PD, GAP, NT]` → `[DEFINITE, GAP, NT]` for `automorphism_group_generators`; full typed signature added.
   - Method table: `[PD, NT]` → `[DEFINITE, NT]` for `automorphism_group_order`; full typed signature added.
   - Added "Definite note" paragraph clarifying the upstream `is_definite(L)` requirement vs `is_positive_definite(L)`.

3. `docs/julia_methods_checklist.md` (§2.8)
   - Both entries updated with typed signatures and explicit `[DEFINITE]` caveats.

4. `docs/TODO.md`
   - Added and checked off Goal 2 contract-fidelity item for this pass.

## Source evidence
- `https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/integer_lattices/`
  - `automorphism_group_generators`: "Given a **definite** lattice `L`, return generators for the automorphism group of `L`."
  - `automorphism_group_order`: "Given a **definite** lattice `L`, return the order of the automorphism group of `L`."
  - Full typed signature: `automorphism_group_generators(L::AbstractLat; ambient_representation::Bool=true, depth::Int=-1, bacher_depth::Int=0)`

## Commit
- `b4936ad` — docs: correct automorphism_group_generators/order definiteness constraint from [PD] to [DEFINITE]

## Validation
- Documentation-only pass; no runtime tests executed.

## Intentional non-edits
- Did not modify unrelated pre-existing dirty files (agent_runner logs, etc.)

## Pattern note
- This is the **second** instance of the same `[PD]` vs `[DEFINITE]` error pattern in this project:
  - Pass 1: Sage `IntegralLattice.orthogonal_group` — `[PD]` → `[DEFINITE]` (commit `08c2e42`)
  - Pass 2: Julia/OSCAR `automorphism_group_generators` / `automorphism_group_order` — `[PD]` → `[DEFINITE]` (commit `b4936ad`)
- Future workers should check other `[PD]`-tagged methods where the upstream may actually say "definite" (not "positive definite").

## Remaining high-impact gaps
1. §2.8 `is_isometric(L1, L2)` — tagged `[PD]` but no explicit definiteness restriction stated in upstream docstring; may warrant a review.
2. §2.8 `is_isometric_with_isometry(L1, L2)` — not confirmed in current upstream docs but documented with a return contract; status should be reviewed.
3. §2.3, §2.4, §2.9: most entries unchecked (no method-tagged tests).
4. §2.14 Construction/accessor/attribute/operations blocks: almost entirely unchecked.
5. Missing local doc copies for flint, gap, ntl, fpylll, forms, g6k, crystallographic_stack, pari_gp.
