---
name: git-commit-guidelines
description: Git commit message format and guidelines. Use when making commits or creating agents that make commits.
---

# Git Commit Guidelines

All commits must follow this format:

```
<area>: <what>

Root cause: <why this was needed>
Behavior enabled: <what agents can now do correctly>
```

**Guidelines:**

- Write 2-3 plain sentences. No headers, no bullets, no markdown.
- Answer only: what specific gap was found, what is now correct or known, and why it matters for the project.
- Skip mechanical details (file names, checklist items, commit hashes).
- If you cannot name a specific gap that you found and fixed, your run has failed.

**Never claim completion:** Tasks have no terminal state. Don't write "all N methods now documented" or similar. This poisons future runs by signaling no work remains.

**Never use provenance files:** Files like `*_provenance_*.md` are closure mechanisms. Git history is the authoritative record.

Example:
```
doc_coverage: Documented 47 Oscar methods across genus, lattice, quadratic_form

Root cause: Oscar package bilinear-form lattice APIs undocumented
Behavior enabled: Users can now discover these methods with source citations to local upstream docs
```

**Always use explicit file list:** `git commit file1 file2 -m "message"`
- NEVER use: `git add .`, `git add -A`, or bare `git commit`
- Multiple agents run concurrently—bare commit sweeps ALL staged changes
