# Day 045: AI SDR Agent v2 - Sequence Generator & CRM Integrator
import sys
from datetime import datetime, timedelta
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Mock Database of Qualified Leads (Enriched & Scored)
QUALIFIED_LEADS = [
    {
        "lead_id": 501,
        "name": "Bruce Wayne",
        "email": "bruce@waynecorp.com",
        "company": "Wayne Enterprises",
        "title": "CEO",
        "score": 90,
        "industry": "Aerospace & Defense",
        "tech_stack": "AWS, React, Python",
        "pain_point": "Manual data syncing between CRM and billing tables causing delayed financial closing."
    },
    {
        "lead_id": 502,
        "name": "Pepper Potts",
        "email": "pepper@stark.com",
        "company": "Stark Industries",
        "title": "CEO",
        "score": 95,
        "industry": "Advanced Robotics",
        "tech_stack": "GCP, Next.js, Rust",
        "pain_point": "Outbound lead routing delays resulting in high marketing lead leakage and slow SDR response times."
    }
]

class OutboundSequenceGenerator:
    def __init__(self, lead: Dict[str, Any]):
        self.lead = lead
        self.sequence: List[Dict[str, Any]] = []

    def compile_sequence(self) -> List[Dict[str, Any]]:
        """Generates a 4-touch GTM outreach sequence with scheduled offsets."""
        base_date = datetime.now()

        # Touch 1: Day 1 - Cold Email (Focus: Technographic & Pain point)
        touch1_date = base_date + timedelta(days=0)
        touch1_body = (
            f"Subject: Streamlining CRM data flows at {self.lead['company']}\n\n"
            f"Hi {self.lead['name'].split()[0]},\n\n"
            f"I saw that {self.lead['company']} is scaling aerospace operations while deploying a stack featuring "
            f"{self.lead['tech_stack'].split(',')[0]} and {self.lead['tech_stack'].split(',')[1]}.\n\n"
            f"Many CEO's tell us that keeping billing data in sync with CRM updates is a major bottleneck—often "
            f"resulting in {self.lead['pain_point'].lower()}\n\n"
            f"Our Revenue Platform automates this sync, cutting transaction reconciliations from days to minutes. "
            f"Would you be open to a 10-minute chat next Tuesday to explore how we can save your operations team 12+ hours weekly?\n\n"
            f"Best,\n"
            f"Sales Development Team"
        )
        self.sequence.append({
            "touchpoint": 1,
            "type": "Email",
            "schedule_date": touch1_date.strftime("%Y-%m-%d"),
            "subject": f"Streamlining CRM data flows at {self.lead['company']}",
            "body": touch1_body,
            "status": "Scheduled"
        })

        # Touch 2: Day 3 - LinkedIn Connect (Focus: Soft connection)
        touch2_date = base_date + timedelta(days=3)
        touch2_body = (
            f"Hi {self.lead['name'].split()[0]} - came across your profile while reviewing growth in the "
            f"{self.lead['industry']} space. Impressive work scaling the {self.lead['company']} team. "
            f"Wanted to connect to share some insights on how operations teams are automating manual pipeline reconciliations."
        )
        self.sequence.append({
            "touchpoint": 2,
            "type": "LinkedIn Connection",
            "schedule_date": touch2_date.strftime("%Y-%m-%d"),
            "subject": "LinkedIn Connection request",
            "body": touch2_body,
            "status": "Scheduled"
        })

        # Touch 3: Day 7 - Follow-up Email (Focus: Case Study & Social Proof)
        touch3_date = base_date + timedelta(days=7)
        touch3_body = (
            f"Subject: Quick follow up re: CRM pipeline automation\n\n"
            f"Hi {self.lead['name'].split()[0]},\n\n"
            f"I wanted to follow up on my previous note. We recently helped Cyberdyne Systems automate their data "
            f"sync loops, which reduced lead-to-sync times from 24 hours to under 30 seconds and drove a 15% increase in pipeline speed.\n\n"
            f"Given your focus at {self.lead['company']}, I thought this might be highly relevant.\n\n"
            f"Do you have 10 minutes next Thursday at 11 AM EST for a quick review?\n\n"
            f"Best,\n"
            f"Sales Development Team"
        )
        self.sequence.append({
            "touchpoint": 3,
            "type": "Email",
            "schedule_date": touch3_date.strftime("%Y-%m-%d"),
            "subject": "Quick follow up re: CRM pipeline automation",
            "body": touch3_body,
            "status": "Scheduled"
        })

        # Touch 4: Day 14 - Break-up Email (Focus: Soft close)
        touch4_date = base_date + timedelta(days=14)
        touch4_body = (
            f"Subject: Permission to close file?\n\n"
            f"Hi {self.lead['name'].split()[0]},\n\n"
            f"I haven't heard back, so I assume streamlining data syncs is not a priority at {self.lead['company']} right now. "
            f"I will close your file for now.\n\n"
            f"If timing shifts in the future and you want to revisit automating your revenue ops, feel free to reach out.\n\n"
            f"Best,\n"
            f"Sales Development Team"
        )
        self.sequence.append({
            "touchpoint": 4,
            "type": "Email",
            "schedule_date": touch4_date.strftime("%Y-%m-%d"),
            "subject": "Permission to close file?",
            "body": touch4_body,
            "status": "Scheduled"
        })

        return self.sequence

