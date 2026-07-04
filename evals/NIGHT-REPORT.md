# Night run report — 2026-07-04 (01:31–06:00)

*Historical snapshot of the v9 overnight run. Current tier sizes and headline numbers
live in `canonical-results.json` (FULL ~5,700 and COMPACT ~3,900 words today).*

Autonomous overnight session. Everything below is local; nothing was committed or
pushed. Doctrine advanced v8 → v9; the package grew an enforcement layer, a regression
suite, and a compact edition.

## Built and validated

**1. Enforcement layer (`harness/`).** The seven-round finding was that two behaviors
(preamble-before-artifact, closing meta-offers) survive any prompt text. The harness
directory now closes them mechanically per surface: `lint_tells.py` (ten deterministic
checks as first built that night, twelve today, from TELLS.md, validated 7/7 on planted
slop, zero false positives on human prose, and it catches the exact preamble blind judges
flagged in archived transcripts), `prefill.md` (the absolute API-side kill), `hooks.md`
(PostToolUse lint + artifact-to-file routing), `output-style-no-slop.md` (generated from
FULL.md, installed to `~/.claude/output-styles/`), and `reflect.md` (a gated
lessons-learned loop for post-deployment evolution, designed around the ACE
context-collapse warning: anchored appends, never holistic rewrites).

**2. Regression suite (`evals/regression/`).** `slop_index.py`: deterministic
EQ-Bench-style lexical composite; baseline table generated over four archived rounds
(doctrine arms ≈ 0 on every probe; control nonzero exactly where judges said: P7
marketing 707.8, P12 memo 104.4). `style_distance.py`: Burrows' Delta stylometric
distance to the Fable reference corpus. Its first honest measurement: doctrine-Opus is
*not* closer to Fable's function-word register than control (0.802 vs 0.674 on P12) —
the doctrine transfers behavior, not weights-level register, and now there's a
deterministic metric proving where that boundary sits.

**3. Position experiment (round 9) — hypothesis falsified.** Removing the agent-harness
framing lines ("You are an assistant… your final message is your reply") changed
nothing: wrapper still 0.00, P6 identical (9.00), P12 slightly worse (4.83 vs 5.83).
One subject wrote "The memo is the deliverable, so it starts at its first word" *as its
preamble* — narrating the rule while violating it. The preamble attractor lives in the
model's agentic register, not the harness framing. This strengthens the enforcement
layer's case: it is not an optional accessory, it is the only fix.

**4. Criticism mining (all 204 sub-perfect judge criticisms, 7 rounds).** Cluster
analysis: 52 wrapper (confirmed floor), 44 headed-essay (confirmed fixed by v5–v7), 17
invented-specifics (confirmed fixed by v8), and four unaddressed clusters that became
v9's verified anchored edits — countable caps for triads (one per prose piece) and
em-dashes (two per 200 words) in C11; pasted-elsewhere artifacts ship bare, no
self-invented titles (C10); "do both, in parallel" must beat each single course on the
same evidence or it is the hedge wearing a verdict's clothes (J7); stated exclusions
("ignore," "handle separately") are constraints — they appear nowhere in the
deliverable (X0). FULL.md is now 5,255 words; deployed copy and output style
regenerated.

**5. Compact edition (`doctrine/COMPACT.md`, 3,200 words).** Distilled with all 45 rule
behaviors intact (independent coverage audit: zero missing, verdict ship). Fills the
tier gap between the kernel (~680 words) and FULL.

## Round 10 validation (COMPACT + v9, harsh blind judging)

| Arm | P6 advice | P12 memo | Notes |
|---|---|---|---|
| COMPACT (3,200 w) | **9.25** | **5.50** | Matches FULL's best-ever P6 (9.25, v7) and ties FULL's P12 — at 61% of the context cost. Validated as the recommended middle tier. |
| v9 FULL (5,255 w) | — | 5.50 | The X0 exclusions edit moved selection (crit2 1.00 → 1.50); do-both persists (crit1 1.00 — the same all-models-disagree-with-the-rubric convergence as rounds 6–7); wrapper 0.00, floor as expected. |

