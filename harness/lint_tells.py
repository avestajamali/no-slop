#!/usr/bin/env python3
"""no-slop tells lint — deterministic checks from doctrine/TELLS.md.

Usage:
  python lint_tells.py FILE [FILE...]      report per file
  python lint_tells.py --fail FILE...      exit 1 if any finding (CI gate)
  cat text | python lint_tells.py -        read stdin
  python lint_tells.py --hook              Claude Code PostToolUse hook mode:
                                           reads the hook JSON from stdin, lints the
                                           written file, reports findings on stderr,
                                           exits 2 so the agent sees and fixes them

Checks are mechanical by design: they catch the tells a model emits despite
instructions. They judge density and pattern, not single occurrences, so
legitimate prose passes. Zero dependencies.
"""

import re
import sys

# --- Rule data (from TELLS.md sections 1-5) -----------------------------------

LEXICON = [
    "delve", "delves", "delving", "tapestry", "intricate", "interplay",
    "meticulous", "meticulously", "garner", "boasts", "bolstered", "vibrant",
    "testament", "showcase", "showcases", "showcasing", "foster", "fosters",
    "fostering", "leverage", "leverages", "leveraging", "cutting-edge",
    "seamless", "seamlessly", "holistic", "empower", "empowers", "empowering",
    "unlock", "unlocks", "unlocking", "elevate", "elevates", "transformative",
    "nestled", "groundbreaking", "renowned",
]

CIRCUMLOCUTIONS = [
    "in order to", "due to the fact that", "has the ability to", "at this point in time",
    "in the event that", "for the purpose of", "with regard to", "it is important to note that",
]

INFLATION = [
    "stands as a testament", "serves as a testament", "pivotal role",
    "underscores its", "underscores the importance", "highlights the importance",
    "evolving landscape", "indelible mark", "deeply rooted", "key turning point",
    "setting the stage", "industry-leading", "commitment to excellence",
    "trusted partner", "rich history", "natural beauty", "in the heart of",
    "diverse array",
]

PREAMBLE_OPENERS = [
    r"^i['’]ll (write|draft|create|put together)\b",
    r"^(sure|certainly|absolutely|great|happy to)\b[,!.]?",
    r"^this is an? \w+ (task|question|request)\b",
    r"^(here['’]s|here is) (the|a|your)\b.{0,40}:$",
    r"^let me\b",
    r"^i have (everything|what) i need\b",
    r"^no tools (are )?needed\b",
]

CLOSING_OFFERS = [
    r"let me know if\b", r"feel free to\b", r"happy to (help|assist|adjust|refine)\b",
    r"if you (want|need|['’]d like),? i can\b", r"just say the word\b",
    r"hope (this|that) helps\b", r"say which and i['’]ll\b",
]

NOT_JUST_X_BUT_Y = re.compile(
    r"\b(not (just|only|merely|simply) .{2,60}?[,;]? but (also )?|"
    r"it['’]s not about .{2,60}?[,;]? it['’]s about )", re.I)

CONCLUSION_OPENERS = re.compile(
    r"^(in conclusion|in summary|overall|to sum up|ultimately|in essence)\b", re.I | re.M)


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", text.lower())


