# Daily work

Use this folder for project context and ticket notes. Start with the [Copilot guide](COPILOT_GUIDE.md) if you want AI assistance, or use the [Python commands](#run-commands-without-copilot) directly.

## Work on a ticket

1. **Create a brief.** In Copilot chat, enter:

   ```text
   /ca-jira-ticket-init A-111 - implement a hello world application using python
   ```

   This creates `tickets/active/A-111/brief.md` with your supplied details. With only an ID, it creates an incomplete brief. Fill in requirements and acceptance criteria before relying on it.

2. **Do the work.** Attach the brief and relevant context to your chat. Edit and test in the affected repositories. For a change review, record a verified starting commit per repository and account for existing uncommitted/untracked work.
3. **Archive when finished.** Run `/ca-jira-ticket-archive A-111`. Use `/ca-jira-ticket-restore A-111` to resume later.

Creation makes only `brief.md` by default. Repeating it preserves existing files; newly supplied details are **not added to an existing brief**. Request a separate update when needed. Archive/restore move the complete local ticket, including attachments; they do not change Jira status or Git history.

## Find your files

| Location | Use it for |
|---|---|
| [Project overview](project/overview.md) and [reference map](project/reference-map.md) | Verified project context and authoritative sources |
| [Active tickets](tickets/active/) / [archive](tickets/archive/) | Briefs, optional plans/reviews/notes and attachments |
| [Knowledge](../{{knowledge_link}}/README.md) | Reusable guides |
| `.github/skills/` | Editable workflow instructions and templates |
| `tools/` and `.framework/` | Daily commands, configuration and validation records; keep these folders |

## Copilot commands

| Command | Action |
|---|---|
| `/ca-jira-ticket-init ID` | Create a brief; add task details after the ID |
| `/ca-jira-ticket-archive ID` | Move a ticket to the archive |
| `/ca-jira-ticket-restore ID` | Return an archived ticket to active work |
| `/ca-change-review` | Review selected changes against requirements and verified baselines |
| `/ca-config-audit` | Inspect local framework configuration without repairing it |

See [skill checks and fallback](COPILOT_GUIDE.md#check-the-skills) if commands are unavailable.

## Run commands without Copilot

Open a terminal **in this folder (`{{ai_work}}/`)**, using an approved Python 3.9+ interpreter. On Windows, replace `python3` with your executable; in PowerShell, prefix a quoted executable path with `&`.

```sh
python3 -I -S -B tools/workspace_manager.py ticket create A-111 --description "implement a hello world application using python"
python3 -I -S -B tools/workspace_manager.py ticket archive A-111
python3 -I -S -B tools/workspace_manager.py ticket restore A-111
python3 -I -S -B tools/workspace_manager.py validate
python3 -I -S -B tools/workspace_manager.py audit
python3 -I -S -B tools/workspace_manager.py refresh --interactive
```

- Add `--with plan,review,notes,files` to `ticket create` for selected extra resources; choose only what you need.
- `refresh` alone previews; `refresh --apply` executes. Add `--remove-missing` to include configuration-only cleanup. See [refresh choices](../README.md#add-hide-or-remove-a-repository).
- Add `--help` after a subcommand for other options, including JSON output and saving audit reports.

## Check the workspace

`validate` checks files, links and recorded changes. `audit` also inspects local instructions/skills for possible conflicts. Both are read-only unless you request a saved report. Intentional context/configuration edits appear as informational notes; these checks do not prove Copilot loading.

If an operation reports an incomplete ticket transfer, inspect **both locations** and the marker before cleanup. Do not delete either copy until reconciled. For backup and relocation, see the [root guide](../README.md#move-back-up-or-remove-this-folder).
