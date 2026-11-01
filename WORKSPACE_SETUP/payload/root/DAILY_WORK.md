# Daily work

Use **Copilot skills** for the workflows below, or the [optional Python commands](#optional-python-reference). For workspace setup, see the [root guide](../README.md#get-started); for Copilot context and discovery, see the [Copilot guide](COPILOT_GUIDE.md).

## Work on a ticket

1. **Create a brief.** In Copilot chat, enter:

   ```text
   /ca-jira-ticket-init A-111 - add a Python greeting
   ```

   Replace `A-111` with your ID. Complete requirements and acceptance criteria in `tickets/active/A-111/brief.md`. Tickets are local; Jira is not queried or updated.

2. **Record baselines before editing code.** Init leaves them unfilled. Ask the agent:

   > Record each affected repository's full HEAD commit hash and existing uncommitted/untracked work in the brief's baseline table before editing code.

3. **Implement, test and review.** Attach the brief and relevant context, then request `/ca-change-review` against the recorded baselines.
4. **Archive when finished.** Run `/ca-jira-ticket-archive A-111`. Use `/ca-jira-ticket-restore A-111` to resume later.

Init creates only a brief unless you request optional files. Repeating it **preserves existing briefs without adding details**. Archive/restore leave Jira/Git unchanged.

You can also move the whole ticket folder, including attachments, between `tickets/active/` and `tickets/archive/`. Keep it unchanged, keep one copy and wait for ticket commands to finish. The commands refuse collisions and verify copied contents. External links to the ticket may need updating after either method.

## Copilot commands

| Command | Action |
|---|---|
| `/ca-jira-ticket-init ID` | Create a brief with details supplied after the ID |
| `/ca-jira-ticket-archive ID` | Move a ticket to the archive |
| `/ca-jira-ticket-restore ID` | Resume an archived ticket |
| `/ca-change-review` | Review against the brief and baselines |
| `/ca-config-audit` | Check Code-AI files, links and AI customizations |
| `/ca-workspace-refresh` | Preview and apply approved VS Code repository-list updates |

Type `/` in Copilot chat to choose a command; add your ticket ID or review context. Missing commands? See [skill checks and fallback](COPILOT_GUIDE.md#check-the-skills).

## Update the VS Code repository list

After adding, renaming or removing repository folders, use `/ca-workspace-refresh` or a root refresh launcher. The [root guide](../README.md#add-hide-or-remove-a-repository) explains approvals, missing folders, selections and possible chat interruption. For initial setup, use the launcher before opening VS Code.

## Check the Code-AI framework

Use `/ca-config-audit` after customization or for missing/damaged framework files. It validates the layout, files and links, then inspects AI Work and registered repository customizations for issues such as duplicate skill names. Global configuration and ticket attachments are excluded.

Intentional context/configuration edits appear as notes; changed tools/generated guides can be errors. Checks do not repair files, test project code or prove Copilot loading. Reports are saved only when requested.

## Find your files

| Location | Contents |
|---|---|
| [Project overview](project/overview.md) / [reference map](project/reference-map.md) | Project context and source links |
| [Active tickets](tickets/active/) / [archive](tickets/archive/) | Briefs, notes and attachments |
| [Knowledge](../{{knowledge_link}}/README.md) | Reusable guides |
| `.github/skills/` | Workflow instructions and templates |
| `tools/` and `.framework/` | Tools and setup records; keep both folders |

**Transfer error:** Inspect **both active/archive copies** and `.ticket-transfer-incomplete.json` before deleting anything. See [backup and relocation](../README.md#move-back-up-or-remove-this-folder) in the root guide.

### Ticket creation recovery

If ticket creation fails or is interrupted, stop ticket commands and inspect that ticket folder.
The tool refuses further create/archive/restore operations while `.ticket-creation-incomplete/`
exists. Its `resources.json` lists the resources being added; `.done` receipts record completed
publications. Missing receipts mean **unconfirmed**, even if the final resource exists. An empty
or damaged record means the intended resource list is unknown; use the original command too.
The error reports recorded completion and pending/unconfirmed resources without reading attachments.

1. Confirm no ticket command is running. A hard process termination can also leave
   `tickets/.ticket-operation.lock`; inspect it and remove it manually only when no operation is active.
2. Preserve existing user files. Compare final resources with any `.ticket-create-*` staging files;
   staging bytes can be incomplete and may contain private task details. Reconcile the requested
   resources manually. Do not infer corruption from differences against a template.
3. After reconciliation, remove only this ticket's creation record and reconciled staging files.
   Retry create explicitly for missing resources. Existing files remain unchanged.

New files are fully prepared and verified before publication. Publication requires local hard-link
support; unsupported filesystems stop with an incomplete record rather than replacing a user file.
This detects interrupted operations, but does not promise persistence after power loss. Do not edit
the ticket concurrently with a ticket command. Older unmarked partial tickets require manual inspection;
the tool cannot distinguish them from completed user-edited files. Existing workspaces are not upgraded automatically.

## Optional Python reference

For troubleshooting, unavailable skills or users who prefer direct commands.

<details>
<summary>Show terminal commands</summary>

With Python 3.9+, open a terminal **in `{{ai_work}}/`** and run only the command you need. On Windows PowerShell, replace `python3` with `& 'C:\Path\To\python.exe'`, using your approved executable's actual path.

```sh
python3 -I -S -B tools/workspace_manager.py ticket create A-111 --description "add a Python greeting"
python3 -I -S -B tools/workspace_manager.py ticket archive A-111
python3 -I -S -B tools/workspace_manager.py ticket restore A-111

# Framework files and links
python3 -I -S -B tools/workspace_manager.py validate
# All validation checks, plus AI customizations
python3 -I -S -B tools/workspace_manager.py audit
# Review and approve repository-list updates
python3 -I -S -B tools/workspace_manager.py refresh --interactive
```

Replace the example ID/description with yours. For optional resources, add `--with plan,review,notes,files` to creation, listing only what you need. Use `--format json` with validate/audit, or `audit --save-report check.json` to save under `.framework/reports/`. Subcommand `--help` lists other options.

</details>
