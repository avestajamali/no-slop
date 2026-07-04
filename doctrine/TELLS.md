# Machine tells — a field guide

A companion to the No-Slop Doctrine (rule C11). This is the catalog of patterns that
make a reader feel "an AI wrote this." Load it whenever the deliverable is prose that
has to stand on its own — an article, a report, an email, documentation, marketing
copy — and sweep for these before sending.

Primary source: Wikipedia's editor-maintained catalog
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
generalized here beyond Wikipedia to any agent-written text. The lexicon lists drift as
models change; treat them as living lists, not scripture.

**How to use this file.** Every tell below is a *symptom*. Swapping a flagged word for
a synonym treats the symptom and creates a new tell; the fix is always the underlying
doctrine rule, cited per section. A tell is evidence of a behavior — kill the behavior.

---

## 1. Vocabulary tells

The stock lexicon. No single word proves anything; density does.

- **Importance inflation:** stands as / serves as a testament, pivotal, crucial, vital,
  key role, underscores, highlights, reflects broader trends, enduring legacy,
  indelible mark, deeply rooted, key turning point, evolving landscape, focal point,
  setting the stage, marking a shift.
- **The classic set (2023–2024, still radioactive):** delve, tapestry, intricate,
  interplay, meticulous, garner, boasts, bolstered, vibrant, landscape (metaphorical),
  testament.
- **The current set (2024–):** showcase, foster, highlight (as verb of significance),
  emphasize, enhance, align with, crucial, enduring, vibrant.
- **Promotional register:** rich, profound, renowned, groundbreaking, nestled,
  in the heart of, natural beauty, diverse array, commitment to, state-of-the-art.

**Fix (C8, C5):** claims sized to evidence, adjectives backed or cut. If a thing
matters, show the number or the consequence; "pivotal" is a claim with no invoice.

## 2. Sentence-shape tells

- **Copula avoidance.** Writing "serves as", "stands as", "functions as", "boasts",
  "features", "represents" where the true verb is *is* or *has*. Plain copulas are not
  weak writing; dodging them is.
- **Negative parallelism.** "Not just X, but Y." "It's not about X — it's about Y."
  "X rather than Y" as a reflex. One per document is rhetoric; three is a fingerprint.
- **The rule of three.** Triads everywhere: "fast, reliable, and secure." The triad is
  the shape of performed thoroughness — three items chosen for rhythm, not because
  there are three things (C5).
- **Significance-dangling participles.** A factual clause with an unearned analytical
  tail: "…, highlighting the company's commitment to innovation", "…, underscoring its
  regional importance", "…, ensuring long-term growth." The tail asserts meaning no
  source or evidence established.
- **Elegant variation.** Refusing to repeat a word — the report becomes "the document,"
  then "the analysis," then "the publication," all one thing. Repeating the right word
  is clarity; the thesaurus walk is the tell.

**Fix (C2, C8):** say it plainly once; let facts carry their own weight; delete
analytical tails you cannot source.

## 3. Content tells

- **The empty significance paragraph.** Analysis that evaluates nothing: "This approach
  offers valuable insights and resonates with broader industry trends." Zero falsifiable
  content.
- **Vague authority.** "Experts argue," "observers have noted," "industry reports
  suggest," "several publications" — attribution theater. Name the expert or drop the
  claim (E1, C4).
- **The challenges-and-outlook formula.** "Despite its successes, X faces several
  challenges… Looking ahead, X is well positioned to…" — the template ending of a
  thousand generated profiles. If you have specific challenges with evidence, state
  them as facts; if not, end earlier.
- **Both-sidesing as depth.** Balanced-sounding surveys that commit to nothing (J1's
  bad example, stretched to essay length).
- **Preemptive self-defense.** Disclaimers, caveats, and policy citations deployed to
  ward off criticism before any was made — including knowledge-cutoff disclaimers
  ("as of my last update…") inside a deliverable.

**Fix (J1, C4, C10):** verdicts with reasoning, named sources, endings that end.

## 4. Structure and formatting tells

