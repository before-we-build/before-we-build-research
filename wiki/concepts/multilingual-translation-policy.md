---
title: Multilingual Translation Policy
type: concept
tags: [policy, multilingual, translation, wiki, conventions]
created: 2026-04-26
updated: 2026-04-26
lang: en
canonical: multilingual-translation-policy.md
sources: []
---

# Multilingual Translation Policy

This page defines the first practical multilingual convention for the PsyCalc wiki.

## Status

This is a **project policy** for wiki maintenance. It does not change the epistemic status of typology claims. All typology mappings in every language remain **heuristic**, **hypothesis-level**, and **non-deterministic** unless explicitly supported otherwise.

## File Naming

- Canonical English/default page: `page.md`
- Russian translation: `page-ru.md`
- Ukrainian translation: `page-uk.md`
- Do **not** create `*-en.md` files for now.

Examples:

- `main-idea.md`
- `main-idea-ru.md`
- `main-idea-uk.md`

## Slug Stability

- Keep the canonical English slug stable.
- Translate the **title** and **content**, not the underlying canonical slug.
- Translation files add a language suffix but remain anchored to the same canonical page.

## Frontmatter Rules

Canonical English pages should include:

```yaml
lang: en
canonical: page.md
```

Translations should include:

```yaml
lang: ru | uk
canonical: page.md
translation_of: page.md
```

## Wikilink Policy

- RU and UK pages should prefer a translated target when it exists.
- If no translated target exists yet, fall back to the canonical English page.

Examples:

- RU page: `[[compatibility-level-boundaries-ru]]` if available, otherwise `[[compatibility-level-boundaries]]`
- UK page: `[[main-idea-uk]]` if available, otherwise `[[main-idea]]`

## Scope Note

- Translation does not authorize stronger claims.
- Avoid deterministic or scientifically proven wording unless a page explicitly documents such evidence.
- Preferred wording remains: *heuristic*, *hypothesis*, *proposed mapping*, *interpretation*, *non-deterministic*.
