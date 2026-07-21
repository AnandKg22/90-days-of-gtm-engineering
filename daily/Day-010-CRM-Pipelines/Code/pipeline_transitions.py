# Pipeline Velocity & Currency Converter Engine
import time
import datetime
from typing import List, Dict, Any

# 1. Exchange rates to base USD
EXCHANGE_RATES = {
    "USD": 1.0000,
    "INR": 0.0120,
    "SGD": 0.7400
}

class StageHistoryEntry:
    def __init__(self, stage_name: str):
        self.stage_name = stage_name
        self.entered_at = time.time()
        self.exited_at = None
        
    def get_duration(self) -> float:
        if not self.exited_at:
            return time.time() - self.entered_at
        return self.exited_at - self.entered_at

class DealRecord:
    def __init__(self, deal_id: str, name: str, local_amount: float, currency_code: str):
        self.deal_id = deal_id
        self.name = name
        self.local_amount = float(local_amount)
        self.currency_code = currency_code if currency_code in EXCHANGE_RATES else "USD"
        self.stage = "Discovery"
        
        # Chronological log of stage entries
        self.history: List[StageHistoryEntry] = [StageHistoryEntry("Discovery")]
        
    def get_amount_usd(self) -> float:
        return self.local_amount * EXCHANGE_RATES[self.currency_code]
        
    def transition_to(self, next_stage: str):
        # 1. Exit current active stage
        if self.history:
            self.history[-1].exited_at = time.time()
            
        old_stage = self.stage
        self.stage = next_stage
        
        # 2. Enter next stage
        self.history.append(StageHistoryEntry(next_stage))
        print(f"[TRANSITION] Deal '{self.name}': {old_stage} ===> {next_stage}")

if __name__ == "__main__":
    print("=" * 65)
    print("        INITIALIZING PIPELINE VELOCITY & CURRENCY RUN")
    print("=" * 65)
    
    # 1. Initialize Deals in local currencies
    deal1 = DealRecord("d_01", "Tolani Cadet Licenses", 830000.00, "INR") # ~$9,960 USD
    deal2 = DealRecord("d_02", "Singapore Campus Deal", 13500.00, "SGD")   # ~$9,990 USD
    
    print(f"Deal 1: {deal1.name} | Local: {deal1.currency_code} {deal1.local_amount:,.2f} | USD: ${deal1.get_amount_usd():,.2f}")
    print(f"Deal 2: {deal2.name} | Local: {deal2.currency_code} {deal2.local_amount:,.2f} | USD: ${deal2.get_amount_usd():,.2f}")
    print("-" * 65)
    
    # 2. Simulate Stage Transitions over time
    print("[*] Simulating pipeline deal progression...")
    
    # Deal 1 spends 1.5 seconds in Discovery, then moves to Proposal
    time.sleep(1.5) 
    deal1.transition_to("Proposal")
    
    # Deal 2 spends 1.0 second in Discovery, then moves to Demo
    time.sleep(1.0)
    deal2.transition_to("Demo")
    
    # Deal 1 spends 2.0 seconds in Proposal, then wins!
    time.sleep(2.0)
    deal1.transition_to("Won")
    
    # 3. Print Pipeline Velocity Analytics
    print("\n" + "=" * 65)
    print("               PIPELINE STAGE VELOCITY REPORT")
    print("=" * 65)
    
    for deal in [deal1, deal2]:
        print(f"\\nDeal: '{deal.name}' | Total Value: ${deal.get_amount_usd():,.2f} USD")
        print("Stage Duration Log:")
        for entry in deal.history:
            duration = entry.get_duration()
            status = "Completed" if entry.exited_at else "Active (Current)"
            print(f"  - Stage: {entry.stage_name:<12} | Duration: {duration:.2f}s | Status: {status}")
            
    print("=" * 65)
