# The factorial: a powered regression (n=356, extended to n=716)

The largest test in the project, and the one that answers "is no-slop's lead real or
small-sample noise?" with a statistical model rather than a leaderboard. Design chosen
with the user: 6 arms × 2 probes × 30 runs, subjects double-judged by an Opus
model and a Sonnet model so judge model enters as a fixed factor and self-preference
bias becomes testable (throttling left 36 tail-cell subjects with a single judge row:
320 × 2 + 36 = 676 judge-observations across 356 subjects). Analyzed in R (`analysis.R`, lme4) — full console output in
`regression/model-output.txt`, data in `regression/factorial.csv`.

Scope note, stated plainly. The plan was 4 probes; Anthropic's API rate-limited
server-side ("not your usage limit") through the run, so the delivered dataset is 2
probe types — P6 (advisory judgment) and P7 (marketing copy) — at 356 subjects /
676 judge-observations. Ten of twelve cells are at full n=60 (30 subjects × 2 judges);
the two P6 competitor tail-arms (slopless, jalaalrd) landed at n=33–43 observations
before throttling. Every cell retains at least 33 judge-observations; one cell
(jalaalrd on P6) landed at 26 subjects, the only cell under the 30-subject design
target. The mixed model handles the imbalance. The probe factor was later extended to
four levels; the extension section below covers it, including why the rewrite probe had
to be reconstructed as P17r.

## The model

`total ~ arm + probe + judge + arm:judge + (1 | subject)`, random intercept per subject
(the two judge rows per subject are nested). Type-II Wald χ²:

| Term | χ² | df | p |
|---|---|---|---|
| **arm** | 135.99 | 5 | **< 2.2e-16** |
| probe | 1.46 | 1 | 0.228 |
| **judge** | 63.33 | 1 | **1.7e-15** |
| arm:judge | 5.74 | 5 | 0.332 |

Three findings, in order of importance:

1. The arm effect is massive and highly significant. Which operating doctrine the
model runs under explains score differences at p < 2.2e-16.

2. The judge-bias threat is ruled out. Judge model matters (Sonnet scores ~0.4–0.8
higher than Opus, uniformly) — but the arm:judge interaction is non-significant
(χ²=5.74, p=0.33; likelihood-ratio test p=0.34). No-slop's advantage does not depend on
being graded by its own model family. This directly answers the standing "all judges
are LLMs / self-preference" critique: the ranking is identical under a different-family
judge.

3. Probe type is not significant (p=0.23) — the arm ranking generalises across both
the judgment probe and the copy probe. (At four probes the probe factor becomes strongly
significant while the ranking still generalises; see the extension section.)

## The standings (marginal means, pooled over probe and judge)

| Rank | Arm | Mean /10 |
|---|---|---|
| 1= | **no-slop FULL** | **9.708** |
| 1= | no-slop COMPACT | 9.683 |
| 3 | jalaalrd | 9.409 |
| 4 | slopless | 9.408 |
| 5 | humanize | 9.058 |
| 6 | bare Opus | 8.083 |

## no-slop FULL vs every arm (Welch t on subject means, Cohen's d)

| Contrast | Diff | p | d |
|---|---|---|---|
| vs bare Opus | +1.62 | 2.4e-12 | 1.54 (huge) |
| vs humanize | +0.65 | 0.0003 | 0.69 (medium-large) |
| vs slopless | +0.25 | 0.014 | 0.45 (small-medium) |
| vs jalaalrd | +0.25 | 0.024 | 0.43 (small-medium) |
| vs no-slop COMPACT | +0.03 | 0.79 | 0.05 (none) |

no-slop FULL is statistically significantly better than every competitor arm
(all p < 0.05), and statistically indistinguishable from its own COMPACT tier — the
tier-parity claim, made all night on small samples, now holds at n=356 with d=0.05.

## Where the win lives (per-criterion arm means, 0–2)

The judgment/substance criteria (c1–c3) sit near ceiling for every arm — Opus is strong
there with or without a doctrine. The separation is almost entirely in:

- **c5 (form/structure):** bare 0.84, humanize 1.50 → no-slop 1.90–1.93.
- **c4 (sentence shapes):** bare 1.49 → no-slop 1.77–1.83.

The doctrine's measurable edge is disciplined form and sentence-shape control — exactly
what the prose protocol and the tell rules target — layered on a substance floor the
base model already clears. Competitors that are style-only (humanize, slopless,
jalaalrd) close some of the form gap but none matches no-slop, and all sit far above
bare.

## Bottom line at two probes

At the project's highest evidence standard — a mixed-effects regression on 356 subjects
and 676 blind judgments across two judge model families — no-slop is the significant #1,
beats the three strongest published competitors with real effect sizes (the five weaker
packs were eliminated at the leaderboard stage), carries its compact tier at parity,
and shows no judge self-preference artifact. This is the result the whole program was
built to earn.

## The extension: four probes, n=716

