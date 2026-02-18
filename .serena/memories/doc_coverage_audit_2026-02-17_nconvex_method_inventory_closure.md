# Doc Coverage Audit Handoff (2026-02-17): NConvex method-inventory blocker closure

## Objective addressed
- SECOND GOAL: method-level completeness for existing package surfaces (argument contracts, type surfaces, assumptions/caveats) on NConvex.
- FIRST GOAL check: no additional missing top-level package checklist file discovered in this pass; focused on clearing remaining method-inventory blocker in already-created `NConvex` checklist surface.

## Completed work
- Replaced source-blocked placeholder status in NConvex surfaces with source-backed method inventory:
  - `docs/nconvex_methods_checklist.md`
  - `docs/nconvex/lattice/nconvex_lattice_reference.md`
  - `docs/nconvex/upstream/nconvex_online_provenance_2026-02-17.md`
- Added full method-level checklist coverage across:
  - shared convex-object methods,
  - cone/fan/polyhedron/polytope methods,
  - LP and zsolve surfaces,
  - source-only declaration surfaces (explicitly marked as source-only, not manual-indexed).
- Captured argument surfaces and operational caveats from canonical manual pages:
  - TopcomInterface availability caveat for triangulation-based fan methods,
  - `SolveLinearProgram` `max_or_min ∈ {"max", "min"}` contract,
  - optional `signs` contract for `SolveEqualitiesAndInequalitiesOverIntergers`.
- Reconciled umbrella GAP docs to remove stale NConvex blocker language and expose representative methods:
  - `docs/gap_methods_checklist.md`
  - `docs/gap/lattice/gap_lattice_methods_reference.md`
- Appended continuity entry:
  - `docs/project/doc_coverage_audit_changelog.md` (`Pass ID: 20260217-15`).

## Sources used
- NConvex package/manual:
  - `https://homalg-project.github.io/NConvex/`
  - `https://homalg-project.github.io/NConvex/doc/chap0_mj.html`
  - `https://homalg-project.github.io/NConvex/doc/chapInd_mj.html`
  - `https://homalg-project.github.io/NConvex/doc/chap3_mj.html`
  - `https://homalg-project.github.io/NConvex/doc/chap4_mj.html`
  - `https://homalg-project.github.io/NConvex/doc/chap5_mj.html`
  - `https://homalg-project.github.io/NConvex/doc/chap6_mj.html`
  - `https://homalg-project.github.io/NConvex/doc/chap7_mj.html`
- NConvex source declarations:
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/ConvexObject.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Cone.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Fan.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Polyhedron.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Polytope.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/ZSolve.gd`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/PackageInfo.g`
  - `https://raw.githubusercontent.com/homalg-project/NConvex/master/README.md`

## Intentional non-edits
- Did not modify unrelated dirty/untracked files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `scripts/doc_coverage_scheduler.py`
  - `.serena/`
  - `scripts/__pycache__/`
- Did not check any checklist boxes.
- Did not update `docs/method_ground_truth_tracker.csv` (no new `method:` tagged tests in this pass).

## Validation
- Attempted `just test` failed in this environment: `/bin/sh: 1: just: not found`.

## Remaining high-impact gaps
1. Add method-tagged tests for representative NConvex methods and propagate evidence to `docs/method_ground_truth_tracker.csv`.
2. Re-audit source-only (`[SRC]`) NConvex declarations against future manual regeneration; move entries from source-only to manual-backed when upstream docs expose them.

## Commit
- `3434318` — docs: expand NConvex method-level coverage and clear blocker
- `9b84b90` — docs: record pass 20260217-15 commit hash