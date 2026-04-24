---
title: Civilian Career Role Families
type: source
tags: [career, civilian, roles, esco, typology, advisor]
created: 2026-04-24
updated: 2026-04-24
sources: [.opencode/data/civilian-career-roles.md, wiki/concepts/esco-typology-mapping.md]
---

# Civilian Career Role Families

This page ingests the shared role-family catalog used by `civilian-career-advisor`. It is a practical mapping layer between typological signals, ESCO-style work features, and civilian career recommendations.

The catalog is not an exhaustive labor-market database. It is used to generate **role-fit hypotheses** that must be checked against real skills, portfolio evidence, credentials, location, salary needs, and current vacancies.

## Work Feature Tags

- `tech-heavy`
- `people-heavy`
- `structure-heavy`
- `stress-heavy`
- `hands-on`
- `analysis-heavy`
- `coordination-heavy`
- `autonomy-high`
- `autonomy-low`
- `long-horizon`
- `routine-heavy`
- `sales-heavy`
- `care-heavy`
- `field-heavy`
- `creative-heavy`

## Role Families

| Role family | Core features | Good signals | Main risks |
|-------------|---------------|--------------|------------|
| DevOps / SRE / Platform Engineering | `tech-heavy`, `structure-heavy`, `analysis-heavy`, `stress-heavy`, `long-horizon`, `coordination-heavy` | systems thinking, practical diagnostics, operational responsibility | alert fatigue, unclear ownership, chaotic on-call culture |
| Systems / Network / Cloud Administration | `tech-heavy`, `structure-heavy`, `hands-on`, `analysis-heavy`, `routine-heavy` | maintenance mindset, precision, patience with infrastructure | repetitive tickets, legacy systems, after-hours incidents |
| Cybersecurity Operations | `tech-heavy`, `analysis-heavy`, `stress-heavy`, `structure-heavy`, `long-horizon` | calm under pressure, pattern detection, disciplined process | shift work, alert overload, adversarial pressure |
| Data / BI / Operations Analysis | `analysis-heavy`, `structure-heavy`, `tech-heavy`, `coordination-heavy` | metrics, explanation, structured thinking | stakeholder ambiguity, low data quality, repetitive reporting |
| QA / Test Automation | `tech-heavy`, `structure-heavy`, `analysis-heavy`, `routine-heavy` | consistency, defect detection, practical logic | low autonomy, undervalued gatekeeper role, monotonous cycles |
| Technical Writing / Documentation | `structure-heavy`, `analysis-heavy`, `coordination-heavy`, `creative-heavy` | explanatory logic, clarity, continuity preservation | low feedback, SME dependence, less hands-on technical work |
| Technical Project / Release / Operations Management | `coordination-heavy`, `structure-heavy`, `stress-heavy`, `people-heavy`, `long-horizon` | structured communication, planning, cross-team translation | politics, status games, meeting overload, accountability without authority |
| Implementation / Solutions Engineering | `tech-heavy`, `people-heavy`, `coordination-heavy`, `analysis-heavy` | technical explanation, practical adaptation, bounded client contact | sales pressure, emotional labor, unclear scope |
| Technical Support / Customer Success Engineering | `people-heavy`, `tech-heavy`, `stress-heavy`, `care-heavy`, `coordination-heavy` | patience, explanation, technical empathy | emotional pressure, angry users, low control over product issues |
| Training / Instruction / Mentoring | `people-heavy`, `structure-heavy`, `creative-heavy`, `care-heavy` | explanatory ability, emotional tone-setting, patience | audience management, repetitive basics, unstable demand |
| Logistics / Operations Coordination | `coordination-heavy`, `structure-heavy`, `hands-on`, `stress-heavy`, `routine-heavy` | practical organization, continuity, reliability | time pressure, interruptions, low strategic autonomy |
| Field / Hardware / Industrial Technician | `hands-on`, `field-heavy`, `tech-heavy`, `stress-heavy`, `routine-heavy` | practical sensing, real-world troubleshooting, material systems | travel, physical load, weather or site constraints |
| Product / Business Analysis | `analysis-heavy`, `people-heavy`, `coordination-heavy`, `long-horizon`, `structure-heavy` | user-to-technical translation, process mapping | ambiguity, politics, constant reprioritization |
| Sales / Business Development | `sales-heavy`, `people-heavy`, `stress-heavy`, `autonomy-high` | drive, social assertiveness, status tolerance | rejection, quotas, performative confidence |
| Care / Psychology / Social Support | `care-heavy`, `people-heavy`, `stress-heavy`, `long-horizon` | emotional steadiness, ethical attention, patience | compassion fatigue, boundary load, institutional pressure |

## Use In Career Matching

1. Gather typology profile: Socionics, Psychosophy, Temporistics.
2. Gather civil background: current work, tools, portfolio, education, constraints.
3. Convert candidate roles into work-feature tags.
4. Match role features to typological signals and proven work history.
5. Rank recommendations by confidence.

## Confidence Levels

- **High confidence:** typology, proven background, and role-family features all align.
- **Medium confidence:** typology aligns, but proof of skill or market fit is partial.
- **Low confidence:** interesting experiment, but requires a trial project, retraining, or strong external validation.

## Important Caveat

Typology should not override observed performance. Proven skills, work history, constraints, and market demand are stronger evidence than type-based inference.

## See Also

- [[esco-typology-mapping]]
- [[composite-profile-sli-elvf-vpnb]]
- [[smart-mobilization-research-note]]
