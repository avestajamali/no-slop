# Fable review handoff

You are a fresh Claude Fable agent asked to audit no-slop before it goes public on
GitHub. This document is self-contained: it carries everything you need to understand
the product, check its evidence, and pick up the open work, without the conversation
that built it. Every number here is drawn from `evals/canonical-results.json` (version
v12, dated 2026-07-06), which is the single source of truth. Where a figure appears, it
matches that file exactly. If you find any number in the public docs that disagrees with
the canonical JSON, treat the JSON as correct and the doc as the bug.

## What the product is

no-slop is a behavioral doctrine plus an enforcement layer that makes Claude Opus write
and judge like a stronger model. The doctrine is a set of decision procedures — each with
a trigger, an action, and a failure mode — that transfer the working style of a frontier
model (distilled from extended work with Claude Fable 5) onto any capable model, primarily
Claude Opus. "Slop" is defined as any gap between what output performs and what it
delivers: the survey of options instead of the recommendation, the hedge instead of the
verdict, the confident claim that was never checked, the agreement the model does not
hold. The doctrine closes that gap with 45 rules across five pillars (epistemics, judgment,
design taste, communication, execution), a priority ladder that resolves rule collisions,
eight calibration cases, and a pre-send self-check.

The measured claim, stated at the product's highest evidence standard, is that no-slop is
the significant number one in its powered regression against the three strongest published
packs, with real effect sizes, no judge self-preference artifact, and a compact tier that
holds at parity; the five weaker retrieved packs were beaten head-to-head at the earlier
leaderboard stage.

## The five tiers

The doctrine ships in five forms so it can be deployed against different context budgets
and harness slots. Word counts and roles below are the canonical figures.

- FULL — about 5,700 words, the always-on identity edition. Maximum effect; load into
  always-loaded context so it shapes every response from the first token.
- COMPACT — about 3,900 words. All rule behaviors intact, rationale compressed. It
  matched FULL at n=716 with an effect size of d=0.03 (statistically indistinguishable; d=0.05 at the original n=356).
  The recommended tier when tokens matter.
- KERNEL — about 700 words, the top-procedures distillation. Doubles as a subagent
  preamble; it ends with a clause written specifically for delegated agents.
- SKILL — the invocable packaging (Claude Code skill). Loads the full doctrine on
  invocation with the kernel inlined as fallback.
- OUTPUT_STYLE — the harness-slot edition, for the output-style mechanism.

The enforcement layer that sits under the tiers has four parts: `lint_tells.py` (a
deterministic zero-dependency lint with 12 checks), a prefill guide, hooks plus an
artifact-to-file mechanism, and a reflect loop.

## The evidence chain

Every headline result below is from the canonical JSON, with its n and its p-value or
effect size attached. Read them in this order: the factorial is the load-bearing result,
the leaderboard is the head-to-head standings, and the blind-spot battery is the honest
accounting of where the doctrine is weak.

### The factorial (the load-bearing result)

This is the largest test in the project and the one that answers "is no-slop's lead real
or small-sample noise?" with a statistical model rather than a leaderboard.

Design: 6 arms × 2 probes (P6 advice, P7 copy) × 30 runs, subjects double-judged by
an Opus model and a Sonnet model; server throttling left 36 tail-cell subjects with a
single judge row. That gives n=356 subjects and n=676 judge-observations (320 × 2 + 36).
The model fit in R (lme4) was `total ~ arm + probe + judge + arm:judge + (1 | subject)`,
a random intercept per subject.

Type-II Wald results:

- arm effect: p < 2.2e-16. Which operating doctrine the model runs under explains
  score differences with the strongest significance the test can report.
- judge effect: p = 1.7e-15. Judge model matters; Sonnet scores about 0.4 to 0.8
  higher than Opus, uniformly.
- probe effect: p = 0.228 (not significant). The arm ranking generalizes across both
  the judgment probe and the copy probe.
- arm:judge interaction: p = 0.332 (not significant). This is the self-preference
  control, and it clears: no-slop's advantage does not depend on being graded by its own
  model family. The standing "all judges are LLMs, so this is self-preference" critique is
  answered directly — the ranking is identical under a different-family judge.

