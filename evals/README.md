# Evidence index

Thirteen-plus blind-judged trial waves (about 2,700 agents), with all raw judge data
preserved and scrubbed: numbered rounds 1–10c, then the 2026-07-04 waves — the
competitive leaderboard, the evolutionary tournament, the n=356 factorial, and the
blind-spot battery with its settling matches. There is no round
8; that number went to a landscape survey, and the raw files skip it. Read in order,
or jump to the summary you need:

| Doc | What it covers |
|---|---|
| [`probes.md`](probes.md) | Round-1 probe design: five planted-defect tasks, one per doctrine pillar, with rubrics and the blind-judging protocol. |
| [`probes-round2.md`](probes-round2.md) | The harder round-2 probes: false premise, ambiguity, error contamination, thin-brief copy, and the three-arm (control/kernel/full) design. |
| [`results.md`](results.md) | Round 1: the doctrine moves calibration honesty and plain failure reporting by +1.0 each, and catches its own first induced failure. |
| [`results-round2.md`](results-round2.md) | Rounds 2: kernel tier validated; two negative findings that drove v5. |
| [`results-rounds3-5.md`](results-rounds3-5.md) | The iteration loop: what instruction fixed (naming the unit of analysis) and the measured floor it cannot fix (the artifact preamble). |
| [`results-round6-7.md`](results-round6-7.md) | The Fable benchmark: doctrine-Opus beats the unguided reference model on low-context advice; the high-context gap decomposed. |
| [`NIGHT-REPORT.md`](NIGHT-REPORT.md) | Rounds 9–10c: framing hypothesis falsified, criticism mining → v9, COMPACT tier validated across all probe classes, enforcement layer built. |
| [`leaderboard.md`](leaderboard.md) | The competitive head-to-head: every retrievable published pack across eight probe types, the v11 confirmation match, and the final standings. |
| [`results-blindspots.md`](results-blindspots.md) | The honest-limits battery: doctrine half-life, over-refusal control, sycophancy under pressure, the six-probe expansion, v12 revalidation and settling. |
| [`results-factorial.md`](results-factorial.md) | The powered regression: n=356 subjects / 676 blind judgments, 6 arms × 2 probes × dual judge models, lme4 mixed model. no-slop the significant #1 over every competitor; judge self-preference ruled out. |
| [`canonical-results.json`](canonical-results.json) | The single machine-readable source of truth: every headline number (regression, leaderboard, blind spots, tiers, scale) that the README, the animated assets, and the Fable handoff all draw from. |
| [`regression/`](regression/) | The R analysis (`analysis.R`), the factorial dataset (`factorial.csv`), the saved model output (`model-output.txt`), plus the deterministic pre-screens (Slop Index, stylometric distance) and baselines. |
| [`fixtures/`](fixtures/) | The planted-defect codebases. Each fails exactly as designed — verified before any trial used them. |
| [`raw/`](raw/) | Full trial JSON per round: every subject report and every judge's per-criterion scores with evidence quotes. Usernames scrubbed; machine paths scrubbed. |

Method notes that apply everywhere. Judges are blind: they never learn that other
arms exist, and they never learn which model produced a transcript. Scoring is 0–2
per criterion against fixed rubrics. Fixture probes are judged on actual workspace
state rather than self-reports. Cell sizes in the numbered rounds are n=2–4 (the factorial runs 30
subjects per cell; settling matches run n=4), so read small-cell per-criterion deltas
under 0.5 as noise, and remember that prompt-position delivery underestimates
identity-position deployment.
