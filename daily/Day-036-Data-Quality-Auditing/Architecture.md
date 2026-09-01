# GTM Architecture - Day 036: Data Quality & Auditing

This document details the GTM database pipeline mapping dirty CRM leads through validation checks and duplicates filters.

---

## 🔄 Data Auditing and Quarantine Pipeline

The diagram below details the pipeline, showing how dirty records are checked and split:

```mermaid
graph TD
    Raw[(CRM Lead Input Stream)] -->|1. Ingest| DupCheck{Duplicate Email?}
    
    DupCheck -->|Yes: Compare timestamps| DupOlder[older timestamp]
    DupCheck -->|No: Pass to validations| Validations{Check Constraint Audits}
    
    DupOlder -->|2. Route to quarantine| Quarantine[(Quarantine Log JSON)]
    
    subgraph Constraint Audits
        Validations -->|Malformed email| Quarantine
        Validations -->|Negative deal amount| Quarantine
        Validations -->|Null company name| Quarantine
        Validations -->|All rules pass| CleanDB[(Clean CRM Tables)]
    end
    
    CleanDB -->|3. Load clean sets| Looker[Looker Quality Scorecard]
```

---

## ⚙️ SQL Data Quality Audit View

To isolate bad records dynamically inside BigQuery, GTM Engineers query this quarantine view:

```sql
CREATE VIEW v_quarantine_records AS
SELECT 
    lead_id,
    email,
    company_name,
    deal_amount,
    timestamp,
    ARRAY_TO_STRING([
        CASE WHEN email NOT LIKE '%@%._%' THEN 'Malformed Email' END,
        CASE WHEN deal_amount < 0.0 THEN 'Negative Deal Amount' END,
        CASE WHEN company_name IS NULL OR company_name = '' THEN 'Missing Company Name' END
    ], ' | ') AS quarantine_reasons
FROM raw_crm_leads
WHERE email NOT LIKE '%@%._%'
   OR deal_amount < 0.0
   OR company_name IS NULL 
   OR company_name = '';
```
