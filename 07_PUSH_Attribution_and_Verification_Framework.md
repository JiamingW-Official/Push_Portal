> **Document ID:** 07 | **Version:** 1.1 | **Last Updated:** 2026-04-05 | **Status:** Active
> **Authoritative For:** Attribution layers, confidence scoring, verification methods, campaign-type measurement, reporting logic
> **See Also:** [Doc 02] for workflow verification step integration; [Doc 08] for fraud-related verification signals; [Doc 10] for attribution metrics in dashboard context

# PUSH — Attribution and Verification Framework Skill

## Purpose
This document defines how Push should think about attribution, proof quality, confidence levels, and result legitimacy.

Attribution is not a reporting add-on.
It is one of the core systems that determines trust, pricing power, repeat merchant behavior, and long-term defensibility.

---

## 1. Attribution Philosophy

Push does not need perfect attribution on day one.  
But it must build **credible attribution confidence**.

The objective is not to claim impossible certainty.  
The objective is to make results more structured, trustworthy, and decision-useful than today’s alternatives.

---

## 2. What Attribution Should Answer

Attribution should help answer:

- Did the creator actually fulfill the campaign?
- Did the audience receive the content?
- Did the campaign create meaningful merchant-side action?
- Which creators are more commercially effective?
- Which campaign types are worth repeating?

---

## 3. Layers of Verification

### Layer 1: Fulfillment Verification
Confirms that the creator executed required actions.

Examples:
- visit proof
- timestamped upload
- merchant acknowledgement
- draft submission
- content link submission
- presence evidence

### Layer 2: Content Verification
Confirms that required content was actually published and visible.

Examples:
- live URL
- screenshot evidence
- posting timestamp
- persistence checks
- basic compliance review

### Layer 3: Engagement Context
Captures directional indicators without over-trusting them.

Examples:
- views
- clicks
- saves
- replies
- swipe actions
- map opens

### Layer 4: Merchant-Side Action
Captures value closer to commerce.

Examples:
- redemptions
- bookings
- first-time visit markers
- offer claims
- check-in completions
- event attendance confirmation

### Layer 5: Repeat Signal
Captures longer-term relevance.

Examples:
- merchant repeat booking of creator
- creator invited into higher-value campaign
- repeat campaign type success
- return merchant behavior

---

## 4. Confidence Scoring

Push should avoid binary thinking where attribution is either “fully proven” or “useless.”

Instead, create confidence levels such as:

### Low Confidence
- content posted
- light engagement reported
- no redemption evidence

### Medium Confidence
- content posted
- visit confirmed
- claim or intent signal exists
- limited merchant-side action seen

### High Confidence
- content posted
- fulfillment confirmed
- merchant-side redemption or booking evidence present
- campaign outcome legible enough for repeat decisions

This is more realistic and operationally useful.

---

## 5. Attribution by Campaign Type

Not all campaign types should be measured the same way.

### Sampling Campaign
Best measured by:
- fulfillment completion
- content publication
- offer claim
- merchant observation
- optional redemption

### Event Fill Campaign
Best measured by:
- RSVP or attendance
- check-in
- event code or invite usage
- time-window correlation

### Product Launch Campaign
Best measured by:
- content publication
- first-wave claims or redemptions
- merchant-side awareness signal
- repeat demand in short window

### Off-Peak Traffic Campaign
Best measured by:
- time-window redemption
- visit counts during targeted periods
- repeat merchant perception of impact

---

## 6. Attribution Failure Modes

### Failure Mode A: Over-Reliance on Views
Views are easy to collect but weak as a primary commercial signal.

### Failure Mode B: Overclaiming Causality
Push should not imply direct causality when only directional evidence exists.

### Failure Mode C: One-Size-Fits-All Measurement
Different merchant goals require different proof logic.

### Failure Mode D: Poor Merchant Interpretation
Even good data fails if merchants cannot understand what happened.

---

## 7. Platform Design Implications

To support good attribution, Push should:
- define verification method at campaign creation
- match campaign type to proof logic
- expose clear proof steps to creators
- show confidence level in merchant dashboard
- separate vanity indicators from business indicators
- maintain audit-friendly milestone logs

---

## 8. Merchant Reporting Logic

Good reporting should tell merchants:

- what was delivered
- what was observed
- how strong the result confidence is
- how this creator compares to others
- whether the campaign appears worth repeating

Avoid dashboards that flood merchants with superficial stats.

---

## 9. Creator Reporting Logic

Creators should see:
- what was verified
- how their score changed
- what metric category improved
- what they need to unlock higher-tier work

This converts attribution into progression logic.

---

## 10. Final Standard

Push attribution is strong when it:
- increases trust
- supports repeat buying decisions
- improves creator sorting
- resists manipulation
- stays honest about confidence limits

Attribution should make Push more credible than informal creator commerce, not more theatrical.
