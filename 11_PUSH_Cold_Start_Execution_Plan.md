> **Document ID:** 11 | **Version:** 1.0 | **Last Updated:** 2026-04-05 | **Status:** Active
> **Authoritative For:** Cold start execution, week-by-week launch plan, first merchant/creator acquisition tactics
> **See Also:** [Doc 09] for GTM experiment framework | [Doc 05] for execution skills | [Doc 01] for strategic alignment

# PUSH — Cold Start Execution Plan

## Overview
This is not a strategy document. This is a step-by-step execution plan for the first 12 weeks of Push, starting from zero merchants and zero creators in a single US neighborhood focused on F&B.

The plan is divided into 3 phases:
- **Phase 1 (Week 1-4):** Foundation — build supply on both sides manually
- **Phase 2 (Week 5-8):** First campaigns — prove the workflow works
- **Phase 3 (Week 9-12):** Validate repeat — prove merchants come back

---

## Phase 1: Foundation (Week 1-4)

### Week 1: Zone Selection & Merchant Scouting

**Monday-Tuesday: Zone Selection**
Pick ONE neighborhood (not a whole city). Selection criteria:
- At least 30 independent F&B shops within a 15-minute walking radius
- Not dominated by chains (Starbucks, Dunkin won't work initially)
- Active local food/lifestyle creator scene on Instagram
- Walkable and photogenic (creators need good content opportunities)

**Recommended zones by city:**
- LA: Silver Lake, Echo Park, or Sawtelle
- NYC: Williamsburg, LES, or Astoria
- SF: Mission District or Hayes Valley

**Wednesday-Friday: Merchant Scouting (Goal: identify 30 prospects)**
Walk the neighborhood. For each prospect, note:
- Business name, address, Instagram handle
- Type (cafe, bakery, boba, dessert, brunch spot)
- Vibe check: Is the space photogenic? Is the food visual?
- Busy hours vs dead hours (observe foot traffic)
- Owner-operated vs managed (owner-operated is better for early sales)
- Current social media presence (do they already work with creators?)

**Tool:** Use a Google Sheet with columns: Name, Address, Instagram, Type, Visual Score (1-5), Dead Hours, Owner-Operated (Y/N), Current Creator Activity, Contact Status

**Saturday-Sunday: Creator Research (Goal: identify 50 creator prospects)**
Search Instagram and TikTok:
- Location tags for the neighborhood
- Hashtags: #[neighborhood]eats, #[neighborhood]food, #[city]foodie, #[city]cafe
- Local food bloggers with 1K-15K followers (micro-creators, not macro)
- Look at who has tagged the prospect merchants already

For each creator prospect, note:
- Handle, platform, follower count, engagement rate (likes/followers)
- Content quality (1-5)
- Posting frequency
- Location relevance (do they actually visit this neighborhood?)
- Contact method (DM, email in bio)

---

### Week 2: First Merchant Conversations

**Goal: Have conversations with 15 merchants, get 8 soft commitments**

**How to approach (in person, not email):**
Walk in during a slow period (Tuesday-Thursday, 2-4pm). Order something. Then:

**Opening script:**
"Hey, I noticed you guys have a great spot here. I'm building something called Push — we help local shops like yours get new customers through local food creators. Instead of you having to find and manage creators yourself, we handle the matching, the deliverables, and we track whether it actually works. Would you be open to trying it out for free as one of our first partners?"

**Key points to hit:**
- FREE for the first campaign (remove all friction)
- You handle everything (matching, management, verification)
- They just need to provide the offer (free item or discount)
- Emphasis: "We track whether it actually brings people in"
- Timeline: "We're launching in [2-3 weeks], you'd be in the first batch"

**What to capture from interested merchants:**
- What are your slow days/hours?
- What item would you be willing to offer creators? (free coffee, free pastry, etc.)
- What would make this worth it for you? (more weekday traffic? more Instagram exposure? first-time visitors?)
- Best way to follow up?

**Realistic conversion:** 15 conversations → 8 interested → 5-6 committed for first batch

---

### Week 3: Creator Outreach & Website MVP

**Creator outreach (Goal: Get 20 creators signed up)**

DM script for Instagram/TikTok:
"Hey [name]! Love your content at [specific place they posted about]. I'm launching Push — a platform that connects local food creators with shops in [neighborhood] for paid campaigns. We're starting with [number] spots in our first batch and I think you'd be a great fit. Interested in learning more?"

**What to tell interested creators:**
- How it works: you visit a partnered shop, create content, post it, and get paid
- First campaigns pay [specific: $25-50 cash + free food/drink]
- You build a performance score that unlocks better-paying campaigns
- We handle the logistics — you just show up, create, and post

**Website MVP requirements (build this week):**
- Landing page explaining Push for both merchants and creators
- Merchant signup form (name, business, address, Instagram, goals, availability)
- Creator signup form (name, handles, location, content type, availability)
- Campaign listing page (what's available)
- Simple admin dashboard for you to manage campaigns manually
- Tech: Next.js or simple React site, deploy on Vercel, use Airtable or Supabase as backend for now

---

### Week 4: Campaign Setup & Dry Run

**Set up first 5 campaigns manually:**
For each merchant, create a campaign with:
- Merchant name and location
- Offer: what the creator gets (e.g., "2 free drinks + $30 cash")
- Deliverables: what the creator must do (e.g., "1 Instagram Reel or TikTok, must tag @merchant and @push, must show the location")
- Proof requirements: screenshot of published post, timestamp
- Deadline: 5 days from acceptance
- Slots: 2-3 creators per campaign

**Match creators to campaigns:**
- Match by location proximity, content style, and category fit
- Send each matched creator the campaign details via DM or email
- Get explicit acceptance

**Dry run: Do 1-2 campaigns yourself**
- Visit a merchant yourself, create sample content, post it
- Document the entire flow: what worked, what was confusing
- Use this to refine the creator instructions

---

## Phase 2: First Campaigns (Week 5-8)

### Week 5-6: Execute First Campaign Batch

**Launch 5 campaigns simultaneously**
- 5 merchants × 2-3 creators each = 10-15 campaign slots
- You personally manage every campaign via DM/text/email
- Track in Google Sheet: creator, merchant, status, proof submitted (Y/N), content URL, merchant feedback

**Daily ops during active campaigns:**
- Morning: check for overdue proofs, send reminders
- Afternoon: review submitted proofs, confirm with merchants
- Evening: track content publication, save URLs

**After each completion:**
- Pay creator within 24 hours (Venmo/Zelle — fast and visible)
- Ask merchant: "Did you notice any new faces? How was the content quality? Would you do this again?"
- Ask creator: "How was the experience? Was anything confusing? Would you do another one?"

**Document everything:** What went wrong, what went right, what was confusing

---

### Week 7-8: Second Batch + First Improvements

**Goal: 5-8 more campaigns, including at least 2 repeat merchants from batch 1**

If merchants from batch 1 want to go again, that's your strongest signal. Track:
- **Merchant repeat rate:** how many of the original 5 want a second campaign?
- **Creator repeat rate:** how many of the first creators want another campaign?
- **Time-to-fill:** how fast do creators accept when you offer a campaign?
- **Proof completion rate:** what % of creators complete on time?
- **Content quality:** are merchants satisfied with what was produced?

**Iterate on the website:**
- Add campaign status tracking (so creators can see their campaigns)
- Add basic post-campaign reporting for merchants
- Add creator profiles with completion history

**Key numbers to hit by end of Week 8:**
- 8+ merchants have run at least 1 campaign
- 15+ creators have completed at least 1 campaign
- 3+ merchants have run a SECOND campaign (repeat!)
- Proof completion rate > 80%
- Creator satisfaction > 4/5
- Merchant satisfaction > 3.5/5

---

## Phase 3: Validate Repeat (Week 9-12)

### Week 9-10: Scale to 15 Merchants, Introduce Scoring

**Expand merchant base:**
- Referral from existing merchants: "Know any other shops that would want this?"
- Walk-in outreach to 10 more prospects in the same neighborhood
- Target: 15 active merchants by end of week 10

**Introduce basic creator scoring:**
Display on creator profiles:
- Campaigns completed: [number]
- Completion rate: [%]
- Average merchant rating: [X/5]
- Tier badge: "Explorer" / "Operator" / "Proven" / "Closer" / "Partner"

**Introduce standby:**
When a creator drops out last-minute, notify nearby qualified creators:
"🚨 [Merchant Name] has an open campaign slot for tomorrow. $30 + free items. Accept within 2 hours."

---

### Week 11-12: First Paid Campaigns + Data Review

**Transition from free to paid:**
After proving value through free campaigns, introduce merchant pricing:
- First campaign: FREE (already done)
- Second campaign: FREE (already done for repeaters)
- Third campaign onwards: $49/campaign flat fee (introductory price)
- Or: $79/month for up to 3 campaigns

**Have the pricing conversation:**
"You've run [X] campaigns with us and [results]. Going forward, campaigns are $49 each or $79/month for 3. That's way less than what agencies charge, and you've already seen it works."

**Week 12 data review — the numbers that matter:**
1. Merchant repeat rate (target: 40%+ of merchants run 2+ campaigns)
2. Creator completion rate (target: 85%+)
3. Time-to-fill (target: <48 hours)
4. Merchant willingness to pay (target: 30%+ convert to paid)
5. NPS or satisfaction score (target: >7/10 both sides)
6. Total campaigns completed (target: 25+)
7. Revenue (target: any revenue proves willingness to pay)

**Go/No-Go decision framework:**
- ✅ GO if: merchant repeat > 30%, completion > 80%, some willingness to pay
- ⚠️ ITERATE if: one metric is weak but others are strong — diagnose and fix
- ❌ PIVOT if: no merchant repeat, creators unreliable, zero willingness to pay

---

## Budget Estimate (12 weeks)

| Item | Cost |
|------|------|
| Creator payments (first batch, ~15 creators × $30-50) | $450-750 |
| Creator payments (second batch, ~20 slots × $30-50) | $600-1000 |
| Domain + hosting (Vercel free tier + domain) | $15/year |
| Google Workspace | $7/month |
| Tools (Airtable/Supabase free tier) | $0 |
| Walking-around money (buying food at merchants during scouting) | $200 |
| Miscellaneous | $200 |
| **Total estimated: $1,500 - $2,200** | |

This is deliberately bootstrapped. The biggest cost is creator payments, and those go down as merchants start paying.

---

## Tools Stack (MVP)

| Function | Tool | Cost |
|----------|------|------|
| Website | Next.js + Vercel | Free |
| Database | Supabase (free tier) | Free |
| Campaign management | Google Sheets → then website admin | Free |
| Creator/merchant comms | DM + email | Free |
| Creator payments | Venmo/Zelle → then Stripe | Free → 2.9% |
| Content tracking | Manual → then website | Free |
| Analytics | Google Analytics + manual tracking | Free |

---

## What Success Looks Like at Week 12

You have:
- A working website where merchants can browse creators and creators can browse campaigns
- 15 merchants who have used Push, 5+ who have paid
- 25+ creators with real performance history on the platform
- 25+ completed campaigns with verified outcomes
- Data showing whether the core hypothesis works: can Push make merchant-creator collaboration structured, measurable, and repeatable?

That data is what you take into the next phase: raising money, hiring, or expanding to the next neighborhood.
