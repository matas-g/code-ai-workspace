# Use Copilot with Code-AI

The [orientation file](.github/copilot-instructions.md) points Copilot to your context and tickets. Check that it loads; otherwise attach relevant files yourself.

## Prepare once

1. Open [{{vscode_workspace_name}}.code-workspace](../ide_configs/{{vscode_workspace_name_link}}.code-workspace) in VS Code. If **AI Work**, **Knowledge** or repositories are missing, [refresh the workspace](../README.md#add-hide-or-remove-a-repository).
2. Sign in to your approved Copilot account and select **Local**. Use **Ask** for questions, **Plan** for planning and **Agent** for authorized execution; available tools vary by mode.
3. Fill in the context files from verified sources:

   | File | Add |
   |---|---|
   | [Project overview](project/overview.md) | Repository responsibilities, interfaces and behavior to preserve |
   | [Reference map](project/reference-map.md) | Authoritative source links, owners and dates checked |

## Start a task

[Create or open a ticket](DAILY_WORK.md#work-on-a-ticket), then attach its brief and relevant files. Ask Copilot to read them first. Ticket creation does not fetch Jira requirements.

Consult [Knowledge](../{{knowledge_link}}/README.md) and company documentation as needed. Avoid attaching the whole framework. Check answers and test changes; repository and company instructions still apply.

## Check automatic context loading

Use synthetic context for this check:

1. Run **Chat: Open Customizations**, select **Instructions** and find `{{ai_work}}/.github/copilot-instructions.md`. This confirms discovery only.
2. Start a **fresh chat** with a MAIN repository file active. Ask a question answered by your overview/reference map. Do not attach or name the orientation or tell Copilot where to read.
3. Inspect **References** or available chat debug details to confirm the orientation was included. Check that Copilot read relevant context and answered correctly. A correct answer or repeated keyword alone is insufficient evidence.

Repeat for OTHER/DOCS roots, available modes, custom names and relocation; check repository guidance still applies. Record OS, package, Python and IDE/extension versions, environment, mode and evidence. This full matrix remains unverified; structural validation does not certify loading.

## If context is missing

Attach the [orientation](.github/copilot-instructions.md), relevant project files and current brief. This fallback does not count as an automatic-loading test.

Check `github.copilot.chat.codeGeneration.useInstructionFiles` and applicable policy. Respect restrictions; do not move instructions globally or into company repositories as a workaround. Instructions do not govern inline suggestions.

You can edit the orientation; refresh preserves it. Keep its links relative.

## Check the skills

Look for the [five `ca-` commands](DAILY_WORK.md#copilot-commands) in the slash-command menu. Check skills separately from orientation loading.

Create a synthetic ticket, then archive and restore it. Check captured details, preserved edits on repeat creation and unchanged attachments. Verify review loads its checklist and audit reports findings. Direct Python success does not prove skill loading.

If skills are unavailable, use the [daily Python commands](DAILY_WORK.md#run-commands-without-copilot). Attach the [review procedure](.github/skills/ca-change-review/SKILL.md) and [checklist](.github/skills/ca-change-review/resources/review-checklist.md) for a manual review workflow.

## Further help

[VS Code instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) · [Verification](https://code.visualstudio.com/docs/agent-customization/custom-instructions#verify-your-instructions) · [Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)

Documentation checked 25 October 2026; UI labels may differ in your installed version.
