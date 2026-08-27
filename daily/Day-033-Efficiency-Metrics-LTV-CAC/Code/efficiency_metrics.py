# GTM LTV:CAC & Payback Calculator
import sys
from typing import List, Dict, Any

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Marketing Campaign Spend Logs
marketing_spend_data = [
    {"channel": "google", "amount_spent": 12000.00},
    {"channel": "linkedin", "amount_spent": 20000.00},
    {"channel": "email", "amount_spent": 1500.00}
]

# Won Accounts Details (Annual Values)
won_accounts_data = [
    # Google Acquisitions (4 customers)
    {"customer_id": "cust_g1", "annual_value": 10000.00, "channel": "google"},
    {"customer_id": "cust_g2", "annual_value": 12000.00, "channel": "google"},
    {"customer_id": "cust_g3", "annual_value": 8000.00, "channel": "google"},
    {"customer_id": "cust_g4", "annual_value": 6000.00, "channel": "google"},
    
    # LinkedIn Acquisitions (2 customers)
    {"customer_id": "cust_l1", "annual_value": 25000.00, "channel": "linkedin"},
    {"customer_id": "cust_l2", "annual_value": 30000.00, "channel": "linkedin"},
    
    # Email Acquisitions (5 customers)
    {"customer_id": "cust_e1", "annual_value": 2000.00, "channel": "email"},
    {"customer_id": "cust_e2", "annual_value": 3000.00, "channel": "email"},
    {"customer_id": "cust_e3", "annual_value": 1500.00, "channel": "email"},
    {"customer_id": "cust_e4", "annual_value": 2500.00, "channel": "email"},
    {"customer_id": "cust_e5", "annual_value": 1000.00, "channel": "email"}
]

class GTMEfficiencyCalculator:
    def __init__(self, spend: List[Dict[str, Any]], accounts: List[Dict[str, Any]]):
        self.spend = spend
        self.accounts = accounts
        
    def compile_channels_report(self) -> Dict[str, Dict[str, Any]]:
        # Constant SaaS factors
        gross_margin = 0.80
        annual_churn_rate = 0.12 # 12% churn
        
        # 1. Aggregate Spend by channel
        spend_totals = {}
        for s in self.spend:
            spend_totals[s["channel"]] = s["amount_spent"]
            
        # 2. Group Won values by channel
        channel_data = {}
        for acct in self.accounts:
            ch = acct["channel"]
            val = acct["annual_value"]
            if ch not in channel_data:
                channel_data[ch] = {"count": 0, "total_value": 0.0}
            channel_data[ch]["count"] += 1
            channel_data[ch]["total_value"] += val
            
        # 3. Calculate metrics per channel
        report = {}
        for ch, data in channel_data.items():
            count = data["count"]
            total_val = data["total_value"]
            spend_val = spend_totals.get(ch, 0.0)
            
            avg_acv = total_val / count
            avg_mrr = avg_acv / 12.0
            
            # CAC = total spend / customer count
            cac = spend_val / count
            
            # LTV = ACV * margin / churn
            ltv = (avg_acv * gross_margin) / annual_churn_rate
            
            # LTV:CAC Ratio
            ltv_cac_ratio = ltv / max(1.0, cac)
            
            # Payback = CAC / (MRR * margin)
            payback_months = cac / (avg_mrr * gross_margin)
            
            report[ch] = {
                "spend": spend_val,
                "acquisitions": count,
                "cac": cac,
                "acv": avg_acv,
                "ltv": ltv,
                "ratio": ltv_cac_ratio,
                "payback": payback_months
            }
        return report

if __name__ == "__main__":
    calculator = GTMEfficiencyCalculator(marketing_spend_data, won_accounts_data)
    channel_report = calculator.compile_channels_report()
    
    print("=" * 65)
    print("             VIVAEXAMS GTM ACQUISITION EFFICIENCY ENGINE")
    print("=" * 65)
    
    print(f"{'Channel':<10} | {'Spend':<9} | {'Acq':<3} | {'CAC':<9} | {'LTV':<10} | {'Ratio':<5} | {'Payback':<7}")
    print("-" * 65)
    for ch, metrics in channel_report.items():
        print(f"{ch:<10} | "
              f"${metrics['spend']:<8,.0f} | "
              f"{metrics['acquisitions']:<3} | "
              f"${metrics['cac']:<8,.0f} | "
              f"${metrics['ltv']:<9,.0f} | "
              f"{metrics['ratio']:>4.1f}x | "
              f"{metrics['payback']:>5.1f}m")
    print("-" * 65)
    
    # Audit Analysis Warnings
    print("ACQUISITION CHANNELS ROI REPORT:")
    for ch, metrics in channel_report.items():
        print(f"  * Channel '{ch}':")
        if metrics["ratio"] >= 3.0:
            print(f"    - [SUCCESS] LTV:CAC is healthy ({metrics['ratio']:.1f}x).")
        else:
            print(f"    - [WARNING] LTV:CAC is unprofitable ({metrics['ratio']:.1f}x). Reduce budget allocation.")
            
        if metrics["payback"] <= 12.0:
            print(f"    - [SUCCESS] Payback is fast ({metrics['payback']:.1f} months). Low cash flow risk.")
        else:
            print(f"    - [WARNING] Payback is slow ({metrics['payback']:.1f} months). Cash flow risk exceeded.")
        print("    " + "." * 55)
    print("=" * 65)
