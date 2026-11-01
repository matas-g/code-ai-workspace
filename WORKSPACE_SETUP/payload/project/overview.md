# Project overview — not yet populated

This is a template, not a statement of actual architecture. Fill it from verified sources.

## Purpose

Not yet recorded.

## Repositories and responsibilities

| Repository | Responsibility | Interfaces/dependencies |
|---|---|---|
| Not yet recorded | Not yet recorded | Not yet recorded |

## Data flow and external interfaces

Not yet recorded.

## Existing behavior and important constraints

Not yet recorded.

## Git naming conventions

These are editable defaults, not verified company policy. Use them when the target repository and company guidance do not specify a convention. Record verified exceptions and their sources below; surface contradictory guidance before choosing a name.

### Branch names

Format: `<type>/<ticket-id>_<short-description>`.

- Use `feature` or `bugfix` for the type. Default to `feature` when no type is specified.
- Preserve the ticket ID's canonical spelling, such as `ABC-123`. For a GitHub issue such as `#42`, use `42` in the branch name.
- Use a short lowercase description with words separated by underscores.
- Without a ticket, use `<type>/<short-description>`; do not invent an ID.

Examples: `feature/ABC-123_add_export`, `bugfix/42_handle_empty_input`, `feature/update_setup_guide`.

### Commit messages

Subject format: `<ticket-id> <Change area>. <Short summary>`.

- Preserve the ticket reference, such as `ABC-123` or `#42`. For multiple tickets, list the relevant references separated by spaces before the change area.
- Use 1–4 words for the change area to identify the affected part of the system or the type of change, such as `CSV export`, `Input validation` or `Documentation`. Follow it with a period and a space.
- Start the summary with a capitalized action verb, keep it concise and omit the final period.
- Without a ticket, use `<Change area>. <Short summary>`. Add a body when the reason, impact or validation needs explanation.
- Follow repository-specific formats for release, merge, revert or automated commits when defined.

Examples: `ABC-123 CSV export. Add download option`, `#42 Input validation. Handle empty input`, `Documentation. Update setup guide`.

### Repository-specific exceptions

| Repository | Branch format | Commit format | Authoritative source / last verified |
|---|---|---|---|
| Not yet recorded | Use defaults unless overridden | Use defaults unless overridden | Not yet recorded |

Before suggesting or using a branch name or commit message, read these rules and the target repository's applicable guidance. Naming rules do not authorize creating a branch or making a commit.

## Sources and verification date

Not yet recorded. See the [reference map](reference-map.md).
