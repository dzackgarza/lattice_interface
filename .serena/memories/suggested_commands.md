# Suggested Commands
- Run standard suite: `just test`
- Run full suite including in-progress wrapper tests: `just test-full`
- Targeted pytest in Sage env: `HOME=/tmp/sage-home conda run -n sage python -m pytest -q <path_or_test>`
- Run docs scheduler once: `uv run scripts/doc_coverage_scheduler.py --once`
- Start/stop scheduler: `scripts/start_doc_coverage_scheduler.sh` / `scripts/stop_doc_coverage_scheduler.sh`
- Quick git history on docs: `git log --oneline -- docs/`
- Search files: `rg --files`
- Search text: `rg "<pattern>" docs tests`