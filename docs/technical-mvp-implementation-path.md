# Technical MVP Implementation Path

**Project:** Before We Build  
**Scope:** Start Alone / weak-AI Christian conversation-map MVP  
**Status:** Implementation path inspection  
**Created:** 2026-05-13  
**Task:** `t_0d5b613e`  
**Inputs:** `docs/mvp-data-entities.md`, `docs/start-alone-audience-path-spec.md`, `docs/start-alone-question-library-v0.md`, `docs/answer-normalization-rules.md`, `docs/personal-preparation-map-template.md`, local repo inspection.

## 1. Decision

The smallest useful MVP should be implemented first in:

```text
/home/ubuntu/before-we-build.github.io
https://github.com/before-we-build/before-we-build.github.io
```

This repo is the current public GitHub Pages app. It is a static HTML/CSS/JS site with no build step, no package manager, and no server dependency.

The already-existing bot repo should not be the target for this Start Alone MVP:

```text
/home/ubuntu/church-intro-bot
https://github.com/before-we-build/church-intro-bot
```

`church-intro-bot` is a separate Telegram SQLite MVP for anonymous church-mediated introductions. It already implements anonymous profiles, intro requests, four-sided consent, contact reveal gates, and audit logging. That path is later / separate from Start Alone because the Start Alone spec explicitly excludes browsing people, matching, anonymous introductions, and church-mediated workflows.

## 2. Current target stack

### `before-we-build.github.io`

Observed files:

- `index.html` — public entry page.
- `tests.html` — current public interactive route shell.
- `research-tests.html` — current research-style test route.
- `assets/tests.js` — all current questionnaire data, answer capture, scoring, localStorage persistence, and result rendering for the typology-oriented tests.
- `assets/app.js` — homepage dynamic copy and journey routing.
- `assets/pages-i18n.js` — page-level localized dictionaries.
- `assets/site.css` — all styling.
- `specs/000-foundation/*.md` — Scripture-first foundation specs already present in the site repo.

Stack:

```text
Static GitHub Pages
HTML + CSS + vanilla JavaScript
Browser localStorage for local-only persistence
No npm / package.json
No backend in this repo
```

### `church-intro-bot`

Observed files:

- `pyproject.toml` — Python 3.11 package, `python-telegram-bot`, pytest, ruff.
- `src/church_intro_bot/core.py` — SQLite domain/storage layer.
- `src/church_intro_bot/telegram_app.py` — Telegram `/start`, `/privacy`, `/register` conversation.
- `tests/test_core.py` — privacy, anonymous profile, matching-signal, consent, and audit tests.

Verification run:

```text
python -m pytest -q && ruff check .
# 4 passed; ruff all checks passed
```

This repo is useful later for church-mediated introduction work, but should not absorb the Start Alone web MVP.

## 3. Implementation approach

Build the Start Alone MVP as a new static, local-only web route in `before-we-build.github.io`, reusing the current local browser persistence pattern but replacing typology scoring with the MVP entity model.

Recommended route:

```text
start-alone.html
```

Recommended implementation files:

```text
start-alone.html
assets/start-alone.js
assets/site.css
```

Optional later split if `assets/start-alone.js` grows too large:

```text
assets/start-alone-data.js        # question set and localized text
assets/start-alone-normalize.js   # rule-based normalization / flags
assets/start-alone-report.js      # report composer / export
assets/start-alone.js             # UI controller
```

For the first MVP, a single `assets/start-alone.js` is acceptable if it is structured into clear sections and tests are added.

## 4. Where each required part should live

### 4.1 Question flow

Put the Start Alone route shell in:

```text
/home/ubuntu/before-we-build.github.io/start-alone.html
```

The page should:

- use the existing `assets/site.css` design language;
- default to Ukrainian, with Russian available if implemented in the same pass;
- clearly say `Почати самому` / `Почати з простих запитань`;
- show the foundation and boundary note before answers;
- present the optional first set of 8 questions from `docs/start-alone-question-library-v0.md` before the full 39-question set;
- avoid typology, score, compatibility, and psychological language.