Round 10c completed the COMPACT tier evidence on the judgment probes (harsh judging,
workspace-inspecting judges): **P8 false-premise 10.00, P10 error-contamination 10.00,
P9 ambiguity 8.75** — the 39% cut holds the judgment ceiling. One P8 run is the
night's showcase transcript: refused the user's destructive instruction with evidence,
left the valid CSV byte-identical, fixed the real parser bug with the stdlib csv
module, and every claim in its report reproduced exactly on judge re-run.

v9's two P7-targeted edits (triad/em-dash numeric caps, no self-invented titles) were
validated separately in round 10b (P7 × 3, harsh judging, total 7.33): the
**bare-artifact rule bound** — zero self-invented titles (previously routine), em-dash
saturation gone, and disclosure flags now correctly placed after the copy instead of
woven through it — while the **triad cap did not bind** (criterion 4 = 0.50; subjects
produced 2–4 lists-of-three regardless). Third failed instruction attempt on triads →
per the night's division of labor, triad detection moved to `lint_tells.py` instead,
where it now mechanically flags the exact outputs the doctrine couldn't fix (verified
against the round-10b transcripts). Lexicon and promotional-register criteria held at
2.00. Those doctrine wins are stable.

## New mechanisms found in tonight's sweeps (not yet built)

- Petri (Anthropic, MIT) — spec-to-probe auditor/judge loops with eval-awareness
  mitigations; the natural next step for the conformance suite (one round-7 subject
  detected it was in an eval — Petri 2.0 addresses exactly that).
- Kiro-style rule routing — frontmatter-gated injection (always/auto/fileMatch)
  per doctrine section; plus its documented failure mode: always-rules not inherited
  by subagents, which no-slop's kernel-preamble already covers but a conformance probe
  should verify.
- rulesync / Ruler / microsoft-apm — compile one canonical doctrine to 20+ agent
  formats (CLAUDE.md, cursor rules, copilot-instructions, skills); plus
  `.claude-plugin/marketplace.json` for one-command install. The right packaging move
  before the public GitHub launch.
- DeepEval synthesizer — programmatic golden generation (input → filter → evolve →
  style) to grow the probe set per doctrine clause.
- repeng control vectors — the sub-prompt "slop dial"; not applicable to Claude
  (no activation access), documented as the boundary of what a prompt product can do.

## The 04:00 audit (post token-reset addendum)

With the fresh budget, a 23-agent pre-publication panel audited the whole package —
two hostile lenses on COMPACT.md (which had shipped on a single coverage-auditor's
testimony) and two coherence auditors across every doc. **19 findings confirmed, 0
rejected.** The big one: COMPACT had been distilled from v8 while the v9 edits were
being mined in the same parallel workflow — a race condition that left all four v9
clauses out of the shipping tier. All four restored in COMPACT's register (then ~3,400
words, 45 rules verified; ~3,900 today), plus a standalone-deployment pointer fix and the E2
settled-knowledge guard. The rest were doc coherence: stale word counts, a
"ten rounds" claim that didn't survive arithmetic, a missing style_distance mention,
a two-steps-that-were-three miscount in SKILL.md — all fixed, and the round-10 trial
scores stand as scores for the v8-distill (the restored clauses are additive; noted
here rather than silently absorbed into the parity claim). Process lesson recorded in
the README's updating section: every doctrine edit now lists COMPACT among the
distillations to re-check.

## The dogfood test

Before closing, the night's own documents went through `lint_tells.py`. It flagged
its author: 22 em-dashes in 877 words in this very report, triad saturation in the
evals index, highlighter-bold in the reflect doc. The product-facing files were fixed
(verified clean in the 04:00 audit pass); this report keeps its own findings as
evidence — the lint fires on a capable writer's genuine register, not just on
synthetic slop, which is exactly what a tells-check has to do to be worth shipping.
The exercise also improved the tool: two false-positive classes it exposed
(numbered-list run-in labels counted as highlighter bold; table rows and numeric
enumerations counted as triads) are now excluded, with the true positives re-verified
against the round-10b transcripts after each change.

## Honest limitations

- The true output-style test (an actual interactive Claude Code session with
  `/output-style no-slop`) cannot be run from inside workflow subagents; the artifact
  is installed and ready, but its in-session effect is unmeasured. First manual
  session tomorrow is the experiment.
- Round-9/10 cells are n=2–3; directional, not decisive.
- Style-distance and slop-index scales are arbitrary; both are for within-probe
  comparison and regression only.
