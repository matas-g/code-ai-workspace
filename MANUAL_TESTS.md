# Manual tests — Code-AI development tracker

**Last updated:** 29 October 2026<br>
**Version tracking:** See `VERSION` in [workspace_manager.py](WORKSPACE_SETUP/scripts/workspace_manager.py) for the current source version; each result below records the release actually tested.<br>
**Purpose:** Keep track of manual checks while developing this solution. Read this file when asked what still needs manual testing. Update results from explicit tester reports or actual observed manual tests; never infer a pass from an automated test or from file presence.

This is a maintainer-only project file. Keep it outside WORKSPACE_SETUP and exclude it from the ZIP and generated development folders. Product instructions belong in SETUP_GUIDE.md and the generated user guides. Preserve this tracker and its evidence across releases; reopen a passed test only when a relevant change or a new platform/version needs retesting.

## Status and evidence

- **PENDING:** No recorded manual result for the specified environment.
- **PASS / FAIL:** Observed or explicitly reported result, with the environment and evidence recorded below.
- **BLOCKED:** Cannot test in that environment; record the reason and use the documented fallback.
- **REPORTED:** Informal tester confirmation with incomplete environment/scope evidence; do not treat it as comprehensive validation.

For each run, record: date; test ID; release; native OS; Python; VS Code and Copilot versions; selected environment (Local where intended); mode (Ask/Plan/Agent); relevant restrictions; result; concise evidence or sanitized evidence reference; follow-up. Record the model only if it affects the result. Keep secrets and company data out of this tracker.

Use synthetic repositories, ticket IDs and context files for pilot testing. Repeat relevant checks on Windows 11 and under any applicable managed configuration. A macOS result does not close a Windows test. Automated shell/PTY tests do not prove GUI click behavior or Copilot loading.

Reusable local fixtures are in `_tmp/test_data/`: two small independent Git repositories per default grouping directory, copying instructions and optional overview/reference-map examples. See `_tmp/test_data/README.md` before copying them into a generated workspace. `_tmp/` and `_old zips/` are local development aids excluded from version control and product releases. Future superseded release ZIPs and checksums belong in `_old zips/`. Preparing or running sample code does not close any manual test below.

## Outstanding checks

P0 = verify before relying on automatic context. P1 = normal pilot/platform check. P2 = optional editor adoption.

