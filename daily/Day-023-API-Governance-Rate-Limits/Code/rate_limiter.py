# Token Bucket Rate Limiter Simulator
import sys
import time
from typing import Dict, Tuple

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate # tokens per second
        
        # In-memory store: client_id -> (tokens, last_update_timestamp)
        self.buckets: Dict[str, Tuple[float, float]] = {}
        
    def _refill(self, client_id: str, current_time: float) -> Tuple[float, float]:
        if client_id not in self.buckets:
            # First request: initialize bucket to full capacity
            return float(self.capacity), current_time
            
        tokens, last_update = self.buckets[client_id]
        
        # Calculate tokens refilled since last update
        elapsed = current_time - last_update
        refilled_tokens = elapsed * self.refill_rate
        
        # Update tokens, capping at maximum capacity
        new_tokens = min(float(self.capacity), tokens + refilled_tokens)
        return new_tokens, current_time
        
    def allow_request(self, client_id: str) -> Tuple[bool, float, float]:
        now = time.time()
        tokens, last_update = self._refill(client_id, now)
        
        if tokens >= 1.0:
            # Accept Request: consume 1 token
            self.buckets[client_id] = (tokens - 1.0, now)
            return True, tokens - 1.0, 0.0
        else:
            # Reject Request: return False and calculate wait time until next token refill
            self.buckets[client_id] = (tokens, now)
            wait_time = (1.0 - tokens) / self.refill_rate
            return False, tokens, wait_time

if __name__ == "__main__":
    # Capacity = 5, Refill Rate = 2 tokens/sec
    limiter = TokenBucketRateLimiter(capacity=5, refill_rate=2.0)
    client_ip = "192.168.1.50"
    
    print("=" * 65)
    print("             API GATEWAY TOKEN BUCKET RATE LIMITER")
    print("=" * 65)
    print(f"Bucket Capacity: {limiter.capacity} Tokens")
    print(f"Refill Rate:     {limiter.refill_rate} Tokens/Second")
    print("-" * 65)
    
    # 1. Fire a rapid burst of 7 requests (expect first 5 to pass, next 2 to fail)
    print("[BURST 1] Ingesting 7 rapid requests...")
    for i in range(1, 8):
        allowed, tokens_left, wait = limiter.allow_request(client_ip)
        if allowed:
            print(f"  Req {i}: [SUCCESS] HTTP 200 | Tokens Left: {tokens_left:.2f}")
        else:
            print(f"  Req {i}: [REJECTED] HTTP 429 | Too Many Requests | Retry-After: {wait:.2f}s")
        time.sleep(0.05) # Tiny latency between requests
        
    # 2. Wait 1.5 seconds to allow tokens to refill (1.5s * 2/sec = 3 tokens refilled)
    sleep_dur = 1.5
    print(f"\n[*] Waiting {sleep_dur} seconds for token refill...")
    time.sleep(sleep_dur)
    
    # 3. Fire another burst of 4 requests (expect 3 to pass, 4th to fail)
    print("\n[BURST 2] Ingesting 4 requests after refill...")
    for i in range(1, 5):
        allowed, tokens_left, wait = limiter.allow_request(client_ip)
        if allowed:
            print(f"  Req {i}: [SUCCESS] HTTP 200 | Tokens Left: {tokens_left:.2f}")
        else:
            print(f"  Req {i}: [REJECTED] HTTP 429 | Too Many Requests | Retry-After: {wait:.2f}s")
        time.sleep(0.05)
        
    print("=" * 65)
