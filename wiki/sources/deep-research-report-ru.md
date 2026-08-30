---
title: Обзор agent-фреймворков, оркестрации и памяти
type: source
tags: [agents, orchestration, rag, memory, infrastructure, source-summary]
created: 2026-04-15
updated: 2026-08-30
lang: ru
sources: [official project documentation]
translation_group: deep-research-report
semantic_version: 1
reviewed_semantic_version: 1
document_status: active
page_role: source-summary
claim_status: [source-attribution]
claims: []
caveat_ids: []
---

# Выбор agent harnesses, фреймворков, оркестрации и памяти

<!-- section:executive-summary -->
## Краткий вывод

Нет универсального стека. Agent framework организует LLM-вызовы и инструменты; workflow orchestrator обеспечивает долговечное выполнение; serving/runtime отвечает за масштабирование; vector/database layer — за данные и поиск. Выбор должен начинаться с конкретного процесса, требований к приватности и отказоустойчивости, а не с популярности продукта.

Это технический ориентационный отчёт, а не актуальный benchmark. Возможности проектов меняются; перед решением нужно сверять официальную документацию и собственные измерения.

<!-- section:definitions-and-boundaries -->
## Определения и границы

- **Agent harness/framework:** prompts, tools, state и переходы.
- **Workflow orchestrator:** retries, durable state, schedules и human approval.
- **Serving/runtime:** deployment, concurrency, resource control.
- **RAG/data layer:** ingestion, retrieval, metadata, permissions.
- **Memory:** явно спроектированное кратко- или долгосрочное состояние, не «понимание пользователя».

<!-- section:evaluation-criteria-and-typical-tradeoffs -->
## Критерии и компромиссы

<!-- section:architecture-and-responsibility-boundaries -->
### Архитектура и ответственность

Разделять бизнес-процесс, недетерминированный LLM-шаг, долговечное состояние и источник истины. Не отдавать модели скрытую власть над критическими решениями.

<!-- section:scaling-latency-throughput -->
### Масштабирование, задержка и throughput

Измерять полную цепочку: очередь, model latency, tool calls, retrieval, serialization и retries. Длинные контексты и последовательные вызовы часто важнее накладных расходов framework.

<!-- section:reliability-fault-tolerance-state-consistency -->
### Надёжность и согласованность

Нужны idempotency, timeouts, ограниченные retries, checkpointing, versioned state и явное поведение при частичном отказе.

<!-- section:security-privacy-compliance -->
### Безопасность, приватность и compliance

Минимизировать данные, ограничивать инструменты, изолировать tenants, защищать secrets и логировать решения без утечки пользовательского содержания.

<!-- section:observability-and-manageability -->
### Наблюдаемость

Отслеживать шаги, длительность, стоимость, версии prompt/model/tool, ошибки и человеческие вмешательства. Trace не заменяет оценку качества результата.

<!-- section:extensibility-integrations-api-languages-deployment -->
### Расширяемость и deployment

Оценивать языки, API, self-hosting, экосистему, portability и стоимость выхода из продукта.

<!-- section:comparison-of-popular-projects -->
## Сравнение популярных проектов

<!-- section:summary-comparative-table -->
### Сводка

| Категория | Примеры | Сильная сторона | Основное ограничение |
|---|---|---|---|
| agent/RAG framework | LangChain, LlamaIndex, Haystack | быстрая композиция инструментов и retrieval | API churn и скрытая сложность |
| multi-agent framework | AutoGen | диалоги ролей и эксперименты | контроль циклов и воспроизводимость |
| distributed runtime | Ray | масштабирование Python-задач | операционная сложность |
| workflow orchestration | Prefect, Temporal, Airflow | retries, state, schedules | не заменяет agent semantics |
| model serving | BentoML | packaging и serving | отдельное проектирование workflow |
| vector stores | Weaviate, Milvus, Chroma | semantic retrieval | качество зависит от данных и evaluation |

<!-- section:official-documentation-and-repository-links -->
### Официальные ссылки

- LangChain: https://github.com/langchain-ai/langchain · https://docs.langchain.com/
- LlamaIndex: https://github.com/run-llama/llama_index · https://developers.llamaindex.ai/
- Haystack: https://github.com/deepset-ai/haystack · https://docs.haystack.deepset.ai/
- AutoGen: https://github.com/microsoft/autogen · https://microsoft.github.io/autogen/
- Ray: https://github.com/ray-project/ray · https://docs.ray.io/
- Prefect: https://github.com/PrefectHQ/prefect · https://docs.prefect.io/
- Temporal: https://github.com/temporalio/temporal · https://docs.temporal.io/
- Airflow: https://github.com/apache/airflow · https://airflow.apache.org/docs/
- BentoML: https://github.com/bentoml/BentoML · https://docs.bentoml.com/
- Weaviate: https://github.com/weaviate/weaviate · https://docs.weaviate.io/
- Milvus: https://github.com/milvus-io/milvus · https://milvus.io/docs/
- Chroma: https://github.com/chroma-core/chroma · https://docs.trychroma.com/

<!-- section:short-notes-on-each-project -->
### Короткие заметки

