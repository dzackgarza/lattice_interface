# Debug Commit + Network Smoke Test

You are running in a repo. Do the minimum steps to prove you can write, commit, and access the network.

Steps:
1) Create a new file at `tmp/agent_runner_debug/smoke.txt` with a single line: `smoke ok`.
2) Git add and commit the file with message: `agent_runner debug smoke`.
3) Make a network call: `curl -fsSL https://example.com >/dev/null`.
4) Respond with a short summary of what you did.
