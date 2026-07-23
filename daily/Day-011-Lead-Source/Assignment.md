# Project Assignment - Day 011: Lead Attribution Engine

This project requires developing a Python marketing analytics script that tracks lead touchpoints, sanitizes UTM fields, and implements First-Touch and Last-Touch attribution models.

---

## 🎯 Requirements

Your Python simulation must:
1.  Define a user touchpoint object containing: `timestamp`, `utm_source`, `utm_medium`, and `utm_campaign`.
2.  Model a customer journey as a chronological list of touchpoint records ending in a `purchase` event.
3.  Implement two attribution algorithms:
    *   **First-Touch Attribution**: Identifies the very first marketing channel that introduced the user to the website.
    *   **Last-Touch Attribution**: Identifies the marketing channel associated with the final touchpoint before the checkout purchase.
4.  Print an executive attribution summary showing which campaigns receive revenue credit.

---

## 💻 Deliverable Code

A complete, working simulation script has been created and placed in [Code/lead_attribution.py](Code/lead_attribution.py). It models the touchpoint histories, computes both attribution scores, and outputs a formatted breakdown.