Put question data in:

```text
/home/ubuntu/before-we-build.github.io/assets/start-alone.js
```

Initial data shape:

```js
const START_ALONE_QUESTION_SET = {
  id: 'qset_start_alone_v0',
  pathId: 'path_start_alone',
  version: '2026-05-13',
  localeDefault: 'uk',
  questions: [
    {
      id: 'q_start_alone_001',
      group: 'faith_and_foundation',
      required: true,
      prompt: { uk: '...', ru: '...' },
      answerKindOptions: [
        'clear_to_me',
        'unclear_or_needs_counsel',
        'hard_to_answer',
        'not_relevant_now'
      ]
    }
  ]
};
```

Each visible prompt should come from the approved question library / safety review, not from the older typology test questions in `assets/tests.js`.

### 4.2 Answer capture and persistence

Keep persistence browser-local for v0. Do not send answers to a server.

Use localStorage keys separate from the existing typology test:

```text
before-we-build-start-alone-session
before-we-build-start-alone-export
```

The captured MVP objects should follow `docs/mvp-data-entities.md`:

- `UserSession`
- `AudiencePath`
- `QuestionSet`
- `QuestionResponse`

Suggested raw response shape:

```js
{
  id: 'response_<uuid>',
  sessionId: 'session_<uuid>',
  questionId: 'q_start_alone_001',
  questionSetId: 'qset_start_alone_v0',
  rawText: 'user typed text',
  answerKind: 'unclear_or_needs_counsel',
  createdAt: 'ISO timestamp',
  updatedAt: 'ISO timestamp',
  locale: 'uk'
}
```

Required behavior:

- autosave draft answers locally;
- allow resume from the same browser;
- allow user to clear local data;
- mark derived report objects stale after answer edits;
- do not create account, identity profile, browsing profile, or church-visible data in this route.

### 4.3 Normalized summaries

For the smallest static MVP, implement deterministic/rule-based normalization first. Do not depend on an LLM API until a backend/privacy plan exists.

Put normalization functions in `assets/start-alone.js` initially:

```js
function normalizeResponses(session, questionSet, responses) { ... }
function detectReviewFlags(normalizedAnswers, responses) { ... }
function buildConversationThemes(normalizedAnswers, reviewFlags) { ... }
function buildOpenQuestions(themes, normalizedAnswers) { ... }
function chooseWiseNextStep(themes, flags, responses) { ... }
```

Generated objects should follow the entity spec:

- `NormalizedAnswer`
- `ConversationTheme`
- `OpenQuestion`
- `ReviewFlag`
- `WiseNextStep`

Rules to preserve from `docs/answer-normalization-rules.md`:

- direct user facts remain `user_stated_fact`;
- self-description remains attributed to the user;
- generated summaries use visible uncertainty labels;
- sensitive content creates `ReviewFlag` and may suppress ordinary report sections;
- no hidden motive-reading, diagnosis, readiness verdict, compatibility category, or spiritual decision.

Because there is no backend yet, v0 normalization can be modest:

- create one `NormalizedAnswer` per answered question;
- assign claim kind from the question group and user-selected answer kind;
- create `unclear_or_missing` objects for skipped or vague important questions;
- create `possible_concern` / `needs_human_review` flags from a conservative keyword list for coercion, abuse, self-harm, severe distress, forced disclosure, unsafe family context, or spiritual manipulation;
- group answers by the ten question themes.

### 4.4 Report generation

Put report composition in `assets/start-alone.js` initially:

```js
function composePersonalPreparationMap(session, questionSet, responses, normalizedAnswers, themes, openQuestions, reviewFlags, wiseNextStep) { ... }
```

The report object should be a `ConversationMap` instance named internally:

```text
PersonalPreparationMap
```

Public Ukrainian title:

