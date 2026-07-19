# Reflection - Day 007: Sales Roles & Hand-offs

A personal log reflecting on the learning outcomes and concepts mastered on Day 7.

---

## 💡 Key Takeaways & Lessons Learned

1.  **Hand-offs are the Leakiest Part of the Funnel**: When a customer transitions from sales (AE) to post-sales onboarding (CSM), they often repeat their requirements. If the GTM Engineer builds integrations that automatically copy the AE qualification notes, meeting transcripts, and deal size directly into the CSM's dashboard, the customer's onboarding friction drops, reducing early churn.
2.  **Specialization maximizes throughput**: Dividing outbound prospecting (BDR), inbound qualification (SDR), deal closing (AE), and customer adoption (CS) allows each role to focus on their specific metrics (KPIs), increasing overall funnel speed.
3.  **Owner IDs must be synced**: In GTM database replicas, every contact and deal must maintain its active `owner_id`. If ownership transfers in HubSpot, our database should instantly sync that change via webhooks so notifications (such as Slack alerts) route to the correct team member.

---

## 💻 Script Verification

I ran the `Code/org_chart.py` script to test our sales hand-off tracking logic.
*   **Result**: 
    *   Lead starts under SDR ownership (`Rohit`).
    *   SDR qualifies: ownership transfers to AE (`Sarah`), stage moves to `Meeting Booked`, and Calendly alert triggers.
    *   AE closes deal: ownership transfers to CSM (`Amit`), stage moves to `Closed Won`, and Stripe invoice triggers seat provisioning.
    *   The audit trail correctly records timestamps and details for each transition.
*   **Insight**: This programmatic tracking is the template we will use to build automated n8n triggers in Phase 2.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 8: **CRM Fundamentals**. I will focus on understanding contacts, companies, deals, activities, custom property structures, and postgres CRM relational models.
