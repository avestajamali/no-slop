#!/usr/bin/env python3
"""Stylometric distance to a reference corpus (Burrows' Delta, function words).

Style fidelity is a different construct from task quality: judges score whether the
work is right; this scores whether the *register* matches a reference author — here,
the reference model the doctrine imitates. Method: relative frequencies of ~70 English
function words per text, z-scored over the whole comparison set, then Delta =
mean |z_text − z_reference_centroid|. Lower = closer to the reference register.

Usage:
  python style_distance.py --trials RAW.json --ref-arm fable
      Build the reference centroid from arm `fable`'s reports in RAW.json and print
      each arm's mean Delta to it, grouped by probe.

Zero dependencies. Small-n caveat: with few texts per arm the numbers are indicative,
not decisive — use for direction and regression, not headlines.
"""

import json
import math
import re
import sys
from collections import defaultdict

FUNCTION_WORDS = """
the and to of a in that it is was for on with as at by this but not are be or from
have an they which you we his her its their there what all were when who will more
if no out so said up into than them can only other time new some could these two
may then do first any my now such like our over man me even most made after also
did many before must through back years where much your way well down should because
each just those people how too little state good very make world still own see men
work long here get both between life being under never day same another know while
last might us great old year off come since against go came right used take three
""".split()

WORD_RE = re.compile(r"[a-z][a-z'’-]*")


def profile(text):
    ws = WORD_RE.findall(text.lower())
    n = max(len(ws), 1)
    counts = defaultdict(int)
    for w in ws:
        counts[w] += 1
    return [counts.get(fw, 0) * 1000.0 / n for fw in FUNCTION_WORDS]


def main(argv):
    if "--trials" not in argv:
        print(__doc__)
        return 0
    path = argv[argv.index("--trials") + 1]
    ref_arm = argv[argv.index("--ref-arm") + 1] if "--ref-arm" in argv else "fable"

    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    texts = [(t["probe"], t["arm"], profile(t["report"])) for t in data["result"]["trials"]]
    if not any(a == ref_arm for _, a, _ in texts):
        print(f"no texts for reference arm {ref_arm!r}")
        return 1

    # z-normalize each feature over the whole comparison set
    k = len(FUNCTION_WORDS)
    means, stds = [], []
    for i in range(k):
        vals = [p[i] for _, _, p in texts]
        m = sum(vals) / len(vals)
        v = sum((x - m) ** 2 for x in vals) / max(len(vals) - 1, 1)
        means.append(m)
        stds.append(math.sqrt(v) or 1.0)
    z = {id(p): [(p[i] - means[i]) / stds[i] for i in range(k)] for _, _, p in texts}

    for probe in sorted({p for p, _, _ in texts}):
        ref = [z[id(pr)] for p, a, pr in texts if p == probe and a == ref_arm]
        if not ref:
            continue
        centroid = [sum(col) / len(col) for col in zip(*ref)]
        print(probe)
        for arm in sorted({a for p, a, _ in texts if p == probe}):
            deltas = [
                sum(abs(zi - ci) for zi, ci in zip(z[id(pr)], centroid)) / k
                for p, a, pr in texts if p == probe and a == arm
            ]
            tag = " (reference)" if arm == ref_arm else ""
            print(f"  {arm:12s} delta={sum(deltas)/len(deltas):5.3f}  n={len(deltas)}{tag}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
