---
title: Create Social Media Automation Pipeline Agents and Skills
type: agent-improvement-proposal
created: 2026-04-25
updated: 2026-04-25
status: applied
risk: moderate
target_agents:
  - marketing-claims-safety-reviewer
  - short-video-package-builder
  - visual-storyboard-agent
  - social-caption-hashtag-agent
  - publication-planner-agent
required_reviewers:
  - human/project-owner
  - empirical-claims-caveats-reviewer
  - ethics-and-consent-reviewer
sources: [AGENTS.md, user-request]
---

# Agent Improvement Proposal: Create Social Media Automation Pipeline

## 1. Target agent(s)

- `.opencode/agents/marketing-claims-safety-reviewer.md`
- `.opencode/agents/short-video-package-builder.md`
- `.opencode/agents/visual-storyboard-agent.md`
- `.opencode/agents/social-caption-hashtag-agent.md`
- `.opencode/agents/publication-planner-agent.md`

Skill specifications:

- `.opencode/skills/short-video-package-builder.md`
- `.opencode/skills/video-assembler-skill.md`
- `.opencode/skills/social-publisher-skill.md`

## 2. Observed failure or opportunity

The user expected the assistant/agent system to do more than output a TikTok script. They want agents/skills that can automate the social-media pipeline from idea to upload-ready video package and eventually publishing/scheduling.

## 3. Evidence

- User feedback: “ты мне сценарий вывел, но сделала и не выложил видео в тик ток”
- User request: “мне нужны скиллы/агенты которые будут все это делать автоматически”
- User request: “создай нужных агентов найди нужные скиллы”
- Policy reference: `AGENTS.md` requires proposal-first governance for agent changes and human approval for high-risk changes.

## 4. Proposed instruction change

Create a dedicated social-media automation team:

1. `marketing-claims-safety-reviewer` — publication safety review.
2. `short-video-package-builder` — idea to complete upload-ready short-video package.
3. `visual-storyboard-agent` — script to visual production plan.
4. `social-caption-hashtag-agent` — captions, hashtags, CTAs, platform copy.
5. `publication-planner-agent` — manual/scheduler/API publication planning with approval gates.

Create skill specifications for:

1. `short-video-package-builder` — package generation.
2. `video-assembler-skill` — local `.mp4` assembly.
3. `social-publisher-skill` — future high-risk API publication with explicit approval and secret handling.

## 5. Risk assessment

- Risk level: `moderate` for package generation; `high` for future publication automation.
- Why: marketing and dating content can incentivize overclaims, sensitive-attribute misuse, and accidental publication.
- Could this increase overclaiming? `yes`, mitigated by dedicated safety reviewer.
- Could this bypass specialist delegation? `yes`, mitigated by routing rules.
- Could this affect high-stakes advice? `yes`, dating and sensitive identity content can affect real decisions.

Mitigations:

- No auto-publication by default.
- Explicit publication approval required.
- Token/secret storage prohibited in git.
- Sensitive claims routed to ethics/sociology/caveats reviewers.
- Compatibility/type/AI claims reviewed before publication.

## 6. Required reviewers

- [x] human/project owner requested implementation in chat
- [ ] `empirical-claims-caveats-reviewer` for future marketing claim audits
- [ ] `ethics-and-consent-reviewer` for campaigns involving religion, nationality, ethnicity, politics, migration, or dating safety
- [ ] security/process review before enabling real API publication

## 7. Patch sketch

```diff
++ .opencode/agents/marketing-claims-safety-reviewer.md
++ .opencode/agents/short-video-package-builder.md
++ .opencode/agents/visual-storyboard-agent.md
++ .opencode/agents/social-caption-hashtag-agent.md
++ .opencode/agents/publication-planner-agent.md
++ .opencode/skills/short-video-package-builder.md
++ .opencode/skills/video-assembler-skill.md
++ .opencode/skills/social-publisher-skill.md
```

## 8. Acceptance criteria

- [x] The new agents cover the workflow from idea to upload package.
- [x] They do not publish without explicit approval.
- [x] They preserve caveats and route risky claims.
- [x] They separate package generation from high-risk publishing.
- [x] Skill specs identify required integrations and security constraints.

## 9. Rollback note

Delete the added agent and skill files if the pipeline proves unsafe or unmanageable. Do not enable publication automation until credentials, approval gates, audit logs, and security review are in place.
