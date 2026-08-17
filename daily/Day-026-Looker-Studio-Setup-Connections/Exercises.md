# Exercises - Day 026: Looker Studio Connector Setup

This document details the configuration parameters required to connect Looker Studio dashboards to GCP BigQuery, PostgreSQL databases, and Google Sheets.

---

## ⚙️ Looker Studio Connection Blueprints

To connect warehouse sources safely, use the following configuration profiles:

### 1. Google BigQuery Native Connector
*   **Authentication**: OAuth2 (User Credentials) or Service Account File.
*   **Connection Mode**: Custom Query (Recommended) or Table Selection.
*   **Parameters**:
    *   Billing Project ID: `vivaexams-production`
    *   Custom SQL:
        ```sql
        SELECT * FROM `vivaexams-production.vivaexams_gtm.fct_deals`
        ```
*   **Optimization**: Enable **BI Engine** cache for memory reservations.

### 2. PostgreSQL JDBC Database Connector
*   **Authentication**: Username/Password with mandatory SSL.
*   **Host Parameter**: IP Address `104.24.11.89` (Port `5432`).
*   **Database Name**: `vivaexams_gtm_analytics`
*   **Security Certificates**: Upload client SSL Key (`client-key.pem`), client certificate (`client-cert.pem`), and Server CA certificate (`server-ca.pem`).
*   **Query Method**: Connect via Custom SQL view to prevent slow full-table index scans.

### 3. Google Sheets Quick Connector
*   **Source File**: Open file selector -> Choose `vivaexams_icp_leads_2026`.
*   **Options**:
    *   *Use first row as headers*: **Enabled**.
    *   *Include hidden and filtered cells*: **Disabled** (keeps reports clean).
