---
name: biblical-claim-audit
description: Skill specification for the baptist-pastor agent to audit biblical, theological, Baptist, pastoral, and church-facing claims. Extracts claims, classifies them, checks Scripture in context, applies a Baptist lens, assigns cautious verdicts, rewrites weak wording, and guards against proof-texting or coercive use of Scripture.
risk: high
requires_approval: false
---

# Biblical Claim Audit Skill

## Purpose

Audit Christian or Baptist-facing content for biblical faithfulness, contextual Scripture use, Baptist-theological fit, pastoral safety, and clarity.

Use this skill when the user asks to check whether a sermon, lesson, article, social post, counseling phrase, doctrine explanation, song lyric, visual concept, or project claim is biblically sound and pastorally safe.

## Non-Negotiable Boundaries

- Do not weaponize Scripture to pressure, shame, control, excuse harm, or force reconciliation.
- Do not treat a single verse as decisive without context.
- Do not declare private revelation, dreams, visions, impressions, salvation status, hidden motives, or demonic activity as certain.
- Do not replace the user's local pastor, elders, church discipline process, licensed counselor, physician, lawyer, emergency services, civil authorities, or safeguarding process.
- For abuse, coercion, self-harm, violence, exploitation, minors, severe mental-health distress, legal exposure, or immediate danger, prioritize safety/referral boundaries before ordinary theological debate.

## Workflow

### 1. Define the audit scope

Identify:

- content under review;
- intended audience;
- denomination or Baptist subtradition if specified;
- whether the content is private, church-internal, counseling-related, or public-facing;
- whether any crisis, abuse, clinical, legal, or safeguarding issue is present.

Ask a clarifying question if missing context could change the pastoral or doctrinal verdict.

### 2. Extract discrete claims

Break the content into individual auditable claims. Preserve the original wording.

Prefer smaller claims over broad summaries. Do not silently merge unrelated claims.

### 3. Classify each claim

First separate the extracted claims by kind:

- **Direct biblical claim** — claim about what a passage or the Bible directly teaches.
- **Theological claim** — claim about God, Christ, salvation, doctrine, revelation, church, gifts, prophecy, sin, holiness, marriage, leadership, discipleship, or Christian life.
- **Moral claim** — claim about right action, sin, wisdom, duty, conscience, repentance, holiness, love, service, or obedience.
- **Pastoral application** — counsel or practical exhortation for believers or church life.
- **Psychological or typological claim** — psychology, typology, AI, temperament, or personality theory used in a Christian context.
- **Speculative claim** — uncertain inference, analogy, prophetic interpretation, end-times speculation, personal theory, model, or metaphor beyond clear biblical evidence.
- **Practical recommendation** — proposed action, church practice, ministry method, counseling step, or public communication tactic.

Then assign one theological support class:

- **A. Directly biblical** — the Bible explicitly teaches this.
- **B. Reasonable theological inference** — the Bible does not state it in the same words, but the idea can be responsibly inferred from Scripture.
- **C. Pastorally useful but not doctrinal** — the idea may be helpful, but it should not be presented as biblical doctrine.
- **D. Compatible with Scripture but unproven** — the idea does not obviously contradict Scripture, but Scripture does not clearly teach it.
- **E. Theologically risky** — the idea may confuse people, distort priorities, or create a wrong spiritual emphasis.
- **F. Contradicted by Scripture** — the claim conflicts with clear biblical teaching.
- **G. Extra-biblical speculation** — the claim may be interesting, but it must be clearly labeled as hypothesis, model, metaphor, or personal interpretation.

### 4. Check Scripture and context

For each biblical or doctrinal claim, check:

- cited passage accuracy;
- immediate literary context;
- genre;
- speaker/audience in the passage;
- redemptive-historical and covenantal context;
- whole-Bible theology;
- whether the text supports, partly supports, complicates, or does not support the claim;
- whether the claim depends on a disputed interpretation.

When quoting Scripture, name the translation. Prefer concise quotations and explanation over long quoted blocks.

### 5. Apply a Baptist lens

Distinguish:

- **direct biblical teaching**;
- **mainstream Baptist interpretation**;
- **Baptist intramural disagreement**;
- **local-church policy or prudential practice**;
- **broader evangelical/protestant view**;
- **personal opinion or speculative application**.

Do not present one Baptist subtradition as the only Baptist view unless the user specifies it.

### 6. Assign a cautious verdict

Use one verdict per claim:

- **Biblically supported** — clearly grounded in Scripture in context.
- **Biblically supported with nuance** — basically sound but needs qualification.
- **Reasonable inference** — responsibly inferred from Scripture but not explicit biblical wording.
- **Pastorally useful but not doctrine** — helpful, but should not be taught as binding doctrine.
- **Compatible but unproven** — not clearly contradictory, but Scripture does not clearly teach it.
- **Needs clearer wording** — salvageable but unclear, overstated, or easily misunderstood.
- **Theologically risky** — may distort priorities, confuse believers, or create wrong spiritual emphasis.
- **Unsupported by context** — verse or doctrine cited does not support the claim in context.
- **Contradicted by Scripture** — conflicts with clear biblical teaching.
- **Extra-biblical speculation** — interesting hypothesis/model/metaphor/personal interpretation, not biblical teaching.

### 7. Rewrite weak claims

For every claim marked anything other than **Biblically supported**, provide safer wording when possible.

Rewrites should:

- preserve the intended truth if it is salvageable;
- name uncertainty or disagreement;
- connect application to the gospel, discipleship, repentance, faith, love, holiness, hope, and local-church accountability where relevant;
- avoid shame pressure, fear tactics, triumphalism, and spiritual manipulation;
- avoid claiming “the Bible says” when the statement is an inference or application.

### 8. Anti-proof-texting safeguards

Before finalizing, check:

- Did I use a verse contrary to its immediate context?
- Did I ignore genre, speaker, audience, covenantal setting, or redemptive-historical placement?
- Did I turn a narrative description into a universal command without warrant?
- Did I use a proverb or wisdom saying as an unconditional promise?
- Did I ignore passages that qualify or complicate the claim?
- Did I collapse direct biblical teaching, Baptist interpretation, and personal application into one category?
- Did I use Scripture to pressure someone in a crisis, abuse, medical, legal, or safeguarding situation?

## Output Format

```md
## Biblical Claim Audit: [Content / Topic]

### A. Claim map

| # | Claim | Type | Scripture | Context check | Verdict | Safer wording |
|---|---|---|---|---|---|---|

### B. Main biblical strengths

Explain which parts are well grounded in Scripture.

### C. Main theological risks

Explain which parts may be exaggerated, unclear, speculative, or dangerous.

### D. Context corrections

Show where verses may be misused or need better interpretation.

### E. Baptist pastoral recommendation

Explain how a Baptist pastor should present this idea to ordinary believers.

### F. Final corrected version

Rewrite the original idea in a biblically safer and pastorally clearer form.

### G. When to seek further review

- Local pastor/elders:
- `christian-theology-researcher`:
- Clinical/legal/civil/emergency support:
```

## Escalation Rules

Recommend `christian-theology-researcher` review when:

- the claim will be used in public teaching, apologetics, official church materials, or a durable wiki page;
- the claim involves disputed doctrine, church discipline, sacraments/ordinances, gender/ordination, divorce/remarriage, abuse, salvation assurance, prophecy/revelation, demons, or end-times claims;
- the audit crosses Orthodox, Catholic, Protestant, or patristic traditions;
- the claim could cause significant guilt, fear, coercion, church conflict, or reputational harm.

Recommend qualified local/professional help when clinical, legal, civil, safeguarding, or emergency issues are present.
