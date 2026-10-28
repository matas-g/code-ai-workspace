# Setup guide

## Quick setup — five steps

1. **Get the files.** Clone/download the repository, or extract the release ZIP and open `Code-AI-Setup-<version>`. On Windows, use Extract All first. An approved Python 3.9+ interpreter must already be available.
2. **Create the development folder.** Double-click the macOS or Windows Start file beside `WORKSPACE_SETUP`. Review settings and press Enter to reach the read-only preview `[Y/n]`; type `y`/`yes` to create `[y/N]` (Enter cancels). Setup validates the result; type `q`/`quit` to finish. To change settings, decline, edit `WORKSPACE_SETUP/settings.json`, save and relaunch.
3. **Add your repositories.** Clone/add folders under the generated repository groups (defaults: `MAIN_PROJECT`, `OTHER_PROJECTS`, `COMPANY_DOCS`). Unused groups may stay empty. Setup does not clone anything.
4. **Refresh before opening VS Code.** In the generated development folder, double-click the refresh_vscode_workspace launcher for your OS. Review and approve registration, then the workspace folder-list update. Type `q`/`quit` to finish.
5. **Open the saved VS Code workspace** at the path printed by setup. Registered, enabled repositories now appear alongside AI Work and Knowledge. Other IDE users can open/import repositories normally; see the generated README for daily use.

The ZIP contains one enclosing `Code-AI-Setup-<version>/` folder, with the README, both start files and `WORKSPACE_SETUP/` together. An extractor may add another outer folder; open the folder containing the start files. The default generated development folder is created beside those start files, inside the setup folder. You may move the whole generated folder afterward or set `parent_directory` before setup. Keep or move that generated folder before removing installer files; do not delete its enclosing setup folder while it still contains your work.

## Settings (optional)

Edit `settings.json` in this folder before initialization. It is intentionally editable without rebuilding the package manifest. Other package inputs remain hash checked. `configuration-examples/renamed.json` illustrates renamed folders and repository entries; copy desired values into `settings.json`.

- `root_folder_name`: new root folder name, default `Code-AI`.
- `parent_directory`: existing parent directory where that new folder is created. Default `"."` means the launcher directory (or current working directory for direct Python use). Absolute paths choose another location; relative paths start at the launch directory, even when `--config` points elsewhere. Setup never creates missing parent directories, expands `~`/environment variables or changes the parent itself.
- `directories.primary_repositories`: folder for the main project repositories. It does not determine the VS Code filename.
- `directories.other_repositories`: additional development/reference repository group.
- `directories.company_documentation`: company documentation repository group.
- `directories.ai_work`: notes, tickets, local skills, daily tools and local metadata.
- `directories.knowledge`: reusable guides and supporting assets.
- `repositories`: optional entries with unique `id`, `group`, child `directory`, `display_name`, `access` (`develop` or `reference`, intent only), and boolean `include_in_workspace`. Use `display_name` for the base label without a group prefix: VS Code roots automatically show `MAIN ·`, `OTHER ·` or `DOCS ·` according to `group`. Setup never clones repositories or precreates their destination folders. After adding folders manually, the generated refresh_vscode_workspace launchers discover and register them; editing repository JSON is optional customization.
- `vscode_workspace_name`: optional VS Code filename stem, default `Development`; do not include `.code-workspace`. It is independent of repository folder names. Other IDE users may leave the default.
- `schema_version`: leave at `1`. Managed major names use letters, digits, spaces, `_` or `-` and start with a letter/digit. Repository child names also accept dots and Unicode, up to 255 characters, while rejecting separators, control characters and reserved/nonportable names. All names must be distinct within their scope.

### Names used in these instructions

Package guides are static: `<root_folder_name>` means `root_folder_name` from `settings.json`, and `<vscode_workspace_name>` means the VS Code filename stem. VS Code users open `<root_folder_name>/ide_configs/<vscode_workspace_name>.code-workspace` after setup; an explicit `--target` replaces the root path. Setup prints the exact destination and filename using the values you accepted. Generated README links and command paths use your actual selected folder names, and all five main directory names are applied dynamically.

The package name `WORKSPACE_SETUP`, `settings.json`, and internal paths such as `ide_configs/` and `tools/` are fixed. Literal configurable names in examples below are explicitly examples, not required values.

