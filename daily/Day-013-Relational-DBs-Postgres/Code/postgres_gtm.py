# GTM Relational Database & Optimization Engine
import sqlite3
import sys

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def init_database() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # 1. Create Leads Table
    cursor.execute("""
    CREATE TABLE leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        utm_source TEXT DEFAULT 'direct',
        utm_medium TEXT DEFAULT 'none',
        utm_campaign TEXT DEFAULT 'none',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    # 2. Create Deals Table
    cursor.execute("""
    CREATE TABLE deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        amount REAL DEFAULT 0.00,
        stage TEXT DEFAULT 'Discovery',
        FOREIGN KEY (lead_id) REFERENCES leads(id) ON DELETE CASCADE
    );
    """)
    
    # 3. Create Optimization Indexes
    cursor.execute("CREATE INDEX idx_leads_utm_source ON leads(utm_source);")
    cursor.execute("CREATE INDEX idx_deals_lead_id ON deals(lead_id);")
    
    conn.commit()
    return conn

def seed_data(conn):
    cursor = conn.cursor()
    
    # Insert Leads
    leads = [
        ("captain@imsgoa.org", "google", "cpc", "maritime_exam_prep"),
        ("registrar@ametuniv.edu.in", "newsletter", "email", "july_institutions"),
        ("sharma.r@tolani.edu", "google", "cpc", "maritime_exam_prep"),
        ("cadet.admit@oceanic.in", "organic", "search", "seo_ranking"),
        ("training@greatship.com", "organic", "search", "seo_ranking"),
        ("operations@seafarer.sg", "direct", "none", "none")
    ]
    cursor.executemany("INSERT INTO leads (email, utm_source, utm_medium, utm_campaign) VALUES (?, ?, ?, ?)", leads)
    
    # Retrieve lead IDs for deal linkage
    cursor.execute("SELECT id, utm_source FROM leads")
    lead_map = {row[1]: row[0] for row in cursor.fetchall()}
    
    # Insert Deals
    deals = [
        (lead_map["google"], "IMSGOA Campus Deal", 5000.00, "Won"),
        (lead_map["newsletter"], "AMET Enterprise License", 12000.00, "Won"),
        (lead_map["google"], "Tolani Advanced Simulator", 15000.00, "Won"),
        (lead_map["organic"], "Oceanic Cadet Bundle", 3000.00, "Discovery")
    ]
    cursor.executemany("INSERT INTO deals (lead_id, name, amount, stage) VALUES (?, ?, ?, ?)", deals)
    
    conn.commit()

def run_analytics_reports(conn):
    cursor = conn.cursor()
    
    # Query 1: Revenue by utm_source
    print("\n[REPORT 1] REVENUE CLOSED WON BY UTM SOURCE")
    cursor.execute("""
    SELECT 
        l.utm_source,
        COUNT(d.id) AS wins,
        SUM(d.amount) AS total_revenue
    FROM deals d
    JOIN leads l ON d.lead_id = l.id
    WHERE d.stage = 'Won'
    GROUP BY l.utm_source
    ORDER BY total_revenue DESC;
    """)
    for row in cursor.fetchall():
        print(f"  Source: {row[0]:<12} | Wins: {row[1]} | Total Revenue: ${row[2]:,.2f} USD")
        
    # Query 2: Funnel Conversion Rate
    print("\n[REPORT 2] FUNNEL CONVERSION RATE (LEAD -> WON DEAL)")
    cursor.execute("""
    SELECT 
        COUNT(DISTINCT l.id) AS total_leads,
        COUNT(DISTINCT d.id) AS won_deals,
        (CAST(COUNT(DISTINCT CASE WHEN d.stage = 'Won' THEN d.id END) AS FLOAT) / COUNT(DISTINCT l.id) * 100) AS conversion_rate
    FROM leads l
    LEFT JOIN deals d ON d.lead_id = l.id;
    """)
    row = cursor.fetchone()
    print(f"  Total Registered Leads: {row[0]}")
    print(f"  Total Closed Won Deals:  {row[1]}")
    print(f"  Funnel Conversion Rate:  {row[2]:.2f}%")

def audit_query_plan(conn):
    cursor = conn.cursor()
    print("\n" + "=" * 65)
    print("                 SQL QUERY OPTIMIZATION AUDIT")
    print("=" * 65)
    
    # Run EXPLAIN QUERY PLAN to verify index usage
    cursor.execute("""
    EXPLAIN QUERY PLAN
    SELECT l.email, d.name, d.amount
    FROM deals d
    JOIN leads l ON d.lead_id = l.id
    WHERE l.utm_source = 'google';
    """)
    
    print("Query Execution Plan steps:")
    for step in cursor.fetchall():
        print(f"  Step ID: {step[0]} | Detail: {step[3]}")
    print("=" * 65)

if __name__ == "__main__":
    print("=" * 65)
    print("             VIVAEXAMS GTM REPLICA DATABASE ENGINE")
    print("=" * 65)
    
    db_conn = init_database()
    seed_data(db_conn)
    run_analytics_reports(db_conn)
    audit_query_plan(db_conn)
