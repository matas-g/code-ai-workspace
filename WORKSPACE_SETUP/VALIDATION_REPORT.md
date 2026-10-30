# Validation report — design 1.0

**Date:** 30 October 2026<br>
**Status:** macOS pilot. Copilot orientation inclusion across roots/modes, native Windows and physical GUI behavior remain manual checks.

## Unreleased verification — default VS Code workspace name

On 30 October 2026, the default `vscode_workspace_name` changed from `Development` to `Code-AI` in shipped settings, the default configuration example and the omitted-setting fallback. Setup text, current guides/design and existing behavioral checks use `Code-AI.code-workspace`. Explicit custom names, including `Development`, remain supported; existing installations are not renamed.

- Python 3.15.0 and Python 3.9.6: **98 behavioral tests passed on each interpreter**, run serially on macOS against an isolated source copy. Commands: `python3 -I -S -B WORKSPACE_SETUP/tests/test_workspace.py` and `/usr/bin/python3 -I -S -B WORKSPACE_SETUP/tests/test_workspace.py` from that copy.
- Fresh omitted-setting, shipped-default, explicitly named `Development` and custom `Data Platform View` installations each passed validation, audit and generated README workspace-link checks.
- Source hashes and prepared root README/design mirrors were checked after documentation preparation. Logs and smoke results are retained under `_tmp/default-vscode-name-20261030/` in the maintainer project.

No native Windows or actual IDE/Copilot test was performed. Product/design versions and the existing 0.1.18 release ZIP/checksum remain unchanged; this is an unreleased source change. Earlier evidence below retains its original scope.

## Release verification — 0.1.18

Prepared on 29 October 2026 on macOS 26.6.2, Apple Silicon. This release includes the six-skill inventory with ca-workspace-refresh, centralized release-version preparation, revised guides and complete Copilot onboarding. Configuration/manifest/state schemas remain 1 and design version remains 1.0. Existing generated workspaces are not automatically upgraded.

- Python 3.9.6: **98 behavioral tests passed**. Command: `/usr/bin/python3 -I -S -B _tmp/release-0.1.18/verification/WORKSPACE_SETUP/tests/test_workspace.py`.
- Python 3.15.0: **98 behavioral tests passed**. Command: `python3 -I -S -B _tmp/release-0.1.18/verification/WORKSPACE_SETUP/tests/test_workspace.py`.
- Runs were serial against an isolated source copy with synthetic fixtures. Logs are `_tmp/release-0.1.18/python39-tests.log` and `_tmp/release-0.1.18/python315-tests.log`.
- Default/custom-name installations from the extracted final archive each passed **62 local file/section links**, all **six daily Python examples**, the sample ticket command, manual archive/command restore, validation/audit and report saving. Fresh trees contain **30 daily files**, six correctly named skills and installed version 0.1.18. Static project/package documentation passed **40 local file/section links**. The same workflow checks passed against the prepared source.
- The archive has **43 allowlisted source inputs**, their manifest and three enclosing README/launcher copies: **47 files** under `Code-AI-Setup-0.1.18/`. Member bytes, ZIP integrity, executable macOS entrypoint metadata, all source hashes, root document mirrors and the SHA-256 sidecar match. A second build is byte-identical. AGENTS.md, MANUAL_TESTS.md, development fixtures and machine metadata remain outside the archive.

Packaged workflow command: `python3 -I -S -B _tmp/release-0.1.18/check_release.py _tmp/release-0.1.18/extracted/Code-AI-Setup-0.1.18/WORKSPACE_SETUP -packaged`. Results are `_tmp/release-0.1.18/verification.json` and `_tmp/release-0.1.18/archive-verification.json`. The superseded 0.1.17 ZIP/checksum are archived without overwriting existing files.

Native Windows, physical GUI behavior, first-use readability and actual Copilot instruction/skill execution remain manual checks. Pending tracker entries now identify 0.1.18; no manual result was marked passed. The pre-release entries below retain their original dates, version scope and statements about artifacts available at that time; “unreleased” there describes their development-stage status.

## Unreleased documentation verification — complete Copilot onboarding

On 29 October 2026, the quick setup was extended through prerequisites, creation, repository population, refresh, opening VS Code, verified overview/reference-map context, orientation review, a basic context/ticket/audit check and the first daily task. Links identify packaged templates and direct users to their generated copies. Orientation editing is optional; unavailable features have explicit fallback checks. Extended maintainer checks remain separate. The mixed manual-completion table was replaced with focused prerequisites, optional follow-up and conditional troubleshooting. The landing/generated READMEs and design section 14.1 now use the same handoff; runtime behavior and schemas are unchanged.

