# Modern Agentic Research Systems: Ready-to-Use Solutions (2026)

## Executive Summary

**Don't build from scratch.** There are production-ready open-source systems that already work. This document covers proven frameworks from top research labs.

---

## 1. The Agentic Researcher (ZIB-IOL)

**arXiv:** arxiv.org/abs/2603.15914  
**GitHub:** github.com/ZIB-IOL/The-Agentic-Researcher  
**Дата:** March 2026

### Что это
Практическое руководство от института ZIB-IOL (Германия) по AI-assisted research в математике и ML. Включает:
- 5-level taxonomy AI integration
- Open-source sandboxed framework
- "Ten Commandments" для агентов
- CLI coding agents (Claude Code, Codex CLI, Gemini CLI)

### 10 Заповедей для Агентов

```
I. Quantify Uncertainty     — Quantify uncertainty in all claims
II. Verify Independently    — Verify all results independently  
III. Cite Source Code       — Always cite specific line numbers
IV. Test Edge Cases        — Test on edge cases before claiming success
V. Report Failures         — Report all failures and limitations
VI. Be Concise            — Prefer concise over verbose
VII. Think Before Code     — Think before implementing
VIII. Bound Expectations   — Identify theoretical bounds before implementing
IX. Prefer Simplicity     — Simple solutions > complex ones
X. Document Tradeoffs     — Document all assumptions and tradeoffs
```

### Использование

```bash
# Clone
git clone https://github.com/ZIB-IOL/The-Agentic-Researcher.git
cd The-Agentic-Researcher

# Run with Claude Code
claude-code --sandbox ./research_container

# Or with any CLI agent
opencode ./research_container
```

### Результаты
- Longest autonomous session: **20+ hours**
- Autonomous research without human intervention
- Runs inside sandboxed container
- Works with any frontier LLM

---

## 2. Anthropic Multi-Agent Research System

**Ссылка:** anthropic.com/engineering/built-multi-agent-research-system  
**Дата:** June 2025

### Что это
Как Anthropic построил свой Research feature — множество Claude agents для исследования сложных тем.

### Архитектура

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR AGENT                        │
│  (Lead agent plans research, spawns subagents)              │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Subagent  │    │  Subagent  │    │  Subagent  │
│ (searching │    │ (searching │    │ (searching │
│  direction │    │  direction │    │  direction │
│     A)     │    │     B)     │    │     C)     │
└─────────────┘    └─────────────┘    └─────────────┘
        │                   │                   │
        └───────────────────┴───────────────────┘
                            │
                            ▼
                    ┌─────────────────┐
                    │  SYNTHESIS       │
                    │  (Combining all  │
                    │   findings)      │
                    └─────────────────┘
```

### Ключевые Принципы Anthropic

1. **Think like your agents** — понимай как agents думают
2. **Scale effort to query complexity** — не трать 20 часов на простой запрос
3. **Tool design critical** — каждый tool должен иметь чёткую цель
4. **Let agents improve themselves** — дай Claude улучшать промпты
5. **Start wide, then narrow** — сначала breadth-first, потом depth
6. **Parallel tool calling** — до **90% ускорения** с parallel agents

### Результаты
- **90% faster** research с parallel tool calling
- Multi-agent системы лучше для breadth-first queries
- Claude Opus 4 лучший для complex research

---

## 3. InternAgent (Shanghai AI Lab)

**GitHub:** github.com/InternScience/InternAgent  
**Stars:** 1,269  
**Дата:** 2025-2026

### Что это
Унифицированный фреймворк для end-to-end autonomous scientific discovery. Поддерживает:

- **Algorithm Discovery** — создание новых алгоритмов
- **Empirical Discovery** — проверка гипотез в реальных экспериментах
- **3 координационных подсистемы:** Generation, Verification, Evolution

### Архитектура

```
┌─────────────────────────────────────────────────────────────┐
│                    InternAgent 1.5                          │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐   │
│  │ GENERATION │───►│VERIFICATION │───►│ EVOLUTION  │   │
│  │             │    │             │    │             │   │
│  │ Hypothesis  │    │ Method     │    │ Evidence-  │   │
│  │ construction│    │ evaluation  │    │ driven     │   │
│  │ via deep   │    │ solution    │    │ refinement  │   │
│  │ research   │    │ refinement  │    │ long-horizon│  │
│  │             │    │             │    │ memory     │   │
│  └─────────────┘    └─────────────┘    └─────────────┘   │
├─────────────────────────────────────────────────────────────┤
│                  STRUCTURED COGNITIVE MEMORY                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐   │
│  │ Strategy-   │    │  Task-      │    │ Semantic-  │   │
│  │ Procedural  │    │ Episodic    │    │ Knowledge  │   │
│  └─────────────┘    └─────────────┘    └─────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Результаты на Benchmarks