def lint(text):
    findings = []
    n_words = max(len(words(text)), 1)
    lower = text.lower()
    lines = [l for l in text.splitlines() if l.strip()]

    # 1. Vocabulary density (>=3 absolute, or >=2 at >=4 per 1000 words — a single
    # stock word in a short email is legitimate prose, not a fingerprint)
    hits = [w for w in words(text) if w in LEXICON]
    if len(hits) >= 3 or (len(hits) >= 2 and (len(hits) / n_words) * 1000 >= 4):
        plural = "word" if len(hits) == 1 else "words"
        findings.append(f"lexicon: {len(hits)} stock-AI {plural} ({', '.join(sorted(set(hits))[:6])})")

    # 2. Importance inflation / promotional register (any occurrence)
    infl = [p for p in INFLATION if p in lower]
    if infl:
        findings.append(f"inflation: {', '.join(infl[:4])}")

    # 2b. Circumlocutions (>=2 — one can be deliberate emphasis)
    circ = [p for p in CIRCUMLOCUTIONS if p in lower]
    if len(circ) >= 2:
        findings.append(f"circumlocution: {', '.join(circ[:4])}")

    # 3. Not-just-X-but-Y pivots (>=2, or 1 in <250 words)
    pivots = NOT_JUST_X_BUT_Y.findall(text)
    if len(pivots) >= 2 or (len(pivots) == 1 and n_words < 250):
        findings.append(f"contrast-pivot: {len(pivots)} not-just-X-but-Y construction(s)")

    # 3b. Triad saturation (>=2 "X, Y, and Z" lists in prose — the tell three doctrine
    # iterations failed to instruct away; it lives here instead). Table rows and
    # numeric enumerations ("10, 10b, and 10c") are structure, not rhythm — skipped.
    prose_lines = [l for l in text.splitlines() if not l.lstrip().startswith("|")]
    triads = re.findall(
        r"\b[\w'’-]+(?: [\w'’-]+){0,2}, [\w'’-]+(?: [\w'’-]+){0,2},? (?:and|or) [\w'’-]+",
        "\n".join(prose_lines))
    triads = [t for t in triads if not re.search(r"\d", t)]
    # Threshold scales with length (~1 per 300 words past 600) so long-form text,
    # where triads accumulate worst, stays covered instead of exempt.
    if len(triads) >= max(2, n_words // 300):
        findings.append(f"triad saturation: {len(triads)} lists-of-three in {n_words} words")

    # 4. Em-dash saturation (per TELLS: ~4 per 200 words, minimum 4)
    dashes = text.count("—") + text.count(" -- ")
    if dashes / n_words * 200 >= 4 and dashes >= 4:
        findings.append(f"em-dash saturation: {dashes} in {n_words} words")

    # 5. Bold-label bullet scaffolding (>=3 bullets of the form '- **Label:**' / '- **Label.**')
    scaffolds = re.findall(r"^\s*[-*•]\s+\*\*[^*\n]{2,60}?[:.]?\*\*[:.]?(?:\s|$)", text, re.M)
    if len(scaffolds) >= 3:
        findings.append(f"bold-label scaffold: {len(scaffolds)} labeled bullets")

    # 6. Inline emphasis-bolding (bold spans in running prose, excluding headings,
    # bullets, table rows, and standalone bold labels — those are document structure,
    # not highlighter bold. Bullet markers need a following space so that a
    # "**Run-in label.** prose..." paragraph is counted, not skipped.
    prose_bold = 0
    for l in lines:
        if re.match(r"^\s*(\||[-*•]\s|#{1,6}\s|\d+[.)]\s|\*\*[^*\n]+\*\*[:.]?\s*$)", l):
            continue
        prose_bold += len(re.findall(r"\*\*[^*\n]{2,40}\*\*", l))
    if prose_bold >= 4:
        findings.append(f"highlighter bold: {prose_bold} bold spans in running prose")

    # 7. Horizontal-rule saturation (a --- between most sections). A leading YAML
    # frontmatter block is metadata, not horizontal rules — stripped before counting.
    hr_text = re.sub(r"\A---[ \t]*\n.*?\n---[ \t]*\n", "", text, flags=re.S)
    rules = len(re.findall(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", hr_text, re.M))
    headings = len(re.findall(r"^#{1,6}\s", text, re.M))
    if rules >= 3 and rules >= max(headings, 2):
        findings.append(f"horizontal-rule saturation: {rules} rules / {headings} headings")

    # 8. Preamble opener before the artifact (first non-empty line)
    if lines:
        first = lines[0].strip().lower()
        for pat in PREAMBLE_OPENERS:
            if re.search(pat, first):
                findings.append(f"preamble opener: {lines[0].strip()[:70]!r}")
                break

    # 9. Closing meta-offer (last 2 non-empty lines)
    tail = " ".join(lines[-2:]).lower() if lines else ""
    offers = [p for p in CLOSING_OFFERS if re.search(p, tail)]
    if offers:
        findings.append("closing meta-offer in final lines")

    # 10. Restating conclusion section
    if CONCLUSION_OPENERS.search(text):
        findings.append("conclusion opener (In conclusion / In summary / Overall ...)")

    return findings


def hook_main():
    """Claude Code PostToolUse hook: JSON on stdin, findings on stderr, exit 2.

    Exit 2 is the blocking path — Claude Code feeds stderr back to the agent,
    which fixes its own draft. Non-prose files pass through silently.
    """
    import json
    try:
        payload = json.load(sys.stdin)
    except (ValueError, EOFError):
        return 0
    path = (payload.get("tool_input") or {}).get("file_path", "")
    if not path or not path.lower().endswith((".md", ".markdown", ".txt")):
        return 0
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return 0
    findings = lint(text)
    if findings:
        print(f"lint_tells: {len(findings)} machine-tell finding(s) in {path}", file=sys.stderr)
        for f in findings:
            print(f"  - {f}", file=sys.stderr)
        print("Fix these in the file before moving on.", file=sys.stderr)
        return 2
    return 0


def main(argv):
    if "--hook" in argv:
        return hook_main()
    fail_mode = "--fail" in argv
    paths = [a for a in argv if a not in ("--fail",)]
    if not paths:
        print(__doc__)
        return 0
    any_findings = False
    read_error = False
    for p in paths:
        if p == "-":
            text, label = sys.stdin.read(), "stdin"
        else:
            try:
                text, label = open(p, encoding="utf-8", errors="replace").read(), p
            except OSError as e:
                # exit 2, not 1 — a typo'd path must not read as a lint failure in CI
                print(f"{p}: cannot read ({e.strerror or e})")
                read_error = True
                continue
        findings = lint(text)
        if findings:
            any_findings = True
            print(f"{label}: {len(findings)} finding(s)")
            for f in findings:
                print(f"  - {f}")
        else:
            print(f"{label}: clean")
    if read_error:
        return 2
    return 1 if (fail_mode and any_findings) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
