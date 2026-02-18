# Doc Coverage Audit Handoff (2026-02-18): crystallographic selector-domain closure

## Objectives covered
- FIRST GOAL (cursory package check): completed a brief in-repo package-surface scan (`docs/*/lattice` vs `docs/*_methods_checklist.md`); no clear missing in-scope bilinear-form lattice package checklist surface was found in this pass.
- SECOND GOAL (active focus): resolved the open Goal 2 contract-fidelity queue item for crystallographic optional selectors by lifting accepted domains where source-backed and triaging non-canonical selectors.
- TODO integration: marked the Goal 2 selector-domain task complete in `docs/TODO.md`.

## Completed edits
1. `docs/crystallographic_stack/lattice/crystallographic_stack_lattice_reference.md`
- Lifted explicit domains for `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`:
  - `normedQclass`: `false` or list of elements from the normalizer in `GL(d,Z)`.
  - `orbitsQclass`: boolean; `true` returns all representatives in each orbit.
- Replaced selectorized CARAT signatures with source-backed active forms:
  - `BravaisGroup(R)`, `PointGroupsBravaisClass(R)`, `BravaisSubgroups(R)`, `BravaisSupergroups(R)`, `NormalizerInGLnZ(R)`, `CentralizerInGLnZ(R)`.
- Added explicit non-canonical-signature triage for legacy selectorized variants with `f`/`s`/`k`.
- Updated references to Cryst package manual, GAP ref chapter 44, CARATInterface manual, and GAP3 Cryst mirror for selector semantics.

2. `docs/crystallographic_stack_methods_checklist.md`
- Updated checklist signatures for CARAT methods to one-argument canonical forms.
- Replaced deferred selector caveat with explicit domain constraints for `normedQclass`/`orbitsQclass`.
- Added explicit note that `f`/`s`/`k` are not active canonical selector parameters in this checklist surface.
- Updated references to source-backed manuals.

3. `docs/crystallographic_stack/upstream/crystallographic_stack_online_provenance_2026-02-17.md`
- Added source URLs and extraction summary for selector-domain evidence.
- Added `Selector-domain closure (2026-02-18)` section documenting:
  - lifted `normedQclass`/`orbitsQclass` domains,
  - demotion of selectorized `f`/`s`/`k` CARAT signatures as non-canonical in active surface.
- Added network retrieval note for direct `CHAP002.htm` access timeouts (2 attempts, timeout class) while retaining indexed snippet evidence.

4. `docs/TODO.md`
- Checked off the open Goal 2 selector-domain task with updated wording reflecting closure + `f`/`s`/`k` triage.

## Commit
- `2f212c2` — docs: resolve crystallographic selector-domain contracts

## Validation
- Documentation-only pass; no runtime tests executed.
- Committed only assignment-owned files; unrelated dirty files were left untouched.

## Intentional non-edits
- Did not modify pre-existing unrelated changes:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`

## Remaining high-impact gaps
1. Execute TODO scope-migration backlog: archive clearly out-of-scope polyhedral/LP package surfaces and reconcile cross-links.
2. Reconcile crystallographic signatures in umbrella GAP surfaces (`docs/gap_methods_checklist.md`, `docs/gap/lattice/gap_lattice_methods_reference.md`) with the now-corrected crystallographic-stack contracts.
3. Add `method:`-tagged tests for crystallographic-stack methods newly stabilized in canonical form.