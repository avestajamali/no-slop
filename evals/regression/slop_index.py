#!/usr/bin/env python3
"""Deterministic Slop Index for regression between doctrine versions.

Composite modeled on EQ-Bench's published weighting: 60% stock-lexicon frequency,
25% contrast-pattern ("not just X, but Y") frequency, 15% slop-trigram frequency —
each expressed per 1,000 words, so scores are length-normalized. Lower is better;
zero is achievable by ordinary careful prose. The absolute scale is arbitrary —
compare scores only within the same probe/task, across doctrine versions or arms.

Usage:
  python slop_index.py FILE...                 score files
  python slop_index.py --trials RAW.json       score every subject report in an
                                               archived trial JSON, grouped by
                                               probe/arm (regression mode)
This is a pre-screen, not a judge: it catches lexical/pattern regressions for free
so blind-judged rounds are spent only on behavior.
"""

import json
import re
import sys

LEXICON = {
    "delve", "delves", "delving", "tapestry", "intricate", "intricacies",
    "interplay", "meticulous", "meticulously", "garner", "boasts", "bolstered",
    "vibrant", "testament", "showcase", "showcases", "showcasing", "foster",
    "fosters", "fostering", "leverage", "leverages", "leveraging",
    "cutting-edge", "seamless", "seamlessly", "holistic", "empower", "empowers",
    "empowering", "unlock", "unlocks", "unlocking", "elevate", "elevates",
    "transformative", "nestled", "groundbreaking", "renowned", "pivotal",
    "crucial", "underscore", "underscores", "underscoring",
}

CONTRAST = re.compile(
    r"\b(not (just|only|merely|simply) .{2,60}?[,;]? but (also )?|"
    r"it['’]s not about .{2,60}?[,;]? it['’]s about |"
    r"isn['’]t (just|only) .{2,60}?[,;]? (it['’]s|but) )", re.I)

TRIGRAMS = [
    "a testament to", "plays a vital", "plays a crucial", "in today's fast",
    "at the end of the day", "the world of", "when it comes to",
    "a wide range", "an array of", "the power of", "take it to the next",
    "look no further", "in the heart of", "stands as a", "serves as a",
    "committed to providing", "a game changer",
]


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", text.lower())


def score(text):
    ws = words(text)
    n = max(len(ws), 1)
    lex = sum(1 for w in ws if w in LEXICON)
    piv = len(CONTRAST.findall(text))
    low = text.lower()
    tri = sum(low.count(t) for t in TRIGRAMS)
    per_k = 1000.0 / n
    return round(60 * lex * per_k + 25 * piv * per_k * 10 + 15 * tri * per_k * 10, 2)
    # pivots and trigrams are ~10x rarer than lexicon words in slop text,
    # so they carry a 10x multiplier to hold the published 60/25/15 intent.


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    if argv[0] == "--trials":
        from collections import defaultdict
        agg = defaultdict(list)
        for path in argv[1:]:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            for t in data["result"]["trials"]:
                agg[(path, t["probe"], t["arm"])].append(score(t["report"]))
        for (path, probe, arm), xs in sorted(agg.items()):
            print(f"{path}  {probe:22s} {arm:12s} mean={sum(xs)/len(xs):6.2f}  runs={[round(x,1) for x in xs]}")
        return 0
    for p in argv:
        text = sys.stdin.read() if p == "-" else open(p, encoding="utf-8", errors="replace").read()
        print(f"{'stdin' if p == '-' else p}: {score(text)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
