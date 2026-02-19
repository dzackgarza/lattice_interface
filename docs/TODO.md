# Documentation Gaps - Bilinear-Form Lattice Methods

This file tracks missing prerequisites for building the per-package method checklists correctly.
The checklists themselves track per-method completion; this file tracks what must exist *before* checklist entries can be filled out with source-backed accuracy (primarily: local copies of upstream docs).

**STATUS (2026-02-19)**: Goal 1 NOT COMPLETE - local doc copies missing for 8 packages.

## Goal 1: Local Doc Integration (MANDATORY PREREQUISITE)

Local upstream docs under `docs/**/upstream/` are required before contract-fidelity work can proceed.

### Packages needing integration

- [ ] flint (has .rst files under upstream/, needs integration check)
- [ ] GAP core (core GAP docs)
- [ ] NTL (has .txt/.cpp.html files under upstream/, needs integration check)
- [ ] fpylll (partial - needs completion)
- [ ] forms (GAP package - partial)
- [ ] g6k (partial)
- [ ] crystallographic_stack (partial)
- [ ] pari_gp (partial)

### Packages with integrated local docs (complete)

- [x] hypercells (full chapter snapshots)
- [x] flatter (README and example profiles)
- [x] SageMath (integral lattice docs)
- [x] Oscar/Hecke (Julia lattice docs)