| Benchmark | Результат |
|-----------|-----------|
| GAIA | Leading performance |
| HLE | Leading performance |
| GPQA | Leading performance |
| SGI-bench | Leading performance |
| **MLE-Bench** | State-of-the-art |

### Доступ

```bash
# Clone
git clone https://github.com/InternScience/InternAgent.git

# Submit issue for access
# или используй open-source части
```

---

## 4. MARS (Modular Agent with Reflective Search)

**arXiv:** arxiv.org/abs/2602.02660  
**Для:** Automated AI Research

### Что это
Фреймворк оптимизированный для AI research, а не general coding.

### 3 Ключевых Пpillars

1. **Budget-Aware Planning** — Monte Carlo Tree Search с cost constraints
2. **Embedded Reflection** — учится из прошлых ошибок
3. **Memory-Aware Priors** — использует накопленный опыт

### Результаты

| Метрика | Улучшение |
|---------|-----------|
| Token usage | -28% |
| Agent calls | -17% |
| Time-to-success | -19% |

### Особенность
REDEREF controller — **training-free**, работает с любой моделью.

---

## 5. Robin (Multi-Agent Scientific Discovery)

**arXiv:** arxiv.org/abs/2505.13400  
**Для:** Therapeutics research

### Что это
Первый multi-agent system который **fully automates** все intellectual steps scientific process.

### Агенты

```
┌─────────────────────────────────────────────────────────────┐
│                       ROBIN                                 │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐   │
│  │    CROW      │    │   FALCON    │    │    FINCH    │   │
│  │              │    │             │    │             │   │
│  │ Concise      │    │ Deep        │    │ Scientific  │   │
│  │ literature   │    │ literature  │    │ data       │   │
│  │ summaries    │    │ analysis    │    │ analysis    │   │
│  │ (PaperQA2)   │    │             │    │             │   │
│  └─────────────┘    └─────────────┘    └─────────────┘   │
│         │                  │                  │              │
│         └──────────────────┼──────────────────┘              │
│                            ▼                                │
│              ┌─────────────────────────┐                   │
│              │    HYPOTHESIS RANKING   │                   │
│              │    (LLM Judge)         │                   │
│              └─────────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### Результаты
- Discovered **novel therapeutic candidates**
- Iterative lab-in-the-loop framework
- First complete AI-driven scientific discovery pipeline

---

## 6. SciDER (Scientific Data-centric End-to-end Researcher)

**arXiv:** arxiv.org/abs/2603.01421  
**PyPI:** `pip install scider`

### Что это
End-to-end система для scientific research lifecycle. На базе **LangGraph**.

### Особенности

| Компонент | Описание |
|-----------|---------|
| Ideation Agent | Generates keywords, retrieves literature |
| Data Analysis | Handles raw scientific data |
| Experimentation | Runs experiments |
| **Test-time Memory** | Remembers across sessions |

### Сравнение с другими

| Framework | Ideation | Data Analysis | Experimentation | Memory |
|-----------|----------|---------------|-----------------|--------|
| AI Scientist | ✓ | ✗ | ✓ | ✗ |
| AI Researcher | ✓ | ✗ | ✓ | ✓ |
| **SciDER** | ✓ | ✓ | ✓ | ✓ |

---

## 7. Agentic Hybrid RAG (Literature Review)

**GitHub:** github.com/Kamaleswaran-Lab/Agentic-Hybrid-Rag  
**Для:** Scientific literature review

### Архитектура

```
┌─────────────────────────────────────────────────────────────┐
│                    Neo4j Knowledge Graph                     │
│                    + FAISS Vector Store                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              LLaMA-3.3-70B-versatile Agent                  │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐   │
│  │ GraphRAG    │    │ VectorRAG   │    │ Uncertainty │   │
│  │ (Cypher)    │    │ (similarity)│    │ Estimation  │   │
│  └─────────────┘    └─────────────┘    └─────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Sources
- PubMed API
- ArXiv
- Google Scholar
- **Uncertainty quantification** — помечает low-confidence ответы

---

## 8. The AI Scientist (Sakana AI)

**GitHub:** github.com/SakanaAI/AI-Scientist  
**Статус:** Production, papers passed peer review

### Pipeline

