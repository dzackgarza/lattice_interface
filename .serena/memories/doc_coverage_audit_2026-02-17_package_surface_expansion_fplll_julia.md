# Doc Coverage Audit Handoff (2026-02-17): package checklist surface expansion

## Objective addressed
- FIRST GOAL: ensure checklist coverage surfaces exist for known lattice-method packages; prioritize missing package surfaces.

## Completed work
- Added a new first-class checklist + reference surface for `fplll` (previously missing as a dedicated package surface):
  - `docs/fplll_methods_checklist.md`
  - `docs/fplll/lattice/fplll_lattice_reference.md`
- Expanded top-level Julia checklist package coverage to include package sections present in the Julia reference but previously absent from checklist surface:
  - added `LLLplus.jl` checklist section with explicit method signatures and Euclidean/PD caveat.
  - added `LatticeAlgorithms.jl` checklist section with source-backed method signatures and Euclidean/PD caveat.
  - added explicit minor-package checklist anchors for `LatticeBasisReduction.jl` and `MinkowskiReduction.jl` with triage caveats (method-signature capture pending upstream API source capture).
- Aligned `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` section 6 with explicit runtime method names (`lll`, `islllreduced`, `kz`, `closest_point`, `closest_point_Dn`, `Dn`, `distance`, `distances`) instead of capability-only wording.
- Added repository/source references for newly surfaced package methods where available.

## Commit
- `a6e6e95` — docs: add missing lattice package checklist surfaces

## Validation attempts
- `just test` failed in this environment: `just: command not found`.
- targeted Sage pytest command failed in this environment: `conda: command not found`.

## Intentional non-edits
- Did not modify pre-existing unrelated dirty/untracked files:
  - `AGENTS.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - `.serena/`, `docs/interface_design_playbook.md`, `docs/test_coverage_playbook.md`, `scripts/__pycache__/`
- Did not check off any checklist boxes.

## Remaining high-impact gaps
1. Create authoritative per-method signature inventory for `LatticeBasisReduction.jl` and `MinkowskiReduction.jl` from upstream docs/source (currently only checklist anchors + caveats).
2. Consider whether additional major package surfaces (outside currently documented map) require first-class checklists (for example, if project scope confirms NTL/FLINT-first or other research-critical stacks).
3. Add navigation references for new `fplll` checklist surface in stable non-dirty index/playbook docs once those files are reconciled in a clean state.
4. Build `method:` tagged tests for newly surfaced `fplll` and Julia package entries so checklist items can move from inventory to coverage.
