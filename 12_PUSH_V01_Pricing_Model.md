> **Document ID:** 12 | **Version:** 1.0 | **Last Updated:** 2026-04-05 | **Status:** Active
> **Authoritative For:** Specific pricing numbers, fee structures, payment flows
> **See Also:** [Doc 06] for economic framework | [Doc 11] for cold start pricing transitions

# PUSH — V0.1 Pricing Model

## Pricing Philosophy
Price for learning, not for revenue. In the first 3 months, pricing should:
- Remove friction for merchants to try Push
- Prove willingness to pay exists
- Establish value perception early
- Not destroy margins when you need to scale

---

## Phase 1: Free Launch (Week 1-8)

### Merchant Pricing: $0
Everything free. The goal is data and repeat behavior, not revenue.

What merchants provide:
- The offer to creators (free food/drink, typically $8-15 retail value)
- Their time for brief feedback after each campaign

What Push provides:
- Creator matching
- Campaign management
- Proof collection and verification
- Post-campaign summary

### Creator Compensation
| Campaign Type | Creator Gets |
|---|---|
| Standard F&B visit + 1 post | Free item (merchant provides) + $25-35 cash (Push pays) |
| Premium content (Reel/TikTok) | Free item + $40-50 cash |
| Story-only (lower effort) | Free item + $15-20 cash |

Creator payment timing: Within 24 hours of verified completion via Venmo/Zelle.

### Why These Numbers
- $25-35 is enough to motivate micro-creators (1K-15K followers) for a 1-2 hour commitment
- Below $25 feels exploitative for the effort involved
- Above $50 is unsustainable at this stage
- Free item from merchant costs them $3-8 (COGS), not retail price

---

## Phase 2: Introductory Paid (Week 9-12)

### Merchant Pricing

**Option A: Per-Campaign Pricing**
| Tier | Price | What's Included |
|---|---|---|
| Starter | $49/campaign | 2 creator slots, basic reporting, standard matching |
| Growth | $79/campaign | 3 creator slots, detailed reporting, priority matching |

**Option B: Monthly Subscription (Recommended)**
| Plan | Price | Campaigns/month | Extra Campaign |
|---|---|---|---|
| Basic | $99/month | Up to 3 campaigns | $39 each |
| Pro | $199/month | Up to 8 campaigns | $29 each |

**Recommended starting point:** Option B, Basic plan at $99/month. Why:
- Subscription creates habit and recurring revenue signal
- $99/month is less than 1 Instagram ad campaign
- 3 campaigns/month is realistic for a small F&B shop
- Monthly commitment increases merchant seriousness

### Creator Compensation (Phase 2)
Now funded by merchant fees instead of Push's pocket:

| Source | Amount |
|---|---|
| Merchant provides | Free item ($8-15 value) |
| Push pays creator from campaign fee | $20-30 per campaign |
| Push keeps | $19-49 per campaign (margin) |

### Platform Take Rate (Future)
Not implemented in Phase 2, but designed for Phase 3+:
- 15% take rate on all creator payouts processed through Push
- Applied when campaign fees alone don't capture enough value
- Only activate when attribution is strong enough to justify

---

## Pricing Comparison: Push vs Alternatives

| Method | Cost to Merchant | Measurability | Effort |
|---|---|---|---|
| DM a creator directly | $50-200 per post + product | None | High (find, negotiate, manage) |
| Local marketing agency | $500-2000/month | Low-Medium | Low |
| Instagram/Facebook Ads | $200-1000/month | Medium | Medium |
| **Push Basic** | **$99/month** | **Medium-High** | **Very Low** |

This comparison is your sales weapon. Push is cheaper than all alternatives AND requires less merchant effort.

---

## Payment Flow Architecture

### Phase 1-2 (Manual)
```
Merchant pays Push → Venmo/Zelle or Stripe invoice
Push pays Creator → Venmo/Zelle within 24h of verification
```

### Phase 3+ (Automated via Stripe Connect)
```
Merchant subscribes → Stripe monthly billing
Campaign completes → Auto-verification
Creator payout → Stripe Connect transfer (T+2 days)
Platform fee → Auto-deducted
```

---

## Financial Model: First 12 Weeks

### Revenue Projections (Conservative)
| Week | Paying Merchants | Revenue |
|---|---|---|
| 1-8 | 0 | $0 (free phase) |
| 9 | 2 | $198 |
| 10 | 3 | $297 |
| 11 | 4 | $396 |
| 12 | 5 | $495 |
| **Total W9-12** | | **~$1,386** |

### Cost Projections
| Item | Total 12 Weeks |
|---|---|
| Creator subsidies (Phase 1) | $750-1,200 |
| Domain + tools | $50 |
| Misc operations | $200 |
| **Total** | **~$1,000-1,450** |

### Break-even trajectory
At $99/month per merchant, you need ~15 paying merchants to cover ongoing creator costs when creators are paid from campaign fees instead of your pocket. This is achievable by Month 4-5.

---

## Pricing Experiments to Run

1. **$49 vs $99 per month**: Test with different merchant cohorts
2. **Per-campaign vs subscription**: Which gets higher adoption?
3. **Creator payout sensitivity**: Does $25 vs $35 affect completion rate?
4. **Standby premium**: Would merchants pay $20 extra for guaranteed fill?

---

## Rules and Guardrails

- NEVER charge a merchant before they've completed at least 1 free campaign
- ALWAYS pay creators within 24 hours (this is a trust-building non-negotiable)
- Creator minimum payout: $15 (below this feels exploitative)
- Merchant maximum first-month price: $99 (no premium tiers until proven value)
- No annual contracts in Phase 1-2 (monthly only, cancel anytime)
- Refund policy: Full refund if campaign gets zero completions
