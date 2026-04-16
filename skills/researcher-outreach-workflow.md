# SKILL: researcher-outreach-workflow

## Purpose

Run a complete researcher outreach cycle from target selection to first contact, follow-up, and meeting prep.

## When to Use

- The project is ready to be shown outside the repo
- You want to contact researchers, labs, or adjacent technical partners
- You need a repeatable process instead of ad hoc cold emails

## Goal

Produce a small batch of high-quality outreach with:
- a clear research framing
- a compact evidence packet
- one concrete ask per target
- prepared answers to obvious objections

## Workflow Overview

```text
1. Readiness gate
2. Target selection
3. Research translation
4. Evidence packet assembly
5. Ask design
6. Message personalization
7. Objection prep
8. Send + track
9. Follow-up + meeting prep
```

## Step 1: Readiness Gate

**Objective:** Do not start outreach before the project can survive first contact.

### Check
- Can the project be explained in 3 sentences without typology jargon?
- Is the current epistemic status explicit?
- Is there at least one credible validation path?
- Is there one concrete artifact to show?

### Required Inputs
- `research-bridge-builder`
- `evidence-packager`

### Exit Criteria
- 1-sentence thesis is stable
- strongest claim is bounded
- there is one artifact to send

### If This Fails
- do not outreach yet
- tighten claims first

---

## Step 2: Target Selection

**Objective:** Build a shortlist that is small, specific, and role-aware.

### Use
- `researcher-targeter`

### Output
- 5 high-fit targets for immediate outreach
- 5 backup targets

### Required Fields Per Target
- name
- role
- why them
- overlap hypothesis
- collaboration role
- risk

### Rules
- split targets into `academic`, `applied`, `adjacent`
- prefer method overlap over status
- define the reason for contacting each person

### Exit Criteria
- every target has a clear role: reviewer, advisor, pilot partner, benchmark source, or collaborator

---

## Step 3: Research Translation

**Objective:** Translate the project into language a researcher can evaluate.

### Use
- `research-bridge-builder`

### Produce
```yaml
problem_statement: "..."
research_translation: "..."
method_anchor: "..."
novelty_claim: "..."
validation_path: "..."
epistemic_status: "hypothesis | prototype | validated component"
```

### Rules
- lead with method, not with ontology
- treat niche typologies as schema languages or hypothesis generators
- separate source-backed claims from project synthesis

### Exit Criteria
- can explain the project without saying `trust the typology`

---

## Step 4: Evidence Packet Assembly

**Objective:** Give the researcher something reviewable in under 3 minutes.

### Use
- `evidence-packager`

### Packet Must Include
1. thesis
2. novelty
3. what already exists
4. what is still hypothesis-only
5. validation roadmap
6. specific ask

### Good Packet Size
- short email-safe summary
- optional one-pager
- one concrete repo/page/demo link

### Exit Criteria
- a busy researcher can understand the project and the ask without a call

---

## Step 5: Ask Design

**Objective:** Turn vague interest into a concrete low-friction next step.

### Use
- `collaboration-ask-designer`

### Preferred Ask Types
- 20-minute sanity check
- benchmark pointer
- evaluation-design review
- pilot-study consultation
- ablation-plan feedback

### Rules
- first ask must be small
- tie the ask to their actual expertise
- make the expected output concrete

### Exit Criteria
- ask can be answered with one yes/no decision

---

## Step 6: Message Personalization

**Objective:** Write one message per target that clearly says why them.

### Use
- `outreach-personalizer`

### Message Structure
1. short hook
2. one relevant paper / artifact of theirs
3. one-sentence delta between their work and ours
4. specific ask
5. optional link to evidence packet

### Rules
- mention one or two works only
- keep first contact concise
- do not ask for broad collaboration immediately

### Exit Criteria
- if you remove the target's name, the message should stop making sense

---

## Step 7: Objection Prep

**Objective:** Be ready for the strongest pushback before sending.

### Use
- `objection-handler`

### Prepare Responses For
- pseudoscience concern
- why not Big Five only
- why simulation should predict real outcomes
- where validation comes from
- what survives if typology mapping fails

### Rules
- agree with fair criticism
- narrow claims
- show validation path
- never defend weak claims out of habit

### Exit Criteria
- each objection has: fair core, bounded answer, next validation step

---

## Step 8: Send + Track

**Objective:** Run outreach like a small experiment, not like random messaging.

### Track Per Target
```yaml
target: "..."
date_sent: "..."
status: "sent | replied | follow_up_due | call_scheduled | closed"
ask: "..."
response_signal: "..."
next_action: "..."
```

### Cadence
- send in small batches of 3-5
- observe which framing gets replies
- revise before the next batch

### Rules
- do not send 20 generic emails at once
- treat outreach copy as an iterated artifact

---

## Step 9: Follow-Up + Meeting Prep

**Objective:** Convert replies into useful conversations.

### If No Reply
- send one follow-up after a reasonable delay
- shorten the ask further if needed

### If Positive Reply
Prepare:
- 3-minute project summary
- one evidence packet
- one specific question for them
- one note on what kind of feedback is most useful

### If Skeptical Reply
- answer the objection directly
- narrow the claim
- offer a smaller ask

---

## Recommended Deliverables

By the end of one outreach cycle, you should have:
1. a ranked list of 10 targets
2. one stable research framing
3. one evidence packet
4. 5 personalized first-contact drafts
5. objection notes
6. a tracking sheet

## Suggested Weekly Cadence

### Day 1
- readiness gate
- target selection

### Day 2
- research translation
- evidence packet

### Day 3
- ask design
- first 3 personalized messages

### Day 4
- objection prep
- send first batch

### Day 5+
- track replies
- revise framing
- send next batch

## Dependencies

- `researcher-targeter`
- `research-bridge-builder`
- `evidence-packager`
- `outreach-personalizer`
- `collaboration-ask-designer`
- `objection-handler`

## Related Skills

- `type-mapper`
- `persona-validator`
- `explanation-generator`
