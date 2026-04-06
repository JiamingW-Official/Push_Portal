> **Document ID:** 14 | **Version:** 2.0 | **Last Updated:** 2026-04-06 | **Status:** Active
> **Authoritative For:** Core invariant, MVP loop, timing thesis, failure modes, beachhead wedge, behavior design, positioning lines, competitive alternatives, north star metric, growth flywheel, OS positioning, data moat, founder-market fit
> **See Also:** [Doc 01] for master strategy | [Doc 05] for execution skills | [Doc 11] for cold start plan

# PUSH — Strategic Foundations

## 1. Core Invariant

**Push only rewards verified, repeatable value creation.**

This is the unbreakable design principle. Every feature, every tier rule, every payout decision must pass three tests:
1. **Can it be verified?** — If we can't prove it happened, it doesn't count
2. **Can it be repeated?** — One-off value is not enough; the system must compound
3. **Does it create real value?** — Vanity metrics, impressions, and follower counts are not value

Why this matters:
Without an invariant, you will be pulled toward:
- UI features that look impressive but don't drive outcomes
- Social features that generate engagement but not revenue
- "Platform-looking" features that don't actually solve the merchant's problem

Every design decision should be filtered through this invariant.

---

## 2. Minimum Viable Loop (MVP Loop)

The smallest business unit that proves Push works:

**1 merchant + 5 creators = 1 complete loop**

| Step | Action | Who |
|------|--------|-----|
| 1 | Merchant publishes campaign (goal + offer + slots) | Merchant |
| 2 | 3–5 creators apply and are matched | Platform |
| 3 | Creators visit, create content, submit proof | Creator |
| 4 | Merchant confirms delivery, rates quality | Merchant |
| 5 | Platform records data → creator score updates → merchant considers repeat | Platform |

**If this loop runs once, Push is alive.**
**If the merchant repeats, Push is a business.**
**If the loop can't complete, nothing else matters.**

This loop must be the first thing that works. Everything else — scoring, tiers, automation — is built on top of a working loop.

---

## 3. Why Now (Timing Thesis)

Three structural shifts make this the right moment:

### Signal 1: Creator Supply Overflow
- 200M+ creators globally, 50M+ in the US
- Micro-creators (1K–15K followers) are everywhere
- But commercial structure is missing — 99% of local deals happen over DMs
- **Supply is massive. Infrastructure is zero.**

### Signal 2: Brands Shift from Exposure to Conversion
- 72% of local businesses plan to increase creator spend (Localiq 2025)
- They no longer believe in follower counts — they want measurable results
- Already paying $500–$2K/mo on Yelp ads that don't convert
- **The budget exists. The channel doesn't.**

### Signal 3: Local Commerce Rebound
- Cafés, wellness, events — local experience economy growing fast
- High frequency + visual content = perfect for creator partnerships
- No one has built the Shopify for local creator commerce
- Agencies charge $3K+ minimums, influencer platforms target e-commerce only
- **The market isn't competitive — it's empty.**

**One-line summary:** Supply exists, demand exists, but the infrastructure doesn't.

---

## 4. Failure Modes

If Push fails, it will be because of one of these:

| Failure Mode | What Happens | How We Prevent It |
|---|---|---|
| Creator supply quality is too low | Merchants get bad content, churn immediately | Multi-dimensional scoring (v2), tier gates, violation system, quality is 25% of Push Score |
| Merchants don't repeat | No economic model, unsustainable unit economics | Free first campaign, template-driven repeat, dashboard showing ROI, subscription habit loop |
| Attribution isn't credible | Core value prop collapses, merchants lose trust | Structured proof chain (visit → content → publish → verify), merchant confirmation gate |
| Platform gets bypassed | Merchants and creators go direct, Push gets hollowed out | Non-portable credit capital, tier-locked perks, compounding switching costs |

Key insight: We don't just list risks — we proactively design defenses into the system architecture.

→ See [Doc 04] for the full 16-risk register with prioritization framework.

---

## 5. Beachhead Wedge

We don't say "all local businesses." We say:

**One ZIP code. Three categories. NYC café + dessert + beauty.**

Why this wedge:
- **High frequency**: Customers visit weekly, not annually
- **Visual content**: Photogenic products = strong creator content
- **Creator-dense**: NYC has the highest micro-creator density in the US
- **Small-ticket testable**: $8–15 COGS per creator visit, low risk for merchants
- **Owner-operated**: Decision-maker is on-site, fast sales cycle

