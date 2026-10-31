# Code AI Workspace — Development Framework Design

**Design version:** 1.0  
**Prepared:** 20 October 2026  
**Updated:** 31 October 2026<br>
**Status:** Current implementation specification; platform validation results and remaining checks are recorded in VALIDATION_REPORT.md.  
**Audience:** Developers, maintainers, security reviewers, and an AI agent implementing the solution.  
**Supported initial environments:** Native Windows 11 and macOS; shared files/Python tools usable with any editor. Generated IDE integration is VS Code only; other IDE project import and Copilot discovery require manual setup/testing.  
**Use case:** Multi-repository development with shared project context, ticket notes, and reusable workflows.

This repository-only document defines the complete implementation deliverables and behavior. Platform support claims require the [validation evidence](VALIDATION_REPORT.md). User installation instructions belong in WORKSPACE_SETUP/README.md, SETUP_GUIDE.md and RELEASE_NOTES.md; development/release commands belong in [DEVELOPMENT.md](DEVELOPMENT.md). This is the single canonical design; no package or root mirror is maintained.

## 1. Outcome and operating principles

Build a small, portable development folder that combines ordinary editing, Git, testing, and code review with optional Copilot assistance. A developer can use it without an AI agent. Copilot uses the same files and deterministic commands that the developer uses manually.

The framework provides:

- Convenient access to independent repositories from a VS Code multi-root workspace.
- One folder for each Jira ticket, including its notes and supporting files.
- Project context and links to authoritative company documentation.
- A reusable technical knowledge base with guides and screenshots.
- A small set of reusable Copilot workflows.
- A reproducible setup package, local validation, and documented recovery.

**The initializer creates one new directory and writes only inside that directory. It must refuse a target that already exists, including an empty directory. It must not change any other computer configuration.**

Keep initial operation simple. Do not introduce a background service, agent orchestration platform, plugin dependency, automatic synchronization, custom VS Code extension, or mandatory cloud integration.

### 1.1 Requirement language

- **MUST / MUST NOT:** Required implementation behavior.
- **SHOULD:** Recommended behavior; explain any implementation deviation.
- **MAY:** Optional capability, not a first-release requirement.
- **Manual:** An action performed separately by the developer, outside the initializer and its automatic completion flow.

### 1.2 Requirements and implementation defaults

The framework has the following requirements:

1. The framework must remain practical and easy to use in daily VS Code and GitHub Copilot work.
2. It must support conventional development and extensive AI assistance.
3. It must be easy to distribute and initialize on Windows 11 and macOS.
4. Setup creates a new directory with its own structure and files, refuses an existing target, and makes no changes outside the new directory.
5. All required external changes must be performed manually and clearly documented in the setup guide.
6. Ticket material stays together and the complete folder can be archived.
7. Major directory names and the chosen root location are configurable.
8. Skills own their templates and resources.
9. Reproducibility, private recovery, configuration auditing, and low context overhead matter.
10. The framework must operate without MCP.
11. The solution must support review under applicable organizational security policies.

The concrete names, JSON schema, command interface, Python implementation, and minimal skill set below are implementation defaults. Follow them unless a platform or policy incompatibility requires a documented adjustment. Organizational security and deployment approvals remain separate from design approval.

### 1.3 Environment and adoption plan

- Python 3.9+ is required. Verify the installed version and any applicable software approval during manual prerequisite checks.
- Target the latest stable VS Code and GitHub Copilot extension available to the developer at testing time. Record exact tested versions; “latest” is a moving target, not an indefinite compatibility guarantee. Use an approved update channel where organizational policy applies.
- Copilot is limited to the developer's Local configuration, with Ask, Plan, and Agent interaction modes. Do not require another harness, background/cloud agents, or a switch away from Local.
- Local skills are optional and subject to applicable policy. Actual discovery in the non-Git, multi-root layout requires testing on the installed versions.
- Evaluate the framework with synthetic data on macOS and Windows 11. Record platform results separately; availability of one platform need not block a pilot on the other.
- Source and versioned releases may be published on GitHub or shared directly. Publishing does not imply production readiness or organizational approval; broad rollout and formal adoption are outside the initial scope.
- Each user chooses their own backup destination. Recommend durable cloud backup where permitted; restricted information must use storage permitted by the applicable policy. Setup never configures backup software or synchronization.

### 1.4 Initialization

- Separate the disposable initializer distribution from the generated daily framework. Never copy `WORKSPACE_SETUP`, source tests/design/payloads, setup launchers or a maintenance workspace into the generated root.
- The ZIP contains one enclosing `Code-AI-Setup-<version>/` folder. Its immediate contents are `README.md`, `Start macOS.command`, `Start Windows.cmd`, and `WORKSPACE_SETUP/`. Users need not enter the source folder unless customizing settings.
- Default to `<launcher directory>/Code-AI`, configurable through `WORKSPACE_SETUP/settings.json` (`root_folder_name`, `parent_directory`); direct CLI anchors relative locations to the current directory. `--target` overrides the default.
- Before the file preview, show effective settings, short descriptions, usage locations and the exact editable configuration path. Ask `[Y/n]` to continue: Enter opens the read-only preview; `n`/`no` or EOF exits immediately without preview or writes; invalid answers reprompt. Declining requires editing settings and relaunching.
- After accepting settings, show the actual file/directory preview and ask separately for creation approval. Freeze the validated settings before either prompt; never reread different values during creation.
- After creation, validate automatically. Print success only after validation succeeds; retain the console on success, preview cancellation and error until `q`/`quit` or manual closure. Initial settings rejection exits without a keep-open shell. Physical macOS Terminal closure depends on the user's profile; never change that profile or automate unrelated windows.
- Use an already installed approved Python 3.9+ and standard library. Never download/install Python, use an automatic-install manager, change quarantine/execution policy, authenticate, clone or configure backups.
- Daily commands reside only at `<ai_work>/tools/workspace_manager.py`, independently of installer files. Local metadata resides at `<ai_work>/.framework/`. All six skills are local daily workflows.

### 1.5 Naming and editor scope

Use development folder for the outer generated tree and VS Code workspace for the saved .code-workspace view. Configuration schema 1 uses root_folder_name, parent_directory and directories.primary_repositories. Default AI working files go under AI_WORK. ide_configs is a fixed generic helper container; only the VS Code helper is generated. Optional vscode_workspace_name defaults to Code-AI; never derive its filename from a repository group. Project names/folders and IDE filenames are separate concepts.

Shared files and Python tools are usable with any editor, including manual IntelliJ/Eclipse workflows. Do not claim automatic integration or equivalent Copilot behavior. Keep VS Code-specific settings explicit, and require its helper to remain for current validation. No IDE selector, plugin installation, native project generation or project import is automatic.

## 2. Scope and first release

### 2.1 Required first-release capabilities

1. Offline, deterministic initialization from a reviewed local package, with optional clickable Mac/Windows launchers.
2. A read-only preview and explicit execution command.
3. Configurable top-level names and repository inventory.
4. One daily multi-root workspace.
5. Project overview and reference-map templates.
6. A topic-oriented knowledge-base skeleton.
7. Ticket create, archive, and restore commands.
8. Six workspace skills: `ca-jira-ticket-init`, `ca-jira-ticket-archive`, `ca-jira-ticket-restore`, `ca-change-review`, `ca-config-audit`, and `ca-workspace-refresh`.
9. Read-only structural validation and configuration auditing.
10. Manual setup, backup, recovery, and removal instructions.
11. Automated tests of the file operations and a documented VS Code/Copilot smoke test on both platforms.

### 2.2 Explicit exclusions

The initializer MUST NOT:

- Install or update Python, Git, VS Code, extensions, packages, or certificates.
- Run a package manager or create a virtual environment.
- Clone, initialize, commit, fetch, or otherwise operate a Git repository.
- Authenticate, invoke a credential helper, or provision tokens.
- Change global or user-level Copilot instructions, skills, agents, or settings.
- Change VS Code user settings, profiles, synchronization, trust decisions, or extension state.
- Change Git configuration, shell profiles, PATH, environment variables, OS permissions, registry, keychain, scheduled tasks, or system settings.
- Enable MCP, plugins, hooks, browser automation, telemetry, or network access.
- Read unrelated home directories or discover existing global configuration automatically.
- Move or modify existing development directories, company repositories, notes, or documentation.
- Open VS Code or run arbitrary applications/generated workspace tasks automatically. A developer explicitly opening a clickable launcher may open a terminal and run the approved Python setup flow; this is the requested entrypoint, not an automatic post-install action.

The first release does not provide Jira API integration, spreadsheet processing, a database, a full-machine backup system, automatic configuration deployment into company repositories, automatic package updates, or WSL/SSH/container support.

## 3. Architecture and trust boundaries

There are three distinct activities:

| Activity | Who performs it | Permitted scope |
|---|---|---|
| Framework creation and testing | Implementing agent/developer | Authorized implementation/sandbox directory |
| Workspace initialization | Deterministic initializer | A single newly created target directory |
| Manual completion and development | Developer, optionally assisted later | Explicitly permitted tools, repositories, and company controls |

Generating this design or implementing the package is not authorization to install it on a real company computer. Tests MUST use synthetic fixtures. Real installation and manual completion are separate developer actions.

The source distribution can be outside the target. Initialization may read its own reviewed package, an explicitly supplied configuration file, standard-library/runtime files, and the minimum path metadata needed to validate the destination. It MUST NOT modify existing source-package files or write outside the new target, including when that target is a new descendant of the source directory. Do not turn prerequisite checking into a recursive scan of the machine.

An assistant may explain manual completion steps, but the initializer and setup agent MUST NOT execute those steps on the developer's behalf as part of initialization. In particular, generating a convenient post-install script that performs external changes would violate this design.

The write restriction applies to program-directed filesystem changes and subprocesses. The implementation MUST NOT claim to prevent ordinary OS auditing, antivirus activity, or changes made by the Python runtime's host environment. Use an approved interpreter; disable bytecode and site initialization as specified in section 8. The program itself has no network or external-process requirement.

Workspace files and natural-language instructions are not security boundaries. Company endpoint, identity, network, filesystem, and Copilot controls remain authoritative. A prohibition written in Markdown cannot enforce filesystem permissions or stop an authorized terminal from using available credentials.

## 4. Directory structure

The default new root is `Code-AI` beneath the launch directory. Configurable `parent_directory` chooses an existing parent, and `root_folder_name` its new child. The clickable launchers first select their own containing directory; direct Python use follows the terminal's current directory. An explicit absolute `--target` overrides this location. Refuse every existing target.

The following tree uses placeholders for configurable names; section 5.4 maps each placeholder to its setting. An explicit `--target` can replace the workspace root path.

