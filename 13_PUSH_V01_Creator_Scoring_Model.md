> **Document ID:** 13 | **Version:** 2.0 | **Last Updated:** 2026-04-06 | **Status:** Active
> **Authoritative For:** Specific scoring weights, tier thresholds, score calculations, tier qualifications and perks
> **See Also:** [Doc 01] for strategic pillar (Creator Credit) | [Doc 07] for attribution feeding into scores

# PUSH — V2.0 Creator Scoring Model

## Scoring Philosophy
The score must be:
- Simple enough to compute with spreadsheet data in Phase 1
- Meaningful enough that higher scores predict better campaign outcomes
- Transparent enough that creators understand how to improve
- Resistant to gaming
- **Recency-aware** — recent performance matters more than historical
- **Outcome-linked** — rewards actual business results, not vanity metrics

---

## Push Score v2: Composite Formula

**Base Score = (Completion × 0.25) + (Quality × 0.25) + (Reliability × 0.20) + (Merchant Satisfaction × 0.15) + (Conversion Impact × 0.10) + (Consistency × 0.05)**

**Final Score = Base Score × Recency Modifier × Category Modifier**

Score range: 0-100

### Dimension 1: Completion Rate (Weight: 25%)
Formula: `(Campaigns completed / Campaigns accepted) × 100`

| Completion Rate | Score Contribution |
|---|---|
| 95-100% | 25 points |
| 85-94% | 20 points |
| 70-84% | 15 points |
| 50-69% | 8 points |
| Below 50% | 0 points |

Why: A creator who doesn't complete is worthless to the merchant. This is the most fundamental reliability signal. Reduced from 30% to 25% to balance with quality, which drives actual conversion.

### Dimension 2: Content Quality (Weight: 25%)
In Phase 1, based on merchant rating of content (1-5 stars).
In Phase 2+, add: proof format compliance, content guideline adherence, A/B performance.

Formula: `(Average merchant content rating / 5) × 100`

| Avg Rating | Score Contribution |
|---|---|
| 4.5-5.0 | 25 points |
| 3.5-4.4 | 19 points |
| 2.5-3.4 | 12 points |
| Below 2.5 | 5 points |

Why equal to Completion: Quality directly drives conversion. A completed but low-quality campaign wastes everyone's time. Benchmarked against Fiverr/Upwork where client rating is the dominant signal.

### Dimension 3: Reliability (Weight: 20%)
Measures: on-time proof submission, deadline adherence, no-show rate, brief compliance

Formula: `((On-time submissions / Total submissions) × 0.5 + (1 - No-show rate) × 0.3 + Brief compliance rate × 0.2) × 100`

| Reliability Score | Score Contribution |
|---|---|
| 90-100% | 20 points |
| 75-89% | 15 points |
| 60-74% | 10 points |
| Below 60% | 0 points |

### Dimension 4: Merchant Satisfaction (Weight: 15%)
Post-campaign merchant feedback: "Would you work with this creator again?" (1-5 scale)

Formula: `(Average rebook score / 5) × 100`

| Avg Score | Score Contribution |
|---|---|
| 4.5-5.0 | 15 points |
| 3.5-4.4 | 11 points |
| 2.5-3.4 | 7 points |
| Below 2.5 | 0 points |

Why: Repeat intent is the strongest trust signal. Airbnb's Superhost similarly weights review scores heavily. Merchant satisfaction directly predicts platform retention on both sides.

### Dimension 5: Conversion Impact (Weight: 10%)
Replaces "Engagement Proxy" from v1. Measures actual business outcomes, not vanity metrics.

In Phase 1: Based on redemption codes used + merchant-reported foot traffic change.
In Phase 2+: Add attribution signals from Doc 07.

Formula: `min((Attributed conversions / Expected baseline) × 100, 100)`

| Conversion Signal | Score Contribution |
|---|---|
| Strong (measurable lift) | 10 points |
| Moderate (some signals) | 7 points |
| Weak (minimal evidence) | 3 points |
| None | 0 points |

Why: Replaces Engagement because engagement is gameable and weakly linked to merchant ROI. Conversion Impact measures what merchants actually care about: did people show up and spend money? Inspired by Shopify Collabs' shift to sales-based commission tiers.

### Dimension 6: Consistency (Weight: 5%) — NEW in v2
Measures: How stable a creator's performance is across campaigns. Low variance = high consistency.

Formula: `max(0, 100 - (Standard deviation of per-campaign scores × 2))`

| Consistency | Score Contribution |
|---|---|
| Very stable (σ < 5) | 5 points |
| Stable (σ 5-10) | 4 points |
| Variable (σ 10-20) | 2 points |
| Erratic (σ > 20) | 0 points |

Why: Merchants need predictability. A creator who scores 90 one week and 40 the next is less valuable than one who consistently hits 70. Uber Pro and Airbnb Superhost both evaluate over rolling windows for this reason.

---

## Score Modifiers (v2 additions)