What we don't do:
- ❌ "All local businesses" — too broad, no density
- ❌ "All US cities" — no network effects without geographic density
- ❌ "E-commerce creators" — different problem, different infrastructure
- ❌ "Enterprise brands" — wrong customer size for our model

Expansion path: One neighborhood → 3 neighborhoods (same city) → second city → multi-city

---

## 6. Behavior Design

Push is not just a system — it is a behavior engine.

### Creator Behavior Drivers

| Mechanism | Psychological Trigger | Effect |
|---|---|---|
| Limited campaign seats | FOMO (scarcity) | Act now or miss the opportunity |
| Standby queue | Gamification (near-miss) | Always one slot away — stay engaged |
| Tier progression | Growth narrative | "I'm building something valuable" |
| Fast payouts (T+3 → instant) | Instant gratification | Effort → money today, not next month |
| Non-portable score | Loss aversion | Leaving means losing everything built |

### Merchant Behavior Drivers

| Mechanism | Psychological Trigger | Effect |
|---|---|---|
| Campaign templates | Cognitive ease | Don't think, just launch |
| One-click repeat | Habit loop | Worked once → do it again |
| Real-time dashboard | Illusion of control | "I can see what's happening" |
| Creator tier badges | Social proof / safety | Picking a vetted creator, not guessing |
| ROI comparisons | Anchoring | "$79/mo vs $500/mo agency" makes Push look cheap |

### Why this matters:
The best infrastructure in the world fails if people don't use it. Behavior design ensures that both sides of the marketplace have clear, immediate, and recurring reasons to engage.

---

## 7. Killer Lines (Positioning)

Use these in pitch decks, investor conversations, and external communications:

**Primary (most versatile):**
> Push is where local businesses stop guessing and start buying results from creators.

**Infrastructure framing (for technical audiences):**
> Push builds the credit system for the creator economy in local commerce.

**Alternative comparison (for competitive discussions):**
> All existing solutions help you find creators. None help you operate them as a system.

**Timing (for "why now" conversations):**
> Supply exists, demand exists, but the infrastructure doesn't.

**Invariant (for product/design alignment):**
> Push only rewards verified, repeatable value creation.

---

## 8. Competitive Alternatives: Why Not?

| Alternative | Why Merchants Use It | Why It Fails |
|---|---|---|
| DM a creator directly | Free to try, feels personal | Not scalable, not comparable, not repeatable. No data, no accountability |
| Local marketing agency | Low effort for merchant | Too expensive ($500–2K/mo), not designed for creator-level granularity |
| TikTok / Yelp / IG Ads | Familiar platform, easy to start | Distribution only — no accountability for results, no creator relationship |
| Brand deal platforms | Access to large creators | $5K+ minimums. A boba shop with $300/mo budget doesn't exist in their world |

**Push's position:** Cheaper than all alternatives AND requires less merchant effort AND provides full attribution. The only option that operates creators as a repeatable system.

---

## 10. North Star Metric

**The one number**: Verified repeat campaign value per merchant

- Combines: merchant retention + creator delivery + verified outcomes
- If this number grows, Push is winning. If it stalls, nothing else matters.
- Why this metric: it can't grow unless BOTH sides are working. A vanity metric (GMV, total campaigns) can grow while the system is broken.

---

## 11. Growth Engine (Self-Reinforcing Flywheel)

6-step loop:

1. More merchants join →
2. More campaigns created →
3. More creator opportunities →
4. Better creators stay (because opportunities + score investment) →
5. Better results (because better creators) →
6. Merchant repeat (because results are real) → back to 1.

Each cycle compounds the data layer, making matching smarter and results more predictable.

---

## 12. Operating System Positioning

Push is not a platform. Push is an operating system.

- **Platform** = connects two sides. Replaceable.
- **Operating System** = makes both sides perform. Irreplaceable.
- The switching cost is the accumulated intelligence inside: creator scores, merchant playbooks, matching algorithms trained on real campaign data.
- Benchmark: Shopify is an OS for e-commerce. Push is the OS for local creator commerce.

---

## 13. Data Moat (The Performance Data Layer)

Two-sided data that no competitor can replicate without running the same campaigns:

- **Creator-side:** completion rates by category/location, reliability across time windows, content quality per merchant type, conversion lift per creator profile
- **Merchant-side:** which campaigns drive repeat visits, which creators convert for which categories, optimal timing/pricing/offer structure, repeat strategy patterns that predict LTV
- **Together:** an irreplicable matching engine that gets smarter with every campaign

---

## 14. Founder-Market Fit (Enhanced)

