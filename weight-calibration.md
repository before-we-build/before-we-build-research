# Weight Calibration Research Plan

## Objective

Empirically determine the optimal weights for each typological level (strategic / operational / tactical) and the correct aggregation operation (additive vs multiplicative) in the compatibility scoring formula.

## Current Hypotheses

| Parameter | Hypothesis A (plan.md) | Hypothesis B (autoreasearch.md) |
|-----------|------------------------|--------------------------------|
| Operation | Multiplicative (`*`) | Additive (`+`) |
| Strategic weight | 0.40 | 0.40 |
| Operational weight | 0.30 | 0.30 |
| Tactical weight | 0.20 | 0.30 |
| Extra term | `reciprocal_interest_prior` (0.10) | `confidence` (post-multiplication) |
| Risk penalty | `- risk_penalty` | `0.60 * risk` |

## Research Questions

1. **Which aggregation model fits real outcomes better?**
   - Additive: `base = w₁·s + w₂·o + w₃·t`
   - Multiplicative: `base = w₁·s · w₂·o · w₃·t` (or normalized variant)
   - Hybrid: `base = w₁·s + w₂·o + w₃·t · synergy_factor`

2. **What are the validated weights?**
   - Do strategic conflicts truly have 2x the impact of tactical conflicts?
   - Is there a non-linear relationship (e.g., threshold effects)?

3. **What is the theoretical justification?**
   - Strategic level: values, life direction, time horizon
   - Operational level: goal alignment, role complementarity
   - Tactical level: communication style, conflict resolution patterns

## Methodological Approach

### Phase 1: Literature Review

**Objective:** Gather empirical evidence on hierarchy of compatibility factors.

| Source | Type | Relevant Finding |
|--------|------|------------------|
| Gottman Institute | Longitudinal relationship research | "The Four Horsemen" patterns are tactical-level predictors; value misalignment is strategic-level predictor |
| Finkel et al. (2012) | interdependence theory | Both situational and stable factors matter; interaction effects present |
| Buss & Shackelford (1997) | mate retention | Strategic traits (personality, values) predict long-term satisfaction; tactical (conflict management) predicts stability |
| Markman et al. (1993) | premarital prediction | Communication patterns (tactical) predict divorce better than values (strategic) at 6-year follow-up |
| Watson et al. (2014) | Big Five & marital outcomes | Personality (strategic proxies) predict satisfaction; conflict behavior (tactical) predicts dissolution |

**Search queries:**
- "hierarchy of compatibility factors relationship outcomes"
- "strategic vs tactical compatibility prediction marriage"
- "weight of values vs communication in relationship satisfaction"

### Phase 2: Expert Elicitation

**Objective:** Obtain priors from domain experts on weight ratios.

**Experts to consult:**
- Therapists / relationship counselors
- Socionics practitioners with documented case outcomes
- Dating platform data scientists (if accessible)

**Method:** Modified Delphi process
1. Present expert with 20 paired scenarios with known outcomes
2. Expert ranks by importance
3. Aggregate and iterate

### Phase 3: Simulation Calibration

**Objective:** Use simulation to validate weights against synthetic ground truth.

**Process:**
1. Generate synthetic population with known typological profiles
2. Inject compatibility "ground truth" with known weight parameters
3. Run AutoResearch pipeline with candidate formulas
4. Measure: precision@K, recall@K, RMSE against ground truth

**Candidate formulas to test:**

```
Formula F1 (additive uniform):
  base = (strategic + operational + tactical) / 3

Formula F2 (additive weighted - autoreasearch):
  base = 0.40*strategic + 0.30*operational + 0.30*tactical

Formula F3 (multiplicative - plan.md):
  base = 0.40*strategic * 0.30*operational * 0.20*tactical * 0.10*reciprocal

Formula F4 (multiplicative normalized):
  base = (w₁·s) · (w₂·o) · (w₃·t) / (w₁·w₂·w₃)  [normalized to 0-1]

Formula F5 (geometric mean variant):
  base = (strategic^0.4 * operational^0.3 * tactical^0.3)

Formula F6 (minimum threshold):
  base = min(strategic, operational, tactical)  [compatibility limited by weakest link]
```

### Phase 4: A/B Testing with Real Users

**Objective:** Validate formula in production with actual matching outcomes.

**Metrics to track:**
- Short-term: response rate, conversation initiation
- Medium-term: second date rate, 3+ date retention
- Long-term: relationship formation, satisfaction scores (6-month, 12-month)

**Experimental design:**
- Control: current formula (baseline)
- Treatment: candidate formulas
- Minimum sample: n=500 per arm for statistical power
- Primary metric: 6-month relationship formation rate

### Phase 5: Sensitivity Analysis

**Objective:** Determine robustness of weights to perturbations.

**Methods:**
- Monte Carlo simulation with ±20% weight perturbations
- Identify which weight errors have largest impact on ranking
- Establish confidence intervals for each weight

## Validation Checklist

- [ ] Literature review complete with minimum 10 peer-reviewed sources
- [ ] Expert elicitation with minimum 5 domain experts
- [ ] Simulation calibrated against synthetic ground truth (R² > 0.7)
- [ ] A/B test with statistical significance (p < 0.05)
- [ ] Sensitivity analysis complete
- [ ] Final formula documented with confidence intervals

## Theoretical Framework for Weight Justification

### Why strategic might be most important (w=0.40)

- Values misalignment creates unsolvable conflicts (divorce research)
- Life direction incompatibility (children, career, location) is hard-stop
- Temporal horizons affect long-term planning capacity

**Evidence:** Buss & Shackelford (1997) - mate retention strategies focus on strategic traits

### Why operational matters (w=0.30)

- Goal alignment affects day-to-day coordination
- Role complementarity reduces friction in task distribution
- Mid-level alignment predicts relationship satisfaction

**Evidence:** Finkel et al. (2012) - interdependence theory emphasizes mutual goal pursuit

### Why tactical is important but not dominant (w=0.30)

- Communication patterns are trainable (DBT, couples therapy)
- Tactical incompatibility can be compensated by strategic/operational fit
- Direct predictor of conflict escalation patterns

**Evidence:** Markman et al. (1993) - communication predicts dissolution but values predict satisfaction

### Why multiplication vs Addition matters

**Multiplicative interpretation:**
- Compatibility is a product of all levels
- Weak link (low score on any level) dramatically reduces overall compatibility
- "Strategic incompatibility can't be compensated by tactical compatibility"

**Additive interpretation:**
- Partial compensation possible
- Strong tactical fit can offset moderate strategic misalignment
- More optimistic for "opposites attract" cases

**Evidence needed:** Does data support compensation or hard-floor effect?

## Open Questions

1. Is there a threshold effect (e.g., if any level < 0.3, overall = 0)?
2. Do weights vary by user segment (age, relationship goals)?
3. Should weights be personalized per user based on revealed preferences?
4. How do risk flags interact with weights (multiplicative penalty vs additive)?

## References

- Buss, D. M., & Shackelford, T. K. (1997). From vigilance to violence: Mate retention tactics in married couples. *Journal of Personality and Social Psychology*.
- Finkel, E. J., et al. (2012). The Mate Retention Inventory–Short Form (MRI–SF). *Personality and Individual Differences*.
- Gottman, J. M., & Silver, N. (1999). *The Seven Principles for Making Marriage Work*. Crown Publishers.
- Markman, H. J., et al. (1993). Communication and change processes that predict success in couples making the transition to parenthood. *Family Process*.
- Watson, D., et al. (2014). Predicting prospective marital satisfaction from couples' histories of problem behaviors. *Journal of Personality and Social Psychology*.
