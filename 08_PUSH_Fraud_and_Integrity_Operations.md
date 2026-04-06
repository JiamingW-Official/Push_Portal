> **Document ID:** 08 | **Version:** 1.1 | **Last Updated:** 2026-04-05 | **Status:** Active
> **Authoritative For:** Fraud types, integrity signals, review tiers, enforcement framework, merchant integrity controls
> **See Also:** [Doc 04] for fraud entries in risk register; [Doc 07] for verification methods supporting fraud prevention; [Doc 10] for integrity metrics tracking

# PUSH — Fraud and Integrity Operations Skill

## Purpose
This document defines how Push should think about fraud, low-integrity behavior, manipulation risks, and trust-preserving enforcement.

Fraud is not a side issue.
For a company like Push, fraud directly affects:
- merchant trust
- creator quality
- attribution credibility
- repeat revenue
- platform reputation

---

## 1. Fraud Philosophy

The goal is not to police everything aggressively.  
The goal is to preserve a trusted commercial environment while minimizing false positives and operational drag.

Push should assume that fraud will emerge from:
- opportunistic creators
- weak merchants
- collusion
- system loopholes
- incentive misalignment

---

## 2. Major Fraud Types

### Type 1: Fake Fulfillment
A creator claims they visited, completed, or posted, but did not truly satisfy the campaign.

### Type 2: Fake Merchant-Side Validation
A merchant confirms weak or false completion for convenience or collusive reasons.

### Type 3: Fake Redemption
Offer usage is inflated through:
- self-redemption
- friend loops
- non-genuine visits
- repeat abuse

### Type 4: Engagement Inflation
Creators present high vanity metrics with little true campaign value.

### Type 5: Collusion
Merchant and creator coordinate to game payout, rating, or campaign status.

---

## 3. Integrity Risk Signals

Push should monitor signals such as:
- sudden result spikes
- proof patterns that repeat unnaturally
- same-device or same-location anomalies
- suspicious redemption timing
- merchant-creator pairs with abnormal mutual benefit
- creators with high completion but weak merchant value
- creators who target only low-verification campaigns

---

## 4. Fraud Prevention by Design

The strongest fraud control is structural, not punitive.

### Strong Design Choices
- milestone-based workflow
- campaign-specific proof requirements
- selective verification depth
- creator credit impact
- merchant accountability
- delayed settlement where needed
- anomaly-triggered review, not universal manual review

---

## 5. Review Tiers

### Tier 1: Passive Review
Low-risk campaigns or trusted users proceed with minimal friction.

### Tier 2: Triggered Review
Campaign enters review if specific risk flags appear.

### Tier 3: Manual Investigation
Reserved for:
- payout disputes
- repeated suspicious patterns
- suspected collusion
- merchant complaints with evidence

This tiered system preserves user experience while keeping risk manageable.

---

## 6. Enforcement Framework

Push should avoid vague moral language and instead apply rule-based consequences.

Possible consequences:
- warning
- score reduction
- tier downgrade
- payout delay
- campaign ineligibility
- temporary suspension
- permanent removal

Consequences should be:
- explainable
- consistent
- proportional

---

## 7. Merchant Integrity Controls

Merchants should also be subject to platform integrity rules.

Possible merchant abuse:
- bait-and-switch demands
- unfair rejections
- refusing settlement
- manipulating proof standards after acceptance
- colluding with favored creators

Merchant integrity should affect:
- creator visibility
- ability to attract good creators
- support priority
- future campaign quality routing

---

## 8. Fraud vs Mistake

Not every failure is fraud.

Push should distinguish:
- confusion
- weak execution
- lateness
- bad fit
from:
- intentional deception
- repeated gaming
- coordinated abuse

This distinction matters for both fairness and retention.

---

## 9. Integrity Dashboard Concepts

Internally, the platform should track:
- risk score by campaign
- risk score by creator
- risk score by merchant
- anomaly density by category
- dispute cluster by geography
- settlement hold reason
- repeat suspicious pairings

This allows operations to become evidence-based rather than reactive.

---

## 10. Final Standard

A strong integrity system should:
- protect merchants without crushing creator trust
- discourage abuse without overburdening good users
- create consequences that matter economically
- make the platform safer than informal alternatives

Integrity is not just protection.  
It is part of the product.
