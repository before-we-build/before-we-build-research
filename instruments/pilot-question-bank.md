---
title: Before We Build pilot question bank
type: instrument
status: pilot
schemaVersion: 1.0.0
bankVersion: 2026-07-28.1
---

# Before We Build pilot question bank

This is the single canonical browser question bank. Keep the payload below valid JSON and update bankVersion whenever a browser-visible item changes. The site loads this Markdown file and accepts only the question-bank JSON block.

~~~question-bank
{
  "schemaVersion": "1.0.0",
  "bankVersion": "2026-07-28.1",
  "tests": {
    "socionics": {
      "version": "socionics-exploratory-v0.5",
      "mode": "socionics",
      "calibrationStatus": "exploratory",
      "labels": {
        "ru": [
          "Информация и общение",
          "Исследовательский профиль восьми способов воспринимать и передавать информацию; код типа до калибровки не выводится"
        ],
        "en": [
          "Information and communication",
          "An exploratory profile of eight ways of perceiving and sharing information; no type code is reported before calibration"
        ],
        "uk": [
          "Інформація і спілкування",
          "Дослідницький профіль восьми способів сприймати й передавати інформацію; код типу до калібрації не виводиться"
        ]
      },
      "dims": [
        "Ti",
        "Te",
        "Fi",
        "Fe",
        "Si",
        "Se",
        "Ni",
        "Ne"
      ],
      "items": [
        {
          "id": "soc_1",
          "scale": "Ti",
          "version": "1.2",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне легче понять тему, когда я вижу порядок и связи между частями.",
            "en": "I understand a topic more easily when I see the order and links between its parts.",
            "uk": "Мені легше зрозуміти тему, коли я бачу порядок і зв’язки між частинами."
          }
        },
        {
          "id": "soc_2",
          "scale": "Ti",
          "version": "1.2",
          "reverse": true,
          "status": "pilot",
          "text": {
            "ru": "Мне тяжело выстраивать строгие логические схемы и формальные определения.",
            "en": "I find it hard to construct strict logical schemas and formal definitions.",
            "uk": "Мені важко вибудовувати суворі логічні схеми та формальні визначення."
          }
        },
        {
          "id": "soc_3",
          "scale": "Te",
          "version": "1.2",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я быстро спрашиваю, что реально сработало на практике.",
            "en": "I quickly ask what actually worked in practice.",
            "uk": "Я швидко питаю, що реально спрацювало на практиці."
          }
        },
        {
          "id": "soc_4",
          "scale": "Te",
          "version": "1.2",
          "reverse": true,
          "status": "pilot",
          "text": {
            "ru": "Практическая полезность и эффективные действия интересуют меня в последнюю очередь.",
            "en": "Practical utility and efficient actions matter to me least of all.",
            "uk": "Практична користь та ефективні дії цікавлять мене в останню чергу."
          }
        },
        {
          "id": "soc_5",
          "scale": "Fi",
          "version": "1.2",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я замечаю, когда между людьми меняется доверие или близость.",
            "en": "I notice when trust or closeness between people changes.",
            "uk": "Я помічаю, коли між людьми змінюється довіра або близькість."
          }
        },
        {
          "id": "soc_6",
          "scale": "Fi",
          "version": "1.2",
          "reverse": true,
          "status": "pilot",
          "text": {
            "ru": "Мне сложно улавливать тонкие оттенки личных отношений и симпатий.",
            "en": "I find it difficult to catch subtle shades of personal relationships and affinities.",
            "uk": "Мені складно вловлювати тонкі відтінки особистих стосунків і симпатій."
          }
        },
        {
          "id": "soc_7",
          "scale": "Fe",
          "version": "1.2",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я быстро замечаю общее настроение в разговоре.",
            "en": "I quickly notice the shared mood in a conversation.",
            "uk": "Я швидко помічаю загальний настрій у розмові."
          }
        },
        {
          "id": "soc_8",
          "scale": "Fe",
          "version": "1.2",
          "reverse": true,
          "status": "pilot",
          "text": {
            "ru": "Мне трудно управлять эмоциональной атмосферой в компании.",
            "en": "I find it hard to manage the emotional atmosphere in a group.",
            "uk": "Мені важко керувати емоційною атмосферою в компанії."
          }
        },
        {
          "id": "soc_9",
          "scale": "Si",
          "version": "1.2",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Когда что-то не так, я первым делом замечаю комфорт, усталость и телесные ощущения.",
            "en": "When something is off, I first notice comfort, tiredness, and body sensations.",
            "uk": "Коли щось не так, я насамперед помічаю комфорт, втому й тілесні відчуття."
          }
        },
        {
          "id": "soc_10",
          "scale": "Si",
          "version": "1.2",
          "reverse": true,
          "status": "pilot",
          "text": {
            "ru": "Я часто игнорирую физический комфорт и сигналы своего тела.",
            "en": "I often ignore physical comfort and bodily signals.",
            "uk": "Я часто ігнорую фізичний комфорт і сигнали свого тіла."
          }
        },
        {
          "id": "soc_11",
          "scale": "Se",
          "version": "1.2",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В напряжённой ситуации я быстро замечаю, где есть сила и ресурсы.",
            "en": "In a tense situation, I quickly notice where there is force and resources.",
            "uk": "У напруженій ситуації я швидко помічаю, де є сила й ресурси."
          }
        },
        {
          "id": "soc_12",
          "scale": "Se",
          "version": "1.2",
          "reverse": true,
          "status": "pilot",
          "text": {
            "ru": "Мне тяжело проявлять прямое волевое давление и отстаивать позиции.",
            "en": "I find it hard to exert direct forceful pressure and defend positions.",
            "uk": "Мені важко проявляти прямий вольовий тиск і відстоювати позиції."
          }
        },
        {
          "id": "soc_13",
          "scale": "Ni",
          "version": "1.2",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я часто чувствую, к чему постепенно идёт ситуация.",
            "en": "I often sense where a situation is gradually heading.",
            "uk": "Я часто відчуваю, до чого поступово йде ситуація."
          }
        },
        {
          "id": "soc_14",
          "scale": "Ni",
          "version": "1.2",
          "reverse": true,
          "status": "pilot",
          "text": {
            "ru": "Мне сложно улавливать скрытые тенденции и развитие событий во времени.",
            "en": "I struggle to catch hidden trends and the development of events over time.",
            "uk": "Мені складно вловлювати приховані тенденції та розвиток подій у часі."
          }
        },
        {
          "id": "soc_15",
          "scale": "Ne",
          "version": "1.2",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Меня оживляет, когда появляются неожиданные идеи и варианты.",
            "en": "I feel energized when unexpected ideas and options appear.",
            "uk": "Мене оживляє, коли з’являються несподівані ідеї та варіанти."
          }
        },
        {
          "id": "soc_16",
          "scale": "Ne",
          "version": "1.2",
          "reverse": true,
          "status": "pilot",
          "text": {
            "ru": "Множество неясных вариантов скорее сбивает меня с толку, чем вдохновляет.",
            "en": "A multitude of unclear options confuses me rather than inspires me.",
            "uk": "Безліч неясних варіантів швидше збиває мене з пантелику, ніж надихає."
          }
        },
        {
          "id": "soc_ac_1",
          "scale": "attention",
          "attention": 2,
          "version": "1.2",
          "text": {
            "ru": "Проверка внимательности: выберите вариант 2.",
            "en": "Attention check: choose option 2.",
            "uk": "Перевірка уважності: оберіть варіант 2."
          }
        }
      ],
      "measurementModel": "socionics-element-profile-v1"
    },
    "psychosophy": {
      "version": "psychosophy-pilot-v0.6",
      "mode": "position",
      "calibrationStatus": "precalibration",
      "measurementModel": "multi-indicator-position-contrast-v2",
      "minCellItems": 3,
      "labels": {
        "ru": [
          "Энергия и действие",
          "Как Воля, Логика, Эмоция и Физика участвуют в выборе как цель, материал решения, критерий или ресурс"
        ],
        "en": [
          "Energy and action",
          "How Will, Logic, Emotion, and Physics enter a choice as target, material, criterion, or resource"
        ],
        "uk": [
          "Енергія і дія",
          "Як Воля, Логіка, Емоція та Фізика беруть участь у виборі як ціль, матеріал рішення, критерій або ресурс"
        ]
      },
      "aspects": [
        "Воля",
        "Логика",
        "Эмоция",
        "Физика"
      ],
      "code": {
        "Воля": "В",
        "Логика": "Л",
        "Эмоция": "Э",
        "Физика": "Ф"
      },
      "items": [
        {
          "id": "psy_will_1_1",
          "scale": "Воля|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда распределяет ограниченные усилия между тремя выполнимыми направлениями; общая задача, ограничения и обязательства по каждому направлению известны. Я задаю порядок целей, вокруг которого распределяются усилия.",
            "en": "A team is allocating limited effort among three feasible directions; the shared task, constraints, and commitments attached to each direction are known. I set the order of goals around which effort is allocated.",
            "uk": "Команда розподіляє обмежені зусилля між трьома здійсненними напрямами; спільне завдання, обмеження й зобов’язання за кожним напрямом відомі. Я задаю порядок цілей, навколо якого розподіляються зусилля."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "shared-priorities",
          "aspect": "Воля",
          "position": 1,
          "tetradId": "воля-shared-priorities-v1",
          "contextDomain": "team"
        },
        {
          "id": "psy_will_1_2",
          "scale": "Воля|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "План уже выполняется; два способа следующего действия одинаково выполнимы, а цель, приоритет, обязательства и ближайшая задача известны. Я ориентирую промежуточное решение на выбранный приоритет.",
            "en": "A plan is already under way; two ways of taking the next action are equally feasible, and the goal, priority, commitments, and immediate task are known. I orient the intermediate decision toward the chosen priority.",
            "uk": "План уже виконується; два способи наступної дії однаково здійсненні, а мета, пріоритет, зобов’язання й найближче завдання відомі. Я орієнтую проміжне рішення на обраний пріоритет."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "plan-in-progress",
          "aspect": "Воля",
          "position": 1,
          "tetradId": "воля-plan-in-progress-v1",
          "contextDomain": "personal"
        },
        {
          "id": "psy_will_1_3",
          "scale": "Воля|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В общем проекте есть два одинаково выполнимых варианта цели; обязательства каждого варианта и задачи следующего этапа известны, и нужно выбрать один вариант. Я ориентирую следующий этап на выбранную цель.",
            "en": "A shared project has two equally feasible goal options; the commitments of each option and the next-stage tasks are known, and one option must be chosen. I orient the next stage around the chosen goal.",
            "uk": "У спільному проєкті є два однаково здійсненні варіанти мети; зобов’язання кожного варіанта й завдання наступного етапу відомі, і потрібно обрати один варіант. Я орієнтую наступний етап на обрану мету."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "shared-goal-change",
          "aspect": "Воля",
          "position": 1,
          "tetradId": "воля-shared-goal-change-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_will_2_1",
          "scale": "Воля|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда распределяет ограниченные усилия между тремя выполнимыми направлениями; общая задача, ограничения и обязательства по каждому направлению известны. Я связываю направления в последовательность совместных действий.",
            "en": "A team is allocating limited effort among three feasible directions; the shared task, constraints, and commitments attached to each direction are known. I connect the directions into a sequence of joint actions.",
            "uk": "Команда розподіляє обмежені зусилля між трьома здійсненними напрямами; спільне завдання, обмеження й зобов’язання за кожним напрямом відомі. Я пов’язую напрями в послідовність спільних дій."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "shared-priorities",
          "aspect": "Воля",
          "position": 2,
          "tetradId": "воля-shared-priorities-v1",
          "contextDomain": "team"
        },
        {
          "id": "psy_will_2_2",
          "scale": "Воля|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "План уже выполняется; два способа следующего действия одинаково выполнимы, а цель, приоритет, обязательства и ближайшая задача известны. Я соединяю предыдущее решение с одним из текущих способов действия.",
            "en": "A plan is already under way; two ways of taking the next action are equally feasible, and the goal, priority, commitments, and immediate task are known. I connect the previous decision with one of the current courses of action.",
            "uk": "План уже виконується; два способи наступної дії однаково здійсненні, а мета, пріоритет, зобов’язання й найближче завдання відомі. Я поєдную попереднє рішення з одним із поточних способів дії."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "plan-in-progress",
          "aspect": "Воля",
          "position": 2,
          "tetradId": "воля-plan-in-progress-v1",
          "contextDomain": "personal"
        },
        {
          "id": "psy_will_2_3",
          "scale": "Воля|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В общем проекте есть два одинаково выполнимых варианта цели; обязательства каждого варианта и задачи следующего этапа известны, и нужно выбрать один вариант. Я развиваю выбранную цель через последовательность совместных решений.",
            "en": "A shared project has two equally feasible goal options; the commitments of each option and the next-stage tasks are known, and one option must be chosen. I develop the chosen goal through a sequence of joint decisions.",
            "uk": "У спільному проєкті є два однаково здійсненні варіанти мети; зобов’язання кожного варіанта й завдання наступного етапу відомі, і потрібно обрати один варіант. Я розвиваю обрану мету через послідовність спільних рішень."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "shared-goal-change",
          "aspect": "Воля",
          "position": 2,
          "tetradId": "воля-shared-goal-change-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_will_3_1",
          "scale": "Воля|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда распределяет ограниченные усилия между тремя выполнимыми направлениями; общая задача, ограничения и обязательства по каждому направлению известны. Я различаю варианты распределения по обязательствам направлений.",
            "en": "A team is allocating limited effort among three feasible directions; the shared task, constraints, and commitments attached to each direction are known. I distinguish the allocation options by the commitments attached to the directions.",
            "uk": "Команда розподіляє обмежені зусилля між трьома здійсненними напрямами; спільне завдання, обмеження й зобов’язання за кожним напрямом відомі. Я розрізняю варіанти розподілу за зобов’язаннями напрямів."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "shared-priorities",
          "aspect": "Воля",
          "position": 3,
          "tetradId": "воля-shared-priorities-v1",
          "contextDomain": "team"
        },
        {
          "id": "psy_will_3_2",
          "scale": "Воля|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "План уже выполняется; два способа следующего действия одинаково выполнимы, а цель, приоритет, обязательства и ближайшая задача известны. Я исключаю промежуточное решение, нарушающее принятое обязательство.",
            "en": "A plan is already under way; two ways of taking the next action are equally feasible, and the goal, priority, commitments, and immediate task are known. I rule out an intermediate decision that violates the accepted commitment.",
            "uk": "План уже виконується; два способи наступної дії однаково здійсненні, а мета, пріоритет, зобов’язання й найближче завдання відомі. Я відкидаю проміжне рішення, що порушує прийняте зобов’язання."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "plan-in-progress",
          "aspect": "Воля",
          "position": 3,
          "tetradId": "воля-plan-in-progress-v1",
          "contextDomain": "personal"
        },
        {
          "id": "psy_will_3_3",
          "scale": "Воля|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В общем проекте есть два одинаково выполнимых варианта цели; обязательства каждого варианта и задачи следующего этапа известны, и нужно выбрать один вариант. Я различаю варианты цели по связанным с ними обязательствам.",
            "en": "A shared project has two equally feasible goal options; the commitments of each option and the next-stage tasks are known, and one option must be chosen. I distinguish the goal options by the commitments attached to them.",
            "uk": "У спільному проєкті є два однаково здійсненні варіанти мети; зобов’язання кожного варіанта й завдання наступного етапу відомі, і потрібно обрати один варіант. Я розрізняю варіанти мети за пов’язаними з ними зобов’язаннями."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "shared-goal-change",
          "aspect": "Воля",
          "position": 3,
          "tetradId": "воля-shared-goal-change-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_will_4_1",
          "scale": "Воля|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда распределяет ограниченные усилия между тремя выполнимыми направлениями; общая задача, ограничения и обязательства по каждому направлению известны. Я распределяю работу по итоговому порядку целей.",
            "en": "A team is allocating limited effort among three feasible directions; the shared task, constraints, and commitments attached to each direction are known. I allocate the work according to the resulting order of goals.",
            "uk": "Команда розподіляє обмежені зусилля між трьома здійсненними напрямами; спільне завдання, обмеження й зобов’язання за кожним напрямом відомі. Я розподіляю роботу за підсумковим порядком цілей."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "shared-priorities",
          "aspect": "Воля",
          "position": 4,
          "tetradId": "воля-shared-priorities-v1",
          "contextDomain": "team"
        },
        {
          "id": "psy_will_4_2",
          "scale": "Воля|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "План уже выполняется; два способа следующего действия одинаково выполнимы, а цель, приоритет, обязательства и ближайшая задача известны. Я выполняю ближайшую задачу в рамках текущего приоритета.",
            "en": "A plan is already under way; two ways of taking the next action are equally feasible, and the goal, priority, commitments, and immediate task are known. I carry out the immediate task within the current priority.",
            "uk": "План уже виконується; два способи наступної дії однаково здійсненні, а мета, пріоритет, зобов’язання й найближче завдання відомі. Я виконую найближче завдання в межах поточного пріоритету."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "plan-in-progress",
          "aspect": "Воля",
          "position": 4,
          "tetradId": "воля-plan-in-progress-v1",
          "contextDomain": "personal"
        },
        {
          "id": "psy_will_4_3",
          "scale": "Воля|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В общем проекте есть два одинаково выполнимых варианта цели; обязательства каждого варианта и задачи следующего этапа известны, и нужно выбрать один вариант. Я организую задачи следующего этапа по выбранному направлению.",
            "en": "A shared project has two equally feasible goal options; the commitments of each option and the next-stage tasks are known, and one option must be chosen. I organize the next-stage tasks according to the chosen direction.",
            "uk": "У спільному проєкті є два однаково здійсненні варіанти мети; зобов’язання кожного варіанта й завдання наступного етапу відомі, і потрібно обрати один варіант. Я організовую завдання наступного етапу за обраним напрямом."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "shared-goal-change",
          "aspect": "Воля",
          "position": 4,
          "tetradId": "воля-shared-goal-change-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_logic_1_1",
          "scale": "Логика|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Нужно разобраться в новой теме; доступны согласующиеся определения, примеры и надёжные источники, а практическая задача известна. Я организую разбор вокруг целостной системы понятий.",
            "en": "A new topic must be understood; compatible definitions, examples, and reliable sources are available, and the practical task is known. I organize the analysis around a coherent system of concepts.",
            "uk": "Потрібно розібратися в новій темі; доступні узгоджені визначення, приклади й надійні джерела, а практичне завдання відоме. Я організовую аналіз навколо цілісної системи понять."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "new-topic",
          "aspect": "Логика",
          "position": 1,
          "tetradId": "логика-new-topic-v1",
          "contextDomain": "learning"
        },
        {
          "id": "psy_logic_1_2",
          "scale": "Логика|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Предварительное объяснение уже отвечает на вопрос; его посылки, примеры и практические последствия известны. Я оформляю объяснение как завершённую систему.",
            "en": "A preliminary explanation already answers the question; its premises, examples, and practical consequences are known. I frame the explanation as a complete system.",
            "uk": "Попереднє пояснення вже відповідає на питання; його засновки, приклади й практичні наслідки відомі. Я оформлюю пояснення як завершену систему."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "preliminary-explanation",
          "aspect": "Логика",
          "position": 1,
          "tetradId": "логика-preliminary-explanation-v1",
          "contextDomain": "analysis"
        },
        {
          "id": "psy_logic_1_3",
          "scale": "Логика|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Два объяснения одинаково согласуются с доступными фактами; для следующего шага нужно выбрать рабочую версию. Я отдаю приоритет версии с более цельной системой понятий.",
            "en": "Two explanations fit the available facts equally well; a working version must be chosen for the next step. I give priority to the version with the more coherent system of concepts.",
            "uk": "Два пояснення однаково узгоджуються з доступними фактами; для наступного кроку потрібно обрати робочу версію. Я віддаю перевагу версії з ціліснішою системою понять."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "competing-explanations",
          "aspect": "Логика",
          "position": 1,
          "tetradId": "логика-competing-explanations-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_logic_2_1",
          "scale": "Логика|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Нужно разобраться в новой теме; доступны согласующиеся определения, примеры и надёжные источники, а практическая задача известна. Я собираю модель темы из связей между определениями и примерами.",
            "en": "A new topic must be understood; compatible definitions, examples, and reliable sources are available, and the practical task is known. I assemble a model of the topic from the links between definitions and examples.",
            "uk": "Потрібно розібратися в новій темі; доступні узгоджені визначення, приклади й надійні джерела, а практичне завдання відоме. Я складаю модель теми зі зв’язків між визначеннями й прикладами."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "new-topic",
          "aspect": "Логика",
          "position": 2,
          "tetradId": "логика-new-topic-v1",
          "contextDomain": "learning"
        },
        {
          "id": "psy_logic_2_2",
          "scale": "Логика|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Предварительное объяснение уже отвечает на вопрос; его посылки, примеры и практические последствия известны. Я развиваю объяснение через связи между посылками и примерами.",
            "en": "A preliminary explanation already answers the question; its premises, examples, and practical consequences are known. I develop the explanation through the links between its premises and examples.",
            "uk": "Попереднє пояснення вже відповідає на питання; його засновки, приклади й практичні наслідки відомі. Я розвиваю пояснення через зв’язки між засновками й прикладами."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "preliminary-explanation",
          "aspect": "Логика",
          "position": 2,
          "tetradId": "логика-preliminary-explanation-v1",
          "contextDomain": "analysis"
        },
        {
          "id": "psy_logic_2_3",
          "scale": "Логика|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Два объяснения одинаково согласуются с доступными фактами; для следующего шага нужно выбрать рабочую версию. Я объединяю связи из обеих версий в новую рабочую модель.",
            "en": "Two explanations fit the available facts equally well; a working version must be chosen for the next step. I combine the connections from both versions into a new working model.",
            "uk": "Два пояснення однаково узгоджуються з доступними фактами; для наступного кроку потрібно обрати робочу версію. Я поєдную зв’язки з обох версій у нову робочу модель."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "competing-explanations",
          "aspect": "Логика",
          "position": 2,
          "tetradId": "логика-competing-explanations-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_logic_3_1",
          "scale": "Логика|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Нужно разобраться в новой теме; доступны согласующиеся определения, примеры и надёжные источники, а практическая задача известна. Я выделяю связь понятий, от которой зависит применение темы.",
            "en": "A new topic must be understood; compatible definitions, examples, and reliable sources are available, and the practical task is known. I single out the conceptual link on which applying the topic depends.",
            "uk": "Потрібно розібратися в новій темі; доступні узгоджені визначення, приклади й надійні джерела, а практичне завдання відоме. Я виокремлюю зв’язок понять, від якого залежить застосування теми."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "new-topic",
          "aspect": "Логика",
          "position": 3,
          "tetradId": "логика-new-topic-v1",
          "contextDomain": "learning"
        },
        {
          "id": "psy_logic_3_2",
          "scale": "Логика|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Предварительное объяснение уже отвечает на вопрос; его посылки, примеры и практические последствия известны. Я выделяю посылку, от которой зависит вывод объяснения.",
            "en": "A preliminary explanation already answers the question; its premises, examples, and practical consequences are known. I single out the premise on which the explanation’s conclusion depends.",
            "uk": "Попереднє пояснення вже відповідає на питання; його засновки, приклади й практичні наслідки відомі. Я виокремлюю засновок, від якого залежить висновок пояснення."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "preliminary-explanation",
          "aspect": "Логика",
          "position": 3,
          "tetradId": "логика-preliminary-explanation-v1",
          "contextDomain": "analysis"
        },
        {
          "id": "psy_logic_3_3",
          "scale": "Логика|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Два объяснения одинаково согласуются с доступными фактами; для следующего шага нужно выбрать рабочую версию. Я различаю версии по их ключевому допущению.",
            "en": "Two explanations fit the available facts equally well; a working version must be chosen for the next step. I distinguish the versions by their key assumption.",
            "uk": "Два пояснення однаково узгоджуються з доступними фактами; для наступного кроку потрібно обрати робочу версію. Я розрізняю версії за їхнім ключовим припущенням."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "competing-explanations",
          "aspect": "Логика",
          "position": 3,
          "tetradId": "логика-competing-explanations-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_logic_4_1",
          "scale": "Логика|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Нужно разобраться в новой теме; доступны согласующиеся определения, примеры и надёжные источники, а практическая задача известна. Я применяю определения и примеры к известной практической задаче.",
            "en": "A new topic must be understood; compatible definitions, examples, and reliable sources are available, and the practical task is known. I apply the definitions and examples to the known practical task.",
            "uk": "Потрібно розібратися в новій темі; доступні узгоджені визначення, приклади й надійні джерела, а практичне завдання відоме. Я застосовую визначення й приклади до відомого практичного завдання."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "new-topic",
          "aspect": "Логика",
          "position": 4,
          "tetradId": "логика-new-topic-v1",
          "contextDomain": "learning"
        },
        {
          "id": "psy_logic_4_2",
          "scale": "Логика|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Предварительное объяснение уже отвечает на вопрос; его посылки, примеры и практические последствия известны. Я использую практические последствия объяснения при ответе на исходный вопрос.",
            "en": "A preliminary explanation already answers the question; its premises, examples, and practical consequences are known. I use the explanation’s practical consequences when answering the original question.",
            "uk": "Попереднє пояснення вже відповідає на питання; його засновки, приклади й практичні наслідки відомі. Я використовую практичні наслідки пояснення, відповідаючи на початкове питання."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "preliminary-explanation",
          "aspect": "Логика",
          "position": 4,
          "tetradId": "логика-preliminary-explanation-v1",
          "contextDomain": "analysis"
        },
        {
          "id": "psy_logic_4_3",
          "scale": "Логика|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Два объяснения одинаково согласуются с доступными фактами; для следующего шага нужно выбрать рабочую версию. Я выбираю версию по её применимости к следующему шагу.",
            "en": "Two explanations fit the available facts equally well; a working version must be chosen for the next step. I choose the version by its applicability to the next step.",
            "uk": "Два пояснення однаково узгоджуються з доступними фактами; для наступного кроку потрібно обрати робочу версію. Я обираю версію за її застосовністю до наступного кроку."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "competing-explanations",
          "aspect": "Логика",
          "position": 4,
          "tetradId": "логика-competing-explanations-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_emotion_1_1",
          "scale": "Эмоция|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В новой группе участники по-разному отреагировали на общее событие; цель разговора и общий тон понятны, и нужно дать свой ответ. Я ориентирую ответ на выбранную эмоциональную тональность.",
            "en": "In a new group, participants reacted differently to a shared event; the conversation’s purpose and shared tone are clear, and a response is needed. I orient the response around the chosen emotional tone.",
            "uk": "У новій групі учасники по-різному відреагували на спільну подію; мета розмови й загальний тон зрозумілі, і потрібно дати власну відповідь. Я орієнтую відповідь на обрану емоційну тональність."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "new-group-reaction",
          "aspect": "Эмоция",
          "position": 1,
          "tetradId": "эмоция-new-group-reaction-v1",
          "contextDomain": "social"
        },
        {
          "id": "psy_emotion_1_2",
          "scale": "Эмоция|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В важном разговоре собеседники одинаково понимают факты, но эмоционально реагируют по-разному; разговор продолжается. Я выражаю переживание как эмоциональный итог своей реплики.",
            "en": "In an important conversation, the participants understand the facts alike but react emotionally in different ways; the conversation continues. I express an experience as the emotional outcome of my contribution.",
            "uk": "У важливій розмові співрозмовники однаково розуміють факти, але емоційно реагують по-різному; розмова триває. Я виражаю переживання як емоційний підсумок своєї репліки."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "emotional-conversation",
          "aspect": "Эмоция",
          "position": 1,
          "tetradId": "эмоция-emotional-conversation-v1",
          "contextDomain": "social"
        },
        {
          "id": "psy_emotion_1_3",
          "scale": "Эмоция|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В важном разговоре реакцию поняли иначе, чем было задумано; цель разговора не изменилась, и его можно продолжить. Я сохраняю исходную тональность как ориентир нового выражения.",
            "en": "In an important conversation, a reaction was understood differently from what was intended; the conversation’s purpose is unchanged, and it can continue. I retain the original tone as the reference point for a new expression.",
            "uk": "У важливій розмові реакцію зрозуміли інакше, ніж було задумано; мета розмови не змінилася, і її можна продовжити. Я зберігаю початкову тональність як орієнтир нового вираження."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "misread-reaction",
          "aspect": "Эмоция",
          "position": 1,
          "tetradId": "эмоция-misread-reaction-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_emotion_2_1",
          "scale": "Эмоция|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В новой группе участники по-разному отреагировали на общее событие; цель разговора и общий тон понятны, и нужно дать свой ответ. Я соединяю оттенки прозвучавших реакций в новую форму ответа.",
            "en": "In a new group, participants reacted differently to a shared event; the conversation’s purpose and shared tone are clear, and a response is needed. I combine shades of the expressed reactions into a new response form.",
            "uk": "У новій групі учасники по-різному відреагували на спільну подію; мета розмови й загальний тон зрозумілі, і потрібно дати власну відповідь. Я поєдную відтінки висловлених реакцій у нову форму відповіді."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "new-group-reaction",
          "aspect": "Эмоция",
          "position": 2,
          "tetradId": "эмоция-new-group-reaction-v1",
          "contextDomain": "social"
        },
        {
          "id": "psy_emotion_2_2",
          "scale": "Эмоция|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В важном разговоре собеседники одинаково понимают факты, но эмоционально реагируют по-разному; разговор продолжается. Я преобразую различающиеся реакции в новую тональность разговора.",
            "en": "In an important conversation, the participants understand the facts alike but react emotionally in different ways; the conversation continues. I transform the differing reactions into a new tone for the conversation.",
            "uk": "У важливій розмові співрозмовники однаково розуміють факти, але емоційно реагують по-різному; розмова триває. Я перетворюю відмінні реакції на нову тональність розмови."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "emotional-conversation",
          "aspect": "Эмоция",
          "position": 2,
          "tetradId": "эмоция-emotional-conversation-v1",
          "contextDomain": "social"
        },
        {
          "id": "psy_emotion_2_3",
          "scale": "Эмоция|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В важном разговоре реакцию поняли иначе, чем было задумано; цель разговора не изменилась, и его можно продолжить. Я создаю новую форму выражения из различия между задуманным и понятым смыслом.",
            "en": "In an important conversation, a reaction was understood differently from what was intended; the conversation’s purpose is unchanged, and it can continue. I create a new form of expression from the difference between the intended and understood meanings.",
            "uk": "У важливій розмові реакцію зрозуміли інакше, ніж було задумано; мета розмови не змінилася, і її можна продовжити. Я створюю нову форму вираження з розбіжності між задуманим і зрозумілим сенсом."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "misread-reaction",
          "aspect": "Эмоция",
          "position": 2,
          "tetradId": "эмоция-misread-reaction-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_emotion_3_1",
          "scale": "Эмоция|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В новой группе участники по-разному отреагировали на общее событие; цель разговора и общий тон понятны, и нужно дать свой ответ. Я различаю формы ответа по сохраняемому эмоциональному смыслу.",
            "en": "In a new group, participants reacted differently to a shared event; the conversation’s purpose and shared tone are clear, and a response is needed. I distinguish response forms by the emotional meaning they preserve.",
            "uk": "У новій групі учасники по-різному відреагували на спільну подію; мета розмови й загальний тон зрозумілі, і потрібно дати власну відповідь. Я розрізняю форми відповіді за емоційним сенсом, який вони зберігають."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "new-group-reaction",
          "aspect": "Эмоция",
          "position": 3,
          "tetradId": "эмоция-new-group-reaction-v1",
          "contextDomain": "social"
        },
        {
          "id": "psy_emotion_3_2",
          "scale": "Эмоция|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В важном разговоре собеседники одинаково понимают факты, но эмоционально реагируют по-разному; разговор продолжается. Я отбираю продолжения по эмоциональному смыслу реакций.",
            "en": "In an important conversation, the participants understand the facts alike but react emotionally in different ways; the conversation continues. I select possible continuations by the emotional meaning of the reactions.",
            "uk": "У важливій розмові співрозмовники однаково розуміють факти, але емоційно реагують по-різному; розмова триває. Я відбираю продовження за емоційним сенсом реакцій."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "emotional-conversation",
          "aspect": "Эмоция",
          "position": 3,
          "tetradId": "эмоция-emotional-conversation-v1",
          "contextDomain": "social"
        },
        {
          "id": "psy_emotion_3_3",
          "scale": "Эмоция|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В важном разговоре реакцию поняли иначе, чем было задумано; цель разговора не изменилась, и его можно продолжить. Я отделяю задуманный эмоциональный смысл от полученной интерпретации.",
            "en": "In an important conversation, a reaction was understood differently from what was intended; the conversation’s purpose is unchanged, and it can continue. I separate the intended emotional meaning from the received interpretation.",
            "uk": "У важливій розмові реакцію зрозуміли інакше, ніж було задумано; мета розмови не змінилася, і її можна продовжити. Я відокремлюю задуманий емоційний сенс від отриманого тлумачення."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "misread-reaction",
          "aspect": "Эмоция",
          "position": 3,
          "tetradId": "эмоция-misread-reaction-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_emotion_4_1",
          "scale": "Эмоция|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В новой группе участники по-разному отреагировали на общее событие; цель разговора и общий тон понятны, и нужно дать свой ответ. Я передаю цель разговора через общий эмоциональный тон.",
            "en": "In a new group, participants reacted differently to a shared event; the conversation’s purpose and shared tone are clear, and a response is needed. I convey the conversation’s purpose through the shared emotional tone.",
            "uk": "У новій групі учасники по-різному відреагували на спільну подію; мета розмови й загальний тон зрозумілі, і потрібно дати власну відповідь. Я передаю мету розмови через загальний емоційний тон."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "new-group-reaction",
          "aspect": "Эмоция",
          "position": 4,
          "tetradId": "эмоция-new-group-reaction-v1",
          "contextDomain": "social"
        },
        {
          "id": "psy_emotion_4_2",
          "scale": "Эмоция|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В важном разговоре собеседники одинаково понимают факты, но эмоционально реагируют по-разному; разговор продолжается. Я передаю содержание разговора через эмоциональную форму реплики.",
            "en": "In an important conversation, the participants understand the facts alike but react emotionally in different ways; the conversation continues. I convey the conversation’s content through the emotional form of my contribution.",
            "uk": "У важливій розмові співрозмовники однаково розуміють факти, але емоційно реагують по-різному; розмова триває. Я передаю зміст розмови через емоційну форму своєї репліки."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "emotional-conversation",
          "aspect": "Эмоция",
          "position": 4,
          "tetradId": "эмоция-emotional-conversation-v1",
          "contextDomain": "social"
        },
        {
          "id": "psy_emotion_4_3",
          "scale": "Эмоция|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В важном разговоре реакцию поняли иначе, чем было задумано; цель разговора не изменилась, и его можно продолжить. Я подбираю эмоциональную форму к неизменной цели разговора.",
            "en": "In an important conversation, a reaction was understood differently from what was intended; the conversation’s purpose is unchanged, and it can continue. I match the emotional form to the conversation’s unchanged purpose.",
            "uk": "У важливій розмові реакцію зрозуміли інакше, ніж було задумано; мета розмови не змінилася, і її можна продовжити. Я добираю емоційну форму до незмінної мети розмови."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "misread-reaction",
          "aspect": "Эмоция",
          "position": 4,
          "tetradId": "эмоция-misread-reaction-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_physics_1_1",
          "scale": "Физика|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда проектирует рабочее место из элементов двух конфигураций; цена и пригодность для задачи одинаковы, а потребности пользователей и ограничения известны. Я организую пространство вокруг желаемого физического состояния.",
            "en": "A team is designing a workspace from elements of two configurations; cost and task suitability are equal, and user needs and constraints are known. I organize the space around the desired physical state.",
            "uk": "Команда проєктує робоче місце з елементів двох конфігурацій; ціна й придатність до завдання однакові, а потреби користувачів і обмеження відомі. Я організовую простір навколо бажаного фізичного стану."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "shared-workspace",
          "aspect": "Физика",
          "position": 1,
          "tetradId": "физика-shared-workspace-v1",
          "contextDomain": "practical"
        },
        {
          "id": "psy_physics_1_2",
          "scale": "Физика|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Для регулярной работы есть несколько одинаково пригодных и доступных вариантов; различаются только их физические свойства. Я выбираю вариант по ощущению, которое хочу поддерживать во время работы.",
            "en": "Several equally suitable and accessible options are available for regular work; they differ only in their physical properties. I choose an option by the physical feel I want to maintain while working.",
            "uk": "Для регулярної роботи є кілька однаково придатних і доступних варіантів; вони відрізняються лише фізичними властивостями. Я обираю варіант за відчуттям, яке хочу підтримувати під час роботи."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "regular-use-choice",
          "aspect": "Физика",
          "position": 1,
          "tetradId": "физика-regular-use-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "psy_physics_1_3",
          "scale": "Физика|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В общем пространстве две конфигурации одинаково подходят задаче и по-разному отвечают известным потребностям в комфорте; их элементы можно сочетать. Я ориентирую договорённость на желаемое состояние пространства.",
            "en": "In a shared space, two configurations suit the task equally and meet known comfort needs in different ways; their elements can be combined. I orient the agreement toward the desired state of the space.",
            "uk": "У спільному просторі дві конфігурації однаково відповідають завданню й по-різному задовольняють відомі потреби в комфорті; їхні елементи можна поєднувати. Я орієнтую домовленість на бажаний стан простору."
          },
          "positionRole": "target",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "comfort-disagreement",
          "aspect": "Физика",
          "position": 1,
          "tetradId": "физика-comfort-disagreement-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_physics_2_1",
          "scale": "Физика|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда проектирует рабочее место из элементов двух конфигураций; цена и пригодность для задачи одинаковы, а потребности пользователей и ограничения известны. Я сочетаю элементы конфигураций в новое устройство пространства.",
            "en": "A team is designing a workspace from elements of two configurations; cost and task suitability are equal, and user needs and constraints are known. I combine elements of the configurations into a new spatial arrangement.",
            "uk": "Команда проєктує робоче місце з елементів двох конфігурацій; ціна й придатність до завдання однакові, а потреби користувачів і обмеження відомі. Я поєдную елементи конфігурацій у нове облаштування простору."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "shared-workspace",
          "aspect": "Физика",
          "position": 2,
          "tetradId": "физика-shared-workspace-v1",
          "contextDomain": "practical"
        },
        {
          "id": "psy_physics_2_2",
          "scale": "Физика|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Для регулярной работы есть несколько одинаково пригодных и доступных вариантов; различаются только их физические свойства. Я формирую способ регулярного использования через сочетание физических свойств.",
            "en": "Several equally suitable and accessible options are available for regular work; they differ only in their physical properties. I shape regular use through the combination of physical properties.",
            "uk": "Для регулярної роботи є кілька однаково придатних і доступних варіантів; вони відрізняються лише фізичними властивостями. Я формую спосіб регулярного використання через поєднання фізичних властивостей."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "regular-use-choice",
          "aspect": "Физика",
          "position": 2,
          "tetradId": "физика-regular-use-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "psy_physics_2_3",
          "scale": "Физика|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В общем пространстве две конфигурации одинаково подходят задаче и по-разному отвечают известным потребностям в комфорте; их элементы можно сочетать. Я соединяю элементы обеих конфигураций в новый вариант пространства.",
            "en": "In a shared space, two configurations suit the task equally and meet known comfort needs in different ways; their elements can be combined. I combine elements of both configurations into a new spatial option.",
            "uk": "У спільному просторі дві конфігурації однаково відповідають завданню й по-різному задовольняють відомі потреби в комфорті; їхні елементи можна поєднувати. Я поєдную елементи обох конфігурацій у новий варіант простору."
          },
          "positionRole": "creative",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "comfort-disagreement",
          "aspect": "Физика",
          "position": 2,
          "tetradId": "физика-comfort-disagreement-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_physics_3_1",
          "scale": "Физика|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда проектирует рабочее место из элементов двух конфигураций; цена и пригодность для задачи одинаковы, а потребности пользователей и ограничения известны. Я исключаю сочетания, нарушающие известные физические ограничения.",
            "en": "A team is designing a workspace from elements of two configurations; cost and task suitability are equal, and user needs and constraints are known. I rule out combinations that violate the known physical constraints.",
            "uk": "Команда проєктує робоче місце з елементів двох конфігурацій; ціна й придатність до завдання однакові, а потреби користувачів і обмеження відомі. Я відкидаю поєднання, що порушують відомі фізичні обмеження."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "shared-workspace",
          "aspect": "Физика",
          "position": 3,
          "tetradId": "физика-shared-workspace-v1",
          "contextDomain": "practical"
        },
        {
          "id": "psy_physics_3_2",
          "scale": "Физика|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Для регулярной работы есть несколько одинаково пригодных и доступных вариантов; различаются только их физические свойства. Я отбираю варианты по физическому условию работы.",
            "en": "Several equally suitable and accessible options are available for regular work; they differ only in their physical properties. I select the options by a physical condition of the work.",
            "uk": "Для регулярної роботи є кілька однаково придатних і доступних варіантів; вони відрізняються лише фізичними властивостями. Я відбираю варіанти за фізичною умовою роботи."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "regular-use-choice",
          "aspect": "Физика",
          "position": 3,
          "tetradId": "физика-regular-use-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "psy_physics_3_3",
          "scale": "Физика|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В общем пространстве две конфигурации одинаково подходят задаче и по-разному отвечают известным потребностям в комфорте; их элементы можно сочетать. Я сопоставляю сочетания с известными потребностями в комфорте.",
            "en": "In a shared space, two configurations suit the task equally and meet known comfort needs in different ways; their elements can be combined. I compare the combinations with the known comfort needs.",
            "uk": "У спільному просторі дві конфігурації однаково відповідають завданню й по-різному задовольняють відомі потреби в комфорті; їхні елементи можна поєднувати. Я зіставляю поєднання з відомими потребами в комфорті."
          },
          "positionRole": "criterion",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "comfort-disagreement",
          "aspect": "Физика",
          "position": 3,
          "tetradId": "физика-comfort-disagreement-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_physics_4_1",
          "scale": "Физика|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда проектирует рабочее место из элементов двух конфигураций; цена и пригодность для задачи одинаковы, а потребности пользователей и ограничения известны. Я настраиваю параметры пространства под известную задачу.",
            "en": "A team is designing a workspace from elements of two configurations; cost and task suitability are equal, and user needs and constraints are known. I configure the space parameters for the known task.",
            "uk": "Команда проєктує робоче місце з елементів двох конфігурацій; ціна й придатність до завдання однакові, а потреби користувачів і обмеження відомі. Я налаштовую параметри простору під відоме завдання."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 1,
          "facet": "frame",
          "context": "shared-workspace",
          "aspect": "Физика",
          "position": 4,
          "tetradId": "физика-shared-workspace-v1",
          "contextDomain": "practical"
        },
        {
          "id": "psy_physics_4_2",
          "scale": "Физика|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Для регулярной работы есть несколько одинаково пригодных и доступных вариантов; различаются только их физические свойства. Я подбираю вариант к рабочему процессу по его физическим свойствам.",
            "en": "Several equally suitable and accessible options are available for regular work; they differ only in their physical properties. I match an option to the work process by its physical properties.",
            "uk": "Для регулярної роботи є кілька однаково придатних і доступних варіантів; вони відрізняються лише фізичними властивостями. Я добираю варіант до робочого процесу за його фізичними властивостями."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 2,
          "facet": "process-result",
          "context": "regular-use-choice",
          "aspect": "Физика",
          "position": 4,
          "tetradId": "физика-regular-use-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "psy_physics_4_3",
          "scale": "Физика|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "В общем пространстве две конфигурации одинаково подходят задаче и по-разному отвечают известным потребностям в комфорте; их элементы можно сочетать. Я учитываю требования к комфорту при организации задачи.",
            "en": "In a shared space, two configurations suit the task equally and meet known comfort needs in different ways; their elements can be combined. I incorporate the comfort requirements when organizing the task.",
            "uk": "У спільному просторі дві конфігурації однаково відповідають завданню й по-різному задовольняють відомі потреби в комфорті; їхні елементи можна поєднувати. Я враховую вимоги до комфорту під час організації завдання."
          },
          "positionRole": "resource",
          "responseMode": "matched-vignette",
          "indicator": 3,
          "facet": "divergence",
          "context": "comfort-disagreement",
          "aspect": "Физика",
          "position": 4,
          "tetradId": "физика-comfort-disagreement-v1",
          "contextDomain": "change"
        },
        {
          "id": "psy_ac_1",
          "scale": "attention",
          "attention": 2,
          "version": "2.0",
          "text": {
            "ru": "Проверка внимательности: выберите вариант 2.",
            "en": "Attention check: choose option 2.",
            "uk": "Перевірка уважності: оберіть варіант 2."
          }
        }
      ]
    },
    "temporistics": {
      "version": "temporistics-pilot-v0.6",
      "mode": "position",
      "calibrationStatus": "precalibration",
      "measurementModel": "multi-indicator-position-contrast-v2",
      "minCellItems": 3,
      "labels": {
        "ru": [
          "Время и направление",
          "Как прошлое, настоящее, будущее и большой смысл участвуют в выборе как цель, материал решения, критерий или ресурс"
        ],
        "en": [
          "Time and direction",
          "How past, present, future, and larger meaning enter a choice as target, material, criterion, or resource"
        ],
        "uk": [
          "Час і напрям",
          "Як минуле, теперішнє, майбутнє й великий сенс беруть участь у виборі як ціль, матеріал рішення, критерій або ресурс"
        ]
      },
      "aspects": [
        "Past",
        "Present",
        "Future",
        "Eternity"
      ],
      "code": {
        "en": {
          "Past": "P",
          "Present": "N",
          "Future": "F",
          "Eternity": "E"
        },
        "ru": {
          "Past": "П",
          "Present": "Н",
          "Future": "Б",
          "Eternity": "В"
        },
        "uk": {
          "Past": "Ми",
          "Present": "Тп",
          "Future": "Мб",
          "Eternity": "Вч"
        }
      },
      "items": [
        {
          "id": "tmp_past_p1_personal_choice",
          "scale": "Past|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю один из двух осуществимых способов продолжить важное дело; известны текущие условия и итоги похожих прошлых решений. Я задаю желаемый результат как продолжение выбранной линии прошлого.",
            "en": "I am choosing between two feasible ways to continue an important undertaking; the current conditions and outcomes of similar past decisions are known. I define the desired outcome as a continuation of a chosen line from the past.",
            "uk": "Я обираю один із двох здійсненних способів продовжити важливу справу; відомі поточні умови й результати схожих минулих рішень. Я задаю бажаний результат як продовження обраної лінії минулого."
          },
          "positionRole": "target",
          "indicator": 1,
          "context": "personal-choice",
          "aspect": "Past",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "past-personal-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_past_p1_shared_project",
          "scale": "Past|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает следующий этап проекта; всем известны текущие ограничения, исходный замысел, прежние решения и их результаты. Сложившаяся линия проекта задаёт для меня результат следующего этапа.",
            "en": "A team is choosing the next project stage; the current constraints, original intent, earlier decisions, and their outcomes are known to everyone. For me, the established project line defines the outcome of the next stage.",
            "uk": "Команда обирає наступний етап проєкту; усім відомі поточні обмеження, початковий задум, попередні рішення та їхні результати. Сформована лінія проєкту задає для мене результат наступного етапу."
          },
          "positionRole": "target",
          "indicator": 2,
          "context": "shared-project-history",
          "aspect": "Past",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "past-shared-project-history-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_past_p1_new_evidence",
          "scale": "Past|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Перед решением появляется надёжный документ, меняющий моё представление о последовательности прошлых событий; текущая цель, условия и варианты остаются прежними. Обновлённая линия событий задаёт результат, к которому должно вести решение.",
            "en": "Before a decision, a reliable document changes my understanding of the sequence of past events; the current objective, conditions, and options remain unchanged. The revised line of events defines the outcome toward which the decision should lead.",
            "uk": "Перед рішенням з’являється надійний документ, що змінює моє уявлення про послідовність минулих подій; поточна мета, умови й варіанти залишаються незмінними. Оновлена лінія подій задає результат, до якого має вести рішення."
          },
          "positionRole": "target",
          "indicator": 3,
          "context": "new-historical-evidence",
          "aspect": "Past",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "past-new-historical-evidence-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_past_p2_personal_choice",
          "scale": "Past|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю один из двух осуществимых способов продолжить важное дело; известны текущие условия и итоги похожих прошлых решений. Последовательность прежних решений и последствий я превращаю в схему следующего шага.",
            "en": "I am choosing between two feasible ways to continue an important undertaking; the current conditions and outcomes of similar past decisions are known. I turn the sequence of earlier decisions and consequences into a plan for the next step.",
            "uk": "Я обираю один із двох здійсненних способів продовжити важливу справу; відомі поточні умови й результати схожих минулих рішень. Послідовність попередніх рішень і наслідків я перетворюю на схему наступного кроку."
          },
          "positionRole": "creative",
          "indicator": 1,
          "context": "personal-choice",
          "aspect": "Past",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "past-personal-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_past_p2_shared_project",
          "scale": "Past|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает следующий этап проекта; всем известны текущие ограничения, исходный замысел, прежние решения и их результаты. Историю прежних решений и результатов я преобразую в структуру следующего этапа.",
            "en": "A team is choosing the next project stage; the current constraints, original intent, earlier decisions, and their outcomes are known to everyone. I transform the history of earlier decisions and outcomes into the structure of the next stage.",
            "uk": "Команда обирає наступний етап проєкту; усім відомі поточні обмеження, початковий задум, попередні рішення та їхні результати. Історію попередніх рішень і результатів я перетворюю на структуру наступного етапу."
          },
          "positionRole": "creative",
          "indicator": 2,
          "context": "shared-project-history",
          "aspect": "Past",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "past-shared-project-history-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_past_p2_new_evidence",
          "scale": "Past|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Перед решением появляется надёжный документ, меняющий моё представление о последовательности прошлых событий; текущая цель, условия и варианты остаются прежними. Обновлённое описание прошлых событий я превращаю в схему текущего решения.",
            "en": "Before a decision, a reliable document changes my understanding of the sequence of past events; the current objective, conditions, and options remain unchanged. I turn the revised account of past events into a structure for the current decision.",
            "uk": "Перед рішенням з’являється надійний документ, що змінює моє уявлення про послідовність минулих подій; поточна мета, умови й варіанти залишаються незмінними. Оновлений опис минулих подій я перетворюю на схему поточного рішення."
          },
          "positionRole": "creative",
          "indicator": 3,
          "context": "new-historical-evidence",
          "aspect": "Past",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "past-new-historical-evidence-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_past_p3_personal_choice",
          "scale": "Past|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю один из двух осуществимых способов продолжить важное дело; известны текущие условия и итоги похожих прошлых решений. Последствия прежних решений определяют, какой вариант я считаю приемлемым.",
            "en": "I am choosing between two feasible ways to continue an important undertaking; the current conditions and outcomes of similar past decisions are known. The consequences of earlier decisions determine which option I consider acceptable.",
            "uk": "Я обираю один із двох здійсненних способів продовжити важливу справу; відомі поточні умови й результати схожих минулих рішень. Наслідки попередніх рішень визначають, який варіант я вважаю прийнятним."
          },
          "positionRole": "criterion",
          "indicator": 1,
          "context": "personal-choice",
          "aspect": "Past",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "past-personal-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_past_p3_shared_project",
          "scale": "Past|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает следующий этап проекта; всем известны текущие ограничения, исходный замысел, прежние решения и их результаты. Для меня приемлемо продолжение, соответствующее результатам прежних этапов.",
            "en": "A team is choosing the next project stage; the current constraints, original intent, earlier decisions, and their outcomes are known to everyone. For me, an acceptable continuation is one that is consistent with the outcomes of earlier stages.",
            "uk": "Команда обирає наступний етап проєкту; усім відомі поточні обмеження, початковий задум, попередні рішення та їхні результати. Для мене прийнятним є продовження, що відповідає результатам попередніх етапів."
          },
          "positionRole": "criterion",
          "indicator": 2,
          "context": "shared-project-history",
          "aspect": "Past",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "past-shared-project-history-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_past_p3_new_evidence",
          "scale": "Past|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Перед решением появляется надёжный документ, меняющий моё представление о последовательности прошлых событий; текущая цель, условия и варианты остаются прежними. Я считаю приемлемым вариант, согласующийся с обновлённой последовательностью событий.",
            "en": "Before a decision, a reliable document changes my understanding of the sequence of past events; the current objective, conditions, and options remain unchanged. I consider an option acceptable when it is consistent with the revised sequence of events.",
            "uk": "Перед рішенням з’являється надійний документ, що змінює моє уявлення про послідовність минулих подій; поточна мета, умови й варіанти залишаються незмінними. Я вважаю прийнятним варіант, що узгоджується з оновленою послідовністю подій."
          },
          "positionRole": "criterion",
          "indicator": 3,
          "context": "new-historical-evidence",
          "aspect": "Past",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "past-new-historical-evidence-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_past_p4_personal_choice",
          "scale": "Past|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю один из двух осуществимых способов продолжить важное дело; известны текущие условия и итоги похожих прошлых решений. Я использую сведения о прежних решениях как справочный материал при выборе.",
            "en": "I am choosing between two feasible ways to continue an important undertaking; the current conditions and outcomes of similar past decisions are known. I use information about earlier decisions as reference material for the choice.",
            "uk": "Я обираю один із двох здійсненних способів продовжити важливу справу; відомі поточні умови й результати схожих минулих рішень. Я використовую відомості про попередні рішення як довідковий матеріал під час вибору."
          },
          "positionRole": "resource",
          "indicator": 1,
          "context": "personal-choice",
          "aspect": "Past",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "past-personal-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_past_p4_shared_project",
          "scale": "Past|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает следующий этап проекта; всем известны текущие ограничения, исходный замысел, прежние решения и их результаты. Я использую историю проекта как справочный материал для следующего этапа.",
            "en": "A team is choosing the next project stage; the current constraints, original intent, earlier decisions, and their outcomes are known to everyone. I use the project history as reference material for the next stage.",
            "uk": "Команда обирає наступний етап проєкту; усім відомі поточні обмеження, початковий задум, попередні рішення та їхні результати. Я використовую історію проєкту як довідковий матеріал для наступного етапу."
          },
          "positionRole": "resource",
          "indicator": 2,
          "context": "shared-project-history",
          "aspect": "Past",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "past-shared-project-history-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_past_p4_new_evidence",
          "scale": "Past|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Перед решением появляется надёжный документ, меняющий моё представление о последовательности прошлых событий; текущая цель, условия и варианты остаются прежними. Я включаю новые сведения о прошлом в материалы текущего решения.",
            "en": "Before a decision, a reliable document changes my understanding of the sequence of past events; the current objective, conditions, and options remain unchanged. I include the new information about the past among the materials for the current decision.",
            "uk": "Перед рішенням з’являється надійний документ, що змінює моє уявлення про послідовність минулих подій; поточна мета, умови й варіанти залишаються незмінними. Я включаю нові відомості про минуле до матеріалів поточного рішення."
          },
          "positionRole": "resource",
          "indicator": 3,
          "context": "new-historical-evidence",
          "aspect": "Past",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "past-new-historical-evidence-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_present_p1_current_conditions",
          "scale": "Present|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Для текущей задачи нужно выбрать ближайший результат и способ действия; известны более широкая цель, роли, доступное время и ресурсы. Я задаю ближайший результат как состояние, которого нужно достичь сейчас.",
            "en": "A near-term outcome and course of action must be chosen for a current task; the broader objective, roles, available time, and resources are known. I define the near-term outcome as the state that needs to be reached now.",
            "uk": "Для поточного завдання потрібно обрати найближчий результат і спосіб дії; відомі ширша мета, ролі, доступний час і ресурси. Я задаю найближчий результат як стан, якого потрібно досягти зараз."
          },
          "positionRole": "target",
          "indicator": 1,
          "context": "plan-vs-current-conditions",
          "aspect": "Present",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "present-plan-vs-current-conditions-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_present_p1_team_session",
          "scale": "Present|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "На встрече группа выбирает следующее действие; известны цель проекта, состав участников, повестка и оставшееся время. Результат, который нужно получить на этой встрече, задаёт направление выбора.",
            "en": "At a meeting, a group is choosing its next action; the project objective, participants, agenda, and remaining time are known. The outcome to be reached in this meeting defines the direction of the choice.",
            "uk": "На зустрічі група обирає наступну дію; відомі мета проєкту, склад учасників, порядок денний і час, що залишився. Результат, якого потрібно досягти на цій зустрічі, задає напрям вибору."
          },
          "positionRole": "target",
          "indicator": 2,
          "context": "live-team-session",
          "aspect": "Present",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "present-live-team-session-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_present_p1_unfamiliar_setting",
          "scale": "Present|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я прихожу в незнакомую организацию выполнить конкретную задачу; её цель известна, а роли, правила и ресурсы видны на месте. Состояние, которое нужно получить здесь за время моего участия, задаёт результат.",
            "en": "I enter an unfamiliar organization to complete a specific task; its objective is known, while the roles, rules, and resources can be observed on site. The state to be reached here during my involvement defines the outcome.",
            "uk": "Я приходжу до незнайомої організації виконати конкретне завдання; його мета відома, а ролі, правила й ресурси видно на місці. Стан, якого потрібно досягти тут за час моєї участі, задає результат."
          },
          "positionRole": "target",
          "indicator": 3,
          "context": "unfamiliar-setting",
          "aspect": "Present",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "present-unfamiliar-setting-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_present_p2_current_conditions",
          "scale": "Present|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Для текущей задачи нужно выбрать ближайший результат и способ действия; известны более широкая цель, роли, доступное время и ресурсы. Из текущих ролей, времени и ресурсов я составляю способ действия.",
            "en": "A near-term outcome and course of action must be chosen for a current task; the broader objective, roles, available time, and resources are known. I compose a course of action from the current roles, time, and resources.",
            "uk": "Для поточного завдання потрібно обрати найближчий результат і спосіб дії; відомі ширша мета, ролі, доступний час і ресурси. Із поточних ролей, часу й ресурсів я складаю спосіб дії."
          },
          "positionRole": "creative",
          "indicator": 1,
          "context": "plan-vs-current-conditions",
          "aspect": "Present",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "present-plan-vs-current-conditions-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_present_p2_team_session",
          "scale": "Present|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "На встрече группа выбирает следующее действие; известны цель проекта, состав участников, повестка и оставшееся время. Из текущих вкладов участников и оставшегося времени я формирую следующее действие.",
            "en": "At a meeting, a group is choosing its next action; the project objective, participants, agenda, and remaining time are known. I form the next action from the participants’ current contributions and the remaining time.",
            "uk": "На зустрічі група обирає наступну дію; відомі мета проєкту, склад учасників, порядок денний і час, що залишився. Із поточних внесків учасників і часу, що залишився, я формую наступну дію."
          },
          "positionRole": "creative",
          "indicator": 2,
          "context": "live-team-session",
          "aspect": "Present",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "present-live-team-session-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_present_p2_unfamiliar_setting",
          "scale": "Present|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я прихожу в незнакомую организацию выполнить конкретную задачу; её цель известна, а роли, правила и ресурсы видны на месте. Наблюдаемые роли, правила и ресурсы я соединяю в способ своего участия.",
            "en": "I enter an unfamiliar organization to complete a specific task; its objective is known, while the roles, rules, and resources can be observed on site. I combine the observed roles, rules, and resources into a way of participating.",
            "uk": "Я приходжу до незнайомої організації виконати конкретне завдання; його мета відома, а ролі, правила й ресурси видно на місці. Спостережувані ролі, правила й ресурси я поєдную у спосіб своєї участі."
          },
          "positionRole": "creative",
          "indicator": 3,
          "context": "unfamiliar-setting",
          "aspect": "Present",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "present-unfamiliar-setting-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_present_p3_current_conditions",
          "scale": "Present|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Для текущей задачи нужно выбрать ближайший результат и способ действия; известны более широкая цель, роли, доступное время и ресурсы. Я считаю действие приемлемым, если оно соответствует текущим ролям, времени и ресурсам.",
            "en": "A near-term outcome and course of action must be chosen for a current task; the broader objective, roles, available time, and resources are known. I consider an action acceptable when it fits the current roles, time, and resources.",
            "uk": "Для поточного завдання потрібно обрати найближчий результат і спосіб дії; відомі ширша мета, ролі, доступний час і ресурси. Я вважаю дію прийнятною, якщо вона відповідає поточним ролям, часу й ресурсам."
          },
          "positionRole": "criterion",
          "indicator": 1,
          "context": "plan-vs-current-conditions",
          "aspect": "Present",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "present-plan-vs-current-conditions-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_present_p3_team_session",
          "scale": "Present|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "На встрече группа выбирает следующее действие; известны цель проекта, состав участников, повестка и оставшееся время. Состояние обсуждения, состав участников и оставшееся время определяют, какое действие приемлемо.",
            "en": "At a meeting, a group is choosing its next action; the project objective, participants, agenda, and remaining time are known. The state of the discussion, the participants, and the remaining time determine which action is acceptable.",
            "uk": "На зустрічі група обирає наступну дію; відомі мета проєкту, склад учасників, порядок денний і час, що залишився. Стан обговорення, склад учасників і час, що залишився, визначають, яка дія є прийнятною."
          },
          "positionRole": "criterion",
          "indicator": 2,
          "context": "live-team-session",
          "aspect": "Present",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "present-live-team-session-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_present_p3_unfamiliar_setting",
          "scale": "Present|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я прихожу в незнакомую организацию выполнить конкретную задачу; её цель известна, а роли, правила и ресурсы видны на месте. Наблюдаемые условия определяют, какие действия приемлемы в этой обстановке.",
            "en": "I enter an unfamiliar organization to complete a specific task; its objective is known, while the roles, rules, and resources can be observed on site. The observed conditions determine which actions are acceptable in this setting.",
            "uk": "Я приходжу до незнайомої організації виконати конкретне завдання; його мета відома, а ролі, правила й ресурси видно на місці. Спостережувані умови визначають, які дії є прийнятними в цій обстановці."
          },
          "positionRole": "criterion",
          "indicator": 3,
          "context": "unfamiliar-setting",
          "aspect": "Present",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "present-unfamiliar-setting-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_present_p4_current_conditions",
          "scale": "Present|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Для текущей задачи нужно выбрать ближайший результат и способ действия; известны более широкая цель, роли, доступное время и ресурсы. Я использую сведения о текущих условиях как исходные данные для задачи.",
            "en": "A near-term outcome and course of action must be chosen for a current task; the broader objective, roles, available time, and resources are known. I use information about the current conditions as input for the task.",
            "uk": "Для поточного завдання потрібно обрати найближчий результат і спосіб дії; відомі ширша мета, ролі, доступний час і ресурси. Я використовую відомості про поточні умови як вихідні дані для завдання."
          },
          "positionRole": "resource",
          "indicator": 1,
          "context": "plan-vs-current-conditions",
          "aspect": "Present",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "present-plan-vs-current-conditions-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_present_p4_team_session",
          "scale": "Present|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "На встрече группа выбирает следующее действие; известны цель проекта, состав участников, повестка и оставшееся время. Я использую ход текущего обсуждения как контекст для следующего действия.",
            "en": "At a meeting, a group is choosing its next action; the project objective, participants, agenda, and remaining time are known. I use the current discussion as context for the next action.",
            "uk": "На зустрічі група обирає наступну дію; відомі мета проєкту, склад учасників, порядок денний і час, що залишився. Я використовую перебіг поточного обговорення як контекст для наступної дії."
          },
          "positionRole": "resource",
          "indicator": 2,
          "context": "live-team-session",
          "aspect": "Present",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "present-live-team-session-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_present_p4_unfamiliar_setting",
          "scale": "Present|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я прихожу в незнакомую организацию выполнить конкретную задачу; её цель известна, а роли, правила и ресурсы видны на месте. Я использую наблюдаемые условия как исходные данные при выполнении задачи.",
            "en": "I enter an unfamiliar organization to complete a specific task; its objective is known, while the roles, rules, and resources can be observed on site. I use the observed conditions as input while carrying out the task.",
            "uk": "Я приходжу до незнайомої організації виконати конкретне завдання; його мета відома, а ролі, правила й ресурси видно на місці. Я використовую спостережувані умови як вихідні дані під час виконання завдання."
          },
          "positionRole": "resource",
          "indicator": 3,
          "context": "unfamiliar-setting",
          "aspect": "Present",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "present-unfamiliar-setting-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_future_p1_personal_choice",
          "scale": "Future|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю один из двух осуществимых личных вариантов; мои текущие потребности известны, а прогноз ближайших и отдалённых последствий каждого доступен. Желаемое будущее состояние задаёт для меня результат выбора.",
            "en": "I am choosing between two feasible personal options; my current needs are known, and a forecast of each option’s near-term and long-term consequences is available. The desired future state defines the outcome of the choice for me.",
            "uk": "Я обираю один із двох здійсненних особистих варіантів; мої поточні потреби відомі, а прогноз найближчих і віддалених наслідків кожного доступний. Бажаний майбутній стан задає для мене результат вибору."
          },
          "positionRole": "target",
          "indicator": 1,
          "context": "personal-long-range-choice",
          "aspect": "Future",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "future-personal-long-range-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_future_p1_team_roadmap",
          "scale": "Future|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает один из двух осуществимых планов; известны требования и текущие ограничения, а для обоих доступны прогнозы этапов и последствий. Представленное в прогнозе конечное состояние задаёт результат плана.",
            "en": "A team is choosing between two feasible plans; the requirements and current constraints are known, and forecasts of the stages and consequences are available for both. The end state represented in the forecast defines the outcome of the plan.",
            "uk": "Команда обирає один із двох здійсненних планів; відомі вимоги й поточні обмеження, а для обох доступні прогнози етапів і наслідків. Представлений у прогнозі кінцевий стан задає результат плану."
          },
          "positionRole": "target",
          "indicator": 2,
          "context": "team-roadmap",
          "aspect": "Future",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "future-team-roadmap-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_future_p1_disrupted_forecast",
          "scale": "Future|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Новый надёжный прогноз делает прежний план невыполнимым; известны текущие требования и прогнозируемые последствия осуществимых вариантов замены. Осуществимое будущее состояние задаёт конечный результат решения.",
            "en": "A new reliable forecast makes the previous plan unworkable; the current requirements and projected consequences of feasible replacements are known. A feasible future state defines the final outcome of the decision.",
            "uk": "Новий надійний прогноз робить попередній план нездійсненним; відомі поточні вимоги й прогнозовані наслідки здійсненних варіантів заміни. Здійсненний майбутній стан задає кінцевий результат рішення."
          },
          "positionRole": "target",
          "indicator": 3,
          "context": "disrupted-forecast",
          "aspect": "Future",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "future-disrupted-forecast-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_future_p2_personal_choice",
          "scale": "Future|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю один из двух осуществимых личных вариантов; мои текущие потребности известны, а прогноз ближайших и отдалённых последствий каждого доступен. Прогнозируемую последовательность последствий я превращаю в ход дальнейших действий.",
            "en": "I am choosing between two feasible personal options; my current needs are known, and a forecast of each option’s near-term and long-term consequences is available. I turn the projected sequence of consequences into a course of further action.",
            "uk": "Я обираю один із двох здійсненних особистих варіантів; мої поточні потреби відомі, а прогноз найближчих і віддалених наслідків кожного доступний. Прогнозовану послідовність наслідків я перетворюю на хід подальших дій."
          },
          "positionRole": "creative",
          "indicator": 1,
          "context": "personal-long-range-choice",
          "aspect": "Future",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "future-personal-long-range-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_future_p2_team_roadmap",
          "scale": "Future|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает один из двух осуществимых планов; известны требования и текущие ограничения, а для обоих доступны прогнозы этапов и последствий. Из прогнозируемых этапов я формирую маршрут выполнения плана.",
            "en": "A team is choosing between two feasible plans; the requirements and current constraints are known, and forecasts of the stages and consequences are available for both. I form the plan’s implementation route from the projected stages.",
            "uk": "Команда обирає один із двох здійсненних планів; відомі вимоги й поточні обмеження, а для обох доступні прогнози етапів і наслідків. Із прогнозованих етапів я формую маршрут виконання плану."
          },
          "positionRole": "creative",
          "indicator": 2,
          "context": "team-roadmap",
          "aspect": "Future",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "future-team-roadmap-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_future_p2_disrupted_forecast",
          "scale": "Future|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Новый надёжный прогноз делает прежний план невыполнимым; известны текущие требования и прогнозируемые последствия осуществимых вариантов замены. Обновлённую последовательность будущих событий я превращаю в структуру нового плана.",
            "en": "A new reliable forecast makes the previous plan unworkable; the current requirements and projected consequences of feasible replacements are known. I turn the revised sequence of future events into the structure of a new plan.",
            "uk": "Новий надійний прогноз робить попередній план нездійсненним; відомі поточні вимоги й прогнозовані наслідки здійсненних варіантів заміни. Оновлену послідовність майбутніх подій я перетворюю на структуру нового плану."
          },
          "positionRole": "creative",
          "indicator": 3,
          "context": "disrupted-forecast",
          "aspect": "Future",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "future-disrupted-forecast-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_future_p3_personal_choice",
          "scale": "Future|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю один из двух осуществимых личных вариантов; мои текущие потребности известны, а прогноз ближайших и отдалённых последствий каждого доступен. Я считаю вариант приемлемым по его прогнозируемым последствиям.",
            "en": "I am choosing between two feasible personal options; my current needs are known, and a forecast of each option’s near-term and long-term consequences is available. I consider an option acceptable based on its projected consequences.",
            "uk": "Я обираю один із двох здійсненних особистих варіантів; мої поточні потреби відомі, а прогноз найближчих і віддалених наслідків кожного доступний. Я вважаю варіант прийнятним за його прогнозованими наслідками."
          },
          "positionRole": "criterion",
          "indicator": 1,
          "context": "personal-long-range-choice",
          "aspect": "Future",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "future-personal-long-range-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_future_p3_team_roadmap",
          "scale": "Future|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает один из двух осуществимых планов; известны требования и текущие ограничения, а для обоих доступны прогнозы этапов и последствий. Прогнозируемые последствия определяют приемлемость плана.",
            "en": "A team is choosing between two feasible plans; the requirements and current constraints are known, and forecasts of the stages and consequences are available for both. The projected consequences determine whether a plan is acceptable.",
            "uk": "Команда обирає один із двох здійсненних планів; відомі вимоги й поточні обмеження, а для обох доступні прогнози етапів і наслідків. Прогнозовані наслідки визначають прийнятність плану."
          },
          "positionRole": "criterion",
          "indicator": 2,
          "context": "team-roadmap",
          "aspect": "Future",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "future-team-roadmap-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_future_p3_disrupted_forecast",
          "scale": "Future|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Новый надёжный прогноз делает прежний план невыполнимым; известны текущие требования и прогнозируемые последствия осуществимых вариантов замены. Приемлемость замены для меня зависит от её прогнозируемых последствий.",
            "en": "A new reliable forecast makes the previous plan unworkable; the current requirements and projected consequences of feasible replacements are known. For me, a replacement’s acceptability depends on its projected consequences.",
            "uk": "Новий надійний прогноз робить попередній план нездійсненним; відомі поточні вимоги й прогнозовані наслідки здійсненних варіантів заміни. Прийнятність заміни для мене залежить від її прогнозованих наслідків."
          },
          "positionRole": "criterion",
          "indicator": 3,
          "context": "disrupted-forecast",
          "aspect": "Future",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "future-disrupted-forecast-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_future_p4_personal_choice",
          "scale": "Future|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю один из двух осуществимых личных вариантов; мои текущие потребности известны, а прогноз ближайших и отдалённых последствий каждого доступен. Я использую прогнозируемые последствия как исходные данные для выбора.",
            "en": "I am choosing between two feasible personal options; my current needs are known, and a forecast of each option’s near-term and long-term consequences is available. I use the projected consequences as input for the choice.",
            "uk": "Я обираю один із двох здійсненних особистих варіантів; мої поточні потреби відомі, а прогноз найближчих і віддалених наслідків кожного доступний. Я використовую прогнозовані наслідки як вихідні дані для вибору."
          },
          "positionRole": "resource",
          "indicator": 1,
          "context": "personal-long-range-choice",
          "aspect": "Future",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "future-personal-long-range-choice-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_future_p4_team_roadmap",
          "scale": "Future|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает один из двух осуществимых планов; известны требования и текущие ограничения, а для обоих доступны прогнозы этапов и последствий. Я использую прогнозируемые этапы и последствия как исходные данные для плана.",
            "en": "A team is choosing between two feasible plans; the requirements and current constraints are known, and forecasts of the stages and consequences are available for both. I use the projected stages and consequences as input for the plan.",
            "uk": "Команда обирає один із двох здійсненних планів; відомі вимоги й поточні обмеження, а для обох доступні прогнози етапів і наслідків. Я використовую прогнозовані етапи й наслідки як вихідні дані для плану."
          },
          "positionRole": "resource",
          "indicator": 2,
          "context": "team-roadmap",
          "aspect": "Future",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "future-team-roadmap-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_future_p4_disrupted_forecast",
          "scale": "Future|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Новый надёжный прогноз делает прежний план невыполнимым; известны текущие требования и прогнозируемые последствия осуществимых вариантов замены. Я включаю новый прогноз в исходные данные для выбора замены.",
            "en": "A new reliable forecast makes the previous plan unworkable; the current requirements and projected consequences of feasible replacements are known. I include the new forecast among the inputs for choosing a replacement.",
            "uk": "Новий надійний прогноз робить попередній план нездійсненним; відомі поточні вимоги й прогнозовані наслідки здійсненних варіантів заміни. Я включаю новий прогноз до вихідних даних для вибору заміни."
          },
          "positionRole": "resource",
          "indicator": 3,
          "context": "disrupted-forecast",
          "aspect": "Future",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "future-disrupted-forecast-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_eternity_p1_major_goal",
          "scale": "Eternity|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю одну из двух осуществимых долгосрочных целей; известны ресурсы, последствия и связанные с каждой более широкие замыслы и принципы. Более широкий замысел задаёт результат, которому должен служить выбор.",
            "en": "I am choosing between two feasible long-term goals; the resources, consequences, and broader purposes and principles linked to each are known. The broader purpose defines the outcome that the choice should serve.",
            "uk": "Я обираю одну з двох здійсненних довгострокових цілей; відомі ресурси, наслідки та пов’язані з кожною ширші задуми й принципи. Ширший задум задає результат, якому має служити вибір."
          },
          "positionRole": "target",
          "indicator": 1,
          "context": "major-goal",
          "aspect": "Eternity",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-major-goal-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_eternity_p1_shared_mission",
          "scale": "Eternity|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает одну из двух осуществимых стратегий; известны ближайшая задача, ограничения, последствия и согласованное предназначение проекта. Общее предназначение задаёт результат, которому должна служить стратегия.",
            "en": "A team is choosing between two feasible strategies; the immediate task, constraints, consequences, and agreed project purpose are known. The shared purpose defines the outcome that the strategy should serve.",
            "uk": "Команда обирає одну з двох здійсненних стратегій; відомі найближче завдання, обмеження, наслідки й узгоджене призначення проєкту. Спільне призначення задає результат, якому має служити стратегія."
          },
          "positionRole": "target",
          "indicator": 2,
          "context": "shared-mission",
          "aspect": "Eternity",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-shared-mission-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_eternity_p1_meaning_conflict",
          "scale": "Eternity|1",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Два осуществимых решения соответствуют разным трактовкам предназначения проекта; известны текущие ограничения и практические последствия обоих. Трактовка того, чему должен служить проект, задаёт желаемый результат.",
            "en": "Two feasible decisions correspond to different interpretations of the project purpose; the current constraints and practical consequences of both are known. The interpretation of what the project should serve defines the desired outcome.",
            "uk": "Два здійсненні рішення відповідають різним трактуванням призначення проєкту; відомі поточні обмеження й практичні наслідки обох. Трактування того, чому має служити проєкт, задає бажаний результат."
          },
          "positionRole": "target",
          "indicator": 3,
          "context": "meaning-conflict",
          "aspect": "Eternity",
          "position": 1,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-meaning-conflict-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_eternity_p2_major_goal",
          "scale": "Eternity|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю одну из двух осуществимых долгосрочных целей; известны ресурсы, последствия и связанные с каждой более широкие замыслы и принципы. Цель, более широкий замысел и принципы я связываю в основание для действия.",
            "en": "I am choosing between two feasible long-term goals; the resources, consequences, and broader purposes and principles linked to each are known. I connect the goal, broader purpose, and principles into a basis for action.",
            "uk": "Я обираю одну з двох здійсненних довгострокових цілей; відомі ресурси, наслідки та пов’язані з кожною ширші задуми й принципи. Ціль, ширший задум і принципи я поєдную в основу для дії."
          },
          "positionRole": "creative",
          "indicator": 1,
          "context": "major-goal",
          "aspect": "Eternity",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-major-goal-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_eternity_p2_shared_mission",
          "scale": "Eternity|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает одну из двух осуществимых стратегий; известны ближайшая задача, ограничения, последствия и согласованное предназначение проекта. Предназначение, ближайшую задачу и последствия я соединяю в структуру стратегии.",
            "en": "A team is choosing between two feasible strategies; the immediate task, constraints, consequences, and agreed project purpose are known. I combine the purpose, immediate task, and consequences into the structure of the strategy.",
            "uk": "Команда обирає одну з двох здійсненних стратегій; відомі найближче завдання, обмеження, наслідки й узгоджене призначення проєкту. Призначення, найближче завдання й наслідки я поєдную в структуру стратегії."
          },
          "positionRole": "creative",
          "indicator": 2,
          "context": "shared-mission",
          "aspect": "Eternity",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-shared-mission-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_eternity_p2_meaning_conflict",
          "scale": "Eternity|2",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Два осуществимых решения соответствуют разным трактовкам предназначения проекта; известны текущие ограничения и практические последствия обоих. Соотношение двух трактовок я преобразую в формулировку решения.",
            "en": "Two feasible decisions correspond to different interpretations of the project purpose; the current constraints and practical consequences of both are known. I transform the relationship between the two interpretations into a formulation for the decision.",
            "uk": "Два здійсненні рішення відповідають різним трактуванням призначення проєкту; відомі поточні обмеження й практичні наслідки обох. Співвідношення двох трактувань я перетворюю на формулювання рішення."
          },
          "positionRole": "creative",
          "indicator": 3,
          "context": "meaning-conflict",
          "aspect": "Eternity",
          "position": 2,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-meaning-conflict-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_eternity_p3_major_goal",
          "scale": "Eternity|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю одну из двух осуществимых долгосрочных целей; известны ресурсы, последствия и связанные с каждой более широкие замыслы и принципы. Я считаю цель приемлемой, если она согласуется с принципом, применимым в разных ситуациях.",
            "en": "I am choosing between two feasible long-term goals; the resources, consequences, and broader purposes and principles linked to each are known. I consider a goal acceptable when it is consistent with a principle that applies across situations.",
            "uk": "Я обираю одну з двох здійсненних довгострокових цілей; відомі ресурси, наслідки та пов’язані з кожною ширші задуми й принципи. Я вважаю ціль прийнятною, якщо вона узгоджується з принципом, застосовним у різних ситуаціях."
          },
          "positionRole": "criterion",
          "indicator": 1,
          "context": "major-goal",
          "aspect": "Eternity",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-major-goal-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_eternity_p3_shared_mission",
          "scale": "Eternity|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает одну из двух осуществимых стратегий; известны ближайшая задача, ограничения, последствия и согласованное предназначение проекта. Для меня стратегия приемлема, когда её результат соответствует общему предназначению.",
            "en": "A team is choosing between two feasible strategies; the immediate task, constraints, consequences, and agreed project purpose are known. For me, a strategy is acceptable when its outcome is consistent with the shared purpose.",
            "uk": "Команда обирає одну з двох здійсненних стратегій; відомі найближче завдання, обмеження, наслідки й узгоджене призначення проєкту. Для мене стратегія прийнятна, коли її результат відповідає спільному призначенню."
          },
          "positionRole": "criterion",
          "indicator": 2,
          "context": "shared-mission",
          "aspect": "Eternity",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-shared-mission-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_eternity_p3_meaning_conflict",
          "scale": "Eternity|3",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Два осуществимых решения соответствуют разным трактовкам предназначения проекта; известны текущие ограничения и практические последствия обоих. Принятая трактовка предназначения определяет, какое решение я считаю приемлемым.",
            "en": "Two feasible decisions correspond to different interpretations of the project purpose; the current constraints and practical consequences of both are known. The adopted interpretation of the purpose determines which decision I consider acceptable.",
            "uk": "Два здійсненні рішення відповідають різним трактуванням призначення проєкту; відомі поточні обмеження й практичні наслідки обох. Прийняте трактування призначення визначає, яке рішення я вважаю прийнятним."
          },
          "positionRole": "criterion",
          "indicator": 3,
          "context": "meaning-conflict",
          "aspect": "Eternity",
          "position": 3,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-meaning-conflict-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_eternity_p4_major_goal",
          "scale": "Eternity|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я выбираю одну из двух осуществимых долгосрочных целей; известны ресурсы, последствия и связанные с каждой более широкие замыслы и принципы. Я использую более широкие замыслы и принципы как смысловой контекст выбора.",
            "en": "I am choosing between two feasible long-term goals; the resources, consequences, and broader purposes and principles linked to each are known. I use the broader purposes and principles as interpretive context for the choice.",
            "uk": "Я обираю одну з двох здійсненних довгострокових цілей; відомі ресурси, наслідки та пов’язані з кожною ширші задуми й принципи. Я використовую ширші задуми й принципи як смисловий контекст вибору."
          },
          "positionRole": "resource",
          "indicator": 1,
          "context": "major-goal",
          "aspect": "Eternity",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-major-goal-v1",
          "contextDomain": "personal"
        },
        {
          "id": "tmp_eternity_p4_shared_mission",
          "scale": "Eternity|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Команда выбирает одну из двух осуществимых стратегий; известны ближайшая задача, ограничения, последствия и согласованное предназначение проекта. Я использую предназначение проекта как общий контекст разработки стратегии.",
            "en": "A team is choosing between two feasible strategies; the immediate task, constraints, consequences, and agreed project purpose are known. I use the project purpose as shared context for developing the strategy.",
            "uk": "Команда обирає одну з двох здійсненних стратегій; відомі найближче завдання, обмеження, наслідки й узгоджене призначення проєкту. Я використовую призначення проєкту як спільний контекст розроблення стратегії."
          },
          "positionRole": "resource",
          "indicator": 2,
          "context": "shared-mission",
          "aspect": "Eternity",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-shared-mission-v1",
          "contextDomain": "team"
        },
        {
          "id": "tmp_eternity_p4_meaning_conflict",
          "scale": "Eternity|4",
          "version": "3.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Два осуществимых решения соответствуют разным трактовкам предназначения проекта; известны текущие ограничения и практические последствия обоих. Я использую обе трактовки предназначения как контекст текущего решения.",
            "en": "Two feasible decisions correspond to different interpretations of the project purpose; the current constraints and practical consequences of both are known. I use both interpretations of the purpose as context for the current decision.",
            "uk": "Два здійсненні рішення відповідають різним трактуванням призначення проєкту; відомі поточні обмеження й практичні наслідки обох. Я використовую обидва трактування призначення як контекст поточного рішення."
          },
          "positionRole": "resource",
          "indicator": 3,
          "context": "meaning-conflict",
          "aspect": "Eternity",
          "position": 4,
          "responseMode": "matched-vignette",
          "tetradId": "eternity-meaning-conflict-v1",
          "contextDomain": "change"
        },
        {
          "id": "tmp_ac_1",
          "scale": "attention",
          "attention": 2,
          "version": "2.0",
          "text": {
            "ru": "Проверка внимательности: выберите вариант 2.",
            "en": "Attention check: choose option 2.",
            "uk": "Перевірка уважності: оберіть варіант 2."
          }
        }
      ]
    }
  }
}
~~~
