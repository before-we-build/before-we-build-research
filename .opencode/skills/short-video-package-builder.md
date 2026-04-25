---
name: short-video-package-builder
description: Skill specification for producing upload-ready short-video packages for TikTok, Reels, Shorts, Facebook, X, and Threads. Generates package files but does not publish.
risk: moderate
requires_approval: false
---

# Short Video Package Builder Skill

## Purpose

Automate the non-publishing part of the social video workflow:

```text
brief → script → storyboard → subtitles → caption → safety checklist → assembly spec → upload package
```

## Outputs

Recommended output directory:

```text
outputs/social/YYYY-MM-DD/<slug>/
  brief.md
  script.md
  storyboard.md
  subtitles.srt
  caption.md
  safety-review.md
  assembly-spec.md
  metadata.json
```

## Required Inputs

- topic;
- platform;
- target audience;
- desired length;
- language;
- CTA;
- safety constraints.

## Safety

- No publication.
- No account tokens.
- Claims involving compatibility, typology, AI, religion, nationality, or sensitive identity should be reviewed before publication.

## Future Implementation Options

- Markdown-only package generation.
- Python package writer.
- Integration with video assembler skill.
