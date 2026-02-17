# Documentation Coverage Audit Playbook

## Scope (Narrow and Non-Negotiable)

This playbook is only for documentation auditing, documentation completion, and documentation organization.

It is not for:

- implementing code,
- changing runtime behavior,
- changing test semantics,
- forcing green CI by narrowing scope,
- checking boxes in checklists.

The sole output target is higher-integrity documentation coverage for lattice-theoretic methods across the research ecosystem.

## Execution Contract

- [ ] Work only on documentation auditing, completion, and organization.
- [ ] Do as much in-scope work as needed to produce a real quality improvement.
- [ ] If no positive-gradient edit exists, record a no-edit pass and stop.
- [ ] Always leave explicit follow-up tasks for future passes.

## Hard Constraints

- [ ] Never check off checklist items in this playbook or in top-level method checklists.
- [ ] Never use alias-crediting/token-map shortcuts to claim coverage.
- [ ] Never hide missing methods by narrowing scope or expanding ignore lists.
- [ ] Never weaken mathematically precise text into vague language.
- [ ] Never treat reword-only churn as progress.

## Canonical Inputs

- [ ] `README.md`
- [ ] `TEST_QUALITY.md`
- [ ] `AGENTS.md`
- [ ] `docs/sage_methods_checklist.md`
- [ ] `docs/julia_methods_checklist.md`
- [ ] `docs/lattice_wrapper_capability_checklist.md`
- [ ] `docs/method_ground_truth_tracker.csv`
- [ ] Source manifests and local upstream snapshots (for example `docs/sage/SOURCES.md`, `docs/*/upstream/*`)

## Deterministic Preflight (Required, Non-Blocking)

Run in this order before any edit:

- [ ] `git status --short`
- [ ] `git log --oneline -- docs | head -n 20`
- [ ] `date -u +"%Y-%m-%d %H:%M:%S UTC"`
- [ ] If the tree is dirty, continue with a docs-only pass and record the pre-existing dirty state in the changelog.
- [ ] If required inputs are missing, continue by documenting the missing inputs as top-priority follow-up tasks.

## Target Selection (Deterministic)

Start with this priority:

- [ ] Highest-severity unresolved gap from previous post-pass "Remaining gaps".
- [ ] Highest-priority handoff task from the latest changelog post-pass entry.
- [ ] If none, choose next ecosystem by round-robin order:
`sage -> julia -> gap -> fpylll -> pari_gp -> latticegen -> cross-ecosystem`.
- [ ] If multiple equivalent targets remain, choose lexicographically smallest checklist file path.

Expand beyond the initial target only when it improves clarity and remains within doc-audit scope.

## Pass Loop (Repeat Until Fixed Point)

- [ ] Review current docs coverage surfaces (Sage, Julia/Oscar/Hecke, GAP, fpylll, PARI/GP, latticegen, and other in-repo ecosystems).
- [ ] Enumerate all lattice-theoretic method families expected in active research workflows.
- [ ] Diff expected families against currently documented methods/checklists.
- [ ] Classify each gap: missing method, duplicate method, unclear contract, stale claim, unsupported claim, or organization defect.
- [ ] Propose edits that strictly improve coverage integrity and mathematical precision.
- [ ] Reject edits that are net-zero or negative gradient (see "No-Edit Conditions").
- [ ] Apply approved doc edits.
- [ ] Append post-pass changelog entry with outcomes and remaining gaps.
- [ ] Re-run one more read-only audit pass to verify no new inconsistencies were introduced.

Operationalization:

- [ ] Keep edit scope tight and intentional.
- [ ] Before finalizing, run `git diff -- docs` and confirm every changed file is documentation.
- [ ] If diff includes non-doc files, revert those non-doc changes and record incident in post-pass notes.

## Fixed-Point Stop Condition

Stop only when all are true:

- [ ] No newly discovered lattice-theoretic method families remain undocumented in top-level checklists.
- [ ] No checklist item has ambiguous mathematical contract text.
- [ ] No source-backed claim lacks provenance to local snapshot or canonical online source.
- [ ] No organizational duplication causes contradictory method status.
- [ ] A fresh audit pass produces no high-signal edits.

## Git Workflow (Docs-Only)

- [ ] Start each pass by reviewing current branch state with `git status` and recent doc history with `git log -- docs`.
- [ ] Create small, reviewable commits per audit pass.
- [ ] Keep commit scope doc-only unless explicitly authorized otherwise.
- [ ] Use commit messages that encode pass intent and result (audit/add/clarify/reconcile).
- [ ] Avoid mixing unrelated ecosystems in one commit when it reduces review clarity.

Commit guidance:

