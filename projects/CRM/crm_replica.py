# SQLite Mini CRM Database Replica Engine
import sqlite3

def init_crm_db():
    # 1. Connect to an in-memory database
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # 2. Run DDL commands to create tables
    cursor.execute("""
    CREATE TABLE companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        domain TEXT UNIQUE,
        employee_count INTEGER
    );
    """)
    
    cursor.execute("""
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER,
        first_name TEXT,
        last_name TEXT,
        email TEXT UNIQUE,
        FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE SET NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER,
        name TEXT NOT NULL,
        stage TEXT,
        amount REAL,
        FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
    );
    """)
    
    cursor.execute("""
    CREATE TABLE contacts_deals (
        contact_id INTEGER,
        deal_id INTEGER,
        role TEXT,
        PRIMARY KEY (contact_id, deal_id),
        FOREIGN KEY (contact_id) REFERENCES contacts(id) ON DELETE CASCADE,
        FOREIGN KEY (deal_id) REFERENCES deals(id) ON DELETE CASCADE
    );
    """)
    
    cursor.execute("""
    CREATE TABLE activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_id INTEGER,
        type TEXT,
        subject TEXT,
        logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (contact_id) REFERENCES contacts(id) ON DELETE CASCADE
    );
    """)
    
    conn.commit()
    return conn

def seed_data(conn):
    cursor = conn.cursor()
    
    # 1. Insert Companies
    cursor.execute("INSERT INTO companies (name, domain, employee_count) VALUES ('Tolani Maritime Institute', 'tolani.edu', 120)")
    tolani_id = cursor.lastrowid
    
    cursor.execute("INSERT INTO companies (name, domain, employee_count) VALUES ('AMET University', 'ametuniv.edu.in', 250)")
    amet_id = cursor.lastrowid
    
    cursor.execute("INSERT INTO companies (name, domain, employee_count) VALUES ('IMSGOA Maritime College', 'imsgoa.org', 60)")
    imsgoa_id = cursor.lastrowid
    
    # 2. Insert Contacts
    cursor.execute("INSERT INTO contacts (company_id, first_name, last_name, email) VALUES (?, 'Ravi', 'Sharma', 'sharma.r@tolani.edu')", (tolani_id,))
    ravi_id = cursor.lastrowid
    
    cursor.execute("INSERT INTO contacts (company_id, first_name, last_name, email) VALUES (?, 'Anil', 'Kumar', 'registrar@ametuniv.edu.in')", (amet_id,))
    anil_id = cursor.lastrowid
    
    cursor.execute("INSERT INTO contacts (company_id, first_name, last_name, email) VALUES (?, 'Vikram', 'Singh', 'captain@imsgoa.org')", (imsgoa_id,))
    vikram_id = cursor.lastrowid
    
    # 3. Insert Deals
    cursor.execute("INSERT INTO deals (company_id, name, stage, amount) VALUES (?, 'Tolani 500 Cadet Licenses', 'Legal', 10000.00)", (tolani_id,))
    tolani_deal_id = cursor.lastrowid
    
    cursor.execute("INSERT INTO deals (company_id, name, stage, amount) VALUES (?, 'AMET Campus Deployment', 'Demo', 20000.00)", (amet_id,))
    
    cursor.execute("INSERT INTO deals (company_id, name, stage, amount) VALUES (?, 'IMSGOA Mock Exam Bundle', 'Proposal', 5000.00)", (imsgoa_id,))
    imsgoa_deal_id = cursor.lastrowid
    
    # 4. Insert Associations (N:M)
    cursor.execute("INSERT INTO contacts_deals (contact_id, deal_id, role) VALUES (?, ?, 'Primary Evaluator')", (ravi_id, tolani_deal_id))
    cursor.execute("INSERT INTO contacts_deals (contact_id, deal_id, role) VALUES (?, ?, 'Economic Buyer')", (vikram_id, imsgoa_deal_id))
    
    # 5. Insert Activities
    cursor.execute("INSERT INTO activities (contact_id, type, subject) VALUES (?, 'Email', 'Sent bulk license pricing table')", (ravi_id,))
    cursor.execute("INSERT INTO activities (contact_id, type, subject) VALUES (?, 'Call', 'Qualified proctoring requirements with Dean')", (vikram_id,))
    
    conn.commit()

def run_queries(conn):
    cursor = conn.cursor()
    
    # Query 1: Contacts and Employer Companies
    print("\n[QUERY 1] CONTACTS & EMPLOYERS REPORT")
    cursor.execute("""
    SELECT c.first_name, c.last_name, c.email, comp.name 
    FROM contacts c
    LEFT JOIN companies comp ON c.company_id = comp.id
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]} {row[1]} ({row[2]}) works at: {row[3]}")
        
    # Query 2: Deals Pipeline
    print("\n[QUERY 2] DEALS PIPELINE REPORT")
    cursor.execute("""
    SELECT d.name, comp.name, d.stage, d.amount 
    FROM deals d
    JOIN companies comp ON d.company_id = comp.id
    """)
    for row in cursor.fetchall():
        print(f"  Deal: '{row[0]}' | Client: {row[1]} | Stage: {row[2]} | Amount: ${row[3]:,.2f}")
        
    # Query 3: Activity Log with Contact Names
    print("\n[QUERY 3] ACTIVITY AUDIT LOG")
    cursor.execute("""
    SELECT c.first_name, c.last_name, a.type, a.subject, a.logged_at 
    FROM activities a
    JOIN contacts c ON a.contact_id = c.id
    """)
    for row in cursor.fetchall():
        print(f"  [{row[4]}] {row[0]} {row[1]} | {row[2]}: '{row[3]}'")

if __name__ == "__main__":
    print("=" * 65)
    print("           INITIALIZING MINI CRM DATABASE SIMULATION")
    print("=" * 65)
    
    connection = init_crm_db()
    seed_data(connection)
    run_queries(connection)
    
    print("=" * 65)
