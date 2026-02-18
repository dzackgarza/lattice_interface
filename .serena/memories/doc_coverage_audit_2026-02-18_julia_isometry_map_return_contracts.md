# Doc Coverage Audit Handoff (2026-02-18): Julia isometry map-return contract fidelity

## Objectives covered
- FIRST GOAL (cursory package-surface check): performed a brief in-scope package maintenance scan against current checklist surfaces and prior package-gap memories; no clear new bilinear-form lattice package surface requiring a new checklist was identified in this pass.
- SECOND GOAL (active phase focus): tightened method-level contract completeness for existing in-scope Julia/Hecke isometry APIs by replacing vague map-return descriptions with source-backed tuple return and precondition contracts.
- TODO queue integration: added and checked off a Goal 2 contract-fidelity item in `docs/TODO.md` for this Julia isometry contract pass.

## Completed edits
1. `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
- Tightened `is_isometric_with_isometry(L1, L2)` with explicit tuple return contract and documented kwargs (`depth`, `bacher_depth`, `ambient_representation`) from upstream docs.
- Tightened finite quadratic module methods:
  - `is_isometric_with_isometry(T, U)`
  - `is_anti_isometric_with_anti_isometry(T, U)`
  with tuple-return semantics and documented modulus/rescale + semiregular decomposition preconditions.
- Tightened `TorQuadModuleWithIsom` methods:
  - `is_isomorphic_with_map(Tf, Sg)`
  - `is_anti_isomorphic_with_map(Tf, Sg)`
  to explicit `(true, map)` vs `(false, 0)` contracts.
- Updated section source-note wording to reference the 2026-02-18 addendum.

2. `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md`
- Mirrored the same contract tightening for:
  - `is_isometric_with_isometry(L1, L2)`
  - `is_isometric_with_isometry(T, U)` / `is_anti_isometric_with_anti_isometry(T, U)`
  - `is_isomorphic_with_map(Tf, Sg)` / `is_anti_isomorphic_with_map(Tf, Sg)`
- Updated source-note wording to reference the new addendum.

3. `docs/julia_methods_checklist.md`
- Added caveat bullets for:
  - `is_isometric_with_isometry(L1, L2)` tuple-return + kwargs.
  - `is_isometric_with_isometry(T, U)` and `is_anti_isometric_with_anti_isometry(T, U)` tuple-return + preconditions.
  - `is_isomorphic_with_map(Tf, Sg)` and `is_anti_isomorphic_with_map(Tf, Sg)` tuple-return failure sentinel.
- Updated `Last updated` stamp to `2026-02-18`.

4. `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- Added `Pass-19 addendum (2026-02-18)` recording upstream evidence URLs and verified tuple-return/precondition contracts.

5. `docs/TODO.md`
- Added and checked off a Goal 2 queue item for this pass.

## Upstream evidence added in this pass
- `https://docs.oscar-system.org/v1.4/Hecke/manual/lattices/integrelattices/`
- `https://docs.oscar-system.org/v1/Hecke/manual/quad_forms/torquadmod/`
- `https://docs.oscar-system.org/dev/Hecke/manual/quad_forms/torquadmodwithisom/`

## Commit
- `261486d` — docs: tighten Julia isometry map-return contracts

## Validation
- Attempted targeted static doc tests, but test runner is unavailable in this environment:
  - `pytest -q tests/julia_pytest/test_quadform_and_isom_static.py` -> `pytest: command not found`
  - `pytest -q tests/julia_pytest/test_oscar_bridge_static.py` -> `pytest: command not found`

## Intentional non-edits
- Did not modify unrelated pre-existing dirty files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`

## Remaining high-impact gaps
1. Continue Goal 2 signature-fidelity tightening for other Julia map-return APIs where row text still says only "explicit map" without return tuple/sentinel semantics.
2. Proceed with open TODO scope-migration backlog (out-of-scope polyhedral/toric archives) once in-scope contract-fidelity priorities for active surfaces are satisfied in the run plan.