# Doc Coverage Audit Handoff (2026-02-17): TOPCOM checklist surface

## Objective addressed
- FIRST GOAL: add checklist coverage for a known lattice-method package not yet represented with a checklist surface.

## Completed work
- Added a first-class TOPCOM checklist surface:
  - `docs/topcom_methods_checklist.md`
- Added matching detailed TOPCOM reference surface:
  - `docs/topcom/lattice/topcom_lattice_reference.md`
- Added upstream provenance snapshot for canonical source evidence:
  - `docs/topcom/upstream/topcom_online_provenance_2026-02-17.md`
- Included source-backed command inventory, argument/option surfaces, and domain caveats (triangulation/oriented-matroid scope vs indefinite quadratic-form scope).

## Commit
- `823d4e9` — docs: add topcom checklist and reference surfaces

## Validation attempts
- `just test` failed in this environment: `/bin/bash: line 1: just: command not found`.
- `conda run -n sage pytest -q sage_doc/test_integrallattice_static.py -k "method:"` failed in this environment: `/bin/bash: line 1: conda: command not found`.

## Intentional non-edits
- Did not modify pre-existing unrelated dirty/untracked files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `scripts/doc_coverage_scheduler.py`
  - `.serena/`
  - `scripts/__pycache__/`
- Did not check any checklist boxes or alter `docs/method_ground_truth_tracker.csv`.

## Remaining high-impact gaps
1. Evaluate whether standalone `cddlib` (core, not only GAP CddInterface wrapper) should receive a dedicated checklist/reference surface for ecosystem-level completeness.
2. Evaluate whether `mptopcom` (parallel TOPCOM package noted upstream) warrants a dedicated checklist surface.
3. Add method-tagged tests for high-impact TOPCOM commands/options (enumeration families and regular/nonregular/unimodular filters) so boxes can be checked.
