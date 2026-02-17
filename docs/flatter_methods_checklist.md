# flatter Method Test Gap Checklist

Tracks flatter-relevant methods/commands documented in `docs/flatter/lattice/flatter_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. CLI Surface

- [ ] `flatter [OPTION] [INPUT_FILE [OUTPUT_FILE]]`
- [ ] `-a ALPHA`
- [ ] `-rhf R`
- [ ] `-logcond C`
- [ ] `-p PREC`
- [ ] `-t THRS`
- [ ] `-v`
- [ ] `-q`
- [ ] `-h`

## 2. Package Utility Surface

- [ ] `./test.sh`
- [ ] `./test_perf.py [NTRIALS] [NROWS] [START_R] [STEP_R]`
- [ ] `make test`

---

## Domain Caveats

- `flatter` is a floating-point Euclidean lattice-basis reduction tool; it is not an indefinite-form genus/isometry classifier.
- Upstream presents `flatter` primarily as a CLI-first tool; this checklist tracks documented command/options and repository utility scripts.

---

## References

- `docs/flatter/lattice/flatter_lattice_reference.md`
- `docs/flatter/upstream/flatter_online_provenance_2026-02-17.md`
- flatter repository/readme: `https://github.com/keeganryan/flatter`
