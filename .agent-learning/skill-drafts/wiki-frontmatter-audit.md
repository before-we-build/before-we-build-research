# Skill Draft: wiki-frontmatter-audit

Status: draft / inactive
Created: 2026-04-28
Updated: 2026-04-28
Proposed by: master-orchestrator
Related logs: `.agent-learning/logs/2026-04-28-skill-generation-bootstrap.md`
Related proposal: `.agent-learning/proposals/2026-04-28-create-skill-generation-loop.md`

## Purpose

Provide a repeatable low-risk workflow for checking whether wiki pages follow PsyCalc wiki schema conventions.

This skill is for structure and metadata audit only. It does not validate typological, empirical, clinical, theological, military, or compatibility claims.

## When to use

- When asked to audit one or more files under `wiki/`.
- Before or after adding a wiki page.
- When checking whether a page follows `AGENTS.md` wiki conventions.

## When not to use

- Do not use as a substitute for source provenance review.
- Do not use to judge whether claims are true.
- Do not use to rewrite domain content without separate user request.
- Do not use for raw source files outside `wiki/` unless explicitly adapted.

## Required inputs

- Target wiki file path or list of paths.
- Current `AGENTS.md` wiki conventions.
- Relevant `index.md` entry if checking catalog consistency.

## Workflow

1. Read the target wiki page.
2. Check for YAML frontmatter.
3. Verify required frontmatter fields:
   - `title`
   - `type`
   - `tags`
   - `created`
   - `updated`
   - `sources`
4. Check that `type` is one of:
   - `concept`
   - `entity`
   - `relation`
   - `source`
5. Check that filename is kebab-case.
6. Check that internal references use wikilinks where appropriate.
7. Check that source-backed claims have a `sources` entry or explicit caveat.
8. Check that PsyCalc is not reduced to Cognitive Matchmaker except on application-specific pages.
9. Report findings as pass / warning / fail.
10. If edits are requested, make only minimal structural corrections unless the user asks for content rewriting.

## Required checks

- Page has required frontmatter.
- `updated` date is current when edits are made.
- Source references are present when the page makes source-backed claims.
- The page preserves the project framing:
  - PsyCalc is the broader ontology/framework.
  - Cognitive Matchmaker is a downstream dating-oriented application.

## Caveats to preserve

- Typological mappings in PsyCalc are project heuristics and research hypotheses.
- Structural compliance does not mean empirical validity.
- A clean wiki page can still need specialist review for domain claims.

## Forbidden shortcuts

- Do not invent sources.
- Do not mark a claim as validated only because it appears in another generated wiki page.
- Do not silently change the meaning of a page while fixing metadata.
- Do not replace specialist review with this audit.

## Output format

```text
## Wiki Frontmatter Audit: <file>

Status: pass / warnings / fail

Findings:
- [pass/warning/fail] <finding>

Suggested fixes:
- <fix>

Requires specialist review: yes/no
Reason: <brief reason>
```

## Reviewer requirements

Human review is enough for this low-risk structural skill.

Specialist review is required if the skill is expanded to evaluate domain claims, source interpretations, compatibility logic, clinical boundaries, theology, statistics, or empirical validity.

## Acceptance criteria

- The skill identifies missing or malformed frontmatter.
- The skill distinguishes structural audit from domain validation.
- The skill does not invent citations or rewrite claims without request.
- The skill preserves PsyCalc vs Cognitive Matchmaker scope boundaries.

## Rollback / deactivation

If this skill causes over-editing or false confidence, move it out of `approved-skills/` or remove runtime references to it. Keep the draft and review trail for audit history.
