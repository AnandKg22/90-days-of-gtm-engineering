# GTM Architecture - Day 020: Google BigQuery Ingestion Pipeline

This document details the Google Cloud Platform (GCP) GTM architecture that streams telemetry logs into partitioned BigQuery collections.

---

## 🔄 GCP Telemetry to BigQuery Pipeline Flow

The diagram below details the data flow from client website events, through cloud serverless functions, into BigQuery storage:

```mermaid
graph TD
    Client[Next.js Website Client] -->|1. user_activity: track calls| Segment[Segment CDP Ingest]
    Segment -->|2. Webhook Event Bundle| GCF[GCP Cloud Function Receiver]
    
    subgraph Google BigQuery Warehouse
        GCF -->|3. Streaming Insert| BQ_Table[(leads_partitioned Table)]
        BQ_Table -->|4. Split records by date| Partitions[(Daily Date Partitions)]
    end
    
    subgraph Data Analytics & BI
        Dashboard[Looker Studio Dashboard] -->|5. SQL Query with Date Filter| Partitions
    end
```

---

## ⚙️ BigQuery Table Configuration

To ensure query performance and minimize data scanning costs, we configure GTM tables in BigQuery as follows:

1.  **Date Partitioning**: The table is partitioned by the transaction's creation date (`created_date`). Queries that target specific dates (such as today's performance report) will bypass all other daily partitions, scanning only matching rows.
2.  **Clustering**: The table is clustered by `company_name` and `utm_source`. BigQuery sorts rows with matching values close to each other on storage disk, allowing high-performance filtering.
