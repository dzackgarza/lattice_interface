# Documentation Gaps - Bilinear-Form Lattice Methods

Real doc work needed - incomplete/missing contracts, unverified signatures.

## Sage - Odd Lattice Incompleteness

- [ ] `TorsionQuadraticModule.is_genus(sig, even=False)` - upstream marks odd-lattice branch incomplete
- [ ] Document exact status of odd-lattice genus handling vs. documented `even=False` caveat

## Julia/Hecke - Contract Verification Needed

- [ ] Verify `integer_genera` signature constraints (det sign compatibility, parity)
- [ ] Verify `hermitian_genera` imaginary quadratic field requirement
- [ ] Clarify `embed_in_unimodular` even-lattice-only restriction
- [ ] Resolve `quadratic_space_with_isometry` conflicting default wording (`check::Bool=false`)

## fpylll - BKZ Signatures

- [ ] BKZ method signatures not fully rendered in upstream docs
- [ ] Verify actual BKZ API contracts against source

## GAP - Crystallographic

- [ ] `CrystCat*` aliases vs canonical names need triage

---

These represent actual incomplete or unverified documentation. Check `docs/**/*reference.md` and `docs/**/*provenance*.md` for source details.
