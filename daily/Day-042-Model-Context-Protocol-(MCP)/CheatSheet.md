# Cheat Sheet - Model Context Protocol (MCP)

This cheat sheet compiles JSON-RPC 2.0 schemas, client configurations, and key method mappings for the Model Context Protocol.

---

## 1. Key MCP Methods

| Method Name | Direction | Payload Description |
| :--- | :--- | :--- |
| **`initialize`** | Client $\rightarrow$ Server | Init handshake, sends client capabilities. |
| **`tools/list`** | Client $\rightarrow$ Server | Requests list of registered tool schemas. |
| **`tools/call`** | Client $\rightarrow$ Server | Requests execution of tool by name with args. |
| **`resources/list`** | Client $\rightarrow$ Server | Requests list of available read-only resources. |
| **`resources/read`** | Client $\rightarrow$ Server | Reads raw file or DB context via URI reference. |

---

## 2. JSON-RPC 2.0 Message Formats

### Tool Invocation Request (Client $\rightarrow$ Server)
```json
{
  "jsonrpc": "2.0",
  "id": 102,
  "method": "tools/call",
  "params": {
    "name": "get_crm_contact",
    "arguments": {
      "email": "bruce@waynecorp.com"
    }
  }
}
```

### Tool Response (Server $\rightarrow$ Client)
```json
{
  "jsonrpc": "2.0",
  "id": 102,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Found contact in CRM: Bruce Wayne..."
      }
    ]
  }
}
```

---

## 3. Claude Desktop Configuration File

To mount your local Python MCP server to **Claude Desktop**, edit `claude_desktop_config.json`:
*   *Windows Path*: `%APPDATA%\Claude\claude_desktop_config.json`
*   *Mac Path*: `~/Library/Application Support/Claude/claude_desktop_config.json`

### Configuration Schema:
```json
{
  "mcpServers": {
    "gtm-crm-server": {
      "command": "python",
      "args": [
        "D:/Books/90Days-GTM-Engineer/90-days-of-gtm-engineering/daily/Day-042-Model-Context-Protocol-(MCP)/Code/mcp_crm_server.py"
      ],
      "env": {
        "PORT": "5000"
      }
    }
  }
}
```

---

## 4. Standard Python Stdio Server Template

```python
import sys
import json

def main():
    # Read from client stdin
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            # Process req...
            res = {"jsonrpc": "2.0", "id": req.get("id"), "result": {}}
            # Write to client stdout
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
```
