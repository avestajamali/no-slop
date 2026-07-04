# Claude Code hooks — lint written artifacts automatically

Claude Code hooks cannot edit the assistant's chat text, but they see every file the
agent writes. That is enough to make the enforcement layer automatic for
artifact-to-file workflows: whenever the agent writes or edits a Markdown/text
deliverable, lint it. If tells are found, the finding list is fed back to the agent as
context, and the agent (already carrying the doctrine) fixes its own draft.

Add to `.claude/settings.json` (project) or `~/.claude/settings.json` (user):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "python \"<path-to>/no-slop/harness/lint_tells.py\" --hook" }
        ]
      }
    ]
  }
}
```

Behavior: Claude Code hands the hook the tool call as JSON on stdin; `--hook` mode reads
it, lints the written file (Markdown and text only — source code passes through
untouched), and on findings prints them to stderr and exits 2, the blocking exit code
Claude Code feeds back to the agent, which treats them like any failing check. Clean
files and non-prose files exit 0 silently.

The complementary pattern is **artifact-to-file routing**: for any deliverable, have
the agent write the artifact to a file and keep chat for status. The preamble then
lands harmlessly in chat while the artifact itself is born clean, and the hook
verifies it stays that way. This sidesteps the preamble floor entirely, which is why
it is the recommended default for agent-produced deliverables.
