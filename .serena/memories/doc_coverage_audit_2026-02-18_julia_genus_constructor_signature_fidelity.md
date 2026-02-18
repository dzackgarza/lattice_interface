# Doc Coverage Audit Handoff (2026-02-18): Julia genus-constructor signature fidelity

## Objectives covered
- FIRST GOAL (cursory package-surface maintenance): re-ran a brief in-scope package check during this pass; no clear new bilinear-form lattice package checklist gap identified.
- SECOND GOAL (active phase): tightened method-level signature/argument constraints for existing in-scope Julia genus-constructor surfaces where `...` placeholders remained.
- TODO queue integration: added and checked off Goal 1 + Goal 2 items in `docs/TODO.md` for this pass.

## Completed edits
1. `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
- Replaced placeholder `integer_genera(sig, det; ...)` with source-backed typed overloads and determinant sign/parity constraints.
- Replaced placeholder `hermitian_genera(E, rank, sigs, det; ...)` with source-backed typed signature + default keyword semantics + domain constraints.
- Tightened `hermitian_local_genera` to typed signature with explicit ideal/determinant/scale arguments.
- Expanded source-note scope to include §2.7 and §2.16 plus Hecke genera manuals.

2. `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md`
- Replaced `integer_genera(sig, det; ...)` placeholder with typed overloads and determinant constraints.
- Split coarse `hermitian_genera(...) / hermitian_local_genera(...)` row into two typed rows with explicit constraints.
- Added canonical genus manuals to Sources list (`quad_forms/genera`, `quad_forms/genusherm`).

3. `docs/julia_methods_checklist.md`
- Replaced `integer_genera(sig, det; ...)` checklist entry with typed overloads and caveat bullets for determinant sign/parity constraints.
- Replaced `hermitian_genera(...)/hermitian_local_genera(...)` placeholders with typed signatures and caveat bullets.

4. `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- Added Pass-22 addendum documenting upstream evidence URLs and verified signatures/constraints for `integer_genera`, `hermitian_genera`, and `hermitian_local_genera`.

5. `docs/TODO.md`
- Added and checked off:
  - Goal 1 cursory package-surface maintenance re-run note for this pass.
  - Goal 2 genus-constructor signature-fidelity completion item.

## Upstream evidence used in this pass
- https://docs.oscar-system.org/v1.4/Hecke/manual/quad_forms/genera/
- https://docs.oscar-system.org/v1.4/Hecke/manual/quad_forms/genusherm/

## Commit
- `6615be5` — docs: tighten Julia genus constructor signatures

## Validation
- Attempted targeted static doc test:
  - `pytest -q tests/julia_pytest/test_quadform_and_isom_static.py`
  - result: `pytest: not found` in this environment.

## Intentional non-edits
- Did not touch unrelated pre-existing dirty files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`

## Remaining high-impact gaps
1. Continue Goal 2 closure for remaining Julia methods still carrying `...` placeholders in active in-scope surfaces (e.g., selected stabilization/embedding helpers) when source-backed typed signatures are available.
2. Proceed with open TODO scope-migration backlog (archiving out-of-scope polyhedral/toric surfaces) after in-scope contract-fidelity priorities remain adequately covered for the run.