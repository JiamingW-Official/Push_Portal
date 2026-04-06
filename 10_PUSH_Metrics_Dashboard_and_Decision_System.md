> **Document ID:** 10 | **Version:** 1.1 | **Last Updated:** 2026-04-05 | **Status:** Active
> **Authoritative For:** All metrics definitions, dashboard structure, decision rules, metric traps
> **See Also:** [Doc 06] for economic metrics context; [Doc 07] for attribution metrics context; [Doc 08] for integrity metrics context; [Doc 09] for GTM metrics context

# PUSH — Metrics Dashboard and Decision System Skill

## Central Reference Note
This document serves as the central metrics reference for the PUSH framework. Other PUSH documents ([01] through [09]) define the strategic and operational contexts; this document defines how to measure progress against those contexts.

## Purpose
This document defines which metrics matter, how they should be interpreted, and how Push should avoid making bad decisions from noisy or shallow data.

Metrics are only useful if they shape better strategic and product decisions.

---

## 1. Metric Philosophy

Push should not optimize for surface growth.
It should optimize for:
- trust
- repeatability
- creator quality
- merchant quality
- clean transactions
- defensible data accumulation

Metrics must help answer:
- Is the marketplace healthy?
- Is the workflow working?
- Is the retention real?
- Is the wedge correct?
- Is the platform becoming stronger over time?

---

## 2. North Star Candidate

A strong North Star candidate is:

**Verified repeat campaign value generated per active merchant cohort**

Why this works:
- it ties value to merchants
- it requires campaign completion quality
- it emphasizes repeat behavior
- it discourages vanity metrics

---

## 3. Merchant Metrics

### Activation Metrics
- merchant onboarding completion
- first campaign launch rate
- time-to-first-campaign
- campaign setup abandonment rate

### Quality Metrics
- merchant approval turnaround time
- merchant dispute rate
- merchant satisfaction
- campaign report open rate

### Retention Metrics
- merchant second-campaign rate
- 30-day merchant repeat rate
- 60-day merchant repeat rate
- average campaigns per active merchant

These tell whether Push is becoming a true merchant operating layer.

---

## 4. Creator Metrics

### Activation Metrics
- creator onboarding completion
- time-to-first-application
- time-to-first-approved campaign
- time-to-first-completion

### Quality Metrics
- completion rate
- proof rejection rate
- merchant rating
- reliability trend
- dispute rate

### Retention Metrics
- creator second-campaign rate
- 30-day active creator repeat rate
- tier progression rate
- premium retention if applicable

These help distinguish true creator quality from shallow signups.

---

## 5. Campaign Metrics

- time-to-fill
- fill rate
- standby usage rate
- completion rate
- verification completion rate
- payout completion rate
- dispute density
- average campaign manual-intervention load

Campaign health is one of the clearest indicators of system quality.

---

## 6. Marketplace Liquidity Metrics

- application-to-approval ratio
- slot fill speed
- qualified creator density per campaign
- standby response speed
- creator opportunity coverage by zone
- merchant fill reliability by neighborhood

Liquidity is essential because Push depends on local density and time-sensitive fulfillment.

---

## 7. Integrity Metrics

- fraud flag rate
- false-positive review rate
- suspicious redemption rate
- suspicious creator pairings
- suspicious merchant pairings
- settlement hold rate
- repeat dispute actor concentration

These metrics protect trust and defensibility.

---

## 8. Economic Metrics

- subscription revenue by merchant cohort
- campaign fee revenue
- take-rate revenue
- support cost per completed campaign
- contribution margin per campaign cohort
- average revenue per retained merchant
- creator premium conversion rate
- creator premium retention rate

These determine whether the business becomes robust or merely busy.

---

## 9. Decision Rules

Metrics should trigger decisions.

### Example Rule 1
If merchant repeat is low but campaign fill is high:
- the problem is likely campaign outcome quality, not supply quantity.

### Example Rule 2
If creator signups are high but completion is low:
- supply quality is weak, not top-of-funnel volume.

### Example Rule 3
If standby usage is high but fulfillment quality drops:
- urgency is working, but screening is weak.

### Example Rule 4
If support load rises faster than completed campaigns:
- the workflow is not scaling cleanly.

---

## 10. Dashboard Structure

Push should maintain dashboards for:

### Executive Dashboard
- retention
- repeat rates
- campaign quality
- net revenue quality
- integrity health

### Product Dashboard
- workflow friction
- activation
- milestone drop-off
- standby behavior
- campaign completion states

### Ops Dashboard
- exceptions
- disputes
- payout delays
- fraud triggers
- merchant approval bottlenecks

### GTM Dashboard
- merchant pipeline
- creator supply quality
- vertical comparisons
- neighborhood density quality

---

## 11. Metrics Traps to Avoid

### Trap A: Celebrating Signups
Signups without completion or repeat are weak.

### Trap B: Overvaluing Views
Views are not the core business outcome.

### Trap C: Ignoring Support Cost
A campaign that works only with heavy manual intervention is not healthy.

### Trap D: Mistaking Repeat for Quality
Repeat behavior matters only if the economics remain healthy and trust remains high.

---

## 12. Final Standard

A strong Push metric system should:
- clarify where the system is getting stronger
- expose false progress quickly
- distinguish volume from quality
- help the team make sharper, not noisier, decisions

Good dashboards do not just describe the company.  
They discipline it.
