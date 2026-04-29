# Skill Generation Policy

This policy defines how PsyCalc agents may create reusable skill drafts from repeated work.

## Goal

Make recurring procedures easier to repeat without allowing silent self-modification.

Agents may notice repeated tasks and draft reusable procedures, but they must not silently change active behavior, agent routing, or domain claims.

## Core rule

```text
Auto-draft is allowed.
Auto-apply is not allowed without explicit human approval.
```

## Allowed without approval

- Notice repeated workflows or recurring failures.
- Record observations in `.agent-learning/logs/`.
- Create inactive skill drafts in `.agent-learning/skill-drafts/`.
- Create proposals in `.agent-learning/proposals/`.
- Recommend reviewers and acceptance criteria.

## Requires approval

- Moving a draft into `.agent-learning/approved-skills/`.
- Connecting an approved skill to a runtime skill system.
- Updating `.opencode/agents/*.md` to invoke a skill.
- Changing routing or delegation behavior.
- Weakening caveats or increasing certainty in any domain.

## High-risk domains

Skills involving these areas require specialist review before approval:

- empirical claims and validation;
- compatibility scoring;
- typing people;
- source provenance and citation status;
- Socionics, Psychosophy, or Temporistics theory;
- neuroscience, clinical, theology, military, public-figure, legal, or ethics-adjacent claims.

## Skill draft requirements

Each skill draft must include:

1. purpose;
2. when to use;
3. when not to use;
4. required inputs;
5. step-by-step workflow;
6. required checks and caveats;
7. forbidden shortcuts;
8. output format;
9. reviewer requirements;
10. acceptance criteria;
11. rollback or deactivation notes.

## Safe first use cases

Good initial candidates are narrow, low-risk maintenance workflows:

- wiki frontmatter audit;
- filename and wikilink checks;
- log/proposal/review template completeness checks;
- provenance-label formatting checks.

Avoid starting with high-risk skills such as definitive typing, medical interpretation, theology judgment, or compatibility score calibration.
