---
name: push-attribution
description: "Push attribution system (QR code), verification framework, fraud detection, and integrity operations. Use for any attribution, verification, or fraud question."
---

# Push Attribution & Integrity — Complete Reference

## 1. QR Code Attribution System (Updated 2026-04-11)

### How It Works
1. Each campaign, each participating creator gets a **unique referral ID**
2. Creator publishes content with referral link
3. Fans access referral page via creator's link
4. At the store, consumer scans **merchant's QR code** at checkout (NOT merchant scans consumer)
5. Referral page shows "Activated! Referred by [Creator Name]" + countdown verification code
6. Consumer shows confirmation screen to barista → receives offer/discount

### Design Principles
- **Zero merchant ops burden:** Merchant places ONE daily-rotating QR code at register. Done.
- **No consumer registration required:** Just a webpage showing referral confirmation
- **Transaction-level attribution:** Creator → fan → transaction → repeat purchase — complete chain

### TGTG-Style Promotional Structure
- First X slots (e.g., 20) get FREE product (coffee/pastry)
- After slots filled → remaining referral holders get discount
- Creates FOMO + community effect (Too Good To Go model)
- Merchants already budget for promotions → Push makes promo spend trackable

### Data Captured
- Which creator brought how many customers
- Spend amount per referred customer
- Customer spending level and preferences
- Most popular items
- Repeat visit behavior

## 2. Five Layers of Verification

### Layer 1: Fulfillment Verification
- Visit proof (QR scan timestamp + location)
- Creator actually visited the location
- Merchant QR code scanned = visit confirmed

### Layer 2: Content Verification
- Live URL of published post
- Screenshot backup
- Posting timestamp
- Content persistence check (still live after X days)
- Content matches campaign requirements

### Layer 3: Engagement Context (Directional Only)
- Views, clicks, saves, map opens
- NOT used for scoring heavily (most gameable)
- 10% weight in Push Score

### Layer 4: Merchant-Side Action
- QR code redemptions tracked
- Booking/reservation evidence
- Check-in counts during campaign window
- Event attendance numbers

### Layer 5: Repeat Signal
- Repeat booking by same merchant
- Creator tier progression
- Campaign success pattern data

## 3. Confidence Levels

| Level | Criteria | Action |
|-------|---------|--------|
| Low | Content posted, light engagement, no redemption | Flag for review |
| Medium | Content posted, visit confirmed, limited merchant action | Standard payout |
| High | Content posted, visit confirmed, redemption/QR evidence | Full payout + score boost |

## 4. Attribution by Campaign Type

| Type | Key Verification |
|------|-----------------|
| Sampling | QR scan + content published + product claimed |
| Event Fill | RSVP + check-in + QR code usage |
| Product Launch | Content published + first-wave claims + repeat demand |
| Off-Peak Traffic | Time-window QR scans + visit count |

## 5. Fraud Types & Detection

### Type 1: Fake Fulfillment
Creator claims visit without genuine engagement.
**Detection:** QR scan timestamp mismatch, content analysis shows no real visit, photo metadata check

### Type 2: Fake Merchant Validation
Merchant confirms false completion (e.g., friend's business).
**Detection:** Repeated same-merchant/creator pairing (>3 consecutive), unusually high confirmation rate

### Type 3: Fake Redemption
Self-redemption, friend loops, repeat abuse of single referral.
**Detection:** Same-device scans, same IP, unusual redemption timing, repeat QR scans from same user

### Type 4: Engagement Inflation
Buying likes/views to inflate metrics.
**Detection:** Engagement spike analysis, follower/engagement ratio anomaly, engagement only 10% of score (not worth gaming)

### Type 5: Collusion
Merchant-creator coordination to extract platform value.
**Detection:** Repeated pairing patterns, unusual completion/satisfaction scores, geographic anomalies

## 6. Integrity Risk Signals
- Sudden performance spikes
- Unnatural proof timing patterns
- Same-device/location across multiple "different" users
- Suspicious redemption clustering
- High completion rate + weak merchant satisfaction (gaming indicator)

## 7. Three-Tier Review System

### Tier 1: Passive (Low Risk)
- Trusted users with clean history
- Auto-approve if proof meets standard criteria
- Spot-check 10% randomly

### Tier 2: Triggered (Medium Risk)
- Specific risk flag detected
- Manual review of flagged items
- 24-hour review SLA

### Tier 3: Investigation (High Risk)
- Disputes, repeated patterns, suspected collusion
- Full manual investigation
- 48-hour resolution SLA
- Settlement held during investigation

## 8. Enforcement Ladder
Warning → Score reduction → Tier downgrade → Payout delay → Campaign ineligibility → Suspension → Permanent removal

Principles: Explainable, consistent, proportional. Every enforcement action must be justifiable and communicated clearly.

## 9. AI Verification Roadmap (Agentic Phase 1)
When Push reaches 50+ campaigns:
- **Content quality auto-scoring:** Multimodal AI analyzes composition, lighting, brand fit
- **Proof-of-visit auto-verification:** Geo-tag + timestamp + visual scene analysis
- **Fraud pattern recognition:** Anomaly detection on redemption, timing, pairing patterns
- **Receipt/QR OCR:** Automatic verification of transaction records

This is the highest-ROI AI investment — it's the largest ops cost AND it strengthens Push's core trust layer.

## 10. 30-Day Attribution Window
- All transactions through a creator's referral link within 30 days count toward their commission
- Enables tracking of repeat purchases driven by initial creator content
- Window resets if consumer uses a different creator's link
