# Exercises - Day 007: Commercial Information Flow Map

This document maps out the B2B data hand-offs and information flow checkpoints across the sales org.

---

## 🔄 Org Data Hand-off Pipeline

Below is the step-by-step transaction workflow showing data transfers and system actions:

```
[Inbound Form] 
      │ (1. Lead Created)
      ▼
┌─────────────┐
│  SDR Team   │ ──(2. Qualifies Lead & Books Calendly Demo)──> [Calendly / Zoom]
└─────────────┘                                                      │
                                                           (3. Match AE Owner)
                                                                     ▼
                                                              ┌─────────────┐
                                                              │   AE Team   │
                                                              └──────┬──────┘
                                                                     │ (4. SOW / Stripe Paid)
                                                                     ▼
                                                              ┌─────────────┐
                                                              │   CS Team   │
                                                              └─────────────┘
```

---

### 1. Inbound to SDR Hand-off (Lead Intake)
*   **Trigger**: Prospect submits a demo request form on VivaExams.
*   **Data Transferred**: First Name, Email, Organization Name, Student Size.
*   **System Action**: HubSpot creates a Contact record. If student size > 100, the system sets status to `New Lead` and routes the record to the SDR team.

### 2. SDR to AE Hand-off (Meeting Booking)
*   **Trigger**: SDR calls the lead, qualifies their budget/need, and shares the AE's Calendly booking link.
*   **Data Transferred**:
    *   `sdr_notes`: "Client wants online mock proctoring for 500 cadets."
    *   `meeting_date`: "2026-07-16 14:00:00"
    *   `owner_id`: Set to AE's HubSpot ID.
*   **System Action**: Calendly API triggers n8n. n8n creates a Deal record in the Sales Pipeline, attaches the meeting invite, copies `sdr_notes` to the deal description, and sends a Slack briefing to the AE.

### 3. AE to CS Hand-off (Onboarding & Activation)
*   **Trigger**: AE closes the deal (HubSpot Deal stage moved to `Closed Won` after Stripe payment success).
*   **Data Transferred**:
    *   `deal_value`: $7,500
    *   `license_seats`: 500
    *   `onboarding_deadline`: Contract start date + 14 days.
    *   `customer_goals`: "Needs to deploy Class IV prep exams by next month."
*   **System Action**: n8n detects the stage change. It:
    1. Creates a record in the Customer Success Database.
    2. Assigns a Customer Success Manager (CSM) via round-robin.
    3. Fires a Slack alert to the CSM:
       > 🏆 **Deal Closed Won!** AMET University is now a customer. CSM Assigned: Amit. Target Onboarding: Aug 1.
    4. Triggers an automated customer email with login credentials and onboarding documentation.