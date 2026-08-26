# GTM Cohort NDR & GRR Calculator
import sys
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Mock Cohort Dataset: 12-month contract snapshots (Jan 2025 vs Jan 2026)
cohort_contract_data = [
    {"company_id": 101, "name": "Tolani Maritime Institute", "start_mrr": 5000.00, "end_mrr": 8000.00},  # Expansion (+$3000)
    {"company_id": 102, "name": "IMSGOA Maritime College", "start_mrr": 2000.00, "end_mrr": 2000.00},   # Flat
    {"company_id": 103, "name": "AMET University", "start_mrr": 15000.00, "end_mrr": 12000.00},        # Contraction (-$3000)
    {"company_id": 104, "name": "Global Shipping Corp", "start_mrr": 8000.00, "end_mrr": 0.00},         # Churned (-$8000)
    {"company_id": 105, "name": "Marine Academy Asia", "start_mrr": 10000.00, "end_mrr": 12000.00},     # Expansion (+$2000)
    {"company_id": 106, "name": "Pacific Transit Inc", "start_mrr": 4000.00, "end_mrr": 0.00},          # Churned (-$4000)
    {"company_id": 107, "name": "Singapore Cadet School", "start_mrr": 6000.00, "end_mrr": 9000.00}     # Expansion (+$3000)
]

class CohortRetentionCalculator:
    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data
        
    def compile_cohort_report(self) -> Dict[str, Any]:
        start_mrr_total = 0.0
        end_mrr_total = 0.0
        
        expansion_total = 0.0
        contraction_total = 0.0
        churn_total = 0.0
        
        for record in self.data:
            s_mrr = record["start_mrr"]
            e_mrr = record["end_mrr"]
            
            start_mrr_total += s_mrr
            end_mrr_total += e_mrr
            
            if e_mrr > s_mrr:
                # Upgraded
                expansion_total += (e_mrr - s_mrr)
            elif e_mrr == 0.0:
                # Cancelled
                churn_total += s_mrr
            elif e_mrr < s_mrr:
                # Downgraded
                contraction_total += (s_mrr - e_mrr)
                
        # Calculate Ratios
        ndr = (end_mrr_total / start_mrr_total) * 100.0
        grr = ((start_mrr_total - contraction_total - churn_total) / start_mrr_total) * 100.0
        
        return {
            "start_mrr": start_mrr_total,
            "end_mrr": end_mrr_total,
            "expansion": expansion_total,
            "contraction": contraction_total,
            "churn": churn_total,
            "ndr": ndr,
            "grr": grr
        }

if __name__ == "__main__":
    calculator = CohortRetentionCalculator(cohort_contract_data)
    report = calculator.compile_cohort_report()
    
    print("=" * 65)
    print("             VIVAEXAMS COHORT REVENUE RETENTION ENGINE")
    print("=" * 65)
    print(f"Total Cohort Customers:   {len(cohort_contract_data)}")
    print(f"Starting Cohort MRR:      ${report['start_mrr']:,.2f}")
    print(f"Ending Cohort MRR:        ${report['end_mrr']:,.2f}")
    print("-" * 65)
    print(f"  (+) Expansion MRR:      ${report['expansion']:,.2f}")
    print(f"  (-) Contraction MRR:    ${report['contraction']:,.2f}")
    print(f"  (-) Churned MRR:        ${report['churn']:,.2f}")
    print("-" * 65)
    print(f"  (=) Net Dollar Retention (NDR):   {report['ndr']:.1f}%")
    print(f"  (=) Gross Dollar Retention (GRR): {report['grr']:.1f}%")
    print("-" * 65)
    
    # Audit alerts
    print("COHORT HEALTH AUDIT LOG:")
    if report["ndr"] >= 100.0:
        print("  [SUCCESS] NDR is healthy (>= 100.0%). Net negative churn achieved.")
    else:
        print("  [WARNING] NDR is failing (< 100.0%). Churn outpaces upsell expansions.")
        
    if report["grr"] >= 80.0:
        print("  [SUCCESS] GRR is stable (>= 80.0%). Baseline retention is secure.")
    else:
        print("  [CRITICAL] GRR is unstable (< 80.0%). Baseline customer retention is failing.")
    print("=" * 65)
