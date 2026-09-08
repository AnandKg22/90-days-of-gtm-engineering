# Day 040: AI Revenue Automation Platform (ARAP) v1 - Backend
import os
import sys
import json
import sqlite3
import random
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

app = Flask(__name__, static_folder='static', template_folder='templates')

DB_PATH = os.path.join(os.path.dirname(__file__), 'arap_database.db')

# Setup SQLite Database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Leads Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        company TEXT NOT NULL,
        title TEXT NOT NULL,
        revenue REAL NOT NULL,
        region TEXT NOT NULL,
        segment TEXT NOT NULL,
        status TEXT DEFAULT 'New',
        score INTEGER DEFAULT 0,
        enrich_tech_stack TEXT,
        enrich_employees INTEGER,
        enrich_funding TEXT,
        enrich_industry TEXT,
        ai_summary TEXT,
        ai_pain_points TEXT,
        ai_email TEXT,
        crm_sync_status TEXT DEFAULT 'Pending',
        crm_hubspot_id TEXT,
        crm_salesforce_id TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Activity Log Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER,
        action TEXT NOT NULL,
        details TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Pre-populate with mock data if empty
    cursor.execute('SELECT COUNT(*) FROM leads')
    if cursor.fetchone()[0] == 0:
        mock_leads = [
            ("Bruce", "Wayne", "bruce@waynecorp.com", "Wayne Enterprises", "CEO", 50000000.0, "AMER", "Enterprise", "New", 0),
            ("Sarah", "Connor", "sconnor@cyberdyne.co", "Cyberdyne Systems", "Operations Director", 8500000.0, "AMER", "Mid-Market", "New", 0),
            ("Deckard", "Shaw", "d.shaw@tyrell.co.jp", "Tyrell Corp", "VP of Engineering", 22000000.0, "APAC", "Enterprise", "New", 0)
        ]
        for l in mock_leads:
            cursor.execute('''
            INSERT INTO leads (first_name, last_name, email, company, title, revenue, region, segment, status, score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', l)
            
        mock_activities = [
            (None, "SYSTEM_START", "ARAP v1 Database Initialized with mock data."),
            (1, "LEAD_INGEST", "Lead Bruce Wayne (Wayne Enterprises) ingested via lead intake form."),
            (2, "LEAD_INGEST", "Lead Sarah Connor (Cyberdyne Systems) ingested via bulk API."),
            (3, "LEAD_INGEST", "Lead Deckard Shaw (Tyrell Corp) ingested via webhook integration.")
        ]
        for a in mock_activities:
            cursor.execute('''
            INSERT INTO activities (lead_id, action, details)
            VALUES (?, ?, ?)
            ''', a)
            
    conn.commit()
    conn.close()

# Initialize DB on load
init_db()

def db_query(query, params=(), one=False, commit=False):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, params)
    
    if commit:
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id
        
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Dynamic Lead Scorer Algorithm
def score_lead(title: str, revenue: float, email: str, segment: str) -> Tuple[int, List[str]]:
    score = 40  # Base starting score
    factors = ["Base starting score: +40"]
    
    # 1. Title/Role Fit
    title_lower = title.lower()
    if any(t in title_lower for t in ["ceo", "cto", "cfo", "cio", "vp", "president", "founder", "director"]):
        score += 25
        factors.append("C-Suite / VP / Decision Maker Title: +25")
    elif any(t in title_lower for t in ["manager", "head", "lead"]):
        score += 15
        factors.append("Management / Team Lead Role: +15")
        
    # 2. Revenue (Firmographics)
    if revenue >= 10000000.0:  # > 10M
        score += 25
        factors.append("Enterprise Firmographic Revenue (> $10M): +25")
    elif revenue >= 1000000.0:  # > 1M
        score += 15
        factors.append("Mid-Market Firmographic Revenue (> $1M): +15")
    else:
        score += 5
        factors.append("SMB Firmographic Revenue (< $1M): +5")
        
    # 3. Email domain quality
    free_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    domain = email.split('@')[-1] if '@' in email else ""
    if domain in free_domains:
        score -= 20
        factors.append("Generic/Free Email Domain: -20")
    else:
        score += 10
        factors.append("Corporate Email Domain verified: +10")
        
    # 4. Target ICP Segment Match
    if segment == "Enterprise":
        score += 15
        factors.append("ICP Segment Match (Enterprise): +15")
    elif segment == "Mid-Market":
        score += 10
        factors.append("ICP Segment Match (Mid-Market): +10")
        
    # Clamp score between 0 and 100
    score = max(0, min(100, score))
    return score, factors

# Mock Enrichment Engine
def mock_enrich_company(company: str) -> Dict[str, Any]:
    industries = ["Advanced Tech", "AI & Robotics", "Logistics", "Financial Services", "Cybersecurity", "Manufacturing"]
    tech_stacks = [
        "React, Node.js, PostgreSQL, AWS, Salesforce, Google Workspace",
        "Vue.js, Django, PostgreSQL, Azure, HubSpot, Slack",
        "Next.js, FastAPI, MongoDB, AWS, HubSpot, Jira",
        "Laravel, MySQL, GCP, Salesforce, Slack, Notion"
    ]
    funding_rounds = ["Series A ($12M)", "Series B ($35M)", "Series C ($75M)", "Bootstrapped", "Publicly Traded"]
    
    random.seed(hash(company))
    
    return {
        "industry": random.choice(industries),
        "tech_stack": random.choice(tech_stacks),
        "funding": random.choice(funding_rounds),
        "employees": random.randint(50, 4500)
    }

# High-fidelity local AI Copywriter / Summarizer (Fallback for Gemini)
def local_ai_generate(lead: Dict[str, Any], enrich_data: Dict[str, Any]) -> Tuple[str, str, str]:
    company = lead["company"]
    name = f"{lead['first_name']} {lead['last_name']}"
    title = lead["title"]
    tech = enrich_data["tech_stack"]
    industry = enrich_data["industry"]
    
    summary = (
        f"{company} is a leading enterprise operating in the {industry} sector. "
        f"They deploy a modern technology stack including {tech.split(',')[0]} and {tech.split(',')[1]} to power their operations. "
        f"The company has recently scaled its team and is looking to automate core operations to improve efficiency."
    )
    
    pain_points = (
        f"1. **Integration Silos**: Operating with separate {tech.split(',')[-2].strip()} and CRM tools causes data delays.\n"
        f"2. **Operational Latency**: Manual lead handling by team members like {name} restricts lead speed.\n"
        f"3. **Technical Overhead**: Maintaining disjointed APIs on GCP/AWS requires extensive engineering hours."
    )
    
    email = (
        f"Subject: Accelerating operational efficiency at {company}\n\n"
        f"Hi {lead['first_name']},\n\n"
        f"I noticed that {company} is growing rapidly in the {industry} space. "
        f"With your tech stack utilizing {tech.split(',')[0]} and {tech.split(',')[1]}, I suspect your sales and engineering teams "
        f"are spending valuable hours manually syncing data between tools. As {title}, I'm sure streamlining this is top of mind.\n\n"
        f"Our Revenue Automation Platform integrates seamlessly with your tools to eliminate manual data entry, "
        f"meaning AEs can focus on deals instead of copy-pasting.\n\n"
        f"Would you be open to a brief 10-minute sync next Tuesday at 2 PM to explore how we can save your team 15+ hours a week?\n\n"
        f"Best regards,\n"
        f"Revenue Operations Team"
    )
    
    return summary, pain_points, email

# API Route: Login Page / Simulated Auth
@app.route('/')
def home():
    return render_template('index.html')

# API Route: Fetch all leads
@app.route('/api/leads', methods=['GET'])
def get_leads():
    leads = db_query('SELECT * FROM leads ORDER BY score DESC, id DESC')
    leads_list = []
    for l in leads:
        leads_list.append(dict(l))
    return jsonify(leads_list)

# API Route: Ingest a new lead via Intake Form
@app.route('/api/leads', methods=['POST'])
def add_lead():
    data = request.json
    first_name = data.get("first_name", "").strip()
    last_name = data.get("last_name", "").strip()
    email = data.get("email", "").strip()
    company = data.get("company", "").strip()
    title = data.get("title", "").strip()
    revenue = float(data.get("revenue", 0.0))
    region = data.get("region", "AMER")
    segment = data.get("segment", "Mid-Market")
    
    if not first_name or not email or not company:
        return jsonify({"error": "Missing required fields: first_name, email, company"}), 400
        
    try:
        lead_id = db_query('''
        INSERT INTO leads (first_name, last_name, email, company, title, revenue, region, segment, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, email, company, title, revenue, region, segment, 'New'), commit=True)
        
        # Log lead ingestion activity
        db_query('''
        INSERT INTO activities (lead_id, action, details)
        VALUES (?, 'LEAD_INGEST', ?)
        ''', (lead_id, f"Lead {first_name} {last_name} ({company}) successfully submitted via intake form."), commit=True)
        
        # Simulate Workflow Automation trigger: automatically enrich and score
        enrich_and_score_lead_pipeline(lead_id)
        
        return jsonify({"message": "Lead submitted and processing pipeline triggered", "lead_id": lead_id}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email address already exists"}), 400

# Pipeline function for workflow automation (triggers enrichment, scoring, AI copywriting, and updates state)
def enrich_and_score_lead_pipeline(lead_id: int):
    # Fetch lead details
    lead = dict(db_query('SELECT * FROM leads WHERE id = ?', (lead_id,), one=True))
    
    # 1. Run Company Enrichment
    enrich = mock_enrich_company(lead["company"])
    
    # 2. Run Lead Scoring Engine
    score, factors = score_lead(lead["title"], lead["revenue"], lead["email"], lead["segment"])
    
    # 3. Generate AI Summary, Pain Points, and Outreach
    summary, pain_points, email = local_ai_generate(lead, enrich)
    
    # 4. Update lead record
    db_query('''
    UPDATE leads 
    SET status = 'Enriched',
        score = ?,
        enrich_tech_stack = ?,
        enrich_employees = ?,
        enrich_funding = ?,
        enrich_industry = ?,
        ai_summary = ?,
        ai_pain_points = ?,
        ai_email = ?
    WHERE id = ?
    ''', (score, enrich["tech_stack"], enrich["employees"], enrich["funding"], enrich["industry"], summary, pain_points, email, lead_id), commit=True)
    
    # Log activities
    db_query('''
    INSERT INTO activities (lead_id, action, details)
    VALUES (?, 'LEAD_ENRICH', ?)
    ''', (lead_id, f"Enriched firmographics: Industry={enrich['industry']}, Employees={enrich['employees']}. Lead score calculated at {score}."), commit=True)
    
    db_query('''
    INSERT INTO activities (lead_id, action, details)
    VALUES (?, 'AI_ANALYSIS', ?)
    ''', (lead_id, "Completed AI Pain-Point Analysis and generated personalized email copy."), commit=True)

# API Route: Force Enrich a Lead
@app.route('/api/leads/<int:lead_id>/enrich', methods=['POST'])
def enrich_lead(lead_id):
    enrich_and_score_lead_pipeline(lead_id)
    lead = dict(db_query('SELECT * FROM leads WHERE id = ?', (lead_id,), one=True))
    return jsonify(lead)

# API Route: CRM Synchronization (Simulated Salesforce/HubSpot)
@app.route('/api/leads/<int:lead_id>/crm-sync', methods=['POST'])
def crm_sync(lead_id):
    lead = db_query('SELECT * FROM leads WHERE id = ?', (lead_id,), one=True)
    if not lead:
        return jsonify({"error": "Lead not found"}), 404
        
    lead = dict(lead)
    
    # Simulate CRM API latency and response
    hs_id = f"hs_contact_{random.randint(100000, 999999)}"
    sf_id = f"sf_lead_{random.randint(500000, 899999)}"
    
    db_query('''
    UPDATE leads 
    SET status = 'Synced',
        crm_sync_status = 'Success',
        crm_hubspot_id = ?,
        crm_salesforce_id = ?
    WHERE id = ?
    ''', (hs_id, sf_id, lead_id), commit=True)
    
    # Log activity
    db_query('''
    INSERT INTO activities (lead_id, action, details)
    VALUES (?, 'CRM_SYNC', ?)
    ''', (lead_id, f"Synced lead to HubSpot (ID: {hs_id}) and Salesforce (ID: {sf_id}). Status: Success."), commit=True)
    
    # Log simulated Email notification
    db_query('''
    INSERT INTO activities (lead_id, action, details)
    VALUES (?, 'EMAIL_NOTIFICATION', ?)
    ''', (lead_id, f"Slack notification and email alert dispatched to Account Manager: New Hot Lead ({lead['company']} - Score: {lead['score']}) Synced."), commit=True)
    
    return jsonify({
        "status": "Success",
        "hubspot_id": hs_id,
        "salesforce_id": sf_id
    })

# API Route: Dashboard Analytics and Metrics
@app.route('/api/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Stats
    cursor.execute('SELECT COUNT(*) FROM leads')
    total_leads = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM leads WHERE score >= 70')
    sql_count = cursor.fetchone()[0] # Hot Leads
    
    cursor.execute('SELECT AVG(score) FROM leads')
    avg_score = cursor.fetchone()[0] or 0
    
    cursor.execute('SELECT COUNT(*) FROM leads WHERE crm_sync_status = "Success"')
    synced_count = cursor.fetchone()[0]
    
    # Pipeline calculation: Won value or expected pipeline
    # To model ARR: count of synced leads * average assumed ARR ($25,000)
    est_pipeline = synced_count * 25000.0
    
    # Funnel counts
    cursor.execute('SELECT status, COUNT(*) FROM leads GROUP BY status')
    funnel_dist = {row[0]: row[1] for row in cursor.fetchall()}
    
    # Segment distributions
    cursor.execute('SELECT segment, COUNT(*) FROM leads GROUP BY segment')
    segment_dist = {row[0]: row[1] for row in cursor.fetchall()}
    
    # Recent Activities
    cursor.execute('SELECT * FROM activities ORDER BY id DESC LIMIT 15')
    recent_activities = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return jsonify({
        "total_leads": total_leads,
        "hot_leads": sql_count,
        "avg_score": round(avg_score, 1),
        "synced_count": synced_count,
        "est_pipeline": est_pipeline,
        "funnel": funnel_dist,
        "segments": segment_dist,
        "activities": recent_activities
    })

# API Route: Fetch activities list
@app.route('/api/activities', methods=['GET'])
def get_activities():
    activities = db_query('SELECT * FROM activities ORDER BY id DESC LIMIT 50')
    activities_list = [dict(a) for a in activities]
    return jsonify(activities_list)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting GTM Capstone Backend server on http://localhost:{port}...")
    app.run(host='0.0.0.0', port=port, debug=True)