| ID | Priority | Manual check | macOS | Windows 11 |
|---|---|---|---|---|
| COP-01 | P0 | Discover the generated AI Work orientation in the Local customization UI; confirm actual inclusion in References/debug evidence in a fresh chat. | REPORTED (partial; request inclusion confirmed) | PENDING |
| COP-02 | P0 | Cross-root and mode matrix: fresh chats with MAIN, OTHER and DOCS files active, in Ask/Plan/Agent where available; verify orientation loading and relevant project-context reading. | REPORTED (partial; see observations) | PENDING |
| COP-03 | P0 | Repeat automatic loading with custom major folder names/VS Code filename, then after moving/renaming the complete generated tree and removing the installer. | PENDING | PENDING |
| COP-04 | P1 | Coexistence with repository instructions; relevant context only; incomplete/stale overview/reference-map fields are surfaced without invented facts. | PENDING | PENDING |
| COP-05 | P1 | Instructions unavailable or policy blocked: direct attachments and normal Python commands remain usable; no global changes or policy bypass are required. | PENDING | PENDING |
| SKILL-01 | P1 | Original three skills (jira-ticket-init, change-review, config-audit): synthetic ticket creation, review checklist and read-only audit. Distinguish skill discovery from orientation discovery. | REPORTED successful (pre-0.1.10) | PENDING |
| SKILL-02 | P1 | 0.1.10 init prompt capture: ID-only, supplied details, multiline/Unicode/quotes, no invented requirements, repeat initialization preserves an edited brief and reports unapplied details. | PENDING | PENDING |
| SKILL-03 | P1 | New archive/restore slash skills: discovery, shared helper loading, full-folder preservation, repeat no-ops, collision refusal and operation after relocation. Prior CLI success does not close this test. | PENDING | PENDING |
| SKILL-04 | P1 | 0.1.11 prefixed skills: discover and invoke ca-jira-ticket-init, ca-jira-ticket-archive, ca-jira-ticket-restore, ca-change-review and ca-config-audit. Verify helper/checklist loading, prompt capture and archive/restore after custom naming and relocation. No old unprefixed framework copies in a fresh installation; unrelated skills remain available. | PENDING | PENDING |
| SKILL-05 | P1 | Unreleased ca-workspace-refresh: initial setup recommends the manual launcher before opening the saved workspace. Verify slash discovery, read-only preview/no-op, declined and approved updates, changed-preview reapproval, explicit missing-entry cleanup, custom names and relocation. With the target workspace open, test adding the first MAIN root, replacing/removing the first root and later additions; record extension/chat interruption and launcher recovery. Check settings and repository files remain intact. | PENDING | PENDING |
| SETUP-01 | P1 | Native extraction and GUI double-click Start: default/custom names; settings [Y/n] Enter shows preview without writes, creation [y/N] Enter cancels; explicit decline, EOF/invalid input, success and existing-target error. Check trust/association behavior and q/quit/window retention. | PENDING | PENDING |
| CLI-01 | P1 | Validate/audit and setup validation: readable result/counts; errors and warnings before manual checks/notes; intentional configuration/context edits understood as informational. Check narrow terminals, long paths, colour/NO_COLOR, JSON mode and saved audit report confirmation. | PENDING | PENDING |
| REFRESH-01 | P1 | GUI refresh launcher: three groups, ordinary docs folders, aligned statuses/paths, long/Unicode names, narrow terminal, prominent No changes; [y/N] Enter cancels each write phase, [y/N/remove-missing] requires the explicit cleanup keyword; short/full answers and invalid input. | REPORTED partial (No changes) | PENDING |
| REFRESH-02 | P1 | Missing folders, rename/group move, explicit remove-missing, disabled/custom entries and partial cancellation; confirm configuration-only cleanup and correct VS Code roots. | PENDING | PENDING |
| VSCODE-01 | P1 | Open the actual saved multi-root workspace; confirm labels/order and independent Git roots. Edit workspace settings/comments in VS Code, refresh, and check preservation; editor changes during preview must cause refusal. | PENDING | PENDING |
| PLATFORM-01 | P1 | Approved interpreter discovery/missing-interpreter handling; Windows literal paths, reparse refusal and console input; macOS Finder/Terminal trust and physical closure behavior. | PENDING | PENDING |
| DAILY-01 | P1 | Small end-to-end project task with selected context, meaningful tests, review from verified per-repo baseline, ticket archive/restore with attachments and reusable knowledge. | REPORTED partial (task/lifecycle) | PENDING |
| RECOVERY-01 | P1 | Restore an approved backup to another location; check notes/assets, configuration, tools and unpublished work coverage, then validate and repeat key context checks. | PENDING | PENDING |
| DOC-01 | P1 | 0.1.17 onboarding (filenames: root README.md, AI Work/DAILY_WORK.md and COPILOT_GUIDE.md): a new user can follow the three shortened guides to open the workspace, create/review/archive a ticket, refresh repositories, find command help and use the Copilot attachment fallback. Check that repository labels, local ticket folders, starting Git commits, refresh choices and the Python working directory are understood. Check rendered tables and links with default/custom names. Automated link checks do not certify readability or Copilot discovery. | PENDING | PENDING |
| DOC-02 | P1 | Unreleased DAILY_WORK.md: a new user can follow the main workflow using Copilot skills and refresh launchers without entering Python commands. Verify the optional Python reference is at the bottom, its disclosure opens/renders correctly, and direct links reach it with default/custom names. Preserve baseline, refresh interruption and transfer-recovery guidance. | PENDING | PENDING |
| DOC-03 | P1 | Unreleased repository/release landing README: a new user can identify prerequisites, create the development folder, add repositories, run the manual refresh launcher and then open the populated VS Code workspace. Verify GitHub/source-download and extracted-release entry points, rendered layout/tables, help links and custom-path wording. | PENDING | PENDING |
| DOC-04 | P1 | Unreleased guide organization: follow installation/settings in SETUP_GUIDE.md, folder management/recovery in the generated README, ticket/audit workflows in DAILY_WORK.md and context/discovery in COPILOT_GUIDE.md. Verify cross-guide links, manual ticket moves, refresh interruption recovery and optional terminal examples with default/custom names, without the installer present. Automated link checks do not establish readability. | PENDING | PENDING |
| DOC-05 | P1 | Unreleased end-to-end onboarding: follow the quick setup through Copilot sign-in/Local selection, verified overview/reference-map content, orientation review, one-root/mode context check and sample ticket/audit. Verify source-template links lead to the corresponding generated sections with default/custom names; editing orientation and running the full maintainer matrix are not required. Exercise unavailable-feature fallbacks before daily work. | PENDING | PENDING |
| OTHER-IDE-01 | P2 | If adopting IntelliJ/Eclipse, test manual project import, shared notes/tools and actual Copilot features separately. | PENDING | PENDING |

