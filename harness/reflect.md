# The reflection loop — how the doctrine keeps learning after deployment

The doctrine was hardened by trial rounds, but deployment produces the same signal for
free: every lint finding, every judged regression, every "no, always X" correction from
a user is evidence about where the doctrine's text fails to bind. This loop captures
that evidence and converts it into doctrine changes without the failure mode that kills
evolving rule documents.

**The failure mode to avoid** (documented by Stanford's Agentic Context Engineering
work, arXiv 2510.04618): holistic rewrites of a rules document cause *context
collapse* — each rewrite smooths away hard-won specific rules toward general mush. The
no-slop trial history confirms it from the other direction: the rules that changed
behavior named their exact unit ("every noun phrase about the subject is a factual
claim"); generality never moved anything. So: **rules are appended and anchored, never
globally rewritten.**

## The loop

1. **Capture.** Failures append to `lessons-learned.md` beside the deployed doctrine,
   one line each, with the trigger: lint findings (`lint_tells.py` output), judge
   criticisms from any eval round, and user corrections verbatim ("no — never repeat
   the caveat at the end"). A Claude Code hook can automate the lint captures
   (see `hooks.md`); corrections are cheapest logged the moment they happen.
2. **Reflect (periodic, not per-incident).** When the file has substance, run a
   reflection pass: cluster the lessons, discard one-offs, and for each recurring
   pattern draft a *delta* — an anchored insertion in doctrine voice that names its
   unit of analysis and its trigger. The prompt shape that works: "which of these
   lessons recur, which are already covered by the doctrine's current text, and what
   is the smallest anchored insertion that would have prevented the recurring ones?"
3. **Gate.** A human approves each delta before it enters `FULL.md`. Auto-applied
   self-edits compound errors; the gate is what keeps the doctrine's thirteen-plus rounds
   of validated behavior from drifting. Rotate `lessons-learned.md` after each reflection
   so it never grows unbounded.
4. **Re-verify.** Any applied delta goes through the regression pre-screen
   (`../evals/regression/`) and, if it touches behavior rather than wording, one
   judged probe round. Distillations (`KERNEL.md`, `COMPACT.md`, the output style) are
   regenerated or re-checked after every accepted delta.

## Why this beats re-running big trial rounds

Trial rounds are the right tool for validating a doctrine version; they are the wrong
tool for *finding* the next fix — deployment surfaces real failures faster and in the
user's actual distribution of tasks. The loop keeps iteration cheap (capture is free,
reflection is one prompt) while the gate and the regression suite keep it safe.
