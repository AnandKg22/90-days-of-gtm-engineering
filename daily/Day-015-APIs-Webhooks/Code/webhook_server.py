# Lightweight Webhook HTTP Receiver Server
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

# Ensure UTF-8 output formatting for terminal compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SHARED_SECRET = "vivaexams_secret_token_1120"

class WebhookReceiverHandler(BaseHTTPRequestHandler):
    # Overriding log_message to prevent console clutter during testing
    def log_message(self, format, *args):
        pass

    def do_POST(self):
        # 1. Route validation
        if self.path != "/webhook":
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode("utf-8"))
            return
            
        # 2. Security token validation
        secret_header = self.headers.get("X-Webhook-Secret")
        if secret_header != SHARED_SECRET:
            self.send_response(401)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Unauthorized: Invalid secret token"}).encode("utf-8"))
            return
            
        # 3. Read raw body payload
        content_length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(content_length)
        
        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except Exception:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Malformed JSON payload"}).encode("utf-8"))
            return
            
        # 4. Process event metadata
        event_name = payload.get("event_name", "unknown")
        data = payload.get("data", {})
        
        print(f"\n[INBOUND WEBHOOK RECEIVED]")
        print(f"  Event Name: {event_name}")
        print(f"  Data Payload: {json.dumps(data)}")
        
        # 5. Return success acknowledgement
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "event_processed", "received": True}).encode("utf-8"))

def run_server(port=8080):
    server_address = ("", port)
    httpd = HTTPServer(server_address, WebhookReceiverHandler)
    print(f"[*] Webhook server listening on port {port}... Press Ctrl+C to exit.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Shutting down webhook server.")
        httpd.server_close()

# 6. Test framework to execute handler logic in script run (preventing lock blocking)
def run_internal_unit_test():
    print("=" * 65)
    print("           WEBHOOK RECEIVER API TEST SUITE")
    print("=" * 65)
    
    # Simulating BaseHTTPRequestHandler operations internally
    import io
    
    class MockRequest:
        def __init__(self, body_bytes, headers_dict, path="/webhook"):
            self.body = io.BytesIO(body_bytes)
            self.headers = headers_dict
            self.path = path
        def makefile(self, *args, **kwargs):
            return self.body

    # Test Case 1: Send valid payload with correct secret key
    print("[TEST 1] Sending valid payload with correct secret key...")
    payload = {"event_name": "stripe.payment_intent.succeeded", "data": {"amount": 8000.00, "customer": "dean@imsgoa.org"}}
    body_data = json.dumps(payload).encode("utf-8")
    
    headers = {
        "X-Webhook-Secret": SHARED_SECRET,
        "Content-Length": str(len(body_data)),
        "Content-Type": "application/json"
    }
    
    # Mocking standard handler connection variables
    class TestHandler(WebhookReceiverHandler):
        def __init__(self, request, client_address, server):
            self.request = request
            self.client_address = client_address
            self.server = server
            self.headers = request.headers
            self.path = request.path
            self.rfile = request.makefile()
            self.wfile = io.BytesIO()
            self.response_code = None
            self.response_headers = {}
            
        def send_response(self, code, message=None):
            self.response_code = code
        def send_header(self, keyword, value):
            self.response_headers[keyword] = value
        def end_headers(self):
            pass

    mock_req = MockRequest(body_data, headers)
    handler = TestHandler(mock_req, ("127.0.0.1", 1234), None)
    handler.do_POST()
    
    print(f"  Result Code:   {handler.response_code}")
    print(f"  Result Headers: {handler.response_headers}")
    print(f"  Result Body:    {handler.wfile.getvalue().decode('utf-8')}")
    print("-" * 65)

    # Test Case 2: Send request with invalid secret key
    print("[TEST 2] Sending request with invalid secret key...")
    mock_req_invalid = MockRequest(body_data, {"X-Webhook-Secret": "invalid_key"})
    handler_invalid = TestHandler(mock_req_invalid, ("127.0.0.1", 1234), None)
    handler_invalid.do_POST()
    
    print(f"  Result Code:   {handler_invalid.response_code}")
    print(f"  Result Body:    {handler_invalid.wfile.getvalue().decode('utf-8')}")
    print("=" * 65)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_internal_unit_test()
    else:
        run_server()
