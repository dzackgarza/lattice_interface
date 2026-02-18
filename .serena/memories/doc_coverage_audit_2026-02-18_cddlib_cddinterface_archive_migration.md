# Doc Coverage Audit Handoff (2026-02-18): cddlib + CddInterface archive migration

## Objectives covered
- FIRST GOAL (cursory maintenance check): performed a brief in-scope package-surface check against current checklist inventory and recent handoff memories; no clear new bilinear-form lattice package checklist gap was identified in this pass.
- Scope-gate alignment work (active queue): migrated two known out-of-scope polyhedral package surfaces (`cddlib`, `CddInterface`) into `docs/archive/scope_violations/` and converted old active paths into redirect notes.
- TODO queue integration: checked off the two queue items for moving cddlib and CddInterface docs in `docs/TODO.md`.

## Completed edits
1. Archived moved surfaces (full-content copies):
- `docs/archive/scope_violations/cddlib_methods_checklist.md`
- `docs/archive/scope_violations/cddlib/lattice/cddlib_lattice_reference.md`
- `docs/archive/scope_violations/cddlib/upstream/cddlib_online_provenance_2026-02-17.md`
- `docs/archive/scope_violations/cddinterface_methods_checklist.md`
- `docs/archive/scope_violations/cddinterface/lattice/cddinterface_lattice_reference.md`
- `docs/archive/scope_violations/cddinterface/upstream/cddinterface_online_provenance_2026-02-17.md`

2. Redirect stubs at previous active locations (to avoid broken paths during incremental migration):
- `docs/cddlib_methods_checklist.md`
- `docs/cddlib/lattice/cddlib_lattice_reference.md`
- `docs/cddlib/upstream/cddlib_online_provenance_2026-02-17.md`
- `docs/cddinterface_methods_checklist.md`
- `docs/cddinterface/lattice/cddinterface_lattice_reference.md`
- `docs/cddinterface/upstream/cddinterface_online_provenance_2026-02-17.md`

3. Cross-reference updates in GAP umbrella docs:
- `docs/gap_methods_checklist.md`
  - CddInterface caveat/reference now points to archived checklist path.
- `docs/gap/lattice/gap_lattice_methods_reference.md`
  - CddInterface detailed-inventory note now points to archived checklist/reference paths.

4. TODO updates:
- `docs/TODO.md`
  - marked complete:
    - `Move cddlib docs`
    - `Move CddInterface docs`

## Commit
- `2c700ff` — docs: archive cddlib and CddInterface scope-violation surfaces

## Validation
- Ran targeted local path checks on touched non-TODO files: no missing `docs/*.md` references detected.
- Confirmed touched archive files no longer self-reference pre-archive internal paths.
- Documentation-only pass; no runtime tests executed.

## Intentional non-edits
- Did not modify unrelated pre-existing dirty files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `prompt.md`
  - `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`

## Remaining high-impact gaps
1. Continue scope-migration queue for remaining out-of-scope package surfaces (`4ti2`, `latte_integrale`, `normaliz`, `lrslib`, `polymake`, `topcom`, `palp`, `toric`, `nconvex`, and remaining cdd-style umbrella sections).
2. Complete umbrella-file archiving for GAP and Sage mixed docs (remove or archive out-of-scope sections, not just standalone package files).
3. Reconcile active navigation references globally (including playbook/index surfaces) once dirty-state constraints on `docs/documentation_coverage_audit_playbook.md` are resolved or with explicit partial-staging strategy.
4. Run repository-wide link/path validation after broader archive migration batch lands.