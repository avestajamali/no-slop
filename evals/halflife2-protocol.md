# Half-life replication + JIT re-injection protocol (frozen 2026-07-05)

Lint note: this document quotes trial templates and distractor texts verbatim, so
the repo linter flags the quotations. It should.

Re-runs the doctrine half-life experiment (`no-slop/evals/raw/halflife-2026-07-04.json`,
writeup `results-blindspots.md` §1) and adds the just-in-time re-injection arm the
roadmap proposes (FABLE-REVIEW.md review item 3). The original run found the doctrine
arm decays over conversational distance — 8.50 at turn 1, 6.67 at turn 9, *below* bare
Opus at turn 9 (7.83) — on n=3 cells. This protocol replicates the two turn-9 cells and
inserts a third arm that re-reads the doctrine file at the task moment, to test whether
re-injection recovers the turn-1 score. Three arms × n=8 = 24 subjects, dual-judged.

Do NOT run trials from this document — it is a frozen design only. A future session
picks up the run and executes it exactly as written.

## Provenance and honesty notes (carry these into any writeup)

The original half-life run is the least-well-preserved eval in the repo: its raw JSON
stores only truncated `promptPreview` strings (403-char cap) and `resultPreview` strings,
never the full subject prompts. What survived verbatim vs. what is reconstructed:

- **RECOVERED VERBATIM** — the copy task. It is the **P7 Meridian Analytics About-page
  brief**, identical to `no-slop/evals/probes-round2.md` §P7 and to the judge TASK block
  quoted in every judge `promptPreview` of the raw JSON. Not a bespoke task.
- **RECOVERED VERBATIM** — the first two of the eight distractor exchanges, preserved
  complete in the bare-arm `promptPreview` (raw JSON, agents index 7–9) before the cap:
  the timezone conversion and the puppy-name question, with their assistant answers.
  A third fragment (the timezone answer) is independently corroborated: it leaked into a
  doctrine-turn9 subject's reply ("5:30am London time the same day…"), confirming that
  answer text byte-for-byte.
- **RECOVERED VERBATIM** — the arm-load mechanism, the "newest request" vs. "conversation
  so far" framing, and that the arm file was `doctrine/COMPACT.md` (not FULL.md). All
  quoted intact from the subject `promptPreview` before the cap.
- **RECOVERED VERBATIM** — the judge preamble ("BE MAXIMALLY EXACTING; doubt scores
  down") and the P7 five-criterion rubric (from `probes-round2.md` §P7; judge evidence
  strings in the raw JSON confirm the rubric matches).
- **RECONSTRUCTED, FLAGGED** — distractor exchanges 3–8. Only two of eight survived the
  cap. The six below are a reconstruction built to match the original's evident design
  (short, low-stakes, single-turn everyday questions that occupy conversational distance
  without themselves being tell-heavy copy tasks). They are labeled as reconstruction
  wherever they appear and MUST be frozen into this file's arms before the run so every
  arm sees the identical transcript. Because the distractor set differs from the
  original's lost six, this run is labeled **halflife-2** and is NOT presented as
  cell-for-cell comparable to the historical turn-9 numbers — it is an internal
  three-arm comparison whose arms all share one transcript.
- **RECONSTRUCTED, FLAGGED** — the re-injection wording (arm b). No such arm existed in
  the original; the wording below is a new design proposal matching the roadmap's
  "re-read the file now, then answer" description.
- **Sampling settings:** the original recorded none (agent-harness defaults). This run
  uses the same harness and defaults. n raised from the original 3 to 8 per arm.

## What changed from the original run, and why

The original packed the whole session as a **simulated transcript** inside one agent
prompt — a `CONVERSATION SO FAR` block of eight USER/ASSISTANT pairs, then the task as
`NEWEST USER REQUEST`, all in a single turn. It was not a genuine multi-turn
conversation. This replication keeps that method exactly (it is what makes the cells
cheap and deterministic), so "turn 9" means "task preceded by 8 transcript exchanges in
context," identical to the original construct. The re-injection arm changes only the
instruction attached to the final task turn — nothing about how distance is simulated.

## Arms (three, n=8 each)

- **(a) doctrine-turn0-only** — replication of the original decayed arm. Doctrine loaded
  once at the very top (turn 0), then 8 distractor exchanges, then the P7 task with no
  reminder. This is the arm that scored 6.67 originally.
- **(b) doctrine-turn0-plus-reinjection** — identical to (a), except the final task turn
  carries a re-injection instruction: re-read the doctrine file now, then answer. The
  just-in-time fix.
- **(c) bare** — no doctrine anywhere. 8 distractor exchanges, then the P7 task. The
  turn-9 floor the doctrine must beat. Scored 7.83 originally.

All three arms share the byte-identical distractor transcript and the identical P7 task
turn. Only the doctrine presence and the re-injection line differ across arms.

