# Exercises - Day 039: Funnel Analysis & Weighted Forecasting

This document details practical exercises on calculating weighted sales forecasts, building funnel visualizations, and evaluating GTM conversion efficiency.

---

## 📋 Exercise 1: Weighted Sales Forecasting Calculation

### Scenario:
A GTM team has five active deals in their pipeline. You need to calculate the **Weighted Sales Forecast** for the quarter to help finance budget marketing operations.

| Deal ID | Company Name | Deal Value (ARR) | CRM Stage | Close Probability |
| :--- | :--- | :--- | :--- | :--- |
| #101 | Cyberdyne Systems | $30,000 | Discovery | 10% |
| #102 | Tyrell Corp | $150,000 | Qualification | 25% |
| #103 | Stark Industries | $120,000 | Proposal | 50% |
| #104 | Wayne Enterprises | $85,000 | Negotiation | 80% |
| #105 | Oscorp Industries | $60,000 | Proposal | 50% |

### Calculation:
The weighted forecast is calculated by multiplying each deal value by its corresponding stage probability:

$$\text{Weighted Forecast} = \sum (\text{Value} \times \text{Probability})$$

*   **Deal #101**: $\$30,000 \times 0.10 = \$3,000$
*   **Deal #102**: $\$150,000 \times 0.25 = \$37,500$
*   **Deal #103**: $\$120,000 \times 0.50 = \$60,000$
*   **Deal #104**: $\$85,000 \times 0.80 = \$68,000$
*   **Deal #105**: $\$60,000 \times 0.50 = \$30,000$

$$\text{Total Weighted Forecast} = \$3,000 + \$37,500 + \$60,000 + \$68,000 + \$30,000 = \$198,500$$

*   **Total Unweighted Pipeline Value**: $\$345,000$
*   **Weighted Sales Forecast**: $\$198,500$ (indicates a more realistic target for cash flow modeling).

---

## ⚙️ Exercise 2: SQL Funnel Leakage Query

To detect where leads are dropping off (leaking) in the sales process, run this SQL statement. It calculates the drop-off percentage from each funnel stage to the next:

```sql
WITH stage_counts AS (
    SELECT 
        COUNT(CASE WHEN stage = 'Discovery' THEN 1 END) AS count_discovery,
        COUNT(CASE WHEN stage = 'Qualification' THEN 1 END) AS count_qualification,
        COUNT(CASE WHEN stage = 'Proposal' THEN 1 END) AS count_proposal,
        COUNT(CASE WHEN stage = 'Negotiation' THEN 1 END) AS count_negotiation,
        COUNT(CASE WHEN stage = 'Closed Won' THEN 1 END) AS count_won
    FROM fact_deals
)
SELECT 
    -- Stage volumes
    count_discovery,
    count_qualification,
    count_proposal,
    count_negotiation,
    count_won,
    -- Step-by-step conversion drop-offs
    ROUND((1 - (count_qualification::numeric / NULLIF(count_discovery, 0))) * 100, 2) AS discovery_leakage_pct,
    ROUND((1 - (count_proposal::numeric / NULLIF(count_qualification, 0))) * 100, 2) AS qualification_leakage_pct,
    ROUND((1 - (count_negotiation::numeric / NULLIF(count_proposal, 0))) * 100, 2) AS proposal_leakage_pct,
    ROUND((1 - (count_won::numeric / NULLIF(count_negotiation, 0))) * 100, 2) AS negotiation_leakage_pct
FROM stage_counts;
```

### Analysis of Leakage:
*   A high **qualification_leakage_pct** indicates poor lead quality or mismatched ICP.
*   A high **negotiation_leakage_pct** suggests pricing issues, blocker resistance, or competitor displacement.