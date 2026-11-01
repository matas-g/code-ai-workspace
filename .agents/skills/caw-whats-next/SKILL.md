---
name: caw-whats-next
description: Give a brief live summary of this project's open GitHub issues labelled next and recommend one to implement. Read-only; use for choosing work, not reprioritizing or implementing it.
---

# Choose the next issue

Locate the Code AI Workspace repository from the current directory and its parents using `AGENTS.md` and `WORKSPACE_SETUP/scripts/workspace_manager.py`. Read [contributor instructions](../../../AGENTS.md), including the maintainer issue-workflow rules. This skill belongs to this project's development process, outside the product payload.

Fetch current open issues with the exact `next` label in the confirmed repository. Prefer the connected GitHub tools; paginate or disclose a limited result set. Read enough of their bodies and relevant recent comments to identify the outcome, remaining acceptance criteria and actual blockers. Do not infer priority from issue number or age.

Recommend one ready issue based on the owner's current delivery scope, consequence, real prerequisites and ability to finish and verify it. Use targeted local source/evidence checks only when needed to resolve stale or conflicting claims. Keep missing verification distinct from a confirmed bug. Prefer one independently reviewable outcome; suggest a small bundle only when it is clearly easier to implement and review together.

If no open issues carry `next`, say so and inspect other open issues to suggest up to three candidates without labelling them. If all candidates are blocked, identify what is missing and suggest an available independent task if one exists. If access fails, report that limitation rather than presenting cached status as current.

Aim for 100–150 words: one linked line per candidate with its outcome and material blocker, followed by one recommendation and reason. If the shortlist is unexpectedly large, show the most relevant few and disclose the remainder. Give a simple next action such as “Implement #N.”

Do not change files, labels, issue content or state; implement work; run product tests/builds; or perform full-project onboarding for this summary.
