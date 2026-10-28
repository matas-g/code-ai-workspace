# Code AI Workspace

Keep repositories, task notes and reusable knowledge in one development folder. Each repository retains its Git history and tests; Copilot is optional.

## Get started

1. **Clone repositories** directly under the groups below, for example `{{primary_repositories}}/my-repo/`. Ordinary documentation folders work too; groups can stay empty.
2. **Refresh manually for initial setup.** Double-click [refresh_vscode_workspace macOS.command](refresh_vscode_workspace%20macOS.command) or [refresh_vscode_workspace Windows.cmd](refresh_vscode_workspace%20Windows.cmd). Review two steps: record folders in local configuration, then update VS Code's folder list. Type `q` to finish. Use the launcher before opening the saved workspace; the Copilot refresh skill is optional for later updates.
3. **Open [{{vscode_workspace_name}}.code-workspace](ide_configs/{{vscode_workspace_name_link}}.code-workspace)** in VS Code to see selected repositories together. For Copilot, [prepare project context]({{ai_work_link}}/COPILOT_GUIDE.md#prepare-once) and [verify your setup]({{ai_work_link}}/COPILOT_GUIDE.md#verify-your-setup), then continue with [daily work]({{ai_work_link}}/DAILY_WORK.md).

## Where things go

| Folder | Contents |
|---|---|
| `{{primary_repositories}}/` | Main repositories (**MAIN** labels) |
| `{{other_repositories}}/` | Other repositories (**OTHER** labels) |
| `{{company_documentation}}/` | Documentation folders (**DOCS** labels) |
| [{{ai_work}}]({{ai_work_link}}/DAILY_WORK.md) | Context, tickets, skills and commands (**AI Work**) |
| [{{knowledge}}]({{knowledge_link}}/README.md) | Reusable guides/assets (**Knowledge**) |
| `ide_configs/` | Saved workspaces and other IDE-specific configuration files |

Repositories appear separately, for example **MAIN · my-repo**. **DOCS** is a label, not a read-only restriction.

## Add, hide or remove a repository

After folder changes, run either root refresh launcher or `/ca-workspace-refresh` in Copilot. Refresh checks immediate child folders only, preserving custom labels and selections.

| What you want | What to do |
|---|---|
| Add a folder | Put it in a repository group, then refresh. New entries are enabled. |
| Hide a folder in VS Code | In `{{ai_work}}/.framework/installation.json`, find its `repositories` entry, set `include_in_workspace` to `false`, then refresh. |
| Keep a missing folder registered | Choose `y`/`yes`. Its selection stays unchanged; enabled entries reappear when the folder returns and you refresh. |
| Remove missing registrations | Choose `remove-missing`: remove **all listed missing registrations**, without deleting folders. |
| Rename a folder or move it between groups | Refresh treats it as a missing old entry and a new entry. Custom labels/selections do not transfer. |

In the launcher, **Enter or `n` cancels the current step.** Approved registrations stay saved if you cancel the workspace update; rerun refresh to finish. Up-to-date steps show **No changes** without prompting.

Refresh replaces the VS Code folder list, including manually added folders; settings, tasks and other content are preserved. If files change during preview, rerun. Restore missing group folders and review warnings.

Updating an open workspace, especially its first folder, can [restart extensions](https://code.visualstudio.com/api/references/vscode-api#workspace.onDidChangeWorkspaceFolders) and interrupt Copilot. If interrupted, use the launcher to inspect and finish the update. Actual IDE behavior remains a manual check.

For terminal use, see the [optional Python reference]({{ai_work_link}}/DAILY_WORK.md#optional-python-reference).

## Move, back up or remove this folder

- **Move:** Close the editor, move or rename the entire development folder (including hidden files), then reopen the saved workspace. Keep internal folder names and the VS Code filename unchanged. Added repositories/tools may have external paths to check.
- **Back up:** Use permitted storage with recoverable history. Git restores committed files; also back up uncommitted work and untracked notes/attachments. Test a restore elsewhere, run a [framework check]({{ai_work_link}}/DAILY_WORK.md#check-the-code-ai-framework) and check your files.
- **Discard the installer:** Keep the generated tree, including its refresh launchers, `{{ai_work}}/tools/` and `{{ai_work}}/.framework/`. Move it out of the setup folder before deleting that enclosing folder.

Delete this folder only after checking your backup. There is no automatic upgrade or restore; initialization always needs a new folder.

## IntelliJ, Eclipse and other editors

Open/import repositories normally. Setup generates only the VS Code workspace; keep that file for validation even if unused. Notes and Python tools work in other editors; check their Copilot features separately.
