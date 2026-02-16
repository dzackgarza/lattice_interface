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

## Interface Design Rule (Non-Negotiable)
- NEVER prioritize backward compatibility during interface design stage.
- If the interface is still being defined, backward compatibility is not a valid constraint.
- Prioritize mathematical correctness, coherent type ontology, and clear contracts first.
- Remove/rename incorrect interface types immediately rather than preserving legacy names.

## TDD Marker
- Use `@pytest.mark.tdd_red` only as an annotation for tests intentionally in RED phase.
- `tdd_red` is metadata only; it does not change test behavior.
- `tdd_red` tests must still run normally and fail naturally until implementation is complete.
- Do not replace failing tests with `skip`/`xfail`; remove `tdd_red` when the test turns green.
- `tdd_red` is reserved ONLY for NEW interface-contract development.
- NEVER use `tdd_red` when testing behavior of EXISTING libraries, existing tools, or already-implemented external APIs.

## Test Quality Rules
- Follow `TEST_QUALITY.md` as the complete, authoritative test-quality standard for this repository.

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
