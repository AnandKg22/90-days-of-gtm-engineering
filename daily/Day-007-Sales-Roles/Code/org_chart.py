# Sales Organization Hand-off Tracker
import datetime
from typing import List, Dict, Any

class TeamMember:
    def __init__(self, name: str, role: str, email: str):
        self.name = name
        self.role = role # SDR, AE, CSM
        self.email = email

class LeadRecord:
    def __init__(self, lead_id: str, name: str, sdr: TeamMember, ae: TeamMember, csm: TeamMember):
        self.lead_id = lead_id
        self.name = name
        self.sdr = sdr
        self.ae = ae
        self.csm = csm
        self.current_owner = sdr # Starts with SDR
        self.stage = "Lead Intake"
        self.hand_off_history: List[str] = []
        
    def log_event(self, description: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {description}"
        self.hand_off_history.append(log_entry)
        print(log_entry)

class HandOffPipeline:
    def __init__(self):
        pass
        
    def qualify_lead(self, lead: LeadRecord, notes: str):
        print(f"\\n[*] Qualify Lead: '{lead.name}' by SDR {lead.sdr.name}")
        lead.current_owner = lead.ae
        lead.stage = "Meeting Booked"
        event_desc = (f"SDR Hand-off to AE: Lead qualified. Ownership transferred from "
                      f"{lead.sdr.name} ({lead.sdr.role}) to {lead.ae.name} ({lead.ae.role}). "
                      f"Qualification Notes: '{notes}'")
        lead.log_event(event_desc)
        
        # Mock Notification
        print(f"  [SLACK AE ALERT] To: {lead.ae.name} | Hubspot Deal created for '{lead.name}'. "
              f"Meeting scheduled. Notes: {notes}")
        
    def close_won_deal(self, lead: LeadRecord, contract_val: float):
        print(f"\\n[*] Close Deal: '{lead.name}' by AE {lead.ae.name}")
        lead.current_owner = lead.csm
        lead.stage = "Closed Won"
        event_desc = (f"AE Hand-off to CS: Opportunity won (${contract_val:,.2f}). "
                      f"Ownership transferred from {lead.ae.name} ({lead.ae.role}) to "
                      f"{lead.csm.name} ({lead.csm.role}).")
        lead.log_event(event_desc)
        
        # Mock Notification
        print(f"  [SLACK CS ALERT] To: {lead.csm.name} | Account '{lead.name}' is Won. "
              f"CSM assigned. Please schedule kickoff. Contract: ${contract_val:,.2f}")
        print(f"  [EMAIL CUSTOMER] To: {lead.name} Admin | Welcome to VivaExams! Onboarding initiated.")

if __name__ == "__main__":
    # 1. Define Commercial Org Structure
    sdr_rep = TeamMember("Rohit", "SDR", "rohit@vivaexams.com")
    ae_rep = TeamMember("Sarah", "AE", "sarah@vivaexams.com")
    csm_rep = TeamMember("Amit", "CSM", "amit@vivaexams.com")
    
    # 2. Initialize Prospect Lead
    lead = LeadRecord(
        lead_id="l_7701", 
        name="Tolani Maritime Institute", 
        sdr=sdr_rep, 
        ae=ae_rep, 
        csm=csm_rep
    )
    
    print("=" * 65)
    print("             VIVAEXAMS SALES HAND-OFF PIPELINE")
    print("=" * 65)
    print(f"Lead Created:   {lead.name}")
    print(f"Initial Owner:  {lead.current_owner.name} ({lead.current_owner.role})")
    print(f"Stage:          {lead.stage}")
    print("-" * 65)
    
    # Run pipeline transitions
    pipeline = HandOffPipeline()
    
    # SDR Qualifies and books demo
    pipeline.qualify_lead(lead, "Wants bulk mock test licenses for 600 marine cadets.")
    
    # AE runs demo, negotiates, and closes deal
    pipeline.close_won_deal(lead, 8000.00)
    
    print("\\n" + "=" * 65)
    print("                 FINAL HAND-OFF LOG SUMMARY")
    print("=" * 65)
    print(f"Prospect:      {lead.name}")
    print(f"Final Stage:    {lead.stage}")
    print(f"Active Owner:   {lead.current_owner.name} ({lead.current_owner.role})")
    print("\\nFull Pipeline Audit Trail:")
    for entry in lead.hand_off_history:
        print(f"  {entry}")
    print("=" * 65)
