---
name: ca-workspace-refresh
description: Preview and apply Code-AI repository registrations and saved VS Code folder-list updates on request.
disable-model-invocation: true
---

# Refresh the VS Code repository list

Use the installed [workspace tool](../../../tools/workspace_manager.py), resolving its absolute path
from this skill rather than the terminal working directory. Run it with an approved Python 3.9+
executable and `-I -S -B`, quoting the script path. Do not edit configuration or workspace JSON yourself.

For initial VS Code setup, recommend manually running the development root's refresh_vscode_workspace
launcher before opening the saved workspace. For later chat-driven refreshes, follow this procedure:

1. Run `workspace_manager.py refresh` for a read-only preview. Summarize new registrations, missing
   folders, warnings and proposed VS Code folder changes. Explain that manual roots outside the
   inventory will be removed from the view; settings and repository contents are preserved.
   If nothing changes, report that and stop without applying.
2. Obtain approval for the displayed changes unless already supplied. Retain missing registrations
   by default. Use `--remove-missing` only when the user explicitly requests removal of all listed
   missing registrations; include it in both preview and apply. This removes configuration entries,
   never folders. Explain that changing the open workspace's folders, especially its first folder,
   may restart extensions and interrupt Copilot. Do not promise uninterrupted chat.
3. Immediately before applying, repeat the same read-only preview. If the proposed changes differ,
   show the new preview and obtain approval for those changes. Tell the user that applying is the
   final action and that, if chat is interrupted, they can inspect the result with the launcher.
   Run `workspace_manager.py refresh --apply` with the approved options as the final tool action.
   If chat continues, report the actual command result; do not require a follow-up tool call.

Use these noninteractive commands rather than answering terminal prompts or driving the launcher.
On refusal, error or partial completion, stop and report what the tool returned; completed registration
changes may remain saved. Do not retry writes automatically, emulate a repair, reopen VS Code,
clone/move repositories or change global settings. The [daily guide](../../../DAILY_WORK.md#update-the-vs-code-repository-list)
documents the manual fallback. Actual skill discovery and interruption behavior require IDE testing.
