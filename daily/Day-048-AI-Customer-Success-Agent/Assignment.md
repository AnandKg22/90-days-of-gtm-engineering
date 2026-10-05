# Project Assignment - Day 048: Customer Success Assistant

This project requires developing a Python Customer Success Assistant. It acts as an automated account monitoring engine that tracks usage, alerts CSMs to churn risks, and drafts expansion pitches.

---

## 🎯 Requirements

Your CS Assistant must:
1.  **Monitor Account Health**:
    *   Accept metrics for customer companies: product adoption rate (0.0 to 1.0), open support tickets count, and onboarding status.
2.  **Calculate Customer Health Score (CHS)**:
    *   Formulate a 100-point score using weighted parameters: product adoption (60% weight), onboarding status (15% weight), and support ticket penalties (25% weight, deducting 5 points per ticket).
3.  **Execute Churn Risk Escalation Workflows**:
    *   If the CHS falls below 50.0 (Red Rating):
        *   Simulate triggering high-priority Slack notifications to the assigned CSM.
        *   Draft a personalized executive health review email template to coordinate a technical support call.
4.  **Detect Expansion Opportunities**:
    *   If the CHS is above 80.0 (Green Rating) and seat utilization is $\ge 90\%$:
        *   Draft a personalized upsell proposal email pitching account license expansions.
5.  **Audit Setup Progress**:
    *   Check for incomplete onboarding tasks and flag warnings to CSMs.

---

## 💻 Deliverable Code

A complete, working Customer Success Assistant has been created and is available in [Code/customer_success_assistant.py](Code/customer_success_assistant.py). It runs portfolio audits for Stark Industries, Wayne Enterprises, and Cyberdyne Systems.