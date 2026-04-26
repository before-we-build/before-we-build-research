---
title: Create Baptist Pastor Agent
type: agent-learning-log
created: 2026-04-26
updated: 2026-04-26
source: user-request
status: proposed
---

# Learning Log: Create Baptist Pastor Agent

## Trigger

The user requested a new specialist agent named **Baptist Pastor** for Christianity, Bible, Baptist theology, church life, preaching, discipleship, pastoral care, spiritual discernment, Christian ethics, and safety/usefulness for a Baptist audience.

## Observation

The repository already has `christian-theology-researcher` for broad Christian theological review and pastoral caveats. It lacks a narrower Baptist-oriented pastoral agent for sermon/discipleship/church-life usefulness, Baptist doctrinal distinctives, and audience-safety review.

## Decision

This is a high-stakes theological/pastoral domain change. It should be treated as a proposal-first addition with explicit caveats: the agent must not claim real pastoral office, replace a local church, declare divine guidance, diagnose spiritual states, or handle crisis/abuse/medical/legal issues without referral boundaries.

## Action

- Created a proposal in `.agent-learning/proposals/2026-04-26-create-baptist-pastor.md`.
- Recommended `.opencode/agents/baptist-pastor.md` as the target filename.
- Recommended review by `christian-theology-researcher` and human/project owner before implementation.

## Follow-up

If approved, add the agent file and update orchestrator/organization routing. Future audits should verify that the agent remains Baptist-useful without weakening theological, pastoral, clinical, legal, or abuse-safety caveats.
