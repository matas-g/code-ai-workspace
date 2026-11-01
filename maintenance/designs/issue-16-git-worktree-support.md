# Investigate and Design Support for Git worktrees

**Draft — proposed functionality, not implemented.**

- Owning issue: [#16](https://github.com/matas-g/code-ai-workspace/issues/16).
- Created: 1 November 2026, from the maintainer discussion.
- Purpose: preserve requirements, candidate approaches and open decisions before investigation starts. This is not an implementation-ready specification or a readiness decision.
- Ownership: GitHub owns status, priority and completion criteria. This document owns the detailed draft; [DESIGN.md](../DESIGN.md) remains the canonical product contract.
- Delivery: repository-only maintenance material; exclude it from installation ZIPs and generated workspaces. Do not duplicate the draft as an issue attachment.

## Problem and intended outcome

Users occasionally need a separate Git checkout for a Jira ticket while continuing to use their established project overview, reference mappings, knowledge, local ticket files and custom AI_WORK skills in VS Code with GitHub Copilot.

Two approaches were rejected as recommended usage: opening the original checkout and its worktree together in one VS Code workspace, because searches and agent context contain duplicate code; and initializing a complete new Code-AI tree per worktree, because that adds setup and lacks the user's accumulated context and skills.

Investigate a task-specific VS Code workspace containing the selected worktree and relevant original shared folders. Git retains the repository relationship; Code-AI supplies shared context and an explicit active-checkout identity. Creating the worktree does not itself implement a Jira integration.

## Requirements captured from the owner

### Layout and workspace contents

Consider an additional configurable directory, defaulting to `git_worktrees`, beside the existing repository groups. It is not another repository group and must stay outside normal registration/refresh scanning and the main workspace's roots.

The proposed single-repository task layout is:

```text
Code-AI/
├── MAIN_PROJECT/
│   └── app/                         # Original checkout
├── AI_WORK/                         # Existing context, tickets and user skills
├── KNOWLEDGE_BASE/                  # Existing shared knowledge
├── COMPANY_DOCS/                    # Existing documentation
├── ide_configs/
│   └── Code-AI.code-workspace       # Existing main workspace
└── git_worktrees/
    └── A-1111/
        ├── repo/                    # Actual linked Git worktree
        └── A-1111.code-workspace    # Task view, outside tracked repository content
```

These are illustrative defaults, not literal paths to encode in the skill. The task directory uses the Jira ticket ID, such as `A-1111`, rather than the full ticket summary. Derive shared folder paths from effective installed configuration and generate relative workspace paths from the task workspace file.

The task workspace contains the selected worktree, original AI_WORK and KNOWLEDGE_BASE, and relevant company documentation/supporting roots. It excludes the original checkout of the affected repository. Do not add the entire development root, which would expose both copies again. Decide how supporting roots are selected and whether documentation is included as a group or as selected registered folders.

### Interactive skill inputs

The proposed entry point is `ca-git-worktree-init`. It must work when invoked without a fully populated prompt; users should not need to remember argument names or order.

Ask explicitly for missing inputs together, retaining supplied values and making defaults visible:

| Input | Required behavior or design question |
|---|---|
| Repository | Select the relevant registered Git repository; never guess between multiple candidates. Determine a sensible confirmation flow when only one exists. |
| Source branch | Default to `main`, subject to explicit user selection. |
| Jira ticket ID | Identify the task directory and selected local ticket; do not infer requirements from the ID. |
| New-branch choice | Ask whether to create a named branch or reuse the source branch. An accepted blank answer, “same”, or an equivalent response means reuse. |
| Exact commit SHA | Optional override selecting the precise starting commit instead of the source branch's latest tip. |
| Remote | Identify and show the source remote; whether `origin` can be a default and when to ask remain design decisions. |

Missing invocation text is not an answer to an input question. Ask first; after that prompt, accept blank/“same” for branch reuse without generating a task branch. The branch-naming policy is unresolved below, not a required separate skill.

### Latest source versus an explicit commit

Without an explicit SHA, always attempt to retrieve/update the specified source branch from its selected remote and use the latest commit obtained by that successful update. Record the resolved full commit SHA. Do not silently create from an older local branch or stale remote-tracking ref after a failed update.

An explicit SHA takes precedence over the latest branch tip. Verify that it resolves to the requested commit, obtain missing objects if necessary through the selected remote, and report failure rather than silently substituting the tip. Decide whether source-branch membership is required for a supplied SHA and how abbreviated hashes are validated.

The owner described this as pulling the latest source branch. The design must specify Git mechanics that achieve that result in both creation and reuse modes. A literal pull integrates into the current branch; fetch plus a new branch at the fetched SHA may preserve the original checkout more directly. Existing local source branches may be behind, ahead or diverged. A successful pull/fast-forward check alone does not establish that a local branch with additional commits equals the fetched remote tip.

The successful checkout's baseline must equal the selected fetched or pinned commit. Do not reset existing history, merge, rebase or stash unrelated work merely to force that result. Determine the exact stop-and-explain flow when the requested combination cannot be satisfied. Record the remote, source branch and SHA used; do not claim that a previously fetched tip remains the remote's current tip indefinitely.

### Creating or reusing branches

An explicitly requested new branch is created from the selected baseline. Do not require every task to use a freshly invented branch.

When the user accepts blank/“same”, attempt to check out the existing local source branch in the new worktree. Git normally refuses a branch already checked out elsewhere. Report that conflict and obtain a different explicit choice; do not force the duplicate checkout, switch the original repository, invent a new branch, or silently select detached HEAD.

The investigation must resolve these cases:

| Case | Constraint to preserve |
|---|---|
| New name supplied and unused | Create from the exact selected baseline, following the chosen convention policy. |
| Reused local branch available and at selected baseline | Check out that branch without creating another. |
| Reused branch checked out elsewhere | Explain the conflict; no force or silent substitution. |
| Reused branch behind, ahead or diverged | Define permitted update behavior and refusal/choice flow while preserving the exact-baseline requirement and existing work. |
| Source branch exists only on the remote | Resolve explicitly: automatically creating a local tracking branch would conflict with the request not to create a branch. Guard against Git's implicit branch-creation behavior. |
| Explicit SHA differs from reused branch tip | Resolve the incompatible request; no silent reset, new branch or detached checkout. |
| Requested new name or task destination already exists | Define refusal versus explicit verified resume; never overwrite or force-reset it. |

Also decide upstream behavior for a newly created task branch; creating from a source remote branch must not accidentally establish an unintended push/pull target.

### Shared context, links and custom skills

Reuse the original shared folders in place. Do not copy a fresh overview, knowledge tree or skill collection into each task, and do not rewrite shared instructions for whichever task window was opened most recently.

Distinguish three path cases:

1. Relative Markdown links between shared files generally remain valid because those files have not moved. Moving the `.code-workspace` file does not rebase links inside an existing instruction file.
2. Links to the original `MAIN_PROJECT/app` can remain valid while referring to the wrong checkout for task edits. This is a semantic routing problem, not necessarily a broken-link problem.
3. User-added skills, shell snippets, absolute paths and terminal-working-directory assumptions need separate inspection. File-relative framework helpers are better placed to work unchanged, but the new IDE workflow is not yet verified.

Design a task-specific active-checkout mapping: ticket ID, logical repository ID, original repository location, active worktree location, branch, source remote/branch and verified baseline SHA. Decide whether it lives in task metadata, the selected ticket brief or both, how conflicting/stale values are detected, and how a new Copilot chat receives it. A metadata file's existence alone does not prove automatic loading.

Shared guidance should resolve code operations to the active checkout while retaining authoritative documentation links. The existing overview/reference map may describe a different branch's behavior; task conclusions still need verification against the selected checkout. Separate task windows can share context, but changes to those shared files are visible to all of them. Define shared versus task-specific note ownership and avoid concurrent editing of the same ticket.

Verify Copilot orientation inclusion, repository instructions and custom skill discovery in the task workspace. Preserve explicit attachment/direct-command fallbacks. Workspace visibility, instruction prose and reference labels are not filesystem permission boundaries.

## Optional branch-naming reuse: unresolved

No separate naming skill or dependency has been approved. First determine whether conventions recorded in the project overview or repository guidance are sufficient, and how contradictory conventions are resolved.

Compare these options during investigation:

| Option | Main question |
|---|---|
| Read the existing overview/repository convention | Is ordinary guidance sufficient without another skill or duplicated rule source? |
| Small naming skill | Would formatting, suggesting, validating and returning a name provide a useful reusable capability? How would a supplied name be handled? |
| Broader branch-creation skill | Should it also perform Git branch creation, and if so how are mutations, baseline selection, conflicts and worktree creation responsibilities separated? |

If a skill is justified, define its single purpose, the authoritative convention location, inputs/outputs, reuse mechanism and verification. Do not copy branch-naming formats into each consumer. The naming skill's own identifier and behavior remain undecided. A reuse-source-branch choice must not invoke branch-name generation or create a branch.

## Current implementation and integration boundaries

Inspection during the discussion found:

- [workspace_manager.py](../../WORKSPACE_SETUP/scripts/workspace_manager.py): `DEFAULTS`/configuration validation define the existing directory names. `GROUPS` and `registration_plan` scan immediate children of the three repository groups; `workspace_bytes` generates the main workspace. Worktrees have no explicit configuration or model today.
- The same runtime resolves the owning development root from the installed AI_WORK tools. Refresh updates the canonical main workspace; audit inspects AI_WORK and the registered repository inventory. Running these shared skills in a task window does not automatically make their scope task-specific. Decide whether to retain and explain parent scope or add explicitly selected task scope.
- [Orientation](../../WORKSPACE_SETUP/payload/root/copilot-instructions.md) links the original repository groups. [Overview](../../WORKSPACE_SETUP/payload/project/overview.md) and [reference map](../../WORKSPACE_SETUP/payload/project/reference-map.md) are user-populated templates; they do not currently provide an active-worktree mapping.
- [Ticket initialization](../../WORKSPACE_SETUP/payload/skills/ca-jira-ticket-init/SKILL.md) resolves its helper relative to the skill. The [brief template](../../WORKSPACE_SETUP/payload/skills/ca-jira-ticket-init/templates/brief.md) records repository ID, branch and baseline but lacks an explicit checkout-path field. Define cooperation with ticket initialization without overwriting an existing brief or treating an ID as fetched Jira data.
- [Copilot guidance](../../WORKSPACE_SETUP/payload/root/COPILOT_GUIDE.md) already distinguishes discovery from actual instruction inclusion and provides fallbacks; the worktree flow needs actual manual evidence of its own.

Keep Python setup/runtime tools offline, standard-library-only and free of subprocess requirements. Investigate whether the explicitly invoked skill performs Git/network commands while a local helper only prepares/validates paths and workspace data. Document the scoped change needed to the canonical design's current no-automatic-Git contract; do not silently broaden ordinary setup or ticket operations.

If later approved, align effective configuration, initialization, runtime layout, release inventory/mappings, generated guides, skills and focused tests. Preserve installer independence and moved/renamed development folders. Existing workspaces have no automatic upgrade; decide their adoption path. This investigation does not implement those changes, alter product versions, install software, authenticate, publish branches or release artifacts.

## Failure, lifecycle and portability questions

- Validate ticket IDs, Git refs and destination paths as data, not shell syntax; handle spaces, Unicode, leading dashes, case collisions and redirected paths consistently with supported environments.
- Define an exclusive new-task reservation, observed Git state and recoverable phases. If fetching, worktree creation or workspace-file publication fails, report what actually happened and preserve inspectable results. Repeated or interrupted runs must not overwrite task code or silently reset branches.
- Use Git-aware removal rather than treating a linked checkout as an ordinary disposable folder. Define handling for modified/untracked files, ignored local files, remaining task metadata and whether cleanup is manual or needs a separately scoped workflow.
- Preserve shared tickets/context when removing a task checkout. Archiving a local ticket must not implicitly delete the worktree or change Git/Jira state.
- Relative VS Code paths do not by themselves make Git's linkage portable. Compare version-gated relative Git worktree links with documented `git worktree repair` after moving the entire development folder; retain Git-version compatibility limits explicitly.
- Consider repository-specific dependencies, ignored environment files, hooks, submodules, build outputs and occupied service ports. Select an honest initial support boundary rather than implicitly promising full environment replication.
- Decide whether the first implementation supports one repository per ticket or multiple selected worktrees. The proposed `repo/` layout currently assumes one; do not silently register the same ticket twice for different repositories.

## Investigation evidence and verification plan

No worktree, IDE or Copilot experiment was performed while preparing this draft. Source inspection and documentation references are not evidence that the proposed skill works.

The investigation should identify a small useful prototype/evidence plan, keeping synthetic fixtures under `_tmp/` and avoiding changes to real user branches. Proposed coverage:

- Local synthetic Git remotes: successful latest-source selection, source advanced after clone, update failure, exact SHA, unavailable SHA, branch-in-use, remote-only branch, local behind/ahead/diverged branch, explicit new name and branch/destination collisions.
- Default/custom directory names, spaces/Unicode, invocation from an unrelated terminal directory, installer removal and complete development-root relocation.
- Workspace folder lists and relative paths include only the chosen checkout plus selected shared roots. Confirm original shared document links remain valid and original-checkout links do not misdirect task edits.
- Interrupted creation, repeat/resume policy and Git-aware cleanup preserve code, user metadata and shared context. Verify ignored-file handling separately from clean `git status` output.
- Actual VS Code/Copilot runs with recorded versions: no-input/partial-input invocation, accepted defaults, blank/“same”, new-branch choice, optional SHA, original/user-added skill discovery, instruction inclusion, repository guidance, two simultaneous task windows and fallback behavior.
- Define tests for any new local helpers and the existing isolated behavioral suite when implementation affects behavior/packaging. Specify release exclusions and adopted-platform limits. Native Windows and other unavailable environments remain unverified until actually tested.

## Readiness decision and handoff

This draft does not mark the functionality ready. The investigation must resolve or explicitly bound the open questions, document the recommended design and supporting evidence, and record the maintainer's reviewed readiness decision in the owning issue.

If the decision is **ready for implementation**, create a separate GitHub implementation issue with the reviewed scope, acceptance criteria, verification requirements and links to this design and investigation. Add the implementation issue link back to the investigation and the investigation link to the implementation issue **before closing #16**. Implementation need not be completed to close a properly handed-off design investigation.

If the decision is not ready or not to proceed, record the reasons and required next investigation or disposition; do not create an implementation issue merely to satisfy a checklist. GitHub remains the only progress/priority queue.

When implementation eventually lands, move the accepted behavior into the canonical design and shipped user guidance, then mark this draft superseded with resolving links. Preserve the issue history without maintaining a second current specification.

## Reference material

Official references consulted during the 1 November 2026 discussion; recheck relevant behavior during investigation:

- [Git worktrees](https://git-scm.com/docs/git-worktree): branch checkout restrictions, explicit creation, implicit tracking-branch creation, removal, relative links and repair.
- [Git fetch](https://git-scm.com/docs/git-fetch) and [pull](https://git-scm.com/docs/git-pull): retrieving remote commits versus integrating into the current branch.
- [VS Code worktrees](https://code.visualstudio.com/docs/sourcecontrol/branches-worktrees) and [multi-root workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces): separate windows, selected roots and relative workspace paths.
- [Copilot custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) and [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills): file-relative references, skill resources, harness-specific loading and verification.
