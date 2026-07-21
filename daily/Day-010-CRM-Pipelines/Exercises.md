# Exercises - Day 010: Multi-Currency Pipeline Design

This document contains the multi-currency configuration specifications and calculations designed for international sales.

---

## 💱 Multi-currency Conversion Model

To support international deals, the billing and CRM schemas normalize all currencies to a corporate base currency (USD):

### 1. Exchange Rate Reference Table
These multipliers are fetched daily from exchange rate APIs and stored in the database:

| Local Currency | Code | USD Exchange Rate Multiplier |
| :--- | :--- | :--- |
| **US Dollar** (Base) | `USD` | `1.0000` |
| **Indian Rupee** | `INR` | `0.0120` |
| **Singapore Dollar** | `SGD` | `0.7400` |

---

## 🔮 Sample Conversion Math

When international deals are logged, the pipeline aggregates their values using active rates:

### 1. Tolani Maritime Academy (India)
*   *Local Contract Value*: `INR 830,000`
*   *USD Normalized Value*:
    $$INR \; 830,000 \times 0.0120 = \$9,960.00 \; USD$$

### 2. Singapore Maritime Academy (Singapore)
*   *Local Contract Value*: `SGD 13,500`
*   *USD Normalized Value*:
    $$SGD \; 13,500 \times 0.7400 = \$9,990.00 \; USD$$

### 3. US Merchant Marine Academy (USA)
*   *Local Contract Value*: `USD 10,000`
*   *USD Normalized Value*:
    $$USD \; 10,000 \times 1.0000 = \$10,000.00 \; USD$$

---

## ⚙️ SQL Database Conversion View
We build a database VIEW that automatically joins active deals to the currency rates table, presenting normalized values for pipeline reports:

```sql
CREATE VIEW normalized_deals AS
SELECT 
    d.id,
    d.name,
    d.local_amount,
    d.currency_code,
    (d.local_amount * r.usd_rate) AS amount_usd,
    d.stage
FROM deals d
JOIN currency_rates r ON d.currency_code = r.code;
```