```text
<root_folder_name>/
├── README.md
├── .gitignore
├── refresh_vscode_workspace macOS.command
├── refresh_vscode_workspace Windows.cmd
├── ide_configs/
│   └── <vscode_workspace_name>.code-workspace
├── <primary_repositories>/                 # manual clones later; no per-repository placeholders
├── <other_repositories>/
├── <company_documentation>/
├── <knowledge>/
│   ├── README.md
│   └── examples/example-guide/
│       ├── guide.md
│       └── assets/example-diagram.svg
└── <ai_work>/
    ├── DAILY_WORK.md
    ├── COPILOT_GUIDE.md          # onboarding, verification and fallback
    ├── .github/copilot-instructions.md  # short, user-editable orientation
    ├── tools/workspace_manager.py          # daily validation/audit/refresh/ticket commands
    ├── tools/terminal_output_formatter.py  # shared setup/refresh presentation
    ├── tools/vscode_workspace_updater.py   # minimal JSONC folder-list editor
    ├── .framework/
    │   ├── installation.json    # effective names and repository inventory
    │   ├── installed-state.json
    │   └── reports/             # empty until explicitly saving a report
    ├── .github/skills/
    │   ├── ca-config-audit/SKILL.md
    │   ├── ca-workspace-refresh/SKILL.md
    │   ├── ca-change-review/
    │   │   ├── SKILL.md
    │   │   └── resources/review-checklist.md
    │   ├── ca-jira-ticket-archive/SKILL.md
    │   ├── ca-jira-ticket-restore/SKILL.md
    │   └── ca-jira-ticket-init/
    │       ├── SKILL.md
    │       ├── scripts/ticket.py
    │       └── templates/{brief,plan,review,notes}.md
    ├── project/{overview,reference-map}.md
    └── tickets/{active,archive}/
```

The five major directory names are configurable. Internal paths remain fixed. Create the empty group/ticket/report directories; create no planned repository child folders, backup tree, large skill catalog or empty knowledge taxonomy.

No outer Git repository, installer/source folder, source manifest/payload baseline, maintenance workspace, global instruction file, root `AGENTS.md`, root `CLAUDE.md` or root `.github` tree is generated. Skills, templates, orientation, Copilot guide, daily tools and metadata shown above are the entire runtime dependency set. The installer files may be removed after success without breaking daily use. With the default parent, the generated development folder lives inside the enclosing setup folder: keep or move the complete generated folder before deleting the enclosing folder. No automatic relocation or cleanup occurs. New knowledge categories emerge as notes accumulate.

## 5. Configuration contract

Use UTF-8 JSON and Python's standard library. YAML is unnecessary for the initial release. Skill frontmatter remains YAML because the Copilot skill format requires it; the framework's own configuration is JSON.

### 5.1 Example installation configuration

This illustrative configuration uses the shipped default directory names and two example repository entries. Users may choose different names and repositories in settings.json.

```json
{
  "schema_version": 1,
  "root_folder_name": "Code-AI",
  "parent_directory": ".",
  "vscode_workspace_name": "Code-AI",
  "directories": {
    "primary_repositories": "MAIN_PROJECT",
    "other_repositories": "OTHER_PROJECTS",
    "company_documentation": "COMPANY_DOCS",
    "ai_work": "AI_WORK",
    "knowledge": "KNOWLEDGE_BASE"
  },
  "repositories": [
    {
      "id": "platform-sql",
      "group": "primary_repositories",
      "directory": "sql-repo",
      "display_name": "SQL Development",
      "access": "develop",
      "include_in_workspace": true
    },
    {
      "id": "engineering-docs",
      "group": "company_documentation",
      "directory": "engineering-docs",
      "display_name": "Engineering",
      "access": "reference",
      "include_in_workspace": true
    }
  ]
}
```

Configuration schema_version 1 is required. Directory keys, root_folder_name, parent_directory and vscode_workspace_name are optional with documented defaults; every field in a supplied repository entry is required. `repositories` defaults to an empty list. Missing directory entries use the documented defaults. Unknown keys, duplicate JSON keys, unsupported schema versions, and wrong value types MUST be errors rather than silently ignored.

Rules:

- The target is optional on the command line: omission selects `<parent_directory>/<root_folder_name>` (defaults `.` and `Code-AI`). An explicit target must be an absolute path and is not interpolated into configuration files.
- Fixed runtime internal names: `ide_configs`, `tools`, `.framework`, `.github/skills`, `project`, `tickets`, `active`, `archive`, and the documented filenames. `WORKSPACE_SETUP` is reserved for source distribution only.
- `parent_directory` is a nonempty, control-character-free native directory path. Default `.` refers to the launcher/current working directory. An absolute value selects a specific parent; relative values are anchored to the launch working directory, never the config file's directory. The parent must already exist and pass redirection checks. Reject UNC, unsupported foreign path syntax, drive-relative Windows paths and `~`/environment-variable expansion. `--target` overrides both location and name; no missing ancestors are created.
- All five named directories are configurable single path components. `root_folder_name` configures the default root basename; `--target` can separately override the full path.
- A repository `group` must name one of `primary_repositories`, `other_repositories`, or `company_documentation`.
- Repository `directory` is one portable component under its group. Nested repository paths are not supported.
- Repository IDs are unique lowercase ASCII identifiers matching `[a-z][a-z0-9-]{0,63}`.
- `access` is `develop` or `reference`. It describes intent and is not permission enforcement.
- `include_in_workspace` is an explicit boolean; reference material is not included merely because it exists on disk.
- Display names are bounded base labels, without control characters or a manually entered group prefix. JSON serialization handles escaping; workspace generation adds the group prefix for display only.
- No executable commands, environment expansion, arbitrary expressions, remote URLs, secrets, or shell fragments are accepted as configuration.
- The configuration does not store clone URLs. Developers obtain approved URLs separately and clone manually.

### 5.2 Portable names and path safety

For major framework directory components, accept 1–64 ASCII characters from letters, digits, spaces, underscores, and hyphens; require the first character to be a letter or digit. Reject leading/trailing whitespace, reserved Windows device names (case-insensitive), `.`/`..`, separators, drive syntax, colons, and NUL/control characters. Reject case-insensitive collisions among all top-level fixed and chosen names, and among repository paths within a group.

The enclosing target path may contain Unicode and spaces. Apply major-name restrictions only to framework-managed names; repository child names follow section 7.3. Preserve spelling; do not silently normalize user names. If the final basename is not portable between Windows and macOS, report it rather than silently renaming it. Native path-length or OS failures must produce a clear message without raising system limits automatically.

Require an existing parent directory. Do not create missing ancestors outside the target. Refuse filesystem roots, home-directory replacement, an existing file/directory/symlink at the target, or an unsafe destination. A new descendant directory inside the source package is allowed because only allowlisted inputs are copied; never copy the source tree recursively. Reject symlinks and Windows junctions/reparse points in the destination ancestry used for writes; do not follow them into another location. Fail closed if the implementation cannot safely identify the relevant redirection on a supported platform.

Every generated path must resolve inside the newly created target. Validate paths structurally, not with string-prefix comparisons. Reject `..`, absolute output paths, duplicate destinations, drive changes, and source assets that redirect outside the reviewed package.

Do not attempt to defend against a malicious local administrator concurrently replacing path components. Document that limitation and do not describe these checks as an OS sandbox.

### 5.3 Local state and ownership

Both local state files reside under `<ai_work>/.framework/`. `installation.json` holds the validated effective configuration, including defaults. The installer MUST omit the setup-only `parent_directory` from this installed configuration, even if the developer specified an absolute path. It contains no original absolute setup path. The root is derived from the installed tool's location. This makes moving the complete tree possible without rewriting stored machine paths.

`installed-state.json` has this illustrative shape (replace the path placeholder with the actual configured name):

```json
{
  "schema_version": 1,
  "package_version": "<release version>",
  "design_version": "1.0",
  "initialization_status": "complete",
  "vscode_workspace_name": "Code-AI",
  "managed_files": [
    {
      "path": "ide_configs/<vscode_workspace_name>.code-workspace",
      "owner": "generated",
      "sha256": "<64 lowercase hexadecimal characters>"
    }
  ]
}
```

The example version and hash are placeholders in this specification only. Actual state MUST contain the initialized package version and real hashes. Record the selected vscode_workspace_name in installed state, alongside directory_names. Refuse edits that change either after initialization; moving/renaming the outer development folder remains supported because its path is derived from the installed tool. Record every created file except the state file itself and transient initialization markers. Record created directories separately if needed for empty-directory validation. Use root-relative `/` paths.

Ownership classes:

- `framework`: Daily runtime and deterministic ticket scripts. Changes are errors; never auto-repair. Daily launcher/helper scripts are included; source-only package files are not installed.
- `generated`: Workspace files and generated entrypoint documents. Regeneration is explicit. Workspace folders are refreshed with preview/concurrent-edit checks; other workspace properties remain user controlled. Other generated files retain hash drift checks.
- `user`: Project overview, reference map, Copilot orientation, knowledge example and installed editable skill resources. Initial hashes are baselines; later changes are normal and are not automatically errors.
- `local`: Installation configuration. Private and user-editable within the supported schema.

Ticket content, company repositories, new knowledge articles, and saved reports are user data, not files continuously reconciled against release hashes. No hash inventory of entire corporate repositories or attachments is created by default.

### 5.4 Configurable names in user-facing text

Generated file links, command paths, workspace roots and terminal messages MUST use the validated effective configuration. An explicit --target determines the actual displayed root path/name. Never present a shipped default as the developer's selected value. Keep generated local links relative and URL-encode their path components where needed.

Static distribution READMEs and guides cannot assume a particular user's configuration. Use clear placeholders with a nearby explanation, generic file descriptions, or explicitly labelled default/example values. Do not rewrite source-package documentation when a user edits settings.json; its integrity checks must remain usable.

| Placeholder | Setting |
|---|---|
| `<root_folder_name>` | `root_folder_name`, unless `--target` overrides the root path |
| `<primary_repositories>` | `directories.primary_repositories` (repository container only) |
| `<other_repositories>` | `directories.other_repositories` |
| `<company_documentation>` | `directories.company_documentation` |
| `<ai_work>` | `directories.ai_work` |
| `<knowledge>` | `directories.knowledge` |
| `<vscode_workspace_name>` | `vscode_workspace_name`, default `Code-AI`; filename stem only |

`parent_directory` is an existing setup parent, not a name embedded in generated links. Repository group/directory/display/access/selection values must be read from configuration; literal sample repository names are permitted only in clearly labelled examples. Defaults in schema examples, default configuration files, central fallback constants and synthetic test fixtures are intentional values, not user-facing assumptions.

## 6. Distribution package and reproducibility

Distribute a versioned ZIP and separate SHA-256 checksum through a trusted release channel, such as GitHub Releases. Adjacent hashes detect accidental changes, not malicious replacement of an archive and its hashes.