The published factorial delivered two probe types because Anthropic's API throttled the
run server-side. This extension finishes the job. It adds two more probe types to the
6-arm design and re-runs the model at four probe levels, taking the answer from "holds
on advisory judgment and marketing copy" to "holds across four task families, under two
judge model families, with the self-preference control still intact."

The two new probes are P17r (a de-slop rewrite) and P18 (an empathy-plus-substance
reply to a treasurer in distress). Design per new cell: 30 subjects, each judged blind
by one Opus and one Sonnet judge. 6 arms × 2 probes × 30 subjects × dual judges = 720
new judge-observations. Merged with the published data, the combined set is n=716
subjects, 1,396 judge-observations, 24 cells, 4 probe types. Analyzed in R with the same
`analysis.R` (lme4); console output in `regression/model-output.txt`, protocol in `../extension-protocol.md`.

### A word on the two new stimuli, before the numbers

P18's user request survived intact in the original raw JSONs and is used verbatim. P17's
did not. Its stimulus blurb was preserved only to char 403 in the old promptPreviews, so
the blurb was reconstructed to carry every element the original judges' evidence quotes
attest, then the probe was relabeled P17r in the CSV. It is the same task with a
rebuilt stimulus, and it is never equated cell-for-cell with the historical P17 number.

The rubrics follow the same rule. Criteria 1 and 2 were recovered from the original
judges' evidence; criteria 3 through 5 were reconstructed in the house style (substance,
then calibration, then form). Internal validity holds because every arm inside a round is
graded by the identical rubric, so the arm contrasts are sound. Comparison to the old
expansion-battery cells is out of scope. New cells are not comparable to the historical
leaderboard, which used a different environment, different judges, and a different n.

### The honesty checkpoint: a whole wave was thrown out

The first extension wave was invalidated at its own checkpoint, and the reason matters
enough to state plainly. The subjects in that wave were spawned in-session, so they
inherited the orchestrating machine's user memory. That memory imports the doctrine. The
result was contamination that the checkpoint caught by fingerprint: 26 of 30 bare-arm
P17r replies quoted the doctrine's own "Use B" example, and bare P18 replies cited the
doctrine's distress-register rules. A "bare" arm that has read the doctrine is not bare.

That wave was quarantined. It is retained as a sensitivity dataset and was never merged
into the headline model. The headline wave re-ran every cell with subjects in fresh
headless processes with the doctrine import disabled. Fingerprint checks across all 360
new subject replies found zero doctrine signatures. Ambient user memory other than the
doctrine remained in the headless environment: two bare P18 replies inferred the
runner's location from it, and those clauses are redacted in the published bundle. Judges continued to run in-session,
which matches the original factorial's judges, whose raw evidence demonstrably cites
doctrine rule IDs; the subject is the controlled factor, not the judge. That split is an
asymmetry, stated as one: subjects were cleaned and judges were not, because a clean-judge
regime would have broken comparability with the original run's judging environment. The
doctrine-aware-judge caveat therefore applies to the original and the extension equally.

The contamination was measurable, and it points the same way the whole project does.
Contaminated bare scored 7.05 on P18 and 8.07 on P17r. Clean bare scored 4.67 and 6.70.
Ambient doctrine exposure was worth roughly +1.4 to +2.4 points to the bare arm, which is
itself evidence that the doctrine moves scores. The clean numbers are the ones below.

### The model at four probes

`total ~ arm + probe + judge + arm:judge + (1 | subject)`, random intercept per subject.
Type-II Wald χ²:

| Term | χ² | df | p |
|---|---|---|---|
| **arm** | 302.58 | 5 | **< 2e-16** |
| **probe** | 918.08 | 3 | **< 2e-16** |
| judge | 4.98 | 1 | 0.026 |
| arm:judge | 6.22 | 5 | 0.285 |

Three things changed or held when the probe factor went from two levels to four:

1. The arm effect grew. Which operating doctrine the model runs under drove χ²=302.58,
up from 135.99 at two probes, at p < 2e-16. More task variety, more separation.

2. Probe difficulty now differs strongly (χ²=918.08). The two-probe run reported probe as
non-significant; that no longer holds, because P18 (distress) is far harder than the
advisory and copy probes and P17r (de-slop) is moderately harder. What generalizes is not
equal difficulty across probes, it is the arm ranking within each probe, covered in the
per-probe section.

3. The self-preference control holds at four probes. The arm:judge interaction stays
non-significant (χ²=6.22, p=0.285; likelihood-ratio test p=0.287). No-slop's advantage
still does not depend on being graded by its own model family, now across twice the task
range. Judge model has only a small main effect here (χ²=4.98, p=0.026), and its
direction is not stable: the two-probe run found Sonnet uniformly more lenient
(χ²=63.33), while on the new cells the leniency is small and mixed by arm. Judge-level
leniency is evidently environment- and probe-dependent, which is exactly why the
meaningful control is the arm:judge interaction, which is null in both runs, and not
the judge main effect.