- [ ] Commit docs changes from this pass, including changelog/handoff updates.
- [ ] If no doc content changed, still record pass results in changelog/handoff.
- [ ] Preferred commit format:
`docs(audit): pass <PASS_ID> <target> <audit|add|clarify|reconcile>`

## Changelog Protocol (Required Before and After Each Pass)

Maintain `docs/project/doc_coverage_audit_changelog.md` and enforce this sequence:

- [ ] Add a **Pre-Pass Entry** before editing.
- [ ] Review and approve pre-pass intent against scope and no-edit rules.
- [ ] Perform the pass.
- [ ] Add a **Post-Pass Entry** immediately after editing.
- [ ] Add explicit handoff tasks for the next agent inside the post-pass entry.

Required entry fields (both pre and post):

- [ ] Date/time (UTC) and pass ID.
- [ ] Target ecosystems/modules.
- [ ] Planned/actual method families touched.
- [ ] Rationale for every substantive edit.
- [ ] Explicit list of edits intentionally not made (with reason).
- [ ] Net quality gradient: positive/zero/negative with justification.
- [ ] Remaining risks/gaps.

Chronological rule:

- [ ] Pass entries must be append-only and strictly time-ordered.
- [ ] Never edit old pass bodies except to fix factual logging mistakes; if corrected, add a correction note in a new pass.

## Local Copies of Online Docs (When Required)

Add local upstream snapshots when any of the following is true:

- [ ] A checklist method references an online page not already snapshotted locally.
- [ ] Existing local snapshot is missing sections needed for method-level verification.
- [ ] Upstream docs changed and current local copy is stale for current audit claims.

Snapshot rules:

- [ ] Save under ecosystem/module `upstream/` folders using stable filenames.
- [ ] Record canonical URL and fetch date in source manifest (`SOURCES.md` or equivalent).
- [ ] Prefer official documentation/source pages over secondary summaries.
- [ ] Do not claim method coverage from memory when a local snapshot is feasible.

Freshness rule:

- [ ] If targeted source snapshot metadata is older than 90 days, schedule refresh in the same pass when feasible; otherwise record explicit deferral reason in post-pass notes.

## Top-Level Checklist Quality Rules

- [ ] Keep method entries at top-level checklist granularity (clean scan-first structure).
- [ ] Use exact runtime method names and signatures when practical.
- [ ] Include caveats for definiteness/domain/algorithmic constraints.
- [ ] Split overloaded or semantically distinct methods into separate bullets when needed.
- [ ] Keep each checklist as an auditable inventory, not a narrative essay.
- [ ] Preserve unchecked boxes; audit tracks status in changelog, not by checking items.

Formatting guard:

- [ ] Keep checklist edits line-stable where possible (surgical additions/clarifications) to preserve diff auditability.

## No-Edit Conditions (Edit Is Not Warranted)

Do not edit when:

- [ ] Proposed text only rephrases wording without improving mathematical precision.
- [ ] Proposed simplification removes constraints/caveats required for correctness.
- [ ] Proposed consolidation obscures method-level accountability.
- [ ] Proposed deletion removes provenance links without replacing them.
- [ ] Proposed expansion adds speculative methods unsupported by canonical sources.
- [ ] Proposed organization change increases reviewer search cost or ambiguity.
- [ ] Proposed reordering changes many lines without increasing coverage precision.
- [ ] Proposed edit cannot be tied to a specific documented gap category.

Mark these as "intentional non-edits" in the pass changelog.

## Research-Ecosystem Completeness Standard

For this playbook, "accounted for" means every known lattice-theoretic method in scope is one of:

- [ ] Explicitly listed in a top-level checklist with a mathematically meaningful description/caveat, or
- [ ] Explicitly marked out-of-scope as non-lattice infrastructure with source-backed rationale.

No third state is allowed.

## Review Output per Pass

Each pass must produce:

- [ ] Updated docs (if positive-gradient edits existed), and
- [ ] Updated pre/post changelog entries, and
- [ ] A concise unresolved-gaps list for the next pass, and
- [ ] Explicit queued handoff tasks in the post-pass changelog entry.

If no positive-gradient edits exist, the pass still records a no-edit post-pass entry and fixed-point evidence.

## Drift Prevention Rules

- [ ] Every pass must either close one documented gap or sharpen one method contract/caveat with source backing.
- [ ] A pass that does neither is `zero` gradient and must not alter checklists beyond minimal logging artifacts.
- [ ] Re-audit each ecosystem at least once every 6 completed passes; if skipped, force it as the next target.
- [ ] Keep "remaining gaps" actionable (method family + file path + reason), never generic.

## Handoff Tasks (Required)

Store handoff tasks only in changelog post-pass entries.

- [ ] Include only actionable tasks with exact file path and gap category.
- [ ] Each task must have a short acceptance condition.
- [ ] Keep tasks concise and prioritized for the next pass.