```text
Code-AI-Setup-<version>/
  README.md
  Start macOS.command
  Start Windows.cmd
  WORKSPACE_SETUP/
    SETUP_GUIDE.md, RELEASE_NOTES.md
    settings.json
    package-manifest.json
    scripts/{workspace,start,workspace_manager,terminal_output_formatter,vscode_workspace_updater}.py
    launchers/{refresh_vscode_workspace macOS.command,refresh_vscode_workspace Windows.cmd}  # templates deployed into new development roots
    configuration-examples/{default,renamed}.json
    payload/{root,project,knowledge,examples,skills}/...
```

The repository contains development sources beyond this installation inventory. Keep maintenance documents, the full changelog/validation history, tests and build tooling out of the ZIP. The canonical user README and Start launcher sources are emitted once at the enclosing root, with no duplicate inner copies. Daily refresh-launcher templates remain inside the package because the initializer deploys them. The generated development tree remains a third, daily-use boundary with its existing tools and guides.

The release builder uses an explicit user-package `INVENTORY` plus three enclosing `ENTRYPOINTS`; no directory-recursive inclusion. It writes a manifest and deterministic ZIP with normalized timestamps, a 755 macOS entrypoint and a checksum sidecar. Every ZIP member path MUST begin with `Code-AI-Setup-<package_version>/`, derived from the manifest package version rather than the output filename. Keep all manifest source paths relative to `WORKSPACE_SETUP`; the enclosing folder is distribution packaging only. No package member sits outside this folder. Extraction tools may add an additional outer folder; document that users open the folder containing the README and launchers. It never overwrites a release archive. Arbitrary files, source `.git`, caches, credentials, reports, private config and test sandboxes are excluded. The reviewed default `settings.json` is deliberately distributed; users must not redistribute personal edits as an official default.

`scripts/workspace_manager.py` owns the single product `VERSION` constant and independent `DESIGN_VERSION`. The maintainer builder reads those literal strings without executing runtime code. Preparation updates the canonical user README's package-version label and manifest hashes; `--output-dir` derives the default ZIP filename from the same version. The repository README is independent and this design lives only under maintenance/. Preparation never rewrites repository/maintenance documents; the former `--sync-project-docs` option is removed. Builds write only inside the package and the requested archive/checksum paths. General guides avoid repeating the current product version. Changelog entries and validation/manual-test evidence retain their explicitly recorded release versions and are never automatically relabelled. ZIP timestamps are fixed independently of release dates.

Manifest schema 1 declares `package_version`, `design_version`, `minimum_python`, `files` and `directories`. Each file entry contains `source`, `sha256`, `destinations`; each destination has `directory_id`, `relative_path`, `render` (`copy` or `markdown`) and `owner` (`framework`, `generated`, `user`). Installer-only user inputs have an empty destinations list. Repository-only documents/tools/tests are omitted entirely. The enclosing README and Start launchers are outside the initializer input manifest and covered by the whole-ZIP checksum. Logical IDs are the five configured directories plus `root` and `ide_configs`; no `setup` output ID exists. The runtime contains an independent expected output/ownership inventory, including the two daily refresh launchers and helper modules, preventing source-only material or unexpected paths from being deployed.

Only the exact `settings.json` source entry may have `mutable: true`. Its initial byte hash records the shipped default, but initialization permits user edits and validates their schema. Every other listed input must match its hash before creation. Do not require users to rebuild a manifest to customize settings. A supplied `--config` file is parsed/validated separately. Integrity hashes are local baselines, not authenticity signatures or OS security controls.

The installer reads source files and renders the small deployment plan in memory, then copies only destination-mapped daily assets. No source payload baseline is installed. Deployed user-owned skills/templates can be customized and backed up; reviewed changes may be proposed manually for a future product release.

## 7. VS Code workspaces

### 7.1 Daily development workspace

`ide_configs/<vscode_workspace_name>.code-workspace` is generated as valid JSON, with paths relative to its own directory. VS Code supports named roots and relative paths in workspace files. [S1]

It includes:

1. Each selected, currently present primary development repository as a separate root, in configuration order.
2. The AI working directory.
3. The knowledge base.
4. Selected, currently present other repositories individually, in configuration order.
5. Selected, currently present documentation repositories individually, in configuration order.

Generate each repository label as `<prefix> · <display_name>` using `MAIN` for `primary_repositories`, `OTHER` for `other_repositories`, and `DOCS` for `company_documentation`. These fixed prefixes reflect logical groups even when directory names are customized. Store the base label only in configuration; users do not enter the group prefix. Keep `AI Work` and `Knowledge` unchanged. Preserve configuration order within each group and never add prefix-only separator roots, parent roots or virtual nesting. Paths and repository metadata remain independent of display labels.

Grouped navigation extensions such as Secondary Explorer or File Focus may be evaluated manually later if prefixes prove inconvenient. They are optional experiments; do not install, configure, recommend through workspace metadata or depend on them. Their actual compatibility remains untested.

Do not include the entire new root, the setup package, snapshots/backups, whole reference-parent folders, or both a parent and one of its children. Default empty configuration opens only AI working material and the knowledge base.

Do not include nonexistent repository paths. Planned repositories appear in the setup completion report as pending until manually cloned and followed by `refresh`.

Example using the shipped default directory names and the two illustrative repository entries from section 5.1 after their clones exist:

```json
{
  "folders": [
    {"name": "MAIN · SQL Development", "path": "../MAIN_PROJECT/sql-repo"},
    {"name": "AI Work", "path": "../AI_WORK"},
    {"name": "Knowledge", "path": "../KNOWLEDGE_BASE"},
    {"name": "DOCS · Engineering", "path": "../COMPANY_DOCS/engineering-docs"}
  ],
  "settings": {}
}
```

The workspace MUST NOT weaken security controls or encode trust, tool approval, MCP, account, telemetry, model, network, or Settings Sync preferences. No automatically executed tasks or extension installation. Leave settings empty initially.

Opening a workspace is a manual action and may cause normal VS Code indexing or workspace storage outside the chosen directory. This is separate from the initializer's filesystem contract; do not open it automatically or claim the VS Code session itself is confined to the target.

### 7.1a Other IDEs and the scope of IDE helpers

Use `ide_configs/` as a neutral container for generated IDE helper files. The first implementation generates only `<vscode_workspace_name>.code-workspace`; the `vscode_workspace_name` setting defaults to Code-AI and is independent of `directories.primary_repositories`. Do not add an IDE selector or native IntelliJ/Eclipse metadata generation. Shared repository groups, ticket/context/knowledge files and deterministic Python tools remain usable from any editor. Other IDE users manually open/import their projects and retain the unused VS Code file because current validation requires it.

Refresh, repository display_name and include_in_workspace apply only to the generated VS Code file. Documentation and terminal prompts must say so. IntelliJ/Eclipse project configuration, feature parity and automatic Copilot skill discovery need independent tests; direct Python commands and Markdown procedures remain the fallback. Do not change global settings or install IDE/plugins automatically.

### 7.2 Daily maintenance without installer sources

Do not create a maintenance workspace. The daily AI root exposes all six explicit skills and `tools/workspace_manager.py`. Validation, audit, refresh and ticket commands derive their paths from that installed script and local `.framework` files. No command reads a source manifest or installer folder after initialization. Daily refresh launchers and their console/JSONC helpers are installed alongside the runtime.

### 7.3 Discovery, refresh and configuration changes

Generated daily launchers `refresh_vscode_workspace macOS.command` and `refresh_vscode_workspace Windows.cmd` live at the development root. They invoke the installed runtime's `refresh --interactive` through an existing Python 3.9+ interpreter and retain their terminal until q/quit. Setup launchers remain disposable and separate. Both interactive flows use the same deployed console presentation helper. Refresh previews align the left name and right status/path columns, using terminal display widths. When both columns cannot fit, preserve full names and indent details consistently. Up-to-date phases display a prominent No changes statement before any warnings, without a change legend. Confirmation prompts use [Y/n] only to continue from settings to the read-only setup preview, and [y/N] for creation and both refresh writes. Enter selects the capitalized default; EOF always cancels. Missing-entry registration uses [y/N/remove-missing], with cleanup requiring the explicit keyword. Both y/yes and n/no are accepted; invalid input repeats the prompt. No-change refresh phases skip confirmation, and final [q/quit] requires explicit input to exit.

Discovery scans only immediate ordinary child directories of the three configured groups, without Git commands, repository-content inspection, recursion or a required .git marker. New entries get unique deterministic IDs, the actual folder name as their base display_name, include_in_workspace=true, and develop intent for primary/other groups or reference intent for company docs. New additions are ordered by group then folder name; existing entry order and fields are preserved. Skip unsafe/nonportable names and redirections with warnings. Missing group directories stop the operation rather than offering mass removal. Distinct case-insensitive folder collisions are refused.

Match existing entries by group and child folder. Never infer identity across renames/moves: the old entry is missing and the new folder is a new enabled registration with fresh defaults. Existing custom display names, IDs, selections and access intent remain unchanged. Repository child names may contain dots and Unicode (up to 255 characters) but must be one portable component, without separators, controls, reserved Windows names, trailing dots or surrounding whitespace. Major framework names retain the stricter 1–64 character rules.

The interactive flow has two separately durable approvals:

1. Preview new registrations and every missing entry. y/yes adds new entries and retains missing entries with their existing selection; remove-missing adds new entries and removes ALL listed missing entries from configuration only. No folders/Git data are deleted. n/no, blank or EOF cancels the operation. Offer the choice even if there are only missing entries. If neither additions nor missing entries exist, skip this prompt.
2. Using the saved configuration, preview additions/removals/label changes/reordering in the VS Code folders array. Ask y/yes only if it differs. On decline, leave the workspace untouched and retain previously approved registration changes. Settings and every other workspace property remain untouched.

Enabled entries whose folders are absent are excluded and warned about. Retained enabled entries return after the folder returns and refresh runs. Missing disabled entries remain disabled. Renames/moves do not carry old custom values to new entries. Old entries can be cleaned through the explicit remove-missing choice.

The workspace is user editable between runs. Refresh makes the inventory authoritative for the folders array, always including AI Work and Knowledge; it may replace manual root changes and remove external roots. It MUST preserve bytes outside that array value, including settings/tasks/launch/extensions, comments, BOM, line endings and formatting. JSONC comments and trailing commas are accepted; malformed/ambiguous documents and duplicate properties are refused. The folders value itself is regenerated only when its semantic list changes. Empty/missing folders arrays can be populated without rewriting unrelated content. Whole-file workspace drift is no longer an error; framework/generated documentation drift remains protected.

The noninteractive refresh command previews discovery plus workspace changes without writes. --apply explicitly performs both phases; --remove-missing includes the same configuration-only cleanup, with or without --apply. --interactive exposes the two prompts and accepts cleanup only via the typed choice. Direct commands exit normally; clickable launchers retain output until q/quit on cancellation, success and failure. Unknown/blank final input cannot execute commands or dismiss output. Never install/download interpreters or change terminal profiles.

