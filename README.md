# Code AI Workspace — start here

A portable development folder for independent repositories, project context, ticket notes and optional GitHub Copilot workflows in VS Code. The Python tools also work without Copilot.

**Development status:** 0.1.16 pilot; native Windows and some Copilot/GUI checks remain pending. See [validation results](WORKSPACE_SETUP/VALIDATION_REPORT.md).

1. **Extract the ZIP and open the `Code-AI-Setup-<version>` folder containing this README.** On Windows, use Extract All first. An approved Python 3.9+ interpreter must already be installed.
2. **Double-click `Start macOS.command` or `Start Windows.cmd`.** Both files are beside this README, outside `WORKSPACE_SETUP`.
3. **Review the settings and press Enter or type `y`/`yes` to continue to the read-only preview `[Y/n]`.** To change them, decline, edit `WORKSPACE_SETUP/settings.json`, save and start again.
4. **Review the file preview and type `y`/`yes` to create `[y/N]`; Enter cancels.** Setup creates and validates your new development folder. Review the result, then type `q` or `quit` to finish.
5. **Open your repositories in your preferred IDE.** VS Code users can open `ide_configs/<vscode_workspace_name>.code-workspace`; setup prints the exact path.

`root_folder_name` names the development folder, and `parent_directory` in `WORKSPACE_SETUP/settings.json` chooses its parent directory; `"."` means beside the launcher. The parent must already exist. You can move or rename the entire generated development folder afterward.

`vscode_workspace_name` defaults to `Development` and controls only the VS Code filename, independently of `directories.primary_repositories`. Other IDE users can ignore that helper file but must keep it for validation.

By default, the new development folder is created inside this setup folder, beside the launchers. Some extractors add another outer folder; open the one containing the README and start files.

Clone/add approved folders under the generated repository groups, then double-click its refresh_vscode_workspace launcher to review registration and workspace updates. Start with the generated README; daily commands are in DAILY_WORK.md inside the AI working folder. You can move the complete generated folder elsewhere. Remove installer files only after keeping or moving the generated folder; do not delete a setup folder that still contains your work.

Setup writes only inside the new development folder. Existing destinations are refused. No software installation, sign-in, repository cloning, global settings or backup configuration occurs.

Declining the first settings prompt exits immediately. After later outcomes, `q`/`quit` exits the launcher; Windows closes the launched window. macOS Terminal may retain a finished window under its existing profile; setup changes no profile or automation permissions.

Optional details: [setup guide](WORKSPACE_SETUP/SETUP_GUIDE.md), [configuration](WORKSPACE_SETUP/settings.json).
