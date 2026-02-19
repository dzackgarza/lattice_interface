# Documentation Coverage Audit Playbook

## Role

Documentation worker for this mathematics project.

## Job

Bring the current documentation into alignment with what the project documentation is supposed to be.

## Scope Definition (Mandatory)

For this project, "lattice theory" is strictly:

- free `R`-modules of finite rank,
- equipped with a symmetric nondegenerate bilinear form,
- and method surfaces that explicitly operate on that structure (for example: Gram/form operations, discriminant forms/groups, genus/spinor genus, local-global invariants, isometry/equivalence, signature, integral quadratic form workflows).

Out of scope unless explicit bilinear-form lattice APIs are present:

- polyhedral/cone/H-V representation tooling,
- (semi)linear programming and generic optimization stacks,
- toric/fan/polytope pipelines,
- counting/enumeration stacks (for example Ehrhart/lattice-point pipelines) that do not operate on symmetric nondegenerate bilinear-form lattices,
- packages using "lattice" in the physics sense (periodic atomic arrangements, moiré patterns) without bilinear-form structure.

## In-Scope Package Registry

Every package with a checklist in this repository and the mathematical reason it is in scope:

| Package | Scope justification |
|---------|---------------------|
| SageMath | Integral/rational lattice constructors, Gram/discriminant/genus/isometry APIs, quadratic forms over ℤ |
| Oscar.jl / Hecke.jl / Nemo.jl | ℤ-lattice constructors, bilinear-form operations, genus/isometry/automorphism APIs |
| GAP (core) | Integer-matrix normal forms (HNF/SNF), lattice-relevant matrix algebra |
| Forms (GAP) | Sesquilinear and quadratic forms on free modules over finite fields — direct instances of R-modules with bilinear forms |
| HyperCells (GAP) | Triangle-group tessellations as fundamental domains of reflection groups acting on $L \otimes \mathbf{R}$, tied to indefinite bilinear-form lattice structure |
| Crystallographic stack (GAP) | Crystallographic groups as subgroups of $O(L)$, operating on lattices via their bilinear form |
| fpylll | LLL/BKZ/SVP/CVP algorithms on Euclidean lattices with inner-product (bilinear-form) structure (Python interface to fplll) |
| g6k | Sieving algorithms for SVP/BKZ on Euclidean lattices with inner-product structure |
| flatter | Lattice basis reduction operating on bilinear-form structure |
| FLINT | Integer-matrix reduction and normal-form algorithms (HNF/SNF/LLL) on ℤ-modules |
| NTL | Integer-matrix LLL and normal-form algorithms on ℤ-modules |
| PARI/GP | Explicit `qf*` quadratic-form APIs: reduction, equivalence, genus, representation |

Out of scope (documented but not tracked for checklist completion):

| Package | Reason |
|---------|--------|
| fplll | C++ backend; superseded by fpylll as the project's interface surface |
| latticegen (fplll utility) | Benchmark instance generator with no bilinear-form API surface; covered by fpylll checklist |
| latticegen (Python/moiré) | Physics "lattice" (periodic image patterns), not bilinear-form lattice |

## FIRST GOAL (MANDATORY)

Ensure checklist coverage exists for all known relevant in-scope bilinear-form lattice packages in the ecosystem.

**CRITICAL PREREQUISITE**: Before checklist entries can be filled with source-backed accuracy, local copies of upstream documentation must exist under `docs/**/upstream/`. Without these local snapshots:
- Method signatures cannot be verified against actual source
- Argument contracts cannot be backed by cited documentation  
- The checklist completeness assessment is meaningless

If a known in-scope package lacks both:
1. A checklist surface in this repository, AND
2. Local upstream doc copies under `docs/**/upstream/`

Then creating that checklist surface AND integrating the local doc copies are co-equal first priorities.

Track specific package status in `docs/TODO.md` — do not litter this playbook with rotting timestamps and package lists.

## SECOND GOAL (MANDATORY)

**Prerequisite**: Goal 1 is NOT complete until local doc copies are integrated for all in-scope packages. Do not proceed to Goal 2 work until the local doc prerequisite is demonstrably met.

