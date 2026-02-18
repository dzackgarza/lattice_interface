# Doc Coverage Audit Handoff (2026-02-17): OSCAR isometry/discriminant contracts

## Completed work
- Reconciled local docs against current OSCAR stable/dev isometry surfaces for:
  - `QuadSpaceWithIsom`,
  - `ZZLatWithIsom`,
  - `TorQuadModuleWithIsom`.
- Updated `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` with source-backed contract fixes/additions:
  - finite/infinite-order framing for `ZZLatWithIsom`,
  - explicit `order_of_isometry(::QuadSpaceWithIsom)` edge semantics (`PosInf`, rank-zero `-1`),
  - explicit caveat for `quadratic_space_with_isometry(...; check)` default ambiguity in upstream generated docs,
  - added `trace_lattice_with_isometry(H, res)` overload,
  - added typed discriminant-group surface `discriminant_group(TorQuadModuleWithIsom, Lf; ambient_representation=true)`,
  - added `image_in_Oq(Lf)` under discriminant-action methods,
  - clarified `torsion_quadratic_module_with_isometry(T, f; check=true)` action-data breadth,
  - documented upstream `TorQuadModuleWithMap` signature typo caveat for `automorphism_group` page context.
- Updated `docs/julia_methods_checklist.md` to track the same methods/caveats explicitly.
- Added provenance localization file:
  - `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`.

## Key decisions
- Prioritized high-impact indefinite/discriminant-action contracts over generic matrix-level additions.
- Treated upstream default-parameter inconsistency for `check` as a caveat (not as a hard claim) to avoid asserting an unstable default.
- Localized online evidence into an in-repo provenance note rather than only inline links.

## Intentional non-edits
- Did not edit `docs/method_ground_truth_tracker.csv` in this pass because newly documented surfaces here are contract/provenance reconciliation work, and several additions (e.g. `image_in_Oq`, typed discriminant-group overloads) need dedicated method-tagged test provenance before tracker rows can be confidently marked.
- Did not change local upstream snapshot text files (`spacewithisom.md`, `latwithisom.md`, `torquadmodwithisom.md`) beyond using them as reproducible references.

## Remaining high-impact gaps
1. Add explicit checklist/reference coverage for `discriminant_group(::Type{TorQuadModuleWithIsom}, Lf::ZZLatWithIsom)` return-shape contracts with method-tagged test linkage if already available in migrated Julia docs.
2. Add/verify method-level tracking for `image_in_Oq` in static Julia doc tests, then propagate to tracker CSV.
3. Add a small dedicated contract note for `integer_lattice_with_isometry(...; ambient_representation=...)` (meaning of ambient vs lattice representation choice) backed by upstream docs/tests.
4. Audit local/global/rational isometry caveats in §2.8 against latest OSCAR dev docs for drift in definiteness requirements.

## Validation
- Attempted targeted pytest run in Sage env failed due missing `conda` binary in current execution environment.

## Commit
- `9943b6a`