# SKILL: evidence-packager

## Purpose

Package the project into a compact evidence packet that a researcher can assess quickly.

## When to Use

- Before outreach
- Before a call with a researcher
- When someone asks for a summary, one-pager, demo notes, or validation posture

## Required Artifacts

1. **One-sentence thesis**
2. **What is new**
3. **What is already implemented / specified**
4. **What is hypothesis-only**
5. **Validation roadmap**
6. **Specific ask**

## Output Format

```yaml
packet:
  thesis: "..."
  novelty: ["...", "..."]
  current_assets: ["...", "..."]
  open_risks: ["...", "..."]
  validation_plan: ["...", "..."]
  ask: "..."
```

## Rules

- Keep the packet reviewable in under 3 minutes
- Make uncertainty explicit
- Include one concrete artifact: repo, page, demo flow, matrix, or pilot design
- Never bury the ask at the end without context

## What Belongs In The Packet

- cleaned conceptual model
- strongest external research anchors
- current epistemic status
- one or two experiments you want help with

## What Does Not Belong

- long ideology
- unvalidated exact percentages
- giant literature dump without narrative

## Dependencies

- `research-bridge-builder`

## Related Skills

- `outreach-personalizer`
- `collaboration-ask-designer`