- **Bold-label bullet scaffolding.** Every bullet a **Bolded Phrase:** followed by a
  sentence. One or two is formatting; a whole document of them is a machine skeleton.
- **Inline emphasis-bolding.** Key phrases bolded mid-sentence throughout running
  prose. Bold marks the one thing the skimming reader must not miss; several per
  paragraph is a highlighter, not emphasis — importance inflation (§1) done in
  formatting instead of vocabulary.
- **Structure as costume.** Headers, tables, and nested bullets wrapping content that
  is three paragraphs of prose (C7). Answers are not documents.
- **Title Case Headings** where the surrounding convention is sentence case — and
  heading levels that skip (an H4 under an H2).
- **Em-dash saturation.** The em-dash is legitimate; four per paragraph doing the work
  of commas, colons, and periods is a fingerprint.
- **Horizontal-rule saturation.** A `---` before every heading or between every
  section. A rule is punctuation for a hard topic break; as default section chrome it
  is a fingerprint. One or two in a long document earn their place the way any
  structure does (C7).
- **The summary that restates.** A closing section ("In conclusion, …", "Overall, …")
  that repeats what was just said, shorter and vaguer. Cut it entirely.
- **Emoji as structure,** decorative section icons, and curly quotes in contexts where
  everything else uses straight quotes.
- **Wrong markup for the medium.** Markdown syntax in a system that doesn't render it
  (asterisk-bold in an email or wiki), bare bullet characters where the medium has real
  list markup, leftover template tags or placeholders ("[Company Name]").

**Fix (C7, D4):** structure only where content demands it; match the medium's idiom
exactly.

## 5. Process-leak tells

- **Talking to the requester inside the artifact.** "Here's a draft you can adapt…",
  "I've kept the tone professional as requested…", "Let me know if…" — inside the
  document itself (C10's signature failure).
- **Narrated deliberation.** "Let me first consider…", an inventory of the judgment
  calls made, meta-commentary stacked around the deliverable.
- **Register shift at the seam.** Text inserted into an existing document that is
  noticeably more polished, more hedged, or differently voiced than what surrounds
  it — the primary tell when editing rather than authoring fresh. Abrupt topic resets
  betraying a stitched-together generation are the same failure at paragraph scale.
  Fix: match the surrounding register (D4); the insertion should read as if written by
  whoever wrote the rest.
- **Refusal or capability fragments.** "As an AI, I cannot…" embedded mid-document.
  Largely a legacy sign of older models; on freshly authored output it almost never
  fires — check for it mainly when incorporating text generated elsewhere (a
  delegate's draft, a pasted generation).

**Fix (C10):** the deliverable is the deliverable. Anything addressed to the requester
goes outside it, in one line if it earns its place.

## 6. Fabrication tells

The tells that are not style but lies, and the first things a hostile reader checks:

- Citations that don't resolve: broken links, DOIs pointing at unrelated papers,
  ISBNs that fail checksum, book references with no page numbers.
- Sources that were never read, cited with confidence (E1, E8).
- Quotes that paraphrase, presented as quotes. Numbers that are round, presented as
  measured (C8).
- Tracking debris (`utm_source=…`) copied into references — evidence of paste, not
  reading.

**Fix (rung 1, E1):** cite only what you opened; verify identifiers resolve before
shipping; a missing citation is honest, a fabricated one is fatal.

---

## The sweep

Before sending prose that must stand on its own, one pass, in this order:

1. **Fabrications** — every citation, quote, number, and identifier traceable? (§6)
2. **Process leaks** — anything addressed to the requester inside the artifact? And if
   this edits an existing document: does the inserted text match the surrounding
   register? (§5)
3. **Structure** — is the shape earned by the content, or is it costume? (§4)
4. **Content** — does every analytical claim have an owner and evidence? (§3)
5. **Sentences** — copulas restored, triads broken where unearned, tails deleted? (§2)
6. **Vocabulary** — density check against the lexicons; rewrite the sentence, don't
   swap the word. (§1)

The goal is not to disguise anything — text that survives this sweep reads human
because it is doing what human experts do: claiming only what it can back, in the
plainest shape that carries it.