Example locations (edit the same JSON, keeping its other fields):

```json
"parent_directory": "/Users/yourname/Projects"
```

Windows JSON uses doubled backslashes:

```json
"parent_directory": "C:\\Users\\yourname\\Projects"
```

With `"root_folder_name": "Code-AI"`, the result is a new `Code-AI` child of the chosen parent. Use a native local path for the OS running setup. Redirected/symlinked parents and Windows UNC paths are refused.

The effective configuration is frozen before the two confirmations. If changed during setup, rerun to use the new values. Existing roots are always refused, even empty ones. Choose a new name/location; inspect any partial root before removing it manually.

The capitalized prompt choice is the Enter default: `[Y/n]` continues from settings to the read-only preview; `[y/N]` cancels creation or refresh changes. Both short and full answers are accepted, invalid input repeats the prompt, and EOF cancels even at the yes-default preview question.

## Manual command alternative

Run from the extracted package's top level; use the full path to your approved interpreter if needed. On macOS:

```sh
python3 -I -S -B WORKSPACE_SETUP/scripts/start.py
```

On Windows PowerShell (replace the example interpreter path):

```powershell
& 'C:\Path\To\python.exe' -I -S -B WORKSPACE_SETUP/scripts/start.py
```

`start.py --config FILE` selects another JSON file. `--target ABSOLUTE_NEW_PATH` overrides both `root_folder_name` and `parent_directory`. Direct command use anchors relative locations to the current working directory; clickable launchers first change to their own directory.

For noninteractive preview/creation use `WORKSPACE_SETUP/scripts/workspace.py plan`, then `init --apply` with the same optional flags. From the new workspace root, validate afterward with `<ai_work>/tools/workspace_manager.py validate`; `<ai_work>` means your `directories.ai_work` setting. The clickable flow performs validation automatically.

## Manual completion and daily use

All computer changes outside the generated folder remain manual: install approved prerequisites if absent; handle OS file trust/associations under company policy; open VS Code and make trust choices; sign in to approved Copilot; clone approved repositories; select an allowed backup location. No setup command performs these steps.

The generated root README contains the self-contained folder map, repository-inventory refresh steps, skill discovery check/fallback and backup/recovery guidance. Its `<ai_work>/DAILY_WORK.md` leads with Copilot skills and refresh launchers; direct Python commands are an optional reference at the bottom. No daily command depends on `WORKSPACE_SETUP`; retain only the generated workspace if desired. Keep a trusted release separately if future fresh initialization is needed.

## Add repositories and refresh VS Code

After initialization, clone or add approved folders directly under your three configured repository groups. Double-click `refresh_vscode_workspace macOS.command` or `refresh_vscode_workspace Windows.cmd` in the **generated development folder**. These daily launchers use the same style, interpreter discovery and console retention as Start; they need no installer. The macOS launcher is created executable.

For initial VS Code setup, run this launcher manually before opening the saved workspace. Later, `/ca-workspace-refresh` offers a chat preview and approval flow using the same tool. Updating an open workspace, especially its first folder, may restart extensions and interrupt Copilot; use the launcher to inspect and finish updates if needed. Actual skill discovery and interruption behavior remain manual checks.

The first preview lists new enabled registrations and missing-entry warnings. `y`/`yes` registers additions and retains missing entries; `remove-missing` registers additions and removes **all displayed missing entries from configuration only**. It never deletes folders or Git data. `n`/`no`, blank or EOF cancels. When no registration changes or missing entries exist, no prompt appears.

The second preview lists additions, removals, label updates and order changes to the VS Code folders list. Confirm with `y`/`yes` only if changes exist. Registration already approved remains saved if this second step is declined. Settings and all other content outside the folders value are preserved byte for byte, including comments, trailing commas, BOM and line endings. The changed folders value is regenerated. VS Code's own folder-list edits may be replaced because the inventory is authoritative when refresh runs. Final `q`/`quit` exits the launcher; unknown/blank input keeps output visible. Preview statuses/paths use aligned columns, with indented details for narrow terminals. Up-to-date phases show **No changes** without a change legend. Refresh prompts display `[y/N]` or `[y/N/remove-missing]`: Enter cancels, and cleanup requires the explicit `remove-missing` keyword. Both short and full answers (`y`/`yes`, `n`/`no`) are accepted.

