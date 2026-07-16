# Project Assignment - Day 004: ICP Lead Validator

This project requires developing a programmatic lead qualifier that scores incoming prospects against our B2B Ideal Customer Profile.

---

## 🎯 Requirements

Your Python validation engine must:
1.  Define an ICP template with target values for:
    *   `target_industries`
    *   `min_employees` / `max_employees`
    *   `target_countries`
    *   `target_technologies`
2.  Score incoming customer profiles on a 100-point scale based on the following weights:
    *   **Industry Match**: 35 points max
    *   **Employee Count Fit**: 25 points max
    *   **Technographics Match**: 20 points max
    *   **Geography Fit**: 20 points max
3.  Assign prospects to a Lead Fit Tier:
    *   `High Fit`: Score >= 75
    *   `Medium Fit`: 40 <= Score < 75
    *   `Low Fit`: Score < 40

---

## 💻 Deliverable Code

A complete, working validation engine has been created and placed in [Code/icp_validator.py](Code/icp_validator.py). It models these scoring criteria and evaluates several mock companies, printing a clean validation log.
