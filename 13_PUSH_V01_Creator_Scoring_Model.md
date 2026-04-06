> **Document ID:** 13 | **Version:** 1.0 | **Last Updated:** 2026-04-05 | **Status:** Active
> **Authoritative For:** Specific scoring weights, tier thresholds, score calculations
> **See Also:** [Doc 01] for strategic pillar (Creator Credit) | [Doc 07] for attribution feeding into scores

# PUSH — V0.1 Creator Scoring Model

## Scoring Philosophy
The score must be:
- Simple enough to compute with spreadsheet data in Phase 1
- Meaningful enough that higher scores predict better campaign outcomes
- Transparent enough that creators understand how to improve
- Resistant to gaming

---

## Push Score: Composite Formula

**Push Score = (Completion × 0.30) + (Reliability × 0.20) + (Quality × 0.25) + (Merchant Satisfaction × 0.15) + (Engagement × 0.10)**

Score range: 0-100

### Dimension 1: Completion Rate (Weight: 30%)
Formula: `(Campaigns completed / Campaigns accepted) × 100`

| Completion Rate | Score Contribution |
|---|---|
| 95-100% | 30 points |
| 85-94% | 24 points |
| 70-84% | 18 points |
| 50-69% | 10 points |
| Below 50% | 0 points |

Why highest weight: A creator who doesn't complete is worthless to the merchant. This is the most fundamental reliability signal.

### Dimension 2: Reliability (Weight: 20%)
Measures: on-time proof submission, deadline adherence, no-show rate

Formula: `((On-time submissions / Total submissions) × 0.6 + (1 - No-show rate) × 0.4) × 100`

| Reliability Score | Score Contribution |
|---|---|
| 90-100% | 20 points |
| 75-89% | 15 points |
| 60-74% | 10 points |
| Below 60% | 0 points |

### Dimension 3: Content Quality (Weight: 25%)
In Phase 1, this is based on merchant rating of content (1-5 stars).
In Phase 2+, add: proof format compliance, content guideline adherence.

Formula: `(Average merchant content rating / 5) × 100`

| Avg Rating | Score Contribution |
|---|---|
| 4.5-5.0 | 25 points |
| 3.5-4.4 | 19 points |
| 2.5-3.4 | 12 points |
| Below 2.5 | 5 points |

### Dimension 4: Merchant Satisfaction (Weight: 15%)
Post-campaign merchant feedback: "Would you work with this creator again?" (1-5 scale)

Formula: `(Average rebook score / 5) × 100`

| Avg Score | Score Contribution |
|---|---|
| 4.5-5.0 | 15 points |
| 3.5-4.4 | 11 points |
| 2.5-3.4 | 7 points |
| Below 2.5 | 0 points |

### Dimension 5: Engagement Proxy (Weight: 10%)
In Phase 1, this is directional only. Based on average engagement on campaign posts.
Formula: `min((Avg post engagement rate / 3%) × 100, 100)` (capped at 100, normalized to 3% as "good")

| Engagement | Score Contribution |
|---|---|
| >3% | 10 points |
| 2-3% | 7 points |
| 1-2% | 4 points |
| <1% | 2 points |

Why lowest weight: Engagement is the most gameable and least tied to merchant ROI. It's included as a signal but not dominant.

---

## Tier System

| Tier | Push Score | Badge | Campaigns Required | Unlocks |
|---|---|---|---|---|
| New | N/A | 🆕 | 0 (just signed up) | Basic campaigns only, max 2 active |
| Rising | 50+ | ⭐ | 3+ completed | All standard campaigns, standby eligible |
| Reliable | 70+ | ⭐⭐ | 8+ completed | Priority matching, premium campaigns, higher payout tier |
| Elite | 85+ | ⭐⭐⭐ | 20+ completed | Top-tier campaigns, highest payouts, featured profile, early access |

### Tier Transition Rules
- **Promotion:** Score must be at or above threshold for 2 consecutive campaigns
- **Demotion:** Score drops below tier threshold for 3 consecutive campaigns (grace period)
- **New → Rising:** Automatic after 3 completed campaigns if score ≥ 50
- **Fast track:** Score ≥ 80 after first 3 campaigns → skip to Reliable

---

## Cold Start Scoring (New Creators)

Problem: New creators have no data. Can't compute a real score.

Solution: **Probationary period (first 3 campaigns)**
- Display "New" badge, no numerical score shown
- Internal provisional score starts at 60 (neutral)
- After each campaign, provisional score adjusts based on actual performance
- After 3 campaigns, real score is calculated and tier is assigned
- Strong early performance (all 3 completed on time, avg rating ≥ 4) triggers fast-track to Rising

---

## Score Decay

Scores should not persist forever without activity.

- **Active creators** (1+ campaign in last 30 days): No decay
- **Inactive 30-60 days:** Score decays 2 points/month
- **Inactive 60-90 days:** Score decays 5 points/month
- **Inactive 90+ days:** Score freezes at current level, profile marked "Inactive"
- **Returning after inactivity:** First campaign back restores active status, score resumes from frozen point

Why: Prevents stale high scores from creators who left. Encourages continuous platform engagement.

---

## Score Recovery After Disputes

| Dispute Outcome | Score Impact |
|---|---|
| Creator found at fault (no-show, fake proof) | -15 points |
| Creator partially at fault | -8 points |
| Not creator's fault (merchant issue) | No impact |
| Dispute resolved in creator's favor | +2 points (trust bonus) |

---

## Anti-Gaming Measures

| Gaming Attempt | Detection | Prevention |
|---|---|---|
| Only accepting easy campaigns | Track campaign difficulty distribution | Require mix of campaign types for tier promotion |
| Fake engagement (buying likes) | Engagement spike analysis, follower/engagement ratio | Engagement is only 10% of score; not worth gaming |
| Colluding with friendly merchants | Repeated same-merchant pairing detection | Flag pairs with >3 consecutive campaigns |
| Rushing low-quality content | Merchant content rating | Quality is 25% of score; low ratings hurt fast |

---

## Phase 1 Implementation (Spreadsheet)

For the first 12 weeks, scoring runs on Google Sheets:

Column A: Creator name
Column B: Total campaigns accepted
Column C: Total campaigns completed
Column D: Completion rate (C/B)
Column E: On-time submissions
Column F: Reliability score
Column G: Avg content rating (1-5)
Column H: Avg merchant rebook score (1-5)
Column I: Avg engagement rate
Column J: Push Score (formula)
Column K: Current tier

Formula for J: `=((D×0.30) + (F×0.20) + ((G/5)×0.25) + ((H/5)×0.15) + (MIN(I/0.03,1)×0.10)) × 100`

This transitions to automated calculation when the website backend handles it.

---

## What to Track for Model Improvement

After 8 weeks of real data:
1. Does a higher Push Score predict merchant repeat? (If not, re-weight)
2. Which dimension best predicts merchant satisfaction? (Increase its weight)
3. Are any dimensions redundant? (Simplify)
4. Are tier thresholds too easy or too hard? (Calibrate)
5. Is score decay too aggressive? (Adjust)

The scoring model is a living system. V0.1 is a hypothesis. V0.2 will be informed by real data.
