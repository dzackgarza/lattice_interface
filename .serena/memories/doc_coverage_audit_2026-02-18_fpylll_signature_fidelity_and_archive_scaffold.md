# Doc Coverage Audit Handoff (2026-02-18): fpylll signature fidelity + archive scaffold

## Objectives covered
- FIRST GOAL (cursory maintenance check): brief survey for missing in-scope package surfaces; no clear new bilinear-form lattice package surface requiring checklist creation was identified in this pass.
- SECOND GOAL (active phase focus): tighten method contract correctness/completeness on existing in-scope `fpylll` surface (signatures, defaults, constraints, caveats, source grounding).
- TODO queue execution: completed first two scope-cleanup scaffold items by creating archive structure + archive README and checking them off in `docs/TODO.md`.

## Completed edits
1. `docs/fpylll_methods_checklist.md`
- Replaced placeholder/incorrect signatures with source-anchored signatures.
- Corrected `GSO.Mat` / `MatGSO` constructor surface to include `flags=GSO_DEFAULT` and removed incorrect `precision` parameter.
- Corrected `Enumeration(...)` constructor surface (removed unsupported `threads` parameter).
- Expanded BKZ parameter surface with explicit argument contract and source-anchor caveat.
- Added explicit `Pruning.run(...)`, `adjust_radius_to_gh_bound(...)`, and `gaussian_heuristic(...)` signatures.
- Added provenance-file reference.

2. `docs/fpylll/lattice/fpylll_lattice_reference.md`
- Rewrote to canonical/source-backed contract style.
- Added explicit method signatures, default values, and parameter constraints for core `LLL`, `BKZ`, `Enumeration`, `SVP/CVP`, `Pruning`, and utility APIs.
- Added explicit BKZ doc-gap note: modules page does not fully render BKZ member signatures; signatures are source-anchored.
- Removed non-canonical DeepWiki/Context7 source references and replaced with canonical upstream docs + source files.

3. `docs/fpylll/upstream/fpylll_online_provenance_2026-02-18.md` (new)
- Added dated provenance capture with canonical URLs and signature-fidelity notes used for this pass.

4. `docs/archive/README.md` (new) + archive structure scaffolding
- Added archive scope-policy README.
- Added tracked placeholders:
  - `docs/archive/scope_violations/.gitkeep`
  - `docs/archive/scope_violations/upstream/.gitkeep`

5. `docs/TODO.md`
- Marked complete:
  - create archive folder structure,
  - add archive README.

## Commit
- `eb5d41b` — docs: tighten fpylll method contracts and add scope archive scaffold

## Notes on repository state handling
- Preserved unrelated pre-existing dirty files and did not revert/reset them:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`

## Remaining high-impact gaps
1. Continue TODO scope migration: move known out-of-scope package docs into `docs/archive/scope_violations/` and repair cross-links.
2. Continue Goal 2 across other in-scope package surfaces (e.g., similar signature-fidelity passes where placeholders remain).
3. Add method-tagged tests for the corrected `fpylll` signatures/contracts so checklist boxes can be evidence-closed.

## Validation
- Documentation-only pass; no runtime test suite executed in this environment.