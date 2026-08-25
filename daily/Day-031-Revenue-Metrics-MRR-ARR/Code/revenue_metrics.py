# GTM Revenue Metrics Waterfall Compiler
import sys
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Raw log of subscription contract events
subscription_events = [
    # --- Month 1 (July 2026) ---
    {"customer_id": "cust_01", "event_type": "signup", "mrr_delta": 1000.00, "date": "2026-07-01"},
    {"customer_id": "cust_02", "event_type": "signup", "mrr_delta": 2500.00, "date": "2026-07-05"},
    {"customer_id": "cust_03", "event_type": "signup", "mrr_delta": 1500.00, "date": "2026-07-10"},
    {"customer_id": "cust_01", "event_type": "upgrade", "mrr_delta": 300.00, "date": "2026-07-20"}, # Expansion
    
    # --- Month 2 (August 2026) ---
    {"customer_id": "cust_04", "event_type": "signup", "mrr_delta": 3000.00, "date": "2026-08-01"}, # New
    {"customer_id": "cust_02", "event_type": "downgrade", "mrr_delta": -500.00, "date": "2026-08-10"}, # Contraction
    {"customer_id": "cust_03", "event_type": "cancel", "mrr_delta": -1500.00, "date": "2026-08-15"} # Churn
]

class RevenueWaterfallCompiler:
    def __init__(self, events: List[Dict[str, Any]]):
        self.events = events
        
    def compile_months(self) -> Dict[str, Dict[str, Any]]:
        # 1. Group events by month (YYYY-MM)
        monthly_events: Dict[str, List[Dict[str, Any]]] = {}
        for ev in self.events:
            month_key = ev["date"][:7] # Extracts YYYY-MM
            if month_key not in monthly_events:
                monthly_events[month_key] = []
            monthly_events[month_key].append(ev)
            
        sorted_months = sorted(monthly_events.keys())
        waterfall = {}
        
        starting_mrr = 0.0
        active_customers = set()
        
        for month in sorted_months:
            new_mrr = 0.0
            expansion_mrr = 0.0
            contraction_mrr = 0.0
            churned_mrr = 0.0
            
            month_events = monthly_events[month]
            starting_customers_count = len(active_customers)
            cancelled_customers = 0
            
            for ev in month_events:
                cid = ev["customer_id"]
                delta = ev["mrr_delta"]
                etype = ev["event_type"]
                
                if etype == "signup":
                    new_mrr += delta
                    active_customers.add(cid)
                elif etype == "upgrade":
                    expansion_mrr += delta
                elif etype == "downgrade":
                    # Contraction stored as absolute positive for the waterfall representation
                    contraction_mrr += abs(delta)
                elif etype == "cancel":
                    # Churn stored as absolute positive for the waterfall representation
                    churned_mrr += abs(delta)
                    active_customers.discard(cid)
                    cancelled_customers += 1
                    
            net_new_mrr = new_mrr + expansion_mrr - contraction_mrr - churned_mrr
            ending_mrr = starting_mrr + net_new_mrr
            arr_run_rate = ending_mrr * 12
            
            # Calculate Churn rates
            # Note: Avoid division by zero in Month 1 where Starting MRR/Customers = 0
            customer_churn_rate = (cancelled_customers / max(1, starting_customers_count)) * 100.0 if starting_customers_count > 0 else 0.0
            revenue_churn_rate = (churned_mrr / max(1.0, starting_mrr)) * 100.0 if starting_mrr > 0.0 else 0.0
            
            waterfall[month] = {
                "starting_mrr": starting_mrr,
                "new_mrr": new_mrr,
                "expansion_mrr": expansion_mrr,
                "contraction_mrr": contraction_mrr,
                "churned_mrr": churned_mrr,
                "net_new_mrr": net_new_mrr,
                "ending_mrr": ending_mrr,
                "arr_run_rate": arr_run_rate,
                "customer_churn_rate": customer_churn_rate,
                "revenue_churn_rate": revenue_churn_rate
            }
            
            # Ending MRR becomes Starting MRR of next month
            starting_mrr = ending_mrr
            
        return waterfall

if __name__ == "__main__":
    compiler = RevenueWaterfallCompiler(subscription_events)
    waterfall_data = compiler.compile_months()
    
    print("=" * 65)
    print("             VIVAEXAMS SUBSCRIPTION REVENUE COMPILER")
    print("=" * 65)
    
    for month, metrics in waterfall_data.items():
        print(f"Month Period: {month}")
        print("-" * 65)
        print(f"  (+) Starting MRR:     ${metrics['starting_mrr']:,.2f}")
        print(f"  (+) New MRR:          ${metrics['new_mrr']:,.2f}")
        print(f"  (+) Expansion MRR:    ${metrics['expansion_mrr']:,.2f}")
        print(f"  (-) Contraction MRR:  ${metrics['contraction_mrr']:,.2f}")
        print(f"  (-) Churned MRR:      ${metrics['churned_mrr']:,.2f}")
        print(f"  (=) Net New MRR:      ${metrics['net_new_mrr']:,.2f}")
        print(f"  (=) Ending MRR:       ${metrics['ending_mrr']:,.2f}")
        print(f"  (*) ARR Run Rate:     ${metrics['arr_run_rate']:,.2f}")
        print(f"  (%) Customer Churn:   {metrics['customer_churn_rate']:.1f}%")
        print(f"  (%) Revenue Churn:    {metrics['revenue_churn_rate']:.1f}%")
        
        # Financial Health check warning
        if metrics['revenue_churn_rate'] > 5.0:
            print("  [ALERT] Revenue Churn exceeds 5.0% threshold. Focus on retention!")
        print("=" * 65)