Frameworks ускоряют прототип; orchestrators повышают долговечность; runtimes масштабируют; vector stores предоставляют поиск. Обычно производственная система комбинирует несколько слоёв и сохраняет доменную логику вне framework-specific abstractions.

<!-- section:selecting-solutions-by-use-cases-and-decision-flow -->
## Выбор по сценарию

<!-- section:practical-selection-criteria-by-use-case -->
### Практические критерии

- простой разговор: минимальный harness и явное состояние;
- RAG: ingestion quality, permissions и retrieval evaluation;
- регулируемый workflow: durable orchestrator и approval gates;
- высокая нагрузка: измеренный serving/runtime;
- исследовательский multi-agent: строгие лимиты, trace и evaluation.

<!-- section:recommended-decision-flow-selection-checklist -->
### Рекомендуемый процесс решения

1. Описать I/O, состояние, authority и failure modes.
2. Сделать минимальный reference flow без тяжёлой платформы.
3. Измерить качество, задержку, стоимость и восстановление.
4. Добавлять отдельный слой только для наблюдаемой потребности.
5. Проверить migration/exit plan.

<!-- section:mini-decision-matrix-example-shortlists-by-use-case -->
### Мини-матрица вариантов

Shortlist является началом испытания, а не рекомендацией покупки. Сравнение должно использовать одинаковые данные, модели и нагрузку.

<!-- section:reference-architectures -->
## Референсные архитектуры

<!-- section:simple-conversational-agent-with-short-memory -->
### Простой разговор с короткой памятью

API → policy/input validation → model/tool loop → bounded conversation state → audit metadata.

<!-- section:rag-pipeline-with-vector-db-and-long-term-memory -->
### RAG с долгосрочной памятью

Ingestion → parsing/chunking → ACL-aware index → retrieval/reranking → grounded generation → citation/evaluation. «Memory» должна иметь цель, срок хранения, источник и возможность удаления.

<!-- section:multi-agent-workflow-orchestration -->
### Multi-agent workflow

Orchestrator → ограниченные роли → shared typed state → approval/termination rules → evaluator. Число агентов не является метрикой качества.

<!-- section:performance-cost-and-benchmarks -->
## Производительность, стоимость и benchmarks

<!-- section:where-latency-and-cost-actually-burn -->
### Где расходуются задержка и стоимость

Модельные токены, последовательные вызовы инструментов, retrieval, повторные попытки и большой контекст.

<!-- section:what-to-look-for-in-benchmarks-and-what-s-often-missing -->
### Что искать в benchmark

Одинаковые задачи, качество ответа, p50/p95 latency, стоимость успешной задачи, failure rate, recovery и human correction. Маркетинговые demo не заменяют нагрузочный тест.

<!-- section:recommended-tests-to-run-before-selection -->
### Обязательные испытания

Golden set, adversarial inputs, tool failures, stale retrieval, concurrency, permission leakage, restore from checkpoint и provider migration.

<!-- section:security-compliance-data-privacy-and-migrations -->
## Безопасность, compliance и миграции

<!-- section:security-privacy-checklist-practical -->
### Практический checklist

Least privilege, secret isolation, consent, retention/deletion, encryption, prompt-injection boundaries, human approval для высокорисковых действий и безопасные логи.

<!-- section:observability-compliance-checklist -->
### Observability/compliance

Версии компонентов, trace IDs, причина вмешательства, provenance данных и воспроизводимый audit trail.

<!-- section:migration-and-interoperability -->
### Interoperability

Хранить доменные данные и события в собственных стабильных схемах; изолировать адаптеры; тестировать экспорт и замену provider/framework.

<!-- section:brief-recommendations -->
## Краткие рекомендации

Начинать с самого малого проверяемого стека. Для Before We Build AI остаётся помощником для организации и вопросов, поэтому инфраструктура не должна превращать модель в автономного диагноста или предсказателя людей.

<!-- section:source-assessment -->
## Оценка источника

<!-- section:source-claims -->
### Что утверждает источник

Отчёт сравнивает программные компоненты и архитектурные компромиссы разговорных, поисковых, workflow- и observability-систем.

<!-- section:source-evidence -->
### Какие данные или свидетельства приведены

Он сводит официальную документацию, репозитории и опубликованные benchmarks; единого контролируемого теста всех проектов в нём нет.

<!-- section:source-limitations -->
### Ограничения

Версии, цены, производительность и функции безопасности меняются, а vendor benchmarks и неоднородные нагрузки нельзя прямо сравнивать.

<!-- section:bwb-accepts -->
### Что принимает BWB

BWB принимает инженерные критерии решения, вопросы воспроизводимости и checklists приватности и наблюдаемости для инструментов слабого помощника.

<!-- section:bwb-contested -->
### Что остаётся спорным или открытым

Текущая сравнительная производительность, эксплуатационная стоимость и пригодность для конкретного развёртывания остаются открытыми и требуют локальных тестов.

<!-- section:bwb-rejected-or-historical -->
### Что отвергнуто или хранится только исторически

BWB отвергает представление возможностей ПО как свидетельств о психологии человека и автоматическое решение об отношениях по инфраструктурному результату.
