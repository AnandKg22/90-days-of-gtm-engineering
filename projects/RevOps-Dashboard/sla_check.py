# SLA Response Checker
import datetime

class SLAMonitor:
    def __init__(self, limit_minutes: int = 15):
        self.limit = limit_minutes
        
    def check_leads(self, assigned_leads: list):
        now = datetime.datetime.now()
        for lead in assigned_leads:
            elapsed = now - lead['assigned_time']
            elapsed_minutes = elapsed.total_seconds() / 60.0
            
            if elapsed_minutes > self.limit and not lead['responded']:
                print(f"[SLA BREACH ALERT] Lead {lead['email']} has received no response for {int(elapsed_minutes)} mins!")
            else:
                print(f"[OK] Lead {lead['email']} is inside SLA window.")

if __name__ == "__main__":
    monitor = SLAMonitor(15)
    mock_leads = [
        {"email": "userA@test.com", "assigned_time": datetime.datetime.now() - datetime.timedelta(minutes=5), "responded": False},
        {"email": "userB@test.com", "assigned_time": datetime.datetime.now() - datetime.timedelta(minutes=20), "responded": False}
    ]
    monitor.check_leads(mock_leads)
