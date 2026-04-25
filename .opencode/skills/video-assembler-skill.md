---
name: video-assembler-skill
description: Skill specification for assembling vertical videos from scripts, subtitles, voiceover, background assets, and captions using local tooling such as FFmpeg or MoviePy.
risk: moderate
requires_approval: false
---

# Video Assembler Skill

## Purpose

Create a local `.mp4` video file from approved production assets.

## Suggested Stack

- FFmpeg for rendering and muxing;
- Python MoviePy / PIL for programmatic composition;
- local fonts for subtitles;
- optional TTS provider for voiceover;
- optional music/sound bed with cleared license.

## Inputs

```text
script.md
storyboard.md
subtitles.srt
voiceover.wav/mp3
background.mp4/png/jpg
assembly-spec.md
```

## Outputs

```text
video.mp4
thumbnail.png
render-log.json
```

## Safety

- Do not use copyrighted likeness, music, or video without rights.
- Do not imitate a real person's voice without consent.
- Preserve the approved script and caveat text.

## Future Implementation Options

- `scripts/render_short_video.py`
- FFmpeg template command;
- CapCut/Canva manual-export bridge.
