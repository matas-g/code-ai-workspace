---
name: ca-jira-ticket-archive
description: Move a selected local Jira ticket from active work into the archive, preserving its brief and supporting files.
disable-model-invocation: true
---

# Archive a local ticket

Use the shared [ticket tool](../ca-jira-ticket-init/scripts/ticket.py). Resolve its absolute path from
this skill's location, not the terminal working directory. With an approved Python 3.9+ interpreter,
run `ticket.py archive ID` for the ticket ID explicitly supplied or unambiguously selected by the user.
Example: `/ca-jira-ticket-archive A-111` archives that local ticket. If the ID is unclear, ask which ticket.
Use `python3 -I -S -B "ABSOLUTE_SCRIPT_PATH" archive ID` on macOS, or the approved Windows
Python executable with the same isolation flags. Replace the path placeholder with the resolved tool path.

Summarize the move from `tickets/active/ID` to `tickets/archive/ID`, use normal terminal approvals,
and report the actual result, including an already-archived result. The tool moves the complete folder,
including attachments, without rewriting its contents. It owns collision checks and repeat behavior.

This affects local working files only. Do not change Jira status, Git history or repository files.
Do not infer task completion, merge/overwrite a destination, or emulate a move after the tool refuses it.
If a transfer is incomplete, report the error and retain both locations for manual reconciliation.
