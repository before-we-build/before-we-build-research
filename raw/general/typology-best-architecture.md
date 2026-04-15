# Лучшая Архитектура для Исследования Типологий (2026)

## Главная Находка: agent-topia/evolving_personality

**GitHub:** github.com/agent-topia/evolving_personality  
**Stars:** 908  
**arXiv:** arxiv.org/abs/2601.10025

### Это Exactly то, что нужно!

JPAF (Jungian Personality Adaptation Framework) — фреймворк который:
- Симулирует **все 16 MBTI типов**
- Based on **Carl Jung's Theory**
- **100% MBTI alignment accuracy**
- Использует **dominant-auxiliary coordination**
- Поддерживает **personality evolution**

### Архитектура JPAF

```
┌─────────────────────────────────────────────────────────────┐
│        JUNGIAN PERSONALITY ADAPTATION FRAMEWORK (JPAF)          │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐   │
│  │           INDIVIDUAL STRUCTURE (IS)                   │   │
│  │                                                     │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐          │   │
│  │  │Dominant │  │Auxiliary│  │Tertiary │  Inferior  │   │
│  │  │(1st)   │◄─┤(2nd)   │  │(3rd)    │  (4th)    │   │
│  │  │         │  │         │  │         │           │   │
│  │  └─────────┘  └─────────┘  └─────────┘           │   │
│  │                                                     │   │
│  │  Based on Jung's 8 psychological types              │   │
│  └─────────────────────────────────────────────────────┘   │
│                            │                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         MULTI-SCENARIO CONTEXTING (MSC)             │   │
│  │                                                     │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐          │   │
│  │  │ Work    │  │ Social  │  │ Stress  │  Relax   │   │
│  │  │ Arena   │  │ Arena   │  │ Arena   │  Arena   │   │
│  │  └─────────┘  └─────────┘  └─────────┘          │   │
│  │                                                     │   │
│  │  Role-Relationship-Norm frames                     │   │
│  └─────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│                    THREE MECHANISMS                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│  │ Dominant-  │  │Reinforcement│  │ Reflection │   │
│  │ Auxiliary  │  │Compensation │  │            │   │
│  │ Coordination│  │ Mechanism   │  │ Mechanism  │   │
│  └─────────────┘  └─────────────┘  └─────────────┘   │
│       │                │                │              │
│       └────────────────┼────────────────┘              │
│                        ▼                                 │
│              ┌─────────────────┐                      │
│              │ PERSONALITY     │                      │
│              │ COHERENT YET   │                      │
│              │ ADAPTING       │                      │
│              └─────────────────┘                      │
└─────────────────────────────────────────────────────────────┘
```

### Ключевые Результаты

| Метрика | Результат |
|---------|-----------|
| **MBTI Alignment** | **100%** (all tested models) |
| **Personality Evolution Accuracy** | GPT/Qwen 100%, Llama 92% |
| **Type Activation** | Strong across all 16 types |
| **Compatibility** | Works with Socionics too |

---

## 2. PsyAgent: Big Five Personality Modeling

**arXiv:** arxiv.org/abs/2601.06158

### Для Big Five исследований

