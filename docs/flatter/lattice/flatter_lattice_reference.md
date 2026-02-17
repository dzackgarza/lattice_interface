# flatter Lattice Method Reference
## Floating-point LLL-style reduction CLI

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CLI]` | Command-line interface |
| `[EUCLID]` | Euclidean lattice setting |
| `[RED]` | Reduction workflow |
| `[UTIL]` | Benchmark/test utility surface |

---

## 1. Scope

`flatter` is an open floating-point lattice-basis reduction package with a CLI-centric interface.

Primary surface:

- `flatter` command with reduction-control options,
- repository benchmark/test scripts for reproducible runs.

Not in scope:

- indefinite arithmetic-form classification APIs.

---

## 2. CLI Surface

Upstream README documents the main command and options:

| Command / option | Description | Tags |
|------------------|-------------|------|
| `flatter [OPTION] [INPUT_FILE [OUTPUT_FILE]]` | Main reduction command. | `[CLI, EUCLID, RED]` |
| `-a ALPHA` | Reduction parameter (`0.5 < ALPHA <= 1`). | `[CLI, EUCLID, RED]` |
| `-rhf R` | Alternate reduction parameter based on root-Hermite factor (`R > 1`). | `[CLI, EUCLID, RED]` |
| `-logcond C` | Reduction parameter based on log-condition number (`C >= 0`). | `[CLI, EUCLID, RED]` |
| `-p PREC` | Precision in bits (`PREC >= 1`; default `0` uses auto mode). | `[CLI, EUCLID, RED]` |
| `-t THRS` | Number of threads (`THRS >= 1`; default `1`). | `[CLI, EUCLID, RED]` |
| `-v` | Verbose mode. | `[CLI, EUCLID]` |
| `-q` | Quiet mode. | `[CLI, EUCLID]` |
| `-h` | Help output. | `[CLI]` |

Input/output contract documented by README:

- Input/output matrix entries are integer and represented as plain-text matrices.
- Without explicit files, command reads input from `stdin` and writes output to `stdout`.

---

## 3. Utility Scripts

| Script / command | Description | Tags |
|------------------|-------------|------|
| `./test.sh` | Repository test helper script. | `[UTIL]` |
| `./test_perf.py [NTRIALS] [NROWS] [START_R] [STEP_R]` | Performance benchmark helper with optional dimensional controls. | `[UTIL, EUCLID, RED]` |
| `make test` | Build-system test target. | `[UTIL]` |

---

## 4. Domain Caveat

`flatter` is a Euclidean reduction package and does not expose indefinite-form genus/discriminant/isometry contracts.

---

## 5. Sources

- flatter repository/readme: `https://github.com/keeganryan/flatter`
- local provenance snapshot: `docs/flatter/upstream/flatter_online_provenance_2026-02-17.md`
