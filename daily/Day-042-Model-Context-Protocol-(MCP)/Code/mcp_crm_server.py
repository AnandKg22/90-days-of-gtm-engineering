# Day 042: Model Context Protocol (MCP) - CRM Server
import sys
import json
import traceback
from typing import Dict, Any, List

# Core mock CRM Database
CRM_CONTACTS = {
    "bruce@waynecorp.com": {"name": "Bruce Wayne", "company": "Wayne Enterprises", "title": "CEO", "revenue": 50000000.0, "status": "Synced"},
    "sconnor@cyberdyne.co": {"name": "Sarah Connor", "company": "Cyberdyne Systems", "title": "Operations Director", "revenue": 8500000.0, "status": "Enriched"},
    "pepper@stark.com": {"name": "Pepper Potts", "company": "Stark Industries", "title": "CEO", "revenue": 120000000.0, "status": "Synced"}
}

CRM_DEALS = [
    {"deal_id": 301, "company": "Wayne Enterprises", "value": 120000.0, "stage": "Closed Won", "sales_rep": "Sarah Connor"},
    {"deal_id": 302, "company": "Stark Industries", "value": 250000.0, "stage": "Proposal", "sales_rep": "Bruce Wayne"},
    {"deal_id": 303, "company": "Cyberdyne Systems", "value": 30000.0, "stage": "Discovery", "sales_rep": "Sarah Connor"}
]

CRM_NOTES = []

def log_debug(message: str):
    """Logs debugging statements to stderr (stdout is reserved for JSON-RPC)."""
    sys.stderr.write(f"[DEBUG] {message}\n")
    sys.stderr.flush()

# Tool Handler Functions
def get_crm_contact(arguments: Dict[str, Any]) -> Dict[str, Any]:
    email = arguments.get("email", "").strip()
    contact = CRM_CONTACTS.get(email)
    if contact:
        return {
            "content": [{
                "type": "text",
                "text": f"Found contact in CRM:\nName: {contact['name']}\nCompany: {contact['company']}\nTitle: {contact['title']}\nStatus: {contact['status']}\nRevenue: ${contact['revenue']:,.2f}"
            }]
        }
    return {
        "content": [{
            "type": "text",
            "text": f"No contact found in CRM for email address: '{email}'"
        }],
        "isError": True
    }

def list_recent_deals(arguments: Dict[str, Any]) -> Dict[str, Any]:
    deals_text = "Recent CRM Deal Logs:\n"
    for d in CRM_DEALS:
        deals_text += f"- Deal #{d['deal_id']} | {d['company']:<20} | Value: ${d['value']:,.2f} | Stage: {d['stage']} | Rep: {d['sales_rep']}\n"
    return {
        "content": [{
            "type": "text",
            "text": deals_text.strip()
        }]
    }

def add_crm_note(arguments: Dict[str, Any]) -> Dict[str, Any]:
    company = arguments.get("company", "").strip()
    note_text = arguments.get("note", "").strip()
    if not company or not note_text:
        return {
            "content": [{"type": "text", "text": "Error: Missing required arguments 'company' or 'note'."}],
            "isError": True
        }
    
    note_entry = {
        "company": company,
        "note": note_text,
        "timestamp": "2026-07-13T21:53:00"
    }
    CRM_NOTES.append(note_entry)
    log_debug(f"Added CRM Note for {company}: {note_text}")
    return {
        "content": [{
            "type": "text",
            "text": f"Successfully created CRM Note for '{company}': '{note_text}'"
        }]
    }

# MCP Server Handlers mapping methods to JSON-RPC responses
def handle_initialize(req_id: Any) -> Dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "gtm-crm-mcp-server",
                "version": "1.0.0"
            }
        }
    }

def handle_tools_list(req_id: Any) -> Dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {
            "tools": [
                {
                    "name": "get_crm_contact",
                    "description": "Retrieves contact details, segment status, and revenue from the CRM database using an email address.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "email": {
                                "type": "string",
                                "description": "The work email address of the lead/contact."
                            }
                        },
                        "required": ["email"]
                    }
                },
                {
                    "name": "list_recent_deals",
                    "description": "Lists all active and won sales deals in the CRM pipeline.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {}
                    }
                },
                {
                    "name": "add_crm_note",
                    "description": "Appends an activity note or log update to a target company record in the CRM.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "company": {
                                "type": "string",
                                "description": "The exact name of the target company."
                            },
                            "note": {
                                "type": "string",
                                "description": "The note content to record (e.g. 'Left voicemail, scheduled meeting next week')."
                            }
                        },
                        "required": ["company", "note"]
                    }
                }
            ]
        }
    }

def handle_tools_call(req_id: Any, params: Dict[str, Any]) -> Dict[str, Any]:
    tool_name = params.get("name")
    arguments = params.get("arguments", {})
    
    log_debug(f"Received call for tool: '{tool_name}' with args: {arguments}")
    
    if tool_name == "get_crm_contact":
        res = get_crm_contact(arguments)
    elif tool_name == "list_recent_deals":
        res = list_recent_deals(arguments)
    elif tool_name == "add_crm_note":
        res = add_crm_note(arguments)
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32601,
                "message": f"Method not found: Tool '{tool_name}' is not registered."
            }
        }
        
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": res
    }

def process_request(line: str):
    """Parses and dispatches standard JSON-RPC 2.0 lines from stdin."""
    try:
        req = json.loads(line)
        method = req.get("method")
        req_id = req.get("id")
        params = req.get("params", {})
        
        log_debug(f"Processing method: '{method}' (ID: {req_id})")
        
        if method == "initialize":
            res = handle_initialize(req_id)
        elif method == "tools/list":
            res = handle_tools_list(req_id)
        elif method == "tools/call":
            res = handle_tools_call(req_id, params)
        else:
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: '{method}' is not implemented by this server."
                }
            }
            
        # Write response back to client stdout
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()
        
    except json.JSONDecodeError:
        log_debug("Failed to decode JSON request line.")
    except Exception as e:
        log_debug(f"Unhandled Exception: {str(e)}")
        log_debug(traceback.format_exc())

def main():
    log_debug("GTM CRM MCP Server started. Listening on stdin...")
    for line in sys.stdin:
        line_str = line.strip()
        if line_str:
            process_request(line_str)

if __name__ == "__main__":
    main()
