---
title: Multilingual Translation Policy
type: concept
tags: [policy, multilingual, translation, wiki, conventions]
created: 2026-04-26
updated: 2026-08-30
sources: []
lang: en
translation_group: multilingual-translation-policy
semantic_version: 2
reviewed_semantic_version: 2
document_status: active
page_role: research-appendix
claim_status: [project-definition, normative-rule]
claims:
  - id: equal-language-peers
    status: normative-rule
caveat_ids: [translation-does-not-strengthen-claims]
---

# Multilingual Translation Policy

English | [[multilingual-translation-policy-ru|Русский]] | [[multilingual-translation-policy-uk|Українська]]

<!-- section:purpose -->
## Purpose

Every active Before We Build wiki page has equal English, Russian, and
Ukrainian peers. Translation preserves meaning, evidence status, caveats,
examples, and sources; it does not make a claim stronger.

<!-- section:file-naming -->
## File naming

Use symmetric paths:

- `page-en.md`
- `page-ru.md`
- `page-uk.md`

There is no unsuffixed canonical language page and no silent fallback to a
different language.

<!-- section:metadata -->
## Shared metadata

The three peers share `translation_group`, `semantic_version`,
`document_status`, `page_role`, claim IDs and statuses, caveat IDs, source
IDs, and stable section IDs. Each file declares its own `lang`.

An active page requires `reviewed_semantic_version` to equal
`semantic_version` in all three files. A semantic change updates the three
peers together. Until review is complete, the whole group is `draft` and is
excluded from Start Here.

<!-- section:links -->
## Links

Internal links normally stay in the reader's language. Cross-language links
are allowed only when the text explicitly compares translations. Old paths
are recorded in `wiki/slug-migrations.json`; redirect stubs are not kept.

<!-- section:review -->
## Semantic review

Automation checks structure, but a reviewer must confirm that the three pages
make the same claims, retain the same uncertainty, and do not introduce a
language-specific conclusion. Idiomatic wording is preferred to literal
translation.

<!-- section:caveat -->
## Caveat

`translation-does-not-strengthen-claims`: a project hypothesis remains a
hypothesis in every language, even when one language has a more confident
everyday expression available.