### Recency Weighting
Recent performance should matter more than historical data. Stale scores mislead merchants.

| Time Window | Weight Multiplier |
|---|---|
| Last 90 days | 1.5× |
| 90-180 days | 1.0× |
| 180+ days | 0.5× |

Implementation: Each campaign's score contribution is multiplied by its recency weight before averaging.

### Category Depth Multiplier
Creators who specialize in specific F&B subcategories (cafes, bakeries, boba, etc.) develop expertise that improves outcomes.

| Specialization Level | Multiplier |
|---|---|
| 5+ campaigns in same category | 1.05× (5% bonus) |
| 3-4 campaigns in same category | 1.02× (2% bonus) |
| No specialization | 1.00× (no bonus) |

Caps at 1.05×. Only applies to the specialized category's campaigns.

---

## Tier System

### Color Identity

| Tier | Color | Hex | Meaning |
|---|---|---|---|
| Explorer | Slate | #64748b | Neutral, beginning, unproven |
| Operator | Sky Blue | #0ea5e9 | Reliable, operational, stable |
| Proven | Emerald | #10b981 | Verified, trusted, growing |
| Closer | Amber/Gold | #f59e0b | High-value, results-driven, warm |
| Partner | Violet | #7c3aed | Elite, premium, co-invested |

---

### Explorer — "Enter the system. Prove you can show up."

**Qualification:**
- Complete profile (name, handles, location, content samples)
- Pass content quality check (basic review of existing portfolio)
- No prior violations on platform

**Restrictions:**
- Max 2 active campaigns simultaneously
- Basic campaigns only (no premium or high-value)

**Perks:**
- T+3 payout (3 business days after verification)
- Browse and apply to entry-level campaigns
- Community access (creator forum, resources)
- Probationary scoring (provisional score starts at 60)

---

### Operator — "Consistent execution. The reliable backbone of supply."

**Qualification:**
- Push Score 40+
- 3+ campaigns completed
- 90%+ response rate (accepts/declines within 24h)
- 0 violations in the last 90 days

**Perks:**
- T+2 payout
- All standard campaigns unlocked
- Standby eligible (fill last-minute slots for bonus pay)
- Profile badge (visible to merchants)
- Campaign notifications (push alerts for matching opportunities)
- Basic analytics dashboard

---

### Proven — "Verified performer. Merchants trust you by default."

**Qualification:**
- Push Score 60+
- 8+ campaigns completed
- 60+ days on platform
- 95%+ response rate
- 0 violations in the last 90 days

**Perks:**
- T+1 payout (next business day)
- +5% payout bonus on all campaigns
- Premium campaigns unlocked (higher-budget, branded content)
- Priority matching (shown to merchants first)
- Featured in category search results
- Advanced analytics (conversion data, trend graphs)
- Priority support (faster response from Push team)

---

### Closer — "The acquisition engine. Drives real, measurable business results."

**Qualification:**
- Push Score 75+
- 15+ campaigns completed
- 120+ days on platform
- 30%+ merchant repeat rate (merchants rebook this creator)
- 98%+ response rate
- 0 violations in the last 180 days

**Perks:**
- Same-day payout (within hours of verification)
- +10% payout bonus on all campaigns
- High-value campaigns unlocked (multi-location, chain accounts)
- Dedicated account support (named contact on Push team)
- Campaign co-design (input on campaign structure with merchants)
- Early feature access (beta testing new platform features)
- Merchant repeat priority (auto-recommended to past merchants)

---

### Partner — "The platform's highest-value asset. Long-term, co-invested."

**Qualification:**
- Push Score 85+
- 25+ campaigns completed
- 180+ days on platform
- 50%+ merchant repeat rate
- 99%+ response rate
- 0 violations in the last 365 days
- **Manual review by Push team** (quality gate, similar to Twitch Partner / Fiverr Top Rated)

**Perks:**
- Instant payout (paid within minutes of verification)
- +15% payout bonus on all campaigns
- Co-branded partnership opportunities (joint campaigns with Push branding)
- Revenue share on creator referrals (earn when recruited creators complete campaigns)
- Platform advisory input (quarterly feedback sessions, roadmap influence)
- Custom profile page (personalized portfolio on Push)
- Annual Partner summit invite (networking, exclusive previews)
- Top-tier campaign access (exclusive, invite-only high-budget campaigns)

---

