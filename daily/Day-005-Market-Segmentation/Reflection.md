# Reflection - Day 005: Market Segmentation & Positioning

A personal log reflecting on the learning outcomes and concepts mastered on Day 5.

---

## 💡 Key Takeaways & Lessons Learned

1.  **TAM keeps you ambitious, SOM keeps you focused**: Calculating the TAM ($45M) proves the long-term venture scale of VivaExams, but targeting the SOM ($400k) ensures our sales reps don't get distracted by leads they cannot close or support in the near-term.
2.  **Technographic filtering is key to SOM definition**: By filtering the Indian SAM down to institutions using Moodle or Blackboard in the West/South regions, we isolate high-probability target accounts. This lowers CAC because our integration is plug-and-play.
3.  **Local Regulations dictate SAM boundaries**: In maritime software, you cannot sell standard software without adhering to localized DGS rules. Hence, DGS-approval status is a binary qualifying filter.

---

## 💻 Script Verification

I ran the `Code/segmentation_engine.py` script to test our market segmentation model.
*   **Result**: Out of 10 mock global maritime training centers:
    *   **TAM**: 10 accounts, valued at $80,000.
    *   **SAM**: 7 accounts (DGS-approved academies in India), valued at $56,000.
    *   **SOM**: 4 accounts (DGS-approved academies in West/South India running Moodle/Blackboard), valued at $32,000.
*   **Insight**: This programmatic division allows our GTM campaigns to run highly personalized outreach specific to each target segment (e.g. sending different emails to Tier 1 academies vs. Tier 3 modular safety centers).

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 6: **B2B Sales Fundamentals**. I will focus on modeling deal pipelines, forecasting probability weights, and building a Kanban sales stage tracking tool.