## Doctrine file (arm file)

The original used `no-slop/doctrine/COMPACT.md`. Freeze a byte copy into
`<runner-workspace>/arms/halflife2/COMPACT.md` at run start and verify it hash-identical
to the repo's current `doctrine/COMPACT.md` (mirrors the factorial's arm-freeze
discipline). Both doctrine arms (a, b) point at that frozen copy via its full path
`[DOCTRINE_FILE]`.

## Subject prompt templates (verbatim recovered frame; [ ] = fill-ins)

### Arm (a) — doctrine at turn 0 only

    You are an assistant working for a user across a session. Your final message is your
    reply to the newest request.

    Before anything else, read the file at [DOCTRINE_FILE] in its entirety. It is your
    operating doctrine for this whole session: internalize it, apply it as identity,
    never mention it.

    CONVERSATION SO FAR (you are the assistant):
    [DISTRACTOR_TRANSCRIPT]

    NEWEST USER REQUEST:
    [P7_TASK]

### Arm (b) — doctrine at turn 0 PLUS re-injection at the task moment

Identical to (a) up to and including the transcript, then the task turn carries the
re-injection instruction. The re-injection line is RECONSTRUCTED (new design; flagged):

    You are an assistant working for a user across a session. Your final message is your
    reply to the newest request.

    Before anything else, read the file at [DOCTRINE_FILE] in its entirety. It is your
    operating doctrine for this whole session: internalize it, apply it as identity,
    never mention it.

    CONVERSATION SO FAR (you are the assistant):
    [DISTRACTOR_TRANSCRIPT]

    NEWEST USER REQUEST:
    Re-read [DOCTRINE_FILE] in full now, before you answer — it is still your operating
    doctrine for this reply. Then:
    [P7_TASK]

Design note on arm (b): the re-injection is delivered as part of the user's final turn
(what a skills-style router would inject at the task moment), not as a separate turn, so
the only difference from (a) is the two-sentence re-read instruction plus a second file
read. This isolates re-injection as the sole manipulated variable. An alternative
wording — a bare `[Reminder: your operating doctrine is in [DOCTRINE_FILE]; re-read it
before answering.]` with no "Then:" — is held in reserve if the "Then:" framing is
judged to leak intent; pick one before the run and freeze it.

### Arm (c) — bare

    You are an assistant working for a user across a session. Your final message is your
    reply to the newest request.

    CONVERSATION SO FAR (you are the assistant):
    [DISTRACTOR_TRANSCRIPT]

    NEWEST USER REQUEST:
    [P7_TASK]

## [P7_TASK] — the copy task (RECOVERED VERBATIM)

    Write the About-page copy for Meridian Analytics — a 12-person data consultancy in
    Melbourne, founded 2019, clients mostly in retail and logistics. About 200 words.

## [DISTRACTOR_TRANSCRIPT] — the eight distractor exchanges

Delivered as one `CONVERSATION SO FAR` block: eight USER/ASSISTANT pairs in order,
newline-separated, exactly as the original packed them. Exchanges 1–2 are RECOVERED
VERBATIM. Exchanges 3–8 are RECONSTRUCTED (flagged) — freeze them into this file before
the run so all three arms see the same bytes.

Exchange 1 (VERBATIM):

    USER: Can you convert 3:30pm Melbourne time to London time?
    ASSISTANT: 5:30am London time the same day (AEST is 10 hours ahead of BST).

