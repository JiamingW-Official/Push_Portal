# Push Score Scoring Model

## Composite Formula

**Push Score = (Completion × 0.30) + (Reliability × 0.20) + (Quality × 0.25) + (Merchant Satisfaction × 0.15) + (Engagement × 0.10)**

Range: 0-100

---

## 5 Scoring Dimensions

### 1. Completion Rate (30% weight)
**Formula:** `(Completed / Accepted) × 100`

| Completion % | Points |
|---|---|
| 95-100% | 30 |
| 85-94% | 24 |
| 70-84% | 18 |
| 50-69% | 10 |
| <50% | 0 |

**Rationale:** First and foremost — did you finish what you promised?

---

### 2. Reliability (20% weight)
**Formula:** `((On-time / Total) × 0.6 + (1 - No-show rate) × 0.4) × 100`

| Reliability Score | Points |
|---|---|
| 90-100% | 20 |
| 75-89% | 15 |
| 60-74% | 10 |
| <60% | 0 |

**Components:**
- On-time delivery: 60% of reliability score
- No-show rate: 40% of reliability score

**Rationale:** Can we predict when you'll deliver and that you'll show up?

---

### 3. Content Quality (25% weight)
**Formula:** `(Avg merchant content rating / 5) × 100`

| Merchant Rating | Points |
|---|---|
| 4.5-5.0 ⭐ | 25 |
| 3.5-4.4 | 19 |
| 2.5-3.4 | 12 |
| <2.5 | 5 |

**Rationale:** Does the content actually drive the merchant's business?

---

### 4. Merchant Satisfaction (15% weight)
**Formula:** `(Avg rebook score / 5) × 100`

| Rebook Score | Points |
|---|---|
| 4.5-5.0 ⭐ | 15 |
| 3.5-4.4 | 11 |
| 2.5-3.4 | 7 |
| <2.5 | 0 |

**Rationale:** Would the merchant hire you again? This is the ultimate quality signal.

---

### 5. Engagement Proxy (10% weight)
**Formula:** `min((Avg engagement rate / 3%) × 100, 100)`

| Engagement Rate | Points |
|---|---|
| >3% | 10 |
| 2-3% | 7 |
| 1-2% | 4 |
| <1% | 2 |

**Rationale:** Audience resonance matters, but is capped at 10% to prevent follower-only creators from gaming the system.

---

## Cold Start Scoring

**New Creators:**
- Display "New" badge; no visible score
- Internal provisional score starts at **50** (eligible for Seed tier)
- After **3 completed campaigns** → real score calculated, tier assigned based on performance
- Fast track: If all 3 complete AND avg merchant rating ≥ 4.0 → skip to Operator (score ≥ 65)

---

## Score Decay

**Activity-based decay when creator is inactive:**

| Activity Window | Decay Rate |
|---|---|
| Active (1+ campaign/30 days) | No decay |
| Inactive 30-60 days | -2 points/month |
| Inactive 60-90 days | -5 points/month |
| Inactive 90+ days | Score freezes; profile marked "Inactive" |
| Return from inactive | First campaign back restores active status |

**Rationale:** Inactive creators' historical data becomes less reliable predictors. Returning creators get one campaign to prove they're back in form.

---

## Dispute Impact

When a campaign completion is disputed:

| Outcome | Score Impact |
|---|---|
| Creator at fault (no-show, fake proof, low quality) | -15 |
| Partially at fault (communication breakdown) | -8 |
| Not at fault (merchant issue) | 0 |
| Resolved in creator's favor (merchant false claim) | +2 |

**Rationale:** Disputes are rare; when they happen, significant penalty ensures bad actors exit. Creators wrongly accused get a modest bonus to restore trust.

---

## Tier Transition Rules

### Promotion
- **Condition:** Score at or above tier threshold for **2 consecutive campaigns**
- **Timing:** Auto-applied end-of-campaign
- **From Seed:** Complete 3 campaigns + provisional score ≥ 40 → auto-promote to Explorer

### Demotion
- **Condition:** Score falls below tier threshold for **3 consecutive campaigns** (grace period)
- **Exception:** Demotion never happens during active campaign; only evaluated between campaigns
- **Notification:** Creator receives warning after campaign 1 below threshold; demotion applied after campaign 3

### Fast Track
- **Condition:** Score ≥ 65 achieved within first 3 campaigns
- **Effect:** Skip Explorer, jump directly to Operator
- **Prerequisites:** All 3 campaigns completed, avg merchant rating ≥ 4.0

---

## Anti-Gaming Measures

| Attack Type | Detection Mechanism | Defense |
|---|---|---|
| Cherry-picking easy campaigns | Track campaign difficulty/riskiness distribution | Require balanced mix (at least 1 each of food type, time slot, location) for promotion |
| Fake engagement (buying likes) | Spike analysis; follower/engagement ratio test | Engagement = only 10% of score; easy to game but capped |
| Merchant collusion | Repeated same-merchant pairing | Flag any creator-merchant pair with >3 consecutive campaigns; audit ratings |
| Low-quality rushing | Merchant content rating | Quality = 25% of score; high quality required for tier progression |
| Multi-accounting | Device fingerprint + IP tracking | Link accounts sharing same device; one account per creator |

---

## Phase 1 Spreadsheet Formula

**Columns:** Creator name | Campaigns accepted | Completed | Completion rate | On-time submissions | Reliability | Avg content rating | Avg rebook score | Avg engagement rate | Push Score | Tier

**Excel formula:**
```
=((D×0.30)+(F×0.20)+((G/5)×0.25)+((H/5)×0.15)+(MIN(I/0.03,1)×0.10))×100
```

**Explanation:**
- `D` = Completion rate (already %)
- `F` = Reliability (already %)
- `G` = Avg content rating (1-5 scale)
- `H` = Avg rebook score (1-5 scale)
- `I` = Avg engagement rate (as decimal, e.g., 0.025 for 2.5%)
- `MIN(I/0.03,1)` = Caps engagement contribution at 100%