```
┌─────────────────────────────────────────────────────────────┐
│                       PsyAgent                               │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐   │
│  │         INDIVIDUAL STRUCTURE (IS)                     │   │
│  │                                                     │   │
│  │  O ─── C ─── E ─── A ─── N                       │   │
│  │  │      │      │      │      │                    │   │
│  │  Openness Conscient. Extraversion Agreeable. Neurot. │   │
│  │                                                     │   │
│  │  Machine-usable trait-grounded profile              │   │
│  └─────────────────────────────────────────────────────┘   │
│                            │                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         MULTI-SCENARIO CONTEXTING (MSC)             │   │
│  │                                                     │   │
│  │  Role-Relationship-Norm frames                     │   │
│  │  Spanning 8 everyday arenas                         │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Особенности
- Trait-context interface
- Psychometric-style evaluation в percentile space
- External benchmarks + blinded human study
- Fine-tune compact backbones with PEFT

---

## 3. OASIS: Survey Collection System

**Ссылка:** oasis-surveys.github.io  
**Open Source:** Yes (MIT)

### Для сбора данных опросов

```
┌─────────────────────────────────────────────────────────────┐
│                         OASIS                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────┐    ┌───────────┐    ┌───────────┐        │
│  │   Voice  │    │   Text   │    │Structured│        │
│  │   Agent  │    │   Chat   │    │ Protocol │        │
│  └─────┬─────┘    └─────┬─────┘    └─────┬─────┘    │
│        │                │                │               │
│        └────────────────┼────────────────┘               │
│                         ▼                                  │
│              ┌─────────────────────┐                     │
│              │    PostgreSQL        │                     │
│              │    (Structured)      │                     │
│              └─────────────────────┘                     │
│                         │                                 │
│                         ▼                                 │
│              ┌─────────────────────┐                     │
│              │   Export JSON/CSV   │                     │
│              └─────────────────────┘                     │
└─────────────────────────────────────────────────────────────┘
```

### Возможности
- **Voice agents** (OpenAI Realtime, Gemini Live)
- **Text chat**
- **Semi-structured interviews**
- **10 to 10,000 interviews**
- **Any model** (GPT-4, Claude, Gemini, Mistral)
- **100% open source**

### Установка

```bash
git clone https://github.com/oasis-surveys/oasis.git
cd oasis
docker-compose up
# Открой http://localhost:3000
```

---

## 4. Agentic AutoSurvey: Literature Survey Generation

**arXiv:** arxiv.org/abs/2509.18661

### Для систематических обзоров

```
┌─────────────────────────────────────────────────────────────┐
│                   Agentic AutoSurvey                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐                                        │
│  │  Paper Search  │                                        │
│  │  Specialist    │                                        │
│  └────────┬────────┘                                        │
│           │                                                  │
│           ▼                                                  │
│  ┌─────────────────┐                                        │
│  │  Topic Mining   │                                        │
│  │  & Clustering   │                                        │
│  └────────┬────────┘                                        │
│           │                                                  │
│           ▼                                                  │
│  ┌─────────────────┐                                        │
│  │  Academic Survey│                                        │
│  │  Writer        │                                        │
│  └────────┬────────┘                                        │
│           │                                                  │
│           ▼                                                  │
│  ┌─────────────────┐                                        │
│  │ Quality         │                                        │
│  │ Evaluator       │                                        │
│  └─────────────────┘                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Результаты
- **8.18/10** quality score
- **71% improvement** over AutoSurvey (4.77/10)
- Multi-dimensional quality evaluation

---

## 5. MindMeld: Human-AI Experiments

**Ссылка:** mindmeld.mit.edu  
**От:** MIT

### Для экспериментов с людьми

```
┌─────────────────────────────────────────────────────────────┐
│                        MindMeld                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────┐    ┌───────────┐    ┌───────────┐        │
│  │ Experiment│    │   AI     │    │Prolific  │        │
│  │ Designer  │───►│  Agents  │◄───│ Recruitment│       │
│  │           │    │           │    │           │        │
│  └───────────┘    └─────┬─────┘    └───────────┘        │
│                          │                               │
│                          ▼                               │
│              ┌─────────────────────┐                     │
│              │ Real-Time Chat     │                     │
│              │ + Surveys          │                     │
│              │ + Voting          │                     │
│              └─────────────────────┘                     │
└─────────────────────────────────────────────────────────────┘
```

### Возможности
- No-code experiment design
- Prolific integration (participant recruitment)
- AI agents as participants
- Real-time data collection

---

## 6. SocioSim: AI Survey Swarms

**Ссылка:** sociosim.org

### Для быстрого прототипирования

```
┌─────────────────────────────────────────────────────────────┐
│                        SocioSim                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────┐       │
│  │         SWARM OF AI AGENTS (hundreds/thousands)│       │
│  │                                                   │       │
│  │   Agent₁  Agent₂  Agent₃  ...  Agentₙ        │       │
│  │     │        │       │             │           │       │
│  │     ▼        ▼       ▼             ▼           │       │
│  │   Persona₁ Persona₂ Persona₃ ... Personaₙ     │       │
│  └─────────────────────────────────────────────────┘       │
│                           │                               │
│                           ▼                               │
│              ┌─────────────────────┐                     │
│              │ Statistical Analysis │                     │
│              └─────────────────────┘                     │
└─────────────────────────────────────────────────────────────┘
```

### Особенности
- Hundreds/thousands of unique AI personas
- Multi-model (Google, Anthropic, OpenAI)
- Statistically robust data
- **71% improvement** over single prompt

---

## Полная Архитектура для Исследования Типологий

