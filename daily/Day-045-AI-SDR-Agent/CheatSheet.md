# Cheat Sheet - AI SDR Agents

This cheat sheet compiles sequencing frameworks, copywriting principles, and date scheduling methods for GTM outbound campaigns.

---

## 1. Outbound Copywriting Principles

*   **Subject Lines**: Keep under 6 words. Use lower-case, conversational text (e.g. `reconciliation audit for wayne corp` rather than `CRITICAL: AUTOMATE YOUR SALES FORECASTING`).
*   **The Hook**: Reference their title and specific technographics within the first two sentences.
*   **Length**: Keep the entire email body under 120 words. Long emails do not get read on mobile devices.
*   **Low-Friction CTA**: Avoid asking for "a demo" or "30 minutes". Instead, ask: "Are you open to a brief 10-minute sync next Tuesday?" or "Is this a priority right now?"

---

## 2. Python Datetime Scheduling Code

```python
from datetime import datetime, timedelta

def get_scheduled_sequence_dates(days_offsets: List[int]) -> List[str]:
    base_time = datetime.now()
    schedule_dates = []
    
    for offset in days_offsets:
        touch_date = base_time + timedelta(days=offset)
        schedule_dates.append(touch_date.strftime("%Y-%m-%d"))
        
    return schedule_dates

# Example offsets for a 4-touch campaign: Day 0, Day 3, Day 7, Day 14
dates = get_scheduled_sequence_dates([0, 3, 7, 14])
# Output: ['2026-07-13', '2026-07-16', '2026-07-20', '2026-07-27']
```

---

## 3. Email Deliverability Checklist

Before launching automated outbound SDR sequences, verify your infrastructure:
*   **SPF (Sender Policy Framework)**: Authorizes specific mail servers to send emails on behalf of your domain.
*   **DKIM (DomainKeys Identified Mail)**: Adds a digital signature to emails, verifying the message wasn't altered in transit.
*   **DMARC (Domain-based Message Authentication, Reporting, and Conformance)**: Instructs receiving servers on how to handle emails that fail SPF/DKIM checks (set to `p=quarantine` or `p=reject`).
*   **Domain Warming**: Start new mailboxes at 5 emails/day, increasing slowly to a maximum of 30-40 outbound emails/day.
*   **Secondary Domains**: Never run cold outbound campaigns on your primary corporate domain. Use secondary domains (e.g., `getcompany.com` instead of `company.com`).
