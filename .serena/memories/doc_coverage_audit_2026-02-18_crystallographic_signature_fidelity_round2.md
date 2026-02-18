# Doc Coverage Audit Handoff (2026-02-18): crystallographic stack signature-fidelity closure

## Objectives covered
- FIRST GOAL (cursory package check): performed a brief in-scope package-surface scan; no new clear bilinear-form lattice package surface requiring checklist creation was identified in this pass.
- SECOND GOAL (active phase focus): removed placeholder signatures from the crystallographic stack surface and aligned methods to canonical GAP signatures.
- TODO queue integration: added a Goal 2 contract-fidelity queue entry and checked off the crystallographic signature-lift task in `docs/TODO.md`.

## Completed edits
1. `docs/crystallographic_stack/lattice/crystallographic_stack_lattice_reference.md`
- Rewrote Cryst section with canonical signatures from GAP ref chapter 35:
  - `AffineCrystGroupOnRight(S)`, `AffineCrystGroupOnLeft(S)`, `PointGroup(S)`,
    `TranslationsCrystGroup(S)`, `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`,
    `WyckoffPositions(S)`, `WyckoffOrbit(G, p)`, `WyckoffLattice(G, p)`, `WyckoffNormalClosure(G, p)`.
- Replaced non-canonical/placeholder CARAT section with canonical chapter 44.6 method signatures:
  - `BravaisGroup(R[, f])`, `PointGroupsBravaisClass(R[, f[, s]])`,
    `BravaisSubgroups(R[, f[, s[, k]]])`, `BravaisSupergroups(R[, f[, s[, k]]])`,
    `NormalizerInGLnZ(R[, f])`, `CentralizerInGLnZ(R[, f])`, `IsBravaisEquivalent(R, S)`,
    `CaratZClass(R)`, `CaratQClass(R)`, class-number methods, rational/maximal subgroup surfaces,
    `AffineNormalizer(R)`, `IsCaratZClass(R)`, `IsCaratQClass(R)`.
- Added explicit legacy-alias triage section for `CrystCatZClass(...)`, `CrystCatQClass(...)`, `CrystCatQClasses(...)`.

2. `docs/crystallographic_stack_methods_checklist.md`
- Aligned checklist entries to canonical signatures and added missing canonical methods above.
- Added legacy alias triage section so non-canonical names are not treated as active targets.

3. `docs/crystallographic_stack/upstream/crystallographic_stack_online_provenance_2026-02-17.md`
- Switched canonical signature sources to GAP Reference chapters 35 and 44.
- Recorded closure of placeholder-signature gap and listed newly added canonical methods.
- Added brief first-goal note: no additional in-scope package surface discovered in this pass.

4. `docs/TODO.md`
- Added `Goal 2 Contract-Fidelity Queue (In-Scope Surfaces)` section.
- Marked crystallographic signature-lift task complete.
- Added one open follow-up task for optional selector argument value-domain constraints.

## Commit
- `3892fb1` — docs: lift crystallographic method signatures to canonical GAP refs

## Intentional non-edits
- Did not modify unrelated pre-existing dirty files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`
- Did not move archive/scope-violation package files in this pass.

## Remaining high-impact gaps
1. Lift accepted value-domain constraints for optional selector args (`f`, `s`, `k`, `normedQclass`, `orbitsQclass`) from canonical docs/source-level evidence.
2. Continue TODO scope migration items for known out-of-scope polyhedral package surfaces to archive.
3. Add `method:`-tagged coverage tests for newly canonicalized crystallographic methods (especially `WyckoffNormalClosure`, `IsBravaisEquivalent`, `Carat*` predicates).

## Validation
- Documentation-only pass; no runtime tests executed in this environment.