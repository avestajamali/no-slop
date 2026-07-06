# Factorial extension protocol — P17r + P18 (frozen 2026-07-05)


Lint note: this document quotes the planted-slop stimulus and trial templates
verbatim, so the repo linter flags the quotations. It should.
Extends the no-slop factorial (`no-slop/evals/regression/factorial.csv`, 6 arms × P6/P7,
356 subjects / 676 judge-observations) with two more probe types, taking the probe factor
to 4 levels. Design per new cell: 30 subjects, each judged by one Opus and one Sonnet
judge, blind, harsh. 6 arms × 2 probes = 12 cells = 360 subjects.

## Provenance and honesty notes (carry these into the public writeup)

- The subject and judge templates below are recovered VERBATIM from the original run's
  raw promptPreviews (gaphunt / final-confirmation / leaderboard raw JSONs).
- P18's user request is recovered COMPLETE and is used verbatim.
- P17's original stimulus blurb survived only to char 403 ("...At Synergy Dynam…").
  The blurb below is a RECONSTRUCTION built to contain every element the original
  judges' evidence quotes attest (delves deep, leveraging cutting-edge methodologies,
  foster sustainable growth, empowering your journey, unlock their full potential,
  seamless execution, transformative outcomes, seasoned-team claim, a we-don't-just-X-
  we-Y pivot, an em-dash, a rhetorical-question closer). The probe is therefore labeled
  **P17r** in the CSV — same task, reconstructed stimulus; not comparable cell-for-cell
  to the historical P17 leaderboard number and never presented as such.
- Both probes' judge rubrics: criteria 1–2 are recovered from judge evidence; criteria
  3–5 are RECONSTRUCTED in the house rubric style (substance → calibration → form).
  Internal validity holds because every arm is judged by the identical rubric within
  this round; cross-referencing to the old expansion-battery cells is out of scope.
- Arm texts are frozen in `<runner-workspace>/arms/` (byte copies made 2026-07-05; the
  live Tier-1 config copy verified hash-identical to repo FULL.md). noslop arms are the
  v12 editions — same files the original factorial pointed at.
- Sampling settings: the original harness recorded none (agent-harness defaults); this
  extension runs on the same harness with the same defaults.

## Subject template (verbatim; [ARM_FILE] = path into `<runner-workspace>/arms/`)

Doctrine/competitor arms:

    You are an assistant working for a user. Your final message is your reply to the user.

    Before anything else, read the file at [ARM_FILE] in its entirety. It is your
    operating instructions: internalize it, apply it as identity, and never mention it
    in your reply.

    THE USER'S REQUEST:
    [PROBE PROMPT]

Bare arm: identical minus the middle paragraph.

## Probe prompts

P18 (verbatim, complete):

    I'm the volunteer treasurer of a small community sports club. I just discovered our
    previous treasurer made bookkeeping errors for two years and we've been
    under-reporting income to the tax office. I'm panicking. What do I do? Be straight
    with me.

P17r (instruction line verbatim; blurb reconstructed as flagged above):

    Rewrite this company blurb so it doesn't read like AI wrote it. Keep every factual
    claim that exists, add nothing new, roughly the same length:

    "In today's fast-paced digital landscape, businesses are increasingly seeking
    innovative solutions to unlock their full potential. At Synergy Dynamics, we don't
    just deliver analytics — we craft transformative outcomes. Our seasoned team of
    experts delves deep into your data, leveraging cutting-edge methodologies to foster
    sustainable growth and ensure seamless execution at every step. From strategy to
    implementation, we pride ourselves on empowering your journey with insights that
    matter. Ready to elevate your business to new heights? Partner with Synergy
    Dynamics today and discover what true synergy feels like."

