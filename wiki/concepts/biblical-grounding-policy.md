---
title: Biblical Grounding Policy
type: concept
tags: [christianity, editorial-policy, bible, claims, methodology]
created: 2026-04-26
updated: 2026-04-26
sources: []
---

# Biblical Grounding Policy

## Summary

Any PsyCalc / Cognitive Matchmaker page that makes a Christian normative claim about family, marriage, faith, forgiveness, community, moral discernment, or the spiritual limits of typology should include a nearby biblical grounding block.

**Biblical grounding for the policy:**

- **2 Timothy 3:16–17** — Scripture is useful for teaching, correction, and training in righteousness.
- **Acts 17:11** — claims should be examined against Scripture.
- **1 Thessalonians 5:21** — test everything and hold fast to what is good.

## Claims that require biblical grounding

**Claim:** Biblical grounding is required when a page says or implies what Christians should value, avoid, prioritize, or treat as spiritually primary.

Examples:

- marriage requires fidelity, responsibility, and forgiveness;
- Christian faith gives a foundation for family;
- typology must not become a spiritual verdict;
- compatibility scores must not replace wisdom, counsel, or discernment;
- church community should support rather than control people.

**Biblical grounding:**

- **Matthew 7:24–25** — foundations matter.
- **Colossians 3:12–14** — forgiveness and love are central in Christian relationships.
- **Proverbs 11:14** — counsel protects from isolated judgment.
- **2 Corinthians 4:2** — Christian communication must reject hidden and manipulative practices.

## Claims that usually do not require biblical grounding

**Claim:** Purely editorial, technical, descriptive, or research-methodological statements do not always require biblical grounding, unless they are used to make a Christian moral or spiritual point.

Examples:

- where a wiki page is stored;
- how frontmatter is formatted;
- that PsyCalc treats a mapping as a hypothesis;
- that a model requires empirical validation;
- that a page links to another page.

**Biblical grounding for the boundary:**

- **1 Corinthians 14:40** — work should be done decently and in order.
- **Proverbs 18:17** — claims still need examination when they become substantive.
- **1 Thessalonians 5:21** — testing remains the broader rule.

## Minimal required format

Each normative Christian claim should be followed by a short block:

```markdown
**Claim:** ...

**Biblical grounding:**

- **Book chapter:verses** — short explanation.
```

For strong claims, use two or three references rather than one.

## Language-specific Bible reference names

**Claim:** Bible book names and verse references must match the language of the page. Do not mix English, Russian, and Ukrainian Bible abbreviations in the same display text.

**Biblical grounding:**

- **1 Corinthians 14:9** — speech should be intelligible to its hearers.
- **1 Corinthians 14:40** — work should be done decently and in order.
- **Nehemiah 8:8** — Scripture was explained clearly so people could understand the reading.

### Display rule

- **EN pages** use English names/abbreviations: `1 Cor 13:4–7`, `Col 3:12–14`, `Matt 7:24–25`.
- **RU pages** use Russian names/abbreviations: `1 Кор 13:4–7`, `Кол 3:12–14`, `Мф 7:24–25`.
- **UK pages** use Ukrainian names/abbreviations: `1 Кор 13:4–7`, `Кол 3:12–14`, `Мт 7:24–25`.

Do not display mixed forms such as `1 Cor` on a Russian page, `Мф` on an English page, or `1 Фес` on a Ukrainian page.

### Canonical reference rule

For cross-language consistency, metadata may store a language-neutral identifier such as:

```yaml
bible_refs:
  - canonical_ref: 1-corinthians 13:4-7
    book_id: 1-corinthians
    chapter: 13
    verses: 4-7
    display: "1 Кор 13:4–7"
```

The body text should show only the localized `display` form appropriate to the page language.

### Common localized examples

| canonical_ref | EN display | RU display | UK display |
|---|---|---|---|
| `1-corinthians 13:4-7` | `1 Cor 13:4–7` | `1 Кор 13:4–7` | `1 Кор 13:4–7` |
| `colossians 3:12-14` | `Col 3:12–14` | `Кол 3:12–14` | `Кол 3:12–14` |
| `matthew 7:24-25` | `Matt 7:24–25` | `Мф 7:24–25` | `Мт 7:24–25` |
| `ecclesiastes 4:9-12` | `Eccles 4:9–12` | `Еккл 4:9–12` | `Екл 4:9–12` |
| `1-thessalonians 5:21` | `1 Thess 5:21` | `1 Фес 5:21` | `1 Сол 5:21` |

## Common reference map

- Love over mere compatibility: **1 Corinthians 13:4–7**, **Colossians 3:14**, **John 13:34–35**.
- Marriage as covenantal union: **Genesis 2:24**, **Matthew 19:4–6**, **Ephesians 5:21–33**.
- Forgiveness and repair: **Colossians 3:13**, **Ephesians 4:31–32**, **Matthew 18:15**.
- Community and counsel: **Hebrews 10:24–25**, **Proverbs 11:14**, **Ecclesiastes 4:9–12**.
- Testing human claims: **1 Thessalonians 5:21**, **Acts 17:11**, **Proverbs 18:17**.
- Human dignity beyond type: **Genesis 1:26–27**, **Psalm 139:13–14**, **1 Samuel 16:7**.
- Humility against typological pride: **Romans 12:3**, **Philippians 2:3–4**, **James 2:1**.
- No guarantee of outcomes: **James 4:13–15**, **Proverbs 16:9**, **Proverbs 19:20–21**.

## Editorial rule

If a sentence sounds like “from a Christian point of view, this is true / important / forbidden / primary,” add biblical grounding near it. If the text is only a technical or research note, grounding is optional but still welcome when it affects moral or spiritual interpretation.
