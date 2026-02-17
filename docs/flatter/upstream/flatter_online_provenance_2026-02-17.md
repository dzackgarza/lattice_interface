# flatter Online Provenance Snapshot (2026-02-17 UTC)

Scope: first-class checklist/reference surface creation for `flatter`.

---

## 1. Sources surveyed

- Repository and canonical CLI documentation:
  - `https://github.com/keeganryan/flatter`

---

## 2. Extracted method/command surface

From README usage section:

- Main command:
  - `flatter [OPTION] [INPUT_FILE [OUTPUT_FILE]]`
- Documented options and constraints:
  - `-a ALPHA` (`0.5 < ALPHA <= 1`)
  - `-rhf R` (`R > 1`)
  - `-logcond C` (`C >= 0`)
  - `-p PREC` (`PREC >= 1`, with `0` auto mode)
  - `-t THRS` (`THRS >= 1`)
  - `-v`, `-q`, `-h`
- Input/output contract:
  - integer matrix text format,
  - default `stdin`/`stdout` behavior if file paths are omitted.

From README benchmark/testing section:

- `./test.sh`
- `./test_perf.py [NTRIALS] [NROWS] [START_R] [STEP_R]`
- `make test`

---

## 3. Domain notes captured for docs

- `flatter` is positioned as a Euclidean floating-point lattice reduction tool.
- No upstream surface advertises indefinite arithmetic-form genus/isometry APIs.