### Рекомендуемая Комбинация

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TYPOLOGY RESEARCH ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    PHASE 1: LITERATURE                             │   │
│  │                                                                     │   │
│  │  ┌─────────────────┐    ┌─────────────────┐                      │   │
│  │  │ Agentic        │    │ Agentic        │                      │   │
│  │  │ AutoSurvey     │───►│ Hybrid RAG     │                      │   │
│  │  │ (literature)   │    │ (deep search)  │                      │   │
│  │  └─────────────────┘    └─────────────────┘                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                       │
│                                    ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    PHASE 2: HYPOTHESIS                             │   │
│  │                                                                     │   │
│  │  ┌─────────────────────────────────────────────────────────────┐   │   │
│  │  │  JPAF Framework (agent-topia/evolving_personality)        │   │   │
│  │  │                                                           │   │   │
│  │  │  ┌─────────┐  ┌─────────┐  ┌─────────┐                  │   │   │
│  │  │  │MBTI    │  │Socionics│  │Psychoso-│                  │   │   │
│  │  │  │ Types  │  │ Types   │  │phy      │                  │   │   │
│  │  │  └────┬────┘  └────┬────┘  └────┬────┘                  │   │   │
│  │  │       └───────────┬┴───────────┬┘                       │   │   │
│  │  │                   ▼             ▼                           │   │   │
│  │  │           ┌─────────────────────────────┐                │   │   │
│  │  │           │  Hypothesis Generator     │                │   │   │
│  │  │           │  (Testable predictions)  │                │   │   │
│  │  │           └─────────────────────────────┘                │   │   │
│  │  └─────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                       │
│                                    ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    PHASE 3: DATA COLLECTION                         │   │
│  │                                                                     │   │
│  │  ┌─────────────────┐    ┌─────────────────┐    ┌───────────────┐  │   │
│  │  │ OASIS          │    │ SocioSim       │    │ MindMeld     │  │   │
│  │  │ (voice/text   │    │ (AI agent      │    │ (human-AI    │  │   │
│  │  │  interviews)   │    │  swarms)       │    │  experiments) │  │   │
│  │  └────────┬────────┘    └────────┬────────┘    └───────┬───────┘  │   │
│  │           │                      │                      │            │   │
│  │           └────────────────────┼──────────────────────┘            │   │
│  │                                ▼                                   │   │
│  │                     ┌─────────────────────┐                      │   │
│  │                     │  PostgreSQL / CSV   │                      │   │
│  │                     └─────────────────────┘                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                       │
│                                    ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    PHASE 4: ANALYSIS                              │   │
│  │                                                                     │   │
│  │  ┌─────────────────┐    ┌─────────────────┐                      │   │
│  │  │  SciDER        │    │  Claude Code    │                      │   │
│  │  │  (statistical) │◄───│  (code exec)    │                      │   │
│  │  └─────────────────┘    └─────────────────┘                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                       │
│                                    ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    PHASE 5: PAPER                                │   │
│  │                                                                     │   │
│  │  ┌─────────────────────────────────────────────────────────────┐   │   │
│  │  │  The Agentic Researcher (ZIB-IOL)                          │   │   │
│  │  │  + 10 Commandments + Sandbox                                   │   │   │
│  │  └─────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Быстрый Старт

### Неделя 1-2: Литература

```bash
# 1. Agentic AutoSurvey
git clone https://github.com/...
# Генерируй systematic review

# 2. Agentic Hybrid RAG
git clone https://github.com/Kamaleswaran-Lab/Agentic-Hybrid-Rag
# Deep literature search
```

### Неделя 3: Гипотезы

```python
# Используй JPAF framework
from evolving_personality import JPFAgent

# Создай агентов для каждого типа
for mbti_type in ['INTJ', 'ENTP', ...]:
    agent = JPFAgent(
        type=mbti_type,
        mechanism='dominant-auxiliary'
    )
    # Генерируй предсказания
```

### Неделя 4: Сбор данных

```bash
# OASIS для interviews
git clone https://github.com/oasis-surveys/oasis.git
docker-compose up

# SocioSim для быстрого прототипирования
# sociosim.org - AI survey swarms
```

### Неделя 5: Анализ

```python
# SciDER для статистики
pip install scider

# Или Claude Code
claude-code --sandbox
```

---

## Итоговая Рекомендация

| Фаза | Инструмент | Зачем |
|------|-------------|-------|
| **Literature** | Agentic AutoSurvey + Hybrid RAG | Систематический обзор |
| **Hypothesis** | JPAF (agent-topia) | 100% MBTI alignment |
| **Collection** | OASIS + SocioSim + MindMeld | Surveys + experiments |
| **Analysis** | SciDER + Claude Code | Statistics |
| **Writing** | The Agentic Researcher | Publication-ready |

**Главное:** JPAF framework — это **exactly** то, что нужно для типологических исследований с MBTI/Jungian theory.