Use the shared maintenance lock and atomic same-directory writes. Recheck configuration, installed state, relevant folder availability and workspace bytes before applying their reviewed phase; refuse concurrent changes. Each approved phase is durable independently. A failure after workspace replacement but before recording its new state hash leaves user-editable workspace content recoverable; validation accepts it and a rerun can continue. No multi-file transaction or automatic rollback deletion is claimed.

Directory names and the VS Code filename remain fixed after initialization. Existing installations are not silently upgraded. New installations include the independent runtime, JSONC helper, console helper and daily launchers.

For initial VS Code setup, recommend manually running the refresh launcher before opening the saved workspace. The optional explicit ca-workspace-refresh skill supports later chat-driven updates through the existing noninteractive preview/apply interface. It summarizes the preview, obtains approval for the displayed changes, retains missing entries unless configuration cleanup is explicitly requested, and repeats the preview before applying; changed proposals require renewed approval. Applying is its final tool action, with no required follow-up tool calls. The skill must explain that changes to the open workspace, especially its first root, may restart extensions and interrupt Copilot; actual behavior requires manual IDE testing. If interrupted, the launcher can inspect current state and finish remaining changes. The skill must not edit JSON itself, automatically retry failed writes, reopen the editor or perform Git/global changes.

## 8. Deterministic command-line tools

### 8.1 Implementation constraints

Use company-approved Python 3.9 or later, standard library only, native Windows and macOS. Do not assume Python is preinstalled. Runtime availability is a documented manual prerequisite. No pip, third-party shell modules, Node.js, or administrator access is required. Optional clickable wrappers use the built-in macOS shell/Terminal association and Windows Command Prompt/PowerShell; direct Python commands remain available.

Use `argparse`, `json`, `pathlib`/`os`, `hashlib`, and explicit file operations. Do not use `eval`, dynamic template execution, subprocesses, network libraries, OS credential APIs, or automatic Git operations in the Python tools. Thin, reviewed OS launchers may locate an already installed interpreter, set only their process working directory, invoke Python and retain their terminal. They must not install/download software, call automatic-install managers, run arbitrary input, change profiles or execution policy, or persist environment/configuration changes. Package scripts set `sys.dont_write_bytecode = True` before optional local imports, and documented invocations include `-I -S -B` to avoid user/site initialization and bytecode writes. Package modules must not depend on site-packages or user startup customization.

All CLI commands are noninteractive by default. Optional user choices are flags or JSON. A human-friendly summary appears on stdout; failures go to stderr. No logs or report files unless explicitly requested. Avoid printing absolute user paths except when needed to identify the chosen destination or a failing path; no environment dumps.

### 8.2 Command interface

Commands below are requirements for the tool to implement, not commands available merely because this document exists.

```text
workspace.py plan [--target ABSOLUTE_NEW_PATH] [--config FILE]
workspace.py init [--target ABSOLUTE_NEW_PATH] [--config FILE] --apply
workspace_manager.py validate [--format text|json]
workspace_manager.py audit [--format text|json] [--save-report RELATIVE_PATH]
workspace_manager.py refresh [--apply | --interactive] [--remove-missing]
workspace_manager.py ticket create ID [--description TEXT] [--with plan,review,notes,files]
workspace_manager.py ticket archive ID
workspace_manager.py ticket restore ID
workspace_manager.py --version
```

- `plan` reads package/configuration and produces the complete directory/file plan; it writes nothing.
- `init` without `--apply` fails with usage guidance; it never silently executes after preview.
Human-readable validation/audit reports share the Start/refresh terminal formatter. Show the result and severity counts first, then nonempty Errors, Warnings, Manual checks and Notes sections in that order. Group changed editable local/user files with a concise explanation that intentional edits are normal; do not downgrade generated/framework drift errors. Preserve complete paths and wrap prose. Setup validation uses the same report layout. `--format json` retains the structured report and exit codes, and saved audit reports remain JSON with a location confirmation in text mode. Other direct commands retain JSON output.

- `plan`/`init` belong only to source `WORKSPACE_SETUP/scripts/workspace.py`. Daily commands belong only to installed `<ai_work>/tools/workspace_manager.py`; they derive the AI/root locations from that script, validate local state and refuse incomplete/mismatched locations.
- `validate` and `audit` are read-only unless the user explicitly supplies the audit report option. A saved report destination must be below `<ai_work>/.framework/reports`, absent, and pass all containment/redirection checks.
- `refresh` without flags is a read-only discovery/workspace preview. --interactive prompts separately for registration and workspace edits; --remove-missing previews configuration-only cleanup (or applies with --apply).
- The ticket commands delegate to the installed ticket script with an in-process function call or standard-library import; do not shell out. The skill's script is the one authoritative ticket implementation.
- The ticket script is independently executable and derives AI working paths from its own installation location. It may share only standard-library dependencies; its templates remain beside its skill.

Interactive-only code `4` means initial settings declined (wrappers exit cleanly immediately). Exit codes: `0` success (warnings/pending manual steps may remain), `1` validation/integrity/operation failure, `2` invalid arguments/configuration or existing-target refusal, `3` incomplete initialization caused by a filesystem/runtime error. Return useful machine-readable statuses when `--format json` is chosen.

### 8.3 Initialization algorithm

1. Parse and validate flags, configuration, and package schema. Build a complete in-memory render plan.
2. Validate source hashes and destinations. Check target absence using APIs that detect dangling symlinks as well as ordinary files. Check the existing parent and path redirections. Package failures create nothing.
3. Render all output bytes in memory where reasonable; enforce unique destinations and supported substitutions. No arbitrary Jinja-like language. Placeholder syntax can be simple allowlisted `{{logical_name}}` fields; unresolved or unknown fields are errors.
4. Derive relative links structurally from logical paths. Use forward slashes and URL-encode Markdown path components where necessary. Preserve relative image links inside guides and tickets.
5. Create the target with exclusive directory creation. A race that makes it exist must cause refusal. Never precreate it with `exist_ok=True`.
6. Create an initialization marker inside it, then all planned children with exclusive file creation. Do not stage outside the new target, including elsewhere in the parent, OS temporary directory, home directory, or existing source-package locations.
7. Write effective configuration and initial state. Run internal validation without invoking VS Code, Git, or external tools.
8. Mark completion only after required files, hashes, and links pass. Remove the transient marker and print the result plus the manual completion checklist.

Validate path safety again before writes. Use binary writes for hashed assets and consistent UTF-8/LF for generated text. Do not change existing file ACLs or machine permissions. The reviewed `Start macOS.command` beside the enclosing README is packaged executable. Two daily refresh launchers are installed in the target. The newly created macOS daily launcher gets executable bits inside the target; other generated files use ordinary defaults. No existing external permissions are changed. The core tools run in-process through Python; user-invoked OS launchers are the only shell wrappers.

If initialization fails after creating the root, leave that partial root in place with a clear incomplete marker and diagnostic. Do not recursively delete it, resume into it, or label it complete. A retry at the same path MUST refuse it. The developer inspects/removes the partial root manually or chooses a new destination. A pre-write failure leaves no target at all.

Fresh initialization is intentionally **not idempotent at the same path**: it always refuses an existing root. Deterministic output for equivalent inputs and safe repeat behavior for ticket/validation commands are separate properties.

### 8.4 Clickable setup

Two reviewed launchers sit inside the enclosing `Code-AI-Setup-<version>/` folder, beside the README and `WORKSPACE_SETUP`, and run `WORKSPACE_SETUP/scripts/start.py` through an already installed Python 3.9+ with `-I -S -B`. macOS uses the shell/Terminal association; Windows uses Command Prompt and built-in no-profile PowerShell to locate installed executables through PATH/Python registry entries. Skip Store aliases and manager shims; do not trigger downloads or change policy. Probe version before executing the setup script.

The shared orchestrator first parses/fixes the effective config from `WORKSPACE_SETUP/settings.json` (or `--config`) and shows its absolute path. Explain every configurable value, effective target and fixed internal paths. Ask whether these settings are acceptable, then exit with internal code `4` on `n`/`no` or EOF. Enter continues to the read-only preview. Wrappers translate this to a clean immediate exit and skip their console retention. On macOS the finished window may remain due to Terminal profile settings; do not change them. Invalid answers reprompt.

After settings acceptance, run the same read-only `plan`, display all created directories/files including local state, and ask separately for creation confirmation. Accept only case-insensitive trimmed `y`/`yes`. Declining this second prompt creates nothing and retains the console. With approval, ensure the manifest has not changed since preview, refuse an occupied target, initialize and validate in-process. Read settings once; all output and creation use those frozen values. No unattended `--yes` option exists.

Wrappers retain output on success, preview cancellation and all failures until the user types `q`/`quit` or closes the window manually. Blank/unrecognized input must not dismiss logs or execute commands. Windows ends the launched command file; macOS exits cleanly and lets the existing Terminal profile control physical closure. Do not introduce Terminal automation, permission requests, profile changes or commands that close unrelated sessions. Print the interpreter, effective target, progress, result and manual work; no logs are saved automatically. Missing Python or blocked launchers require manual handling under existing policy.

### 8.5 Terminal presentation and final input

Use a small standard-library presentation helper: short section headings with consistent dividers, blank lines, indented bullets and settings descriptions, distinct destination/config paths, and a separate completion/error section. Wrap prose to terminal width; print complete filesystem paths unchanged so they remain copyable. Preserve scrollback; never clear the screen or animate/redraw progress. Optional ANSI emphasis may be used only in supported interactive terminals, disabled for redirected output, NO_COLOR and Windows consoles without proven ANSI support. Plain text must remain readable; no third-party styling dependency is permitted.

The final q/quit prompt belongs to clickable setup and daily refresh launchers, after the Python flow has returned, so direct CLI behavior remains unchanged. It applies to success, preview cancellation, existing-target errors, interruption and missing-interpreter errors. First settings rejection still exits immediately. Keep the actual result/exit code visible; q/quit is only a clean session exit, not a setup-success signal. EOF ends the launcher without claiming success. Never interpolate entered text into commands.

### 8.6 Manual invocation examples

From the extracted package's top level on macOS:

```sh
python3 -I -S -B WORKSPACE_SETUP/scripts/start.py
python3 -I -S -B WORKSPACE_SETUP/scripts/workspace.py plan
python3 -I -S -B WORKSPACE_SETUP/scripts/workspace.py init --apply
```

All source commands accept optional `--config FILE` and `--target ABSOLUTE_NEW_PATH`. They use configured `parent_directory` and `root_folder_name` (default current directory and `Code-AI`); clickable launchers anchor the working directory to their own location.

For daily commands from the generated root, replace `<ai_work>` with your `directories.ai_work` value before running:

```sh
python3 -I -S -B "<ai_work>/tools/workspace_manager.py" validate
python3 -I -S -B "<ai_work>/tools/workspace_manager.py" refresh
python3 -I -S -B "<ai_work>/tools/workspace_manager.py" refresh --apply
```

