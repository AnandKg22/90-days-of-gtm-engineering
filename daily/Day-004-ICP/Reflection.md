# Reflection - Day 004: Ideal Customer Profile (ICP)

A personal log reflecting on the learning outcomes and concepts mastered on Day 4.

---

## 💡 Key Takeaways & Lessons Learned

1.  **ICP prevents Sales Burnout**: By programmatically filtering out leads that don't fit our ICP, sales reps do not waste time pitching to companies that cannot buy (out of territory, too small, or running incompatible tech).
2.  **Technographic Scraping is a Superpower**: Tracking a prospect's technologies (technographics) allows us to filter leads. For example, if a maritime college runs on Moodle, they are a perfect fit for our VivaExams integration. If they don't, we know we have custom engineering friction.
3.  **Tiered Routing Speed**: High Fit leads must be routed instantly (under 5 minutes) to close deals, while Low Fit leads should bypass the human sales queue entirely and be automated.

---

## 💻 Script Verification

I ran the `Code/icp_validator.py` script to test our lead scoring model.
*   **Result**: 
    *   `Tolani Maritime Academy`: Evaluated as **High Fit (90.0/100)**. (Matched target industry, perfect size, and matches Moodle technology).
    *   `IMSGOA Marine College`: Evaluated as **High Fit (90.0/100)**. (Matched target industry, near-target size, and matches Moodle & Stripe technology).
    *   `Global Shipping Corp`: Evaluated as **Medium Fit (55.0/100)**. (Size was too large for our target, and industry was shipping rather than academy, but matched location and Stripe technology).
    *   `Acme Software Inc`: Evaluated as **Low Fit (0.0/100)**. (No matching parameters).
*   **Insight**: This programmatic scoring ensures our sales team prioritizes high-yield institutional contracts.

---

## 🎯 Plan for Tomorrow
Tomorrow is Day 5: **Market Segmentation**. I will focus on dividing our addressable market (TAM, SAM, SOM) into targeted segments based on employee count, geography, and technological intent.