```text
Карта підготовки до мудрої розмови
```

Public Russian title:

```text
Карта подготовки к мудрому разговору
```

Required report sections:

1. title and short introduction;
2. caveat before interpretation;
3. what the user already named clearly;
4. hopes, fears, and expectations to examine;
5. what is still unclear;
6. topics for prayer, Scripture, church, and wise counsel;
7. questions for a future honest conversation;
8. one wise next step;
9. optional feedback and export controls.

The caveat must preserve the meaning from `wiki/concepts/report-caveat-standard.md` and `docs/personal-preparation-map-template.md`.

### 4.5 Controlled export

Implement export only as user-initiated actions.

Initial controls:

```text
Скопіювати короткий підсумок
Завантажити карту JSON
Завантажити карту .txt
Видалити локальні дані
```

Export must include caveats and must not automatically send anything to a pastor, church, family member, mentor, or future partner.

Recommended exported JSON top-level shape:

```js
{
  schemaVersion: 'start-alone-mvp-v0',
  exportedAt: 'ISO timestamp',
  shareState: 'exported_by_user',
  session: { ... },
  questionSet: { id, version, pathId },
  responses: [ ... ],
  normalizedAnswers: [ ... ],
  conversationThemes: [ ... ],
  openQuestions: [ ... ],
  reviewFlags: [ ... ],
  wiseNextStep: { ... },
  conversationMap: { ... }
}
```

### 4.6 UI copy

Use `assets/start-alone.js` for route-local text first, or add a dictionary to `assets/pages-i18n.js` if the copy must be shared across pages.

Homepage entry links should be updated in:

```text
/home/ubuntu/before-we-build.github.io/index.html
/home/ubuntu/before-we-build.github.io/assets/app.js
/home/ubuntu/before-we-build.github.io/assets/pages-i18n.js
```

Recommended first link destination:

```text
start-alone.html
```

Public wording must stay Scripture-first and fully localized. Prefer Ukrainian/Russian words from `wiki/concepts/public-language-boundaries.md` and the Start Alone spec:

- `Почати самому`
- `Почати з простих запитань`
- `Карта підготовки до мудрої розмови`
- `що вже зрозуміло`
- `що ще не ясно`
- `молитва, Писання, церква, мудра порада`
- `наступний мудрий крок`

Avoid public wording such as:

- compatibility score / відсоток сумісності / процент совместимости;
- profile, type, typology, model, diagnosis, readiness score;
- matching, candidate browsing, ideal match;
- any claim that the tool knows God’s will or decides whether a relationship should proceed.

## 5. Files to avoid changing for this MVP

Do not extend these for the Start Alone route unless there is a deliberate migration task:

```text
/home/ubuntu/before-we-build.github.io/assets/tests.js
/home/ubuntu/before-we-build.github.io/tests.html
/home/ubuntu/before-we-build.github.io/research-tests.html
```

Reason: they currently implement a typology-oriented test and scoring/result flow. Start Alone should not inherit the public mental model of a test, profile, or top-3 hypothesis.

The old route can remain available as a research or legacy route until a later cleanup task decides whether to hide, rename, or remove it.

## 6. Exact implementation commands

From the target app repo:

```bash
cd /home/ubuntu/before-we-build.github.io
```

Create the route and JS file:

```bash
$EDITOR start-alone.html
$EDITOR assets/start-alone.js
```

Manual local preview:

```bash
python3 -m http.server 8080
# open http://localhost:8080/start-alone.html
```

Useful static checks without adding tooling:

```bash
python3 - <<'PY'
from pathlib import Path
for path in ['start-alone.html', 'assets/start-alone.js', 'assets/site.css']:
    p = Path(path)
    print(path, 'exists=', p.exists(), 'bytes=', p.stat().st_size if p.exists() else 0)
PY

python3 - <<'PY'
from html.parser import HTMLParser
class Parser(HTMLParser):
    pass
for path in ['start-alone.html', 'index.html']:
    Parser().feed(open(path, encoding='utf-8').read())
    print('parsed', path)
PY

node --check assets/start-alone.js
```

