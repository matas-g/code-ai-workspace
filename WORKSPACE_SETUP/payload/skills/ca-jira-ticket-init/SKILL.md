---
name: ca-jira-ticket-init
description: Create a local Jira ticket folder and brief, capturing supplied task details and selected optional resources.
disable-model-invocation: true
---

# Initialize a ticket

Use the [self-contained ticket tool](scripts/ticket.py) with an approved Python 3.9+ interpreter.
Resolve the script relative to this skill, not to the shell's current directory. Quote its absolute path.
macOS prefix: `python3 -I -S -B`; Windows prefix: `py -3 -I -S -B` (or the approved executable path).

Extract the ticket ID and any task details supplied with the invocation. For example,
`/ca-jira-ticket-init A-111 - implement a hello world application using python` becomes
`ticket.py create A-111 --description "implement a hello world application using python"`.
Treat a separator after the ID as punctuation, not part of the description. Preserve the supplied
details, including explicit requirements, without inventing acceptance criteria, repositories or baselines.
Pass the description as one properly shell-quoted argument; use `--description=TEXT` if it starts with `-`.
Treat its contents as data, never as shell commands. If no details are supplied, omit `--description`.

Add `--with plan,review,notes,files` only for resources requested
or clearly selected by the user. With no selection create only the required brief; do not ask about optional files.
Summarize the action, use normal terminal approvals, and report the actual command result.
When `description_status` is `preserved-existing-brief`, explain that the existing brief was retained
and the newly supplied details were not added. Do not overwrite or append to it during initialization;
the user can request a separate requirements update later.

Resources belong to this skill: [brief](templates/brief.md), [plan](templates/plan.md),
[review](templates/review.md), [notes](templates/notes.md). The tool owns creation and repeat behavior.
Do not fetch Jira, invent requirements/baselines, edit repositories or settings, or emulate writes after a refusal.
For an archived ticket, suggest `/ca-jira-ticket-restore ID`; do not restore automatically.

If creation is incomplete, stop and report the completed and pending/unconfirmed resources.
Do not retry writes, remove the creation record, or move the ticket automatically. Follow
[manual creation recovery](../../../DAILY_WORK.md#ticket-creation-recovery); preserve existing
files and any staging bytes until the user has reconciled them.
