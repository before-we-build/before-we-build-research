---
title: Remove Typology-Based Career and Military Assignment
type: agent-improvement-proposal
created: 2026-08-30
updated: 2026-08-30
status: approved
risk: high
target_agents: [civilian-career-advisor, military-specialty-advisor, master-orchestrator]
required_reviewers: [human-project-owner, ethics-and-consent-reviewer, empirical-claims-caveats-reviewer, military-domain-reviewer]
sources: [user-approved-repository-clarity-plan-2026-08-30, AGENTS.md]
---

# Agent Improvement Proposal: Remove Typology-Based Role Assignment

## Observed failure

Active instructions ranked professions from type codes and recommended military specialties by alleged typological strengths, pressure tolerance, or order-following. No validated occupational or military outcome model supports those inferences. The military workflow affects safety and opportunity and is therefore especially unsuitable for exploratory typology.

## Approved instruction change

- Rebuild civilian career guidance around qualifications, work samples, observed outcomes, constraints, accommodations, preferences, and current role requirements.
- Allow typology only as an explicitly optional source of a question after direct evidence, never as ranking evidence.
- Rebuild military role guidance around current official information, lawful process, verified competence, medical and safety requirements where appropriate, and informed preference.
- Prohibit typology from military selection, exclusion, assignment, resilience claims, or suitability estimates.
- Remove high/medium/low confidence derived from agreement among type systems.

## Risk assessment

- Risk level: `high`, because the old instructions could affect employment, military placement, health, and safety.
- The patch reduces authority and false confidence; it does not create a new decision model.
- Current role information remains subject to verification by the military-role researcher and responsible human authorities.

## Acceptance criteria

- [x] No active agent maps a type code to an occupation or military specialty.
- [x] Career output separates evidence, preferences, uncertainty, and next tests.
- [x] Military output never uses typology as a selection or assignment criterion.
- [x] Agent routing describes both roles consistently.

## Rollback

Do not restore type-based role assignment from history. A future occupational measure would require a separate validated construct, external review, fairness and safety evidence, and explicit owner approval; military use would require additional lawful and domain-specific authorization.