The 2-probe scope cap was later lifted. A 2026-07-06 wave extended the probe factor to
four types (P6, P7, P17r de-slop rewrite, P18 empathy) at n=716 subjects and 1,396
judge-observations. Probe difficulty now differs sharply (probe χ²=918.08, p<2e-16), but
the arm ranking still generalises: a no-slop tier ranks first on all four probes and bare
ranks last on all four, and the arm:judge self-preference interaction remains
non-significant (χ²=6.22, p=0.285). See `results-factorial.md`, the extension section.

Arm means (marginal, pooled over probe and judge, out of 10):

| Rank | Arm | Mean | n (obs) | Opus | Sonnet |
|---|---|---|---|---|---|
| 1 | no-slop FULL | 9.708 | 120 | 9.52 | 9.90 |
| 2 | no-slop COMPACT | 9.683 | 120 | 9.47 | 9.90 |
| 3 | jalaalrd | 9.409 | 93 | 8.98 | 9.78 |
| 4 | slopless | 9.408 | 103 | 9.02 | 9.68 |
| 5 | humanize | 9.058 | 120 | 8.88 | 9.23 |
| 6 | bare Opus | 8.083 | 120 | 7.75 | 8.42 |

no-slop FULL versus every other arm (Welch t on subject means, Cohen's d):

| Contrast | Diff | p | d |
|---|---|---|---|
| vs bare Opus | +1.62 | 2.4e-12 | 1.54 |
| vs humanize | +0.65 | 0.0003 | 0.69 |
| vs slopless | +0.25 | 0.014 | 0.45 |
| vs jalaalrd | +0.25 | 0.024 | 0.43 |
| vs no-slop COMPACT | +0.03 | 0.79 | 0.05 |

no-slop FULL is significantly better than every competitor arm (all p < 0.05) and
statistically indistinguishable from its own COMPACT tier (d=0.05). The tier-parity claim,
asserted on small samples earlier in the project, holds at n=356.

Where the win lives: the substance criteria (c1 to c3) sit near ceiling for every arm, so
Opus is already strong on judgment with or without a doctrine. The separation is almost
entirely in c5 (form and structure — bare 0.84 versus no-slop 1.92) and c4 (sentence
shapes). The doctrine's measurable edge is disciplined form and sentence-shape control,
layered on a substance floor the base model already clears.

### The competitive leaderboard

Every published competitor pack that could be retrieved was run head-to-head under
identical conditions on the two core probes; the three strongest were then carried into
six more probe types, giving each of the eight fields a highest-n, same-round comparison
under harsh blind judging. The competitor packs benchmarked: harshaneel/humanize, BioInfo/slopless,
jalaalrd/anti-ai-slop-writing, blader/humanizer (27k stars), adenaufal/anti-slop-writing,
hardikpandya/stop-slop, conorbronsdon/avoid-ai-writing, realrossmanngroup/no_ai_slop_writing_rules.

Final board, no-slop v12, highest-n per field:

| Field | no-slop score |
|---|---|
| P6 advice | 9.88 |
| P7 copy | 8.75 |
| P13 email | 9.50 |
| P14 explainer | 9.75 |
| P16 longform | 8.75 |
| P17 rewrite | 10.00 |
| P18 empathy | 9.50 |
| P19 social | 8.50 |

Result: won 7 of 8 fields outright, tied 1, lost 0 at highest n. Two structural findings
from the head-to-head worth carrying forward. The most-starred pack (blader/humanizer,
27k stars) underperformed, scoring below five smaller packs — stars measure distribution,
not effect. And every competitor is style-only: all operate on surface tells, none carries
epistemics, calibration, decision procedures, verification discipline, or agentic behavior.
Several explicitly optimize for AI-detector evasion, which no-slop deliberately does not:
its objective is writing that is right and plain, with undetectability as a side effect.

### Version progression

Advisory-probe total across doctrine versions (mixed n), showing the climb: v4 8.33,
v5 8.67, v5h 9.0, v6 8.75, v7 9.25, v11 confirmation 9.88.

### Scale of the program

About 3,900 agents total, 13-plus trial rounds, five adversarial panels, two judge model
families (Opus 4.8 and Sonnet 5).

## Methodology and its honesty caveats

The evidence is real but it has named limits. A Fable audit should confirm each of these
is disclosed in the public docs, not buried.

*LLM judges and the self-preference control.* All scoring is done by LLM judges, which
invites the "the judge shares the subject's biases" critique. The factorial was designed
to make that testable rather than assumed: subjects are judged by both an Opus model
and a Sonnet model (all but the 36 throttled tail subjects), judge enters the model as a
fixed factor, and self-preference shows up
as an arm:judge interaction. That interaction is non-significant (p=0.332), so the ranking
holds under a different-family judge. This is the control, and its result is the caveat's
answer, not a hand-wave.

*Small-n regression to the mean.* The single strongest lesson in the project is that
small-n cells must never be read as standings. In the blind-spot battery, two competitor
highs (jalaalrd 9.75 and slopless 10.00, both at n=2) regressed by 1.9 to 5.3 points when
n was doubled to 4 with same-round judges. Every contested cell in the final board was
settled at n=4 for this reason. Any Fable reviewer tempted to quote a single high or low
cell should check whether it survived a settling match.

*Server rate-limit scope cap.* The factorial was planned for 4 probe types; Anthropic's
API rate-limited server-side ("not your usage limit") through the run, so the delivered
dataset is 2 probe types (P6 advice, P7 copy). Ten of twelve cells reached full n=60; the
two P6 competitor tail-arms (slopless, jalaalrd) landed at 33 to 43 observations before
throttling, which is why their n in the arm table is below 120. Every cell retains at least
33 judge-observations (one cell, jalaalrd on P6, landed at 26 subjects, under the 30-subject
design target); the mixed model handles the imbalance. P17 and P18 remain available to
extend the probe factor when the server is calmer.

*The two documented floors.* Two behaviors persist that instruction alone did not fix.
First, the wrapper/preamble floor: agentic Opus at prompt position emits a one-line
preamble before a requested artifact regardless of the prompt (six variants tested,
magnitude shrank about 90%, the binary never flipped). The mechanical fix is the
artifact-to-file harness mechanism. Second, the half-life floor, now retired: the n=3
wave measured the doctrine at 8.5 on turn 1 but 6.67 after eight distractor exchanges,
below bare Opus at turn 9 (7.83). The n=8 halflife-2 replication overturned that read:
the doctrine held 9.06 against bare 8.31 at turn 9, and just-in-time re-injection was
directionally strongest at 9.25 (see results-blindspots.md).

*Blind-spot battery, the honest non-wins.* Over-refusal: doctrine 8.04 versus bare
7.42 overall, no systematic overcorrection, and the doctrine strengthens needed caveats
rather than stripping them. Pressure/sycophancy: doctrine 6.69 versus bare 6.50, parity, an
honest non-win, with graceful compliance where the user legitimately owns the call (9.75 on
the brand-voice scenario). Pressure resistance is a measured non-strength, flagged as a
future target rather than claimed as a win.

## The doctrine's design principles

The doctrine is built as decision procedures rather than trait adjectives, because
contrastive bad/good procedures measurably move model behavior where "be rigorous" does
not; it opens with a stance (senior collaborator judged on truth, goal-movement, and
finishedness) and a six-rung priority ladder (truthful reporting, irreversibility, the
evidenced goal, correctness before momentum, simplicity before ambition, momentum before
polish) that resolves collisions between rules by rank rather than by vibe. The five
pillars run epistemic discipline (ground every claim in what you observed; track observed
versus inferred versus assumed; treat a pattern-match as a hypothesis; a delegate's report
is testimony, not observation), judgment (make the call and expose the reasoning that would
let the user overrule it; know whose decision it is; resolve ambiguity by the cost of
guessing wrong), design taste (solve at the problem's own altitude; additions must earn
permanence; delete before you add; match the local idiom), communication (lead with the
verdict; report failure as plainly as success; calibrate certainty words to evidence;
deliver the artifact, not the making-of; the C11 machine-tells rule with its countable
seven-class prose protocol), and execution (read the whole request first; done is an
observation not a feeling; an error is information a verbatim retry throws away; secrets
travel by location, never by value). The self-check at the end is the pre-send pass that
each of these rolls up into.

## Open work a Fable agent could pick up

Prioritized, highest-leverage first. Each is scoped so you can start without more context.

1. **Extend the factorial to four probes. DONE (2026-07-06).** The probe factor now runs
   four levels — P6, P7, P17r (de-slop rewrite, stimulus reconstructed, so not equated with
   the historical P17) and P18 (empathy). The extended fit lands n=716 subjects and 1,396
   judge-observations across 24 cells: arm χ²=302.58 p<2e-16, probe χ²=918.08 p<2e-16 (probe
   difficulty differs sharply, but the ranking still generalises — a no-slop tier is first
   on all four probes and bare last on all four), and the arm:judge self-preference
   interaction stays non-significant (χ²=6.22, p=0.285). This is the single largest boost to
   the headline evidence, and it is in. See the extension section of `results-factorial.md`.

2. **Human-label calibration subset. Open, kit built.** The labeling kit exists; the
   labels themselves are not yet collected. Every score in the project is still an LLM
   judgment, so a stratified human-labeled subset correlated against the LLM judges — to
   validate the judge or quantify its bias — remains the deepest un-checked assumption in
   the evidence chain. Awaiting the labels.

3. **Just-in-time re-injection for the half-life decay. DONE (2026-07-06).** The
   re-injection arm was built and measured in the halflife-2 wave (n=8 per arm, dual-judged).
   Re-injecting the doctrine just before the task scored 9.25 against bare's 8.31 (d=0.94)
   and the turn-0 arm's 9.06, so it is directionally the strongest arm, consistent with the
   roadmap's architectural fix. The same wave also retired the old below-bare decay claim as
   an n=3 read that did not survive n=8. The re-injection margin over turn 0 (d=0.21) is not
   yet significant at this n. See the halflife-2 subsection of `results-blindspots.md`.

4. **Cross-model subject test. Open.** Every subject in the trials is still Claude Opus, so
   the doctrine's model-independence claim ("nothing in it depends on a specific model")
   remains asserted rather than measured; running the doctrine as subject on a non-Anthropic
   capable model would test whether the transfer holds off the family it was distilled from.

## Where every file lives

Repo root: the repository itself.

*Doctrine* (`doctrine/`):
- `FULL.md` — the complete doctrine, always-on identity edition.
- `COMPACT.md` — the validated middle edition.
- `KERNEL.md` — the ~700-word distillation and subagent preamble.
- `TELLS.md` — the machine-writing field guide behind rule C11, mapped to the doctrine
  rule that fixes each tell's root cause.

*Skill* (`skill/`):
- `SKILL.md` — Claude Code skill packaging; loads the full doctrine on invocation.

*Harness / enforcement layer* (`harness/`):
- `lint_tells.py` — deterministic, zero-dependency lint, 12 checks.
- `output-style-no-slop.md` — the output-style tier.
- `prefill.md` — assistant-prefill guide.
- `hooks.md` — Claude Code hook config.
- `reflect.md` — the reflect loop.
- `README.md` — harness overview.

*Evals* (`evals/`):
- `canonical-results.json` — the single source of truth for all numbers. Read first.
- `results-factorial.md` — the n=356 regression writeup (the load-bearing result).
- `leaderboard.md` — the competitive head-to-head across eight probe types.
- `results-blindspots.md` — half-life, over-refusal, pressure, expansion battery.
- `results.md`, `results-round2.md`, `results-rounds3-5.md`, `results-round6-7.md` — the
  trial-by-trial history that produced the version progression.
- `NIGHT-REPORT.md` — the overnight-wave summary.
- `README.md` — evals overview.
- `probes.md`, `probes-round2.md` — the probe definitions.
- `fixtures/` — planted-defect fixtures used by the probes (bugtrace, contam, notify,
  premise, reports, stats subfolders).
- `raw/` — every trial's raw JSON, one file per round (leaderboard, tournament, halflife,
  gaphunt, overrefusal-pressure, settling, audit-package, final-confirmation, v12-reval,
  and the numbered trials runs). These back the writeups; open them if a summary figure
  needs its source.

*Evals regression scorer* (`evals/regression/`):
- `analysis.R` — the lme4 model.
- `model-output.txt` — full R console output for the factorial.
- `factorial.csv` — the factorial dataset.
- `slop_index.py`, `style_distance.py` — deterministic lexical pre-screen scorers.
- `baseline.md`, `README.md` — the baseline table and regression overview.

*Root:*
- `README.md` — the public front door, with the deployment-tier instructions.
- `LICENSE` — the repository license.
- `docs/FABLE-REVIEW.md` — this document.
- `docs/README.md` — the docs-directory overview.
- `docs/assets/` — four animated SVGs the root README embeds.

One reading order for the audit: `canonical-results.json`, then `results-factorial.md` and
`regression/model-output.txt` together to check the headline stats against their source,
then `leaderboard.md` and `results-blindspots.md` for the standings and the caveats, then
`doctrine/FULL.md` for the product itself. If any public number disagrees with the
canonical JSON, the JSON wins.
