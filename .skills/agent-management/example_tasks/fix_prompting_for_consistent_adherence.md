# Example Task: Fix Prompting for Consistent Guideline Adherence

## Scenario

Agents are not consistently following project-wide guidelines. Every agent should execute a predictable workflow: read prompt/skill → perform nontrivial work → collect into git commit → provide value-explaining summary. Deviations from this pattern indicate structural problems in the prompting system.

## FIRST: Check Ntfy

```bash
curl -s "https://ntfy.sh/dzg-lattice-doc-updates/json?poll=1&since=all" | jq -c '{time: .time, title: .title, message: .message}'
```

The ntfy feed tells you which agents ran, their elapsed time, and their claimed output. A 2-minute run with "no gaps found" in last_message is a behavioral failure you can immediately identify.

## ⚠️ CRITICAL: Do Not Trust Agent-Generated Signals

The ntfy feed shows agent self-summaries. Commit messages are agent-written. Line counts in diffs can be misleading. **You will be fooled if you trust these.**

**You MUST read the actual git diffs:**

```bash
git show <commit_hash>
```

Rate work against this scale:
- **10/10**: Erdos-level problem solved
- **6-9/10**: Complete new package integration (research readme + checklist + upstream docs)
- **4-5/10**: Thorough completion of assigned task (entire scope covered, every item verified)
- **2-3/10**: Kick-the-can (found multiple issues, verified some, asserted rest without proof)
- **1/10**: One fix, then stop. Minimum viable completion to avoid "no-commit = failure"

### Examples of Misrating

**1/10 rated as 4-5/10:**
ntfy shows: "SUCCESS, +4/-2 lines, 2m08s, Fix signature mismatch in fmpz_mat_hnf_modular_eldiv"

Manager reads transcript, sees agent "found real gap, fixed it properly," rates 4-5/10.

**Actual rating: 1/10.** One tiny fix in 2 minutes. Task was to audit entire reference doc. Agent found one thing, fixed it, stopped. Minimum viable completion.

**2/10 work:**
+44/-41 lines. 50% verified citations, 50% "NOT IN MANUAL" assertions without proof. Kick-the-can - verified some, asserted rest.

**4-5/10 work:**
Audited entire FLINT reference doc. Found 5+ signature mismatches. Fixed all with source verification. Thorough completion of assigned scope.

**6-9/10 work:**
Found undocumented package. Fetched upstream docs. Created new research_readme.md with all methods. Created checklist. Full package integration.

## Failure Mode Detection

### Low-Effort Completions (Most Common)

Agents claiming task completion after 1-3 minutes on substantial tasks. Examine transcripts for:

1. **False completion markers used as shortcuts**:
   - "COMPLETED" or status headers in files
   - Checklists with checked items
   - Serena memories summarizing "prior work"
   - TODO items marked done
   - Any artifact that lets an agent conclude "nothing left to do" without examining actual files

2. **Performance theater**:
   - Verbose documentation or memories declaring how much was done
   - Summary-style writing that should be in git history or commit messages
   - Reformatting existing content as "work"

3. **Trivial changes masquerading as progress**:
   - Semantic equivalents (rewording without adding meaning)
   - Minor clarifications or disambiguations
   - Cosmetic formatting changes
   - Git diffs of only several lines on tasks meant to be substantial

### Verify-And-Stop (Common in Perpetual Tasks)

Agents that pick a task type, verify no gaps exist for that task, then declare success instead of pivoting. Examine transcripts for:

1. **Task selection without pivot instruction**:
   - Agent invents own approach instead of using provided example tasks
   - No "read example tasks first" instruction in prompt
   - No "pick one at random" guidance

2. **Verification framing**:
   - Task framed as "verify X" rather than "fix gaps in X"
   - Last message says "no gaps found" or "verification complete"
   - Agent treats absence of obvious problems as success

3. **Missing perpetual-work framing**:
   - No explicit statement that task has no terminal state
   - No instruction to pivot to different task/package if current one has no gaps
   - No "a no-commit run is a failure" rule

Fix pattern: Add "Immediate Next Step" requiring example task reading, add explicit pivot instruction, frame job as "find and fix gaps" not "verify there are none".

### Churning / Timeout (Less Common)

