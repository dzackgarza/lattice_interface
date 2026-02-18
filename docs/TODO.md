# TODO

## Scope Cleanup (Bilinear-Form Lattice Theory Only)

- [x] Create archive folder structure for out-of-scope docs:
  - `docs/archive/`
  - `docs/archive/scope_violations/`
  - `docs/archive/scope_violations/upstream/`
- [x] Add `docs/archive/README.md` explaining that archived content is out of scope for lattice theory in this project (free `R`-modules with symmetric nondegenerate bilinear form).

## Move Known Scope-Violation Surfaces to Archive

- [ ] Move pycddlib docs (explicit example scope violation):
  - `docs/pycddlib_methods_checklist.md`
  - `docs/pycddlib/lattice/pycddlib_lattice_reference.md`
  - `docs/pycddlib/upstream/pycddlib_online_provenance_2026-02-17.md`
- [ ] Move cddlib docs:
  - `docs/cddlib_methods_checklist.md`
  - `docs/cddlib/lattice/cddlib_lattice_reference.md`
  - `docs/cddlib/upstream/cddlib_online_provenance_2026-02-17.md`
- [ ] Move CddInterface docs:
  - `docs/cddinterface_methods_checklist.md`
  - `docs/cddinterface/lattice/cddinterface_lattice_reference.md`
  - `docs/cddinterface/upstream/cddinterface_online_provenance_2026-02-17.md`
- [ ] Move polyhedral/LP-centered package docs identified as out of scope:
  - `docs/4ti2_methods_checklist.md`
  - `docs/latte_integrale_methods_checklist.md`
  - `docs/normaliz_methods_checklist.md`
  - `docs/lrslib_methods_checklist.md`
  - `docs/polymake_methods_checklist.md`
  - `docs/topcom_methods_checklist.md`
  - `docs/palp_methods_checklist.md`
  - `docs/toric_methods_checklist.md`
  - `docs/nconvex_methods_checklist.md`
  - plus matching package subfolders under `docs/<package>/` and `docs/<package>/upstream/` where present.

## Archive Out-of-Scope Sections From Mixed Files

- [ ] Archive out-of-scope package families from GAP umbrella checklist/reference:
  - move/archive `NConvex`, `toric`, `Normaliz`, and cdd-style polyhedral surfaces from:
    - `docs/gap_methods_checklist.md`
    - `docs/gap/lattice/gap_lattice_methods_reference.md`
- [ ] Archive toric/polyhedral sections from Sage umbrella docs:
  - move/archive toric/fan/polytope sections that are not bilinear-form lattice APIs from:
    - `docs/sage_methods_checklist.md`
    - `docs/sage/lattice/sagemath_lattice_reference.md`
- [ ] Sweep remaining umbrella docs for out-of-scope references and archive them (do not delete content).

## Reconcile Cross-References After Archiving

- [ ] Replace active-scope links with archive links for out-of-scope entries in:
  - `docs/documentation_coverage_audit_playbook.md` (references + upstream living map)
  - umbrella checklists/references where affected
  - any index/navigation pages that link moved files.
- [ ] Add redirects or replacement notes in moved file locations (or update all links directly).

## Validation

- [ ] Run link/path checks to ensure no broken references remain after archiving.
- [ ] Confirm cron prompt/playbook package targeting no longer includes out-of-scope stacks.
- [ ] Commit cleanup as a dedicated scope-migration commit.