Here `<ai_work>` means `directories.ai_work`. On Windows PowerShell replace `python3` with `& 'C:\Path\To\python.exe'` for the approved installed executable; the rest of the flags/arguments are the same. No PATH or interpreter installation changes are automatic.

## 9. Copilot integration

### 9.1 Supported customization profile

Target the latest stable VS Code and GitHub Copilot extension in the developer's Local configuration. Ask, Plan, and Agent are interaction modes in that configuration; selecting Agent must not be treated as authorization to switch execution environments. Do not require Agent Host, a different harness, a background/cloud agent, or another extension. Selecting a Claude model within Copilot does not by itself select the separate Claude harness.

Document Ask for questions, Plan for planning, and Agent for authorized tool-assisted execution. Do not assume identical skill or tool availability in all three modes. Record actual VS Code and extension versions, the displayed Local configuration/harness, interaction mode, and policy restrictions in smoke-test results. Test the Local-specific customization behavior rather than assuming newer harness documentation applies. Do not hardcode a minimum VS Code version without testing it.

The official documentation consulted for this design describes `.github/skills` project skills, slash invocation, progressive resource loading, matching skill/directory names, and `disable-model-invocation` for explicit invocation. User and workspace support depends on harness. Duplicate skill names across roots can be ambiguous. [S2]

All skills created by this framework or for its maintenance MUST use the `ca-` (Code-AI) prefix in their folder names, frontmatter names and invocation examples. Preserve this rule for future skills. The release builder rejects unprefixed packaged skill paths, and strict validation checks the prefix. This namespace does not apply to unrelated third-party or repository-owned skills inspected by audit.

Use only the project skill locations shown in this design. Do not install user/global customizations. Keep frontmatter minimal:

```yaml
---
name: ca-jira-ticket-init
description: Create a local Jira ticket folder and selected supporting files from a supplied ticket ID.
disable-model-invocation: true
---
```

Use the same explicit-invocation setting for `ca-jira-ticket-archive`, `ca-jira-ticket-restore`, `ca-change-review`, `ca-config-audit` and `ca-workspace-refresh`. No experimental forked context, hooks, custom agents, additional discovery settings, or plugin installation is needed. These are workflow choices, not security enforcement.

### 9.2 Repository instructions and shared context

Company repositories remain authoritative for their own conventions and tests. Setup MUST NOT write into a cloned repository. Put a concise example `.github/copilot-instructions.md` in `WORKSPACE_SETUP/payload/examples`, with documentation for a developer to propose it through normal repository review later.

The example should describe repository purpose, approved build/test commands, preserved behavior, and where to find relevant shared documentation. Do not embed absolute paths or another developer's configurable sibling directory names in a company-committed file. Prefer repository-local references; developers attach external project context explicitly when needed.

Generate a concise orientation at `<ai_work>/.github/copilot-instructions.md`, plus `<ai_work>/COPILOT_GUIDE.md` for human onboarding. The orientation itself is the project instruction file, not an extra indirection through a second bootstrap file. It points to the overview/reference map, explicitly selected active ticket brief, knowledge, three repository groups and daily commands. It asks the agent to consult relevant project context, reuse current chat context, surface incomplete templates and read detailed sources on demand; never ingest unrelated tickets/attachments or invent architecture/evidence.

Render paths and labels from the effective configuration. Orientation links resolve from its .github directory; use URL-encoded relative links to support spaces and relocation. Deploy the orientation as user-owned and the guide as generated documentation. Refresh must not overwrite orientation edits. Validation/audit check presence, ownership and local resources, and explicitly distinguish these checks from Copilot discovery.

This file is intended for automatic loading where the selected Local/Copilot environment discovers project instructions and loading is enabled. Do not claim always-on inheritance across this non-Git multi-root layout without manual evidence. The guide must cover Chat: Open Customizations, fresh-chat References/debug evidence and relevant-file reading/answer correctness for MAIN/OTHER/DOCS roots and available Ask/Plan/Agent modes, repeated with custom names and relocation. It must explain that instruction support is environment-dependent and does not govern inline suggestions. [S3] The orientation is additive; do not assume it overrides repository/company guidance or establishes tool authorization.

The guide must remain usable without the installer. It explains how to populate the overview/reference map and select a ticket, verify orientation and skills separately, and use explicit attachments/direct commands when loading is absent. Document the Local instruction-file discovery setting for manual inspection, but do not change settings, create global instructions, initialize an outer repository or modify company clones automatically. Discovery checks remain manual release evidence, not a new initialization prerequisite. Official instruction documentation was rechecked on 24 October 2026 for this addition.

### 9.3 Discovery verification and fallback

Where local skills are permitted, multi-root discovery/inclusion of the orientation and skills in this exact non-Git AI working directory MUST still be tested in the Local configuration on the versions actually used. Run this experiment early in the macOS pilot, before relying on the skill architecture. Documentation of supported locations is not proof that the actual installation loads them.

If the orientation or skills are absent or prohibited by policy:

1. Report the condition plainly.
2. Keep all CLI operations and Markdown guides usable.
3. Offer the documented manual alternative: attach the orientation and relevant overview/reference-map/ticket files, run the ticket tool directly, or attach the review procedure/checklist as chat context.
4. Do not silently move skills to a global folder, change settings, initialize Git as a workaround, or install a plugin.

Use the available customization diagnostics/References UI for evidence of loading; asking the model to repeat a keyword alone is not adequate proof. Record blocked features separately from structurally valid installation. [S4]

## 10. Ticket workflow and command contracts

### 10.1 Ticket identity and location

Accept uppercase IDs matching `[A-Z][A-Z0-9]{0,19}-[1-9][0-9]{0,9}`. Reject invalid IDs with an example rather than silently rewriting them. More permissive company-specific patterns can be a later schema change.

