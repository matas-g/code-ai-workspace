# Daily work

Each ticket is a local task folder for requirements, notes and attachments. Jira-style IDs do not connect to Jira. Use [Copilot](COPILOT_GUIDE.md) or [Python](#run-commands-without-copilot).

## Work on a ticket

1. **Create a brief.** In Copilot chat, enter:

   ```text
   /ca-jira-ticket-init A-111 - add a Python greeting
   ```

   Replace `A-111` with your ID. This creates `tickets/active/A-111/brief.md`; complete missing requirements and acceptance criteria. An ID alone leaves an incomplete template.

2. **Work and review.** For review, record each repository's starting Git commit (baseline) and existing uncommitted/untracked work **before editing**. Attach the brief/context, implement and test, then request `/ca-change-review` with the brief and baselines.
3. **Archive when finished.** Run `/ca-jira-ticket-archive A-111`. Use `/ca-jira-ticket-restore A-111` to resume later.

Creation defaults to `brief.md`. Repeating it preserves files and **does not add details to an existing brief**; edit it separately. Archive/restore preserve attachments, refuse collisions and leave Jira/Git unchanged.

## Find your files

| Location | Use it for |
|---|---|
| [Project overview](project/overview.md) and [reference map](project/reference-map.md) | Verified project context and authoritative sources |
| [Active tickets](tickets/active/) / [archive](tickets/archive/) | Briefs, optional documents and `files/` attachments |
| [Knowledge](../{{knowledge_link}}/README.md) | Reusable guides |
| `.github/skills/` | Editable workflow instructions and templates |
| `tools/` and `.framework/` | Commands, configuration and validation records; keep both folders |

## Copilot commands

| Command | Action |
|---|---|
| `/ca-jira-ticket-init ID` | Create a brief; add details after the ID |
| `/ca-jira-ticket-archive ID` | Move a ticket to the archive |
| `/ca-jira-ticket-restore ID` | Return an archived ticket to active work |
| `/ca-change-review` | Review changes against your brief and starting commits |
| `/ca-config-audit` | Inspect local framework configuration without repairing it |

See [skill checks and fallback](COPILOT_GUIDE.md#check-the-skills) if commands are unavailable.

## Run commands without Copilot

Open a terminal **in `{{ai_work}}/`**. With Python 3.9+, run one command below. In Windows PowerShell, replace `python3` with `& 'C:\Path\To\python.exe'`, using your approved executable's actual path.

```sh
python3 -I -S -B tools/workspace_manager.py ticket create A-111 --description "add a Python greeting"
python3 -I -S -B tools/workspace_manager.py ticket archive A-111
python3 -I -S -B tools/workspace_manager.py ticket restore A-111
python3 -I -S -B tools/workspace_manager.py validate
python3 -I -S -B tools/workspace_manager.py audit
python3 -I -S -B tools/workspace_manager.py refresh --interactive
```

- Add `--with plan,review,notes,files` to `ticket create` for optional documents and an attachment folder; list only what you need.
- `refresh` alone previews; `refresh --apply` writes changes. For missing entries, see [refresh choices](../README.md#add-hide-or-remove-a-repository).
- For JSON: `validate --format json`. To save an audit: `audit --save-report check.json` (under `.framework/reports/`). Use subcommand `--help` for more options.

## Check the workspace

`validate` checks files, links and changes since setup; `audit` also checks local customizations, including duplicate skill names. Neither repairs files or proves Copilot loading. Context/configuration edits are informational; edited tools/generated guides may be errors. Only saving an audit report writes files.

For incomplete transfers, inspect **both active and archive copies** and `.ticket-transfer-incomplete.json` before deleting anything. See the root guide for [backup and relocation](../README.md#move-back-up-or-remove-this-folder).
