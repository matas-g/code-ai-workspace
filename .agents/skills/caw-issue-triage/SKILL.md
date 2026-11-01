---
name: caw-issue-triage
description: Review this project's GitHub issue scope and priorities, recommend a small next shortlist, and apply issue or label updates when the user requests them. Use for queue maintenance, not implementation.
---

# Maintain a small useful issue queue

Locate this repository using `AGENTS.md` and `WORKSPACE_SETUP/scripts/workspace_manager.py`; read [contributor instructions](../../../AGENTS.md) and their maintainer issue-workflow rules. Use current GitHub issues as the live queue and [the backlog index](../../../maintenance/BACKLOG.md) only for legacy mappings and deferred scope.

Inspect the relevant open issues, bodies and progress/blocker comments. Check matching closed issues before proposing new work or reopening a reported defect. Read current source or evidence where it materially affects relevance; preserve historical results and distinguish confirmed defects, inspection proposals and missing verification.

Recommend a few ready `next` issues, normally two to four, based on the owner's current delivery scope, impact, actual prerequisites and observable completion. Use `bug`, `improvement` and `verification` for the kind of work. Related fixes can share a checklist; split only for independently useful priority or completion. Explain real blockers plainly. Keep speculative maintenance/future-platform ideas deferred until useful; do not add Projects, milestones, estimates, hierarchies or status-label families.

A request to review or recommend is read-only. A request to apply identified changes authorizes those updates without another approval round. If the requested outcome leaves a material product or scope decision unresolved, present the concrete options; proceed with independent authorized work. Creating this skill does not authorize live issue changes.

Before a mutation, re-read affected issues and current labels. Preserve unrelated labels, body context and other metadata; prefer additive/removal label operations over replacing the entire label set. Keep completed checklists and evidence intact. For new issues, check duplicates and use a short problem/outcome, observable “Done when” checklist and resolving references; include enough context when supporting material is unpublished locally. Close/reopen only within the requested scope and supported by evidence.

After updates, read back the affected issues to confirm the intended changes. If interrupted or a write result is uncertain, inspect current state before retrying. Finish with linked recommendations or the actual before/after changes and any unresolved blockers/access limits. Do not implement product fixes or create a second local status queue.