```
Idea → Code → Experiment → Analysis → Paper → Peer Review
```

### Особенности
- Генерирует **novel** исследования
- Automated peer review system
- Papers accepted at workshops

---

## Сравнительная Таблица

| System | Focus | Lang | Open Source | Stars | Best For |
|--------|-------|------|-------------|-------|----------|
| **InternAgent** | General | Python | Yes | 1,269 | End-to-end discovery |
| **The Agentic Researcher** | Math/ML | Python | Yes | - | Research methodology |
| **Anthropic Research** | General | Any | No | - | Architecture patterns |
| **MARS** | AI Research | Python | Yes | - | Cost-efficient research |
| **Robin** | Therapeutics | Python | Paper only | - | Drug discovery |
| **SciDER** | Data | Python | Yes | - | Data-heavy research |
| **Hybrid RAG** | Literature | Python | Yes | - | Literature review |
| **The AI Scientist** | General | Python | Yes | - | Paper generation |

---

## Быстрый Старт: Что Использовать

### Для Типологий Исследования (наш случай)

**Рекомендация: Комбинация**

```
1. The Agentic Researcher (methodology + 10 commandments)
        ↓
2. Anthropic Multi-Agent patterns (orchestration)
        ↓
3. SciDER (data analysis + memory)
        ↓
4. Agentic Hybrid RAG (literature review)
```

### Установка

```bash
# 1. The Agentic Researcher
git clone https://github.com/ZIB-IOL/The-Agentic-Researcher.git

# 2. SciDER (если нужен data analysis)
pip install scider

# 3. Claude Code (для CLI agent)
# Download from anthropic.com/claude-code

# 4. InternAgent (для advanced discovery)
git clone https://github.com/InternScience/InternAgent.git
```

### Пример Workflow

```python
# Using concepts from all systems

from crewai import Agent, Task, Crew

# 1. Literature Review (Hybrid RAG pattern)
literature_agent = Agent(
    role="Literature Scout",
    goal="Find all research on typologies",
    tools=[search_pubmed, search_arxiv, uncertainty_estimator]
)

# 2. Hypothesis Generation (The Agentic Researcher pattern)
hypothesis_agent = Agent(
    role="Scientist",
    goal="Generate testable hypotheses",
    backstory="""Follow The Agentic Researcher's 10 Commandments:
    1. Quantify uncertainty
    2. Verify independently
    3. Think before implementing""",
    tools=[literature_agent]
)

# 3. Data Analysis (SciDER pattern)
analysis_agent = Agent(
    role="Data Analyst",
    goal="Analyze typology data with memory",
    tools=[memory_store, statistical_tests]
)

# 4. Writing (Anthropic pattern)
writer_agent = Agent(
    role="Paper Writer",
    goal="Write publication-ready paper",
    verbose=True
)

# Orchestrate (Anthropic orchestrator pattern)
crew = Crew(
    agents=[literature_agent, hypothesis_agent, analysis_agent, writer_agent],
    process="hierarchical"
)

result = crew.kickoff()
```

---

## Anthropic's 8 Принципов для Research Agents

Независимо от фреймворка, Anthropic рекомендует:

1. **Think like your agents** — понимай limitations
2. **Build evals** — автоматизированная оценка
3. **Scale effort to complexity** — effort = complexity
4. **Tool design critical** — каждый tool = distinct purpose
5. **Let agents improve themselves** — дай agents улучшать промпты
6. **Start wide, then narrow** — breadth-first → depth
7. **Guide thinking process** — extended thinking mode
8. **Parallel tool calling** — 90% faster

---

## Key References

| Paper | arXiv | Key Contribution |
|-------|-------|-----------------|
| The Agentic Researcher | 2603.15914 | 10 Commandments, methodology |
| Anthropic Multi-Agent | - | Architecture patterns |
| InternAgent 1.5 | 2602.08990 | End-to-end discovery |
| MARS | 2602.02660 | Cost-efficient research |
| Robin | 2505.13400 | Full pipeline |
| SciDER | 2603.01421 | Data-centric |
| Hybrid RAG | 2508.05660 | Literature review |
| The AI Scientist | 2408.06292 | Paper generation |

---

## Итог

**Не изобретай велосипед.** Используй готовые системы:

1. **The Agentic Researcher** — для methodology и quality control
2. **Anthropic patterns** — для orchestration
3. **InternAgent/SciDER** — для end-to-end research
4. **Hybrid RAG** — для literature review
5. **The AI Scientist** — для paper generation

**Комбинируй** лучшие практики из всех систем под свою задачу.
