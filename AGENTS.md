# Playbook Router

Use the [shared math container](https://github.com/dzackgarza/ai-review-ci/blob/main/SAGE-CONTAINER.md#use-the-image)
(`ghcr.io/dzackgarza/sage:develop`) for Lean/elan, Sage with mypy, GAP,
Julia/Oscar, Macaulay2, and Singular. The guide covers image pull/run commands,
CI use, and the host launchers.

Use the playbook that matches the assignment type.

## Assignment Type Routing

- Documentation-only assignments:
  - `agents/doc_coverage/playbook.md`
- Code/test/runtime behavior assignments:
  - `agents/test_coverage/playbook.md`
- Interface-contract/type-surface design assignments:
  - `agents/interface_design/playbook.md`

When an assignment spans multiple types, apply the relevant playbooks together.