Fresh default/custom-name installations each passed **62 local file/section links**, the **six daily Python examples**, the new `TEST-1` sample through the direct-command fallback, manual archive/command restore, validation/audit and report saving. Synthetic overview/reference-map edits remained informational. Static project/package documents passed **40 local file/section links**; all **43 source hashes** and both root document mirrors matched. Command: `python3 -I -S -B _tmp/copilot-onboarding/check_guides.py -final`. Results are `_tmp/copilot-onboarding/verification.json`. The setup guide is 1719 words versus 1658 before this change (about 4% longer).

The linked official [instruction](https://code.visualstudio.com/docs/agent-customization/custom-instructions) and [skill](https://code.visualstudio.com/docs/agent-customization/agent-skills) references were rechecked on 29 October 2026. No IDE/Copilot session was exercised; these checks do not certify onboarding usability, automatic loading or skill execution by Copilot. DOC-05 remains pending on both platforms. The behavioral suite was not rerun for this documentation-only change; prior results below retain their original scope. No new delivery ZIP or product/design version change was made.

## Unreleased documentation verification — guide organization

Reviewed the current implementation and project documents, excluding release ZIPs, machine metadata and the `_tmp`/`_old zips` development folders. The landing README retains the project overview and quick start; SETUP_GUIDE.md owns installation/settings/troubleshooting; the generated root README owns folder management, refresh choices and recovery; DAILY_WORK.md owns ticket/review/audit workflows and the optional Python reference; COPILOT_GUIDE.md owns context preparation, discovery and fallback. Knowledge guides retain their separate note-authoring purpose. The comprehensive design and historical evidence are preserved.

Repeated refresh, ticket and Copilot procedures in the setup guide were replaced with guide pointers; short entry-point quick starts remain usable independently. The setup guide is **1658 words**, down from **2672** (about 38% shorter). The five distinct landing/setup/generated guides are about **19% shorter overall**, using whitespace-delimited counts that include headings, tables and commands. Wording also clarifies manual ticket moves, external ticket links, audit scope and outer-folder renaming. Runtime behavior is unchanged.

The organization follows [GitHub's README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) and [Google's linking guidance](https://developers.google.com/style/cross-references): keep a useful landing page, provide enough context for the immediate action and link selectively to related detail. VS Code's [instruction](https://code.visualstudio.com/docs/agent-customization/custom-instructions), [skill](https://code.visualstudio.com/docs/agent-customization/agent-skills) and [workspace event](https://code.visualstudio.com/api/references/vscode-api#workspace.onDidChangeWorkspaceFolders) references were rechecked on 28 October 2026; their documented behavior does not establish this layout's actual Copilot compatibility.

On 28 October 2026, **98 behavioral tests passed** on Python 3.9.6 and Python 3.15.0 on macOS, run serially against an isolated source copy. Commands: `/usr/bin/python3 -I -S -B _tmp/guide-coherence/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/guide-coherence/verification/WORKSPACE_SETUP/tests/test_workspace.py`. Logs are `_tmp/guide-coherence/python39-tests.log` and `_tmp/guide-coherence/python315-tests.log`.

Default and custom-name installations each passed **56 local file/section links**, all **six daily Python examples**, manual archive followed by command restore with unchanged brief contents, JSON validation/audit and explicit report saving. Static project/package documentation passed **32 local file/section links**. The 43 source hashes and root README/design mirrors match; results are `_tmp/guide-coherence/verification.json`. These automated checks do not certify rendered usability or IDE discovery. DOC-04 remains pending on both platforms; prior manual results are unchanged. No new delivery ZIP or version change was made; the released archive below retains its original contents.

## Unreleased verification — repository landing README

The shared repository/release README now explains capabilities, prerequisites, a five-step quick start, generated layout, scope/portability, help and contribution entry points. Repository population and manual refresh precede opening VS Code. The setup guide follows the same sequence. The structure follows [GitHub's README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), checked on 28 October 2026. The builder relocates package-relative Markdown links for the root copy, including fragments, while preserving external URLs and same-document anchors.

On 28 October 2026, **98 behavioral tests passed** on Python 3.9.6 and Python 3.15.0 on macOS 26.6.2, Apple Silicon. Commands: `/usr/bin/python3 -I -S -B _tmp/readme-landing/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/readme-landing/verification/WORKSPACE_SETUP/tests/test_workspace.py`, run serially. Logs are `_tmp/readme-landing/python39-tests.log` and `_tmp/readme-landing/python315-tests.log`. The release test additionally verifies that relocated guide links reach the same bytes and preserve external/section targets.

Additional checks passed all 12 local file/section links in each of the repository, package, extracted-root and extracted-package README copies. A 47-file test archive initialized default/custom-name trees; synthetic repository folders in all three groups, followed by approved interactive refresh, produced the expected five VS Code roots and successful validation. Results are `_tmp/readme-landing/navigation-checks.json`. These checks do not open VS Code or certify usability; DOC-03 remains pending on both platforms. No new delivery ZIP was created, and the existing release archive/version remain unchanged.

## Unreleased documentation verification — daily workflow

DAILY_WORK.md now leads with Copilot skills and refresh launchers, with all manual Python examples in a collapsed optional reference at the bottom. The guide is 633 words, down from 825 (about 23% shorter). Baseline capture, initial manual refresh, preservation and recovery guidance remain included.

Read-only default/custom-name plans each verified 44 local links/anchors across the guides, orientation and refresh skill, and parsed all six Python examples against the current CLI. Checks also confirmed terminal examples appear only in the final disclosure, source hashes match and design copies are synchronized. Results are recorded in `_tmp/daily-work-focus/verification.json`. Runtime behavior is unchanged; the behavioral suite was not rerun for this documentation edit. Actual rendering and first-use readability remain pending under DOC-02 in MANUAL_TESTS.md. No new release ZIP was created.

## Unreleased development verification — refresh skill

The new explicit ca-workspace-refresh skill delegates to the existing noninteractive refresh tool. It previews changes, requests approval, repeats the preview before applying, retains missing registrations unless cleanup is explicitly requested, and applies as its final tool action. Guides recommend the manual launcher before first opening the VS Code workspace and explain possible Copilot interruption during later updates. No refresh algorithm, configuration schema or automatic upgrade behavior changes.

On 28 October 2026, **98 behavioral tests passed** on Python 3.9.6 and Python 3.15.0, run serially against `_tmp/workspace-refresh-skill/verification/WORKSPACE_SETUP` on macOS 26.6.2, Apple Silicon. Commands: `/usr/bin/python3 -I -S -B _tmp/workspace-refresh-skill/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/workspace-refresh-skill/verification/WORKSPACE_SETUP/tests/test_workspace.py`. Logs are `_tmp/workspace-refresh-skill/python39-tests.log` and `_tmp/workspace-refresh-skill/python315-tests.log`.

The extended namespace test requires all six skill folders. A new behavioral test covers default/custom-name installation, metadata and deployed links, user ownership, relocation, read-only preview, application with settings/repository-content preservation, and validation errors when the new skill is removed. Existing archive/manifest, launcher, ticket and concurrent-edit tests also pass. The unreleased source inventory has 43 inputs and generates 30 daily files; these counts do not describe the existing released archive below.

Final read-only default/custom-name plans each passed 44 local file/section link checks across the three guides, orientation and new skill. All 43 current source hashes match the manifest and both design copies are synchronized.

The generic Codex skill validator could not run because its local PyYAML dependency is unavailable. The actual Copilot frontmatter was checked with the framework's strict metadata validator; no dependency was installed. Automated checks do not execute Copilot or prove its approval behavior. SKILL-05 in MANUAL_TESTS.md remains pending on both platforms for discovery, approval/reapproval, first-root changes, interruption and launcher recovery. No new delivery ZIP was created; version and released archive remain unchanged.

## Unreleased development verification — centralized release versioning

On 28 October 2026, **97 behavioral tests passed** on Python 3.9.6 and Python 3.15.0, run serially against an isolated source copy. Commands: `/usr/bin/python3 -I -S -B _tmp/release-versioning/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/release-versioning/verification/WORKSPACE_SETUP/tests/test_workspace.py`. Logs are `_tmp/release-versioning/python39-tests.log` and `_tmp/release-versioning/python315-tests.log`.

Four new tests cover a synthetic version change propagated through the default ZIP filename, enclosing folder, README labels, source hashes, fresh installed state and daily CLI; static version reading without runtime execution; invalid version/output refusal before preparation writes; explicit root-document synchronization; preservation of historical test/changelog content; and byte-identical repeated ZIP builds. Existing custom-name, relocation, launcher and daily workflow coverage also passes.

The product version remains unchanged until a new release is prepared. No new delivery ZIP was created for this development change; the released archive and evidence below remain associated with their original versions. No manual GUI/Copilot result is inferred from these automated checks.

## Verification — released 0.1.17

- macOS 26.6.2, Apple Silicon.
- Python 3.9.6: **93 behavioral tests passed**.
- Python 3.15.0: **93 behavioral tests passed**.
- Commands: `/usr/bin/python3 -I -S -B _tmp/guide-review-0.1.17/verification/WORKSPACE_SETUP/tests/test_workspace.py` and `python3 -I -S -B _tmp/guide-review-0.1.17/verification/WORKSPACE_SETUP/tests/test_workspace.py`, run serially against an isolated source copy; each test uses synthetic directories. Logs remain in the ignored `_tmp` development folder.
- Existing default/custom-name, local-link, relocation, audit, ownership and package-inventory checks use the renamed daily tools. The distribution-boundary test also verifies exclusion of a synthetic maintainer MANUAL_TESTS.md input.
- Synthetic fixtures only; no real development workspace, corporate repository, sign-in, global setting or Copilot session was changed.

## New-user guide review (0.1.17)

The generated README clarifies repository labels, the two refresh approvals, disabled/missing entries and backup coverage. DAILY_WORK.md explains local ticket folders, recording a starting Git commit before edits, the Python working directory and incomplete-transfer recovery. COPILOT_GUIDE.md defines orientation and skills, explains where to find customization controls and preserves separate discovery/loading checks. Contributor-only AGENTS.md is organized as short maintenance rules.

The three guide templates total **1467 words**, down from **1553** (about 6% shorter), counting headings, tables and commands. The design's operating boundaries, configuration schema and command behavior are unchanged. VS Code instruction/skill documentation was rechecked on 28 October 2026; references are linked in COPILOT_GUIDE.md.

Default and custom-name generation each passed 41 local file/section link checks, all six documented Python commands, validation, audit and explicit report saving, alongside the existing behavioral suite. These checks establish structural correctness, not first-use usability or actual Copilot loading. DOC-01 and the existing platform/Copilot checks remain pending; no manual result is inferred from automated checks. Existing workspaces retain their original generated guides.

## IDE configuration wording

Version 0.1.16 changes the generated root README table to describe ide_configs as holding saved workspaces and other IDE-specific configuration files. No setup, refresh or IDE discovery behavior changes. The packaged README, source hashes, archive checksum and fresh default/custom-name generation are checked for this release; manual test results remain unchanged.

## Daily guide filename

Version 0.1.15 deploys the AI working guide as DAILY_WORK.md from payload/root/DAILY_WORK.md. Its contents are byte-for-byte identical to the previous AI_README.md template. The development-root README.md, knowledge README.md and COPILOT_GUIDE.md retain their names; no redundant AI-root README alias is installed.

Root navigation, Copilot guide section links, the orientation's daily-guide link, setup completion text, runtime required-file inventory, release mappings and current design/setup references use the new name. Existing default/custom-layout tests now assert DAILY_WORK.md exists and the old AI-root README.md does not. All 93 behavioral tests pass on both interpreters listed above, including relocation and release checks.

Additional synthetic default and custom-name checks verified 41 local file/section links across the three guides and orientation, successful validate/audit, and refusal when DAILY_WORK.md is missing even if the old README name exists. Package/source hashes, archive checksum and synchronized design copies are checked for the new release. These checks do not certify IDE discovery or first-use readability; manual results remain unchanged.

Existing generated workspaces are not automatically renamed or upgraded. Their older tools and file inventories remain paired with the original filenames; the new name applies to fresh 0.1.15 installations.

## Shorter generated guides (0.1.14)

Version 0.1.14 changes documentation and release metadata only. The root README starts with setup and repository management; the AI working README covers the ticket lifecycle and daily commands; COPILOT_GUIDE.md covers context preparation, loading verification and fallback. Repeated explanations, optional extension suggestions and low-value implementation details were removed. Less common CLI options remain available through subcommand help and the design retains the full technical contracts.

| Generated guide | Previous words | Revised words |
|---|---|---|
| Root README | 1320 | 574 |
| AI working README | 791 | 527 |
| COPILOT_GUIDE.md | 840 | 450 |

Whitespace-delimited counts include headings, tables and commands: 2951 to 1551 words overall (about 47% shorter).

The edit follows [GitHub README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) and [Google technical-writing guidance](https://developers.google.com/style/paragraph-structure): put the common task first, use short paragraphs/action headings, and link to related details. Current VS Code instruction and skill documentation was checked on 25 October 2026; this is documentation verification, not IDE discovery evidence.

Synthetic default and custom-name installations passed validation. The three rendered templates in each layout had 31 valid local file/section links, with no unresolved configuration tokens. The existing 93 behavioral tests passed on each interpreter listed above; no prose-matching tests were added. Final archive/source hash checks and generated-guide checks cover the packaged files. The full framework skill resources, runtime mappings and Copilot orientation remain unchanged apart from the runtime package version.

First-use readability, actual IDE rendering and the existing Copilot/platform checks remain manual. DOC-01 was added to MANUAL_TESTS.md with pending status; no prior manual result was closed or reset. Existing generated workspaces are not automatically rewritten, because these guides have generated-file baselines.

## Public distribution review

Version 0.1.13 generalizes project origins, platform adoption and security requirements without changing the initialization boundary, configuration schema or daily operations. Historical manual observations retain their recorded results and limits; identifying paths, debug identifiers and private artifact names have been removed. Technical platform/interpreter versions remain as compatibility evidence.

Git ignore checks exclude local development fixtures, archived releases, machine metadata, caches and common credential files. A source scan found no remaining identifying origin details, non-placeholder home paths, email addresses or common credential signatures. The new archive contains only the explicit release inventory. These checks cover the current source and release; private development folders are outside the publication set. No Git history was available in the reviewed source folder.

## Consistent confirmation defaults

Start displays `[Y/n]` only for continuing from reviewed settings to the read-only preview; empty/whitespace input proceeds without creating files. The creation confirmation and both refresh write phases display `[y/N]`, with empty/whitespace input canceling. Missing-entry registration displays `[y/N/remove-missing]`; only the explicit keyword requests configuration cleanup. Short/full answers remain case-insensitive, invalid input repeats the prompt, and EOF cancels even at the yes-default question.

Behavioral coverage verifies read-only preview through Enter, creation cancellation through blank/no/EOF and successful explicit creation afterward. Refresh checks verify matching labels, blank cancellation of each write phase, preservation of already-approved registrations, and explicit missing-entry cleanup. No-change phases still skip prompts; the existing native launcher test covers final Enter retention and q/quit. Native Windows and physical GUI confirmation behavior remain manual checks in SETUP-01 and REFRESH-01.

## Framework skill namespace

All five packaged skills now use `ca-` in their directory names, frontmatter names and slash commands. Shared ticket-helper links, runtime loading/required-file inventory, release mappings, tests and current guides use the prefixed paths. No duplicate old-name aliases are installed. Future framework and framework-maintenance skills follow the same convention, documented in the design and the maintainer-only AGENTS.md. The release builder rejects unprefixed skill paths, and strict packaged-skill validation enforces the prefix; ordinary audit still accepts unrelated skill names.

A namespace regression test checks the exact five generated skill folders, matching metadata and local resources, rejection of an unprefixed framework skill without configuration writes, and successful read-only audit of an unrelated unprefixed skill. Existing relocated ticket lifecycle and release tests cover the renamed helper. Copilot discovery of the renamed commands remains a new manual check (SKILL-04); earlier results under the original names are preserved separately.

## Ticket prompt capture and lifecycle skills

The init skill extracts the supplied ID and task details, passes properly quoted literal text through `--description` and creates only the selected resources. A new brief records those details without inventing acceptance criteria or baselines. The new template field is resolved before inserting user content; braces, quotes, multiline and Unicode text are preserved. Older/custom templates without the field receive an appended details section. Existing briefs remain byte-for-byte intact, with an explicit result when supplied details were not applied. Blank details retain the original template behavior; invalid controls and archive/restore description arguments are refused before changes.

The new ca-jira-ticket-archive and ca-jira-ticket-restore skills invoke the existing sibling ticket helper. All five workflows are packaged, inventoried, link-checked and validated as explicit-invocation skills. No new Git/Jira/network integration or movement implementation is added. Five additional behavioral tests cover capture, repeat preservation, custom/unresolved templates, invalid options and both CLI entry points after custom-name relocation/installer removal, including unchanged archive/restore round trips.

## Readable diagnostic reports

Default validate/audit output and setup validation share the terminal formatter: a result and severity counts followed by nonempty Errors, Warnings, Manual checks and Notes sections. Editable user/local file changes are grouped with an explanation that intentional registration/context edits are normal. Paths remain complete; prose wraps to terminal width, with plain redirected/NO_COLOR/Windows output. Errors and warnings precede informational changes. Copilot loading remains explicitly uncertified.

Diagnostic-output behavioral tests exercise read-only text diagnostics, informational changes, error/warning ordering and exit status, JSON equivalence, saved audit report content/confirmation and narrow output with long Unicode paths. JSON report data and exit codes are unchanged; saved reports remain JSON. Noninteractive refresh/ticket and initializer output remain JSON.

## Daily tool filenames

Generated workspaces contain `tools/workspace_manager.py`, `tools/terminal_output_formatter.py` and `tools/vscode_workspace_updater.py`, deployed from matching source filenames. The initializer remains `scripts/workspace.py`. Both refresh launchers, dynamic helper loading, required-file inventory, package mappings, the ca-config-audit skill and documented daily commands use the new names. The diagnostic text layout is retained; ticket creation additionally supports initial prompt details. Existing installations retain their original filenames and are not automatically upgraded.

The relocation tests run validation, audit, refresh and ticket create/archive/restore without the installer, with default and customized directory names. The native macOS refresh-launcher test exercises the renamed command and formatting helper after relocation, including final quit handling. Windows launcher references are checked structurally; native Windows execution remains pending.

## Copilot orientation and onboarding

The package deploys a short, user-owned `.github/copilot-instructions.md` inside the configured AI Work root. It links to overview/reference-map documents, the active/archive ticket containers, configured repository groups, knowledge and daily commands. Relative links and encoded names support custom directory names and relocation. The orientation asks for relevant context and verified facts; it does not attach the whole framework or grant execution authorization.

The generated AI Work/COPILOT_GUIDE.md explains context preparation, Local discovery inspection, fresh-chat References/debug evidence, cross-root/mode checks, coexistence with repository instructions and explicit-attachment/direct-command fallback. The generated root README, DAILY_WORK.md and setup messages link users to it. Instruction support is environment/settings dependent, does not govern inline suggestions and is not certified by file presence.

Validation/audit require both files, check their local links and inventory ownership, and report orientation edits as informational user drift. Refresh preserves orientation edits. The pending-manual finding points to the generated guide and explicitly avoids certifying actual Copilot loading. No instruction setting, user/global instruction file or corporate clone is modified.

## Manual-test tracking

The development project has a separate MANUAL_TESTS.md tracker, outside WORKSPACE_SETUP. It records stable IDs, priorities, separate macOS/Windows status, evidence requirements and a run template. Historical inspection of a debug export confirms orientation inclusion while a MAIN file is active; the full cross-root/mode discovery matrix remains incomplete. Earlier macOS testing reported successful original three-skill and small task/refresh/direct archive/restore checks. Exact IDE/Python versions and the wider matrix were not supplied, so these reports are scoped separately from the 0.1.10 init-capture/lifecycle checks and 0.1.11 prefixed-command discovery checks, which remain pending. This tracker is excluded from the release archive and generated development folders; it remains a maintainer aid across versions.

## Packaging and compatibility — released 0.1.17

The archive has **42 allowlisted source inputs**, their manifest and three enclosing README/setup-launcher copies: **46 files** under `Code-AI-Setup-0.1.17/`. Development folders generated from that release contain **29 daily files**. Source hashes and the separate SHA-256 sidecar are integrity checks; trusted delivery provides authenticity. Both design copies are synchronized. Configuration/manifest/state schemas remain 1; design version remains 1.0.

Existing generated workspaces are not automatically upgraded. New installations use a fresh absent destination. Previous release ZIPs/checksums are moved into the project's _old zips folder as release housekeeping, not by the installer/runtime.

## Remaining checks

Full automatic orientation coverage for fresh Local chats across MAIN/OTHER/DOCS and available Ask/Plan/Agent modes remains unverified, including custom names and relocation. First MAIN-request inclusion has direct debug evidence, and the original three-skill flow has reported success. Prompt capture and discovery/resource loading for the current six skills, including the unreleased refresh skill, need fresh manual checks. Use the generated COPILOT_GUIDE.md and explicit attachments where automatic loading is unavailable; do not bypass policy or change global settings automatically.

Native Windows interpreter discovery, paths/reparse handling, rendering/input and console closure remain untested. Finder associations/trust prompts and physical macOS window closure require user testing; q/quit exits the process and the existing Terminal profile controls its window. Actual IntelliJ/Eclipse integration remains manual. No organizational approval, OS sandbox or automatic instruction compliance is claimed.
