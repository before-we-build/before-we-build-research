---
title: PsyCalc Agentic Research Validation Pipeline
type: protocol
created: 2026-04-25
updated: 2026-04-25
status: draft
sources: [AGENTS.md]
---

# PsyCalc Agentic Research Validation Pipeline

## Goal

Create a review-gated multi-agent workflow for collecting, cleaning, analyzing, and reporting empirical evidence related to PsyCalc hypotheses.

## Core Rule

Agents may automate research labor, but they may not autonomously convert hypotheses into validated claims.

## Standard Flow

```text
human owner
  -> research-orchestrator
  -> experiment-designer
  -> psychometrics-methodologist
  -> ethics-and-consent-reviewer
  -> data-pipeline-engineer
  -> statistical-validation-agent
  -> scoring-calibration-researcher
  -> source-provenance-auditor
  -> empirical-claims-caveats-reviewer
  -> human approval
```

## Required Artifacts

Each study should produce:

1. `research-question.md`
2. `preregistration.md`
3. `consent-text.md`
4. `data-schema.md`
5. `codebook.md`
6. `quality-checks.md`
7. `analysis-plan.md`
8. `exclusion-log.csv` or equivalent
9. `results-report.md`
10. `limitations.md`

## Evidence Labels

- `primary-source`
- `secondary-source`
- `project-synthesis`
- `hypothesis`
- `empirical-result`
- `statistical-model-output`
- `simulation-output`
- `unsupported`

## Human Approval Required

- Launching studies or recruitment.
- Contacting participants.
- Collecting sensitive or behavioral data.
- Submitting preregistration.
- Excluding data from confirmatory analysis after inspection.
- Publishing reports.
- Changing scoring weights.
- Updating agent instructions.

## Output Standard

Final research packets must distinguish:

- preregistered findings;
- exploratory findings;
- unsupported hypotheses;
- limitations;
- replication needs;
- production implications, if any.