Completeness and provable correctness of all documented methods:

- method coverage,
- argument surfaces,
- types,
- assumptions and constraints.

If any of the above is missing or unsupported for any method, triage that gap immediately.

Scope gate for every assignment:

- before adding or expanding any package surface, verify that the package has explicit APIs for free-module lattices with symmetric nondegenerate bilinear forms.
- if it does not, treat it as out-of-scope and do not prioritize or expand it as a lattice-theory target.

## MINOR GOAL (STRICTLY CONDITIONAL - ONLY AFTER FIRST AND SECOND GOALS ARE VERIFIABLY COMPLETE)

Precision/clarification refinement work, including:

- fine-tuning wording,
- disambiguation,
- structural polish.

**This goal does NOT exist until FIRST and SECOND goals are demonstrably complete.** An agent treating this as an acceptable alternative to the mandatory goals has failed the assignment.

## What The Docs Are Supposed To Be

- Source-backed coverage of all in-scope bilinear-form lattice methods and contracts known in the active ecosystem.
- Mathematically correct and explicit contracts, assumptions, domains, and caveats.
- Clear organization and navigation across checklists and detailed references.

**CHECKLIST FILES (docs/*_methods_checklist.md) TRACK TEST COVERAGE - THAT IS A SEPARATE TASK. DO NOT MIX TEST COVERAGE WITH DOCUMENTATION COMPLETION.**

## When The Task Is Incomplete (Always)

**The task is incomplete if ANY of the following are true:**

1. There exists an in-scope package without integrated local upstream docs under `docs/**/upstream/`.
2. There exists an in-scope package whose reference doc lacks full typed signatures for any method.
3. Any reference entry lacks a cited local doc source for its documented signature and constraints.

**This is an ALL-OR-NOTHING criterion.** The existence of any gap, no matter how small, means the task is incomplete. Do not describe partial progress as completion.

**Do NOT attempt to verify all items before working.** These conditions will not be false for the foreseeable future. The correct response to finding them is to pick a gap and fix it — not to assert whether the conditions hold.

## Quality Questions

Treat these as project-wide values to assess continuously:

- Are there online packages/docs with lattice algorithms not yet represented in the documentation surfaces?
- Are candidate packages truly in scope, i.e. do they explicitly implement lattices as free modules with symmetric nondegenerate bilinear forms?
- Do the docs clearly help a human understand what methods/tools are available and when to use them?
- Is the current organization cohesive and easy to navigate across checklists and detailed references?
- Do older docs need restructuring/reorganization to improve mathematical clarity or discoverability?
- Did any edit remove mathematically relevant information?
- Did the git diff actually improve quality against these questions?
- Were edits grounded in real source documents/snapshots rather than assumptions or innate knowledge?
- Were any mathematical assumptions introduced that are not clearly evidenced in source docs?
- Were critical assumptions omitted (for example, positive-definite-only or ring/domain constraints)?
- Were differing definitions/assumptions of lattices across sources reconciled where needed?
- Were restrictions, assumptions, constraints, or authoritative statements introduced without clear source evidence?
- Is language anywhere in the touched documentation surface vague or mathematically imprecise?
- Are improvements grounded in checkable/provable statements?
- Were vague claims introduced (`usually`, `typically`, `often`, `most of the time`) where exact truth values are available?
- Were weak deferrals left in place (`unknown`, `unverified`, `needs testing`) where questions are reasonably answerable through docs/source/web research?
- Did this assignment improve project-wide alignment to complete known-method coverage, rather than only local wording?
- Did this assignment avoid expanding out-of-scope polyhedral/LP/toric/counting stacks that do not expose bilinear-form lattice APIs?

## Process Guidelines

- Serena memories are for actionable insight only — not summaries of completed work, changelogs, or handoff notes. Write a memory only if it contains something a future agent genuinely needs to act on (e.g. a source URL that is unreachable, a constraint that is non-obvious and would otherwise be wrong, an upstream discrepancy that needs resolution). Do not write memories that describe what you did.
- `docs/TODO.md` is the outstanding work queue:
  - review it at the start of each assignment,
  - execute relevant in-scope open items.
- Git is the change ledger:
  - commit documentation changes produced by the assignment.
  - push those commits after completion, using `GITHUB_TOKEN` from `.env`.
- Dirty git states are normal:
  - never discard/revert/reset/checkout unrelated existing changes,
  - never run destructive repo-wide cleanup,
  - stage, commit, and push only files changed by the assignment.

### Network Bailout Contingency (Mandatory)

- If a known/canonical upstream URL is discovered via web results but direct shell retrieval fails (for example `curl` DNS/TLS/connectivity failure), do not keep looping broad web searches.
- Retry the same URL a small fixed number of times (`<=2`).
- Treat this as an environment access failure, not proof that upstream docs do not exist.
- If a source is genuinely unreachable and the gap is actionable for a future agent, write a Serena memory with the URL and the specific method-surface gap it would fill.
- Then pivot the same run to substantial offline work (not meta-only churn), such as:
  - improving source-backed contracts from local snapshots under `docs/**/upstream/`,
  - correcting invalid/broken links and provenance mismatches,
  - tightening argument/type/constraint tables for already available packages,
  - reconciling checklist/reference consistency using existing local evidence.

## References

Core repository references:

- `README.md`
- `AGENTS.md`
- `TEST_QUALITY.md`
- `docs/sage_methods_checklist.md`
- `docs/julia_methods_checklist.md`
- `docs/gap_methods_checklist.md`
- `docs/forms_methods_checklist.md`
- `docs/hypercells_methods_checklist.md`
- `docs/flint_methods_checklist.md`
- `docs/fpylll_methods_checklist.md`
- `docs/ntl_methods_checklist.md`
- `docs/pari_gp_methods_checklist.md`
- `docs/latticegen_methods_checklist.md`
- `docs/lattice_wrapper_capability_checklist.md`
- `docs/method_ground_truth_tracker.csv`
- local upstream snapshots under `docs/**/upstream/`

Upstream living map:

- SageMath:
  - source: `https://github.com/sagemath/sage`
  - docs: `https://doc.sagemath.org`
- Oscar.jl:
  - source: `https://github.com/oscar-system/Oscar.jl`
  - docs: `https://docs.oscar-system.org`
- Hecke.jl:
  - source: `https://github.com/thofma/Hecke.jl`
  - docs: `https://docs.hecke.thofma.com`
- Nemo.jl (official):
  - source: `https://github.com/Nemocas/Nemo.jl`
  - docs: `https://nemocas.github.io/Nemo.jl/stable/`
- AbstractAlgebra.jl:
  - source: `https://github.com/Nemocas/AbstractAlgebra.jl`
  - docs: `https://nemocas.github.io/AbstractAlgebra.jl/stable/`
- GAP:
  - source: `https://github.com/gap-system/gap`
  - docs hub: `https://www.gap-system.org/doc/`
  - package docs/index: `https://gap-packages.github.io`
- HyperCells (GAP package):
  - package page: `https://gap-packages.github.io/HyperCells/`
  - manual: `https://www.hypercells.net/chap0_mj.html`
- CddInterface (GAP package):
  - package page: `https://homalg-project.github.io/CddInterface/`
  - manual: `https://homalg-project.github.io/CddInterface/doc/chap0_mj.html`
- NConvex (GAP package):
  - package page: `https://homalg-project.github.io/NConvex/`
  - source: `https://github.com/homalg-project/NConvex`
- Forms (GAP package):
  - package page: `https://gap-packages.github.io/forms/`
  - manual: `https://gap-packages.github.io/forms/doc/chap0_mj.html`
- fpylll (Python interface to fplll):
  - `https://github.com/fplll/fpylll`
- NTL:
  - source/docs: `https://libntl.org`
- FLINT:
  - source: `https://github.com/flintlib/flint`
  - docs: `https://flintlib.org/doc/`
- PARI/GP:
  - `https://pari.math.u-bordeaux.fr`
