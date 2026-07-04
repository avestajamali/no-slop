# docs

Presentation and review material for the no-slop project.

- [`FABLE-REVIEW.md`](FABLE-REVIEW.md) — the full handoff: a standalone audit brief that
  lets a fresh Claude Fable agent understand and check the entire project without the
  build conversation. Product, evidence chain with every n and p-value, methodology and
  its honesty caveats, open work, and a repo map.
- [`assets/`](assets/) — animated Claude Design SVGs used in the top-level README. They
  render and loop in GitHub markdown.

## The animated assets

| File | Shows | Loop |
|---|---|---|
| `assets/hero-leaderboard.svg` | The six regression arms racing to their measured means; no-slop first | 6s |
| `assets/before-after.svg` | Four documented machine-tell substitutions, tell to plain | 9s |
| `assets/significance.svg` | Cohen's d against every competitor arm, plus the tier-parity result | 6.5s |
| `assets/half-life.svg` | The measured decay: doctrine at turn 1 vs turn 9, turn-9 bare above it | 6s |

Every number in every asset traces to [`../evals/canonical-results.json`](../evals/canonical-results.json),
the single source of truth. If a doc and the JSON disagree, the JSON is correct and the
doc is the bug.