Discovery scans immediate ordinary child directories only; no recursive search, Git marker, Git command or network access. Existing entries retain all custom values, including disabled selections. New display names use the exact child folder name; MAIN/OTHER/DOCS prefixes are added only when rendering roots. New company-documentation entries default to reference intent; the other groups default to develop intent. Neither enforces permissions. Missing entries retain their selection and return automatically after their folders return and refresh runs. Renames/moves are missing old plus new enabled entries, without inferred identity or transferred custom values. Unsafe names/redirections are warned and skipped; missing group directories stop the operation. Files changed during preview cause refusal.

From the generated root, substitute your configured AI directory for `<ai_work>`:

```sh
python3 -I -S -B "<ai_work>/tools/workspace_manager.py" refresh --interactive
python3 -I -S -B "<ai_work>/tools/workspace_manager.py" refresh
python3 -I -S -B "<ai_work>/tools/workspace_manager.py" refresh --remove-missing
python3 -I -S -B "<ai_work>/tools/workspace_manager.py" refresh --apply
```

Without flags, refresh previews both phases read-only. `--remove-missing` includes configuration-only cleanup in the preview; combine with `--apply` for explicit noninteractive execution. Interactive mode accepts cleanup only through its preview choice. Direct commands do not retain the terminal. Directory/VS Code filename changes after initialization remain unsupported. Existing generated trees are not automatically upgraded; initialize a fresh tree from the chosen release and transfer approved personal content manually, or keep using the old tools.

Daily `validate` and `audit` commands present a result summary and counts, then errors, warnings, manual checks and informational notes. Intentional edits to installation configuration, overview and reference map are normal and are listed together as changes since setup. Empty detail sections are omitted. Setup validation uses the same layout. Add `--format json` for machine-readable diagnostics; data and exit codes are unchanged. `audit --save-report NEW_FILENAME.json` saves JSON under the AI root's `.framework/reports/` and confirms the location in text mode. Other direct maintenance commands retain their JSON output; clickable Start and refresh launchers provide interactive presentation.

## Connect Copilot to the framework

The generated AI working root now includes `.github/copilot-instructions.md`, a short orientation pointing to the overview, reference map, selected ticket brief, knowledge and daily tools. Its links follow configured names and remain relative after relocation. The generated `<ai_work>/COPILOT_GUIDE.md` contains the self-contained onboarding and troubleshooting steps; no installer is needed for them.

Open the complete generated workspace, fill in verified project context and select your approved Copilot Local environment. Use Chat: Open Customizations to confirm discovery, then fresh chats/References/debug evidence to check actual loading and behavior while working in each MAIN/OTHER/DOCS root and available Ask/Plan/Agent modes. Repeat with renamed major folders and after relocation. This multi-root automatic-loading behavior remains unverified until those checks pass. Custom instructions do not govern inline suggestions.

Local instruction discovery depends on `github.copilot.chat.codeGeneration.useInstructionFiles` and any applicable policy. Inspect these manually if needed; setup does not change them. Where loading is unavailable, explicitly attach the orientation and relevant project/ticket files. Do not bypass policy or install global instructions automatically. The orientation is user-editable; refresh preserves its edits and validation checks its presence/local links without claiming Copilot discovery.

## Local ticket skills

The generated AI Work root contains six optional workflows: `ca-jira-ticket-init`, `ca-jira-ticket-archive`, `ca-jira-ticket-restore`, `ca-change-review`, `ca-config-audit` and `ca-workspace-refresh`. In a supported Copilot chat, `/ca-jira-ticket-init A-111 - implement a hello world application using python` creates the local ticket and records the supplied details in its new brief. With no description, the brief starts unrecorded. Missing context and requirements can be refined later; initialization does not invent them or fetch Jira. Existing briefs are preserved, and supplied details that were not applied are reported explicitly.

Use `/ca-jira-ticket-archive A-111` and `/ca-jira-ticket-restore A-111` to move the complete local ticket between active and archive. These skills share the deterministic ticket tool, retain attachments and refuse collisions. No Jira status or Git history changes occur. The generated AI Work/DAILY_WORK.md documents direct-command fallback, including `ticket create ID --description TEXT`. Verify all six skills in the actual IDE; prior direct-command results do not certify the new skill wrappers.

## Using another IDE