class AISDRAgent:
    def __init__(self, leads: List[Dict[str, Any]]):
        self.leads = leads

    def run_sdr_campaign(self):
        """Runs the SDR campaign: qualifies leads, creates sequences, logs updates, and updates CRM."""
        print("=" * 72)
        print("                 AI SDR v2 - SALES OUTBOUND CAMPAIGN")
        print("=" * 72)

        for lead in self.leads:
            print(f"\n[*] Qualifying Lead: {lead['name']} ({lead['company']}) | Score: {lead['score']}")
            
            # Lead Qualification check gate
            if lead["score"] >= 70:
                print(f"  [+] Lead QUALIFIED. Ingesting to Outbound Sequence Engine...")
                
                # 1. Compile Outbound sequence
                seq_generator = OutboundSequenceGenerator(lead)
                sequence = seq_generator.compile_sequence()
                
                # 2. Simulate CRM Sync
                self._update_crm_stage(lead["lead_id"], "Outbound-In-Sequence")
                self._log_crm_activities(lead["lead_id"], sequence)
                
                # 3. Print Outreach touchpoints
                print(f"  [+] OUTBOUND SEQUENCE PLANNED ({len(sequence)} touchpoints):")
                for touch in sequence:
                    print(f"    - Touch {touch['touchpoint']} | Date: {touch['schedule_date']} | Channel: {touch['type']:<20} | Status: {touch['status']}")
                    print(f"      Subject: {touch['subject']}")
                    # Print body preview
                    body_lines = touch['body'].split('\n')
                    body_preview = body_lines[2] if len(body_lines) > 2 else body_lines[0]
                    print(f"      Preview: {body_preview[:80]}...")
                    print("-" * 50)
            else:
                print(f"  [-] Lead DISQUALIFIED (Score {lead['score']} < 70). Skipping outbound sequence.")

        print("=" * 72)
        print("  [SUCCESS] Outbound GTM Campaign sequence compiles and CRM syncing completed.")
        print("=" * 72)

    def _update_crm_stage(self, lead_id: int, status: str):
        """Simulates updating the lead's stage status in CRM database."""
        print(f"  [CRM UPDATE] Lead ID {lead_id} status transitioned to '{status}' in HubSpot/Salesforce.")

    def _log_crm_activities(self, lead_id: int, sequence: List[Dict[str, Any]]):
        """Simulates logging automated outreach tasks in the CRM activity logs."""
        print(f"  [CRM LOG] Registered {len(sequence)} scheduled tasks under Lead ID {lead_id} CRM timeline.")


if __name__ == "__main__":
    sdr_agent = AISDRAgent(QUALIFIED_LEADS)
    sdr_agent.run_sdr_campaign()