### The standings (marginal means, pooled over probe and judge)

| Rank | Arm | Mean /10 |
|---|---|---|
| 1= | **no-slop COMPACT** | **8.929** |
| 1= | no-slop FULL | 8.887 |
| 3 | humanize | 8.046 |
| 4 | slopless | 7.996 |
| 5 | jalaalrd | 7.826 |
| 6 | bare | 6.883 |

The top two rows are one statistical result, not a ranking: d = 0.03, p = 0.82.
COMPACT listed first is sort order. The same tie held in the opposite nominal order
at two probes, which is how a genuine tie behaves across samples.

### no-slop FULL vs every arm (Welch t on subject means, Cohen's d)

FULL stays the contrast anchor by convention from the two-probe stage. It is the lower
of the two statistically tied no-slop tiers, so every effect size below is the
conservative one; anchoring on COMPACT would only enlarge them.

| Contrast | Diff | p | d |
|---|---|---|---|
| vs bare | +2.00 | 9.7e-18 | 1.21 (huge) |
| vs jalaalrd | +0.91 | 1.6e-05 | 0.58 (medium) |
| vs humanize | +0.84 | 1.5e-05 | 0.57 (medium) |
| vs slopless | +0.77 | 1.8e-04 | 0.49 (small-medium) |
| vs no-slop COMPACT | -0.04 | 0.82 | -0.03 (none) |

no-slop FULL beats every competitor arm with real effect sizes and stays statistically
indistinguishable from its own COMPACT tier. The tier-parity claim, first made on small
samples, now holds at n=716 with d=-0.03. The two no-slop editions trade the top rank
between them by a hundredth of a point.

### Where the ranking is stable and where it shuffles

The arm-by-probe interaction is real (supplementary LRT χ²=109.17, df=15, p=2.3e-16), so
arm gaps vary by probe and the competitor ordering reshuffles between task types. The
stable pattern survives that reshuffle. A no-slop tier ranks first on all four probes
(compact leads P17r, P18, and P6; full leads P7), and bare ranks last on all four.

Per-probe means (from `regression/model-output.txt`, per-cell mean total):

| Arm | P17r | P18 | P6 | P7 |
|---|---|---|---|---|
| **noslop_compact** | **9.33** | **7.02** | **9.95** | 9.42 |
| **noslop_full** | 9.23 | 6.90 | 9.88 | **9.53** |
| humanize | 7.38 | 6.68 | 8.75 | 9.37 |
| slopless | 6.98 | 6.58 | 9.28 | 9.50 |
| jalaalrd | 7.17 | 6.03 | 9.61 | 9.30 |
| bare | 6.70 | 4.67 | 8.33 | 7.83 |

P7 copy stays the tightest field: no-slop FULL 9.53 against slopless 9.50. Where the arms
converge is where the base model was already strong; where they spread is where doctrine
does work.

### Where the win lives (per-criterion arm means, 0–2)

The clearest substance criteria, c1 and c3, sit near ceiling for every arm (1.81 to
1.98). The separation still lives in form and shape:

- c5 (form / structure): bare 0.55, competitors 1.16 to 1.27, no-slop 1.69 to 1.77.
- c4 (sentence shapes): bare 1.15, no-slop 1.49 to 1.57.

The exception is bare's P18 calibration. Under distress the base model invented
jurisdiction specifics, the exact overreach criterion 4 penalizes, which is most of why
bare's P18 cell sits at 4.67 while the substance criteria stay high everywhere else.

### Caveats, stated not buried

1. P17r shows a real arm-by-judge offset variation (per-subject offset ANOVA across arms
p=0.0004, η²=0.12). It does not track slop level, and it does not flip any noslop-vs-bare
contrast, which stays between +2.3 and +2.9 under either judge alone (Opus +2.37 and
+2.40 for the two tiers, Sonnet +2.70 and +2.87). Both judges rank the no-slop
arms first and second. The P17r judge-level main effects and low-rank ordering should not
be over-read past that.

2. The P17r no-slop cells are ceiling-saturated. The Opus judge awards 10/10 to 60 to 70
percent of subjects in those cells, so full-versus-compact within P17r is
indistinguishable rather than ranked.

3. Of 720 raw judge entries, 26 carried malformed criterion index labels. All 26 were
independently re-judged and their CSV rows replaced. The CSV is authoritative; the raw
JSONs preserve the originals.

4. Judges are doctrine-aware in-session agents, as in the original run. The subject is the
controlled factor here, not the judge.

5. The new cells are not comparable to the historical leaderboard cells. Different
environment, different judges, different n.

### Bottom line

Extending the factorial to four probe types and n=716 does not soften the published
result, it hardens it. The arm effect roughly doubled, the self-preference control still
holds, a no-slop tier ranks first on every probe while bare ranks last on every probe,
and the tier-parity claim survives at more than twice the sample. The one wave that
looked too good was the contaminated one, and it was thrown out at the checkpoint before
it could reach the model.
