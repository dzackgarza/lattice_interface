# Documentation Gaps - Bilinear-Form Lattice Methods

This file tracks the prerequisite state for building complete documentation.
Reference docs (`docs/*/lattice/*.md`) track method surfaces with source-backed signatures.
Checklist files (`docs/*_methods_checklist.md`) track TEST COVERAGE - separate task.

**STATUS (2026-02-19)**: Goal 1 NOT COMPLETE - 8 packages missing local doc integration.

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


## Goal 2: Contract-Fidelity Work (Post-Integration)

This section tracks gaps in method documentation completeness (argument surfaces, types, assumptions, constraints) for packages with integrated local docs.

### GAP Forms Package (`docs/forms/lattice/forms_lattice_reference.md`)

- [ ] **Explicit Type Specifications:** Add explicit GAP type annotations or descriptions for all function arguments and return values. The current documentation lacks this detail, making it harder to use without consulting the original GAP manual.

### SageMath (`docs/sage_methods_checklist.md`)

- [ ] **Explicit Type Specifications:** Add explicit SageMath type annotations or descriptions for all function arguments and return values to improve clarity and reduce reliance on upstream documentation.

### Julia/Hecke.jl (`docs/julia_methods_checklist.md`)

- [ ] **Explicit Type Specifications:** Add explicit Julia type annotations or descriptions for all function arguments and return values to make the documentation more self-contained.
