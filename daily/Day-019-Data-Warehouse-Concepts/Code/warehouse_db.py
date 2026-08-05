# GTM Data Warehouse ETL Engine
import sqlite3
import sys

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def init_warehouse_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # 1. Staging Tables (Raw ingestion)
    cursor.execute("""
    CREATE TABLE stg_companies (
        company_id INTEGER,
        name TEXT,
        industry TEXT,
        employees INTEGER
    );
    """)
    
    cursor.execute("""
    CREATE TABLE stg_deals (
        deal_id INTEGER,
        company_id INTEGER,
        name TEXT,
        amount REAL,
        seats INTEGER,
        close_date TEXT
    );
    """)
    
    # 2. Dimension Tables (Clean Context)
    cursor.execute("""
    CREATE TABLE dim_companies (
        company_key INTEGER PRIMARY KEY,
        company_name TEXT,
        industry TEXT,
        employee_count_tier TEXT
    );
    """)
    
    cursor.execute("""
    CREATE TABLE dim_dates (
        date_key INTEGER PRIMARY KEY, -- YYYYMMDD
        calendar_date TEXT,
        calendar_year INTEGER,
        calendar_quarter INTEGER,
        month_name TEXT
    );
    """)
    
    # 3. Fact Table (Numeric Metrics & FKs)
    cursor.execute("""
    CREATE TABLE fact_deals (
        deal_key INTEGER PRIMARY KEY,
        company_key INTEGER,
        date_key INTEGER,
        amount_usd REAL,
        license_seats INTEGER,
        FOREIGN KEY (company_key) REFERENCES dim_companies(company_key),
        FOREIGN KEY (date_key) REFERENCES dim_dates(date_key)
    );
    """)
    
    conn.commit()
    return conn

def seed_staging_tables(conn):
    cursor = conn.cursor()
    
    # Seed raw company records
    companies = [
        (1, "Tolani Maritime Institute", "Maritime Academy", 120),
        (2, "AMET University", "Maritime Academy", 250),
        (3, "IMSGOA Maritime College", "Maritime Academy", 45),
        (4, "Global Shipping Corp", "Maritime Shipping", 800)
    ]
    cursor.executemany("INSERT INTO stg_companies VALUES (?, ?, ?, ?)", companies)
    
    # Seed raw deal records
    deals = [
        (101, 1, "Tolani 500 Cadet Licenses", 10000.00, 500, "2026-03-15"), # Q1 2026
        (102, 2, "AMET Campus Deployment", 20000.00, 1000, "2026-06-20"),    # Q2 2026
        (103, 3, "IMSGOA Exam Bundle", 5000.00, 200, "2026-03-30"),          # Q1 2026
        (104, 4, "Global Shipping Pilot", 8000.00, 400, "2026-07-10")         # Q3 2026
    ]
    cursor.executemany("INSERT INTO stg_deals VALUES (?, ?, ?, ?, ?, ?)", deals)
    
    conn.commit()

def run_etl_pipeline(conn):
    cursor = conn.cursor()
    print("[*] Starting ETL Pipeline execution...")
    
    # 1. ETL: Populate dim_companies (with size tiering logic)
    print("  Transforming & Loading dim_companies...")
    cursor.execute("""
    INSERT INTO dim_companies (company_key, company_name, industry, employee_count_tier)
    SELECT 
        company_id,
        name,
        industry,
        CASE 
            WHEN employees <= 50 THEN 'SME (1-50)'
            WHEN employees > 50 AND employees <= 200 THEN 'Mid-Market (51-200)'
            ELSE 'Enterprise (201+)'
        END AS employee_count_tier
    FROM stg_companies;
    """)
    
    # 2. ETL: Populate dim_dates (extracting year, month, quarter from close_date)
    print("  Transforming & Loading dim_dates...")
    # SQL helper to generate date keys from stg_deals close_date
    cursor.execute("""
    INSERT OR IGNORE INTO dim_dates (date_key, calendar_date, calendar_year, calendar_quarter, month_name)
    SELECT DISTINCT
        CAST(REPLACE(close_date, '-', '') AS INTEGER) AS date_key,
        close_date,
        CAST(SUBSTR(close_date, 1, 4) AS INTEGER) AS calendar_year,
        CASE 
            WHEN SUBSTR(close_date, 6, 2) IN ('01','02','03') THEN 1
            WHEN SUBSTR(close_date, 6, 2) IN ('04','05','06') THEN 2
            WHEN SUBSTR(close_date, 6, 2) IN ('07','08','09') THEN 3
            ELSE 4
        END AS calendar_quarter,
        CASE SUBSTR(close_date, 6, 2)
            WHEN '01' THEN 'January' WHEN '02' THEN 'February' WHEN '03' THEN 'March'
            WHEN '04' THEN 'April' WHEN '05' THEN 'May' WHEN '06' THEN 'June'
            WHEN '07' THEN 'July' WHEN '08' THEN 'August' WHEN '09' THEN 'September'
            ELSE 'October'
        END AS month_name
    FROM stg_deals;
    """)
    
    # 3. ETL: Populate fact_deals
    print("  Loading fact_deals...")
    cursor.execute("""
    INSERT INTO fact_deals (deal_key, company_key, date_key, amount_usd, license_seats)
    SELECT 
        deal_id,
        company_id,
        CAST(REPLACE(close_date, '-', '') AS INTEGER) AS date_key,
        amount,
        seats
    FROM stg_deals;
    """)
    
    conn.commit()
    print("[+] ETL Pipeline execution complete.")

def run_sales_digest(conn):
    cursor = conn.cursor()
    print("\n" + "=" * 65)
    print("             VIVAEXAMS SALES PERFORMANCE DIGEST")
    print("=" * 65)
    
    # Query Star Schema
    cursor.execute("""
    SELECT 
        c.employee_count_tier,
        d.calendar_year,
        d.calendar_quarter,
        SUM(f.amount_usd) AS total_revenue,
        SUM(f.license_seats) AS total_seats
    FROM fact_deals f
    JOIN dim_companies c ON f.company_key = c.company_key
    JOIN dim_dates d ON f.date_key = d.date_key
    GROUP BY c.employee_count_tier, d.calendar_year, d.calendar_quarter
    ORDER BY total_revenue DESC;
    """)
    
    for row in cursor.fetchall():
        print(f"Tier:    {row[0]}")
        print(f"Period:  {row[1]} Q{row[2]}")
        print(f"Revenue: ${row[3]:,.2f} USD")
        print(f"Seats:   {row[4]} Licenses Sold")
        print("-" * 65)
    print("=" * 65)

if __name__ == "__main__":
    print("=" * 65)
    print("             VIVAEXAMS CLOUD DATA WAREHOUSE ENGINE")
    print("=" * 65)
    
    db_conn = init_warehouse_db()
    seed_staging_tables(db_conn)
    run_etl_pipeline(db_conn)
    run_sales_digest(db_conn)
