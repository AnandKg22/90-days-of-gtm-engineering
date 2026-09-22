# Exercises - Day 045: Outbound Sequencing & Scheduling

This document details practical exercises on writing outbound sequence scripts, calculating delivery date offsets, and handling reply alerts.

---

## 📋 Exercise 1: Sequence Touchpoint Copywriting Task

### Goal:
Write the complete text copy for **Touch 3 (Value Follow-up)** targeting a VP of Finance at a mid-market SaaS company.

*   *Target Pain Point*: High transaction fees and manual invoice reconciliations.
*   *Social Proof*: Reference helping a similar company (e.g. Acme Corp) save 2.2% on fees and 8 hours of work weekly.
*   *Call-to-Action*: 10-minute slot request.

### Resulting Template:
```text
Subject: Invoice reconciliation cost analysis for [Company]

Hi [First Name],

I wanted to follow up on my previous note. Many finance teams we work with are spending 10+ hours a week manually matching bank logs to billing records, while paying flat 3.0% transaction fees.

We helped the team at Acme Corp automate their reconciliation flows, cutting processing timelines from 3 days to under 5 minutes while reducing payment fees by 20%.

Are you open to a brief 10-minute review next Thursday at 2 PM to see if we can do the same for [Company]?

Best regards,
Sales Development Team
```

---

## ⚙️ Exercise 2: Outbound Reply Detection & Cancellation Loop

When a prospect replies to an email, the GTM platform must immediately cancel all remaining scheduled touchpoints in that sequence to prevent sending automated emails to an active lead.

### Task:
Draft the Python webhook handler logic that intercepts incoming reply notifications and updates task statuses to `Cancelled`:

```python
# Inbound reply handler in GTM orchestrator
def handle_email_reply_webhook(payload: dict, database: list):
    sender_email = payload.get("from_email")
    reply_timestamp = payload.get("received_at")
    
    print(f"[*] Reply received from {sender_email} at {reply_timestamp}.")
    
    # 1. Locate Lead record in database
    for lead in database:
        if lead["email"] == sender_email:
            lead_id = lead["lead_id"]
            
            # 2. Transition lead stage in CRM
            lead["status"] = "Contacted-Replied"
            print(f"  [CRM] Lead ID {lead_id} stage set to 'Replied'.")
            
            # 3. Cancel all downstream scheduled outreach tasks
            cancelled_count = 0
            for task in lead.get("outbound_sequence", []):
                if task["status"] == "Scheduled":
                    task["status"] = "Cancelled"
                    cancelled_count += 1
                    
            print(f"  [LOG] Successfully cancelled {cancelled_count} downstream scheduled tasks.")
            break
```