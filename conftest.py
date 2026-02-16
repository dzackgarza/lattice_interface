from __future__ import annotations

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[object]):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return
    if item.get_closest_marker("tdd_red") is None:
        return
    if not report.passed:
        return

    report.outcome = "failed"
    report.longrepr = (
        "\n"
        "TDD_RED VIOLATION\n"
        "=================\n"
        f"Test `{item.nodeid}` is marked @pytest.mark.tdd_red but it PASSED.\n"
        "A red-phase test must fail until implementation is complete.\n"
        "Remove the tdd_red marker before committing a passing version.\n"
    )
