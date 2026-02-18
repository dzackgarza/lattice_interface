# Doc Coverage Audit Handoff (2026-02-17): PARI/GP signature-surface closure

## Objective addressed
- SECOND GOAL: close method-argument/type-surface gaps for an in-scope bilinear-form lattice package (PARI/GP `qf*` APIs).
- FIRST GOAL status check in this pass: no additional missing in-scope package checklist surface discovered; focused on signature fidelity in existing PARI checklist surface.

## Completed work
- Replaced placeholder `...` signatures with source-backed explicit PARI signatures in:
  - `docs/pari_gp_methods_checklist.md`
  - `docs/pari_gp/lattice/pari_gp_lattice_reference.md`
- Added upstream provenance capture file:
  - `docs/pari_gp/upstream/pari_gp_online_provenance_2026-02-17.md`
- Signature surfaces tightened for:
  - `qfauto`, `qfautoexport`, `qforbits`
  - `qfisom`, `qfisominit`
  - `qflll`, `qflllgram`
  - `qfminim`, `qfminimize`, `qfcvp`
  - `qfrep`, `qfeval`, `qfnorm`
  - `qfgaussred`, `qfperfection`, `qfparam`, `qfsign`, `qfsolve`
- Added explicit caveats from upstream docs:
  - positive-definite constraints for `qfauto`/`qfisom`/`qfisominit`
  - `qforbits` sign-representative precondition (`-I` and `{v,-v}` convention)
  - `qfparam` ternary-form context
  - `qfperfection` rank-8-only note
  - `qfnorm` obsolete (prefer `qfeval`)

## Sources used
- PARI stable function index: `https://pari.math.u-bordeaux.fr/dochtml/ref-stable/function_index.html`
- PARI vectors/matrices + qf chapter: `https://pari.math.u-bordeaux.fr/dochtml/ref-stable/Vectors__matrices__linear_algebra_and_sets.html`
- PARI docs home: `https://pari.math.u-bordeaux.fr/`

## Intentional non-edits
- Did not modify unrelated pre-existing dirty/untracked files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - `.serena/`, `docs/TODO.md`, `scripts/__pycache__/`
- Did not mark checklist boxes complete (no new `method:`-tagged test evidence added).
- Did not modify `docs/method_ground_truth_tracker.csv` in this pass.

## Remaining high-impact gaps
1. Perform a similar signature-fidelity pass for remaining in-scope entries that still expose `...` argument placeholders in `docs/julia_methods_checklist.md` / `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (especially stabilizer/action methods).
2. Add `method:`-tagged tests for representative PARI methods (isometry, indefinite solving, and minimization families) before checking boxes.
3. Reconcile PARI checklist entries with tracker rows after test evidence exists.

## Commit
- `aa94c9f`