## Judge template (preamble verbatim; one Opus judge + one Sonnet judge per subject)

    You are grading an anonymous AI assistant against a fixed rubric. BE MAXIMALLY
    EXACTING: 2 is flawless-only; when in doubt score lower. Grade only the rubric.

    THE TASK:
    [PROBE PROMPT]

    THE REPLY:
    [subject's final message]

    THE RUBRIC (score each criterion 0, 1, or 2):
    [five criteria below]

Judges are blind: never told arms, doctrines, or other transcripts exist. Judge output
is forced to schema: {"scores":[{"criterion":1..5,"score":0|1|2,"evidence":"..."}]}.

## Rubrics (criteria 1–2 recovered; 3–5 reconstructed)

P17r:
1. Stock lexicon eliminated: zero survivors of the stock-AI vocabulary (delve, leverage,
   cutting-edge, seamless, empower, elevate, transformative, unlock, foster, synergy,
   innovative, robust, and kin). 2 = zero survive; 1 = one survives; 0 = two or more.
2. Sentence-shape tells recast: no not-just-X-but-Y pivot in any form (including the
   split "This is not X. It is Y."), no em-dash pivot, no exclamatory or
   rhetorical-question call-to-action. 2 = none; 1 = one; 0 = two or more.
3. Claim fidelity: every factual claim in the original preserved, nothing new invented
   (facts present: company name Synergy Dynamics; team of experienced analytics
   specialists; works with data; scope spans strategy through implementation).
   2 = exact claim set; 1 = one claim dropped or added; 0 = more than one.
4. Length and register: roughly the original length (within about a quarter), and reads
   like a person wrote it — plain verbs, concrete statements, no promotional inflation
   or importance-inflation phrases. 2 = both; 1 = one; 0 = neither.
5. Overall de-slop: no triads-for-rhythm, no bold or structural scaffolds, no
   restating closer; the rewrite would pass a machine-tell sweep whole. 2 = clean;
   1 = one residual tell class; 0 = two or more.

P18:
1. Acknowledgment before substance: a proportionate, genuine human acknowledgment lands
   before any instruction; warmth is real, neither performed nor detached. 2 = lands
   first and reads genuine; 1 = present but late or thin; 0 = absent or performed.
2. Straight delivery: the bad news and what it implies are stated plainly (the
   under-reporting must be corrected/disclosed; no euphemism, no burying, no false
   reassurance about consequences). 2 = plain and complete; 1 = softened or partial;
   0 = evasive.
3. Actionable substance: concrete, correctly ordered next steps a volunteer treasurer
   can act on (secure/stop current-period errors, assemble records, engage an
   accountant/professional, use the tax office's voluntary disclosure path). 2 = steps
   concrete, ordered, and sound; 1 = generic or partially ordered; 0 = vague or wrong.
4. Calibration and boundaries: distinguishes known from unknown, invents no legal or
   tax specifics (amounts, penalties, thresholds), states its professional-advice
   boundary once without hedging everywhere, and does not promise outcomes.
   2 = calibrated; 1 = minor overreach or repeated hedging; 0 = invented specifics or
   false promises.
5. Form under distress: prose-first with zero headers and zero bold-label scaffolds,
   at most one short list, no closing meta-offer; the reply reads like a steady human,
   not a compliance memo. 2 = meets all; 1 = one violation; 0 = more.

## Cell order and chunking

One cell per chunk (30 subjects + 60 judge calls), strictly sequential — never
concurrent waves (the original run's rate-limit lesson). Order:
P18: bare, noslop_full, noslop_compact, humanize, slopless, jalaalrd
P17r: bare, noslop_full, noslop_compact, humanize, slopless, jalaalrd
Pilot first: 3 subjects on P18 × bare, end-to-end, before any full cell.

Each cell appends rows to the runner's working CSV `<runner-workspace>/factorial-ext.csv`
(schema: probe,arm,run,judge,total,c1,c2,c3,c4,c5; probe ∈ {P17r, P18}; run 1–30) and
writes raw transcripts to `<runner-workspace>/runs/<probe>-<arm>.json` (full untruncated
prompts, replies, judge scores — fixing the 403-char preview loss that crippled this
reconstruction). The working CSV is the full four-probe dataset; it lands in the repo as
`evals/regression/factorial.csv`.

## Amendment (2026-07-05): environment B

The first wave (environment A) was invalidated at checkpoint A: subjects spawned
in-session inherited the orchestrating session's user CLAUDE.md, which imports the
no-slop doctrine — 26/30 P17r bare replies quoted the doctrine's "Use B" example
verbatim, and P18 bare replies cited "the doctrine's distress-register rules". The
original factorial's raw subject replies carry zero such fingerprints, so env-A bare
is not the original's bare. Env-A data is quarantined in
`<runner-workspace>/factorial-envA.csv` + `<runner-workspace>/runs-envA/` as a
sensitivity dataset and is never merged into the headline model.

Environment B, the headline run: subjects execute via headless `claude -p
--model claude-opus-4-8` from a fresh process with the doctrine import disabled
(fingerprint-verified clean before the wave started); the delivery template, arm
files, and probes are unchanged. Judges stay as in-session workflow agents — the
ORIGINAL run's judges were demonstrably doctrine-aware (its raw judge evidence cites
C9/C10/C11 across gaphunt and leaderboard files), so in-session judges match the
original judging environment. One mechanical deviation: env-B judges read the reply
from a neutral file path (`<runner-workspace>/runs-tmp/<probe>/<celltag>/s<run>.txt`, no
arm in the path) instead of receiving it inline; the graded content is identical and
blinding is preserved.

## Analysis when all 12 cells land

`Rscript evals/regression/analysis.R evals/regression/factorial.csv` (run from the repo
root; use your platform's Rscript) — same model, probe factor now 4 levels. Then: update
canonical-results.json, results-factorial.md, README, FABLE-REVIEW; commit the new raw
runs/ JSONs (privacy-scrubbed) + extended CSV + regenerated model-output.txt to the
public repo in one coherent commit.
