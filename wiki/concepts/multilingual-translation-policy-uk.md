---
title: Політика багатомовних перекладів
type: concept
tags: [policy, multilingual, translation, wiki, conventions]
created: 2026-04-26
updated: 2026-08-30
sources: []
lang: uk
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

# Політика багатомовних перекладів

[[multilingual-translation-policy-en|English]] | [[multilingual-translation-policy-ru|Русский]] | Українська

<!-- section:purpose -->
## Призначення

Кожна активна сторінка wiki Before We Build має рівноправні англійську,
російську та українську версії. Переклад зберігає зміст, доказовий статус,
застереження, приклади й джерела та не посилює твердження.

<!-- section:file-naming -->
## Назви файлів

Використовується симетрична схема:

- `page-en.md`
- `page-ru.md`
- `page-uk.md`

Канонічної мови без суфікса й прихованого переходу на іншу мову немає.

<!-- section:metadata -->
## Спільні метадані

У трьох версіях збігаються `translation_group`, `semantic_version`,
`document_status`, `page_role`, ідентифікатори та статуси тверджень,
застережень, джерел і розділів. Кожен файл указує власний `lang`.

Активна сторінка вимагає рівності `reviewed_semantic_version` і
`semantic_version` у всіх трьох файлах. Змістову зміну синхронно вносять до
всіх версій. До перевірки вся група має статус `draft` і не потрапляє до
Start Here.

<!-- section:links -->
## Посилання

Внутрішні посилання зазвичай зберігають мову читача. Перехід між мовами
дозволений лише під час явного порівняння перекладів. Старі шляхи записуються
до `wiki/slug-migrations.json`; файли-перенаправлення не зберігаються.

<!-- section:review -->
## Змістова перевірка

Автоматизація перевіряє структуру, але рецензент має підтвердити, що три
сторінки роблять однакові твердження, зберігають однакову невизначеність і не
вводять окремого висновку для однієї мови. Перевага надається природному, а не
дослівному перекладу.

<!-- section:caveat -->
## Застереження

`translation-does-not-strengthen-claims`: проєктна гіпотеза залишається
гіпотезою всіма мовами, навіть якщо однією мовою доступне впевненіше за тоном
побутове формулювання.
