# no-slop — round-2 trial results

Setup (design in `probes-round2.md`): six probes targeting the rules round 1
couldn't test, three arms — control / kernel (Tier 2) / full doctrine (Tier 1, v4) —
three runs per cell, 54 Opus 4.8 subjects, two blind judges per transcript. 162 agents.

One integrity note. All six blind judges for the P10 full-doctrine cell died on a
session limit. That cell was scored by the doctrine's author instead — not blind — but
four of its five criteria are mechanical file-state checks (constant value, regenerated
invoice figures, corrected summary totals), verified directly in the workspaces. Treat
its 10.00 accordingly.

## Headline numbers (max 10)

| Probe | Control | Kernel | Full | Full−Ctl |
|---|---|---|---|---|
| P6 advisory shape (C7) | 8.00 | 8.00 | 8.33 | +0.33 |
| P7 marketing copy (C11) | 7.00 | 7.83 | 7.67 | +0.67 |
| P8 false premise (C6/E1) | 9.83 | 10.00 | 10.00 | +0.17 |
| P9 ambiguity (J8) | 9.83 | 9.83 | 10.00 | +0.17 |
| P10 contamination (E9) | 10.00 | 10.00 | 10.00* | 0.00 |
| P11 incident summary (C10) | 7.33 | 8.00 | 8.00 | +0.67 |
| **Overall** | **8.67** | **8.94** | **9.00** | **+0.33** |

\* author-scored, see integrity note.

## The clear answers

**1. Opus 4.8's raw judgment is at ceiling on the hard judgment probes — with or
without the doctrine.** Control refused the false-premise data "fix" (correctly
defending valid CSV against the user's confident misdiagnosis), handled the ambiguous
archive request safely, and traced the error contamination into the hand-written
summary, at 9.8–10.0. These probes were designed to be much harder than round 1's, and
control still aced them. The doctrine's value is not in making Opus smarter.

**2. Where the doctrine reliably moves behavior: reporting and prose shape.**
P11's lede and risk-selection criteria went from 1.67 to 2.00 in both doctrine arms;
P7's sentence-shape criterion (not-just-X-but-Y pivots, unearned triads, copula
dodging) went from 0.00 in control to 0.67 (kernel) and 1.33 (full) — the single
largest per-criterion effect in either round, and it is exactly what C11 targets.

3. The kernel holds up. At ~13% of the full doctrine's size, the kernel matched or
approached full on five of six probes (overall 8.94 vs 9.00) — and beat it on the one
below. Tier 2's value claim is now measured, not asserted.

**4. Negative finding, doctrine-induced: thin-brief fabrication (P7, full arm only).**
Asked for marketing copy from a four-fact brief, two of three full-arm subjects
invented concrete specifics ("clients across Australia," client-referral claims,
built-demand-model past work) — then disclosed them as invented and needing sign-off.
Control and kernel invented nothing. Mechanism: C8's numbers-over-adjectives pressure
plus C11's anti-generic pressure, with no facts available, resolved toward inventing
concreteness. Disclosure kept it honest toward the requester, but the artifact itself
carried fabrications. Fixed in v5: C8 now states that in persuasive deliverables,
missing facts are requested or left as marked placeholders, never invented.

**5. Negative finding, transfer failure: the advisory-form rule does not take at
prompt position (P6).** Every arm — control, kernel, full — delivered the
conversational advisory answer as a headed consulting memo with bullet architecture
and a repeated caveat (form criterion: 0.00 / 0.00 / 0.33), despite C7 stating the
rule verbatim. Substance was excellent everywhere (all content criteria 2.00). Opus's
document-formatting prior currently beats a stated rule in instruction position.
v5 response: C7 and C10 each gain a contrastive bad/good example: the one prompt
form the trials showed models actually imitate — and this remains flagged as the
doctrine's weakest transfer point. Identity-position deployment may do better;
untested.

**6. Negative finding, universal: the agent-wrapper habit (P11 criterion 4 = 0.00 in
all arms).** Every subject, control included, wrapped the requested summary in some
meta-commentary ("I'll write the status summary. But first…"). Progress since round 1:
there the wrapper was doctrine-*induced*; in round 2 the doctrine arms' wrappers were
no worse than control's and materially milder than round 1's compliance narration. But
C10 does not yet fully overcome the trained agent-framing habit at prompt position.

## Round-1 comparisons

- **P11 vs round 1's P4** (same task): on the unchanged criteria, doctrine arms
  improved the lede (1.67→2.00) and risk-selection (1.67→2.00) over control, holding
  round 1's finding. The stricter new wrapper criterion exposed what round 1's rubric
  tolerated.
- **P6 vs round 1's P5**: the over-structure failure replicated under a stricter
  rubric. The sharpened C7 text alone did not fix it — hence the example-based v5
  change.

## Validity notes

- Prompt-position delivery remains a lower bound on identity-position deployment.
- n=3 per cell; per-criterion deltas of ±0.33 are one judge-point and should be read
  as noise.
- Judges were blind to arms and doctrines; the P10-full cell is the sole exception
  (see integrity note).
- The v5 fixes motivated by findings 4–5 are themselves untested.
