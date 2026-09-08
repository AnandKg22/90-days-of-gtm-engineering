# Cheat Sheet - AI Revenue Automation Platform (ARAP) v1

This cheat sheet compiles API specifications, database commands, and scoring parameters for the ARAP v1 platform.

---

## 1. API Endpoints Reference

All endpoints assume local URL: `http://localhost:5000`

| Method | Endpoint | Description | Payload Schema |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/leads` | List all leads in the database | None |
| **POST** | `/api/leads` | Ingest a new lead and trigger pipeline | `{"first_name": "...", "email": "...", "company": "...", "revenue": 1000000}` |
| **POST** | `/api/leads/<id>/enrich` | Force enrichment and recalculate scoring | None |
| **POST** | `/api/leads/<id>/crm-sync` | Sync lead to Salesforce & HubSpot | None |
| **GET** | `/api/dashboard/stats` | Retrieve metrics and activity logs | None |
| **GET** | `/api/activities` | Retrieve complete system audit logs | None |

---

## 2. Lead Scoring Weight Matrix

The scoring engine aggregates weights based on four primary fields:

```text
Score = Base (40) + Title (max 25) + Firmographics (max 25) + Domain (max 10) + Segment (max 15) -> clamped to [0, 100]
```

*   **Role/Title Authority**:
    *   C-Suite/VP/Founder/Director: **+25**
    *   Manager/Lead/Head: **+15**
*   **Firmographics (Annual Revenue)**:
    *   Enterprise ($\ge \$10\text{M}$): **+25**
    *   Mid-Market ($\ge \$1\text{M}$): **+15**
    *   SMB ($< \$1\text{M}$): **+5**
*   **Domain Verification**:
    *   Corporate domain (e.g. `@waynecorp.com`): **+10**
    *   Free domain (e.g. `@gmail.com`): **-20**
*   **Target Segment Match**:
    *   Enterprise segment selected: **+15**
    *   Mid-Market segment selected: **+10**

---

## 3. Database & Deployment Operations

### Reset database & seed mock records
Run this command from inside the `Code` folder to reset the SQLite database:
```bash
# Delete old database
rm arap_database.db
# Initialize and seed database
python -c "from app import init_db; init_db()"
```

### Install Flask & Start Backend
To run the capstone locally:
```bash
# Install dependencies
pip install flask
# Run server
python app.py
```
