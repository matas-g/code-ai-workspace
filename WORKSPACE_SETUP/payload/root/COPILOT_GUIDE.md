# Use Copilot with Code-AI

The [orientation file](.github/copilot-instructions.md) gives Copilot directions to your project context and tickets. Check that Copilot receives it; otherwise attach relevant files yourself.

## Prepare once

1. For initial setup, manually run the root folder's [refresh launcher](../README.md#get-started), then open [{{vscode_workspace_name}}.code-workspace](../ide_configs/{{vscode_workspace_name_link}}.code-workspace) in VS Code. If **AI Work**, **Knowledge** or repositories are missing, [refresh the workspace](../README.md#add-hide-or-remove-a-repository).
2. Sign in with your approved Copilot account and select **Local** as the chat's execution environment. Use **Ask** for questions, **Plan** for planning and **Agent** for approved changes. Available modes and tools vary.
3. Fill in the context files from verified sources:

   | File | Add |
   |---|---|
   | [Project overview](project/overview.md) | Repository responsibilities, interfaces and behavior to preserve |
   | [Reference map](project/reference-map.md) | Authoritative source links, owners and dates checked |

## Start a task

[Create or open a ticket](DAILY_WORK.md#work-on-a-ticket), attach its `brief.md` and relevant files in chat, and ask Copilot to read them. Jira details are never fetched.

Read [Knowledge](../{{knowledge_link}}/README.md) on demand; avoid attaching everything. Check answers, test changes and follow repository/company guidance.

## Check automatic context loading

Use made-up project facts for this check:

1. In VS Code's Command Palette, run **Chat: Open Customizations** → **Instructions**. Find `{{ai_work}}/.github/copilot-instructions.md`. Listing proves discovery only.
2. Open a file from a **MAIN** repository and start a **new chat**. Ask about a fact in your overview or reference map without attaching or naming those files or the orientation.
3. Expand **References** or inspect chat debug details to confirm orientation inclusion. Check file reads and answer accuracy; a correct answer alone does not prove loading.

Repeat with **OTHER** and **DOCS** files, available modes, renamed folders and after moving the development folder. Check repository guidance still applies. Record OS, package, Python, VS Code/Copilot versions, environment, mode and evidence. Full coverage remains unverified; validation only checks files.

## If context is missing

Attach the [orientation](.github/copilot-instructions.md), relevant project files and current brief. This fallback does not count as an automatic-loading test.

Inspect `github.copilot.chat.codeGeneration.useInstructionFiles` in VS Code Settings and respect applicable policy. Do not copy instructions globally or into company repositories as a workaround. Instructions do not affect inline suggestions.

You can edit the orientation; refresh preserves it. Keep its links relative.

## Check the skills

Skills are on-demand workflows. Type `/` in chat to find the [six `ca-` commands](DAILY_WORK.md#copilot-commands); their discovery is separate from orientation loading.

Using a made-up ticket, check creation, preserved edits on repeat creation, archive/restore and unchanged attachments. Check review loads its checklist and audit returns findings. Python success does not prove skill loading.

For later updates, `/ca-workspace-refresh` previews changes and applies them after approval. Changing the first workspace folder can [restart extensions](https://code.visualstudio.com/api/references/vscode-api#workspace.onDidChangeWorkspaceFolders), potentially interrupting Copilot. Test this separately; use the launcher if chat is interrupted.

For unavailable skills, use the [optional Python reference](DAILY_WORK.md#optional-python-reference). For reviews, attach the [procedure](.github/skills/ca-change-review/SKILL.md) and [checklist](.github/skills/ca-change-review/resources/review-checklist.md).

## Further help

[VS Code instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) · [Verification](https://code.visualstudio.com/docs/agent-customization/custom-instructions#verify-your-instructions) · [Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)

References checked 28 October 2026.
