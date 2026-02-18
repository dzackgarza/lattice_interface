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
- counting/enumeration stacks (for example Ehrhart/lattice-point pipelines) that do not operate on symmetric nondegenerate bilinear-form lattices.

## FIRST GOAL (MANDATORY)

Ensure checklist coverage exists for all known relevant in-scope bilinear-form lattice packages in the ecosystem.
If a known in-scope package lacks a checklist surface in this repository, creating that checklist surface is the first priority.

## SECOND GOAL (MANDATORY)

Completeness and provable correctness of all documented methods:

- method coverage,
- argument surfaces,
- types,
- assumptions and constraints.

If any of the above is missing or unsupported for any method, triage that gap immediately.

Scope gate for every assignment:

- before adding or expanding any package surface, verify that the package has explicit APIs for free-module lattices with symmetric nondegenerate bilinear forms.
- if it does not, treat it as out-of-scope and do not prioritize or expand it as a lattice-theory target.

## MINOR GOAL (ONLY AFTER FIRST AND SECOND GOALS ARE CLEARLY SATISFIED)

Precision/clarity refinement work, including:

- fine-tuning wording,
- disambiguation,
- structural polish.

## What The Docs Are Supposed To Be

- Source-backed coverage of all in-scope bilinear-form lattice methods and contracts known in the active ecosystem.
- Mathematically correct and explicit contracts, assumptions, domains, and caveats.
- Clear organization and navigation across checklists and detailed references.
- Durable continuity and handoffs for future workers.

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

- Serena is the primary continuity and handoff system:
  - activate project,
  - read relevant memories,
  - write/update memories with decisions, remaining gaps, and follow-up tasks.
- `docs/TODO.md` is the outstanding work queue:
  - review it at the start of each assignment,
  - execute relevant in-scope open items,
  - mark completed items as checked (`- [x]`) in the same assignment.
- Git is the change ledger:
  - commit documentation changes produced by the assignment.
- Dirty git states are normal:
  - never discard/revert/reset/checkout unrelated existing changes,
  - never run destructive repo-wide cleanup,
  - stage and commit only files changed by the assignment.

### Network Bailout Contingency (Mandatory)

- If a known/canonical upstream URL is discovered via web results but direct shell retrieval fails (for example `curl` DNS/TLS/connectivity failure), do not keep looping broad web searches.
- Retry the same URL a small fixed number of times (`<=2`) and record the exact failing command + error output in provenance/handoff notes.
- Treat this as an environment access failure, not proof that upstream docs do not exist.
- Earmark the blocked source task for explicit future follow-up with:
  - URL(s),
  - UTC timestamp,
  - observed error class (`dns`, `timeout`, `tls`, etc.),
  - exact remaining method-surface gap.
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
- `docs/cddinterface_methods_checklist.md`
- `docs/nconvex_methods_checklist.md`
- `docs/forms_methods_checklist.md`
- `docs/hypercells_methods_checklist.md`
- `docs/4ti2_methods_checklist.md`
- `docs/normaliz_methods_checklist.md`
- `docs/flint_methods_checklist.md`
- `docs/fplll_methods_checklist.md`
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
- fplll / fpylll:
  - `https://github.com/fplll/fplll`
  - `https://github.com/fplll/fpylll`
- NTL:
  - source/docs: `https://libntl.org`
- FLINT:
  - source: `https://github.com/flintlib/flint`
  - docs: `https://flintlib.org/doc/`
- 4ti2:
  - docs hub: `https://4ti2.github.io`
- Normaliz:
  - source: `https://github.com/Normaliz/Normaliz`
  - docs: `https://www.normaliz.uni-osnabrueck.de`
- PARI/GP:
  - `https://pari.math.u-bordeaux.fr`
