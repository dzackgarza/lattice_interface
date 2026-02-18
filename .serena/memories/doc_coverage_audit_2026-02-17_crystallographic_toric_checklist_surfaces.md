# Doc Coverage Audit Handoff (2026-02-17): crystallographic stack + GAP toric checklist surfaces

## Objective addressed
- FIRST GOAL: create checklist coverage surfaces for known lattice-relevant packages lacking first-class checklists.
- SECOND GOAL (triage/completeness): add source-backed method inventories with explicit caveats where typed signature fidelity is not yet available from current docs.

## Completed work
- Added first-class checklist + detailed reference + provenance surfaces for GAP crystallographic stack packages (`Cryst`, `CARATInterface`, `CrystCat`):
  - `docs/crystallographic_stack_methods_checklist.md`
  - `docs/crystallographic_stack/lattice/crystallographic_stack_lattice_reference.md`
  - `docs/crystallographic_stack/upstream/crystallographic_stack_online_provenance_2026-02-17.md`
- Added first-class checklist + detailed reference + provenance surfaces for GAP `toric` package:
  - `docs/toric_methods_checklist.md`
  - `docs/toric/lattice/gap_toric_lattice_reference.md`
  - `docs/toric/upstream/toric_online_provenance_2026-02-17.md`
- Captured method inventories/caveats directly in new package-specific surfaces; all checklist boxes remain unchecked (no new `method:` test evidence in this pass).

## Sources used
- `https://gap-packages.github.io/cryst/`
- `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/inst.htm`
- `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/crystcat/doc/chap39.htm`
- `https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap035.htm`
- `https://gap-packages.github.io/toric/`
- `https://gap-packages.github.io/toric/doc/chap0_mj.html`
- existing local umbrella mapping: `docs/gap/lattice/gap_lattice_methods_reference.md`

## Key decisions
- Used a single dedicated crystallographic-stack checklist surface to cover tightly coupled package methods where available source chapters co-document CrystCat/CARAT-linked APIs.
- Explicitly documented source-age and package-attribution caveats instead of inferring modern typed signatures without direct evidence.
- Kept changes isolated to new files only because several core docs files were pre-existing dirty edits not created in this pass.

## Intentional non-edits
- Did not modify pre-existing dirty files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `docs/gap_methods_checklist.md`
  - `docs/nconvex_methods_checklist.md`
  - `docs/nconvex/lattice/nconvex_lattice_reference.md`
  - `docs/nconvex/upstream/nconvex_online_provenance_2026-02-17.md`
  - `docs/project/doc_coverage_audit_changelog.md`
  - `scripts/doc_coverage_scheduler.py`
- Did not edit `docs/method_ground_truth_tracker.csv` (no new method-tagged test evidence).

## Validation
- Documentation-surface pass only; no runtime tests executed.
- Staged and committed only assignment files.

## Remaining high-impact gaps
1. Lift full typed signatures for `toric` methods from chapter-level API pages (current surface is runtime-name complete with `...` placeholders).
2. Reconcile crystallographic stack methods against current GAP4 package manuals/source to replace historical-mirror dependency where modern pages expose stronger signatures.
3. Integrate new checklist surfaces into stable navigation files (`docs/documentation_coverage_audit_playbook.md`, `docs/gap_methods_checklist.md`, `docs/project/doc_coverage_audit_changelog.md`) once those pre-existing dirty files are reconciled.
4. Add `method:`-tagged tests for representative methods in both new surfaces before any checklist completion-state updates.

## Commit
- `46fe05d`