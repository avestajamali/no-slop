# Artifact-first delivery on the raw API

The goal is that the reply begins at the artifact's first word — no preamble, no closing
offer. On current models (the Claude 5 family, Opus 4.8/4.7/4.6, Sonnet 5/4.6) this is
achieved by instruction plus mechanical lint, not by prefill: a trailing assistant
message returns a 400 `invalid_request_error`. Assistant prefill still works on legacy
models (Sonnet 4.5, Opus 4.1 and earlier), so the prefill example below is scoped to
those.

## Current models

Two levers do the work. Neither is an absolute guarantee, so pair them with
`lint_tells.py` as the deterministic check on the produced text.

**1. A system-prompt line.** Include something like:

> When the user requests an artifact, the first word of your reply is the first word of
> the artifact — no preamble, no closing offer.

This is strong suppression, not a guarantee — a trained preamble still leaks sometimes.
Run `lint_tells.py` over the result to catch what slips through; its preamble-opener and
closing-meta-offer checks flag exactly these two behaviors.

**2. Structured outputs.** For any artifact whose shape is a schema — a JSON object, a
record, a fixed set of fields — set `output_config` with a `json_schema` format. The
reply is pinned to the artifact shape by construction: the model cannot emit a preamble
outside the schema, because everything it returns must validate against it.

```python
import anthropic

client = anthropic.Anthropic()
resp = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1500,
    system=open("doctrine/FULL.md", encoding="utf-8").read(),
    output_config={"format": {"type": "json_schema", "schema": SCHEMA}},
    messages=[
        {"role": "user", "content": "Extract the fields from this note.\n\n" + notes},
    ],
)
```

For free-form prose artifacts (an email body, a status summary) there is no schema to
pin to — the system-prompt line plus the lint is the current-model path.

## Legacy models

On Sonnet 4.5, Opus 4.1, and earlier, the Messages API lets you pre-fill the beginning
of the assistant's reply. The model must continue from your prefix — so if the prefix is
the artifact's first words, the preamble has nowhere to go.

```python
import anthropic

client = anthropic.Anthropic()
resp = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1500,
    system=open("doctrine/FULL.md", encoding="utf-8").read(),
    messages=[
        {"role": "user", "content": "Write the status summary for my manager.\n\n" + notes},
        # The prefill: reply is forced to begin at the artifact's first token.
        {"role": "assistant", "content": "Subject:"},
    ],
)
summary = "Subject:" + resp.content[0].text
```

Pick the prefill to match the artifact's natural first token:

| Artifact | Prefill |
|---|---|
| Email / memo | `Subject:` |
| Markdown doc | `#` |
| Code file | the shebang or first import |
| JSON | `{` (or use structured outputs / a schema-parsing layer) |
| Plain prose copy | the first two or three words you want, e.g. `Meridian Analytics is` |

Two cautions. A prefill constrains the opening only — closing meta-offers can still
appear at the end; run `lint_tells.py` over the result if the artifact ships
unreviewed. And don't prefill content you haven't decided — a wrong opening forces the
model to build on your mistake (the doctrine's rung 4 applies to you too).
