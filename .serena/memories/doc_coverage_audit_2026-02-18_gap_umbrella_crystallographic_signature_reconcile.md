# Doc Coverage Audit Handoff (2026-02-18): GAP umbrella crystallographic signature reconciliation

## Objectives covered
- FIRST GOAL (cursory maintenance check): performed a brief in-repo package-surface scan for missing checklist surfaces among documented package folders; no new clear in-scope bilinear-form lattice package surface gap was found in this pass.
- SECOND GOAL (active phase focus): reconciled crystallographic method signatures and selector constraints in GAP umbrella docs to match the canonicalized crystallographic-stack surfaces.
- TODO queue integration: added and checked off a Goal 2 queue item for this reconciliation.

## Completed edits
1. `docs/gap_methods_checklist.md`
- Replaced placeholder crystallographic signatures with canonical forms:
  - `AffineCrystGroupOnRight(S)`, `AffineCrystGroupOnLeft(S)`, `PointGroup(S)`, `TranslationsCrystGroup(S)`,
    `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`,
    `WyckoffPositions(S)`, `WyckoffOrbit(G, p)`, `WyckoffLattice(G, p)`, `WyckoffNormalClosure(G, p)`.
- Added canonical CARAT/Bravais surfaces missing from umbrella checklist:
  - `BravaisGroup(R)`, `PointGroupsBravaisClass(R)`, `BravaisSubgroups(R)`, `BravaisSupergroups(R)`,
    `NormalizerInGLnZ(R)`, `CentralizerInGLnZ(R)`, `IsBravaisEquivalent(R, S)`,
    `CaratZClass(R)`, `CaratZClassNumber(R)`, `CaratQClass(R)`, `CaratQClassNumber(R)`,
    `RationalClassesMaximalSubgroups(R)`, `ZClassRepsQClass(R)`, `MaximalSubgroupsRepresentatives(R)`,
    `AffineNormalizer(R)`, `IsCaratZClass(R)`, `IsCaratQClass(R)`.
- Added explicit selector-domain and alias-triage caveats (`normedQclass`, `orbitsQclass`, and legacy `CrystCat*` aliases).
- Added direct references to crystallographic-stack docs and canonical upstream manuals.

2. `docs/gap/lattice/gap_lattice_methods_reference.md`
- Updated section `2.1 Crystallographic lattice stack` package role/tag rows to match canonical stack semantics.
- Replaced placeholder `Cryst` signatures and added missing canonical methods including `WyckoffNormalClosure`.
- Added a dedicated canonical `CARAT/Bravais` method table mirroring active crystallographic-stack contracts.
- Added selector-domain constraints and explicit non-canonical selector/alias triage notes.
- Added source-anchor note pointing to canonical crystallographic-stack reference + provenance files.
- Updated consolidated index section from `Cryst methods` to `Cryst/CARAT methods (canonical)` with the expanded method inventory.

3. `docs/TODO.md`
- Added and checked off:
  - `Reconcile GAP umbrella crystallographic signatures with canonical crystallographic-stack contracts in docs/gap_methods_checklist.md and docs/gap/lattice/gap_lattice_methods_reference.md`.

## Commit
- `60734f9` — docs: reconcile GAP crystallographic signatures with canonical contracts

## Validation
- Verified old placeholder crystallographic signature forms no longer appear in touched GAP umbrella sections.
- Documentation-only pass; no runtime tests executed.

## Intentional non-edits
- Did not modify pre-existing unrelated dirty files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`

## Remaining high-impact gaps
1. Continue TODO scope-migration backlog for clearly out-of-scope polyhedral/LP surfaces to archive.
2. Add `method:`-tagged tests for canonicalized crystallographic signatures now present in GAP umbrella docs.
3. Sweep other in-scope umbrella surfaces for similar signature drift against source-backed per-package canonical references.