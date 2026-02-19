# Example Task: Mathematical Contract Audit

## Goal

Pick one reference doc. For every method, verify that mathematical assumptions and constraints are explicitly stated with upstream citations.

## Workflow

1. **Select a reference doc** — e.g., `docs/sage/lattice/sagemath_lattice_reference.md`
2. **For each method entry, verify:**
   - **Domain constraints**: positive-definite only? indefinite OK? degenerate forms?
   - **Ring/field restrictions**: ℤ-only? ℚ? arbitrary fields?
   - **Non-degeneracy requirements**: does method require non-degenerate form?
   - **Signature constraints**: definite, indefinite, or both?
   - **Integrality constraints**: does method require integral Gram matrix?
3. **Flag missing contracts:**
   - Methods with no domain tag (e.g., `[PD]`, `[INDEF]`, `[DEG]`)
   - Methods with vague caveats ("usually", "typically")
   - Methods with unstated ring assumptions
4. **Add explicit contract language:**
   - Replace vague deferrals with exact truth values from upstream
   - Add tag legend entries for each constraint type

## Example Output

```markdown
Before: `LLL()` — LLL reduction for lattice bases.
After:  `LLL()` — LLL reduction. `[PD, EUCLID]` Requires positive-definite Gram matrix.
        Returns δ-reduced basis with `δ = 0.99` (implicit default).
        Source: docs/sage/upstream/free_quadratic_module_integer_symmetric.html §"LLL Reduction"
```

## Purpose

This task ensures mathematical precision, not vague approximations.

## Anti-Patterns

- Vague claims: `usually`, `typically`, `often`, `most of the time` — replace with exact truth values
- Weak deferrals: `unknown`, `unverified`, `needs testing` — answer through docs/source/web research where reasonably possible
