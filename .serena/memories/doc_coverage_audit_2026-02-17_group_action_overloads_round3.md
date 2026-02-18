# Doc Coverage Audit Handoff (2026-02-17): group-action + direct-sum signature drift pass

## Completed work
- Updated `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` with source-backed signature/contract reconciliation for OSCAR isometry-adjacent surfaces:
  - refined group-action sublattice signatures in §2.9:
    - `invariant_lattice(::ZZLat, ::MatGroup)`
    - `coinvariant_lattice(::ZZLat, ::MatGroup)`
    - added missing `invariant_coinvariant_pair(::ZZLat, ::Union{QQMatrix, Vector{QQMatrix}, MatGroup})`
  - corrected `direct_sum` method surfaces in §2.13 and §2.14 from vector-only shorthand to current upstream vararg+vector signatures:
    - `direct_sum(Vf::Union{QuadSpaceWithIsom, Vector{QuadSpaceWithIsom}}...)`
    - `direct_sum(Lf::Union{ZZLatWithIsom, Vector{ZZLatWithIsom}}...)`
  - added binary-output embedding-map caveat for these `direct_sum` methods.
  - clarified `fingrpact`-derived contracts in §2.17:
    - `is_isometry_group` helper is non-exported (input-check utility context),
    - `extend_to_ambient_space` / `restrict_to_lattice` as basis-representation conversion between lattice and ambient coordinates for collections of isometries.
- Updated `docs/julia_methods_checklist.md` to mirror the same method-surface and caveat corrections (no checkbox state changes).
- Extended `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md` with pass-13 evidence links and contract deltas, including:
  - dev/v1 manual index URLs,
  - release-notes corroboration,
  - vararg+vector `direct_sum` signatures,
  - group-action `invariant_coinvariant_pair` distinction and `fingrpact` utility framing.

## Key decisions
- Prioritized mathematically relevant interface-contract fidelity over broad wording churn.
- Used exact runtime-style signatures where upstream evidence is explicit, avoiding speculative over-typing for stabilizer methods whose detailed signature blocks were not retrievable from cached online pages.
- Kept updates cohesive across reference + checklist + provenance surfaces.

## Intentional non-edits
- Did not modify `docs/method_ground_truth_tracker.csv` in this pass; this was signature/contract reconciliation without new method-tagged test linkage.
- Did not touch unrelated dirty files (`docs/documentation_coverage_audit_playbook.md`, `prompt.md`, `scripts/doc_coverage_scheduler.py`, etc.).
- Did not alter local upstream snapshot content files (`fingrpact.md`, `latwithisom.md`, `spacewithisom.md`), only consumed them as evidence.

## Remaining high-impact gaps
1. Signature-level reconciliation for the `stabilizer_*` family remains partially generic in checklist/reference tables; exact typed signatures should be lifted from canonical upstream docs/source once page/source access is available.
2. Add explicit method-level reconciliation for `extend_to_ambient_space`/`restrict_to_lattice` argument-type surfaces (single matrix vs vector vs matrix-group inputs).
3. Bridge newly reconciled methods to method-tagged Julia doc tests and then propagate to `docs/method_ground_truth_tracker.csv`.
4. Re-check OSCAR docs after next regeneration for the `collections of isometries` page accessibility drift and potential new group-action methods.

## Validation
- `just test` failed in this environment: `just: command not found`.
- Targeted Sage pytest command failed in this environment: `conda: command not found`.

## Commit
- `6e24628`