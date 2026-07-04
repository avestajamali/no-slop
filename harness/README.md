# The enforcement layer

Thirteen-plus rounds of blind-judged trials (see `../evals/`) established a hard fact: prompt
text alone cannot fully suppress two trained habits of agentic models — the preamble
before a requested artifact, and the closing meta-offer. Instructions shrank them ~90%;
they never hit zero. This directory is the answer: mechanical enforcement that closes
the remaining gap at the harness layer, matched to where you run the model.

| Surface | Mechanism | File | Effect on the floor behaviors |
|---|---|---|---|
| Claude Code sessions | Output style (replaces the harness's own response-style block, a higher-privilege slot than CLAUDE.md) | `output-style-no-slop.md` | Removes the competing instruction at its source |
| Raw Anthropic API | Artifact-first delivery: structured outputs, system-prompt pinning, legacy assistant prefill | `prefill.md` | Structured outputs pin the reply to the artifact schema; on legacy models prefill removes the preamble outright |
| Agents that write files | Artifact-to-file routing + deterministic lint | `lint_tells.py`, `hooks.md` | Preamble has no channel; anything that leaks into files is caught mechanically |
| CI / editorial pipelines | Lint as a gate | `lint_tells.py --fail` | Blocks merged/published text containing tells |

## `lint_tells.py`

Zero-dependency Python implementing `doctrine/TELLS.md` as twelve mechanical checks:
stock-lexicon density, importance inflation, circumlocutions, not-just-X-but-Y pivots,
triad saturation (lists-of-three — the tell three doctrine iterations failed to instruct
away), em-dash and horizontal-rule saturation, bold-label scaffolds, highlighter bold,
preamble openers, closing meta-offers, restating conclusions.

```
python lint_tells.py draft.md            # report
python lint_tells.py --fail out/*.md     # CI gate: exit 1 on any finding
cat reply.txt | python lint_tells.py -   # stdin
python lint_tells.py --hook                  # Claude Code PostToolUse hook (see hooks.md)
```

Validated against the trial corpus: flags 7/7 planted tells in slop-heavy marketing
copy, passes human-register prose untouched, and catches the exact preamble that blind
judges flagged in archived trial transcripts.

Checks are density- and pattern-based on purpose — one em-dash is punctuation, four
per paragraph is a fingerprint. Expect near-zero false positives on deliberate prose;
if a finding is wrong, it is usually telling you the sentence reads machine-made even
though a human meant it.

## Installing the output style (Claude Code)

```
cp output-style-no-slop.md ~/.claude/output-styles/no-slop.md
# then select it: /output-style no-slop
```

The file is generated from `../doctrine/FULL.md` — after editing the doctrine,
regenerate by re-concatenating the frontmatter block (first 6 lines of the current
file) with the new FULL.md.

## Which layer to reach for

The doctrine carries the judgment: what to verify, when to push back, how to decide,
what to cut. The enforcement layer carries only delivery mechanics that survive
instruction. Run both: doctrine in context, one mechanical guarantee per surface.
Neither substitutes for the other — lint cannot make a model reason, and no amount of
reasoning text reliably deletes a trained preamble.
