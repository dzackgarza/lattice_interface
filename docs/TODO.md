# TODO

## Scope Cleanup (Bilinear-Form Lattice Theory Only)

- [x] Create archive folder structure for out-of-scope docs:
  - `docs/archive/`
  - `docs/archive/scope_violations/`
  - `docs/archive/scope_violations/upstream/`
- [x] Add `docs/archive/README.md` explaining that archived content is out of scope for lattice theory in this project (free `R`-modules with symmetric nondegenerate bilinear form).

## Goal 1 Package-Surface Maintenance (Current Phase)

- [x] Perform a cursory in-scope package-surface maintenance check against the current checklist set and upstream map; no clear new bilinear-form lattice package checklist gap was identified in this pass.
- [x] Re-run cursory in-scope package-surface maintenance (2026-02-18): compared active checklist inventory against the upstream living map and current in-scope surfaces; no clear new bilinear-form lattice package checklist gap identified.
- [x] Re-run cursory in-scope package-surface maintenance (2026-02-18, genus-signature pass): checked active in-scope checklist inventory against the upstream map while surveying current Hecke genus manuals; no clear new bilinear-form lattice package checklist gap identified.
- [x] Re-run cursory in-scope package-surface maintenance (2026-02-18, `TorQuadModuleWithIsom` drift pass): reviewed active checklist inventory while reconciling current OSCAR torquad-with-isometry docs; no clear new bilinear-form lattice package checklist gap identified.

## Goal 2 Contract-Fidelity Queue (In-Scope Surfaces)

- [x] Lift crystallographic stack signatures to canonical GAP refs (`chap35` + `chap44`) and triage non-canonical `CrystCat*` aliases in:
  - `docs/crystallographic_stack/lattice/crystallographic_stack_lattice_reference.md`
  - `docs/crystallographic_stack_methods_checklist.md`
  - `docs/crystallographic_stack/upstream/crystallographic_stack_online_provenance_2026-02-17.md`
- [x] Lift accepted value-domain constraints for crystallographic optional selectors (`normedQclass`, `orbitsQclass`) and triage non-canonical `f`/`s`/`k` selectorized CARAT signatures.
- [x] Reconcile GAP umbrella crystallographic signatures with canonical crystallographic-stack contracts in:
  - `docs/gap_methods_checklist.md`
  - `docs/gap/lattice/gap_lattice_methods_reference.md`
- [x] Tighten Julia isometry/isomorphism return-shape contracts and finite-module preconditions in:
  - `docs/julia_methods_checklist.md`
  - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
  - `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md`
  - `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- [x] Reconcile `TorQuadModuleWithIsom` submodule-enumerator signatures with upstream typed docs (remove unsupported `quotype` placeholder) in:
  - `docs/julia_methods_checklist.md`
  - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
  - `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md`
  - `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- [x] Reconcile `TorQuadModuleWithIsom.submodules` keyword-contract drift against current OSCAR docs (`quotype::Vector{Int}=Int[]`, selector values `0..3`) in:
  - `docs/julia_methods_checklist.md`
  - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
  - `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md`
  - `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- [x] Clarify Sage odd-lattice contract fidelity for `TorsionQuadraticModule.is_genus(signature_pair, even=True)` against upstream TODO wording and `genus(signature_pair)` odd-lattice examples in:
  - `docs/sage_methods_checklist.md`
  - `docs/sage/lattice/sagemath_lattice_reference.md`
- [x] Tighten `ZZLatWithIsom.order_of_isometry` contract fidelity (order divisor relation + finite/infinite support wording) in:
  - `docs/julia_methods_checklist.md`
  - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
  - `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md`
  - `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- [x] Tighten Julia genus-constructor signatures and argument constraints (`integer_genera`, `hermitian_genera`, `hermitian_local_genera`) in:
  - `docs/julia_methods_checklist.md`
  - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
  - `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md`
  - `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`

## Move Known Scope-Violation Surfaces to Archive

- [x] Move pycddlib docs (explicit example scope violation):
  - `docs/pycddlib_methods_checklist.md` -> `docs/archive/scope_violations/pycddlib_methods_checklist.md`
  - `docs/pycddlib/lattice/pycddlib_lattice_reference.md` -> `docs/archive/scope_violations/pycddlib/lattice/pycddlib_lattice_reference.md`
  - `docs/pycddlib/upstream/pycddlib_online_provenance_2026-02-17.md` -> `docs/archive/scope_violations/pycddlib/upstream/pycddlib_online_provenance_2026-02-17.md`
- [x] Move cddlib docs:
  - `docs/cddlib_methods_checklist.md`
  - `docs/cddlib/lattice/cddlib_lattice_reference.md`
  - `docs/cddlib/upstream/cddlib_online_provenance_2026-02-17.md`
- [x] Move CddInterface docs:
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
