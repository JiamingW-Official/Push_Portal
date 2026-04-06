> **Document ID:** 02 | **Version:** 1.1 | **Last Updated:** 2026-04-05 | **Status:** Active
> **Authoritative For:** Workflow stages, milestone states, merchant/creator/ops workflows, workflow failure mitigations
> **See Also:** [Doc 01] for strategy guiding workflow | [Doc 04] for workflow failure mitigations | [Doc 07] for attribution in workflow | [Doc 08] for fraud controls in workflow

# PUSH — 20x Workflow Architecture Skill

## Purpose
This document redesigns the Push workflow from a basic marketplace flow into a high-leverage operating system for merchants, creators, and platform ops.

The goal is not to add more steps.
The goal is to remove ambiguity, reduce operational waste, and create compounding platform value.

---

## 1. Workflow Design Principles

A 20x workflow must be:
- fast to understand
- hard to misuse
- easy to repeat
- measurable at every stage
- resilient against drop-off and fraud
- capable of producing better data over time

The workflow should not feel like a manual project-management pipeline.  
It should feel like a controlled economic system.

---

## 2. Merchant Workflow (Optimized)

### Stage 1: Merchant Onboarding
Merchant provides:
- business name
- location
- category
- contact
- business hours
- fulfillment capacity
- payment setup

#### Optimization
Use onboarding to build merchant campaign readiness.

Capture:
- preferred demand windows
- average order value
- high-margin products
- capacity constraints
- repeat customer goal
- preferred creator categories

This turns onboarding into operational intelligence.

---

### Stage 2: Goal Selection
Merchant chooses a business objective, such as:
- drive new visits
- increase weekday traffic
- launch a new item
- improve early attendance at an event
- fill underperforming time slots
- generate local awareness with redemption

#### Optimization
Do not force the merchant to create campaigns from scratch.
Translate goals into structured campaign templates.

Example templates:
- Trial Offer Campaign
- Off-Peak Fill Campaign
- Soft Launch Campaign
- New Product Sampling Campaign
- Event Attendance Boost Campaign

---

### Stage 3: Campaign Structuring
Merchant defines:
- offer
- payout type
- slots
- date range
- creator requirements
- verification method
- approval rules
- standby enabled or not

#### Optimization
Pre-suggest defaults based on merchant type and objective.
This reduces weak campaign design and improves consistency.

---

### Stage 4: Candidate Routing
Creators are surfaced through:
- active application
- algorithmic matching
- standby pool
- category fit
- geographic proximity
- credit score compatibility

#### Optimization
Present ranked candidates with rationale:
- strongest fulfillment history
- best local fit
- best category match
- best redemption efficiency
- best reliability

**Attribution Detail:** → See [Doc 07] for the authoritative treatment of how creator attribution signals feed into ranking and candidate presentation.

---

### Stage 5: Campaign Execution
Once approved:
- creator receives clear deliverables
- schedule and constraints are locked
- merchant sees upcoming activity timeline
- proof requirements are explicit

#### Optimization
Avoid chat-based ambiguity.
Use milestone states:

1. Accepted
2. Scheduled
3. Visited
4. Proof Submitted
5. Content Published
6. Verified
7. Settled

---

### Stage 6: Review and Repeat
Merchant receives:
- creator-level result summary
- campaign-level summary
- repeat recommendation
- suggested next campaign type
- standby fill insights
- underused time-slot suggestions

#### Optimization
Always turn campaign completion into the seed of the next campaign.

---

## 3. Creator Workflow (Optimized)

### Stage 1: Creator Onboarding
Capture:
- platform handles
- content categories
- geography
- availability
- transport radius
- preferred campaign types
- schedule constraints

#### Optimization
Ask for operational fit, not just identity.

---

### Stage 2: Opportunity Discovery
Creators discover work through:
- live map
- ranked campaign feed
- standby alerts
- preferred category queue
- tier-qualified opportunity pool

#### Optimization
The feed should answer:
- What can I do now?
- What pays best near me?
- What closes soon?
- What am I one tier away from unlocking?

