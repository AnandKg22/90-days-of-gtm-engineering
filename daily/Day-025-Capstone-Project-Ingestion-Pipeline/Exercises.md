# Exercises - Day 025: GTM Data Ingestion Strategy

This document details the GTM Data Ingestion Strategy blueprint, mapping telemetry streams, security protocols, and database targets.

---

## 📋 GTM Data Ingestion Strategy Blueprint

This blueprint coordinates ingestion methods, verification steps, transforms, and database targets for our primary event sources:

| Step | Ingestion Source | Ingest Method | Security & Auth | Data Transformation Rules | Target Table | Recovery Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Segment Activity** (Clicks, Page Views) | Webhook Ingress (POST) | API token header validation | Extract email domain; flatten nested click JSON array. | `stg_clickstream` | Drop invalid schemas; write to DLQ. |
| **2** | **Stripe Billing** (Checkout events) | Webhook Ingress (POST) | HMAC-SHA256 signature verification | Extract `customer_email`, calculate contract LTV and seats. | `fact_deals` | Exponential retry on 429/503 limits. |
| **3** | **HubSpot CRM** (Contact updates) | REST Pull API (GET) | OAuth2 Bearer Header token | Map company IDs to domains; parse employee counts to segments. | `dim_companies` | Hold pipeline if CRM connection fails. |
| **4** | **Database Logs** (Historical events) | Reverse ETL (Sync) | SSL client certificate | Query daily watermark view columns. | `dim_dates` | Resume sync from last recorded timestamp. |
