# SKILL: dating-ai-failures

## Purpose

Avoid mistakes made by previous LLM dating/compatibility projects by learning from their failures.

## What Went Wrong — Case Studies

### 1. Dolores (AI Girlfriend)

| Issue | What Happened |
|-------|-------------|
| Users wanted adult content | 70% traffic drop after safety filter |
| Individual dev can't sustain API costs | Token-based usage = 1% users = 99% costs |
| No hardware = inequality | User opens app, AI just waits |
| Couldn't evolve past "toy" | Platform hostile to meaningful relationship |

**Lesson**: Can't monetize intimacy, distribution is existential, hardware gap is real.

### 2. Manifold.Love (Prediction Market Dating)

| Issue | What Happened |
|-------|-------------|
| Network effect didn't take off | Users knew each other = initial buzz, then stagnation |
| Geographic distribution | Small, distributed users won't travel |
| Market-making not compelling | No incentive to bet "NO" on unlikely matches |

**Lesson**: Even perfect algorithm is useless without critical mass of local users.

### 3. Speed Dating AI (Dan Kras)

| Issue | What Happened |
|-------|-------------|
| Distribution was the failure | "Model's accuracy, the app's design were far from perfect. But an omniscient compatibility model is useless if a customer's soulmate isn't an active user on the platform." |
| Tech was never the bottleneck | Solving distribution > solving matching algorithm |

**Lesson**: Distribution >> Algorithm. Build for existing communities first.

### 4. $3M AI Companion Startup (2024-2026)

| Issue | What Happened |
|-------|-------------|
| Day-7 retention: 22% | "performative" conversations |
| Memory failures | Contradicted itself, lost trust |
| Personality shifts | Different reply style = felt unstable |
| Monetization backlash | "more romantic" tier = paywalled intimacy |

**Lesson**: Small consistent memory wins > occasional brilliant replies.

### 5. "Love First, Know Later" (arXiv 2025)

| What They Did Right |
|----------------|
| Simulating interactions (not static profiles) |
| Critical moments hypothesis from relationship psychology |
| Proof of convergence |

**What to Learn From**: They proved the paradigm shift mathematically. This is your academic hook.

## Core Error Patterns

### Error 1: Tech Fixation

```
❌ "If we build a better algorithm, users will come"
✓ "Build where users already are. Solve distribution first."
```

### Error 2: Monetizing Intimacy

```
❌ Premium tier = "more romantic" mode
✓ No paywall for emotional connection
✓ Be transparent about what AI is/isn't
```

### Error 3: Static Profiles

```
❌ Match by personality vector similarity only
✓ Simulate interaction first, then assess
✓ Use critical moments framework
```

### Error 4: Personality Instability

```
❌ Let model update rewrite persona
✓ Lock persona anchors, test for drift
✓ Use "memory checkpoints"
✓ Implement persistent memory infrastructure
```

### Error 5: The Distribution Lie

```
❌ "Build it and they will come"
✓ "Perfect compatibility is useless without the right users"
✓ Target existing communities (not cold market)
✓ Geographic density matters
```

## What This Project Does Differently

| Pattern to Avoid | Our Approach |
|----------------|------------|
| Tech-fixation | Build for specific researcher audience first |
| Static matching | Scenario-first simulation |
| Individual dev | Partner with validation researchers |
| Monetize intimacy | Research tool, not product |
| Generic cold outreach | Target method-aligned academics first |

## Key Quote: Dan Kras

> "It is comparatively easy to identify why existing dating services aren't great and how they could be improved. It is much more difficult to figure out how to efficiently acquire a dense, local network of users. Until one has a clear solution to that existential challenge, any investment into a new dating service seems misguided."

## This Project's Strategy

Given we can't solve distribution as a research prototype:

1. Focus on **validation** (not product)
2. Target **researchers** (not consumers)
3. Build **evidence** (not growth)
4. Let others solve the product → distribution problem

## References

- Dolores: https://mazzzystar.github.io/2023/11/16/ai-girlfriend-product/
- Manifold.Love: https://news.manifold.markets/p/manifold-love
- Dan Kras: https://dkras.substack.com/p/dating-experiments
- Love First, Know Later: https://arxiv.org/pdf/2512.11844
- $3M Case Study: fotosdefrases.com
- Heartthrob: https://heartthrob.ai/blog/hidden-labor-of-ai-relationships