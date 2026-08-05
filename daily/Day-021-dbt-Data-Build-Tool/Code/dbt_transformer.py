# dbt Compiler & DAG Execution Engine
import sqlite3
import sys
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 1. dbt SQL Model Templates (with Jinja-style macros)
DBT_MODELS = {
    "stg_leads": {
        "materialized": "view",
        "sql": """
        CREATE VIEW stg_leads AS
        SELECT 
            id AS lead_id,
            LOWER(email) AS email,
            COALESCE(utm_source, 'direct') AS utm_source,
            created_at
        FROM {{ source('raw_crm', 'leads') }};
        """
    },
    "stg_deals": {
        "materialized": "view",
        "sql": """
        CREATE VIEW stg_deals AS
        SELECT 
            id AS deal_id,
            lead_id,
            name AS deal_name,
            amount AS amount_usd,
            stage AS deal_stage
        FROM {{ source('raw_crm', 'deals') }};
        """
    },
    "fct_deals": {
        "materialized": "table",
        "sql": """
        CREATE TABLE fct_deals AS
        SELECT 
            d.deal_id,
            d.deal_name,
            d.amount_usd,
            l.utm_source,
            d.deal_stage
        FROM {{ ref('stg_deals') }} d
        JOIN {{ ref('stg_leads') }} l ON d.lead_id = l.lead_id
        WHERE d.deal_stage = 'Won';
        """
    }
}

class DBTCompiler:
    @staticmethod
    def compile_model(model_name: str, template_sql: str) -> str:
        # Compile source references: {{ source('raw_crm', 'table') }} -> raw_table
        compiled = template_sql
        compiled = compiled.replace("{{ source('raw_crm', 'leads') }}", "raw_leads")
        compiled = compiled.replace("{{ source('raw_crm', 'deals') }}", "raw_deals")
        
        # Compile model references: {{ ref('stg_leads') }} -> stg_leads
        compiled = compiled.replace("{{ ref('stg_leads') }}", "stg_leads")
        compiled = compiled.replace("{{ ref('stg_deals') }}", "stg_deals")
        return compiled.strip()

def seed_raw_warehouse_tables(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # Create raw source tables
    cursor.execute("""
    CREATE TABLE raw_leads (
        id INTEGER PRIMARY KEY,
        email TEXT,
        utm_source TEXT,
        created_at TIMESTAMP
    );
    """)
    cursor.execute("""
    CREATE TABLE raw_deals (
        id INTEGER PRIMARY KEY,
        lead_id INTEGER,
        name TEXT,
        amount REAL,
        stage TEXT
    );
    """)
    
    # Seed records
    cursor.execute("INSERT INTO raw_leads VALUES (1, 'dean@imsgoa.org', 'google', '2026-07-10')")
    cursor.execute("INSERT INTO raw_leads VALUES (2, 'registrar@ametuniv.edu.in', 'newsletter', '2026-07-11')")
    cursor.execute("INSERT INTO raw_deals VALUES (101, 1, 'IMSGOA Exam licenses', 8000.00, 'Won')")
    cursor.execute("INSERT INTO raw_deals VALUES (102, 2, 'AMET Campus Deal', 15000.00, 'Won')")
    conn.commit()

def run_dbt_tests(conn: sqlite3.Connection):
    cursor = conn.cursor()
    print("\n" + "=" * 65)
    print("                 DBT SCHEMA DATA QUALITY TESTS")
    print("=" * 65)
    
    # Test 1: Test Unique on fct_deals.deal_id
    print("[TEST unique] Field: fct_deals.deal_id ...")
    cursor.execute("""
    SELECT deal_id, COUNT(1) 
    FROM fct_deals 
    GROUP BY deal_id 
    HAVING COUNT(1) > 1;
    """)
    failures = cursor.fetchall()
    if failures:
        print(f"  [FAIL] Unique constraint violated on deal_id. Duplicates: {failures}")
    else:
        print("  [PASS] All values are unique.")
        
    # Test 2: Test Not Null on fct_deals.deal_id
    print("\n[TEST not_null] Field: fct_deals.deal_id ...")
    cursor.execute("SELECT COUNT(1) FROM fct_deals WHERE deal_id IS NULL;")
    null_count = cursor.fetchone()[0]
    if null_count > 0:
        print(f"  [FAIL] found {null_count} null records.")
    else:
        print("  [PASS] All values are not null.")
    print("=" * 65)

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    seed_raw_warehouse_tables(conn)
    
    print("=" * 65)
    print("             VIVAEXAMS DBT COMPILER & RUN PIPELINE")
    print("=" * 65)
    
    # 1. Resolve DAG dependency sequence
    # stg_leads and stg_deals must be executed before fct_deals
    execution_dag = ["stg_leads", "stg_deals", "fct_deals"]
    print(f"Computed DBT DAG sequence: {execution_dag}")
    print("-" * 65)
    
    # 2. Compile and execute models in order
    cursor = conn.cursor()
    for model in execution_dag:
        meta = DBT_MODELS[model]
        print(f"[*] Compiling Model: '{model}' (Materialization: {meta['materialized']})")
        compiled_sql = DBTCompiler.compile_model(model, meta["sql"])
        
        print(f"  Compiled SQL:\n  {compiled_sql.replace('\n', '\n  ')}")
        cursor.execute(compiled_sql)
        print(f"  [RUN SUCCESS] Created database view/table: {model}")
        print("-" * 65)
        
    # 3. Verify analytics output in fct_deals
    print("\nQuerying Marts Table: 'fct_deals'...")
    cursor.execute("SELECT * FROM fct_deals;")
    for row in cursor.fetchall():
        print(f"  Deal: '{row[1]}' | Amount: ${row[2]:,.2f} USD | Source: {row[3]} | Stage: {row[4]}")
        
    # 4. Run dbt schema tests
    run_dbt_tests(conn)
