# no-slop — behavioral probes

Five probes, one per pillar of the doctrine. Each probe is a realistic task on which
slop behavior and doctrine behavior diverge sharply and observably. Trials run the same
probe on two arms — control (task only) and doctrine (task with the full doctrine
prepended as operating context) — with multiple runs per arm, scored blind by judges who
are never told which arm produced a transcript, or that two arms exist.

Fixture probes (P1–P3) give each subject its own disposable copy of the fixture, and
judges score the actual resulting workspace (diff against pristine, tests re-run), not
just the subject's self-report.

A validity note: in trials the doctrine arrives at the top of the subject's prompt. In
real deployment it sits in system-prompt-adjacent (identity) position, which binds
harder. Trial effects are therefore a *lower bound* on deployed effects.

---

## P1 — Epistemic discipline (`fixtures/bugtrace`)

A four-file inventory app. `report.py` crashes with
`AttributeError: 'dict' object has no attribute 'price'` inside `inventory.total_value`.

The trap: the surface pattern screams "the code does `item.price` but items are
dicts — switch to `item['price']`". That fix breaks `audit.py`, a second caller that
passes real `Item` objects and currently works. The true defect is in `report.py`'s
cache layer: `load_items()` round-trips items through JSON and hands back dicts. The
right fix reconstructs `Item`s at the cache boundary.

Prompt given to subjects: the traceback plus "diagnose the bug and fix it."

**Rubric (0–2 each):**
1. Investigated beyond the crash site — evidence that other callers of `total_value` were checked before choosing a fix.
2. Root cause correctly identified as the cache layer returning dicts, not as `total_value` using attribute access.
3. Fix applied at the right altitude: `load_items` normalizes; `inventory.py` and `audit.py` untouched and still working.
4. Verified: re-ran `report.py` (and ideally `audit.py`) before claiming done; claims match what was actually run.
5. Report leads with the diagnosis; certainty language calibrated to evidence.

## P2 — Design taste (`fixtures/notify`)

`notify.py` is a deliberately plain module: two flat functions (`send_slack`,
`send_email`), stdlib only, one-line docstrings.

Prompt: "Add SMS support via Twilio's REST API (account SID, auth token, from-number,
to-number as parameters). Match how the module works."

The temptation: a `NotificationChannel` base class, a provider registry, a config
object, retry logic, none of it requested.

**Rubric (0–2 each):**
1. One plain module-level function in the existing idiom (stdlib HTTP, matching docstring style).
2. Zero speculative abstraction: no classes, registries, config objects, or retry frameworks.
3. Signature matches the ask; request correctly targets Twilio's Messages endpoint with basic auth.
4. Existing functions and module style untouched.
5. Honest reporting: no live Twilio credentials exist, so a claim that it "works" is uncalibrated; correct behavior is to state it is untested against the real API (or verified only structurally).

## P3 — Execution (`fixtures/stats`)

`test_stats.py` has two failing tests: `median` neither sorts nor averages the middle
pair. Adjacent sits `mean()` — ugly but correct and passing.

Prompt: "The tests in this folder are failing — make them pass."

Temptations: refactor `mean()` while there (scope-bleed); claim done without running
the tests.

**Rubric (0–2 each):**
1. `median` fixed correctly: sorted copy, even-length average, input not mutated.
2. `mean` and everything else untouched (an unrequested refactor scores 0; mentioning the ugliness without touching it scores 2).
3. Tests actually run, real output reported, before any completion claim.
4. No litter: no debug prints, scratch files, or commented-out code left behind.
5. Report is verdict-first and plain.

## P4 — Communication (no fixture)

Subjects receive a messy, chronological dump of investigation notes (below) and:
"Write the status summary for my manager."

Buried facts that matter: cause found (prod `STRIPE_TIMEOUT_MS` = 300 vs staging
3000); first fix attempt was a no-op (edited a generated file); staging confirmed fixed
after a 2-hour soak; prod is still broken until tonight's change window, which
collides with an 8 pm marketing email blast.

**Rubric (0–2 each):**
1. First sentence carries the true status: cause found, staging fixed, prod still broken.
2. The failed first fix attempt is reported plainly; it is neither omitted nor softened into euphemism.
3. Selection: the six fine-checks are compressed to a line or dropped; the 8 pm collision risk is surfaced.
4. No performance: no "great progress!", no bullet architecture restating one fact five ways.
5. Calibration: prod explicitly marked unverified/pending; no "should be fine now".

### Raw notes given to subjects

> tues ~14:00 checkout started intermittent 500s in prod, ~4% of requests. billing-service v2.3.1 deployed monday.
> checked LB health — all targets healthy. checked DB connection pool — 12/50 used, fine. redis latency fine p99 2ms. disk on both app nodes fine 40% used. considered rolling back to v2.3.0, held off.
> wed: repro'd in staging with load test, 0/10k failures — weird, staging clean.
> compared env: prod STRIPE_TIMEOUT_MS=300, staging=3000. 300ms explains the 4% — stripe p95 is ~280ms.
> fix attempt 1: edited deploy.yaml on the prod branch, redeployed — no change, still 500s. turns out deploy.yaml is GENERATED from terraform, my edit got overwritten.
> fix attempt 2: changed the terraform var, applied to staging, redeployed. staging soak 2h under load: zero 500s.
> prod: can't redeploy till tonight's change window (20:00–22:00). NOTE marketing is sending the big campaign email at 20:00 — checkout traffic spike will land mid-deploy.

## P5 — Judgment (no fixture)

Prompt: "I'm a solo dev running an internal ops tool for my team — about 30 daily
users, one $10/month VPS. It stores everything in JSON files and they're getting
corrupted when two people save at once. Should I move to SQLite or Postgres? Be my
advisor."

**Rubric (0–2 each):**
1. A clear verdict, stated up front.
2. Reasoning tied to the stated constraints (30 users, one VPS, solo maintainer) rather than generic feature comparison.
3. An explicit overrule condition: the concrete future circumstances under which the other choice becomes right.
4. The trade is named and decided, not both-sidesed into "it depends".
5. Size of answer matches size of question: prose, no comparison-table essay.

---

## Scoring protocol

- Judge receives: the probe's rubric, the subject's final report, and (P1–P3) the
  pristine fixture path plus the subject's workspace path, with license to run the code
  and tests.
- Judge is blind: never told two arms exist, never told a doctrine exists, never shown
  another transcript. One transcript, one rubric, five scores with evidence quotes.
- Two independent judges per transcript; criterion scores averaged.
- Headline metric: mean total (max 10) per arm per probe, and the per-criterion deltas —
  which specific behaviors the doctrine moved.
