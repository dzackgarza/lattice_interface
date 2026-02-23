# Example Task: Operational Issues - Commit and Workflow Failures

## Scenario

Agents are failing operational requirements: not creating commits, mismanaging git state, or polluting docs with changelog data that belongs in commit messages. A successful run requires: startup → read task → nontrivial work → cohesive commit → success notification with meaningful progress summary.

## Prerequisites: Check Ntfy First

**ALWAYS check ntfy before doing anything else:**

```bash
curl -s "https://ntfy.sh/dzg-lattice-doc-updates/json?poll=1&since=all" | jq -c '{time: .time, title: .title, message: .message}'
```

Then check crontab:

```bash
date
crontab -l
```

If there are timeouts or usage limit failures, triage those separately. Commit investigation applies only to runs that had opportunity to commit but didn't.

## Primary Failure Mode: No Commit Created

### Investigation

1. **Check notification records** for failures mentioning "no commit" or "empty changeset"
2. **Read the transcript deeply** to determine:
   - Did the agent do partial work then quit early? (prompt adherence issue)
   - Did the agent do real work but forget to commit? (operational instruction issue)
   - Did the agent encounter git errors they couldn't resolve? (tool fluency issue)

### Differentiating Causes

**Partial work / early quit**:
- Transcript shows agent reasoning that "enough" was done
- CoT reveals false completion signals or underestimated scope
- Fix: Prompt/skill updates for stricter task adherence

**Real work, forgot commit**:
- Transcript shows substantive tool calls and file edits
- No git commands near session end
- Agent may have hit token/time limits before commit step
- Fix: Earlier/louder commit instructions in workflow

**Git confusion**:
- Transcript shows git commands that failed or produced unexpected results
- Agent may have been unable to interpret status
- Fix: Clearer git workflow guidance

## Fix Strategies

### Prompt/Skill Updates

When agents consistently fail to commit or quit early:

1. **Research task adherence** in LLM literature:
   - Arxiv papers on instruction following
   - OpenAI/Anthropic research on weaker model behavior
   - Frontier lab publications on workflow compliance

2. **Update instructions** based on findings:
   - Add explicit commit requirements earlier in workflow
   - Frame commit as mandatory, not optional
   - Remove any language that could signal "good enough to stop"

3. **Avoid over-prescription**:
   - Don't mandate exact commit message formats
   - Don't create rigid checklists agents follow blindly
   - Allow dynamic response to changing circumstances
   - Stochastic agents need flexibility, not rules engines

### Model Capability Issues

If a specific model consistently fails task adherence despite prompt fixes:

1. **Document the pattern**: Log all failed instances with timestamps, task names, and failure modes
2. **Notify user via ntfy**:
   ```
   Model [model_name] consistently failing task adherence on [task_type].
   Instances: [count] failures over [time_period].
   Suggest replacing with more capable agent for this task.
   ```
3. This is a last resort—prompt fixes should be attempted first

## Research Requirements

Before making prompt changes:

1. **Read actual research** on:
   - Task adherence in language models
   - Workflow compliance for LLM agents
   - Failure modes in agentic systems
   - Arxiv papers, not blogs
   - Frontier model firm publications (OpenAI, Anthropic, Google DeepMind)

2. **Ground changes in evidence**:
   - Specific transcript excerpts showing failure
   - Research explaining why the failure occurs
   - Principles that address the root cause

## Success Criteria

- All commit-related failures have root causes identified
- Fixes are grounded in transcript evidence and research
- Git state is clean without losing any work
- No changelog pollution in docs or memories
- Prompts ban harmful behaviors without being rigidly prescriptive
- Model capability issues are escalated to user with evidence

## Anti-Patterns to Avoid

- Mandating exact commit message formats (inflexible)
- Creating checklists for git operations (agents follow blindly)
- Using destructive git commands to "clean up"
- Adding changelog sections anywhere except commit messages
- Making prompt changes without transcript evidence
- Escalating to user before attempting prompt fixes
- Over-specifying workflows that must adapt to changing circumstances
