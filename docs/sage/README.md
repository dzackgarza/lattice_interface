# Sage Docs (Official + Local Notes)

This folder contains:

- Local reference notes (`*_reference.md`)
- Official SageMath doc snapshots under each module's `upstream/` directory

## Layout

- `lattice/`
  - `sagemath_lattice_reference.md`
  - `upstream/free_module_integer.html`
- `integral_lattice/`
  - `sage_integral_lattice_reference.md`
  - `upstream/free_quadratic_module_integer_symmetric.html`
- `quadratic_form/`
  - `sage_quadratic_form_reference.md`
  - `upstream/quadratic_form.html`
- `genus/`
  - `sage_genus_reference.md`
  - `upstream/genus.html`
- `torsion_quadratic_module/`
  - `sage_torsion_quadratic_module_reference.md`
  - `upstream/torsion_quadratic_module.html`

See `SOURCES.md` for canonical URLs and fetch date.

## Refresh snapshots

```bash
curl -L -s 'https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_module_integer.html' \
  -o docs/sage/lattice/upstream/free_module_integer.html
curl -L -s 'https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_quadratic_module_integer_symmetric.html' \
  -o docs/sage/integral_lattice/upstream/free_quadratic_module_integer_symmetric.html
curl -L -s 'https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/quadratic_form.html' \
  -o docs/sage/quadratic_form/upstream/quadratic_form.html
curl -L -s 'https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/genera/genus.html' \
  -o docs/sage/genus/upstream/genus.html
curl -L -s 'https://doc.sagemath.org/html/en/reference/modules/sage/modules/torsion_quadratic_module.html' \
  -o docs/sage/torsion_quadratic_module/upstream/torsion_quadratic_module.html
```
