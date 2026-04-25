---
title: Create Social Media Strategy Agent
type: agent-improvement-proposal
created: 2026-04-25
updated: 2026-04-25
status: applied
risk: moderate
target_agents: [social-media-strategy-agent]
required_reviewers: [human/project-owner, empirical-claims-caveats-reviewer]
sources: [AGENTS.md, user-request]
---

# Agent Improvement Proposal: Create Social Media Strategy Agent

## 1. Target agent(s)

- `.opencode/agents/social-media-strategy-agent.md`

## 2. Observed failure or opportunity

The user wants to promote PsyCalc / Cognitive Matchmaker across TikTok, YouTube, Instagram, Facebook, X, and Threads, but does not want to personally operate social media strategy. The existing explanation/outreach agents can produce presentations, stories, and skeptic-safe framing, but there is no dedicated agent for platform strategy, content pillars, growth experiments, and social-media routing.

## 3. Evidence

- User request: “не сам этим заниматься я не хочу давай создавать агентов”
- Prior context: the user identified TikTok, YouTube, Instagram, Facebook, X, and Threads as target channels.
- Policy reference: agent self-improvement workflow in `AGENTS.md` requires proposal-first governance and caveat-preserving agent changes.

## 4. Proposed instruction change

Create a new dedicated agent that can:

- define platform-specific social media strategy;
- distinguish PsyCalc from Cognitive Matchmaker;
- create content pillars and growth experiments;
- route risky claims to appropriate reviewers;
- avoid pseudoscientific, deterministic, clinical, or discriminatory marketing claims.

## 5. Risk assessment

- Risk level: `moderate`
- Why: marketing agents can easily incentivize overclaiming, sensationalism, or sensitive dating claims.
- Could this increase overclaiming? `yes`, if not constrained.
- Could this bypass specialist delegation? `yes`, if not instructed to route risky claims.
- Could this affect high-stakes advice? `yes`, because dating, religion, nationality, and identity can affect life decisions.

Mitigation: the new agent includes mandatory safety rules and routes empirical, ethical, sociological, and sensitive-attribute claims to relevant reviewers.

## 6. Required reviewers

- [x] human/project owner approval requested and given in chat
- [ ] `empirical-claims-caveats-reviewer` for future marketing claim audits
- [ ] `ethics-and-consent-reviewer` for sensitive identity and dating-safety campaigns

## 7. Patch sketch

```diff
++ .opencode/agents/social-media-strategy-agent.md
+ dedicated social media strategy agent for PsyCalc / Cognitive Matchmaker
+ platform guidance for TikTok, YouTube, Instagram, Facebook, X, Threads
+ mandatory anti-overclaim and sensitive-attribute safeguards
```

## 8. Acceptance criteria

- [x] The new rule is narrow and enforceable.
- [x] It does not weaken caveats.
- [x] It preserves delegation-first routing.
- [x] It cites the relevant source/policy/audit finding.
- [x] It can be checked in a future audit.

## 9. Rollback note

Delete `.opencode/agents/social-media-strategy-agent.md` and mark this proposal as superseded or reverted if the agent produces unsafe, misleading, or ungovernable marketing strategy.
