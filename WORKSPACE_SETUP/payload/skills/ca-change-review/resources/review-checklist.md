# Change review checklist

- What acceptance criteria and existing behavior must hold?
- Is each repository baseline verified? Was pre-existing or untracked work handled explicitly?
- Does the comparison cover all ticket commits and the current working changes without confusing unrelated work?
- Are SQL nulls, duplicates, joins, partitions, incremental reruns and representative outputs affected?
- Are Python interfaces, failure paths, input validation and dependencies covered?
- Do infrastructure changes alter replacement/destruction, access scope, providers or state assumptions?
- Are cross-repository dependencies and rollout order addressed?
- Which tests or plans actually ran? Which findings have executable evidence?

Use only relevant questions. No requirement for a separate plan/review file for a trivial edit.
