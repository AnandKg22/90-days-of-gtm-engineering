# Exercises - Day 040: Phase 2 Capstone Extensions

This document details practical exercises designed to expand and test the capabilities of the **AI Revenue Automation Platform (ARAP) v1**.

---

## 📋 Exercise 1: Technology Stack Lead Scoring Heuristic

### Goal:
Modify the scoring algorithm to grant additional points if a company's technology stack matches your target integration list.

### Task:
Update the `score_lead()` function in `app.py` to:
1.  Scan the enriched `enrich_tech_stack` text field.
2.  If the tech stack contains "Salesforce", add **+10** points.
3.  If it contains "HubSpot", add **+10** points.
4.  If it contains "AWS" or "GCP", add **+5** points.

### Sample Code Implementation:
```python
# Insert inside score_lead() function in app.py:
def score_lead_extended(title, revenue, email, segment, tech_stack=""):
    score, factors = score_lead(title, revenue, email, segment)
    
    tech_lower = tech_stack.lower()
    if "salesforce" in tech_lower:
        score += 10
        factors.append("Tech stack contains Salesforce: +10")
    if "hubspot" in tech_lower:
        score += 10
        factors.append("Tech stack contains HubSpot: +10")
    if any(t in tech_lower for t in ["aws", "gcp"]):
        score += 5
        factors.append("Tech stack uses AWS/GCP: +5")
        
    return max(0, min(100, score)), factors
```

---

## ⚙️ Exercise 2: Ingestion Webhook Receiver

### Goal:
Build an API endpoint that acts as a webhook receiver to ingest leads from external sources like Typeform, Jotform, or Facebook Lead Ads.

### Task:
Write a new API route in `app.py` that listens on `POST /api/webhooks/intake`:
1.  Receive a JSON payload from an external form provider.
2.  Parse the custom fields (Typeform field mappings: e.g., `answers[0].text` mapping to `first_name`).
3.  Inject the lead into the database, triggering the enrichment, scoring, and AI copywriting pipelines automatically.

---

## 📊 Exercise 3: SQL Conversion Metrics Query

Write a SQL query to calculate the conversion rate of **Hot Leads (Score $\ge$ 70)** that have been successfully synced to the CRMs:

```sql
SELECT 
    COUNT(CASE WHEN score >= 70 THEN 1 END) AS total_hot_leads,
    COUNT(CASE WHEN score >= 70 AND crm_sync_status = 'Success' THEN 1 END) AS synced_hot_leads,
    ROUND(
        (COUNT(CASE WHEN score >= 70 AND crm_sync_status = 'Success' THEN 1 END)::numeric / 
         NULLIF(COUNT(CASE WHEN score >= 70 THEN 1 END), 0)) * 100, 
        2
    ) AS hot_lead_sync_conversion_rate_pct
FROM leads;
```