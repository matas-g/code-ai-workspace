# Use Copilot with Code-AI

The [orientation file](.github/copilot-instructions.md) gives Copilot directions to your project context and tickets. Check that Copilot receives it; otherwise attach relevant files yourself.

## Prepare once

1. Complete the [root guide's setup steps](../README.md#get-started), then open [{{vscode_workspace_name}}.code-workspace](../ide_configs/{{vscode_workspace_name_link}}.code-workspace) in VS Code. **AI Work**, **Knowledge** and your enabled repositories should be visible.
2. Sign in with your approved Copilot account and select **Local** as the chat's execution environment. Use **Ask** for questions, **Plan** for planning and **Agent** for approved changes. Available modes and tools vary.
3. Fill in the context files from verified sources:

   | File | Add |
   |---|---|
   | [Project overview](project/overview.md) | Repository responsibilities, interfaces and behavior to preserve |
   | [Reference map](project/reference-map.md) | Authoritative source links, owners and dates checked |

   Record enough verified context for your first task; leave unknowns explicit. Review the generated [orientation](.github/copilot-instructions.md), which links these files. Editing it is optional.

## Verify your setup

1. Follow the [automatic context check](#check-automatic-context-loading) in one repository and the mode you intend to use. Confirm both instruction inclusion and relevant context reads.
2. In Agent chat, find the [six commands](DAILY_WORK.md#copilot-commands) in the `/` menu. Run `/ca-jira-ticket-init TEST-1 - verify local ticket creation` with an unused sample ID and normal tool approvals, then check that `tickets/active/TEST-1/brief.md` contains your supplied details.
3. Run `/ca-config-audit`, review its findings and resolve structural errors. A successful audit does not prove Copilot loading.

If automatic context or skills are unavailable, verify the [attachment](#if-context-is-missing) and [skill fallbacks](#check-the-skills) with the same small task. Continue to daily work when these checks pass or the needed fallback works; keep remaining limitations explicit.

## Start a task

[Follow the daily ticket workflow](DAILY_WORK.md#work-on-a-ticket). Attach the selected brief and relevant files in chat, and ask Copilot to read them; folder visibility alone does not supply all context to a request.

Read [Knowledge](../{{knowledge_link}}/README.md) on demand; avoid attaching everything. Check answers, test changes and follow repository/company guidance.

## Check automatic context loading

Use a small verified fact from your overview/reference map; use synthetic context when testing the framework:

1. In VS Code's Command Palette, run **Chat: Open Customizations** → **Instructions**. Find `{{ai_work}}/.github/copilot-instructions.md`. Listing proves discovery only.
2. Open a file from the repository you intend to use and start a **new chat**. Ask about a fact in your overview or reference map without attaching or naming those files or the orientation.
3. Expand **References** or inspect chat debug details to confirm orientation inclusion. Check file reads and answer accuracy; a correct answer alone does not prove loading.

**Extended verification:** Maintainers repeat across **MAIN**, **OTHER** and **DOCS** files, available modes, renamed folders and after moving the development folder. Check repository guidance still applies. Record OS, package, Python, VS Code/Copilot versions, environment, mode and evidence. This full matrix is separate from basic onboarding; coverage remains unverified and validation only checks files.

## If context is missing

Attach the [orientation](.github/copilot-instructions.md), relevant project files and current brief. This fallback does not count as an automatic-loading test.

Inspect `github.copilot.chat.codeGeneration.useInstructionFiles` in VS Code Settings and respect applicable policy. Do not copy instructions globally or into company repositories as a workaround. Instructions do not affect inline suggestions.

You can edit the orientation; refresh preserves it. Keep its links relative.

## Check the skills

Skills are on-demand workflows. Check that the [six `ca-` commands](DAILY_WORK.md#copilot-commands) appear in chat's `/` menu; their discovery is separate from orientation loading.

**Extended verification:** Using a made-up ticket, check preserved edits on repeat creation, archive/restore and unchanged attachments. Check review loads its checklist and audit returns findings. Test refresh approval and [interruption recovery](../README.md#add-hide-or-remove-a-repository) separately. Python success does not prove skill loading.

For unavailable skills, use the [optional Python reference](DAILY_WORK.md#optional-python-reference). For reviews, attach the [procedure](.github/skills/ca-change-review/SKILL.md) and [checklist](.github/skills/ca-change-review/resources/review-checklist.md).

## Further help

[VS Code instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) · [Verification](https://code.visualstudio.com/docs/agent-customization/custom-instructions#verify-your-instructions) · [Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)

References checked 29 October 2026.
