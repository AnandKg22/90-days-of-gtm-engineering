# Project Assignment - Day 044: AI Company Research Assistant

This project requires developing a Python AI Company Research Assistant. It crawls company web resources, extracts firmographic and technographic characteristics, traces exact citation coordinates, maps competitor positions, and evaluates the confidence levels of the gathered data.

---

## 🎯 Requirements

Your Research Assistant must:
1.  **Crawl Web Pages**:
    *   Ingest raw HTML representations of target company homepages, pricing pages, and press releases.
2.  **Extract Firmographics & Technographics**:
    *   Locate meta title, description tags, and developer generator names.
    *   Identify technology components (React, Next.js, database platforms).
3.  **Audit Pricing Models**:
    *   Locate numerical pricing strings (e.g. transactional percents, credit credits, subscription tiers).
4.  **Trace Citations Footnotes**:
    *   Every single data point extracted (company background, tech stack, pricing details, competitors) must be saved with a matching citation link mapping to its raw source element (e.g., `[Source: Homepage Title tag]`).
5.  **Map Competitor Layouts**:
    *   Scan press releases and news feeds for rival names (e.g., Databricks, Maxio) to map competitive positioning.
6.  **Calculate Data Confidence Score**:
    *   Determine the quality of the dossier based on coverage weights: Description Found (+25%), Tech Found (+25%), Pricing Found (+25%), Rivals Found (+25%).
    *   Generate a detailed confidence audit trail log.

---

## 💻 Deliverable Code

A complete, working AI Company Research Assistant script has been created and is available in [Code/ai_research_assistant.py](Code/ai_research_assistant.py). It runs crawls on Stripe and Snowflake, tracks citations, scores confidence, and displays full reports in the terminal.