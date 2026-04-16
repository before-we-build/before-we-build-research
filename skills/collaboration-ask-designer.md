# SKILL: collaboration-ask-designer

## Purpose

Turn vague interest in collaboration into a concrete, low-friction ask.

## When to Use

- You know who to contact, but not what to ask for
- A researcher is interested, but you need a realistic next step
- You want to reduce the perceived cost of helping

## Ask Types

| Ask Type | Best For |
|----------|----------|
| 20-minute sanity check | senior researchers with limited time |
| benchmark / dataset pointer | methods people |
| review of evaluation design | psychometrics / HCI / social simulation researchers |
| pilot-study consultation | applied collaborators |
| co-design of ablation plan | technical research partners |

## Output Format

```yaml
ask:
  type: "..."
  scope: "..."
  why_them: "..."
  time_cost: "..."
  expected_output: "..."
```

## Rules

- Ask for the smallest useful commitment
- Tie the ask to their actual expertise
- Make the output concrete
- Avoid open-ended `let's collaborate` language on first contact

## Examples

- `Could you sanity-check whether this evaluation design would convince you that the simulator measures something real?`
- `Would you point me to the benchmark you would trust most for persona fidelity under pressure?`

## Dependencies

- `researcher-targeter`

## Related Skills

- `outreach-personalizer`
- `evidence-packager`
