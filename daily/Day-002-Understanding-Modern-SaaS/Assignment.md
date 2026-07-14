# Project Assignment - Day 002: Revenue Dashboard

This assignment involves creating a functional dashboard calculation script that processes a list of raw transaction logs and generates an executive revenue digest.

---

## 🎯 Requirements

Your script must parse a dataset of customer accounts and compute the following key business indicators:
1.  **MRR** & **ARR**
2.  **Churn Rate %** (Logo Churn)
3.  **Average CAC** & **LTV**
4.  **LTV : CAC Ratio**
5.  **CAC Payback Period** (in Months)

---

## 📂 File Input Schema (`customers.json`)
The dashboard processes a list of customer JSON entries:

```json
[
  {
    "id": 1,
    "name": "Alpha Corp",
    "mrr": 500.00,
    "cac": 1200.00,
    "status": "Active"
  },
  {
    "id": 2,
    "name": "Beta Corp",
    "mrr": 200.00,
    "cac": 800.00,
    "status": "Churned"
  }
]
```

---

## 💻 Deliverable Code

I have developed a complete execution script in the [Code/metrics_calculator.py](Code/metrics_calculator.py) file. It implements:
*   Structured Pydantic validation for input records.
*   Precise calculation logic handling edge cases (like zero-division if Churn is 0%).
*   A clean CLI table output summarizing business performance.