- NYC-based, at the intersection of creator culture, design systems, and local commerce
- Not a paper idea: 16 failure modes mapped, scoring algorithm built, cold-start plan scripted week by week, every economic assumption stress-tested
- The work is done. What's left is proving it in market.

---

## 15. Unit Economics Loop

Per-campaign economics that prove "the more we do, the more we earn":

| Line Item | Amount |
|---|---|
| Merchant pays | $200 |
| Creator payout | $120 |
| Platform take rate | $20 |
| Campaign fee | $30 |
| Ops & support | $10 |
| **Platform net** | **$70 (35% margin)** |

Why this matters: Without unit economics, you have "a busy system that doesn't make money." Push's margin improves with scale because ops cost drops with automation while creator payout stays stable.

---

## 16. PMF Signal Definition

**The one signal**: When merchants start running campaigns repeatedly *without being pushed*, we know we have product-market fit.

Not user growth. Not downloads. Not creator signups. The only signal that matters: **unprompted merchant repeat**.

Why this is the right signal: It can't be faked, it can't be bought, and it proves both sides of the marketplace are working.

---

## 17. Brutal Simplification (Minimum Viable Push)

If we cut 80% of the product, Push still works with 5 steps:
1. Merchant posts campaign (manual, even a Google Form)
2. Creator accepts (even via DM)
3. Proof submitted (screenshot of published post)
4. Merchant confirms (yes/no)
5. Result recorded (spreadsheet row)

No map. No fancy UI. No complex algorithms. This runs on a spreadsheet + DMs. The system works before the product exists — that's how we know the value is real.

---

## 18. Quality Defense (Why Push Won't Become a Race-to-Bottom Marketplace)

Every marketplace faces the same death spiral: prices drop, quality drops, supply floods. Push prevents this with 4 structural defenses:

1. **Tier System** — Quality gates at every level. Not everyone can access premium campaigns.
2. **Credit History** — Past performance is visible and weighted. New entrants compete on merit, not price.
3. **Verification** — Every outcome is checked. You can't fake your way up.
4. **Access Control** — High-value campaigns are gated by tier and score. The best work goes to the best performers.

**One-line summary**: Push is not an open marketplace — it is a curated, performance-gated system.

---

## 19. Control Point (What Push Actually Controls)

The core resource Push controls is not users, creators, or content. Those are all replaceable.

Push controls: **access to high-quality demand**.

Specifically:
- Which campaigns appear on the platform
- Who can see them
- Who can accept them
- Who gets priority access
- Who gets to keep earning consistently

This is the deepest moat. Whoever controls the distribution of opportunity controls the ecosystem.

---

## 20. Structure Completion Checklist

| Layer | Status | Where |
|---|---|---|
| Idea / Vision | ✅ Complete | Doc 01 |
| Tier System (5 tiers + scoring v2) | ✅ Complete | Doc 13 |
| Risk Register (16 risks) | ✅ Complete | Doc 04 |
| Pricing Model ($79/$249/$699) | ✅ Complete | Doc 12 |
| Workflow Architecture (7 milestones) | ✅ Complete | Doc 02 |
| Retention & Anti-Bypass | ✅ Complete | Doc 01, Doc 06 |
| **Core Invariant** | ✅ Added | This doc (Section 1) |
| **MVP Loop** | ✅ Added | This doc (Section 2) |
| **Timing Thesis** | ✅ Added | This doc (Section 3) |
| **Failure Modes** | ✅ Added | This doc (Section 4) |
| **Beachhead Wedge** | ✅ Added | This doc (Section 5) |
| **Behavior Design** | ✅ Added | This doc (Section 6) |
| **Killer Lines** | ✅ Added | This doc (Section 7) |
| **Competitive Alternatives** | ✅ Added | This doc (Section 8) |
| **North Star Metric** | ✅ Added | This doc (Section 10) |
| **Growth Engine (Flywheel)** | ✅ Added | This doc (Section 11) |
| **OS Positioning** | ✅ Added | This doc (Section 12) |
| **Data Moat** | ✅ Added | This doc (Section 13) |
| **Founder-Market Fit** | ✅ Added | This doc (Section 14) |
| **Unit Economics Loop** | ✅ Added | This doc (Section 15) |
| **PMF Signal Definition** | ✅ Added | This doc (Section 16) |
| **Brutal Simplification** | ✅ Added | This doc (Section 17) |
| **Quality Defense** | ✅ Added | This doc (Section 18) |
| **Control Point** | ✅ Added | This doc (Section 19) |

All nineteen strategic foundation layers are now documented and integrated into the pitch deck and website.
