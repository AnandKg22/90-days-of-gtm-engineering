# GTM Architecture - Day 026: Looker Studio Ingestion & Caching

This document details the data source connection architecture and caching layer designed inside the Looker Studio reporting environment.

---

## 🔄 Data Source Connector Ingestion & Caching Flow

The diagram below details the path of queries from Looker dashboard widgets through caching layers to databases:

```mermaid
graph TD
    User[Looker Studio Dashboard Widget] -->|1. Request KPI metric| Cache{Is Cached in Looker?}
    Cache -->|Yes: within Freshness SLA| Return[Return Cached Value]
    
    Cache -->|No: Cache Expired| BQ_Cache{Is Cached in GCP BI Engine?}
    
    subgraph Google Cloud Platform
        BQ_Cache -->|Yes: RAM Hit| Return_BQ[Return RAM Results]
        BQ_Cache -->|No: Disk Scan| BigQuery[(Google BigQuery Warehouse)]
    end
    
    subgraph PostgreSQL Database
        Cache -->|No: JDBC Connector| Postgres[(Postgres DB)]
    end
    
    subgraph Google Sheets
        Cache -->|No: Sheets API| Sheets[Google Sheets API]
    end
```

---

## ⚙️ Looker Studio Connector Security Configuration

To secure PostgreSQL JDBC connections, specify certificate mappings inside the connector credential prompts:

1.  **SSL Validation**: Force connection encryption.
2.  **Key Pair Upload**:
    *   **Server CA Certificate**: Verifies the server identity.
    *   **Client Certificate**: Verifies the Looker client identity.
    *   **Client Private Key**: Authenticates requests.
