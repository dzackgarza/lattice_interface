# NConvex Method Test Gap Checklist

Tracks GAP `NConvex` package surface documented in `docs/nconvex/lattice/nconvex_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Package Load Surface

- [ ] `LoadPackage("NConvex")`

---

## 2. Method Inventory Triage (Source-Blocked)

- Canonical `NConvex` manual chapter index and method-level pages were not retrievable from current available web endpoints in this environment.
- Do not infer or invent runtime method names; add method checkboxes only after canonical method pages are available.
- Use `docs/nconvex/upstream/nconvex_online_provenance_2026-02-17.md` as continuity for the unresolved method-surface gap.

---

## Domain Caveat

- `NConvex` is a polyhedral-geometry package family and should be treated separately from quadratic-form signature/genus/isometry APIs.

---

## References

- `docs/nconvex/lattice/nconvex_lattice_reference.md`
- GAP package page: `https://gap-packages.github.io/NConvex/`
- NConvex repository: `https://github.com/homalg-project/NConvex`
- Localized provenance and unresolved-gap notes: `docs/nconvex/upstream/nconvex_online_provenance_2026-02-17.md`
