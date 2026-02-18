# Documentation & Test Gap Priorities

## Focus: Bilinear-Form Lattice Methods (In-Scope Only)

Real work needed - not meta-churn.

## Julia (OSCAR/Hecke) - High Priority

Missing test coverage for core bilinear-form lattice APIs:
- [ ] Genus/spinor genus constructors
- [ ] Isometry/equivalence testing
- [ ] Discriminant group/form methods
- [ ] Signature-based lattice construction

## Sage - High Priority

Missing test coverage:
- [ ] Free quadratic module methods
- [ ] Quadratic form genus/spinor genus
- [ ] Lattice reduction (LLL, etc.)
- [ ] Isometry classification

## GAP - Medium Priority

Missing test coverage:
- [ ] Crystallographic methods
- [ ] Forms package methods
- [ ] HyperCells integration

## Tools (fplll/fpylll/g6k) - Lower Priority

- [ ] CLI/API surface test gaps
- [ ] BKZ family coverage

---

The unchecked items in existing checklists represent real work. Prioritize the largest gaps first.

Done items in checklists represent test coverage that exists. Review `docs/*_methods_checklist.md` for complete picture.
