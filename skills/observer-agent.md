# SKILL: observer-agent

## Purpose

External LLM that analyzes conversation transcripts and provides independent compatibility assessments. Acts as an objective third-party observer.

**Based on:** Love First, Know Later's "LLM Observer" methodology

## When to Use

- Need independent validation of simulation results
- Want to compare agent self-assessment vs external view
- Building multi-perspective compatibility scoring

## The Two Perspectives (from Love First)

```
┌─────────────────────────────────────────────────────────────┐
│              LLM PARTICIPANT (Agent Self-Rating)             │
│                                                              │
│  Each agent rates the date from their own perspective:       │
│  "I felt attracted", "The conversation flowed well"         │
│                                                              │
│  Pros: Authentic internal experience                         │
│  Cons: Subjective, may over/under-rate                      │
└─────────────────────────────────────────────────────────────┘
                              VS
┌─────────────────────────────────────────────────────────────┐
│              LLM OBSERVER (External Analysis)                │
│                                                              │
│  External LLM analyzes the full transcript:                  │
│  "Mutual engagement was high", "Conversational flow strong" │
│                                                              │
│  Pros: Objective, sees both sides                           │
│  Cons: Missing internal states                              │
└─────────────────────────────────────────────────────────────┘
```

## How to Use

### Input
```yaml
transcript: |
  Agent A: Hi! I'm Alex. What brings you here tonight?
  Agent B: Hey Alex, I'm Jamie. Just looking to meet new people.
  Agent A: That's cool. I'm a software engineer. What do you do?
  Agent B: I'm in marketing. I love how tech is changing things.
  Agent A: Yeah, it's fascinating. What aspects interest you most?
  ...

agent_a_profile:
  type: "LII"
  name: "Alex"
agent_b_profile:
  type: "ESE"
  name: "Jamie"
```

### Observer Analysis Prompt
```
You are an objective relationship analyst observing a speed dating
conversation. Analyze the transcript and provide an external assessment.

---
TRANSCRIPT:
{transcript}

---
ANALYSIS DIMENSIONS:
1. Mutual Engagement — Did both parties actively participate?
2. Conversational Flow — Was the dialogue natural, with good back-and-forth?
3. Compatibility Signals — Are there signs of shared values, interests?
4. Comfort Level — Did the conversation seem easy or forced?
5. Interest Indicators — Did either party show clear attraction signals?

---
OUTPUT FORMAT:
{
  "mutual_engagement": 0.8,  # 0-1 scale
  "conversational_flow": 0.9,
  "compatibility_signals": 0.7,
  "comfort_level": 0.85,
  "interest_indicators": 0.75,
  "overall_compatibility": 0.8,
  "analysis": "Brief explanation...",
  "key_moments": ["..."]
}
```

### Output
```yaml
observer_assessment:
  mutual_engagement: 0.8
  conversational_flow: 0.9
  compatibility_signals: 0.7
  comfort_level: 0.85
  interest_indicators: 0.75
  overall_compatibility: 0.8
  analysis: |
    Both parties showed active engagement throughout the conversation.
    Agent A (LII) demonstrated intellectual curiosity while Agent B (ESE)
    showed warmth and adaptability. The conversation had natural progression
    from small talk to more substantive topics.
  key_moments:
    - "Agent A asked about interests → natural topic development"
    - "Agent B's warmth created comfortable atmosphere"

# Combined with participant ratings
combined_assessment:
  participant_a: 0.85  # From self-rating
  participant_b: 0.80   # From self-rating
  observer: 0.80        # From external analysis
  final_score: 0.82     # Weighted average
```

## Multi-Perspective Scoring

```python
def calculate_combined_score(participant_a, participant_b, observer):
    """
    Combine perspectives for robust compatibility assessment
    From Love First, Know Later
    """
    # Weight participant ratings higher (they have skin in the game)
    participant_avg = (participant_a + participant_b) / 2

    # Observer provides calibration
    # If observer disagrees with participants, weight down
    observer_disagreement = abs(participant_avg - observer)

    if observer_disagreement < 0.1:
        # Agreement — trust observer
        weights = {"participants": 0.5, "observer": 0.5}
    else:
        # Disagreement — trust participants more
        weights = {"participants": 0.7, "observer": 0.3}

    return (
        weights["participants"] * participant_avg +
        weights["observer"] * observer
    )
```

## LLM Parameters

```yaml
# For Observer Agent
model: "gpt-4o"  # Stronger model for analysis
temperature: 0.3  # Low for consistent analysis
purpose: "Objective compatibility assessment"

# For Participant Self-Rating
model: "gpt-4o"
temperature: 0.7  # Higher for authentic self-reflection
purpose: "Authentic internal experience"
```

## Comparison: Observer vs Participant

| Aspect | Observer | Participant |
|--------|----------|-------------|
| Perspective | External, objective | Internal, subjective |
| Data | Full transcript | Internal feeling |
| Strengths | Sees both sides, consistent | Captures actual experience |
| Weaknesses | Missing internal states | May misread signals |
| Best for | Calibration, validation | Primary signal |

## Integration with Compatibility Scorer

```python
def score_compatibility(pair_id, simulation_results):
    # Get all assessments
    assessments = load_assessments(pair_id)

    # Separate by type
    participant_ratings = [a for a in assessments if a.type == "participant"]
    observer_ratings = [a for a in assessments if a.type == "observer"]

    # Aggregate
    avg_participant = mean([r.score for r in participant_ratings])
    avg_observer = mean([r.score for r in observer_ratings])

    # Final score
    final = calculate_combined_score(avg_participant, avg_participant, avg_observer)

    return {"final_score": final, "breakdown": {...}}
```

## Dependencies

- `simulation-runner` — Generates conversation transcripts
- `compatibility-scorer` — Uses observer ratings in final score

## Related Skills

- `simulation-runner` — Provides transcripts for analysis
- `compatibility-scorer` — Incorporates observer perspective
- `persona-cloner` — Provides agent profiles for context
