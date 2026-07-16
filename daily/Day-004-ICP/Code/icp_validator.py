# GTM Lead Qualification - ICP Validator
from typing import List, Dict, Any

class CompanyProfile:
    def __init__(self, name: str, industry: str, employee_count: int, country: str, tech_stack: List[str]):
        self.name = name
        self.industry = industry
        self.employee_count = employee_count
        self.country = country
        self.tech_stack = tech_stack

class ICPFilter:
    def __init__(self, target_industries: List[str], min_employees: int, max_employees: int,
                 target_countries: List[str], target_technologies: List[str]):
        self.target_industries = target_industries
        self.min_employees = min_employees
        self.max_employees = max_employees
        self.target_countries = target_countries
        self.target_technologies = target_technologies

class ICPValidator:
    def __init__(self, icp: ICPFilter):
        self.icp = icp
        
    def evaluate_company(self, company: CompanyProfile) -> Dict[str, Any]:
        score = 0.0
        details = {}
        
        # 1. Industry Check (35 Points Max)
        if company.industry in self.icp.target_industries:
            score += 35.0
            details["industry_match"] = "Exact Match (+35)"
        else:
            details["industry_match"] = "No Match (+0)"
            
        # 2. Company Size Check (25 Points Max)
        if self.icp.min_employees <= company.employee_count <= self.icp.max_employees:
            score += 25.0
            details["size_match"] = "Perfect Size (+25)"
        elif company.employee_count >= (self.icp.min_employees / 2):
            score += 10.0
            details["size_match"] = "Near Target (+10)"
        else:
            details["size_match"] = "Out of Range (+0)"
            
        # 3. Technographics Check (20 Points Max)
        matched_tech = set(company.tech_stack).intersection(set(self.icp.target_technologies))
        if matched_tech:
            # Score matches proportionally
            tech_score = min(len(matched_tech) * 10.0, 20.0)
            score += tech_score
            details["tech_match"] = f"Matches {list(matched_tech)} (+{int(tech_score)})"
        else:
            details["tech_match"] = "No Target Tech (+0)"
            
        # 4. Geography Check (20 Points Max)
        if company.country in self.icp.target_countries:
            score += 20.0
            details["country_match"] = "Target Country (+20)"
        else:
            details["country_match"] = "Out of Territory (+0)"
            
        # Determine Fit Tier
        if score >= 75.0:
            fit_tier = "High Fit"
        elif score >= 40.0:
            fit_tier = "Medium Fit"
        else:
            fit_tier = "Low Fit"
            
        return {
            "score": score,
            "fit_tier": fit_tier,
            "details": details
        }

# Define Target B2B ICP for VivaExams
viva_exams_icp = ICPFilter(
    target_industries=["Maritime Education", "Marine College", "Maritime Academy"],
    min_employees=50,
    max_employees=300,
    target_countries=["IN", "SG", "AE"],
    target_technologies=["Moodle", "Blackboard", "Stripe"]
)

# Mock incoming leads
leads_to_score = [
    CompanyProfile("Tolani Maritime Academy", "Maritime Academy", 120, "IN", ["Moodle", "React"]), # High Fit
    CompanyProfile("Global Shipping Corp", "Maritime Shipping", 800, "SG", ["Stripe", "Docker"]), # Medium Fit (Size too large, industry wrong)
    CompanyProfile("IMSGOA Marine College", "Marine College", 65, "IN", ["Stripe", "Moodle"]), # High Fit
    CompanyProfile("Acme Software Inc", "Tech SaaS", 25, "US", ["AWS", "Postgres"]) # Low Fit
]

if __name__ == "__main__":
    validator = ICPValidator(viva_exams_icp)
    
    print("=" * 65)
    print("             VIVAEXAMS LEAD QUALIFICATION ENGINE")
    print("=" * 65)
    
    for lead in leads_to_score:
        result = validator.evaluate_company(lead)
        print(f"\\nCompany:       {lead.name}")
        print(f"Industry:      {lead.industry}  | Location: {lead.country}")
        print(f"Employee Size: {lead.employee_count}")
        print(f"Qual Score:    {result['score']} / 100")
        print(f"Fit Tier:      [{result['fit_tier'].upper()}]")
        print(f"Match Log:     {result['details']}")
        print("-" * 65)
    print("=" * 65)