Since 0.1.11, all current framework skills use the `ca-` prefix. Earlier recorded results below retain their original names and do not certify discovery of the renamed skills. Use the current prefixed names when running SKILL-01 through SKILL-03, and record discovery separately under SKILL-04.

Since 0.1.8, include the renamed `tools/workspace_manager.py` entry point in SETUP-01, REFRESH-01, SKILL-01 and DAILY-01. Verify the refresh launcher, direct validation/audit and ticket commands after relocation and installer removal. The tools folder should contain `workspace_manager.py`, `terminal_output_formatter.py` and `vscode_workspace_updater.py`. These checks remain pending until manually observed.

## How to run the context checks

Use the generated **AI Work/COPILOT_GUIDE.md** as the detailed procedure. For COP-01 through COP-03:

1. Populate the synthetic overview with a small verified repository responsibility map and the reference map with a source unique to that fixture. Do not use real confidential information.
2. Open the complete generated .code-workspace file, select the intended Local environment and check Chat: Open Customizations → Instructions. Note the actual displayed labels if they differ by version.
3. Start a fresh chat for each root/mode combination. Ask a task question requiring the fixture's context without attaching/naming the orientation or telling the agent which file to read. Explicit attachment is a separate fallback test.
4. Capture References/debug evidence that the orientation was included, then inspect source citations/file-read activity and answer correctness. Discovery in a list or repetition of a magic phrase is insufficient evidence.
5. Check behavior against relevant repository instructions, repeat after relocation/custom naming, and record unsupported modes or policy blocks separately. Keep the overall matrix pending until its intended combinations are covered.

## Recorded observations

Historical evidence is summarized without local paths, account identifiers, raw debug exports or screenshots. These summaries preserve the recorded scope and result; original private artifacts are not part of the repository.

| Date | Version | Test/scope | Environment | Result and evidence |
|---|---|---|---|---|
| 21 October 2026 | 0.1.5 | Basic refresh flow; new folders in repository groups | Not fully recorded | **REPORTED:** A three-folder registration transcript and an informal successful result were recorded. GUI, cross-platform, cleanup and Copilot checks remain open. |
| 24 October 2026 | 0.1.8 (reported) | Direct validate and audit after adding synthetic repositories/context | macOS; exact Python/VS Code/Copilot versions not recorded | **REPORTED:** Structurally-valid output included informational configuration/overview/reference-map changes and pending manual Copilot checks. This confirms only those command results. |
| 24 October 2026 | Installed release not confirmed | COP-02 partial: project-context navigation and cross-repository lookup | macOS; active root, mode, harness and exact versions not recorded | **REPORTED:** A screenshot showed overview/reference-map reads followed by relevant source/documentation reads and a correct answer to a synthetic project question. The prompt did not name the context files. Fresh-chat status, automatic instruction inclusion and other combinations remain unconfirmed. |
| 24 October 2026 | Installed release not independently confirmed | COP-01 / COP-02: initial MAIN request instruction inclusion | macOS; MAIN source file active; Agent mode; exact VS Code/Copilot versions not recorded | **PASS (request inclusion only):** Inspection of a local debug export confirmed the complete AI Work orientation was included in system instructions before file reads. The prompt did not name or attach it; subsequent tool activity read the project overview. This establishes that request's inclusion only. UI discovery, other roots/modes/platforms and an explicitly documented fresh-chat run remain outstanding. |
| 24 October 2026 | Installed release not confirmed; before 0.1.10 | SKILL-01 and DAILY-01 partial | macOS; exact Python/VS Code/Copilot versions and mode not recorded | **REPORTED successful:** Original three-skill flow, a small brief-driven task with checks, expected Git changes, No changes refresh, and direct ticket archive/restore were reported. No complete transcript or version matrix was recorded. Attachment preservation, collision recovery, other modes/platforms, prompt capture and renamed skill wrappers remain separate checks. |

The initial MAIN request now has direct debug evidence of orientation inclusion, alongside the screenshot's successful project-context navigation. The full discovery/fresh-chat and cross-root/mode matrix remains incomplete. Chat Debug request inspection is usable; the response References UI and separate Agent Debug Logs enablement are not independently confirmed. Automated source/link validation must not close these checks.

## Result entry template

- Date / test ID / release:
- OS / Python / VS Code / Copilot versions:
- Selected environment / mode / relevant model or restrictions:
- Result (PASS, FAIL, BLOCKED, REPORTED):
- Steps/fixture and evidence:
- Remaining combinations or follow-up:
