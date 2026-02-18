# Doc Coverage Audit Handoff (2026-02-18): `TorQuadModuleWithIsom.submodules` keyword-contract drift

## Objectives covered
- FIRST GOAL (cursory in-scope package maintenance): re-ran a brief in-scope package-surface check while reconciling `torquadmodwithisom`; no clear new bilinear-form lattice package checklist gap was identified.
- SECOND GOAL (active phase focus): corrected Julia/Hecke documentation contract drift for `submodules(::TorQuadModuleWithIsom)` by restoring source-backed keyword/selector constraints present in current upstream docs.
- TODO queue integration: added and checked off Goal 1 + Goal 2 entries in `docs/TODO.md` for this pass.

## Completed edits
1. `docs/julia_methods_checklist.md`
- Updated method surface from:
  - `submodules(::TorQuadModuleWithIsom)`
  to:
  - `submodules(::TorQuadModuleWithIsom; quotype::Vector{Int}=Int[])`
- Replaced stale caveat ("no `quotype` keyword") with source-backed selector-domain caveat (`0,1,2,3`).

2. `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
- Updated `TorQuadModuleWithIsom` method table row for `submodules` to include keyword contract.
- Added selector-domain constraint (`0,1,2,3`) in description.
- Replaced stale signature-fidelity caveat with an explicit drift note:
  - local snapshot file still shows bare signature,
  - current upstream docs expose keyword form.

3. `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md`
- Updated `submodules` row to include `quotype` keyword contract and selector-domain constraints.
- Updated source-note wording to include tuple-return + `submodules` keyword-contract addenda.

4. `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- Added `Pass-23 addendum (2026-02-18)` documenting current upstream evidence and the local alignment action.

5. `docs/TODO.md`
- Added and checked off:
  - Goal 1 cursory in-scope maintenance entry for this drift pass.
  - Goal 2 contract-fidelity entry for `TorQuadModuleWithIsom.submodules` keyword reconciliation.

## Upstream evidence used in this pass
- `https://docs.oscar-system.org/v1/Hecke/manual/quad_forms/torquadmodwithisom/`
- `https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/torquadmodwithisom/`

## Commit
- `d8bfecf` — docs: reconcile julia TorQuadModuleWithIsom submodules keyword contract

## Validation
- Performed targeted diff and content sanity checks on touched files (`git diff`, local grep/sed inspection).
- Documentation-only pass; no runtime tests executed.

## Intentional non-edits
- Left unrelated pre-existing dirty files untouched:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`

## Remaining high-impact gaps
1. Continue Goal 2 contract-fidelity sweeps for other Julia `fingrpact` stabilizer-family methods still documented with runtime-name placeholders (`...`) due missing typed dispatch blocks in available docs.
2. Progress outstanding scope-archive TODO backlog (polyhedral/toric/LP families) after confirming no higher-priority in-scope contract drifts remain in active surfaces.