---
title: Before We Build pilot question bank
type: instrument
status: pilot
schemaVersion: 1.0.0
bankVersion: 2026-07-22.1
---

# Before We Build pilot question bank

This is the single canonical browser question bank. Keep the payload below valid JSON and update bankVersion whenever a browser-visible item changes. The site loads this Markdown file and accepts only the question-bank JSON block.

~~~question-bank
{
  "schemaVersion": "1.0.0",
  "bankVersion": "2026-07-22.1",
  "tests": {
    "socionics": {
      "version": "socionics-pilot-v0.3",
      "mode": "socionics",
      "labels": {
        "ru": [
          "Информация и общение",
          "Как вы воспринимаете, сортируете и передаете информацию"
        ],
        "en": [
          "Information and communication",
          "How you perceive, sort, and exchange information"
        ],
        "uk": [
          "Інформація і спілкування",
          "Як ви сприймаєте, сортуєте й передаєте інформацію"
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
          "version": "1.1",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Разбираясь в новой теме, я обычно сначала ищу, как её части связаны и образуют общую систему.",
            "en": "When learning a new topic, I usually first look for how its parts connect and form a coherent system.",
            "uk": "Розбираючись у новій темі, я зазвичай спочатку шукаю, як її частини пов’язані й утворюють цілісну систему."
          }
        },
        {
          "id": "soc_2",
          "scale": "Ti",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Перед спором мне важно договориться, что именно значат слова.",
            "en": "Before an argument, I need to agree on what the words mean.",
            "uk": "Перед суперечкою мені важливо домовитися, що саме означають слова."
          }
        },
        {
          "id": "soc_3",
          "scale": "Te",
          "version": "1.0",
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
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Объяснение кажется мне слабым, если непонятно, что с ним делать.",
            "en": "An explanation feels weak to me if it is unclear what to do with it.",
            "uk": "Пояснення здається мені слабким, якщо незрозуміло, що з ним робити."
          }
        },
        {
          "id": "soc_5",
          "scale": "Fi",
          "version": "1.0",
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
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне важно понимать, где отношения живые, а где только формальные.",
            "en": "It matters to me where relationships are real and where they are only formal.",
            "uk": "Мені важливо розуміти, де стосунки живі, а де лише формальні."
          }
        },
        {
          "id": "soc_7",
          "scale": "Fe",
          "version": "1.0",
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
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне хочется оживить разговор, если люди отвечают сухо или вяло.",
            "en": "I want to liven up a conversation when people respond dryly or weakly.",
            "uk": "Мені хочеться оживити розмову, якщо люди відповідають сухо або мляво."
          }
        },
        {
          "id": "soc_9",
          "scale": "Si",
          "version": "1.0",
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
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Обстановка вокруг сильно влияет на то, насколько мне спокойно и ясно.",
            "en": "The space around me strongly affects how calm and clear I feel.",
            "uk": "Обстановка навколо сильно впливає на те, наскільки мені спокійно і ясно."
          }
        },
        {
          "id": "soc_11",
          "scale": "Se",
          "version": "1.0",
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
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я замечаю, кто занимает место и где в ситуации есть запас силы.",
            "en": "I notice who takes space and where the situation has a reserve of force.",
            "uk": "Я помічаю, хто займає місце і де в ситуації є запас сили."
          }
        },
        {
          "id": "soc_13",
          "scale": "Ni",
          "version": "1.0",
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
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне важнее уловить вероятный ход событий, чем перечислить все варианты.",
            "en": "It matters more to me to catch the likely course of events than to list every option.",
            "uk": "Мені важливіше вловити ймовірний хід подій, ніж перелічити всі варіанти."
          }
        },
        {
          "id": "soc_15",
          "scale": "Ne",
          "version": "1.0",
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
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я легко замечаю варианты, которые другие сначала не видят.",
            "en": "I easily notice options that others do not see at first.",
            "uk": "Я легко помічаю варіанти, які інші спочатку не бачать."
          }
        },
        {
          "id": "soc_ac_1",
          "scale": "attention",
          "attention": 2,
          "version": "1.0",
          "text": {
            "ru": "Проверка внимательности: выберите вариант 2.",
            "en": "Attention check: choose option 2.",
            "uk": "Перевірка уважності: оберіть варіант 2."
          }
        }
      ]
    },
    "psychosophy": {
      "version": "psychosophy-pilot-v0.3",
      "mode": "position",
      "labels": {
        "ru": [
          "Энергия и действие",
          "Как вы расставляете приоритеты, решаете и организуете усилия"
        ],
        "en": [
          "Energy and action",
          "How you set priorities, decide, and organize effort"
        ],
        "uk": [
          "Енергія і дія",
          "Як ви розставляєте пріоритети, вирішуєте й організовуєте зусилля"
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
          "id": "psy_Воля_1",
          "scale": "Воля|1",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Когда надо выбрать, я обычно сам(а) решаю, как поступить.",
            "en": "When a choice is needed, I usually decide for myself what to do.",
            "uk": "Коли треба обрати, я зазвичай сам(а) вирішую, як вчинити."
          }
        },
        {
          "id": "psy_Воля_2",
          "scale": "Воля|2",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне легко помочь человеку выбрать, не давя на него.",
            "en": "It is easy for me to help a person choose without pressuring them.",
            "uk": "Мені легко допомогти людині обрати, не тиснучи на неї."
          }
        },
        {
          "id": "psy_Воля_3",
          "scale": "Воля|3",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне трудно, когда на меня давят или требуют быстрого решения.",
            "en": "It is hard for me when people pressure me or demand a quick decision.",
            "uk": "Мені важко, коли на мене тиснуть або вимагають швидкого рішення."
          }
        },
        {
          "id": "psy_Воля_4",
          "scale": "Воля|4",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне проще действовать, когда кто-то уже решил, что делать.",
            "en": "It is easier for me to act when someone has already decided what to do.",
            "uk": "Мені простіше діяти, коли хтось уже вирішив, що робити."
          }
        },
        {
          "id": "psy_Логика_1",
          "scale": "Логика|1",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Обычно я быстро нахожу своё объяснение и считаю, что понял(а).",
            "en": "I usually find my own explanation quickly and feel that I understand.",
            "uk": "Зазвичай я швидко знаходжу своє пояснення і вважаю, що зрозумів(ла)."
          }
        },
        {
          "id": "psy_Логика_2",
          "scale": "Логика|2",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне нравится вместе разбирать мысли и делать объяснение точнее.",
            "en": "I like working through ideas together and making an explanation more precise.",
            "uk": "Мені подобається разом розбирати думки й робити пояснення точнішим."
          }
        },
        {
          "id": "psy_Логика_3",
          "scale": "Логика|3",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я часто переживаю, не ошибся(лась) ли в рассуждении.",
            "en": "I often worry that I may have made a mistake in my reasoning.",
            "uk": "Я часто хвилююся, чи не помилився(лась) у міркуванні."
          }
        },
        {
          "id": "psy_Логика_4",
          "scale": "Логика|4",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Если тема не главная для меня, мне хватает готового объяснения.",
            "en": "If a topic is not central for me, a ready explanation is enough.",
            "uk": "Якщо тема не головна для мене, мені вистачає готового пояснення."
          }
        },
        {
          "id": "psy_Эмоция_1",
          "scale": "Эмоция|1",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я легко показываю своё настроение и чувства.",
            "en": "I easily show my mood and feelings.",
            "uk": "Я легко показую свій настрій і почуття."
          }
        },
        {
          "id": "psy_Эмоция_2",
          "scale": "Эмоция|2",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне легко поддерживать живой обмен чувствами с людьми.",
            "en": "It is easy for me to support a live exchange of feelings with people.",
            "uk": "Мені легко підтримувати живий обмін почуттями з людьми."
          }
        },
        {
          "id": "psy_Эмоция_3",
          "scale": "Эмоция|3",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я переживаю, если мои чувства звучат не так, как я хотел(а).",
            "en": "I worry when my feelings come across differently than I wanted.",
            "uk": "Я хвилююся, якщо мої почуття звучать не так, як я хотів(ла)."
          }
        },
        {
          "id": "psy_Эмоция_4",
          "scale": "Эмоция|4",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне легче включиться, когда настроение уже понятно.",
            "en": "It is easier for me to engage when the mood is already clear.",
            "uk": "Мені легше включитися, коли настрій уже зрозумілий."
          }
        },
        {
          "id": "psy_Физика_1",
          "scale": "Физика|1",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я хорошо знаю, какой быт, тело и комфорт мне нужны.",
            "en": "I know well what everyday setup, body care, and comfort I need.",
            "uk": "Я добре знаю, який побут, тіло й комфорт мені потрібні."
          }
        },
        {
          "id": "psy_Физика_2",
          "scale": "Физика|2",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне легко устроить практические вещи так, чтобы людям было удобно.",
            "en": "It is easy for me to arrange practical things so people are comfortable.",
            "uk": "Мені легко влаштувати практичні речі так, щоб людям було зручно."
          }
        },
        {
          "id": "psy_Физика_3",
          "scale": "Физика|3",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Телесный или бытовой дискомфорт может долго меня тревожить.",
            "en": "Body or everyday discomfort can trouble me for a long time.",
            "uk": "Тілесний або побутовий дискомфорт може довго мене тривожити."
          }
        },
        {
          "id": "psy_Физика_4",
          "scale": "Физика|4",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я могу долго не менять быт, если всё в целом работает.",
            "en": "I can leave my everyday setup unchanged for a long time if it mostly works.",
            "uk": "Я можу довго не змінювати побут, якщо все загалом працює."
          }
        },
        {
          "id": "psy_ac_1",
          "scale": "attention",
          "attention": 2,
          "version": "1.0",
          "text": {
            "ru": "Проверка внимательности: выберите вариант 2.",
            "en": "Attention check: choose option 2.",
            "uk": "Перевірка уважності: оберіть варіант 2."
          }
        }
      ]
    },
    "temporistics": {
      "version": "temporistics-pilot-v0.3",
      "mode": "position",
      "labels": {
        "ru": [
          "Время и направление",
          "Как вы переживаете прошлое, настоящее, будущее и большой смысл"
        ],
        "en": [
          "Time and direction",
          "How you experience past, present, future, and larger meaning"
        ],
        "uk": [
          "Час і напрям",
          "Як ви переживаєте минуле, теперішнє, майбутнє і великий сенс"
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
          "id": "tmp_Past_1",
          "scale": "Past|1",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я часто понимаю себя через то, что уже было в моей жизни.",
            "en": "I often understand myself through what has already happened in my life.",
            "uk": "Я часто розумію себе через те, що вже було в моєму житті."
          }
        },
        {
          "id": "tmp_Past_2",
          "scale": "Past|2",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне легко помогать людям собрать прошлые события в понятную историю.",
            "en": "It is easy for me to help people put past events into a clear story.",
            "uk": "Мені легко допомагати людям скласти минулі події в зрозумілу історію."
          }
        },
        {
          "id": "tmp_Past_3",
          "scale": "Past|3",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Ошибки прошлого могут надолго менять моё чувство “кто я”.",
            "en": "Past mistakes can change my feeling of “who I am” for a long time.",
            "uk": "Помилки минулого можуть надовго змінювати моє відчуття “хто я”."
          }
        },
        {
          "id": "tmp_Past_4",
          "scale": "Past|4",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне не нужно часто связывать новые события с моей прошлой историей.",
            "en": "I do not need to often connect new events with my past story.",
            "uk": "Мені не потрібно часто пов’язувати нові події з моєю минулою історією."
          }
        },
        {
          "id": "tmp_Present_1",
          "scale": "Present|1",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне важно ясно чувствовать: я здесь и я на своём месте.",
            "en": "It is important for me to clearly feel: I am here and in my place.",
            "uk": "Мені важливо ясно відчувати: я тут і я на своєму місці."
          }
        },
        {
          "id": "tmp_Present_2",
          "scale": "Present|2",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне легче понять своё место, когда я делаю что-то вместе с людьми.",
            "en": "It is easier for me to understand my place when I do something together with people.",
            "uk": "Мені легше зрозуміти своє місце, коли я роблю щось разом із людьми."
          }
        },
        {
          "id": "tmp_Present_3",
          "scale": "Present|3",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне тревожно, когда я не понимаю, где моё место сейчас.",
            "en": "I feel anxious when I do not understand where my place is right now.",
            "uk": "Мені тривожно, коли я не розумію, де моє місце зараз."
          }
        },
        {
          "id": "tmp_Present_4",
          "scale": "Present|4",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я могу спокойно жить моментом, даже если моё место пока неясно.",
            "en": "I can calmly live in the moment even if my place is not clear yet.",
            "uk": "Я можу спокійно жити моментом, навіть якщо моє місце поки неясне."
          }
        },
        {
          "id": "tmp_Future_1",
          "scale": "Future|1",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне важно заранее видеть, что может быть дальше.",
            "en": "It is important for me to see in advance what may come next.",
            "uk": "Мені важливо заздалегідь бачити, що може бути далі."
          }
        },
        {
          "id": "tmp_Future_2",
          "scale": "Future|2",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне легко помогать людям увидеть разные варианты впереди.",
            "en": "It is easy for me to help people see different options ahead.",
            "uk": "Мені легко допомагати людям побачити різні варіанти попереду."
          }
        },
        {
          "id": "tmp_Future_3",
          "scale": "Future|3",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Когда будущее непонятно, мне становится тревожно.",
            "en": "When the future is unclear, I become anxious.",
            "uk": "Коли майбутнє незрозуміле, мені стає тривожно."
          }
        },
        {
          "id": "tmp_Future_4",
          "scale": "Future|4",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Я могу жить спокойно, даже если не знаю точный план дальше.",
            "en": "I can live calmly even if I do not know the exact plan ahead.",
            "uk": "Я можу жити спокійно, навіть якщо не знаю точний план далі."
          }
        },
        {
          "id": "tmp_Eternity_1",
          "scale": "Eternity|1",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне важно видеть большой смысл того, что происходит.",
            "en": "It is important for me to see the larger meaning of what is happening.",
            "uk": "Мені важливо бачити великий сенс того, що відбувається."
          }
        },
        {
          "id": "tmp_Eternity_2",
          "scale": "Eternity|2",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне легко обсуждать с людьми, зачем всё это и какой в этом смысл.",
            "en": "It is easy for me to discuss with people why all this matters and what it means.",
            "uk": "Мені легко обговорювати з людьми, навіщо все це і який у цьому сенс."
          }
        },
        {
          "id": "tmp_Eternity_3",
          "scale": "Eternity|3",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Если я не вижу большого “зачем”, мне становится тяжело.",
            "en": "If I do not see the larger “why”, things feel heavy to me.",
            "uk": "Якщо я не бачу великого “навіщо”, мені стає важко."
          }
        },
        {
          "id": "tmp_Eternity_4",
          "scale": "Eternity|4",
          "version": "1.0",
          "reverse": false,
          "status": "pilot",
          "text": {
            "ru": "Мне не всегда нужен большой смысл, чтобы заниматься текущими делами.",
            "en": "I do not always need a larger meaning to deal with current tasks.",
            "uk": "Мені не завжди потрібен великий сенс, щоб займатися поточними справами."
          }
        },
        {
          "id": "tmp_ac_1",
          "scale": "attention",
          "attention": 2,
          "version": "1.0",
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
