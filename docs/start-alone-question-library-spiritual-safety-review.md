# Start Alone Question Library Spiritual Safety Review

**Project:** Before We Build  
**Reviewed artifact:** `docs/start-alone-question-library-v0.md`  
**Review date:** 2026-05-13  
**Reviewer profile:** spiritual safety / conservative Scripture-first reception

## 1. Overall verdict

**Verdict:** NEEDS_LIGHT_REVISION_BEFORE_PUBLICATION

The library is broadly safe in posture: it is Scripture-first, avoids compatibility scores and ideal-match claims, repeatedly points to prayer, Scripture, church, wise counsel, personal responsibility, and keeps the result framed as a map for conversation rather than a verdict.

No question should be fully rejected. Several questions should be softened before public use because they could be heard as spiritual pressure, surveillance by church/family, doctrinal teaching by the tool, or a prompt that pushes a lonely person toward action faster than wisdom.

## 2. Review gates

| Gate | Result | Notes |
|---|---|---|
| Manipulative wording | PASS_WITH_REWRITES | Some wording uses pressure-shaped forms such as “are you willing,” “what would need to change,” or “only comfort and companionship.” Rewrite to invite examination rather than force a preferred answer. |
| Extra-biblical authority claims | PASS_WITH_PASTOR_CHECK | The draft does not claim authority for the tool, but husband/wife roles, calling, repentance, forgiveness, and family healing require careful church-context wording. |
| AI-as-discernment replacement tone | PASS | The library explicitly says the tool must not discern God’s will, judge readiness, or replace Scripture/prayer/church/counsel. Keep that caveat visible in implementation. |
| Conservative Scripture-first reception | PASS_WITH_REWRITES | Strong overall. Public UI should remove internal English labels and keep the caveat close to generated maps. |
| Privacy/consent | PASS_WITH_IMPLEMENTATION_REQUIREMENT | Line 23 is good: “nothing is shared automatically.” Implementation must preserve private answers, explicit export/share only, and no automatic disclosure to mentors/churches. |

## 3. Required global implementation guardrails

Before these questions become public or app-facing:

1. Show a short caveat before and after the question set:
   > These questions are help for prayerful reflection and honest conversation, not a verdict, not a promise, and not a replacement for Scripture, prayer, church, wise counsel, repentance, or personal responsibility.

2. Keep answers private by default. Sharing with a pastor, mentor, parent, church leader, or another person must be explicit, voluntary, and reversible where possible.

3. Do not rank, score, or color-code people by spiritual readiness, marriage readiness, repentance, teachability, purity, or family fit.

4. Do not let an AI summary infer hidden motives. It may say “you mentioned fear of rejection” if the user wrote that; it must not say “your real motive is fear of rejection.”

5. If answers mention abuse, coercion, serious danger, or self-harm, stop ordinary relationship advice and point toward safe human help. Do not spiritualize endurance under coercion.

6. In Ukrainian/Russian public UI, do not show internal English answer labels like `clear_to_me` or `unclear_or_needs_counsel`. Translate them into natural phrases or keep them internal only.

## 4. Question-by-question review

Legend:
- APPROVED: safe as written for draft use.
- APPROVED_WITH_NOTE: safe if implemented with the stated caveat.
- REWRITE: should be changed before public use.
- PASTOR_CHECK: not necessarily unsafe, but touches doctrine/church tradition and should be reviewed by trusted church leadership before publication.
- REJECTED: should not be used. No questions are rejected in this review.

