# Documentation Gaps - Bilinear-Form Lattice Methods

This file tracks the prerequisite state for building complete documentation.
Reference docs (`docs/*/lattice/*.md`) track method surfaces with source-backed signatures.
Checklist files (`docs/*_methods_checklist.md`) track TEST COVERAGE - separate task.

## Goal 1: Local Doc Integration (MANDATORY PREREQUISITE)

Local upstream docs under `docs/**/upstream/` are required before contract-fidelity work can proceed.

### Packages with integrated local docs

- [x] hypercells (full chapter snapshots)
- [x] flatter (README and example profiles)
- [x] SageMath (integral lattice docs)
- [x] Oscar/Hecke (Julia lattice docs)
- [x] flint (fmpz_lll.rst + fmpz_mat.rst integrated)
- [x] NTL (LLL.txt + mat_ZZ.txt integrated)
- [x] GAP core (matint.xml, chap24/25/26.html and related sources present under upstream/)
- [x] fpylll (.pyx source files + online provenance snapshot present)
- [x] forms (chap1-5 HTML files present)
- [x] g6k (siever.pyx + README + algorithms/*.py present)
- [x] crystallographic_stack (cryst/caratinterface/crystcat .gd and .tex files present)
- [x] pari_gp (HTML upstream sections present)


## Goal 2: Contract-Fidelity Work (Post-Integration)

Completeness and provable correctness of all documented methods across all reference docs under `docs/`. Inspect the actual files.
