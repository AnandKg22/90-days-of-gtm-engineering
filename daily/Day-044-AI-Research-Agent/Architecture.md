# GTM Architecture - Day 044: AI Research Agent

This document details the data extraction pipeline, citation mapping database, and confidence scoring algorithms supporting company research.

---

## 🔄 Research Agent Data Pipeline

The diagram below details the pipeline, showing how raw HTML pages are parsed to compile a structured GTM dossier with citation footnotes:

```mermaid
graph TD
    Domain[Input: Company Domain] -->|1. Parse URLs| Crawler[Crawler Engine]
    
    subgraph HTML Download & Staging
        Crawler -->|2. GET homepage| RawHome[Homepage HTML]
        Crawler -->|2. GET pricing| RawPrice[Pricing HTML]
        Crawler -->|2. GET news| RawNews[News HTML]
    end
    
    subgraph Information Extraction & Footnotes
        RawHome -->|3. Regex/BS4| ExtractHome[Extract background & tech]
        RawPrice -->|3. Regex/BS4| ExtractPrice[Extract prices & contract values]
        RawNews -->|3. Regex/BS4| ExtractNews[Extract competitor mentions & news]
    end
    
    ExtractHome -->|4. Log Source Tag| CitationMap[(Citation Database)]
    ExtractPrice -->|4. Log Source Tag| CitationMap
    ExtractNews -->|4. Log Source Tag| CitationMap
    
    subgraph Data Audit Gate
        CitationMap -->|5. Aggregate Coverage| Scorer[Confidence Scorer Engine]
        Scorer -->|6. Calculate Score| AuditCheck{Is Score >= 80%?}
    end
    
    AuditCheck -->|Yes: Auto-outbound| Compile[Report Compiler / LLM]
    AuditCheck -->|No: Soft warning| Manual[Flag for manual operations check]
    
    Compile -->|7. Generate Dossier| Dossier[GTM Dossier Report]
    Manual -->|7. Generate Dossier| Dossier
```

---

## ⚙️ Citation Footnote Schema

To ensure auditability, GTM databases map citations using a simple relational structure:

```sql
-- 1. Citations Registry Table
CREATE TABLE facts_citations (
    citation_id SERIAL PRIMARY KEY,
    lead_id INT REFERENCES leads(id) ON DELETE CASCADE,
    source_url VARCHAR(500) NOT NULL, -- e.g. "https://stripe.com/pricing"
    element_selector VARCHAR(255) NOT NULL, -- e.g. "meta[name=description]" or "div.pricing-card"
    extracted_text TEXT NOT NULL, -- e.g. "2.9% + 30c per charge"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Whenever the research agent writes to the database, it inserts entries into the citations table and links their `citation_id` to the lead profile.

---

## 📊 Confidence Scoring weights Matrix

The confidence scoring engine calculates values based on data availability across four key categories:

| Target Category | Extraction Marker | Database Field | Weight |
| :--- | :--- | :--- | :--- |
| **Firmographics** | Homepage description meta tag | `description` | **25%** |
| **Technographics** | Framework generator or script tag | `tech_stack` | **25%** |
| **Pricing Models** | Numeric price string or custom tier | `pricing` | **25%** |
| **Competitive Mapping** | Press release competitor mention | `competitors` | **25%** |
