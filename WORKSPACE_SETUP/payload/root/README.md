# Code AI Workspace

Keep independent repositories, ticket notes and reusable knowledge together. Use your usual editor, Git and tests; Copilot is optional.

## Get started

1. **Add your repositories.** Clone or copy approved project folders directly into the three repository groups below. Plain documentation folders work too.
2. **Refresh the workspace.** Double-click [refresh_vscode_workspace macOS.command](refresh_vscode_workspace%20macOS.command) or [refresh_vscode_workspace Windows.cmd](refresh_vscode_workspace%20Windows.cmd). Review and approve registration, then the VS Code folder changes. Type `q` to finish.
3. **Open [{{vscode_workspace_name}}.code-workspace](ide_configs/{{vscode_workspace_name_link}}.code-workspace)** in VS Code. To use Copilot, follow the [Copilot guide]({{ai_work_link}}/COPILOT_GUIDE.md).

## Where things go

| Folder | Contents |
|---|---|
| `{{primary_repositories}}/` | Main project repositories; shown as **MAIN** |
| `{{other_repositories}}/` | Other repositories; shown as **OTHER** |
| `{{company_documentation}}/` | Company documentation; shown as **DOCS** |
| [{{ai_work}}]({{ai_work_link}}/DAILY_WORK.md) | Project context, tickets, skills and daily commands; shown as **AI Work** |
| [{{knowledge}}]({{knowledge_link}}/README.md) | Reusable guides and their assets; shown as **Knowledge** |
| `ide_configs/` | Saved workspaces and other IDE-specific configuration files |

For daily work, use the [ticket and command guide]({{ai_work_link}}/DAILY_WORK.md). Ordinary editing, testing and code review stay in each repository. DOCS labels do not enforce read-only access.

## Add, hide or remove a repository

Run refresh after adding or moving folders, or changing your repository selection. It checks immediate child folders only and preserves existing custom names and selections.

| What you want | What to do |
|---|---|
| Add a folder | Put it in a repository group, then refresh. New entries are enabled. |
| Hide a registered folder in VS Code | Set its `include_in_workspace` to `false` in `{{ai_work}}/.framework/installation.json`, then refresh. |
| Keep a temporarily missing folder registered | Choose `y`/`yes`. It reappears after the folder returns and you refresh. |
| Remove missing registrations | Choose `remove-missing`. This removes **all listed missing entries from configuration only**, without deleting files. |
| Rename a folder or move it between groups | Refresh treats it as a missing old entry and a new entry. Custom labels/selections do not transfer. |

**At each write prompt, Enter or `n` cancels.** If you approve registration but cancel the workspace update, registration stays saved; rerun refresh to finish. Up-to-date steps show **No changes** without prompting.

Refresh replaces the VS Code folder list, including manually added roots. It preserves settings, tasks and other workspace content. If files change during preview, review a fresh preview. Restore missing group folders before retrying; inspect warnings for skipped folders.

For terminal use, see the [daily commands]({{ai_work_link}}/DAILY_WORK.md#run-commands-without-copilot).

## Move, back up or remove this folder

- **Move:** Close the editor and move the whole tree, including hidden files. Reopen the workspace from its new location. Keep the internal folder names and VS Code filename unchanged; repositories or tools added later may have their own external paths.
- **Back up:** Use approved storage with recoverable history. Git alone does not cover notes, attachments or uncommitted work. Restore to another location, run [validation]({{ai_work_link}}/DAILY_WORK.md#check-the-workspace) and check your files and unpublished work.
- **Discard the installer:** Keep the generated tree, including its refresh launchers, `{{ai_work}}/tools/` and `{{ai_work}}/.framework/`. Move it out of the setup folder before deleting that enclosing folder.

Delete the development folder only after checking your backup. There is no automatic upgrade or restore; never initialize over an existing folder.

## IntelliJ, Eclipse and other editors

Open/import repositories normally; notes and Python tools work independently of VS Code. Keep the unused VS Code helper file for validation. Copilot features need separate checks in each editor.
