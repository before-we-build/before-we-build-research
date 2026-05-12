# MVP Cost Estimation (Illustrative)

**Last Updated:** 2026-05-12

This file replaces the older simulation-heavy MVP estimate. The near-term MVP no longer assumes digital twins, 100 scenarios, or multi-agent relationship simulation.

The first product is a weak-AI conversation tool:

```text
question flow + answer summary + conversation map + follow-up questions
```

---

## MVP Scope

### MVP-1: Personal Preparation Map

Included:

- 20–40 question flow;
- save/resume answers;
- AI-assisted answer summary;
- missing-topic detection;
- follow-up question generation;
- plain-language report;
- optional export for mentor/pastor review.

Not included:

- digital twins;
- candidate search;
- scenario simulation;
- compatibility scoring;
- weekly shortlist;
- autonomous concierge actions.

---

## Cost Model

The main cost is ordinary summarization and report generation, not repeated simulation.

### Per single-person session

Approximate token shape:

- User answers: 3,000–8,000 input tokens.
- System instructions and question metadata: 1,000–3,000 input tokens.
- Summary/report output: 1,000–2,500 output tokens.
- Follow-up questions: 500–1,000 output tokens.

Expected LLM calls:

1. normalize answers;
2. identify missing topics;
3. compose report;
4. generate follow-up questions.

This is small enough to run on a low-cost model with optional stronger-model review for sensitive cases.

---

## Pair Mode Cost Model

### MVP-2: Shared Conversation Map

Approximate token shape:

- Person A answers: 3,000–8,000 tokens.
- Person B answers: 3,000–8,000 tokens.
- Theme comparison: 2,000–4,000 tokens.
- Report output: 1,500–3,000 tokens.

Expected LLM calls:

1. normalize A;
2. normalize B;
3. compare by themes;
4. compose shared conversation map;
5. generate questions and review flags.

Still far cheaper than simulation because the model is not running dozens of multi-turn conversations.

---

## Optional Human Review Cost

The serious cost for a Christian product is not only tokens. It is review:

- copy review for Scripture-first framing;
- pastor/mentor review for sensitive claims;
- privacy and consent review;
- support for confused or distressed users.

The MVP should budget time for human review before adding automation.

---

## Deferred Research Cost

The following old cost categories are explicitly deferred:

- persona-generator for digital twins;
- persona-cloner / GNWT-style weights;
- simulation-runner;
- choice-tracker;
- observer-agent scoring;
- repeated scenario batches.

If the project later reopens supervised simulations, create a new estimate based on current model pricing and measured usefulness of the simpler product.

---

## Cost-Control Rules

1. Do not run simulations in MVP-1 or MVP-2.
2. Use small models for drafting summaries.
3. Use stronger models only for review of sensitive reports.
4. Cache normalized answers and generated reports.
5. Prefer deterministic rules for obvious flags before calling an LLM.
6. Keep output humble: no expensive model can justify an unsupported verdict.
