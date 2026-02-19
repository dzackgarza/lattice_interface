# Doc Coverage Audit Handoff (2026-02-19): `is_isometric` / `is_isometric_with_isometry` definiteness constraint

## FIRST GOAL (cursory package-surface maintenance)
- Brief in-scope package-surface maintenance check completed; no new bilinear-form lattice package surface gap identified requiring a new checklist.

## SECOND GOAL (active phase focus)
- Corrected source-backed contract-fidelity error in Julia lattice isometry test methods.
- Previous documentation tagged `is_isometric(L1, L2)` and `is_isometric_with_isometry(L1, L2)` as `[PD]` (positive definite only).
- Source verification via Hecke.jl source code (`src/QuadForm/Lattices.jl`) shows:
  - Implementation explicitly rescales ND to PD: `if ZgramL[1][1, 1] < 0: ZgramL[1] = -ZgramL[1]`
  - Upstream requirement is `is_definite(L)`, supporting both positive and negative definite lattices
  - Only indefinite lattices are excluded from isometry testing

## Completed edits

1. `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (§2.8)
   - Changed `[PD]` → `[DEFINITE]` for both `is_isometric(L1, L2)` and `is_isometric_with_isometry(L1, L2)`
   - Added explicit description: "upstream requires `is_definite(L1)` and `is_definite(L2)` (positive or negative definite); uses LLL to rescale ND to PD before comparison"

2. `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md` (§2.7)
   - Changed `[PD, NT]` → `[DEFINITE, NT]` for both methods
   - Added same explicit description as above

3. `docs/julia_methods_checklist.md` (§2.8)
   - Added caveat to both `is_isometric` entries documenting the definiteness requirement
   - Clarified that LLL rescaling handles ND lattices

4. `docs/TODO.md`
   - Added and checked off Goal 2 contract-fidelity item for this pass

## Source evidence
- Hecke.jl source: `src/QuadForm/Lattices.jl`
  - `is_isometric` docstring: no explicit definiteness constraint stated in docs
  - Implementation: rescaling logic `if ZgramL[1][1, 1] < 0` confirms ND support
  - Upstream `automorphism_group_generators` / `automorphism_group_order` explicitly state "Given a definite lattice L"

## Commit
- `fc23d1b` — docs: correct is_isometric definiteness constraint from [PD] to [DEFINITE]

## Validation
- Documentation-only pass; no runtime tests executed.

## Intentional non-edits
- Did not modify unrelated pre-existing dirty files:
  - `README.md`, `docs/documentation_coverage_audit_playbook.md`, `prompt.md`, `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`, `agent_runner/` logs

## Pattern note (for future workers)
This is the **third** instance of the same `[PD]` vs `[DEFINITE]` error pattern in this project:
- Pass 1: Sage `IntegralLattice.orthogonal_group` — `[PD]` → `[DEFINITE]`
- Pass 2: Julia/OSCAR `automorphism_group_generators` / `automorphism_group_order` — `[PD]` → `[DEFINITE]`
- Pass 3 (this pass): Julia/OSCAR `is_isometric` / `is_isometric_with_isometry` — `[PD]` → `[DEFINITE]`

Continue checking other `[PD]`-tagged methods where upstream may actually say "definite" (not "positive definite"). The definitive source is checking the actual implementation code in Hecke.jl / SageMath source.

## Remaining high-impact gaps
1. Continue Goal 2 contract-fidelity tightening for other `[PD]`-tagged methods that may actually support negative definite lattices.
2. Missing local doc copies still open in TODO.md (flint, gap, ntl, fpylll, forms, g6k, crystallographic_stack, pari_gp).
3. Many unchecked method entries in Julia checklist (§2.3, §2.4, §2.9, §2.14).
