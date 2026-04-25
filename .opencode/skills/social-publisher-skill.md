---
name: social-publisher-skill
description: Skill specification for publishing or scheduling approved social media packages through platform APIs or schedulers. High-risk; requires credentials, secret handling, final preview, and explicit human approval.
risk: high
requires_approval: true
---

# Social Publisher Skill

## Purpose

Publish or schedule approved social media content after human approval.

Supported targets may include:

- TikTok Content Posting API;
- YouTube Data API;
- Meta Graph API for Instagram/Facebook;
- X API;
- Buffer / Later / Hootsuite / Metricool / Publer.

## Hard Requirements

Do not publish unless:

1. credentials are configured outside git;
2. platform/account identity is shown;
3. final video path is shown;
4. caption and hashtags are shown;
5. schedule/publish time is shown;
6. safety review status is shown;
7. user explicitly approves the exact publication.

## Secret Handling

Never store tokens in:

- agent markdown files;
- wiki pages;
- git-tracked config;
- logs or proposals.

Use:

- `.env.local` ignored by git;
- OS keychain;
- 1Password CLI;
- Doppler / Vault;
- CI secrets.

## Audit Log

For every publication, store:

- content package path;
- platform;
- account;
- caption hash;
- video hash;
- approval text;
- timestamp;
- result URL or scheduled ID.
