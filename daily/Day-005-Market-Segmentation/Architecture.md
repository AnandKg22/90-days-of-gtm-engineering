# GTM Architecture - Day 005: Market Segmentation Pipeline

This document details the data pipeline architecture that automates market segmentation and TAM/SAM/SOM classification inside our database.

---

## 🔄 Market Segmentation Data Flow

The diagram below details how raw prospect records are classified, valued, and visualized:

```mermaid
graph TD
    List[Raw Prospect CSV / API Lists] -->|1. Bulk Upload| Engine[Segmentation Engine Service]
    
    subgraph Classification Stage
        Engine -->|2. Check Location/DGS| SAM_Check{Is India & DGS Approved?}
        SAM_Check -->|No| TAM[(TAM Segment)]
        SAM_Check -->|Yes| SOM_Check{Uses Moodle & In South/West?}
        
        SOM_Check -->|No| SAM[(SAM Segment)]
        SOM_Check -->|Yes| SOM[(SOM Segment)]
    end
    
    subgraph Revenue Dashboard
        TAM -->|3. Query Metrics| Dashboard[Analytics Dashboard]
        SAM -->|3. Query Metrics| Dashboard
        SOM -->|3. Query Metrics| Dashboard
    end
```

---

## ⚙️ SQL Segmentation Rules

To run these segments directly in the PostgreSQL database replica, the dashboard queries use conditional SQL grouping:

```sql
-- Compute TAM/SAM/SOM segment counts and contract values
SELECT 
    COUNT(id) AS tam_count,
    SUM(8000) AS tam_value,
    
    COUNT(id) FILTER(WHERE country = 'IN' AND dgs_approved = true) AS sam_count,
    SUM(8000) FILTER(WHERE country = 'IN' AND dgs_approved = true) AS sam_value,
    
    COUNT(id) FILTER(WHERE country = 'IN' AND dgs_approved = true 
                       AND region IN ('West', 'South') 
                       AND 'Moodle' = ANY(tech_stack)) AS som_count,
    SUM(8000) FILTER(WHERE country = 'IN' AND dgs_approved = true 
                       AND region IN ('West', 'South') 
                       AND 'Moodle' = ANY(tech_stack)) AS som_value
FROM academy_prospects;
```
