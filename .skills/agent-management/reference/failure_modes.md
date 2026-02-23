# Agent Management Reference

## Failure Modes Reference Table

| Failure Mode | Transcript Symptoms | Structural Cause | Fix Pattern |
|-------------|---------------------|-----------------|-------------|
| **State Drift** | Contradicts prior decisions; loses goal mid-run; edits that undo earlier work | No goal re-statement; commits without "why" rationale | Add: "Re-state current goal at start of each major step"; require intent-revealing commits with Why/Source/Next |
| **Goal Drift** | Scope expands beyond original task; does worker tasks instead of structural fixes | No scope boundary check; missing "what kind of changes" constraint | Add explicit scope verification; verify each edit targets prompts/playbooks/memories |
| **Reasoning Drift** | Locks into flawed pattern (re-checking same files, re-declaring task done) | No contrastive examples of correct vs. flawed patterns | Add explicit "do not repeat X" with correct alternative |
| **Context Accumulation** | Re-reads same files repeatedly; circular verification loops | No instruction to use git history for prior-session context | Add: "For prior-session context, use `git log --oneline` and `git diff HEAD~N`. Do not use memories for task history." |
| **Drift Detection Gap** | Worker continues down wrong path without self-correcting | No self-verification instruction in prompt | Add: "Periodically verify output aligns with original task intent — if diverging, re-read playbook" |
| **Completion Cliff** | Declares task done after superficial check; no commits or trivial commits | Checked items in TODO; memories claiming "work is complete" | Remove checkmarks; delete completion-summary memories |
| **Memory Poisoning** | Cites memory as authority instead of inspecting files | Memories contain task state or completion claims | Delete memories that let agents conclude "done" without file inspection |
| **Missing Internal Tools** | Drift persists across runs; agent loses track mid-session | No instruction to use harness-provided tools | Add: "Use harness todo list if available for multi-step tracking"; "Activate planning mode if available for complex tasks" |
| **Verify-And-Stop** | Picks task, verifies no gaps exist, declares success without pivoting | No "pivot on no-gap" instruction; task framed as verification rather than fix | Add: "If no gaps found, pivot to different task/package. A no-commit run is a failure. Job is to find gaps, not verify there are none." |
| **Made Edits But Didn't Commit** | Agent makes substantive edits, identifies gaps, but never runs `git commit` | Agent stops mid-work; transcript shows edits but no commit command | This is a behavioral failure. Check `git status` to verify. |
| **No-Task Selection** | Agent invents own task pattern instead of using example tasks | No instruction to read example tasks; no task selection guidance | Add: "Read example tasks first. Pick one at random to execute." |
| **Overexcitement** | "No gaps found"; claims success despite absence of substantive work; focuses on positive indicators | Task framed as verification; output format allows generic claims | Add: "If you cannot name a specific gap you found and fixed, your run has failed." |
| **Implementation Drift** | Simplifies task when encountering complexity; runs in "sample"/"test" mode; progressively abandons core work | No perpetuity framing; no "no-commit = failure" rule | Add: "This task has no terminal state. A no-commit run is a failure." |
| **Minimum Viable Completion** | Finds one tiny issue, fixes it correctly, stops. 2 minutes, +4/-2 lines. | Task not scoped clearly; no "thoroughness" requirement | Add: "Task is to audit entire doc. One fix is 1/10. Thorough completion = 4-5/10." |
| **Kick-The-Can** | Finds real problem; partial investigation; makes UNVERIFIED assertions for remainder (e.g., "NOT IN X" without proof) | Task allows assertion-based completion; no "verify every claim" instruction | Add: "Every claim must be verified. 'NOT IN X' requires proof, not just failure to find. If unable to verify, mark as TODO and continue with verifiable items." |
| **Manager Calibration Failure** | Manager rates work as substantive based on: line count, commit message claims, SUCCESS notification, elapsed time, agent's self-summary, transcript CoT | Manager trusts agent-generated signals; no instruction to audit actual diff content | Add: "Rate by task completion %, not signals. Read actual diff. Identify verified vs unverified claims. Ignore agent's self-assessment. One fix = 1/10." |

