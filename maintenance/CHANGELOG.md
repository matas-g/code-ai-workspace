# Changelog

## Unreleased

- Split the packaged release notes into dated user-visible changes and a separate compatibility reference with known issues and workarounds.

- License Code AI Workspace under MIT. Include the notice in installation ZIPs and beside the daily tools in newly generated workspaces.

- Add a maintainer-only `maintenance/test_data.zip` containing sample repositories with Git histories, populated project context and short copy/refresh instructions. No product or release inputs change.
- Add editable branch-name and commit-message formats to the project overview template, including ticket/no-ticket examples and repository-specific exceptions. Direct agents to these rules through the shared orientation; repository/company requirements take precedence over template defaults. Existing generated workspaces are not automatically updated.
- Set default branches to `feature/<ticket-id>_<short_description>` or `bugfix/<ticket-id>_<short_description>`, choosing `feature` when unspecified. Use commit subjects `<ticket-id> <Change area>. <Short summary>`, with a 1–4 word affected area or change type.

## 0.1.22 — 1 November 2026

- Add the repository-only caw-do-release skill for the established release preparation, isolated verification, ZIP/checksum checks, previous-artifact archival and commit/push workflow. Default to the next patch version or a prepared newer version; use the exact `Release v<version>` commit subject and keep issue references in its body. Align maintainer discovery and release authorization guidance; creating the skill does not execute a release.