### Tier Transition Rules
- **Promotion:** Score must be at or above threshold for 2 consecutive campaigns
- **Demotion:** Score drops below tier threshold for 3 consecutive campaigns (grace period)
- **Explorer → Operator:** Automatic after 3 completed campaigns if score ≥ 40
- **Fast track:** Score ≥ 70 after first 3 campaigns → skip to Proven
- **Partner gate:** Must pass manual review even if numerical thresholds are met
- **Violation cooldown:** Any violation resets promotion counter and triggers a 30-day cooldown before next evaluation
- **Rolling evaluation:** Tier status re-evaluated after every completed campaign (like Airbnb Superhost's quarterly review, but continuous)

---

## Cold Start Scoring (Explorer Creators)

Problem: New creators have no data. Can't compute a real score.

Solution: **Probationary period (first 3 campaigns)**
- Display "Explorer" badge, no numerical score shown
- Internal provisional score starts at 60 (neutral)
- After each campaign, provisional score adjusts based on actual performance
- After 3 campaigns, real score is calculated and tier is assigned
- Strong early performance (all 3 completed on time, avg rating ≥ 4) triggers fast-track to Operator

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
| Fake engagement (buying likes) | Engagement spike analysis, follower/engagement ratio | Replaced with Conversion Impact in v2 — actual redemptions can't be faked |
| Colluding with friendly merchants | Repeated same-merchant pairing detection | Flag pairs with >3 consecutive campaigns; diversification required for Closer+ |
| Rushing low-quality content | Merchant content rating | Quality is 25% of score; low ratings hurt fast |
| Score sniping (only doing campaigns when score is high) | Track campaign frequency gaps | Consistency dimension (5%) penalizes erratic patterns |
| Ghost profiles (signing up, never engaging) | Track days-since-last-activity | Score decay kicks in at 30 days; tier demotion at 90 days |
| Multi-accounting | IP + device + payment method matching | One account per person; violations = permanent ban |

### Violation System (v2 addition)
Inspired by YouTube's strike system and Uber's cancellation rate:

| Violation Type | Penalty | Cooldown |
|---|---|---|
| No-show (confirmed accept, didn't visit) | -20 points + 30-day promotion freeze | 2 no-shows in 90 days = auto-demotion |
| Fake proof (fabricated visit/content) | -25 points + immediate tier demotion | 2 fake proofs = permanent ban |
| Late proof submission (>48h past deadline) | -5 points | 3 late submissions in 30 days = -10 additional |
| Brief non-compliance | -8 points | Warning first, then penalty |
| Off-platform solicitation | -15 points + 60-day promotion freeze | Second offense = permanent ban |
| Merchant complaint (validated) | -10 points | Investigated case-by-case |

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
Column I: Conversion signals (1-5 scale, manual)
Column J: Consistency (std dev of per-campaign scores)
Column K: Push Score (formula)
Column L: Current tier
Column M: Days on platform
Column N: Response rate
Column O: Violation count

Formula for K: `=((D×0.25) + ((G/5)×0.25) + (F×0.20) + ((H/5)×0.15) + ((I/5)×0.10) + (MAX(0,(100-J×2)/100)×0.05)) × 100`

Note: Recency weighting and category multiplier are applied manually in Phase 1 and automated in Phase 2+.

---

## What to Track for Model Improvement

After 8 weeks of real data:
1. Does a higher Push Score predict merchant repeat? (If not, re-weight)
2. Which dimension best predicts merchant satisfaction? (Increase its weight)
3. Are any dimensions redundant? (Simplify)
4. Are tier thresholds too easy or too hard? (Calibrate — target distribution: ~40% Explorer, ~30% Operator, ~18% Proven, ~8% Closer, ~4% Partner)
5. Is score decay too aggressive? (Adjust)
6. Does Conversion Impact dimension add signal beyond Quality + Satisfaction? (If not, merge)
7. Does Consistency dimension differentiate meaningfully? (If all creators have similar σ, remove)
8. Is recency weighting creating too much volatility? (Adjust multipliers)
9. Are violation penalties proportionate? (Track appeal rate and outcomes)
10. Is the Partner manual review gate calibrated correctly? (Track approval/rejection rate)

The scoring model is a living system. V2.0 is a hypothesis informed by competitive benchmarks (Upwork JSS, Airbnb Superhost, Uber Pro, Fiverr Levels). V2.1 will be informed by real data.

---

## Competitive Benchmarks

| Platform | Evaluation Model | Key Insight for Push |
|---|---|---|
| Upwork (JSS) | Rolling 13-of-16-week success score + earnings threshold | Multi-criteria gates prevent gaming any single dimension |
| Airbnb (Superhost) | Quarterly review, 4.8+ rating, <1% cancellation | Strict cancellation penalty drives reliability |
| Uber Pro | 3-month rolling points + rating + cancellation floor | Rolling window creates urgency for continuous engagement |
| Fiverr (Seller Levels) | Orders + revenue + rating + response rate + manual review at top | Manual gate for top tier creates exclusivity and quality control |
| Twitch (Partner) | Concurrent viewers + hours + manual approval | Manual review + community-building metrics = high-trust top tier |
| DoorDash (Rewards) | Real-time tier adjustments based on ongoing metrics | Real-time feedback loop drives higher engagement than periodic snapshots |

Push v2 combines: Upwork's multi-criteria qualification, Airbnb's strict violation penalties, Uber's rolling evaluation, and Fiverr/Twitch's manual Partner gate.
