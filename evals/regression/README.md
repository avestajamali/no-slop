# Regression suite

Deterministic pre-screens that run for free, so blind-judged trial rounds are spent
only on behavior that needs judgment.

- `slop_index.py` — length-normalized lexical composite (60% stock lexicon / 25%
  contrast-pivots / 15% slop trigrams, after EQ-Bench's published weighting). Run it
  on fixed-probe outputs from any new doctrine version and compare against
  `baseline.md`; a rise on any probe is a regression that must be explained before the
  version ships. `--trials RAW.json` scores archived trial files directly.
- `style_distance.py` computes Burrows' Delta stylometric distance to a reference
  corpus (function-word register). `--trials RAW.json --ref-arm fable` builds the
  reference centroid from one arm's reports and prints each arm's mean Delta per
  probe. Compare within a probe only; small-n numbers are directional. First
  measurement (round 6): the doctrine does not move function-word register toward the
  reference model. Behavior transfers; register does not.
- `../../harness/lint_tells.py` — the structural companion (preambles, scaffolds,
  saturation checks); `--fail` makes it a CI gate.

Workflow for any doctrine edit: (1) generate outputs on the fixed probes
(`../probes.md`, `../probes-round2.md` P12), (2) `slop_index.py` + `lint_tells.py`
them, (3) only if both are clean, spend a blind-judged round on the behavioral
criteria. Baseline numbers: `baseline.md`.

The powered factorial also lives here. `analysis.R` fits the mixed model over
`factorial.csv` and saves `model-output.txt`; `armprobe.R` runs the arm:probe
interaction test. `factorial.csv` now carries the four-probe extension (6 arms ×
P6, P7, P17r, P18 × 30 runs, 1,396 judge-observations across 716 subjects). The
published two-probe artifacts are preserved unchanged as `factorial-2probe.csv`
and `model-output-2probe.txt`; the P6/P7 rows in the extended file are a
byte-superset of that original. `halflife2.csv` holds the half-life replication's
per-subject rows.
