# Test Coverage Alignment (2026-02-18) — Checklist Tags Round 1

## Scope executed
- Assignment type: code/test/runtime behavior (applied `docs/test_coverage_playbook.md` and `TEST_QUALITY.md`).
- Updated checklist/test alignment in:
  - `docs/gap_methods_checklist.md`
  - `docs/julia_methods_checklist.md`
  - `docs/sage_methods_checklist.md`
- Added missing explicit method-tagged tests in Sage docs tests:
  - `tests/sage_doc/test_integerlattice_static.py`
    - `test_integerlattice_reduced_basis_preserves_discriminant_after_lll` (`method: reduced_basis`)
  - `tests/sage_doc/test_integrallattice_static.py`
    - `test_integrallattice_degree_matches_rank_for_nondegenerate_example` (`method: degree`)
  - `tests/sage_doc/test_torsionquadraticmodule_static.py`
    - `test_tqm_order_equals_cardinality_for_finite_module` (`method: order`)
  - `tests/sage_doc/test_numberfield_bridge_static.py`
    - `test_numberfield_element_trace_matches_conjugate_sum` (`method: trace`)

## Mapping policy used
- Added `[test: tests/...::test_...]` tags directly on checked checklist lines.
- For Julia/Sage mass alignment, used conservative domain-locked mapping:
  - Julia checklist lines linked only to `tests/julia_pytest/**` method-tagged tests.
  - Sage checklist lines linked only to `tests/sage_doc/**` method-tagged tests.
  - GAP checklist lines linked only to `tests/gap_doc/**` method-tagged tests.
- Avoided global cross-domain alias crediting.

## Notable correctness fixups
- Replaced weak/incorrect test links for Sage `reduced_basis`, `degree()`, `order()`, and number-field `trace()` with explicit tests above.

## Follow-up gaps
- Many checklist entries remain unchecked; only entries with explicit method-tagged test targets were checked.
- Additional rounds can continue method-by-method for remaining unchecked lines.

## Git ledger
- Commit created: `890870e` with staged assignment files only.
- Push attempt failed in current environment due network/DNS resolution failure to GitHub.