| # | Status | Issue / risk | Safer wording or note |
|---:|---|---|---|
| 1 | APPROVED | Good foundation before God; does not promise certainty. | Keep. |
| 2 | APPROVED_WITH_NOTE | “Which Scripture truths” is good, but implementation should not pretend to interpret Scripture for the user. | Keep; optionally add “you already know or want to study with counsel.” |
| 3 | APPROVED_WITH_NOTE | “Where do you need God to search your heart” is biblically recognizable, but could feel heavy if the UI later scores it. | Keep only as private reflection. Do not generate a “heart condition” verdict. |
| 4 | APPROVED | Good Scripture-conviction boundary. | Keep. |
| 5 | REWRITE | “may need patience or surrender” is spiritually plausible but can pressure lonely users into treating ordinary desire for marriage/family as suspect. | “What hope for marriage or family can you name honestly before God, and where might that hope need patience, wisdom, or counsel?” |
| 6 | APPROVED_WITH_NOTE | Good warning against haste; risk of shaming loneliness if repeated bluntly. | Keep with gentle surrounding text: loneliness is a real burden, not a sin by itself. |
| 7 | APPROVED | Names fears without diagnosing them. | Keep. |
| 8 | APPROVED | Good source-of-expectations question. | Keep. |
| 9 | APPROVED | Character growth without scoring. | Keep. |
| 10 | REWRITE | “Where might you need repentance, apology, or change” is direct and good, but can create false guilt if presented as required. | “Is there any area where repentance, apology, wise counsel, or change may be needed before you enter a serious relationship?” |
| 11 | APPROVED | Good teachability question; grounded in trusted believers, not anonymous authority. | Keep. |
| 12 | APPROVED | Practical responsibility question. | Keep. |
| 13 | APPROVED_WITH_NOTE | Safe if “parents” remains optional; some users have unsafe, controlling, absent, or non-Christian family contexts. | Keep; implementation should let users skip categories that are unsafe or not relevant. |
| 14 | REWRITE | “What would your church community already know...” can sound like surveillance or public reputation management. | “What might mature believers who know you well be able to help you see about your walk with God, service, habits, or relationships?” |
| 15 | REWRITE | “Are you willing” can pressure the user toward a yes answer. | “What wise counsel would be helpful before making serious promises, rather than waiting until problems appear?” |
| 16 | APPROVED | Good anti-gossip, anti-pressure, anti-control wording. | Keep. |
| 17 | REWRITE | “only comfort and companionship, or also...” creates a loaded answer and may shame good desires for companionship. | “What do you believe marriage is for before God: companionship, covenant faithfulness, service, holiness, shared responsibility, and other goods you should name clearly?” |
| 18 | APPROVED | Practical and non-manipulative. | Keep. |
| 19 | APPROVED | Good ordinary-life love question. | Keep. |
| 20 | REWRITE + PASTOR_CHECK | Husband/wife, leadership, support, and decisions are doctrine-sensitive. The tool must not teach disputed positions or appear to settle church differences. | “What expectations about husband and wife, leadership, support, and shared decisions should be discussed carefully with Scripture, wise counsel, and your church context in view?” |
| 21 | APPROVED_WITH_NOTE | The answer options are useful, but “attack” can sound harsh. | Keep or soften to “speak sharply.” Do not label the person by one answer. |
| 22 | APPROVED_WITH_NOTE | Very important, but forgiveness wording must not imply remaining in danger or excusing abuse. | Keep; implementation should clarify that forgiveness does not mean hiding coercion, abuse, or ongoing danger. |
| 23 | APPROVED | Good prevention of bitterness/silence/conflict. | Keep. |
| 24 | REWRITE | “Past patterns of conflict” may draw out trauma or sensitive history; needs safe framing. | “Are there any past conflict patterns you want to bring carefully to prayer, wise counsel, or future conversation before marriage?” |
| 25 | APPROVED | Practical, non-scoring. | Keep. |
| 26 | APPROVED | Good practical conversation prompt. | Keep. |
| 27 | APPROVED | Good before-God framing; allows multiple meanings rather than enforcing one. | Keep. |
| 28 | REWRITE | “what would need to change” may feel like a hidden readiness test. | “How do you spend your time now, and what changes might be wise if you were preparing for shared life with someone?” |
| 29 | APPROVED | Good service/responsibility prompt. | Keep. |
| 30 | APPROVED_WITH_NOTE | Strong built-in caveat against pressuring another person. | Keep. |
| 31 | APPROVED | Good sacrifice/adjustment prompt. | Keep. |
| 32 | REWRITE + PASTOR_CHECK | “real calling” can overclaim or make the tool sound able to validate calling. | “Where do you need to distinguish between a settled responsibility, a personal preference, and a dream that still needs prayer, testing, and counsel?” |
| 33 | APPROVED_WITH_NOTE | Good if it avoids assuming children are guaranteed. | Keep with the existing note: where God gives children, not as a promise. |
| 34 | REWRITE | “repentance, boundaries, or healing” near upbringing can imply the user is guilty for family wounds. | “What family patterns from your upbringing would you want to continue, and what patterns may need wisdom, boundaries, counsel, healing, or, where it is truly yours, repentance?” |
| 35 | APPROVED_WITH_NOTE | Good broad family discussion prompt. | Keep; include non-Christian/unsafe-family sensitivity in implementation. |
| 36 | APPROVED | Good purity/consent framing without graphic detail. | Keep. |
| 37 | REWRITE | Could be heard as pushing a fearful person to act. | “How might you tell the difference between wise patience, unwise delay, and fear that should be brought to prayer or counsel?” |
| 38 | APPROVED | Explicitly sends topics to prayer, Scripture, and wise counsel. | Keep. |
| 39 | APPROVED | Concrete next step without haste; good list includes pause and counsel. | Keep. |

## 5. Optional short first set review

| Short-set # | Status | Note / rewrite |
|---:|---|---|
| 1 | REWRITE | “asking God to make clear” could sound like guaranteed certainty. Safer: “What do you need to bring before God before you move toward a serious relationship?” |
| 2 | APPROVED_WITH_NOTE | Same as Q6: keep loneliness gentle, never shame it. |
| 3 | APPROVED | Safe. |
| 4 | APPROVED | Safe. |
| 5 | APPROVED | Safe. |
| 6 | APPROVED | Safe. |
| 7 | APPROVED | Safe. |
| 8 | APPROVED | Safe. |

## 6. Summary counts

- Approved as written: 19 main questions.
- Approved with implementation notes: 9 main questions.
- Rewrite before publication: 11 main questions.
- Pastor/church-context check recommended: 2 main questions.
- Rejected: 0 main questions.

Short first set:
- Approved as written: 6.
- Approved with note: 1.
- Rewrite before publication: 1.
- Rejected: 0.

## 7. Recommended publication decision

Do not publish the question set exactly as v0. Publish after applying the 11 main-question rewrites and the first short-set rewrite above, while keeping the global caveat visible.

The library can proceed to the next planning card after these notes are accepted because the issues are wording-level and implementation-boundary issues, not a failure of the overall concept.
