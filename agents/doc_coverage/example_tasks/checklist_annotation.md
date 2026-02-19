# Example Task: Checklist Annotation

## Goal

Take one checklist file. For every method entry, find its exact location in the local upstream docs and add a citation.

## Workflow

1. **Select a checklist** — e.g., `docs/flint_methods_checklist.md`
2. **For each checklist entry:**
   - Search upstream sources for the method signature
   - Record the exact file and section/line where it appears
   - Add a source citation to the checklist entry
3. **Flag discrepancies:**
   - Method in checklist but not in upstream docs → mark as unverified
   - Method in upstream docs but not in checklist → add missing entry
   - Signature mismatch → note the correct upstream form

## Example Output

```markdown
- [ ] `fmpz_lll_context_init_default(fl)`
      Source: docs/flint/upstream/fmpz_lll.rst §"Context Initialization"
```

## Purpose

This task ensures every checklist entry is grounded in actual upstream evidence.