```text
<ai_work>/tickets/active/ABC-1234/
|-- brief.md
|-- plan.md       # Only when selected
|-- review.md     # Only when selected
|-- notes.md      # Only when selected
`-- files/        # Only when selected
```

The create command validates active and archive paths and refuses redirected paths. If the ID is archived, it must request explicit restore through the documented command rather than creating a second active copy. If both locations exist, report conflict and change neither.

For an existing active ticket, retain every existing file; create only explicitly requested missing placeholders and a missing required brief. Treat an existing file at a required directory path or directory at a required file path as a conflict. Report `created`, `already present`, and `conflict` distinctly. Repeated identical creation is safe. Never regenerate or append boilerplate into populated files.

No default repository inspection, baseline discovery, Jira access, or AI content generation takes place during deterministic ticket creation. New text uses clearly empty fields or `Not yet recorded`, never invented requirements, dates, hashes, evidence, or approvals.

### 10.2 Minimum template contents

`brief.md`:

- Ticket ID and optional Jira link entered by the developer.
- Goal, source of requirements, and acceptance criteria.
- Scope, non-goals, and existing behavior to preserve.
- Affected repositories and baseline evidence table.
- Open questions and short current-status/next-step note.

Baseline table fields: repository ID, branch (if relevant), full verified starting SHA, whether the working tree was clean at capture, and how any pre-existing/untracked changes were handled. All start unrecorded. Include a brief reminder that a SHA alone does not preserve uncommitted changes.

`plan.md`: approach, dependencies/interfaces, meaningful tests, risks/open decisions, and approval record only if explicitly provided. No automatic approval language.

`review.md`: reviewed scope/baselines, findings with evidence/severity, checks actually executed, unresolved risks and pending manual checks. Distinguish static inspection from execution.

`notes.md`: freeform investigation notes and attachment references.

Keep each initial template short; roughly 20–60 lines is a target, not a reason to omit required fields. Optional files are created only when requested. Relative links within ticket folders use paths such as `files/sample.csv` so moving the entire folder preserves them.

### 10.3 Skill behavior

`/ca-jira-ticket-init ABC-1234` creates the default brief via its local script. Optional arguments such as `--with plan,review,files` select other resources. If no optional choice is supplied, create only the brief; do not stop to ask a question. Natural-language requests can be translated into these explicit options.

Task details supplied with the invocation are captured verbatim using `--description TEXT`. For example, `/ca-jira-ticket-init A-111 - implement a hello world application using python` supplies the description after the separator. New briefs place it in the goal/source section, labelled as user-supplied initial details. Do not infer acceptance criteria, repository choices or baselines. With no details, the original unrecorded template behavior remains. The brief template supports `{{initial_description}}`; if a custom template lacks that field, append a labelled supplied-details section without rewriting its contents. Validate template fields before inserting user text so literal braces, quotes and multiline content remain data.

Existing brief files are never overwritten or appended to during initialization. If details are supplied but a brief exists, return `description_status: preserved-existing-brief` and explain that the details were not applied. Further refinement is a separate user-requested update. `--description` is valid only for create.

The skill MUST display or summarize the operation, invoke the script using the permitted terminal flow, and report the actual result. It MUST NOT edit repositories, bypass a command approval, fetch Jira, or manually emulate file creation after the script refuses a conflict.

The developer can perform the identical operation using the direct CLI. Supporting spreadsheets/images are stored as attachments; no plugin is needed to keep them in a folder. An agent may analyze supported attachments later under separate authorization and approved tooling.

The standalone ticket script accepts `create ID [--description TEXT] [--with ...]`, `archive ID`, and `restore ID`, with the same behavior and exit codes as the workspace wrapper. For example, from the AI working directory on macOS:

```sh
python3 -I -S -B .github/skills/ca-jira-ticket-init/scripts/ticket.py create ABC-1234 --with plan,files
```

On Windows, use the documented `py -3 -I -S -B` prefix with the same arguments. The script derives locations from its own file path, so its correctness must not depend on the current working directory.

### 10.4 Archive and restore

The explicit `/ca-jira-ticket-archive ID` and `/ca-jira-ticket-restore ID` skills invoke the shared helper in the sibling ca-jira-ticket-init skill using an absolute path resolved from their own location. They do not duplicate movement code, infer completion, update Jira/Git, or emulate writes after a refusal. They report the actual move/no-op result. These wrappers require their own discovery/resource-loading checks even when direct CLI operations were previously tested.

`ticket archive ID` moves the entire active folder to the flat archive, with no content rewriting. It requires a real source and absent destination. `ticket restore ID` performs the reverse. Refuse collisions; never merge or overwrite.

Use a no-overwrite move strategy, with exclusive destination reservation and explicit recovery on partial failure if necessary; ordinary replace/rename operations that can replace an existing destination are insufficient. Tickets and their descendants must be ordinary files/directories, with no symlinks/junctions; reject before mutation. If safe no-overwrite movement cannot be guaranteed, fail rather than use an unsafe fallback. Do not delete either copy after a failed/partial move without verified completion and clearly reported ownership.

Archiving is an explicit developer action; the framework does not infer Jira resolution. Already archived/restored tickets return an informative no-op if the opposite location is absent. Links to a ticket from outside its folder may need manual updating; only internal relative links are guaranteed to survive.

### 10.5 Normal development and regression safety

For small changes: brief as useful, edit, test, inspect diff, commit through normal processes. For larger changes: establish per-repository baselines, agree the approach, implement/test, then review requirements and cumulative changes in a fresh chat if useful.

Git history is the default source of original tracked content. Avoid copying entire original SQL files just for later comparison. A baseline SHA must be verified per repository. Commit-subject searches are hints, not proof of the ticket's first change. Interleaved changes, renames, merges, rebases, squashes, untracked files, and existing uncommitted work require explicit handling.

The review workflow reads the brief, relevant plan and repository rules; identifies the actual comparison scope; inspects staged/unstaged/untracked and committed changes as relevant; and prioritizes behavioral regressions, missed requirements, interfaces, and evidence. No automatic checkout, reset, stash, commit, or source modification. It may propose tests; running them requires the normal authorized tool flow because tests can write files or access services.

Use representative before/after outputs, application tests, SQL validation, and infrastructure plan evidence where approved and relevant. The framework does not automatically apply infrastructure changes, run production SQL or deployment scripts, or authenticate to services.

## 11. Project context, company references, and knowledge base

`project/overview.md` begins as a clearly incomplete template with project purpose, repository map, interfaces/data flow, and known dependencies. It MUST NOT fabricate actual architecture. Developers fill it from verified sources when needed.

`project/reference-map.md` is a small index: topic, authoritative source path/link, owning team if known, and last checked date. It is not a copied policy manual. Official company docs stay in their own repositories; cite them and note uncertainty when local clones may be stale.

Knowledge articles are organized by topic. Simple notes are Markdown files; articles with assets use `topic/guide.md` and `topic/assets/`. Suggested fields: purpose, prerequisites, procedure, caveats, source links, last verified date. The sample SVG must be static and synthetic, with no script, remote resources, or confidential data.

Ticket-specific notes remain in the ticket. Extract reusable learning into a guide when it has future value and permitted information classification. The official source remains authoritative for company rules. Keep ticket history, personal guidance, and company policy distinguishable.

Do not automatically index/attach all notes or reference repositories to a prompt. The user selects context or the agent reads relevant material on demand. Workspace availability does not mean all files are prompt-attached; indexing and search behavior also need consideration. [S5]

## 12. Validation and configuration audit

### 12.1 Deterministic validation

`validate` checks the effective configuration and installed structure. It does not repair files or execute project code. It should check:

- Root/layout safety, required directories, state completeness, supported schema.
- Required file presence, valid JSON, source package integrity, and unresolved placeholders.
- Parse workspace JSONC safely and compare folders to the generated relative inventory. Report manual/missing root differences as warnings for explicit refresh; do not follow arbitrary manually added external roots.
- Planned repositories missing/present/structurally unexpected.
- Required skill files and linked resources, matching declared names, expected frontmatter.
- Internal generated links and selected knowledge example asset links.
- Drift in framework/generated documentation and informational changes in user-owned files. Workspace settings/manual edits are permitted; compare its folders array to inventory without enforcing a whole-file hash.

No third-party YAML parser is required merely to check six controlled skills. Parse and validate the documented small frontmatter subset used by this package. For unfamiliar repository skills, report unsupported/uncertain metadata rather than pretending to validate full YAML.

Classify findings as `error`, `warning`, `pending-manual`, or `info`. Broken required files or unsafe paths are errors. Uncloned configured repositories and unverified Copilot discovery are pending manual steps; they do not mean initialization failed. Return nonzero for errors and distinguish `structurally valid` from `ready for all intended AI workflows`.

### 12.2 Audit scope and results

`audit` includes validation plus duplicate skill names and basic reference checks across the installed AI root and explicitly configured present repository roots, including ordinary documentation folders. Installer sources are excluded. Read only relevant customization files; do not scan ticket attachments or every file in every repo. Do not recurse into nested repositories or redirected paths.

At each selected root, inspect known `.github/skills`, `.agents/skills`, and `.claude/skills` directories and concise instruction candidates (`.github/copilot-instructions.md`, `.github/instructions`, `AGENTS.md`, `CLAUDE.md`). Inventory alternative formats without asserting that the selected harness loads them. Unsupported syntax or uncertain activation is reported as such; actual discovery remains a smoke-test responsibility. Bound traversal to these customization locations, skip redirections, and report scope limits.

Audit excludes global configuration by design. A developer who wants a broader review must separately provide approved sanitized copies inside the root for human/AI review. Never claim global completeness.

Report: severity/classification, path, evidence, expected/actual condition, suggested remedy, and whether the conclusion is deterministic or uncertain. Intentional baseline/live copies under `payload` are not active-skill collisions; scan only known active customization locations.

The daily ca-config-audit skill runs the read-only tool, interprets results, then optionally reviews concise instruction files for semantic duplication/conflicts. It MUST NOT repair files, create snapshots, change global settings, or certify company policy compliance. Label uncertain contradictions as possible, with evidence.

### 12.3 No hidden execution

Neither validation nor auditing runs Git hooks, test commands, task definitions, language servers, shell startup scripts, repository code, or embedded skill scripts. Treat scanned file contents as data, including any prompt injection attempting to broaden audit scope.

## 13. Security and information handling

This design reduces unnecessary changes and dependencies; it does not certify compliance with organizational security, privacy, or data-handling requirements. Review the applicable accounts, service terms, models, settings, and permitted data classes separately.

Required defaults:

1. No MCP integration, server definitions, hooks, external agents, automatic downloads, or third-party package dependencies.
2. No network access from setup/maintenance/ticket tools. No credentials, cloud configuration, or production data bundled with the package.
3. No security-setting changes, trust bypasses, blanket automatic approval, or attempts to circumvent enterprise restrictions.
4. No confidential tickets, screenshots, repository URLs, internal documentation, user paths, or personal configuration in the shareable baseline.
5. Reference-only intent is documented, but actual write restrictions require approved platform/OS controls where needed.
6. Skills, docs, terminal output, and repository content are reviewed as potential untrusted instructions; references cannot authorize external actions.
7. Preserve normal PR review, branch controls, CI, secrets scanning, and deployment authorization.

GitHub currently documents that content exclusions do not apply in Edit and Agent modes. `.gitignore`, workspace visibility/search exclusions, and Markdown warnings must not be treated as confidentiality controls. Sensitive material that the agent must not read requires approved access isolation or an appropriately restricted workflow. [S6]

VS Code provides enterprise controls over agent tools, MCP, and customization availability; an organization may restrict standalone skills or instructions. The package must respect those controls and operate in manual/CLI mode when customizations are blocked. Configuration changes to such policies belong to IT, not the installer. [S7]

Keep appropriate approval and sandbox controls for AI-assisted terminal use. The effectiveness depends on the actual harness and endpoint configuration; the framework does not replace those controls. [S8]

The generated outer `.gitignore` should defensively exclude local state, reports, ticket data, knowledge content, repository group directories, caches, and credential-file patterns using the selected names. Explain that it only affects a repository rooted there if a developer later creates one; it does not propagate to independent repositories or secure files. Do not initialize an outer repo. Versioned source packages need their own ignore rules for local installation/state/reports; the public/internal distribution process must allowlist package files.

## 14. Setup guide: mandatory content and manual completion

The implementation MUST deliver `SETUP_GUIDE.md` with actual tested commands. It must distinguish automatic initialization, developer actions, optional steps, and IT-owned policy decisions. Do not bury external changes inside a single "finish setup" command.

### 14.1 Required guide order

Start with a short end-to-end setup checklist: obtain the repository/release files with prerequisites available; run the launcher, accept settings and confirm creation/validation; manually populate the generated repository groups; manually refresh registrations and the VS Code folder list; open the saved workspace; prepare Copilot and verified overview/reference-map context; check instruction loading and a small ticket/audit workflow; continue to daily work. Direct users to the actual guides in their generated AI Work folder and name the required sections; do not route setup through unrendered payload templates with installed-relative links. Editing the generated orientation is optional. Basic onboarding checks one intended root/mode and verifies a documented fallback where features are unavailable; the full maintainer platform/root/mode matrix remains separate. Settings changes require editing the named JSON and relaunching. Prerequisites, optional follow-up and conditional troubleshooting follow as focused reference sections.

Maintain two intentionally different landing pages. The repository README explains the product and links to user setup plus maintenance/contributor material. The user installation README is canonical at WORKSPACE_SETUP/README.md and covers prerequisites, quick setup, generated layout, portability, help and current known limitations. Emit that user document once at the ZIP root, relocating its package-relative links while preserving external URLs and same-document anchors. It must not link or refer to absent maintenance files. Keep detailed user operations in SETUP_GUIDE.md and generated daily guides; keep maintainer commands and full history in maintenance/.

Provide precise settings fields, approved-package integrity checks, direct-command alternatives, refusal/error handling and manual external actions below the quick start. Generated user guides must be self-contained for daily folder usage, repository inventory/refresh, validation, tickets, local skill discovery/fallback, backup/recovery and safe removal. They must never require an installer guide that users may delete.

### 14.2 Manual-action table

The guide must provide purpose, exact steps/commands or a link to the approved internal procedure, expected scope of changes, verification, and whether each item is required. An internal policy URL not yet supplied must be explicitly marked for the maintainer to fill before organizational release.

| Manual action | When needed | What to explain |
|---|---|---|
| Install approved Python, Git, VS Code and Copilot | Missing prerequisite | Company software channel; no automatic download/install |
| Sign into corporate Git/Copilot | Access not configured | Approved account/auth flow; credentials never copied into package |
| Resolve endpoint/proxy/certificate restrictions | Environment requires it | IT procedure; setup never modifies trust stores/network configuration |
| Clone company repos into configured locations | To work with source/reference material | Approved URLs and explicit destinations; Git/auth may write outside root |
| Run workspace refresh | After clones/inventory edits | Preview and explicit update of local workspace files |
| Open generated workspace and review trust prompt | To start VS Code work | Trust only reviewed material; IDE may create its own external state |
| Verify selected harness and skill discovery | To enable AI workflows | Diagnostics, slash menu and direct-command fallback |
| Change a required user-level setting | Only if company-approved and actually necessary | Exact setting, reason, prior value, scope and manual rollback |
| Configure backup/private repository | To protect work from machine loss | Approved storage, covered data classes, no public remotes |
| Add repo-local instructions | Optional team adoption | Normal reviewed change in owning repo |

Global Copilot customization is not a prerequisite and is not part of the normal installation path. Do not tell users to create `~/.copilot` merely to use this framework. If an approved harness requires a manual setting, describe it conditionally and verify it; never use generic instructions to disable protection.

### 14.3 Repository population example

The guide may show an illustrative `git clone <approved-url> <configured-path>` command, explicitly identified as a manual developer command. Explain that it may invoke credential helpers or update Git/SSH state outside the root. Do not execute it from setup or a post-install hook. Do not copy/move the developer's existing working trees automatically.

If a developer already has repositories elsewhere, they may continue using them separately. Initialization creates a new contained tree; attaching external paths, symlinking repositories, or merging the framework into an existing development tree is outside its automatic contract.

### 14.4 Troubleshooting minimum

Cover existing target refusal, missing parent/interpreter, invalid names/collisions, denied permissions, path length, incomplete initialization, missing repositories, workspace drift, skills not discovered, policy-blocked customizations, and an unavailable approved model. Each remedy is local/manual and preserves security controls.

## 15. Daily use and context efficiency

The root README should stay concise and link to the AI working DAILY_WORK.md. It must be sufficient for daily use without any installer guide. A developer should be able to find these five actions immediately:

1. Open the daily workspace.
2. Create/open a ticket.
3. Find project/knowledge/reference information.
4. Review/test changes using existing repository tools.
5. Archive a ticket or run a local audit.

Give each generated guide one primary job: the root README covers getting started, repository refresh and recovery; the AI working DAILY_WORK.md covers tickets and daily commands; COPILOT_GUIDE.md covers context preparation, loading checks and fallback. Put the common task first, use short action headings and link to the other guide instead of repeating it. Keep essential preservation/cancellation/recovery rules, but leave implementation details in the design and less common CLI options in subcommand help. These guides must remain self-contained without the installer.

The main DAILY_WORK.md workflow uses Copilot skills and prepared refresh launchers. Keep manual Python invocations together in an optional reference at the bottom, collapsed where Markdown rendering supports it. Direct commands remain available for users without Copilot, troubleshooting and other editors; they are not a required daily step.

Do not require a chat per phase, a plan for every change, an approval record for trivial edits, or a custom agent selection. Use a fresh review chat for complex/high-risk work when independent context is useful. AI is optional; its output remains subject to developer judgment and actual tests.

Persistent repository guidance should remain concise. Keep architecture, ticket history and checklists in on-demand files. The comprehensive design and package templates stay outside daily roots. Keep the current six skills focused; build specialist skills only after repeated use justifies them.

No model, vendor, effort level, or context-window size is required to install or operate the CLI. The guide can recommend a company-approved general coding model for routine assistance and a stronger approved model for difficult design/review, but must not prescribe stale model names, unverified context controls, or an expensive model for copying files.

Measure practical usefulness with simple edits, cross-repository work, and regression reviews. Compare time, tool calls, unnecessary files, retries, context usage when available, and meaningful defects. Do not promise zero token overhead or pretend workspace indexing means all contents enter every prompt.

## 16. Backup, recovery, and removal

### 16.1 Separate the three recoverable things

| Material | Recovery method | Who configures it |
|---|---|---|
| Reviewed framework release | Approved package repository/archive and release manifest | Maintainer/developer manually |
| Local configuration and edited skills/project docs | Approved private backup or private Git/storage | Developer manually |
| Tickets, knowledge assets, source work and unpublished changes | Appropriate approved data/source backups | Developer/company systems |

Each user selects and manually configures their backup destination. Recommend cloud backup with recoverable history where permitted, without selecting a mandatory vendor or introducing a backup integration. For restricted information, follow the applicable storage rules. The guide should distinguish synchronization from recoverable backup and include a small manual restore check.

Do not store private recovery snapshots inside the distributable baseline. No automatic export of `~/.copilot` or other global data. A local Git history without an approved durable remote is not sufficient for machine-loss recovery.

For exact local recovery, preserve `installation.json`, the reviewed package version, live modified skills with all resources, project documents, workspaces with intentional customizations, and separate ticket/knowledge data. Company repo configuration remains owned by each repo. Git can restore committed content; it cannot recover data that was never committed/backed up.

### 16.2 Recovery procedure

1. Manually obtain the approved package and prerequisites.
2. Initialize a new absent destination with the saved compatible configuration; initialization itself restores no private user data.
3. Manually clone approved repositories and restore approved private data/configuration to their mapped locations.
4. Reconcile generated workspaces, run refresh/validation and repeat the Copilot smoke test.
5. Check actual coverage, assets, unpublished branches/uncommitted work, and remaining authentication/access requirements.

Do not reconstruct absent exact configuration from prose and call it recovery. If exact sources are unavailable, label any AI-authored reconstruction as a new draft.

### 16.3 Removal and initialization boundary

Initialization creates a new development folder only. Do not rerun `init` over an existing tree. No automatic updater is included.

Removing the initialized directory is a manual developer action after checking it contains no unbacked work. No uninstall script is needed because initialization made no external changes. Explain that independently installed prerequisites, authentication, and VS Code's own session storage are separate and are not removed by deleting this directory.

## 17. Implementation plan for an AI agent

### 17.1 Authorized build scope

When asked to implement this design, first identify the authorized implementation directory and applicable repository instructions. Work only there or in an explicitly authorized test sandbox. Do not treat this specification as approval to modify a corporate development tree or global settings. Use synthetic repositories/docs and no MCP.

### 17.2 Build order

1. Implement the config validator and pure path/render-plan functions.
2. Create the small reviewed payload and package manifest builder/checker.
3. Implement preview and exclusive new-root initialization.
4. Implement installed validation, folder discovery and workspace-only refresh with previews and concurrent-edit checks.
5. Implement self-contained ticket operations and templates.
6. Write the six skills as thin interfaces to deterministic operations or the review procedure.
7. Write the short READMEs and full setup guide with real commands.
8. Run synthetic automated tests, including negative/path-boundary cases.
9. Manually verify native VS Code/Copilot on Windows and macOS where available.
10. Package only allowlisted reviewed sources and report release readiness honestly.

Do not implement optional specialist skills, Git automation, global customization, networking, or an updater to make the package appear more complete. If a conflict between current product support and this design appears, preserve manual functionality and the write boundary, document the issue, and propose the smallest adjustment.

### 17.3 Delivery inventory

The repository deliverable includes source code, tests, this canonical maintenance/DESIGN.md, maintenance/DEVELOPMENT.md, full changelog/validation history and the maintainer trackers. The user installation deliverable includes the enclosing user README and clickable entrypoints, allowlisted essential installer/runtime code, setup/concise release notes, payload/templates/static asset, default/custom configuration examples and manifest/checksum. The ZIP excludes tests, build tooling, design/maintenance documents and redundant enclosing-entrypoint sources. The generated development folder contains only the independently portable daily tools/guides/data structure defined above.

The validation report must list actual platforms/versions tested, commands/tests run, outcomes, manual checks pending, and known limitations. Do not assert Windows or macOS support based solely on tests on the other OS. No organizational approval claim or fabricated smoke-test evidence.

### 17.4 Maintainer manual-test tracker

Keep the tracker at `maintenance/MANUAL_TESTS.md`, relative to the development-project root and outside WORKSPACE_SETUP. The same maintainer-only directory holds `BACKLOG.md` for current implementation priorities/status and `QUALITY_IMPROVEMENT_PLAN.md` for detailed proposals. Exclude the directory from the release inventory and generated workspaces. Track stable test IDs, priority, macOS/Windows status and explicit evidence with version/environment/mode. Record informal user reports separately from verified passes; automated tests do not close manual GUI/Copilot checks. Include orientation discovery across roots/modes and relocation, skill loading, native launchers, refresh behavior, actual VS Code use and recovery. Preserve evidence across releases and consult the tracker when the user asks what remains to test.

## 18. Acceptance tests and release gates

### 18.1 Automated tests

Use Python `unittest` or equivalent standard-library tests. Fixtures, test temporary directories, bytecode, and reports must remain inside an authorized test sandbox. Verify behavior rather than only reproducing rendering internals.

| ID | Scenario | Required result |
|---|---|---|
| INIT-01 | Default configuration, absent target | Required tree/files generated; correct ownership/hashes; complete state |
| INIT-02 | Rename all five directories and root, including spaces | Workspaces, links, skill commands and validation follow mapping |
| INIT-03 | Existing empty/nonempty directory, file, dangling link | Refuse before mutation; existing contents unchanged |
| INIT-04 | Missing parent, root/home replacement or unsafe path | Refuse; no ancestors/target created |
| CLICK-01 | Clickable setup with y/yes | Settings first, separate preview/creation confirmation, validate, retain terminal output |
| CLICK-02 | Blank, no, EOF, invalid answer, existing target or validation error | No unintended creation or false success; initial settings rejection exits, later outcomes retain visible diagnostics |
| CLICK-03 | Default target inside the source package directory | Create only Code-AI; source files unchanged; no recursive self-copy |
| PY-39 | Native Python 3.9 and newer interpreter | Required workflows/tests pass without new dependencies |
| INIT-05 | Case collisions, reserved names, separators, traversal | Reject before writes |
| INIT-06 | Invalid JSON/schema/duplicate keys/unknown placeholders/hash | Reject before creating target |
| INIT-07 | Two initializers race for target | Only one creates it; the other refuses without touching it |
| INIT-08 | Simulated disk/permission failure after root creation | Incomplete state retained; no completion claim; rerun refuses |
| BOUND-01 | Source package outside target | Source bytes/mtime unchanged; no caches created there |
| BOUND-02 | Instrument all program write/delete/rename/process/network entry points | No write outside target; no process/network calls |
| BOUND-03 | Symlink/junction output or redirected ancestry | Refuse; external sentinel unchanged |
| BOUND-04 | Read-only preview/validate/audit/refresh | No program-directed writes; no hidden report/log/cache |
| WS-01 | Planned repositories absent at initialization | No repo slots created; pending items; no missing workspace roots |
| WS-02 | Manually create mock repo markers, refresh | Separate selected roots, relative paths, setup excluded |
| WS-03 | Unselected refs and overlapping roots | Unselected roots absent; overlap configuration rejected |
| WS-04 | User-edited workspace settings/JSONC and roots | Preview replaces only folders; unrelated bytes preserved; concurrent edits refused |
| TKT-01 | Default ticket creation | Only folder/brief; no invented requirements or baseline |
| TKT-02 | Optional files and identical repeat | Only selected missing resources created; existing bytes preserved |
| TKT-03 | Invalid ID, active/archive collision or redirected path | Refuse safely; no duplicate/overwrite |
| TKT-04 | Archive and restore with binary/text attachments | Every byte and internal relative link preserved |
| TKT-05 | Move failure/concurrent destination | No overwrite or loss; explicit recovery diagnostic |
| AUD-01 | Missing template, broken generated link, duplicate active skill | Evidence-based deterministic findings |
| AUD-02 | User edits overview/installed skill | Informational baseline change, no automatic repair |
| AUD-03 | Report path outside reports or already present | Refuse; existing data unchanged |
| REC-01 | Fresh root from same release/config plus synthetic manual restore | Equivalent configuration/data coverage, no LLM reconstruction |
| PORT-01 | Unicode enclosing parent, spaces and native line endings | Correct portable output/links or explicit OS constraint |

Test the boundary through instrumented I/O and before/after sentinels around source, home/global-config fixtures, and sibling directories. A sentinel alone does not prove all possible external writes are impossible; review imports and all I/O paths too. Real antivirus/OS activity is outside the program test scope.

### 18.2 Manual VS Code/Copilot smoke test on each supported OS

Run testing in two stages:

- **Stage A — macOS pilot:** Test the package and daily workflow using synthetic repositories, notes, tickets, and attachments. Record Local skill discovery and practical usefulness; no private project data or access is required.
- **Stage B — Windows 11 validation:** Test native paths, Python invocation, Local-mode skill discovery, and applicable policy restrictions on Windows 11. Successful macOS tests do not establish Windows support or organizational approval.

A macOS pilot may be published while Windows testing is pending. State untested platforms and policy configurations explicitly; do not describe a single-platform pilot as fully validated across both platforms.

1. Record native OS, Python, exact latest stable VS Code and Copilot extension versions used, Local configuration/harness, account policy restrictions, package version, and date; no secrets in reports. Check Ask, Plan, and Agent behavior without requiring a different execution environment.
2. Run preview/init from a reviewed local package; verify no software/configuration changes were requested.
3. Open the generated daily workspace manually. Check separate root display and independent repo source-control behavior using mock repositories created manually for the test.
4. Verify orientation discovery/inclusion from each MAIN/OTHER/DOCS root in fresh Local chats and available Ask/Plan/Agent modes. Inspect References/debug evidence and context reads/answer correctness, then repeat with renamed folders and after relocation. Verify all six skills and their resources separately; exercise explicit-attachment/direct CLI fallback. Test refresh with the target workspace open, including first-root changes and interruption recovery through the launcher. Record results in the maintainer tracker without shipping it.
5. Create a mock ticket, select optional files, archive and restore an attachment.
6. Verify the daily AI root exposes all six skills, run read-only audit, and check that no installer material is needed. Remove/move the extracted installer and repeat direct daily commands.
7. Make a trivial manual edit and an AI-assisted mock change. Confirm ordinary tests/review remain usable and no mandatory documentation ceremony appears.
8. Review a synthetic regression from a saved per-repo baseline; check findings against executable evidence.
9. Confirm no global customization installation or protection bypass was needed. If policy blocks skills, record degraded/manual support rather than bypassing it.

If either OS or the required harness is unavailable, mark that release gate **not tested**. The package can be delivered as a POC; it must not be labelled fully validated for both platforms.

### 18.3 Release checklist

- [ ] New-directory-only behavior and no external changes hold for every automatic command.
- [ ] All meaningful negative/path/conflict tests pass.
- [ ] Default and fully renamed installations work.
- [ ] Daily operation works without Copilot.
- [ ] Skills work on tested approved versions, or limitations and fallbacks are explicit.
- [ ] Windows 11 and macOS results are recorded separately.
- [ ] Setup guide clearly lists every external/manual action and its scope.
- [ ] Package contains no real corporate/private data, credentials or personal paths.
- [ ] Package release sources and hashes are complete, with all skill resources included.
- [ ] Read-only audit has honest scope and no implicit repairs.
- [ ] Backup/recovery and manual update/removal procedures are understandable.
- [ ] Required organizational approvals and internal procedures are identified before deployment in a managed environment.

## 19. Maintainer reference prompts

These prompts are repository-only implementation/reference material, not required content for the user installation guide. Keep user instructions focused on setup and daily use. Prompts complement deterministic commands and never replace actual execution evidence.

### 19.1 Build the package from this specification

> Implement the self-contained workspace described in maintenance/DESIGN.md inside the authorized project/test directories. Preserve its new-target-only and no-external-changes contract. Use Python standard library, deterministic commands, synthetic fixtures and no MCP. Build the required first release, documentation and acceptance tests. Do not install into real development folders, clone company repositories, change global configuration, authenticate, download dependencies or enable security settings. Report what was actually tested and any platform/Copilot checks still pending.

### 19.2 Help a developer prepare initialization

> Read README.md and SETUP_GUIDE.md. Help me choose an absent target path and the optional directory/repository configuration. Use the read-only plan command. Explain the generated files and manual completion steps. Do not initialize until I explicitly request execution. Do not change anything outside the chosen target or perform prerequisite installation, authentication, repository cloning, or global configuration changes.

### 19.3 Execute an already reviewed initialization

> Run the documented init command for the target and configuration I have explicitly approved, then run local validation. Refuse an existing target and stop on conflicts. Make no changes outside the new target. Report structural results and the manual steps I still need to perform; do not perform those steps automatically.

### 19.4 Start ordinary ticket work

> Read the attached ticket brief and applicable repository instructions. Identify missing requirements or baseline information that materially affects the task. Use the existing code, Git history and tests. Keep the process proportional to the change. Read shared context only when relevant; do not create optional documents unless useful. Preserve normal review and execution permissions.

### 19.5 Review a change independently

> Review the supplied ticket requirements and the full relevant change against its verified baseline in each affected repository. Identify functional regressions, missed requirements, interface problems and inadequate test evidence. Include untracked and uncommitted changes where relevant. Distinguish confirmed findings from uncertainty, and executed checks from static inspection. Do not modify source, switch Git state, run production/deployment commands, or change configuration.

### 19.6 Audit local framework configuration

> Use the ca-config-audit procedure and read-only CLI against this initialized root. Report structural errors, active skill-name collisions, broken resources, generated-file drift and possible instruction contradictions with evidence. Exclude global configuration and private attachments. Do not repair, snapshot, overwrite, or change settings. State the audit's scope and any discovery checks requiring the developer.

### 19.7 Mandatory lean-installation acceptance checks

Initialize default and renamed layouts in synthetic fixtures. Assert the full generated file inventory contains no installer folder, source manifest/payload/tests, setup launcher or maintenance workspace. Move/remove the extracted installer and run installed validation, audit, refresh preview/apply and ticket create/archive/restore in subprocesses with an approved interpreter; run the ticket script directly as well. Confirm all work from relocated trees and renamed AI paths.

Edit only `settings.json` without rebuilding a manifest: preview/init must use the changed valid settings; invalid schema must fail with no writes. Hash changes to immutable source assets must still fail. Verify setting summaries precede preview, first decline/EOF creates nothing and exits without retention, and second decline creates nothing and retains output. Verify frozen config and manifest/target races. Verify every ZIP member shares one versioned enclosing folder, extraction produces only that folder, its README links resolve, and its launchers stay beside WORKSPACE_SETUP. Verify Mac extraction permissions and real launcher behavior, while keeping native Windows and actual Local Copilot discovery as explicit manual gates.

### 19.8 Portable location and quit acceptance checks

Initialize with an absolute configured parent_directory, inspect every generated local link/workspace root/inventory for relative paths and verify no original absolute target/config/source path is persisted. Move and rename the fresh tree to another parent, remove the original parent and installer, then validate/audit/refresh and create a ticket from an unrelated working directory. Repeat with renamed major folders and synthetic asset links. Extra Git/tool-specific relocation checks belong to later manual integration.

Test default `.`, absolute and relative locations, --target precedence, missing/redirected parents, invalid path values and frozen settings. Test real launcher blank/unknown input retains output, q/quit exits, initial settings rejection skips the quit prompt, failure status remains visible, and no command text is executed. Native Windows and physical macOS GUI closure remain separate platform checks. Record the macOS profile limitation explicitly.

### 19.9 Naming schema and independence acceptance checks

Use configuration schema 1 with root_folder_name, parent_directory, directories.primary_repositories and the AI_WORK default. Confirm ide_configs/Code-AI.code-workspace exists when vscode_workspace_name is omitted. Independently customize the root, primary repository group and vscode_workspace_name, including spaces; verify menus, README links, refresh and expected file inventory follow the correct setting without cross-coupling. Reject invalid filename stems and post-initialization filename changes before writes. Reject unsupported schema versions, unknown keys and invalid repository groups before writes. Confirm all current new-target, path/drift, launcher, relocation and no-installer-runtime tests still pass.

## 20. Decision log and remaining verification

| Decision | Reason |
|---|---|
| One new target; refuse any existing destination | Predictable initialization and protection of existing work |
| All automatic writes stay inside target | Predictable scope; easy review/removal |
| Manual prerequisites/auth/clones/global changes | Prevent hidden effects outside the target |
| Standard-library Python and JSON | One implementation across native Windows/macOS, no package install |
| No automatic Git operations | Preserve credentials/configuration and repository independence |
| Disposable installer and independent daily runtime | Keep setup sources out of generated development workspaces |
| Separate knowledge base | Reusable guides have a different lifecycle from tickets |
| Selected individual reference repositories | Keep workspace search and customization scope deliberate |
| Small CLI-backed skill set | AI and manual workflows share deterministic behavior |
| No global customization dependency | Avoid effects on unrelated work and personal settings |
| Private data separate from distributable package | Reduce accidental disclosure and competing sources |
| No same-root install retry or automatic updater | Keep first release safe and understandable |

Target environment: Python 3.9+ and VS Code/Copilot in Local configuration, with optional local skills where permitted. Backup destinations are user-selected. Source and pilot releases may be published or shared directly, with macOS and Windows 11 validation recorded separately.

Remaining environment-specific verification is not permission to add machinery. Record the actual Python version, exact VS Code/Copilot versions and Local configuration, non-Git multi-root skill discovery, applicable device restrictions, allowed data classes, and any needed internal prerequisite/authentication procedures. Each user chooses their backup destination during manual completion; there is no central backup-location decision blocking implementation. Neither central hosting nor availability of a second test platform blocks a clearly labelled pilot release. None changes the initialization write boundary.

## 21. Official sources and verification limits

Consulted 16 October 2026. Product behavior can change; the implementing maintainer must check current official documentation and the installed versions permitted by applicable policy before publishing compatibility claims. These sources support platform facts, not approval of this custom framework.

- **[S1]** [VS Code multi-root workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces) — workspace structure, named roots and relative paths.
- **[S2]** [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) — supported project locations, frontmatter, invocation and resources.
- **[S3]** [VS Code custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) — harness-dependent formats, scope, additive guidance and inline-suggestion limitation.
- **[S4]** [Create and manage agent customizations](https://code.visualstudio.com/docs/agent-customization/overview) — customization management and discovery context.
- **[S5]** [How Copilot understands your workspace](https://code.visualstudio.com/docs/agents/reference/workspace-context) — workspace search/context and indexing.
- **[S6]** [GitHub Copilot content exclusion](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion) — exclusions and their limitations.
- **[S7]** [VS Code enterprise policies](https://code.visualstudio.com/docs/enterprise/policies) — centrally managed feature/tool/customization controls.
- **[S8]** [Secure AI-assisted development in VS Code](https://code.visualstudio.com/docs/agents/run/security) — approvals, execution boundaries and defense layers.

The framework is not implemented or smoke-tested by the act of authoring this document. An agent receiving only this file has sufficient requirements to build and test the package, and must provide actual evidence before reporting acceptance criteria as passed.