Agents that ran the full 15 minutes without completing. Check transcripts for:
- Infinite loops in reasoning
- Repeated failed tool calls
- Getting stuck on a subproblem
- These are usually timeout issues, not prompting problems

## Root Cause Investigation

### 1. Transcript Analysis

For each identified failure, read the full CoT (Chain of Thought) to understand:

- What reasoning led the agent to underestimate scope?
- Did they examine current state deeply or skim?
- What artifact or signal triggered the "done" conclusion?
- Where did the reasoning diverge from productive work?

### 2. Git Diff Assessment (MANDATORY)

**Do not rate work without reading the actual diff.** Run `git show <hash>` for every commit.

Check:
- **Verified vs unverified claims**: If diff says "NOT IN X", is there proof (grep showing no matches, web confirmation)? Or just assertion?
- **Kick-the-can ratio**: What % of claims are verified vs asserted without proof?
- **Semantic content**: Additions vs rewordings vs deletions
- **Task completion %**: Did agent finish the task, or just start it and assert the rest?

A diff with 50% verified claims and 50% unverified assertions is 1-3/10 work, regardless of line count.

### 3. Prompt/Skill/Doc Inspection

Identify what in the structure creates gradients toward shirking:

- Language implying tasks have endpoints or completion states
- Checklists or status markers that can be "satisfied"
- Absence of explicit "no premature stopping" language
- Framing that rewards speed over quality
- Any text that could serve as a "done" signal

## Research Phase (Required)

Before making changes, conduct literature research on:

- LLM prompt engineering for sustained effort
- Task description techniques that prevent reward-hacking
- Frontier model firm publications (Anthropic, OpenAI, Google DeepMind) on alignment and instruction following
- Arxiv papers on:
  - Prompt injection and manipulation
  - Reward hacking in language models
  - CoT failure modes
  - Instruction adherence

Do NOT use:
- Random blog posts
- SEO content
- Unverified tutorials
- Generic web search results

Use sources with empirical backing and citations.

## Fix Protocol

### Constraints

1. **No meta leakage**: Worker prompts must not contain managerial language about "why" the prompt is structured a certain way. The fix should be invisible to the worker.

2. **No negation replacement**: Replacing "you may stop early" with "do not stop early" still primes the behavior. Remove the concept entirely, don't invert it.

3. **Evidence-based changes**: Every edit must trace to specific transcript evidence showing why the current language caused failure.

4. **No blind iteration**: Do not make changes without understanding the CoT failure. If you cannot identify the causal path from prompt to bad behavior, do not edit.

### Git History Analysis

Before editing, review git history of the target prompt/skill:

```bash
git log --oneline --follow -- agents/*/prompt.md
git log --oneline --follow -- .agents/skills/*/SKILL.md
```

Look for:
- Oscillating changes (adding X, removing X, adding X again)
- Fly-swatting patterns (fixing specific bad behaviors one at a time)
- Churn without progress toward stable framings
- Local minima where edits rotate around a broken attractor

If history shows oscillation, the current framing is fundamentally wrong. Research deeper before editing.

### Edit Strategy

1. **Remove closure mechanisms**: Delete language that signals bounded work
2. **Remove satisficing targets**: Delete checklists, completion criteria, status fields
3. **Add perpetuity language**: Frame tasks as ongoing quality goals without terminal states
4. **Remove negation-based guards**: If "do not X" appears, find the positive framing that makes X irrelevant
5. **Verify against research**: Cross-check edits against literature on preventing the identified failure mode

## Verification

After making changes:

1. Ensure edits address specific transcript-identified failure modes
2. Confirm no meta-commentary leaked into worker prompts
3. Check that changes follow research-backed principles
4. Verify git history shows positive gradient (not oscillation)
5. Commit with message explaining the behavioral problem being addressed

## Success Criteria

- All identified failure modes have root causes documented
- Changes are traceable from transcript evidence through research to edit
- No oscillating patterns in prompt/skill history
- Worker prompts contain no managerial meta-commentary
- Changes are grounded in empirical research, not intuition

## Anti-Patterns to Avoid

- Adding "do not stop early" as a band-aid
- Enumerating specific bad behaviors to avoid (primes them)
- Making changes without reading the actual failure transcripts
- Using blog posts or tutorials as authority
- Churning edits that fix surface symptoms without addressing root gradients
- Creating new checklists or status markers as "improvements"
