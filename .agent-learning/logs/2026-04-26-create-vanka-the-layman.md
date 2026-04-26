---
title: Create Vanka the Layman Agent
type: agent-learning-log
created: 2026-04-26
updated: 2026-04-26
source: user-request
status: implemented
---

# Learning Log: Create Vanka the Layman Agent

## Trigger

The user explicitly requested creation of a new expert agent called **Vanka the Layman**.

## Observation

The explanation team has agents for plain-language translation, storytelling, skeptical framing, presentations, and visual explanations. It lacked a deliberately blunt ordinary-person reviewer whose purpose is to test whether a complex idea feels understandable, useful, and worth caring about to a tired non-expert reader.

## Decision

This is a low-to-moderate risk additive agent instruction change. The agent is constrained to layperson comprehension review and does not validate truth, science, typology, ethics, theology, clinical matters, or statistics.

## Action

- Create `.opencode/agents/vanka-the-layman.md`.
- Add governance proposal and lightweight review records.
- Update `.opencode/agents/master-orchestrator.md` routing so public-understandability checks can be delegated to this agent.

## Follow-up

Future audits should verify that the agent remains practical and blunt without becoming insulting, anti-intellectual, or unsafe, and that it does not remove necessary caveats for the sake of simplicity.