The shared repository layout, Markdown notes/knowledge and Python ticket tools can be used with IntelliJ, Eclipse or another editor. Open/import repository projects in that IDE yourself; use its normal approach to view the shared notes. Setup does not generate native IntelliJ/Eclipse projects or metadata and does not change their settings. Copilot's automatic skill discovery and feature availability require separate tests for that IDE; direct commands and Markdown procedures are the fallback.

The helper file in `ide_configs/` is specifically for VS Code. Leave it in place even when ignored because validation checks it. Refresh and repository `include_in_workspace`/`display_name` settings affect that file only. No IDE selector, automatic project import or additional IDE integration is introduced.

## Moving the generated development folder

Immediately after setup, the entire generated folder is portable. Close IDE sessions, move/rename the whole folder, then open/import repositories from the new location. VS Code users reopen the file in `ide_configs/`. No reinitialization or path rewrite is needed. Generated navigation links, workspace roots and inventories are relative; daily tools derive their location from their own files. The setup-only `parent_directory` is omitted from installed configuration, so no old absolute installation path remains.

Once you add repositories, extensions, scripts or external tools, their own absolute paths, linked worktrees or external dependencies may need separate attention. This does not change the portability of the fresh framework.

## Troubleshooting and verification limits

A missing interpreter is reported without downloading/installing anything. Do not bypass company controls if a launcher or PowerShell is blocked; use an approved direct Python invocation or contact your administrator. No execution-policy, quarantine or profile changes are automatic.

Declining the settings prompt exits before preview with no files created. Windows skips the final quit prompt; macOS process exit may leave a finished Terminal window depending on its profile. Preview cancellation, success and errors retain the console until you type `q`/`quit` or close it manually. Blank/unrecognized input leaves it open. Windows uses a literal input prompt, not a command shell, so input cannot execute commands. `q`/`quit` ends the launcher cleanly; it does not change the displayed setup result or turn a failed validation into success. On macOS, exiting closes the physical window only if the existing Terminal profile permits it. Otherwise close the finished window manually. No Terminal automation, permission prompts or global profile changes are added. [Apple explains this profile behavior](https://support.apple.com/guide/terminal/trmlshll/mac).

If initialization fails after creating the target, it retains an incomplete marker and refuses subsequent reuse. Inspect the partial tree manually and choose a new target. Validation checks structure, local links and recorded drift; it does not certify security approval or actual Copilot discovery. Native Windows and VS Code/Copilot tests are release gates recorded separately in VALIDATION_REPORT.md.

## Maintainer commands

Run synthetic tests with the approved interpreter: `python3 -I -S -B WORKSPACE_SETUP/tests/test_workspace.py`.
Set the product version only in `scripts/workspace_manager.py` (`VERSION`, using `MAJOR.MINOR.PATCH`). The independent `DESIGN_VERSION` changes only when the design version changes. Write the changelog and record actual verification separately; the builder never rewrites historical versions or test evidence.

Prepare the README version label, reviewed source hashes and project-root README/design copies with:

```sh
python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py --sync-project-docs
```

Without `--sync-project-docs`, preparation writes only inside `WORKSPACE_SETUP`. This flag requires the existing project-root `README.md` and `WORKSPACE_DESIGN.md` copies. Review the prepared files, run the tests above, then record the actual results and prepare again if documentation changed.

Build with an automatically named ZIP and checksum in an existing absolute directory:

```sh
python3 -I -S -B WORKSPACE_SETUP/scripts/build_release.py --sync-project-docs --output-dir ABSOLUTE_RELEASE_DIRECTORY
```

The default filename is `code-ai-workspace-<version>-macos-pilot.zip`; `--output ABSOLUTE_NEW_ZIP` still accepts a custom filename. Existing archives/checksums are refused. After verifying a newer ZIP, move the previous ZIP and checksum into the project's `_old zips/` folder without overwriting archived files; the builder does not archive them automatically.

Build inputs are explicitly allowlisted; arbitrary local files and personal installed data are excluded. The builder reads version constants without executing runtime code, updates the README before calculating hashes, and uses a fixed ZIP timestamp for reproducibility. It places reviewed launchers, README and source package inside `Code-AI-Setup-<version>/`, independently of any custom ZIP filename. No package files are stored outside it. Changelog entries, validation report versions/dates and manual-test evidence remain explicit records of the release actually reviewed or tested.
