# GAP NConvex Lattice-Oriented Reference
## Polyhedral-geometry package surface status and method-inventory triage

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | Provided by GAP package `NConvex` |
| `[POLY]` | Polyhedral/cone/combinatorial geometry workflow |
| `[TRIAGE]` | Method-level inventory unresolved in current source-access state |

---

## 1. Scope

`NConvex` is an in-scope GAP package for polyhedral geometry workflows in the homalg package ecosystem.
This repository tracks package-level checklist accountability for `NConvex` and records unresolved method-surface gaps explicitly.

---

## 2. Confirmed Surface (Source-Backed in This Pass)

| API | Description | Tags |
|-----|-------------|------|
| `LoadPackage("NConvex")` | Package-load entry point for enabling `NConvex` functionality in GAP sessions. | `[PKG, POLY]` |

Package-level evidence available in this pass confirms:

- package existence and active version stream,
- package role as polyhedral geometry tooling in the GAP/homalg ecosystem,
- repository availability and dependency context.

---

## 3. Method-Level Gap Status

Method-level API inventory is unresolved in this environment for this pass:

- canonical manual chapter endpoints listed by package metadata were not retrievable through available web fetch paths,
- no source-backed method signatures were added to avoid speculative contracts.

Immediate triage rule:

- keep method coverage claims empty until canonical manual/source pages are fetched,
- once retrievable, expand this file and `docs/nconvex_methods_checklist.md` with exact runtime method names, argument surfaces, and constraints.

---

## 4. Domain Notes

- `NConvex` belongs to polyhedral/lattice-point/combinatorial geometry workflows.
- This package is not a standalone arithmetic-lattice signature/genus/isometry framework.

---

## 5. Sources

- GAP package page: `https://gap-packages.github.io/NConvex/`
- NConvex repository: `https://github.com/homalg-project/NConvex`
- Localized unresolved-gap provenance: `docs/nconvex/upstream/nconvex_online_provenance_2026-02-17.md`
