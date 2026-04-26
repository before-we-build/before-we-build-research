---
title: Biblical Claim Audit Skill for Baptist Pastor
type: agent-improvement-proposal
created: 2026-04-26
updated: 2026-04-26
status: applied
risk: high-risk
target_agents: [".opencode/agents/baptist-pastor.md"]
target_skills: [".opencode/skills/biblical-claim-audit.md"]
required_reviewers: ["christian-theology-researcher", "human/project owner"]
sources: ["user request", "AGENTS.md", ".opencode/agents/baptist-pastor.md", ".opencode/agents/christian-theology-researcher.md"]
---

# Agent Improvement Proposal: Biblical Claim Audit Skill for Baptist Pastor

## 1. Target agent(s)

- `.opencode/agents/baptist-pastor.md`
- `.opencode/skills/biblical-claim-audit.md`

## 2. Observed failure or opportunity

The user explicitly requested a reusable skill for `baptist-pastor` called **Biblical Claim Audit** with detailed workflow and output format.

The requested skill intent is to audit Christian/Baptist-facing content by:

- extracting claims;
- classifying claim types;
- checking Scripture and context;
- applying a Baptist lens;
- assigning verdicts;
- rewriting weak or unsafe claims;
- adding anti-proof-texting safeguards.

## 3. Evidence

- Audit/task result: direct user request in the current task.
- File/page references: `.opencode/agents/baptist-pastor.md` has broad review guidance, but no dedicated skill workflow.
- Source or policy references: `AGENTS.md` requires controlled self-improvement workflow and specialist review for Christian theology/pastoral caveats.

## 4. Proposed instruction change

Add a skill file defining the Biblical Claim Audit workflow and add a narrow activation note to `baptist-pastor`.

Core rules:

```md
- Extract discrete claims before judging them.
- Classify each claim as biblical quotation/paraphrase, doctrinal inference, Baptist distinctives/church-practice claim, pastoral application, ethical counsel, testimony/experience, historical/background claim, or speculative claim.
- Check Scripture in context: immediate context, genre, redemptive/covenantal setting, whole-Bible theology, and translation/quotation accuracy.
- Apply a Baptist lens while distinguishing direct biblical teaching, mainstream Baptist interpretation, intramural Baptist disagreement, and local-church policy.
- Assign verdicts using cautious categories.
- Rewrite unsupported, overbroad, or proof-texted claims.
- Do not weaponize Scripture or replace local pastoral, clinical, legal, civil, or emergency help.
```

## 5. Risk assessment

- Risk level: `high-risk`
- Why: The skill affects theological/pastoral claims and could be misused to overstate biblical certainty or pressure users with Scripture.
- Could this increase overclaiming? `yes`, if verdicts are too confident; mitigated by cautious verdict labels and review/referral rules.
- Could this bypass specialist delegation? `yes`, if treated as final doctrine; mitigated by requiring `christian-theology-researcher` review for disputed, high-stakes, cross-tradition, or public-facing claims.
- Could this affect high-stakes advice? `yes`, especially abuse, crisis, mental health, family/church discipline, and legal contexts; mitigated by explicit referral boundaries.

## 6. Required reviewers

- [ ] `empirical-claims-caveats-reviewer`
- [ ] `source-provenance-auditor`
- [ ] `alias-canonical-naming-steward`
- [x] domain specialist: `christian-theology-researcher`
- [x] human/project owner via explicit implementation request

## 7. Patch sketch

```diff
++ .opencode/skills/biblical-claim-audit.md
+---
+name: biblical-claim-audit
+description: Skill specification for Baptist Pastor to audit biblical/theological claims...
+risk: high
+requires_approval: false
+---
+# Biblical Claim Audit Skill
+...

++ .opencode/agents/baptist-pastor.md
+# Available Skills
+## Biblical Claim Audit
+Use `.opencode/skills/biblical-claim-audit.md` when asked to audit biblical/theological claims...
```

## 8. Acceptance criteria

- [x] The new rule is narrow and enforceable.
- [x] It does not weaken caveats.
- [x] It preserves delegation-first routing.
- [x] It cites the relevant source/policy/audit finding.
- [x] It can be checked in a future audit.

## 9. Rollback note

Remove `.opencode/skills/biblical-claim-audit.md` and delete the `Biblical Claim Audit` section from `.opencode/agents/baptist-pastor.md` if the skill causes overconfident doctrine, proof-texting, or unsafe pastoral advice.
