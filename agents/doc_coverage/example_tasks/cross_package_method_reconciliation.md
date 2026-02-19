# Example Task: Cross-Package Method Reconciliation

## Goal

Pick one algorithm that appears across multiple packages (e.g., LLL, HNF, SVP). Verify each package's documentation has complete, package-specific signatures and caveats.

## Workflow

1. **Select a method** — e.g., `LLL`
2. **Inventory all packages implementing it:**
   - SageMath: `IntegralLattice.LLL()`, `IntegerLattice.LLL()`
   - FLINT: `fmpz_lll()`, `fmpz_lll_context_init()`
   - NTL: `LLL()`, `LLL_plus()`
   - fpylll: `LLL.reduction()`, `lll_reduction()`
   - PARI/GP: `qflll()`, `qflllgram()`
   - GAP: `LLLReducedBasis()`, `LLLReducedGramMat()`
3. **For each package:**
   - Verify full signature (all parameters, defaults, return types)
   - Document package-specific behavior differences
   - Capture domain constraints (e.g., "positive-definite only" vs. "works for indefinite")
4. **Note discrepancies:**
   - Different parameter names for same concept
   - Different default values
   - Different return value conventions
   - Package-specific limitations

## Example Output

```markdown
LLL parameter comparison:
- SageMath: `delta=0.99` (implicit), returns new lattice object
- FLINT: `delta ∈ (0.25, 1)` explicit constraint, in-place reduction
- fpylll: `delta=LLL_DEF_DELTA`, `eta=LLL_DEF_ETA` explicit constants
- PARI/GP: `flag` parameter controls output format
```

## Purpose

This task ensures cross-package method surfaces are precisely documented, not vaguely similar.
