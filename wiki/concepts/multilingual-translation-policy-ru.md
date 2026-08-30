---
title: Политика многоязычных переводов
type: concept
tags: [policy, multilingual, translation, wiki, conventions]
created: 2026-04-26
updated: 2026-08-30
sources: []
lang: ru
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

# Политика многоязычных переводов

[[multilingual-translation-policy-en|English]] | Русский | [[multilingual-translation-policy-uk|Українська]]

<!-- section:purpose -->
## Назначение

Каждая активная страница wiki Before We Build имеет равноправные английскую,
русскую и украинскую версии. Перевод сохраняет смысл, доказательный статус,
оговорки, примеры и источники и не усиливает утверждения.

<!-- section:file-naming -->
## Имена файлов

Используется симметричная схема:

- `page-en.md`
- `page-ru.md`
- `page-uk.md`

Канонического языка без суффикса и скрытого перехода на другой язык нет.

<!-- section:metadata -->
## Общие метаданные

У трёх версий совпадают `translation_group`, `semantic_version`,
`document_status`, `page_role`, идентификаторы и статусы утверждений,
оговорок, источников и разделов. Каждый файл указывает собственный `lang`.

Активная страница требует равенства `reviewed_semantic_version` и
`semantic_version` во всех трёх файлах. Смысловое изменение синхронно
вносится во все версии. До проверки вся группа имеет статус `draft` и не
попадает в Start Here.

<!-- section:links -->
## Ссылки

Внутренние ссылки обычно сохраняют язык читателя. Переход между языками
разрешён только при явном сравнении переводов. Старые пути записываются в
`wiki/slug-migrations.json`; файлы-перенаправления не сохраняются.

<!-- section:review -->
## Смысловая проверка

Автоматизация проверяет структуру, но рецензент должен подтвердить, что три
страницы делают одинаковые утверждения, сохраняют одинаковую неопределённость
и не вводят отдельный вывод для одного языка. Предпочтителен естественный, а
не дословный перевод.

<!-- section:caveat -->
## Оговорка

`translation-does-not-strengthen-claims`: проектная гипотеза остаётся
гипотезой во всех языках, даже если в одном языке доступна более уверенно
звучащая бытовая формулировка.
