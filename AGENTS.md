# Sage Lattice Doc Testing Playbook

## Goal
- Keep reference-doc tests mathematically meaningful, explicit, and honest.
- Coverage must reflect real tested behavior, not aliases or hidden exclusions.

## Environment
- Always run Sage tests in the Sage conda env.
- Canonical command: `just test` (the recipe already invokes `conda run -n sage ...`).
- For targeted work: `HOME=/tmp/sage-home conda run -n sage python -m pytest -q <path_or_test>`

## Execution Loop
1. Run `just test`.
2. Read uncovered-method lists from failing `*_coverage` tests.
3. Add one static test per uncovered method.
4. Use docstring tag format in each test:
   - first line: `method: <exact_runtime_method_name>`
5. Re-run targeted coverage tests.
6. Re-run full suite with `just test`.

## Hard Rules
- No token-map or alias-crediting for coverage.
- No per-file blacklist expansions to force green.
- No changing coverage surface (`module_prefixes`) to hide methods.
- No `xfail`/expected-failure markers.
- Do not assert on exceptions as a substitute for behavior tests.

## Test Quality Rules
- Assertions must be mathematically nontrivial.
- Avoid `is not None`, `hasattr`, `isinstance` as primary assertions.
- Use small examples, keep tests fast (<30s when possible).
- Use precise types and contract-correct inputs.
- Every assertion message should be explicit f-string diagnostics.

## Coverage Policy
- Global irrelevant methods live only in `tests/sage/sage_doc/conftest.py`.
- Coverage failures must print uncovered method names.
- A method is either:
  - globally irrelevant infrastructure, or
  - explicitly tested with its own `method:` tag.

## Definition of Done
- `just test` passes.
- Coverage tests pass without hidden exclusions.
- New tests document real current functionality with mathematical assertions.
