---
title: Report Caveat Standard
type: concept
tags: [before-we-build, reports, caveats, scripture-first, pastoral-boundaries]
created: 2026-05-13
updated: 2026-05-13
sources: [project-convention]
---

# Report Caveat Standard

This page defines the reusable caveat block for generated Before We Build reports: personal preparation maps, shared conversation maps, church-mediated review notes, and later audience-specific report formats.

The caveat must appear near the beginning of every generated report, before interpretive sections that name differences, tensions, unclear areas, or next steps. Short reports may use the compact version; longer reports should use the standard version and may repeat a one-sentence reminder near the end.

## Standard caveat block

```text
This report is not a verdict, a pastoral authority, or a promise of marriage, family, agreement, calling, or any guaranteed outcome.

It is a conversation aid: a way to pause, name what is clear, notice what is still unclear, and prepare for honest discussion before God.

Please read it in the light of Scripture, prayer, your church community, wise counsel, and personal responsibility. If the report touches painful, serious, or spiritually weighty matters, bring those questions to trusted mature believers, a pastor, or another appropriate counselor rather than carrying them alone.

Before We Build does not decide for you. It helps you ask better questions so that the next step can be taken humbly, truthfully, and responsibly.
```

## Compact caveat block

Use this when space is limited, such as summary cards or a short export.

```text
This is not a verdict, pastoral authority, or promise. It is a conversation aid to help you notice what is clear, what is unclear, and what should be brought before God with Scripture, prayer, church, wise counsel, and personal responsibility.
```

## One-sentence footer reminder

Use this near the end of longer reports if the report contains strong language about differences, risks, or next steps.

```text
Treat this map as an invitation to prayerful conversation and wise counsel, not as a decision made for you.
```

## What the caveat must protect

Every localized or audience-specific version must preserve these boundaries:

- Not a verdict: the report must not sound like a final yes/no decision about a person, pair, family, church role, team, or shared work.
- Not pastoral authority: the report must not replace Scripture, prayer, church, pastoral care, mature counsel, repentance, obedience, or responsibility before God.
- Not a promise: the report must not promise a spouse, family, match, agreement, calling, healing, compatibility, certainty, or guaranteed result.
- Not hidden motive-reading: the report may summarize answers and name uncertainty, but must not present AI guesses about motives, sin, readiness, or spiritual state as facts.
- Not pressure: the report must not push a person toward disclosure, pursuit, commitment, reconciliation, church role, or partnership without consent and wise human judgment.

## Tone rules

The caveat should sound warm and pastoral in posture without claiming pastoral office.

Prefer:

- “conversation aid”
- “pause before God”
- “what is clear / what is unclear”
- “honest discussion”
- “Scripture, prayer, church, wise counsel”
- “personal responsibility”
- “humble, truthful, responsible next step”

Avoid:

- legalistic liability language as the main tone;
- “AI disclaimer” language that sounds cold or corporate;
- psychology-first framing;
- “the report knows,” “the system sees,” or “the model determines”;
- any phrase that turns the caveat into a small-print escape hatch after making strong claims elsewhere.

## Localization notes for Russian and Ukrainian

The public Russian and Ukrainian versions should be translated naturally, not word-for-word. Keep the meaning close, but use church-familiar language.

Required meaning to preserve:

```text
This report is not a verdict, not pastoral authority, and not a promise. It is help for prayerful conversation: to see what is clear, name what is not yet clear, and bring the next step before God with Scripture, prayer, church, wise counsel, and personal responsibility.
```

Potential Ukrainian wording direction:

```text
Цей звіт — не вирок, не пастирська влада і не обіцянка. Це допомога для молитовної розмови: побачити, що вже зрозуміло, чесно назвати, що ще не ясно, і принести наступний крок перед Богом — зі Святим Письмом, молитвою, церквою, мудрою порадою та особистою відповідальністю.
```

Potential Russian wording direction:

```text
Этот отчёт — не вердикт, не пастырская власть и не обещание. Это помощь для молитвенного разговора: увидеть, что уже ясно, честно назвать, что ещё не ясно, и принести следующий шаг перед Богом — с Писанием, молитвой, церковью, мудрым советом и личной ответственностью.
```

Both localized drafts need native-speaker review before public use.

## Report-composer implementation rule

A report composer should attach one of these caveat blocks before any generated interpretation. If a report section later says “recommended,” “risk,” “concern,” “difference,” or “next step,” the surrounding copy must still keep the caveat true: the system offers questions and preparation, not certainty, spiritual judgment, or a decision.