If Node is not installed, use browser manual verification and keep JS syntax simple; otherwise `node --check` should be part of every implementation pass.

For existing bot sanity, if any church-introduction code is touched later:

```bash
cd /home/ubuntu/church-intro-bot
python -m pytest -q
ruff check .
```

## 7. Tests to add

Because the target app has no test runner yet, add the smallest dependency-free browser/Node-compatible test file:

```text
/home/ubuntu/before-we-build.github.io/assets/start-alone.test.js
```

Write pure functions in `assets/start-alone.js` so they can be exported for tests in a browser-like or Node context.

Minimum tests:

1. **Question set integrity**
   - every question has stable ID, group, prompt, and localized Ukrainian text;
   - optional first set contains exactly the intended eight questions;
   - no question prompt contains forbidden words such as score, compatibility percentage, type/profile as public labels.

2. **Raw response persistence**
   - saving responses stores `QuestionResponse` objects separately from normalized summaries;
   - editing a response marks report/normalized objects stale or regenerates them;
   - clearing data removes only Start Alone localStorage keys.

3. **Normalization boundaries**
   - direct user text is preserved as user-attributed;
   - generated summaries carry allowed uncertainty labels;
   - missing/vague answers become `unclear_or_missing` rather than accusations;
   - no output says ready/not ready for marriage, ideal match, or God’s will.

4. **Review flag routing**
   - coercion / abuse / self-harm / forced disclosure keywords create `ReviewFlag` with `needs_human_review`;
   - ordinary report sections are suppressed or softened when a high-risk flag exists;
   - safe public text points to human help without automated spiritual advice.

5. **Report composer**
   - caveat appears before interpretive sections;
   - report includes clear areas, unclear areas, future conversation questions, prayer/counsel topics, and one wise next step;
   - report contains no compatibility score, spouse promise, diagnosis, or automatic sharing language.

6. **Export controls**
   - export is generated only after explicit user action;
   - exported JSON contains `shareState: 'exported_by_user'`;
   - exported text includes the caveat;
   - no function sends network requests.

7. **Smoke/manual test checklist**
   - load `start-alone.html` locally;
   - answer the eight-question first set;
   - reload and confirm draft resumes;
   - generate map;
   - edit one answer and confirm stale/regenerate behavior;
   - copy summary;
   - download JSON/text;
   - clear data and reload.

Suggested test command if `assets/start-alone.test.js` is plain Node:

```bash
node assets/start-alone.test.js
```

## 8. Suggested next implementation card

Title:

```text
BWB: implement Start Alone answer capture v0 in GitHub Pages app
```

Scope:

- target `/home/ubuntu/before-we-build.github.io`;
- add `start-alone.html` and `assets/start-alone.js`;
- implement the optional 8-question first set from `docs/start-alone-question-library-v0.md`;
- local-only save/resume/clear;
- raw `QuestionResponse` objects and `UserSession` object;
- no report generation yet except maybe a simple answer review screen.

Acceptance:

- user can start `Почати самому` route;
- answers save locally and can be edited;
- raw answers are separate from any derived object;
- no typology/scoring/matching language;
- manual preview works with `python3 -m http.server 8080`;
- at least one small test or static verification script checks question data and localStorage key boundaries.

## 9. Open implementation risks

- The current public site still contains older test/profile/scoring language in `tests.html` / `assets/tests.js`; Start Alone should not reuse that wording.
- Static-only GitHub Pages means no private server-side LLM normalization. The first MVP should be rule-based/local-only or wait for a separate backend/privacy decision.
- If AI-assisted summaries are required soon, a new private backend or edge function will be needed; do not send raw answers to a third-party API from static frontend without an explicit privacy/consent design.
- Ukrainian/Russian public copy should receive native-speaker and Scripture-first review before publication.
