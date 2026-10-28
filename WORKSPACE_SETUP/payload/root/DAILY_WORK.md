# Daily work

Use **Copilot skills for daily work** and **refresh launchers for initial setup**. See [Copilot setup](COPILOT_GUIDE.md) for help. [Python commands](#optional-python-reference) are optional reference only.

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

Init creates only a brief unless you request optional files. Repeating it **preserves existing briefs without adding details**. Archive/restore preserve attachments, refuse collisions and leave Jira/Git unchanged.

Manual moves are also allowed: move the whole ticket folder unchanged between active/archive, keep one copy and wait for ticket commands to finish. The skills add collision checks and file verification.

## Copilot commands

| Command | Action |
|---|---|
| `/ca-jira-ticket-init ID` | Create a brief with details supplied after the ID |
| `/ca-jira-ticket-archive ID` | Move a ticket to the archive |
| `/ca-jira-ticket-restore ID` | Resume an archived ticket |
| `/ca-change-review` | Review against the brief and baselines |
| `/ca-config-audit` | Check Code-AI files, links and AI customizations |
| `/ca-workspace-refresh` | Preview and apply approved VS Code repository-list updates |

Missing commands? See [skill checks and fallback](COPILOT_GUIDE.md#check-the-skills).

## Update the VS Code repository list

- **Initial setup:** Double-click the development root's **refresh_vscode_workspace macOS.command** or **refresh_vscode_workspace Windows.cmd**, then open the saved VS Code workspace.
- **Later folder changes:** Use **`/ca-workspace-refresh`** in Copilot, or run the launcher again. Review and approve the proposed updates.

Refreshing the open workspace may interrupt Copilot, especially if its first folder changes; use the launcher if needed. IDE behavior remains unverified. See [refresh choices](../README.md#add-hide-or-remove-a-repository) for cancellation and missing folders.

## Check the Code-AI framework

Use **`/ca-config-audit`** after customization or for missing/damaged framework files. It checks the Code-AI folder (including its VS Code workspace file), links and duplicate skill names, and explains findings.

Checks include validation; normal context/configuration edits appear as notes. It does not repair files, test project code or prove Copilot loading.

## Find your files

| Location | Contents |
|---|---|
| [Project overview](project/overview.md) / [reference map](project/reference-map.md) | Project context and source links |
| [Active tickets](tickets/active/) / [archive](tickets/archive/) | Briefs, notes and attachments |
| [Knowledge](../{{knowledge_link}}/README.md) | Reusable guides |
| `.github/skills/` | Workflow instructions and templates |
| `tools/` and `.framework/` | Tools and setup records; keep both folders |

**Transfer error:** Inspect **both active/archive copies** and `.ticket-transfer-incomplete.json` before deleting anything. See [backup and relocation](../README.md#move-back-up-or-remove-this-folder) in the root guide.

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

Replace the example ID/description with yours. Add `--with plan,review,notes,files` to creation for selected optional resources. Add `--help` after a subcommand, such as `audit --help`, for more options. Saved audit reports go under `.framework/reports/`.

</details>
