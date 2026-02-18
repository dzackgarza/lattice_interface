# Doc Coverage Audit Handoff (2026-02-17): NTL + FLINT checklist surface expansion

## Objective addressed
- FIRST GOAL: ensure checklist surfaces exist for known relevant lattice-method packages not yet represented as first-class checklists.
- SECOND GOAL (within new surfaces): document source-backed method signatures, argument surfaces, and core constraints/caveats.

## Completed work
- Added new package checklist and detailed reference surfaces for two major lattice-relevant backends that were previously missing as top-level checklists:
  - `docs/ntl_methods_checklist.md`
  - `docs/ntl/lattice/ntl_lattice_reference.md`
  - `docs/flint_methods_checklist.md`
  - `docs/flint/lattice/flint_lattice_reference.md`
- NTL surfaces now include source-backed entries for:
  - exact LLL family (`LLL`, `LLL_plus`, `image`),
  - integer solve (`LatticeSolve`),
  - floating LLL/BKZ families (`[G_]LLL_*`, `[G_]BKZ_*`),
  - HNF (`HNF(mat_ZZ& W, const mat_ZZ& A, const ZZ& D)`) with preconditions.
- FLINT surfaces now include source-backed entries for:
  - LLL context/reduction/reducedness (`fmpz_lll_context_*`, `fmpz_lll*`, `fmpz_lll_is_reduced`, `fmpz_mat_is_reduced`),
  - HNF family (`fmpz_mat_hnf*`, `fmpz_mat_is_in_hnf`),
  - SNF family (`fmpz_mat_snf*`, `fmpz_mat_is_in_snf`).
- Added explicit documented caveats/constraints where available (e.g., FLINT `delta`/`eta` range, low-level floating LLL caveat, NTL `deep` deprecation and HNF input preconditions).

## Key decisions
- Prioritized missing-package checklist creation before additional wording cleanup, in line with FIRST GOAL priority.
- Chose NTL and FLINT because they are active, canonical lattice/integer-matrix backends and previously lacked first-class checklist surfaces in this repository.
- Kept all new checklist boxes unchecked (coverage remains test-evidence-driven).

## Validation
- Docs formatting sanity checks run locally via file inspection and ASCII scan.
- No runtime/doc tests executed in this pass (documentation-surface expansion only).

## Intentional non-edits
- Did not modify unrelated pre-existing dirty files (`AGENTS.md`, `docs/documentation_coverage_audit_playbook.md`, `prompt.md`, `scripts/doc_coverage_scheduler.py`, etc.).
- Did not update `docs/method_ground_truth_tracker.csv` because no new method-tagged test evidence was introduced.
- Did not alter existing checklist completion states.

## Remaining high-impact gaps
1. Add navigation references for the new `ntl`/`flint` checklist surfaces in stable index/playbook surfaces when those files are edited in a clean context.
2. Add method-tagged tests for selected high-impact NTL/FLINT entries (LLL/BKZ/HNF/SNF reducedness contracts) before any checklist box promotion.
3. Reconcile NTL floating-family and BKZ variant coverage against latest upstream docs/source snapshots in a future signature-fidelity pass (especially variant-specific argument nuances).
4. Continue package-surface survey for additional standalone lattice stacks that may warrant first-class checklists if they are confirmed in-scope.

## Commit
- `0bf0afe`