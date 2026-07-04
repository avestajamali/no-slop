# no-slop — rounds 6–7: the Fable benchmark

The question this round answers: **how close does no-slop push Opus 4.8 toward Claude
Fable 5, the model the doctrine was distilled from?** Three arms — Opus 4.8 bare, Opus
4.8 + doctrine (read from file at session start, Tier-3-style delivery), and bare Fable
5 as the reference — on one low-context probe (P6, the advisory question, with five
rounds of baselines) and one new higher-context probe (P12: a ~500-word noisy decision
dump — 12 support tickets with planted red herrings, dueling engineer estimates with a
bad track record, a $340k renewal deadline — "decide patch-vs-rebuild, write the decision
memo"). Judging was deliberately harsher than rounds 2–5: 2 is reserved for flawless,
doubt scores down, any preamble before a requested artifact zeroes the form criterion.
Two blind judges per transcript; judges never told that any arms or models differ, nor
that a doctrine exists.

## Results (max 10, mean of runs)

| Probe | Opus bare | Opus + doctrine | Fable bare |
|---|---|---|---|
| P6 low-context (advice) | 8.00 | **9.00** | 8.00 |
| P12 high-context (memo) | 5.50 | 5.50 → **5.83** (v8) | 7.50 |

## The three findings

**1. On the low-context probe, doctrine-Opus beat bare Fable.** Fable's substance was
flawless (2.00 on all four content criteria) but unguided Fable delivered the advice as
a headed document with a planning preamble — form 0.00, the same trained agent-harness
habit Opus has. The doctrine got Opus to 1.00 on form under harsh capping. The
conclusion cuts both ways: the doctrine transfers real behavior Opus lacks, and the
behaviors it encodes are ones even its source model only exhibits when so directed —
which is precisely the argument for running the doctrine rather than trusting any
model's defaults.

**2. On the high-context probe, Fable's +2.0 edge decomposes into one large piece and
two small ones.** Artifact delivery: Fable produced the memo starting at its first
word in both runs (2.00); Opus arms preambled (0.00–0.50). Micro-epistemics: Opus arms
asserted a colleague's advocacy numbers as fact and invented an unearned estimate
("the bisect is roughly a day"); Fable did some of this too (1.50) but less. Selection:
all arms scored 1 — Opus-doctrine dropped one load-bearing metric, control and Fable
answered the noise items the brief said to handle separately.

**3. The v8 fixes bought what instruction can still buy — and confirmed the floor.**
Two clauses added from round-6 evidence (human testimony is testimony: attribute, don't
restate as fact; doctrine-narration is leaked thinking: cut it) moved epistemics from
1.25 to 1.50 and the decision criterion from 1.00 to 1.33. Total: 5.50 → 5.83. The
wrapper stayed at 0.00 — every subject preambled and appended a closing offer ("say
which and I'll write it"), consistent with the floor documented in
`results-rounds3-5.md`.

## Judgment on the rubric itself, honestly

P12's decision criterion scored 1 for every arm *including Fable*: all seven subjects
across three models independently chose "ship patches now + gate/timebox the rebuild
in parallel" over the rubric's preferred "defer the rebuild decision until after
renewal." Convergence at that level across models indicts the rubric's preferred
answer, not the models. The gated-parallel plan engages the estimate-history risk
explicitly and is arguably the better decision. Read P12 criterion-1 scores as rubric
strictness, not model failure. One v8 run is additionally contaminated: the subject
inspected its working directory and recognized the trial fixtures, then said so in its
reply.

## Bottom line

- Low context: the doctrine takes Opus 4.8 past the unguided reference model. Nothing
  left to close.
- High context: the doctrine + v8 closes roughly a third of the measurable
  non-wrapper gap; the remaining ~1.5 points sit almost entirely in one behavior —
  reply-starts-at-the-artifact — which six variants over seven rounds shrank but never
  eliminated at prompt position, and which bare Fable does natively in memo-shaped
  tasks. Deployed mitigations (identity-position loading, extended thinking) are the
  lever left; more prompt text is not.
- The doctrine ships as v8 (~5,050 words): the round-6/7 additions are E8's
  human-testimony clause and C10's doctrine-leak cut rule.
