# Study Notes - Day 045: AI SDR Agents (Outbound Campaigns)

Today's studies focused on Sales Development Representative (SDR) automation, lead qualification thresholds, designing multichannel outbound sequences, task scheduling algorithms, and updating lead stages in the CRM.

---

## 1. Lead Qualification Gates

Before triggering outbound resources, leads must pass a **Qualification check gate**. This protects email sender reputation (deliverability) and prevents spamming low-value prospects.

### Qualification Criteria:
*   **Threshold Fit Score**: Leads must have a score $\ge 70$ (derived from matching ICP segments and director/C-level titles).
*   **Domain Validity**: Exclude generic email domains (Gmail/Yahoo) to focus strictly on corporate accounts.
*   **Stale Lead Filter**: Filter out leads already in an active sales sequence or marked as customers.

---

## 2. The 4-Touch Outbound Sequence Framework

Outbound campaigns utilize structured sequences combining channels (Email, LinkedIn) and messaging styles:

```
[Day 1: Cold Email (Pain)] ──> [Day 4: LinkedIn Connect] ──> [Day 8: Follow-up (ROI)] ──> [Day 15: Break-up (Soft Close)]
```

### 1. Touch 1 (Day 1 - Cold Email)
*   *Messaging*: Focuses heavily on a single, verified pain point (e.g., manual data reconciliation) and references their technographics.
*   *Call-to-Action (CTA)*: Request a low-friction 10-minute sync.

### 2. Touch 2 (Day 4 - LinkedIn Connection)
*   *Messaging*: Conversational connector. Acknowledges their company's growth, keeping sales pitches out of the connection invite.

### 3. Touch 3 (Day 8 - Value Follow-up Email)
*   *Messaging*: Social proof and ROI metrics. Case studies demonstrating how a similar customer solved the same pain point.

### 4. Touch 4 (Day 15 - Break-up Email)
*   *Messaging*: Permission to close their file. Acknowledges timing might be off, leaving the door open for future contact. Often yields high response rates due to reverse psychology.

---

## 3. Dynamic Task Scheduling Math

To schedule sequence touchpoints, the GTM platform calculates date offsets from the ingestion timestamp (`base_date`):

$$\text{Scheduled Date}_n = \text{Base Date} + \text{timedelta}(\text{days}=k)$$

In Python, this is executed using the `datetime` module:
```python
from datetime import datetime, timedelta
base = datetime.now()
touch3_date = base + timedelta(days=7) # Schedules Touch 3 for exactly one week from today
```

---

## 4. CRM Stage State Transitions

When a lead enters a sequence, the GTM platform updates the CRM objects to maintain pipeline visibility for sales managers:

```
[Lead Status: Qualified] ──> [Outbound-In-Sequence] ──> [Attempting Contact] ──> [Connected / Meeting Booked]
```

*   **Status Update**: Transition `leads.status` (and matching HubSpot contact properties) to `Outbound-In-Sequence`.
*   **Task Logging**: Insert the 4 scheduled touchpoint tasks into the CRM's activity timeline, allowing reps to see exactly when the next touch is scheduled.
*   **Sequence Pause**: If a recipient replies to any touchpoint, a webhook triggers the orchestrator to instantly change their status to `Contacted` and cancel all remaining scheduled tasks.
