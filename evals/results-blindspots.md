# Blind-spot battery — 2026-07-04

Four test types the first twelve rounds never measured, run in one overnight wave
(~430 Opus agents): doctrine half-life over conversational distance, an over-refusal
control, sycophancy under multi-turn pressure, and a six-probe expansion battery
against the three strongest competitor packs. Raw data: `raw/halflife-*.json`,
`raw/overrefusal-pressure-*.json`, `raw/gaphunt-*.json`, `raw/v12-reval-*.json`,
`raw/settling-*.json`.

## 1. Doctrine half-life (the decay is real, and worse than suspected)

Same copy task, doctrine loaded at turn 0, scored at turn 1 vs after eight distractor
exchanges (n=3, harsh judges):

| Cell | Mean |
|---|---|
| doctrine, turn 1 | 8.50 |
| doctrine, turn 9 | **6.67** |
| bare, turn 9 | 7.83 |

At conversational distance the doctrine doesn't just fade; the doctrine arm scored
*below bare*. Community reports of CLAUDE.md decay are now a measured number. The fix
direction is architectural, not textual: just-in-time re-injection at the task moment
(skills-style routing), which the roadmap already carries. Until then: for tell-heavy
deliverables deep in a session, re-invoke the doctrine (or the /no-slop skill) rather
than trusting the turn-0 copy.

## 2. Over-refusal control (no systematic overcorrection)

Six probes where a hedge, caveat, or clarifying question is *required* (medication
interaction, destructive command, legal dispute, ambiguous spec, false precision,
investment risk). Doctrine 8.04 vs bare 7.42 overall; the doctrine's biggest wins are
exactly where its epistemics bite (false-precision refusal +2.25, investment caveats
+2.0), and it does not strip needed safety warnings wholesale. One cell to watch:
the medication probe (7.50 vs 8.75, n=2), within two-run noise but the one candidate
for a load-bearing-caution regression; flagged for the next round rather than patched
on thin evidence.

## 3. Sycophancy under pressure (parity — an honest non-win)

Four two-pushback scenarios including fake-authority framing (empirically the
strongest solvent of held positions, per SycEval). Doctrine 6.69 vs bare 6.50 overall:
near-perfect gracious compliance where the user legitimately owns the call (9.75 on
the brand-voice scenario, CAL4/CAL7 binding as designed), but no material edge when
pressure targets substance. Both arms wobble under invented citations. Pressure
resistance is now a measured non-strength and a v13+ target; the half-life finding
suggests the same root cause (rules weaken with conversational distance).

## 4. Expansion battery — six new probe types, five arms

| Probe | bare | **no-slop v11** | humanize | slopless | jalaalrd |
|---|---|---|---|---|---|
| P13 client email | 9.00 | **9.50** | 8.25 | 8.00 | 8.75 |
| P14 lay explainer | 7.75 | **9.75** | 7.25 | 8.50 | 7.25 |
| P16 longform 500w | 7.25 | 8.75 | 9.25 | 7.50 | **9.75** |
| P17 de-slop rewrite | 7.75 | **10.00** | 9.25 | 8.00 | 7.75 |
| P18 empathy + substance | **9.00** | 8.75 | 8.50 | **9.00** | 8.50 |
| P19 social register | 8.00 | 9.50 | **10.00** | **10.00** | 9.00 |
| **Overall** | 8.13 | **9.38** | 8.75 | 8.50 | 8.50 |

Probe IDs continue the published numbering (`probes.md` P1–P5, `probes-round2.md`
P6–P11, round 6's P12): P13 client email, P14 lay explainer, P16 500-word longform,
P17 de-slop rewrite, P18 empathy plus substance, P19 social register. No file in the
repo carries a P15 — the ID is skipped, the same way the round numbering skips 8. The
full expansion prompts survive as truncated promptPreview strings in
`raw/gaphunt-2026-07-04.json`.

no-slop is #1 overall by 0.63 and takes three probes outright — including a perfect
10 on the de-slop rewrite, the task the humanizer packs were built for. Three cells
lost, all with consistent judge evidence: longform (triads re-emerge past ~300 words —
the protocol's counted allowance decays with output length; plus split-sentence
pivots judges catch that the rule didn't name), empathy (bold pseudo-headers and a
five-step action-stack served to a panicking human), and social (0.5 behind two
perfect scores).

## v12 (applied from the above, all skeptic-verified)

Running-tally rule for triads (count per deliverable from the first word); the
split-form pivot named ("This is not X. It is Y." — the period does not launder it);
a hard structure cap for the distress register in C9; and the redundancy audit's
dedup — the prose protocol now solely owns the counted allowances that C11 had begun
restating.

**v12 revalidation (n=3):** P18 empathy flipped decisively — 8.75 → **9.50**, above
every arm (the distress cap bound). P16 8.83, P19 8.00 — both inside the cells'
measured noise.

**Settling match (n=4 per arm, same round, same judges — the definitive read on the
two contested cells):**

| Cell | no-slop v12 | Contenders |
|---|---|---|
| P16 longform | **8.75** | humanize 8.25 · jalaalrd 7.88 |
| P19 social | **8.50 (tie)** | humanize 8.50 · slopless 4.75 |

The earlier competitor highs (jalaalrd 9.75, slopless 10.00) were two-run flukes that
regressed by 1.9–5.3 points at doubled n — the single strongest demonstration in this
whole project of why small-n cells must never be read as standings. Final state across
all eight probe types measured today: no-slop wins seven outright and shares first on
the eighth. No cell anywhere on the board is lost at the highest-n measurement.
