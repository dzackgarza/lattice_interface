# Test Coverage Playbook

## Scope

Applies only when the assignment changes code, tests, or runtime behavior.

Does not apply to documentation-only assignments.

## Goal

- Keep reference-doc tests mathematically meaningful, explicit, and honest.
- Coverage reflects real tested behavior, not aliases or hidden exclusions.

## Environment

- Run Sage tests in the Sage conda env.
- Canonical command: `just test` (invokes `conda run -n sage ...`).
- Targeted command: `HOME=/tmp/sage-home conda run -n sage python -m pytest -q <path_or_test>`

## Rules

- No token-map or alias-crediting for coverage.
- No per-file blacklist expansions to force green.
- No changing coverage surface (`module_prefixes`) to hide methods.
- No `xfail` or expected-failure markers.
- Do not assert on exceptions as a substitute for behavior tests.

## TDD Marker

- Use `@pytest.mark.tdd_red` only as annotation for intentionally RED tests.
- `tdd_red` is metadata only; it does not change execution behavior.
- `tdd_red` tests still run normally and fail naturally until implementation is complete.
- Do not replace failing tests with `skip` or `xfail`; remove `tdd_red` when test turns green.
- `tdd_red` is reserved only for new interface-contract development.
- NEVER use `tdd_red` for behavior of existing libraries/tools or already-implemented external APIs.

## Coverage Policy

- Global irrelevant methods live only in `tests/sage/sage_doc/conftest.py`.
- Coverage failures print uncovered method names.
- A method is either globally irrelevant infrastructure or explicitly tested with its own `method:` tag.

## Definition of Done

- `just test` passes.
- Coverage tests pass without hidden exclusions.
- New tests document real current functionality with mathematical assertions.

## Reference

- `TEST_QUALITY.md` is the authoritative test-quality standard.
