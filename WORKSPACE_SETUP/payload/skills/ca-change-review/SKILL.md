---
name: ca-change-review
description: Review a ticket change against its requirements and verified per-repository baseline for behavioral regressions.
disable-model-invocation: true
---

# Review a change

Read the supplied brief and relevant plan/repository rules. Use the [review checklist](resources/review-checklist.md)
for the requested scope. Establish a verified baseline per affected repository; missing requirements or a usable
baseline must be surfaced rather than invented. Ticket IDs in commit subjects are candidate hints only.

Inspect cumulative committed and uncommitted changes, including staged/unstaged/untracked work as relevant.
Prioritize behavior, requirements, interfaces, and regression evidence. Cite concrete files/diffs for findings;
distinguish confirmed problems from uncertainty, and static inspection from checks actually executed.

Do not edit source, change branches, reset/stash/commit, authenticate, deploy, or run production SQL.
Suggest meaningful tests; execute them only within the user's authorization and normal tool approvals.
Return a concise findings report; save a review document only when requested. Existing CI/PR review remains in force.
