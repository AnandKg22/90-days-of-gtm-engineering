# SaaS Metrics Calculator & Revenue Dashboard Engine
from typing import List, Dict, Any

# 1. Define customer data structures using standard python classes
class CustomerRecord:
    def __init__(self, id: int, name: str, mrr: float, cac: float, status: str):
        self.id = id
        self.name = name
        self.mrr = float(mrr)
        self.cac = float(cac)
        self.status = str(status)

class SaaSMetrics:
    def __init__(self, total_customers: int, active_customers: int, churned_customers: int,
                 mrr: float, arr: float, avg_cac: float, churn_rate_percent: float,
                 ltv: float, ltv_to_cac_ratio: float, payback_period_months: float):
        self.total_customers = total_customers
        self.active_customers = active_customers
        self.churned_customers = churned_customers
        self.mrr = mrr
        self.arr = arr
        self.avg_cac = avg_cac
        self.churn_rate_percent = churn_rate_percent
        self.ltv = ltv
        self.ltv_to_cac_ratio = ltv_to_cac_ratio
        self.payback_period_months = payback_period_months

# 2. Mock dataset representing early GTM sales data
sample_customers = [
    {"id": 1, "name": "Tolani Maritime Institute", "mrr": 800.00, "cac": 2000.00, "status": "Active"},
    {"id": 2, "name": "AMET University", "mrr": 1200.00, "cac": 3000.00, "status": "Active"},
    {"id": 3, "name": "IMSGOA Maritime College", "mrr": 500.00, "cac": 1500.00, "status": "Active"},
    {"id": 4, "name": "SeaCadets Academy", "mrr": 300.00, "cac": 1000.00, "status": "Churned"},
    {"id": 5, "name": "Marina Training Corp", "mrr": 600.00, "cac": 1800.00, "status": "Active"},
    {"id": 6, "name": "Oceanic Systems", "mrr": 400.00, "cac": 1200.00, "status": "Active"},
    {"id": 7, "name": "Pacific Navigation School", "mrr": 500.00, "cac": 1600.00, "status": "Churned"},
    {"id": 8, "name": "Ganges Shipping Institute", "mrr": 900.00, "cac": 2500.00, "status": "Active"},
    {"id": 9, "name": "Global Port Services", "mrr": 700.00, "cac": 2100.00, "status": "Active"},
    {"id": 10, "name": "Lighthouse Maritime", "mrr": 400.00, "cac": 1400.00, "status": "Active"}
]

# 3. Calculation Engine
def calculate_saas_metrics(records: List[CustomerRecord], gross_margin: float = 0.80) -> SaaSMetrics:
    total_cust = len(records)
    active_cust = sum(1 for c in records if c.status == "Active")
    churn_cust = sum(1 for c in records if c.status == "Churned")
    
    # Financial metrics
    active_mrr = sum(c.mrr for c in records if c.status == "Active")
    active_arr = active_mrr * 12
    total_cac = sum(c.cac for c in records)
    avg_cac = total_cac / total_cust if total_cust > 0 else 0.0
    
    # Rates
    churn_rate = (churn_cust / total_cust) if total_cust > 0 else 0.0
    avg_arpu = active_mrr / active_cust if active_cust > 0 else 0.0
    
    # LTV: ARPU * Gross Margin / Churn Rate
    # Set fallback if churn rate is 0 to avoid zero division
    effective_churn = churn_rate if churn_rate > 0 else 0.01 
    ltv = (avg_arpu * gross_margin) / effective_churn
    
    # Ratios
    ltv_to_cac = ltv / avg_cac if avg_cac > 0 else 0.0
    payback_period = avg_cac / (avg_arpu * gross_margin) if avg_arpu > 0 else 0.0
    
    return SaaSMetrics(
        total_customers=total_cust,
        active_customers=active_cust,
        churned_customers=churn_cust,
        mrr=active_mrr,
        arr=active_arr,
        avg_cac=avg_cac,
        churn_rate_percent=churn_rate * 100,
        ltv=ltv,
        ltv_to_cac_ratio=ltv_to_cac,
        payback_period_months=payback_period
    )

if __name__ == "__main__":
    # Validate records
    validated_records = [
        CustomerRecord(c["id"], c["name"], c["mrr"], c["cac"], c["status"]) 
        for c in sample_customers
    ]
    metrics = calculate_saas_metrics(validated_records)
    
    # Render Dashboard
    print("=" * 50)
    print("       VIVAEXAMS EXECUTIVE REVENUE DASHBOARD")
    print("=" * 50)
    print(f"Total Customer Accounts:  {metrics.total_customers}")
    print(f"Active Subscriptions:    {metrics.active_customers}  | Churned: {metrics.churned_customers}")
    print(f"Logo Churn Rate:         {metrics.churn_rate_percent:.2f}%")
    print("-" * 50)
    print(f"Monthly Recurring (MRR): ${metrics.mrr:,.2f}")
    print(f"Annual Recurring (ARR):  ${metrics.arr:,.2f}")
    print("-" * 50)
    print(f"Average Account CAC:     ${metrics.avg_cac:,.2f}")
    print(f"Customer Lifetime Value: ${metrics.ltv:,.2f}")
    print(f"LTV : CAC Ratio:         {metrics.ltv_to_cac_ratio:.2f}x  (Target: > 3.0x)")
    print(f"CAC Payback Period:      {metrics.payback_period_months:.2f} Months")
    print("=" * 50)