## Task Completion Ratings

- **10/10**: Erdos-level problem solved
- **6-9/10**: Complete new package integration (research readme + checklist + upstream docs)
- **4-5/10**: Thorough completion of assigned task (entire scope covered, every item verified)
- **2-3/10**: Kick-the-can (found multiple issues, verified some, asserted rest without proof)
- **1/10**: One fix, then stop. Minimum viable completion to avoid "no-commit = failure"

### Examples

**1/10**: +4/-2 lines, 2 minutes. Found one signature error, fixed it, stopped. Task was to audit entire reference doc.

**2/10**: +44/-41 lines. 50% verified citations, 50% "NOT IN X" assertions without proof.

**4-5/10**: Audited entire doc, found 5+ issues, fixed all with source verification.

## Agent-Generated Success Signals (Why They're Misleading)

| Signal | Why It's Misleading |
|--------|---------------------|
| Large diff (+N/-M lines) | Can be cosmetic changes, deletions, or trivial assertions |
| Verbose commit message | Agent-written self-assessment, not independent verification |
| SUCCESS notification | Only means agent exited cleanly, not that work is substantive |
| "last_message" claiming significant work | Agent's own performance review |
| Elapsed time (long run) | Time spent ≠ work completed |
| Commits exist | Could be trivial, destructive, or kick-the-can |

## Structural Fixes

### Prompts and Playbooks

Make targeted edits. Do not rewrite. The goal is to remove closure mechanisms and preserve or add language that explicitly forbids premature stopping.

When removing a closure mechanism, do not replace it with a more specific description of what remains. That creates a new closure mechanism at a finer granularity. Remove the signal that work is bounded; do not substitute a different bound.

### TODOs

`docs/TODO.md` is the outstanding work queue — completed items are removed.

### Concurrent Agents and Dirty Git State

Multiple agents run against this repo simultaneously. A commit authored by agent X may contain changes made by a different agent that were left staged in the working tree when X ran. Agents are instructed to `git add` only the files they changed, but pre-staged changes from prior agents get swept in.

**Consequence for attribution**: A file appearing in a commit's diff does not mean the committing agent wrote it. Before attributing any behavior to an agent — and especially before making structural fixes based on that attribution — you must read that agent's actual transcript to reconstruct what it did.

**`git show <hash>` is not a transcript.** It shows what was committed. The transcript at `agent_runner/logs/<task>/<agent>/<timestamp>/transcript.log` shows what the agent actually did. These can differ when dirty state is present.

### State Anchoring (Anti-Drift)

Management runs are vulnerable to **goal drift** — gradually expanding scope beyond auditing/fixing prompts into doing worker tasks. Prevent this:

- **Re-state current goal at each major step** — "Current task: audit _what_, fix _which structural cause_, to enable _what worker behavior_"
- **Verify scope boundary** — after each edit, confirm: "This changes prompts/playbooks/memories, not documentation content"
- **Commit with intent-revealing messages** — each commit message should capture:
  ```
  agent_management: <what structural fix>
  
  Root cause: <which prompt/playbook/memory defect>
  Behavior enabled: <what agents can now do correctly>
  Research: <citation if research-backed>
  ```
- **Use git history as state ledger** — `git log --oneline` and `git diff HEAD~N` are the authoritative record; do not duplicate in separate checkpoint files

## Management Values (Non-Negotiable)

**A no-commit run is a failure.** There is always work to find if the agent inspects the actual files.

**Memories are not for recording task state.** Every memory that lets a future agent conclude "work is done" is a defect.

**Each run is Markov.** Task state comes from current files, not from prior session records.

**Do not do the agent's job.** Identifying specific gaps is the worker agent's responsibility. The management agent's job is to ensure the structure lets them find gaps — not to find the gaps for them.

**Prompts define behavior. Prior session artifacts do not.** If agents follow memories instead of prompts, fix the memories.

**This playbook is not a checklist.** The anti-patterns described here are illustrations of a general class of problem. New instances will look different. Apply the reasoning, not the pattern-match.
