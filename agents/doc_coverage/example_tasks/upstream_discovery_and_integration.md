# Example Task: Upstream Discovery and Integration

## Goal

Pick one in-scope package. Survey what local upstream docs exist, then research online for missing documentation. Integrate any gaps found.

## Workflow

1. **Select a package** — e.g., `g6k`
2. **Inventory local upstream docs:**
   - List all files under `docs/g6k/upstream/`
   - Note what API surfaces they cover (e.g., siever.pyx, README, algorithms/)
3. **Research online:**
   - Find the official repository (e.g., `github.com/fplll/g6k`)
   - Check for documentation not captured locally:
     - README, INSTALL, CONTRIBUTING files
     - Wiki pages or GitHub Pages docs
     - API reference generators (Sphinx, Doxygen output)
     - Tutorial/example notebooks
     - Release notes with new API surfaces
4. **Integrate missing docs:**
   - Fetch missing files into `docs/g6k/upstream/`
5. **Verify reference doc coverage:**
   - After integration, check if reference doc covers all newly added upstream material

## Example Output

```markdown
Added to docs/g6k/upstream/:
- CONTRIBUTING.md (API stability notes)
- docs/siever_params.rst (parameter reference)
- examples/challenge_svp.ipynb (usage patterns)
```

## Purpose

This task ensures local upstream collections are complete, not just convenient.

## Network Contingency

If a known/canonical upstream URL is discovered via web results but direct shell retrieval fails (DNS/TLS/connectivity failure):
- Retry the same URL a small fixed number of times (`<=2`)
- Treat this as an environment access failure, not proof that upstream docs do not exist
- If a source is genuinely unreachable and the gap is actionable, write a Serena memory with the URL and the specific method-surface gap it would fill
- Then pivot to substantial offline work from existing local snapshots
