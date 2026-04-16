# SKILL: outreach-personalizer

## Purpose

Write targeted outreach that clearly explains why a specific researcher should care.

## When to Use

- Sending first contact
- Following up after reading a paper
- Converting a generic outreach draft into a researcher-specific message

## Input

```yaml
target:
  name: "..."
  role: "..."
  relevant_work: ["...", "..."]
project:
  thesis: "..."
  overlap: "..."
  ask: "..."
```

## Output

```yaml
subject: "..."
message: "..."
anchor_work: "..."
specific_ask: "..."
```

## Rules

- Mention exactly one or two relevant works, not five
- State the delta between their work and ours in one sentence
- Ask for one small thing only: feedback, benchmark pointer, intro, 20-minute call
- Sound like a testable research program, not a typology fandom pitch
- Keep first-contact outreach concise

## Bad Patterns

- mass-template praise
- vague `would love to connect`
- overselling pseudoscientific certainty
- asking for collaboration before proving you did the homework

## Dependencies

- `researcher-targeter`
- `research-bridge-builder`
- `collaboration-ask-designer`

## Related Skills

- `evidence-packager`
- `objection-handler`
