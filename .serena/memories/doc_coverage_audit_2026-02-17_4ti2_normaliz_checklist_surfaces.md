# Doc Coverage Audit Handoff (2026-02-17): 4ti2 + Normaliz checklist surface expansion

## Objective addressed
- FIRST GOAL: create checklist coverage surfaces for known lattice-method packages that were not yet represented as first-class top-level checklists.
- SECOND GOAL (triage level): add source-backed command/method signatures and core constraints/caveats for those new package surfaces.

## Completed work
- Added new first-class checklist + detailed reference surfaces for:
  - `4ti2`
    - `docs/4ti2_methods_checklist.md`
    - `docs/4ti2/lattice/4ti2_lattice_reference.md`
  - `Normaliz`
    - `docs/normaliz_methods_checklist.md`
    - `docs/normaliz/lattice/normaliz_lattice_reference.md`
- 4ti2 surface now includes explicit command families:
  - cone/solver: `circuits`, `rays`, `qsolve`, `zsolve`, `zbasis`
  - lattice-ideal/Groebner: `hilbert`, `graver`, `groebner`, `markov`, `minimize`, `normalform`, `walk`
  - support tools: `genmodel`, `gensymm`, `output`, `ppi`
  - documented caveat: homogeneous restrictions in current `qsolve` workflow (manual-backed).
- Normaliz surface now includes explicit interfaces:
  - CLI: `normaliz <project>` plus goal/option forms (`--HilbertBasis`, `--SupportHyperplanes`, `--HilbertSeries`, `--OutputDir`, help/version)
  - PyNormaliz: `Cone(...)`, `Compute`, `IsComputed`, Hilbert basis/series, lattice-point/volume, support-hyperplane APIs, `NmzResult`
  - GAP NormalizInterface wrappers: `NmzCone`, `NmzCompute`, `NmzConeProperty`, property-introspection and selected alias properties
  - documented caveats: project-input rules, string-encoded algebraic/floating outputs in wrapper layers, version-linked alias availability.
- Updated `docs/documentation_coverage_audit_playbook.md` references/living-map to include newly added package checklist surfaces and already-present NTL/FLINT/fplll checklist baselines.

## Sources used
- 4ti2 docs index/manual:
  - `https://4ti2.github.io/toc.html`
  - `https://4ti2.github.io/4ti2_manual.pdf`
  - `https://4ti2.github.io/h.html`
- Normaliz + wrappers:
  - `https://github.com/Normaliz/Normaliz`
  - `https://github.com/Normaliz/PyNormaliz`
  - `https://docs.gap-system.org/pkg/normalizinterface/doc/chap2_mj.html`
  - `https://sources.debian.org/src/normaliz/3.10.4%2Bds-1/doc/Options.tex`

## Commit
- `8e41a12` — docs: add 4ti2 and normaliz checklist surfaces

## Validation
- Verified git staging/commit includes only assignment docs files.
- Did not alter pre-existing unrelated dirty/untracked files (`scripts/doc_coverage_scheduler.py`, `.serena/`, `scripts/__pycache__/`).
- No runtime/test execution attempted (documentation-surface pass).

## Remaining high-impact gaps
1. Evaluate whether additional standalone package surfaces should be elevated from GAP-package-only representation to first-class checklists (for example cddlib-facing and toric/polyhedral stacks) when source-stable method inventories are confirmed.
2. Build `method:`-tagged tests for high-impact new 4ti2/Normaliz entries before any checklist checkmarks.
3. Add deeper per-command argument-contract tables (input file extension requirements and option interactions) from upstream manuals to tighten signature fidelity.