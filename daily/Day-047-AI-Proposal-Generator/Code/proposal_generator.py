# Day 047: AI Proposal Generator - Proposal Automation Tool
import sys
from typing import Dict, Any, List

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Target customer scenarios for proposal generation
PROPOSAL_SCENARIOS = [
    {
        "company": "Stark Industries",
        "segment": "Enterprise",
        "pain_point": "Lead routing latency causing sales pipeline leakages",
        "wasted_hours_monthly": 120,
        "hourly_labor_rate": 80.0,
        "requested_discount": 0.10, # 10% discount
        "tech_stack": "GCP, Snowflake, Kubernetes"
    },
    {
        "company": "Wayne Enterprises",
        "segment": "Enterprise",
        "pain_point": "Manual CRM-to-billing syncing delayed financial closes",
        "wasted_hours_monthly": 180,
        "hourly_labor_rate": 90.0,
        "requested_discount": 0.25, # 25% discount (Exceeds approval limits)
        "tech_stack": "AWS, Salesforce, Oracle Financials"
    },
    {
        "company": "Cyberdyne Systems",
        "segment": "Mid-Market",
        "pain_point": "Inaccurate lead scoring and poor qualification rules",
        "wasted_hours_monthly": 50,
        "hourly_labor_rate": 65.0,
        "requested_discount": 0.0, # No discount
        "tech_stack": "AWS, React, PostgreSQL"
    }
]

class ProposalGenerator:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.company = data["company"]
        self.segment = data["segment"]
        
        # Financial variables
        self.wasted_hours = data["wasted_hours_monthly"]
        self.labor_rate = data["hourly_labor_rate"]
        self.discount = data["requested_discount"]

    def generate_proposal(self) -> str:
        """Assembles dynamic sections, pricing grids, ROI math, and approval statuses into a proposal."""
        # 1. Calculate Pricing
        base_license, implementation, final_total = self._calculate_contract_pricing()
        
        # 2. Calculate ROI Projections
        annual_loss, net_savings, roi_percent = self._calculate_roi(final_total)
        
        # 3. Generate Scope of Work (SOW)
        sow = self._generate_scope_of_work()
        
        # 4. Check Approval Workflow Status
        approval_status = self._check_approval_workflow()

        # Compile Proposal document
        proposal = (
            f"========================================================================\n"
            f"             GTM BUSINESS PROPOSAL: {self.company.upper()}\n"
            f"========================================================================\n"
            f" 📌 EXECUTIVE OVERVIEW\n"
            f"   This proposal outlines the deployment of the GTM Revenue Automation\n"
            f"   platform to resolve {self.company}'s critical operational pain point:\n"
            f"   \"{self.data['pain_point']}\".\n\n"
            f" 🛡️ SCOPE OF WORK (SOW)\n"
            f"{sow}\n"
            f" 💰 COMMERCIAL TERMS & CONTRACT PRICING\n"
            f"   - Segment Tier:           {self.segment}\n"
            f"   - Base Software License:  ${base_license:,.2f}/year\n"
            f"   - Implementation Setup:   ${implementation:,.2f} (one-time)\n"
            f"   - Applied Discount:       {self.discount * 100:.1f}%\n"
            f"   - TOTAL CONTRACT VALUE:   ${final_total:,.2f}/year\n\n"
            f" 📈 FINANCIAL ROI & VALUE MODEL\n"
            f"   - Current Operational Loss: ${annual_loss:,.2f}/year\n"
            f"     (Based on {self.wasted_hours} wasted hours/month at ${self.labor_rate}/hr)\n"
            f"   - Software Cost (Year 1):  ${final_total:,.2f}\n"
            f"   - Projected Net Savings:   ${net_savings:,.2f} in Year 1\n"
            f"   - CUSTOMER ROI ESTIMATED:   {roi_percent:,.1f}% ROI\n\n"
            f" 📝 PROPOSAL APPROVAL STATUS\n"
            f"   - Status:                 {approval_status}\n"
            f"========================================================================"
        )
        return proposal

    def _calculate_contract_pricing(self) -> Tuple[float, float, float]:
        """Determines baseline contract numbers based on GTM company tiers."""
        if self.segment == "Enterprise":
            base_license = 95000.0
            implementation = 15000.0
        else:
            base_license = 45000.0
            implementation = 7500.0
            
        subtotal = base_license + implementation
        final_total = subtotal * (1.0 - self.discount)
        return base_license, implementation, final_total

    def _calculate_roi(self, contract_cost: float) -> Tuple[float, float, float]:
        """Calculates operational losses and software savings return percentages."""
        # Monthly loss * 12 months
        annual_loss = (self.wasted_hours * self.labor_rate) * 12
        net_savings = annual_loss - contract_cost
        
        # ROI % = (Net Savings / Software Cost) * 100
        roi_percent = (net_savings / contract_cost) * 100 if contract_cost > 0 else 0
        return annual_loss, net_savings, roi_percent

    def _generate_scope_of_work(self) -> str:
        """Generates dynamic scope of work steps based on tech stack inputs."""
        stack = self.data["tech_stack"]
        sow = (
            f"   * Phase 1: API Configuration & Connection\n"
            f"     - Establish communication boundaries between our engine and {stack}.\n"
            f"   * Phase 2: CRM & Database Schema Mapping\n"
            f"     - Map contact fields, lead status parameters, and sync routes.\n"
            f"   * Phase 3: Parallel Shadow Testing\n"
            f"     - Run integrations in shadow mode for 14 days to verify data integrity."
        )
        return sow

    def _check_approval_workflow(self) -> str:
        """Evaluates discount compliance thresholds to route approval processes."""
        if self.discount > 0.20:
            return f"PENDING VP APPROVAL (Requested discount of {self.discount*100:.1f}% exceeds 20.0% limit)"
        elif self.discount > 0.0:
            return f"APPROVED BY SALES DIRECTOR (Discount of {self.discount*100:.1f}% within compliance scope)"
        else:
            return "AUTO-APPROVED (Standard pricing applied)"


if __name__ == "__main__":
    print("=" * 72)
    print("                 AI PROPOSAL GENERATION DISPATCHER")
    print("=" * 72)

    for scenario in PROPOSAL_SCENARIOS:
        generator = ProposalGenerator(scenario)
        proposal_doc = generator.generate_proposal()
        print(proposal_doc)
        print("\n\n")
