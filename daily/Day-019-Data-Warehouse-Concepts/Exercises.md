# Exercises - Day 019: Data Warehouse Star Schema Design

This document details the Star Schema data warehouse architecture, featuring DDL schemas for Fact and Dimension tables.

---

## 📐 Data Warehouse Star Schema Design

To compile fast business intelligence dashboards, we design the following dimensional warehouse:

```
                  ┌───────────────┐
                  │  dim_dates    │
                  │ (Dimension)   │
                  └───────┬───────┘
                          │
                          ▼
┌──────────────────┐  ┌───┴──────────┐  ┌──────────────────┐
│  dim_companies   │◄─┤  fact_deals  ├─►│  dim_campaigns   │
│   (Dimension)    │  │    (Fact)    │  │   (Dimension)    │
└──────────────────┘  └──────────────┘  └──────────────────┘
```

---

## 🗄️ SQL DDL Table Schemas

### 1. Dimension: Dates (`dim_dates`)
```sql
CREATE TABLE dim_dates (
    date_key INT PRIMARY KEY, -- format: YYYYMMDD
    calendar_date DATE NOT NULL,
    calendar_year INT NOT NULL,
    calendar_quarter INT NOT NULL,
    month_name VARCHAR(20) NOT NULL
);
```

### 2. Dimension: Companies (`dim_companies`)
```sql
CREATE TABLE dim_companies (
    company_key INT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    industry VARCHAR(100) NOT NULL,
    employee_count_tier VARCHAR(50) NOT NULL -- e.g. "SME (1-50)", "Mid-Market (51-200)", "Enterprise (201+)"
);
```

### 3. Fact: Deals (`fact_deals`)
```sql
CREATE TABLE fact_deals (
    deal_key INT PRIMARY KEY,
    company_key INT NOT NULL REFERENCES dim_companies(company_key),
    date_key INT NOT NULL REFERENCES dim_dates(date_key),
    amount_usd NUMERIC(15, 2) NOT NULL DEFAULT 0.00,
    license_seats INT NOT NULL DEFAULT 0
);
```

---

## 📊 Analytical Aggregate Query

Calculates the total revenue closed grouped by company scale and calendar quarter:
```sql
SELECT 
    c.employee_count_tier,
    d.calendar_year,
    d.calendar_quarter,
    SUM(f.amount_usd) AS total_revenue_usd,
    SUM(f.license_seats) AS total_seats_sold
FROM fact_deals f
JOIN dim_companies c ON f.company_key = c.company_key
JOIN dim_dates d ON f.date_key = d.date_key
GROUP BY c.employee_count_tier, d.calendar_year, d.calendar_quarter
ORDER BY total_revenue_usd DESC;
```
