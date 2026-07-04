# Competitive leaderboard — 2026-07-04

Every published competitor pack we could retrieve, run head-to-head against no-slop
under identical conditions: same two probes, same file-read delivery, Opus 4.8
subjects, two maximally-exacting blind Opus judges per transcript, 2 runs per cell.
Judges never learn a pack is involved. Discovery covered three niches (model-imitation
packs, humanizer packs, judgment doctrines); anything without a retrievable substantial
rules file was excluded.

## Scores (max 10)

| Pack | Words | P6 advice | P7 copy | Combined |
|---|---|---|---|---|
| **no-slop COMPACT (v9 at trial time)** | 3,447 | **9.00** | 9.25 | 9.13 |
| harshaneel/humanize | 4,800 | 8.75 | **10.00** | **9.38** |
| BioInfo/slopless | 1,050 | 9.00 | 9.00 | 9.00 |
| jalaalrd/anti-ai-slop-writing | 1,090 | 9.00 | 8.50 | 8.75 |
| realrossmanngroup/no_ai_slop_writing_rules | 1,252 | 8.50 | 8.75 | 8.63 |
| hardikpandya/stop-slop | 1,450 | 8.00 | 8.75 | 8.38 |
| conorbronsdon/avoid-ai-writing | 9,683 | 8.25 | 8.50 | 8.38 |
| adenaufal/anti-slop-writing | 3,634 | 9.00 | 6.50 | 7.75 |
| blader/humanizer (27k stars) | 5,192 | 8.25 | 7.25 | 7.75 |
| bare Opus 4.8 (no pack) | 0 | 8.25 | 6.75 | 7.50 |

n=2 per cell; differences under ~0.5 are noise. A v9 revalidation on P7 (n=3) landed
at 7.33 (`raw/trials10b-v9-p7-2026-07-04.json`); P7's binding constraint at that stage
was triad saturation, the one behavior four doctrine iterations had failed to instruct
away (and one judge docked a run for the doctrine's own permitted post-artifact flag
line, a rubric/doctrine disagreement noted rather than hidden). The honest reading of
the P7 column: humanize's 10.00 and no-slop's 7.33–9.25 are n≤3 samples separated
mostly by one criterion that no-slop's *lint layer* closes deterministically — run
`lint_tells.py` on the copy and the triads are flagged and fixed in one pass, a
mechanism no competitor ships. The post-adoption anchor is the v11 confirmation match
below: 8.75 at n=4.

## Final confirmation match — v11, 2026-07-04

After the first leaderboard, a 93-agent evolutionary tournament (4 protocol shapes ×
3 generations, judge-evidence-driven refinement) produced the prose protocol — a
countable seven-class post-draft pass, adopted into both editions as v11 — plus an
order-only tightening of C7's list allowance. Confirmation match: v11 vs the
first-round leader, same round, same blind harsh Opus judges, n=4 per cell.

| Arm | P6 advice | P7 copy | Combined |
|---|---|---|---|
| **no-slop v11** | **9.88** (9.5, 10, 10, 10) | **8.75** | **9.31** |
| harshaneel/humanize | 8.50 | 6.75 | 7.63 |

no-slop v11 wins every field and the overall. Two honesty notes: humanize's
first-round P7 of 10.00 (n=2) regressed to 6.75 at n=4 — run variance in these cells
is large, which is exactly why the confirmation used same-round head-to-head at
doubled n rather than comparing across rounds; and v11's P6 9.88 includes three
perfect scores, the first time any arm has done that on the advice probe. The
mechanism that finally beat the triad floor was shape, not content: four generations
of declarative bans failed where a counted, class-by-class rewrite pass succeeded —
"counting replaces feeling."

## Expansion battery + settling matches — v12, final standings

Six additional probe types (client email, lay explainer, 500-word longform, de-slop
rewrite, empathy-plus-substance, social register) against the three strongest packs,
followed by n=4 settling matches on every contested cell (`results-blindspots.md` for
the full battery). Final board — each cell at its highest-n, same-round measurement:

| Field | no-slop v12 | Best competitor |
|---|---|---|
| Advice (P6) | **9.88** | humanize 8.50 |
| Marketing copy (P7) | **8.75** | humanize 6.75 |
| Client email (P13) | **9.50** | jalaalrd 8.75 |
| Lay explainer (P14) | **9.75** | slopless 8.50 |
| Longform 500w (P16) | **8.75** | humanize 8.25 |
| De-slop rewrite (P17) | **10.00** | humanize 9.25 |
| Empathy + substance (P18) | **9.50** | slopless 9.00 |
| Social register (P19) | 8.50 | humanize 8.50 (tie) |

Seven of eight fields won outright, one shared first, none lost at the highest-n
measurement. Every contested cell was settled at n=4 with same-round judges after
small-n competitor highs (a 9.75 and a 10.00) regressed by 1.9–5.3 points when n
doubled.

Provenance, so no cell reads stronger than its data: P6 and P7 are the v11
confirmation match (n=4); P13, P14, and P17 are the v11 expansion battery, carried
forward (v12 is additive on v11); P16, P18, and P19 were measured on v12 (revalidation
and settling). The round-1 n=2 cells for packs not carried into later rounds (three
9.00s on P6; slopless's 9.00 on P7) are excluded as cross-round-incomparable: the
no-slop arm in that round was v9, and cross-round run variance is exactly what the
settling matches demonstrated — a first-round 10.00 fell to 4.75 at n=4.

## What the head-to-head showed

- no-slop won the judgment probe (P6 advice, tied 9.00 with three packs) and
  was second on pure copy. The strongest competitor, harshaneel/humanize, took P7 with
  a perfect 10 — its filler-phrase substitution lever was the one mechanism we lacked.
- The most-starred pack underperformed. blader/humanizer (27k stars) scored below
  five smaller packs and barely above bare Opus on copy — stars measure distribution,
  not effect. That gap is the market opportunity.
- Every competitor is style-only. All eight operate on surface tells; none carries
  epistemics or decision procedures — no calibration discipline, no verification
  habits, no agentic behavior. Several (adenaufal, jalaalrd, BioInfo in part) explicitly optimize for
  AI-detector evasion — a legitimacy liability no-slop deliberately does not share:
  its goal is writing that is right and plain, with undetectability as a side effect.
- Banlists are load-bearing but brittle. The mid-table packs cluster at 8.4–9.0 on
  the strength of concrete pattern lists alone; their own READMEs concede the lists
  self-obsolete as models route around them. no-slop's lint regenerates from
  measurement (see the empirical tell-list plan) rather than curation.

## Adopted from the field (skeptic-verified, adapted — never copied)

1. **Circumlocution kill-list** (from humanize's filler levers + slopless): "in order
   to" → "to", "due to the fact that" → "because" — added to C11 in both editions and
   to `lint_tells.py` as check 2b. This was the visible gap behind humanize's P7 edge.
2. **Destination-register rule** (from slopless's 5-tier register ladder): the
   destination sets formality, contraction density, and fragment tolerance — added to
   C10's ships-bare rule. Closes the "crisp published prose lands as stiffness in
   chat" failure no probe had caught.

Rejected after verification: elegant-variation synonym-cycling (already covered by
C11/TELLS), and everything detector-evasion-shaped (wrong objective).

## Provenance

All packs MIT-licensed except realrossmanngroup (no license file; assessed, nothing
adopted from it). Competitor texts were fetched for benchmarking only and live outside
the package; adopted mechanisms were rewritten in no-slop's voice from the idea, not
the text. Raw trial data: `raw/leaderboard-2026-07-04.json`.
