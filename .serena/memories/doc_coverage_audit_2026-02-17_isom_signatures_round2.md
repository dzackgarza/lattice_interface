# Doc Coverage Audit Handoff (2026-02-17): `with_isometry` signature/contract reconciliation (round 2)

## Completed work
- Reconciled method-surface signatures and contract caveats for Julia OSCAR `QuadFormAndIsom` docs in:
  - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
  - `docs/julia_methods_checklist.md`
  - `docs/julia/oscar_jl/number_theory/quad_form_and_isom/isom_online_provenance_2026-02-17.md`
- Added/clarified high-impact missing method surfaces not previously represented precisely:
  - vector-style direct sums:
    - `direct_sum(::Vector{QuadSpaceWithIsom})`
    - `direct_sum(::Vector{ZZLatWithIsom})`
  - ambient-construction overload:
    - `lattice(::QuadSpaceWithIsom, ::MatElem{<:RationalUnion})`
  - `integer_lattice_with_isometry(...; ambient_representation=...)` representation-basis semantics.
- Corrected isometry-action signatures that were previously mis-modeled in local docs:
  - `is_stable_isometry(::ZZLatWithIsom)`
  - `is_special_isometry(::ZZLatWithIsom)`
  - `special_subgroup(::ZZLat, ::MatGroup)`
  - `stable_orthogonal_group(::ZZLat)` / `stable_subgroup(::ZZLat, ::MatGroup)`
  - `maximal_extension(::ZZLat, ::ZZLat, ::MatGroup)`
  - `saturation(::ZZLat, ::MatGroup, ::MatGroup)` and `saturation(::ZZLat, ::MatGroup)` with precondition caveats.
- Tightened enumeration machinery signatures to exact method surfaces:
  - `admissible_triples(::ZZGenus, ::Int)`
  - `is_admissible_triple(::ZZGenus, ::ZZGenus, ::ZZGenus, ::Int)`
  - `splitting(::ZZLatWithIsom, ::Int, ::Int)` and prime-power split variants.
- Expanded constructor caveat for `torsion_quadratic_module_with_isometry` action-data breadth (`TorQuadModuleMap`, `FinGenAbGroupHom`, `ZZMatrix`, `MatGroupElem`).
- Localized provenance updates with stable/dev/v1 links used for signature drift checks.

## Key decisions
- Prioritized exact runtime signature fidelity over abbreviated pseudo-signatures in checklist/reference surfaces.
- Preserved mathematically meaningful caveats where method availability depends on definiteness/coinvariant constraints.
- Kept updates confined to documentation surfaces (no runtime/test-surface modifications).

## Intentional non-edits
- Did not modify `docs/method_ground_truth_tracker.csv` in this pass because this was contract/signature reconciliation, not new method-test linkage work.
- Did not alter local upstream snapshot text files besides referencing them in provenance.
- Did not modify unrelated dirty files (`docs/documentation_coverage_audit_playbook.md`, `prompt.md`, `scripts/doc_coverage_scheduler.py`, etc.).

## Remaining high-impact gaps
1. Add explicit signature-level reconciliation for `fingrpact` stabilizer methods where local checklist still uses shortened symbolic forms (e.g., untyped `stabilizer_*` forms).
2. Add method-tagged test provenance linkage for newly clarified overloads (`lattice(::QuadSpaceWithIsom, B)`, vector `direct_sum`, saturation overloads) and then propagate into `docs/method_ground_truth_tracker.csv` rows where applicable.
3. Re-audit stable/dev/v1 drift on `QuadFormAndIsom` once OSCAR stable regenerates pages for current releases; current online trees show version-surface divergence.

## Validation
- `just test` could not run in this environment (`just: command not found`).
- Targeted Sage command could not run in this environment (`conda: command not found`).

## Commit
- `5bbf1eb`