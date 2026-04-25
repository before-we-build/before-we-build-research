---
title: Social Media Automation Pipeline Creation
type: agent-learning-log
created: 2026-04-25
updated: 2026-04-25
status: implemented
sources: [AGENTS.md, user-request]
---

# Social Media Automation Pipeline Creation

## Observation

The user wants automatic social-media execution for PsyCalc / Cognitive Matchmaker instead of manually handling content production. The immediate pain point was that the assistant produced only a TikTok script, not a video package or publication workflow.

## Action

Created new agent specifications:

- `marketing-claims-safety-reviewer`
- `short-video-package-builder`
- `visual-storyboard-agent`
- `social-caption-hashtag-agent`
- `publication-planner-agent`

Created skill specifications:

- `short-video-package-builder`
- `video-assembler-skill`
- `social-publisher-skill`

## Safeguards

- No agent publishes content by default.
- Publication requires platform access, secure secret handling, final preview, and explicit user approval.
- Marketing and compatibility claims must be reviewed before publication.
- Sensitive identity topics are routed to ethics/sociology review.

## Next implementation steps

1. Build a local `outputs/social/` package generator.
2. Add a simple FFmpeg/MoviePy renderer for vertical `.mp4` videos.
3. Add brand kit defaults: colors, fonts, subtitle style, disclaimer style.
4. Only later configure scheduler/API publishing.
