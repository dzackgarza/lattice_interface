# Example Task: Unified Method Surface Construction

## Goal

Consolidate all per-package checklist methods into a single unified checklist that contains the union of all methods, with duplicate functionalities grouped together.

## What This Is

Take every method from every package checklist. If two or more methods from different packages perform the same mathematical operation, they become one entry pointing to those checklists.

This is an index — detailed source/doc information lives in the original checklists.

## Workflow

1. **Extract all methods** from all package checklists
2. **Identify duplicates**: Methods from different packages that perform the same mathematical operation
3. **Build unified entries**: One entry per unique mathematical operation, referencing original checklists:

   ```markdown
   ## LLL Reduction
   - SageMath: `IntegralLattice.LLL()` → sage_methods_checklist.md
   - FLINT: `fmpz_lll()` → flint_methods_checklist.md
   - fpylll: `LLL.reduction()` → fpylll_methods_checklist.md
   - NTL: `LLL()` → ntl_methods_checklist.md
   - PARI/GP: `qflll()` → pari_gp_methods_checklist.md
   - GAP: `LLLReducedBasis()` → gap_methods_checklist.md
   
   ## HNF
   - FLINT: `fmpz_mat_hnf()` → flint_methods_checklist.md
   - SageMath: `hermite_form()` → sage_methods_checklist.md
   - GAP: `HermiteNormalForm()` → gap_methods_checklist.md
   ```

4. **Unique methods**: If a method has no equivalent, single entry pointing to its checklist

## Output

`docs/unified_method_surface.md` — union of all methods with grouped implementations, each pointing to its source checklist for details.

## Success Criteria

- Every method from every checklist appears
- Same-operation methods grouped under one heading
- Each entry links to original checklist (not to upstream docs directly)