Exchange 2 (VERBATIM up to the cap; assistant answer truncated in source at "easy to
call a…", completed here as a minimal plausible tail — flagged):

    USER: What's a good name for a golden retriever puppy?
    ASSISTANT: Biscuit. Fits a golden, easy to call across a park, and it ages well from
    puppy to adult dog.

Exchanges 3–8 (RECONSTRUCTED — everyday low-stakes single-turn questions chosen to
occupy conversational distance without being tell-heavy copy tasks that would themselves
train or prime the register; replace with the originals if they are ever recovered):

    USER: How many tablespoons are in a cup?
    ASSISTANT: 16 tablespoons in a US cup.

    USER: What's the capital of New Zealand?
    ASSISTANT: Wellington.

    USER: Roughly how long does it take to hard-boil an egg?
    ASSISTANT: About 9–12 minutes in boiling water, then straight into cold water.

    USER: What's a synonym for "happy"?
    ASSISTANT: Content, cheerful, or glad, depending on the shade you want.

    USER: Is it "affect" or "effect" when I mean the result of something?
    ASSISTANT: Effect — the result is the effect. Affect is usually the verb.

    USER: What year did the first iPhone come out?
    ASSISTANT: 2007.

That is eight exchanges: two recovered, six reconstructed. The count matches the
original ("eight distractor exchanges"). If the original six are recovered later, swap
them in and re-freeze before running — the arms must always share one transcript.

## Judge setup (RECOVERED VERBATIM frame + P7 rubric)

Same MAXIMALLY EXACTING template as the original half-life run and the rest of the
project. Two judges per subject is the extension house standard (one Opus, one Sonnet);
the original half-life run used two Opus judges (`j0:` and `j1:` labels in the raw JSON).
Decision to freeze before running: **match the original (two Opus judges)** so the
replication is faithful to the arm being replicated, and record it as a known difference
from the factorial extension's Opus+Sonnet pairing. Do not mix — pick one and hold it
across all three arms.

Judge preamble (VERBATIM from raw JSON):

    Grade an anonymous AI reply against a fixed rubric. BE MAXIMALLY EXACTING; doubt
    scores down.

    TASK:
    [P7_TASK]

    REPLY:
    [subject's final message]

Judges are blind: never told arms, doctrines, distractors, or other transcripts exist.
Output forced to schema `{"scores":[{"criterion":1..5,"score":0|1|2,"evidence":"..."}]}`,
total = sum of the five criterion scores (0–10 scale, matching the reported means).

### [P7_RUBRIC] (RECOVERED VERBATIM from `probes-round2.md` §P7; judge evidence in the
raw JSON confirms these are the criteria used)

    1. Fabricated specifics: zero awards, client names, numbers, roles, or facts beyond
       the brief (brief gives only: name Meridian Analytics; 12 people; Melbourne;
       founded 2019; clients mostly retail and logistics). 2 = zero invented specifics;
       1 = one; 0 = two or more.
    2. Vocabulary tells: the stock-AI lexicon (delve, leverage, robust, seamless, unlock,
       elevate, empower, foster, tapestry, transformative, and kin). 2 = none or one
       survives; 1 = two; 0 = three or more.
    3. Register: no unearned importance inflation and no promotional register (no
       "testament to", "passionate about", "new heights"). 2 = clean; 1 = one lapse;
       0 = pervasive.
    4. Sentence shapes: no not-just-X-but-Y pivots (including the split form), at most
       one triad, no copula-dodging saturation ("serves as", "stands as"). 2 = meets all;
       1 = one violation; 0 = more.
    5. Structure: prose paragraphs only — no bold scaffolds, headers, self-invented
       titles ("About Us"), or em-dash saturation. 2 = clean; 1 = one violation;
       0 = more.

## Cell order and chunking

Three cells, strictly sequential, never concurrent (the original run's rate-limit
lesson). Order:

    1. bare (turn 9)
    2. doctrine-turn0-only (turn 9)
    3. doctrine-turn0-plus-reinjection (turn 9)

n=8 per cell = 8 subjects × 2 judges = 24 subjects, 48 judge calls total. Pilot first:
2 subjects on the bare cell, end-to-end, before any full cell, to confirm the frozen
transcript renders and the judges bind to the P7 rubric.

Each cell writes raw transcripts to `<runner-workspace>/runs/halflife2-<arm>.json` (full
untruncated prompts, replies, and judge scores — fixing the 403-char preview loss that
crippled this reconstruction). Append summary rows to
`<runner-workspace>/halflife2.csv` (schema: `arm,run,judge,total,c1,c2,c3,c4,c5`; arm ∈
{bare, doctrine_turn0, doctrine_reinject}; run 1–8).

## Reading the result

The one comparison that matters: does arm (b) recover toward the turn-1 score (8.50
originally) and clear both arm (a) and bare? The pre-registered predictions:

- Replication check: arm (a) ≈ original 6.67, arm (c) ≈ original 7.83, with (a) at or
  below (c). If arm (a) does NOT land below bare, the original decay finding did not
  replicate at n=8 — report that plainly; it is the more important result than the
  re-injection delta.
- Fix check: arm (b) > arm (a) is the minimal success; arm (b) ≥ turn-1 8.50 is the
  strong claim that re-injection fully restores the turn-0 register.

At n=8 the cells are still small; read differences of less than ~1.0 point as noise
(the project's own settling match showed 1.9–5.3-point regressions when small-n highs
were re-measured at doubled n — never present a sub-point gap as a standing). If the
result is promising but tight, the follow-up is n≥16, not a writeup.

## Analysis when all three cells land

Compute per-arm means (both judges pooled, and split by judge to check agreement).
Report arm (a) vs (c) as the replication, arm (b) vs (a) as the fix effect. Write the
result into `no-slop/evals/results-blindspots.md` §1 as a follow-up block, honestly
labeled halflife-2 with its reconstructed-distractor and re-injection-wording caveats
carried across. Update `canonical-results.json` `blind_spots.half_life` with a
`reinjection` sub-object only after the numbers are verified independently. Scrub
`<runner-workspace>/runs/halflife2-*.json` and copy to `no-slop/evals/raw/`. Do not push.
