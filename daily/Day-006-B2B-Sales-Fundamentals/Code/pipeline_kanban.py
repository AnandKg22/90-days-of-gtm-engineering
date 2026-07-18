# B2B Sales Pipeline Kanban Simulator
from typing import List, Dict, Any

# 1. Define Stage Probabilities
STAGE_PROBABILITIES = {
    "Discovery": 0.10,
    "Demo": 0.35,
    "Proposal": 0.60,
    "Legal": 0.85,
    "Won": 1.00,
    "Lost": 0.00
}

class Deal:
    def __init__(self, deal_id: str, name: str, amount: float, stage: str):
        self.deal_id = deal_id
        self.name = name
        self.amount = float(amount)
        self.stage = stage if stage in STAGE_PROBABILITIES else "Discovery"

class KanbanBoard:
    def __init__(self):
        self.deals: Dict[str, Deal] = {}
        
    def add_deal(self, deal_id: str, name: str, amount: float, stage: str = "Discovery"):
        self.deals[deal_id] = Deal(deal_id, name, amount, stage)
        print(f"[NEW DEAL] Created '{name}' (${amount:,.2f}) at stage [{stage}]")
        
    def move_deal(self, deal_id: str, next_stage: str):
        if deal_id not in self.deals:
            print(f"[ERROR] Deal ID {deal_id} not found.")
            return
        if next_stage not in STAGE_PROBABILITIES:
            print(f"[ERROR] Invalid stage: {next_stage}")
            return
            
        old_stage = self.deals[deal_id].stage
        self.deals[deal_id].stage = next_stage
        print(f"[STAGE UPDATE] Deal '{self.deals[deal_id].name}': {old_stage} ===> {next_stage}")
        
    def calculate_forecasts(self) -> Dict[str, float]:
        unweighted_total = 0.0
        weighted_total = 0.0
        
        for deal in self.deals.values():
            unweighted_total += deal.amount
            prob = STAGE_PROBABILITIES[deal.stage]
            weighted_total += deal.amount * prob
            
        return {
            "unweighted_pipeline": unweighted_total,
            "weighted_forecast": weighted_total
        }
        
    def render_board(self):
        print("\n" + "=" * 60)
        print("                 PIPELINE KANBAN BOARD")
        print("=" * 60)
        
        # Group deals by stage
        grouped: Dict[str, List[Deal]] = {stage: [] for stage in STAGE_PROBABILITIES}
        for deal in self.deals.values():
            grouped[deal.stage].append(deal)
            
        # Print list for each stage
        for stage, list_deals in grouped.items():
            prob_percent = int(STAGE_PROBABILITIES[stage] * 100)
            print(f"[{stage.upper()} ({prob_percent}%)]")
            if not list_deals:
                print("  (No active deals)")
            else:
                for d in list_deals:
                    print(f"  - {d.name} (${d.amount:,.2f}) [ID: {d.deal_id}]")
            print("-" * 60)
            
        forecasts = self.calculate_forecasts()
        print(f"Unweighted Gross Pipeline: ${forecasts['unweighted_pipeline']:,.2f}")
        print(f"Weighted Revenue Forecast:  ${forecasts['weighted_forecast']:,.2f}")
        print("=" * 60 + "\n")

if __name__ == "__main__":
    board = KanbanBoard()
    
    # 1. Populate initial deals
    board.add_deal("d_001", "Tolani Maritime Academy", 10000.00, "Discovery")
    board.add_deal("d_002", "AMET University", 20000.00, "Demo")
    board.add_deal("d_003", "IMSGOA Maritime College", 5000.00, "Proposal")
    
    # 2. Render board initial state
    board.render_board()
    
    # 3. Simulate deal progression updates
    print("[*] Simulating deal workflow movements...")
    board.move_deal("d_001", "Proposal")  # Tolani goes to Proposal
    board.move_deal("d_003", "Legal")     # IMSGOA goes to Legal
    board.move_deal("d_002", "Won")       # AMET wins!
    
    # 4. Render updated pipeline and final forecasts
    board.render_board()