---

### Stage 3: Application or Standby
Creators can:
- apply normally
- enter standby
- bookmark
- compare eligibility gaps

#### Optimization
Standby must feel strategic, not random.

---

### Stage 4: Fulfillment
Creators perform:
- visit
- capture proof
- follow content requirements
- publish
- submit evidence

#### Optimization
Use:
- checklist format
- deadline visibility
- proof examples
- disqualification rules
- auto-reminders

---

### Stage 5: Settlement and Progression
After completion:
- payout is initiated
- creator score updates
- tier progress updates
- future campaign unlocks may change

#### Optimization
Completion must feel like progression, not just closure.

---

## 4. Platform Ops Workflow (Optimized)

Platform ops should monitor:
- fill rate
- standby conversion
- no-show rates
- merchant repeat rate
- creator repeat rate
- dispute density
- fraud anomalies
- campaign time-to-fill
- campaign time-to-verify

#### Optimization
Create an operations dashboard with exception flags:
- overdue proof
- suspicious redemption spike
- repeat merchant dissatisfaction
- creator reliability drop
- region with weak supply density

---

## 5. 20x Workflow Improvements vs Basic Marketplace Flow

### Traditional Basic Flow
Merchant posts → Creator applies → Merchant accepts → Content happens → Payment maybe

### 20x Push Flow
Merchant goal → Structured campaign → Ranked creator routing → Verified milestones → Settlement → Data feedback loop → Repeat optimization

This improved flow produces:
- clearer merchant outcomes
- more predictable creator expectations
- stronger scoring data
- more repeatable campaigns
- lower operational chaos

---

## 6. Workflow Failure Points

Common weak points:
- vague merchant instructions
- creator ghosting
- proof confusion
- merchant approval delays
- weak fraud controls
- low standby response
- payout delays
- incomplete post-campaign data

Each failure point must have a mitigation path built into workflow design.

---

## 7. Workflow SLA Framework

Every workflow stage has an expected duration. When these SLAs are exceeded, the system should flag, nudge, or auto-escalate.

### Merchant-Side SLAs

| Stage | SLA | If Exceeded |
|-------|-----|-------------|
| Campaign setup (draft → published) | 48 hours | Reminder email; offer setup assistance |
| Creator application review | 24 hours | Auto-approve top-scored applicants; notify merchant |
| Proof/completion confirmation | 24 hours | Auto-approve if proof meets standard criteria |
| Post-campaign feedback submission | 48 hours | Reminder; feedback defaults to "satisfactory" if unsubmitted |

### Creator-Side SLAs

| Stage | SLA | If Exceeded |
|-------|-----|-------------|
| Campaign acceptance after match | 12 hours | Slot opens to next candidate or standby pool |
| Visit completion after acceptance | Per campaign deadline (typically 3-5 days) | Warning at 50% elapsed; auto-cancel at deadline + 24h |
| Proof submission after visit | 24 hours | Reminder; score impact warning |
| Content publication after proof approval | 48 hours | Final reminder; non-completion recorded |

### Platform Ops SLAs

| Stage | SLA | If Exceeded |
|-------|-----|-------------|
| Dispute acknowledgment | 4 hours (business hours) | Auto-escalation to priority queue |
| Dispute resolution | 48 hours | Escalate to senior review; notify both parties of delay |
| Creator payout after verification | 24 hours | Auto-process if no fraud flags; creator notification |
| Fraud flag review | 24 hours | Settlement held; both parties notified |

### SLA Enforcement Principles
- SLAs are not punitive — they are clarity tools that set expectations for all parties
- Auto-actions (auto-approve, auto-cancel) should only trigger for clear-cut cases
- Every SLA breach should be logged for operational health tracking
- SLA metrics feed into the Ops Dashboard → See [Doc 10] for tracking

---

## 8. Final Workflow Standard

A Push workflow is strong when it:
- reduces ambiguity
- generates trust
- creates reusable data
- shortens time-to-value
- increases repeat usage for both sides

The workflow itself is part of the moat.
