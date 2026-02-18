# Doc Coverage Audit Handoff (2026-02-17): missing package checklist surfaces

## Completed work
- Added first-class checklist surfaces for package ecosystems that previously had reference docs but no checklist entry points:
  - `docs/gap_methods_checklist.md`
  - `docs/fpylll_methods_checklist.md`
  - `docs/pari_gp_methods_checklist.md`
  - `docs/latticegen_methods_checklist.md`
- Each new checklist includes:
  - explicit method/command inventory,
  - argument-surface form where source-backed,
  - constraints/caveats for definiteness/domain when relevant,
  - source links to in-repo references + canonical upstream docs.
- Incorporated GAP package ecosystem surfaces (Cryst/CARAT/CrystCat, NormalizInterface, 4ti2Interface, toric, CddInterface, fplll hooks) into a dedicated checklist so package-level lattice methods are now represented as checklist items.
- Added explicit two-toolchain separation for `latticegen` (fplll CLI vs Python moire package) with source-backed API entries for both.

## Key decisions
- Prioritized FIRST GOAL from playbook: create missing checklist surfaces before refining existing Sage/Julia wording.
- Kept all new checklist boxes unchecked (coverage accounting remains test-driven).
- Did not commit modifications to `docs/documentation_coverage_audit_playbook.md` because that file had large pre-existing unrelated changes in the dirty worktree; committing it would have mixed unrelated edits into this assignment.

## Validation
- `just test` could not run in this environment (`just: command not found`).
- Targeted Sage pytest invocation could not run in this environment (`conda: command not found`).

## Intentional non-edits
- Did not modify or stage unrelated dirty files:
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/` and `scripts/__pycache__/`
- Did not check any checklist boxes or alter method_ground_truth tracker rows.

## Remaining high-impact gaps
1. Add these four new checklist files to stable navigation surfaces once `docs/documentation_coverage_audit_playbook.md` is reconciled in a clean branch/state.
2. Build method-tagged test coverage for high-impact methods newly listed in:
   - GAP core normal forms + LLL/search,
   - fpylll BKZ/SVP/CVP/pruning surfaces,
   - PARI `qf*` indefinite and isometry workflows,
   - latticegen (fplll CLI generation modes and Python API routines).
3. Signature-fidelity pass for fpylll BKZ/SVP/CVP sections against source code because current official modules page exposes section headers with incomplete member signatures.
4. Perform optional-package completeness pass for additional GAP package surfaces beyond the current consolidated set if new lattice-relevant methods emerge in package updates.

## Commit
- `2da094a`