- Detect interrupted ticket creation ([#4](https://github.com/matas-g/code-ai-workspace/issues/4)) with an explicit creation record, verified staging and no-overwrite publication. Refuse normal repeat success or transfers until incomplete creation is manually reconciled; report completed/pending resources without storing descriptions in metadata.
- Preserve existing user files and failed staging bytes. Add deterministic partial-write, interruption-boundary, collision, unsupported-publication and metadata regressions; document manual recovery, filesystem requirements and legacy/unupgraded-workspace limits. Package the recovery fix as a macOS pilot; design 1.0 and schemas remain unchanged. Existing generated workspaces are not automatically upgraded.

## 0.1.21 — 1 November 2026

- Separate skill audiences: shipped end-user skills retain `ca-`; repository-only maintenance skills use `caw-`. Rename ca-code-ai-onboarding to caw-chat-onboarding and align current contributor/design references.
- Add caw-whats-next for a short read-only live issue shortlist, caw-issue-triage for requested queue/label maintenance, and caw-implement-issue for one selected issue through scoped implementation, verification and evidence updates. Preserve the release allowlist, shipped skills and historical test outcomes.
- Fix the test write guard's parent-traversal and symlink-destination gaps ([#1](https://github.com/matas-g/code-ai-workspace/issues/1)). Resolve ancestors, check rename/link endpoints, and refuse ambiguous descriptor writes; preserve allowed in-scope operations and restore nested scopes after failures.
- Add tracked synthetic/real guard regressions with external sentinels and document process-wide scope and instrumentation limits. This guard change affects repository tests only.
- Integrate the guard fix in `e7c37a0` and close #1 after pushing to main. Package a new maintenance pilot with updated version/manifest and concise user release notes; daily behavior, design version and schemas remain unchanged. Test tooling and maintainer skills remain repository-only. Retain Python 3.9+; the approved Python-policy implementation remains separate in #11.

## 0.1.20 — 1 November 2026

- Separate repository and installation documentation: keep one canonical design, the full changelog and validation history in maintenance/. Add a development/release guide and a concise user compatibility/known-limitations page.
- Give the repository and installation READMEs independent purposes. Emit the user README once at the installation ZIP root; remove document mirroring and the obsolete --sync-project-docs option.
- Restrict installation ZIPs and their input manifests to user-relevant setup/runtime/configuration/payload files. Exclude development tests/build tooling, maintenance material and duplicate README/Start source copies. Keep the generated daily layout and runtime behavior unchanged.
- Direct setup users to their generated daily/Copilot guides, and add archive exclusion, document-preservation and extracted default/custom relocation checks. Existing published archives and versioned test history remain unchanged.

- Group the maintainer backlog, technical improvement plan and manual-test tracker under `maintenance/`. Update source navigation and contributor guidance; keep these files outside consumer releases and generated workspaces. Runtime behavior and historical test results are unchanged.
- Package the current source as a macOS pilot. Retain Python 3.9+ for this release by owner choice; the approved Python 3.12+ transition remains pending in GitHub issue #11. Design version and configuration/manifest/state schemas remain unchanged; existing generated workspaces are not automatically upgraded.

## 0.1.19 — 30 October 2026

- Change the default VS Code workspace filename from Development.code-workspace to Code-AI.code-workspace. Keep explicit custom names and existing installations unchanged; align settings, setup text, guides and behavioral checks with the new default.
- Package the current implementation as a macOS pilot with refreshed release labels, source hashes and project-root document copies. Design and configuration/manifest/state schemas remain unchanged. Known reliability work in the maintainer improvement plan and native Windows/GUI/Copilot verification remain outstanding.

## 0.1.18 — 29 October 2026

- Extend the quick setup through Copilot sign-in, verified overview/reference-map context, orientation review and a small context/ticket/audit check. Link the detailed generated guides, distinguish basic onboarding from the maintainer matrix, and separate prerequisites, optional follow-up and conditional troubleshooting. Runtime behavior is unchanged.
- Align documentation by purpose: keep installation/settings in SETUP_GUIDE.md, repository refresh/recovery in the generated README, routine tasks/commands in DAILY_WORK.md and context/discovery checks in COPILOT_GUIDE.md. Replace repeated procedures with focused links and shorten the setup reference without changing runtime behavior.
- Rework the shared repository/release README as a landing page with prerequisites, a five-step quick start, generated layout and guide links. Make repository population and manual refresh explicit before opening VS Code; preserve package-relative links in root/ZIP copies.
- Add the explicit ca-workspace-refresh skill for previewing and applying approved repository-list updates through the existing tool. Recommend the manual refresh launcher before first opening the VS Code workspace; document possible Copilot interruption and track IDE verification separately.
- Organize DAILY_WORK.md around Copilot skills and refresh launchers, with a compact ticket workflow and a collapsed optional Python reference at the bottom. Distinguish Code-AI framework checks from VS Code repository-list updates, explain ca-config-audit coverage and update incoming links.
- Clarify that ticket initialization leaves baselines unfilled, with an explicit prompt to record each affected repository's commit hash and existing work before editing code.
- Document manual ticket-folder moves as an alternative to archive/restore commands, with precautions and the commands' additional checks.
- Use workspace_manager.py as the single source for product and design version constants. Release preparation updates the README version before hashing; optionally synchronizes project-root README/design copies and derives the ZIP filename with --output-dir.
- Remove unnecessary current-version references from general guides. Preserve historical changelog and test evidence; keep release dates separate from the fixed reproducible ZIP timestamp. No new runtime dependency or automatic upgrade is added.
- Package the reviewed source as the next pilot release. Existing generated workspaces retain their original files; initialize a fresh destination to use this release.

## 0.1.17 — 28 October 2026

- Clarify first-use instructions for repository labels, refresh choices, local tickets, starting Git commits, Copilot context and terminal commands. Shorten the three generated guides while preserving cancellation, preservation and recovery rules.
- Clarify contributor instructions in AGENTS.md without changing skill naming or release rules. Runtime behavior and configuration schemas are unchanged.
- Refresh source hashes and the pilot archive; existing generated workspaces are not automatically rewritten.

## 0.1.16 — 28 October 2026

- Describe ide_configs as holding saved workspaces and other IDE-specific configuration files in the generated root README. This wording change does not add automatic configuration support for other IDEs.
- Refresh release metadata, source hashes and the pilot archive. Existing generated workspaces are not automatically updated.

## 0.1.15 — 25 October 2026

- Rename the generated AI working guide from README.md to DAILY_WORK.md and rename its source template to match. Keep the development-root README.md and COPILOT_GUIDE.md filenames.
- Update navigation and Copilot orientation links, setup messages, required-file inventory, release mappings and documentation together. New installations use the descriptive filename; existing generated workspaces are not automatically renamed or upgraded.

## 0.1.14 — 25 October 2026

- Rewrite the generated root README, AI working README and COPILOT_GUIDE.md around getting started, daily tasks and Copilot setup respectively.
- Replace repeated prose with short steps, task tables and links; remove optional extension suggestions, internal helper/template details and duplicated command explanations.
- Retain refresh/preservation rules, backup and recovery, direct-command fallback and honest instruction/skill verification limits. No daily command behavior changes; existing generated workspaces are not automatically updated.

## 0.1.13 — 24 October 2026

- Generalize project origins, adoption plans and security guidance for public distribution while preserving the design and runtime behavior.
- Anonymize historical manual-test evidence and retain its original scope and pending checks.
- Exclude local metadata, caches and development fixtures from Git publication; rebuild the manifest and pilot archive.

## 0.1.12 — 24 October 2026

- Standardize confirmations: `[Y/n]` continues from settings to the read-only preview, while `[y/N]` protects creation and both refresh write steps. Enter follows the displayed default; EOF always cancels.
- Show `[y/N/remove-missing]` only when missing registrations exist; cleanup still requires the explicit keyword. Accept short/full answers, repeat invalid input and retain no-change skipping and final `[q/quit]` behavior.
- Update guides, behavioral coverage and pending manual checks. Existing generated workspaces are not automatically updated.

## 0.1.11 — 24 October 2026

- Rename all five framework skills, their folders and slash commands with the `ca-` prefix. Update shared helper paths, required-file inventory, release mappings, tests and current guides together.
- Establish `ca-` as the naming rule for future framework and framework-maintenance skills, with release and strict validation checks. Unrelated audited skills retain their own names.
- Record renamed-skill discovery as a fresh manual check; preserve earlier results under the original names. Existing generated workspaces are not automatically upgraded.

## 0.1.10 — 24 October 2026

- Capture task details supplied to jira-ticket-init in a new brief through the optional `--description` argument. Preserve literal text, keep unknown requirements unrecorded and retain existing brief edits on repeat initialization.
- Add jira-ticket-archive and jira-ticket-restore skills using the existing deterministic ticket mover. Both operate only on local ticket folders and preserve their contents.
- Validate/package all five skills, update daily guides and cover prompt capture, custom templates, repeat preservation and relocated direct-command workflows.
- Record the reported successful original three-skill and finished-workflow checks separately from pending verification of these new capabilities. Existing generated trees are not automatically upgraded.

## 0.1.9 — 24 October 2026

- Format validation/audit results with an overall status, severity counts and separate ordered sections for errors, warnings, manual checks and notes.
- Group editable-file changes with a clear explanation that intentional repository registrations and context updates are normal. Use the same formatter for setup validation; preserve complete paths, wrapping and plain-text readability.
- Confirm saved audit report locations. Preserve JSON data, saved JSON format and command exit codes; other noninteractive commands retain their JSON output.
- Add diagnostic-output coverage and manual terminal checks. Existing generated installations are not automatically updated.

## 0.1.8 — 23 October 2026

- Rename the generated daily tools to `workspace_manager.py`, `terminal_output_formatter.py` and `vscode_workspace_updater.py`, with matching source filenames.
- Update helper loading, refresh launchers, required-file inventory, release mappings, skills, command examples and tests to use the new names. The setup-only `scripts/workspace.py` remains the initializer.
- Existing installations are not automatically renamed or upgraded; new installations use the updated filenames.

## 0.1.7 — 22 October 2026

- Generate a concise AI Work/.github/copilot-instructions.md orientation with relative, configurable links to project context, tickets, knowledge and daily tools. Existing repository/global instructions and settings are untouched.
- Include an independent COPILOT_GUIDE.md for context preparation, cross-root/mode discovery checks, References/debug evidence and explicit-attachment fallback. Automatic Copilot loading remains a manual check.
- Validate and audit the new files/resources; orientation edits are user-owned and preserved by refresh.
- Maintain MANUAL_TESTS.md at the development-project root, excluded from the package and generated workspaces. Native Windows, GUI and actual Copilot loading remain pending.

## 0.1.6 — 21 October 2026

- Align registration statuses and VS Code workspace paths in consistent preview columns. Preserve full names and use indented detail lines when a terminal is too narrow for columns.
- Show a prominent No changes message for up-to-date phases; omit the change legend when there are no registration rows. Warnings remain visible.
- Simplify refresh prompts to Action [yes/no] or Action [yes/remove-missing/no]. Short y/n answers remain accepted.

## 0.1.5 — 21 October 2026

- Added independent macOS/Windows refresh_vscode_workspace launchers in generated development folders, with two previews/approvals and final q/quit retention.
- Discover immediate child folders under configured repository groups; register new folders enabled with exact folder-name labels. Preserve existing IDs, custom labels and selections. Ordinary folders need no Git marker.
- Retain missing entries by default; explicit remove-missing cleans configuration only. Renames/moves are missing old entries plus new registrations.
- Refresh only the workspace folders value. Preserve settings, other properties and surrounding JSONC bytes; ordinary workspace edits no longer fail whole-file drift validation.
- Shared console presentation, concurrent-edit checks, documented direct preview/apply alternatives and expanded behavioral tests.
- No automatic upgrade of existing generated trees. Native Windows and actual Copilot discovery remain pending.

## 0.1.4 — 21 October 2026

Pilot release.

- Repository root labels use automatic `MAIN ·`, `OTHER ·` and `DOCS ·` prefixes. Groups stay together in a predictable order; AI Work and Knowledge retain their names.
- Grouped navigation extensions remain an optional manual experiment if prefixes prove inconvenient.
- Default repository folders are `MAIN_PROJECT` and `OTHER_PROJECTS`, configured with `primary_repositories` and `other_repositories`.
- One enclosing `Code-AI-Setup-<version>/` folder keeps the README, launchers and setup sources together on extraction.
- VS Code displays the AI working folder as **AI Work** and the knowledge folder as **Knowledge**.
- Offline, new-directory setup with settings review, file preview and validation; Python 3.9+ and standard library only.
- Clickable macOS/Windows launchers and a short setup guide.
- Configurable development folder, repository groups and independent VS Code helper filename.
- Portable daily notes, knowledge, local skills and ticket tools, independent of installer files.
- Relative links, structural validation and drift protection. Other IDEs use shared files/tools with manual project setup.
- Native Windows and actual Copilot skill discovery remain pending; see VALIDATION_REPORT.md.
