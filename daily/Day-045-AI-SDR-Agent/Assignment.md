# Project Assignment - Day 045: AI SDR Engine v2

This project requires developing a Python AI SDR v2 Engine. It qualifies leads based on intent scores, generates structured 4-touch outbound sequences (Email, LinkedIn, Follow-up, Break-up), schedules delivery offset dates, and synchronizes status logs to CRMs.

---

## 🎯 Requirements

Your SDR Engine must:
1.  **Lead Qualification Gate**:
    *   Examine input lead data and filter out records with fit scores below 70.
2.  **Multichannel 4-Touch Sequence**:
    *   Compile outreach copy for four sequential touchpoints:
        *   *Touch 1 (Day 1)*: Cold Email targeting technographic indicators.
        *   *Touch 2 (Day 4)*: LinkedIn Connection request text.
        *   *Touch 3 (Day 8)*: Case study and social proof email follow-up.
        *   *Touch 4 (Day 15)*: Break-up email template.
3.  **Dynamic Task Scheduling**:
    *   Calculate date strings for each touchpoint using offset datetime math starting from today's date.
4.  **CRM State Updates**:
    *   Simulate updating contact stages to `Outbound-In-Sequence` in CRM platforms (Salesforce/HubSpot).
    *   Simulate logging the scheduled tasks under the contact's timeline for sales rep visibility.
5.  **Audit Logs**:
    *   Display the complete scheduled campaign outline, subject lines, and body previews in the terminal.

---

## 💻 Deliverable Code

A complete, working AI SDR v2 script has been created and is available in [Code/ai_sdr_v2.py](Code/ai_sdr_v2.py). It processes mock qualified leads (Wayne Enterprises, Stark Industries), generates outbound sequences, schedules touchpoint offsets, and logs CRM transactions.