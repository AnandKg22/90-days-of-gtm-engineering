# Revenue Operations (RevOps) & Data Pipelines

RevOps coordinates Marketing, Sales, Customer Success, and Systems Operations to build clean data flows and maximize conversion efficiency.

---

## 1. The RevOps Architecture

RevOps manages data synchronization and transitions between systems:

```
[Traffic/Ads] ──> [HubSpot Marketing] ──> [n8n Automation] ──> [Salesforce Sales Cloud] ──> [Customer Database]
                       │                                             │                            │
                   Data Capture                              Validation & Route              Usage Signals
```

*   **Marketing Ops**: Manages lead intake forms, attribution, email drip sequences, and list segmentation.
*   **Sales Ops**: Manages deal structures, pipeline stages, forecasting metrics, and CRM properties.
*   **Customer Success Ops**: Tracks product adoption milestones, support tickets, and renewal contracts.

---

## 2. Lead Routing Engines & SLA Enforcement

When a hot lead comes in, we must assign it to the correct Sales Representative instantly and enforce a response Service Level Agreement (SLA).

### Round-Robin Assignment Database Schema

```sql
-- Keep track of active sales reps and their capacity
CREATE TABLE sales_representatives (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    last_assigned_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    current_lead_count INT DEFAULT 0
);

-- Lead assignment queue tracking
CREATE TABLE lead_assignments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    lead_email VARCHAR(255) NOT NULL,
    assigned_rep_id UUID REFERENCES sales_representatives(id),
    assigned_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    responded_at TIMESTAMP WITH TIME ZONE,
    sla_breached BOOLEAN DEFAULT FALSE,
    sla_limit_minutes INT DEFAULT 15
);
```

### Lead Router Engine logic (Python)

```python
import psycopg2
from datetime import datetime, timedelta

def get_next_available_rep(conn):
    cursor = conn.cursor()
    # Find active rep who hasn't been assigned a lead for the longest time
    cursor.execute("""
        SELECT id, email 
        FROM sales_representatives 
        WHERE active = TRUE 
        ORDER BY last_assigned_at ASC 
        LIMIT 1;
    """)
    rep = cursor.fetchone()
    return rep

def assign_lead(conn, lead_email):
    cursor = conn.cursor()
    rep = get_next_available_rep(conn)
    if not rep:
        print("No active sales reps available.")
        return None
    
    rep_id, rep_email = rep
    now = datetime.utcnow()
    
    # 1. Update rep's last assignment timestamp
    cursor.execute("""
        UPDATE sales_representatives 
        SET last_assigned_at = %s 
        WHERE id = %s;
    """, (now, rep_id))
    
    # 2. Record lead assignment
    cursor.execute("""
        INSERT INTO lead_assignments (lead_email, assigned_rep_id, assigned_at) 
        VALUES (%s, %s, %s) 
        RETURNING id;
    """, (lead_email, rep_id, now))
    
    assignment_id = cursor.fetchone()[0]
    conn.commit()
    print(f"Lead {lead_email} assigned to Rep {rep_email}")
    return assignment_id

# Background script checks SLA breach hourly
def check_sla_breaches(conn):
    cursor = conn.cursor()
    # If lead is assigned, not responded to, and time elapsed > 15 mins, mark as breached
    cursor.execute("""
        UPDATE lead_assignments 
        SET sla_breached = TRUE 
        WHERE responded_at IS NULL 
          AND crm_responded = FALSE
          AND assigned_at < NOW() - INTERVAL '15 minutes'
          AND sla_breached = FALSE
        RETURNING id, lead_email;
    """)
    breached_leads = cursor.fetchall()
    conn.commit()
    for assignment_id, email in breached_leads:
        send_sla_alert_to_slack(email)
```
