# SKILL: reward-model

## Purpose

Model compatibility as a reward function that predicts optimal matching. Uses pairwise comparison and inverse reinforcement learning principles.

**Based on:** Love First, Know Later's reward modeling + Pairadigm's Bradley-Terry model

## Theory

### Traditional Matching (Flawed)
```
User A + User B → Compare profiles → "85% match"
```
Problem: Profile similarity ≠ interaction quality

### Reward Modeling (Our Approach)
```
User A + User B → Simulate interaction → Extract reward signal →
Learn what predicts human preferences → Predict optimal matching
```

## Framework

### From Love First, Know Later

```python
"""
Compatibility as Reward Modeling
Each interaction is a multi-agent MDP M = (S, A_i, A_j, T, R, γ)
"""
class CompatibilityRewardModel:
    def __init__(self):
        # LLM policies approximate true human policies
        self.policy_i = LLM_based_policy  # Agent i's behavior
        self.policy_j = LLM_based_policy  # Agent j's behavior

    def estimate_reward(self, trajectory):
        """
        Extract reward from simulated trajectory
        Following inverse reinforcement learning principles
        """
        # Parse trajectory for compatibility signals
        signals = extract_signals(trajectory)

        # Map signals to reward
        reward = self.signal_to_reward(signals)

        return reward

    def predict_match(self, agent_i, agent_j):
        """
        Predict whether agents should be matched
        """
        trajectory = self.simulate_interaction(agent_i, agent_j)
        reward = self.estimate_reward(trajectory)

        # Higher reward = better match
        return reward > threshold
```

### From Pairadigm: Bradley-Terry Model

```python
"""
Bradley-Terry Model for Pairwise Comparison
Compares items pairwise, outputs continuous scores
"""
from pairadigm import Pairadigm
import pandas as pd

# Initialize with items to compare
p = Pairadigm(
    data=pd.DataFrame({
        "persona_id": ["a", "b", "c", "d"],
        "compatibility_features": [features_a, features_b, features_c, features_d]
    }),
    item_id_name="persona_id",
    text_name="compatibility_features"
)

# Generate pairwise comparisons
p.generate_pairings()
p.generate_pairwise_annotations()

# Get continuous scores
scores = p.get_scores()
# Output: {"a": 0.85, "b": 0.72, "c": 0.91, "d": 0.68}
```

## Key Hypotheses (from Love First)

### Hypothesis 1: Sparse Rewards
```
Relationship outcomes determined by CRITICAL MOMENTS
Not by everyday conversations

Critical moments: conflict, major decisions, vulnerability
Everyday: small talk, routine
```

### Hypothesis 2: Deterministic Decisions
```
In critical moments, people show low entropy behavior
They're consistent — not random

This makes simulation tractable
```

### Theorem (Formalized)
```
As LLM policy approximation error → 0:
1. Prediction error → 0
2. Induced matching → Optimal stable matching
```

## Implementation

### Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Simulate Interaction                               │
│  Agent i + Agent j → Trajectory τ                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 2: Extract Compatibility Signals                       │
│                                                              │
│  From Love First:                                            │
│  - Mutual engagement                                        │
│  - Conversational flow                                      │
│  - Compatibility signals                                    │
│  - Comfort level                                           │
│  - Interest indicators                                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 3: Estimate Reward                                    │
│                                                              │
│  R(τ) = w · signals                                         │
│                                                              │
│  Learn weights w from human preference data                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 4: Predict Match                                      │
│                                                              │
│  If R(τ) > threshold: Match                                 │
│  Else: No match                                            │
└─────────────────────────────────────────────────────────────┘
```

### Signal Extraction

```python
def extract_signals(trajectory):
    """
    Extract compatibility signals from conversation
    """
    signals = {
        # From LLM Participant (self-rating)
        "self_attraction": extract_participant_rating(trajectory, "attraction"),
        "self_comfort": extract_participant_rating(trajectory, "comfort"),

        # From LLM Observer (external)
        "mutual_engagement": extract_observer_rating(trajectory, "engagement"),
        "conversational_flow": extract_observer_rating(trajectory, "flow"),

        # From trajectory analysis
        "shared_interests_mentioned": count_shared(trajectory),
        "vulnerability_moments": count_vulnerability(trajectory),
        "conflict_resolution": assess_conflict(trajectory),
    }

    return signals

def estimate_reward(signals):
    """
    Map signals to reward using learned weights
    """
    # Weights learned from human preference data
    weights = {
        "self_attraction": 0.25,
        "self_comfort": 0.20,
        "mutual_engagement": 0.20,
        "conversational_flow": 0.15,
        "shared_interests": 0.10,
        "vulnerability": 0.05,
        "conflict_resolution": 0.05,
    }

    reward = sum(weights[k] * signals[k] for k in weights)

    return reward
```

## Training the Reward Model

### From Human Data (Columbia Dataset)

```python
# Use real human choices to learn reward weights
human_choices = load_columbia_speed_dating_data()

# For each real interaction:
# 1. Simulate with LLM agents
# 2. Extract signals
# 3. Compare to human choice (matched/not)

# Learn weights that maximize prediction accuracy
from sklearn.linear_model import LogisticRegression

X = [extract_signals(simulated) for simulated in interactions]
y = [human.match for human in human_choices]

model = LogisticRegression()
model.fit(X, y)

# Now use model to predict new matches
```

## Validation

### Test on Known Datasets

| Dataset | What it tests |
|---------|---------------|
| Columbia Speed Dating | Initial chemistry |
| Divorce Prediction | Long-term stability |

### Metrics

```python
def evaluate_reward_model(model, test_data):
    predictions = model.predict([extract_signals(s) for s in test_data])

    metrics = {
        "accuracy": accuracy_score(test_data.y, predictions),
        "f1": f1_score(test_data.y, predictions),
        "auc": roc_auc_score(test_data.y, predictions),
    }

    return metrics
```

## LLM Parameters

```yaml
# For simulation (Love First)
persona_generation:
  model: "gemini-2.5-flash-lite"
  temperature: 0.8
  purpose: "Fast persona creation"

conversation_simulation:
  model: "mistral-nemo"
  temperature: 0.6
  purpose: "Natural dialogue generation"

# For analysis (Pairadigm)
comparison_model:
  model: "gpt-4o"
  temperature: 0.3
  purpose: "Consistent pairwise comparison"
```

## Dependencies

- `simulation-runner` — Generates trajectories
- `observer-agent` — Provides external analysis
- `choice-tracker` — Logs decisions

## Related Skills

- `simulation-runner` — Provides interaction data
- `observer-agent` — Extracts external signals
- `compatibility-scorer` — Uses reward estimates
- `choice-tracker` — Logs final decisions
