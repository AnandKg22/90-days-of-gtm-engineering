# Exercises - Day 013: PostgreSQL Schema Design

This document contains the PostgreSQL database DDL schemas and analytical SQL queries designed for our GTM data warehouse replica.

---

## 🗄️ PostgreSQL Database DDL Schema

Below is the DDL code to build the relational tables, constraints, and optimization indexes:

```sql
-- 1. Leads Table (Acquisition tracking)
CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    utm_source VARCHAR(100) DEFAULT 'direct',
    utm_medium VARCHAR(100) DEFAULT 'none',
    utm_campaign VARCHAR(100) DEFAULT 'none',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Deals Table (Sales tracking)
CREATE TABLE deals (
    id SERIAL PRIMARY KEY,
    lead_id INT NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    amount NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    stage VARCHAR(100) NOT NULL DEFAULT 'Discovery',
    closed_at TIMESTAMP
);

-- 3. Optimization Indexes (Speeding up queries on large datasets)
CREATE INDEX idx_leads_email ON leads(email);
CREATE INDEX idx_leads_utm_source ON leads(utm_source);
CREATE INDEX idx_deals_lead_id ON deals(lead_id);
```

---

## 📊 Analytical SQL Queries

### 1. Revenue Closed per Lead Source
Aggregates won contract values grouped by traffic source:
```sql
SELECT 
    l.utm_source,
    COUNT(d.id) AS deals_won_count,
    SUM(d.amount) AS total_revenue_usd
FROM deals d
JOIN leads l ON d.lead_id = l.id
WHERE d.stage = 'Won'
GROUP BY l.utm_source
ORDER BY total_revenue_usd DESC;
```

### 2. Funnel Conversion Rate (Leads to Won Deals)
Calculates the percentage of registered leads who converted to paying customers:
```sql
SELECT 
    COUNT(DISTINCT l.id) AS total_leads,
    COUNT(DISTINCT d.id) FILTER (WHERE d.stage = 'Won') AS won_deals,
    (COUNT(DISTINCT d.id) FILTER (WHERE d.stage = 'Won')::FLOAT / COUNT(DISTINCT l.id) * 100) AS conversion_rate_percent
FROM leads l
LEFT JOIN deals d ON d.lead_id = l.id;
```
