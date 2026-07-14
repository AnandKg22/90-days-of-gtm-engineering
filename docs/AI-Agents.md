# AI Agents in Go-To-Market

This guide details the architectures of AI agents designed to automate prospecting research, email outreach, meeting prep, and customer success campaigns.

---

## 1. Agent Architecture Framework

An AI Agent is structured with four key components:

```
                 ┌──────────────────────┐
                 │       GOAL / TASK    │
                 └──────────┬───────────┘
                            ▼
    ┌───────────────────────────────────────────────┐
    │                REASONING LOOP                 │
    │  (ReAct: Reason -> Action -> Observation)      │
    └──────┬─────────────────┬───────────────┬──────┘
           ▼                 ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────┐
│      MEMORY      │ │    TOOLS     │ │  GUARDRAILS  │
│ (Short/Long Term)│ │ (APIs, Scrape)│ │(Output Format)│
└──────────────────┘ └──────────────┘ └──────────────┘
```

1.  **Reasoning Loop**: The model evaluates input, plans steps, calls tools, and reflects on outcomes.
2.  **Memory**:
    *   **Short-term**: Session tokens, conversation history.
    *   **Long-term**: Vector database retrievals (RAG) containing historical company data.
3.  **Tools**: REST APIs (Scraper, LinkedIn Search, HubSpot CRUD, Email Sender).
4.  **Guardrails**: Validation schemas forcing output to conform to JSON schemas or strict sales playbooks.

---

## 2. Single-Agent vs. Multi-Agent Systems

Complex GTM jobs require task division among multiple specialist agents rather than relying on one generalist.

```
                  ┌──────────────────────┐
                  │    Planner Agent     │
                  └──────────┬───────────┘
                             │ (Delegates Task)
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       ┌─────────────┐┌─────────────┐┌─────────────┐
       │Research Agt ││ Writer Agt  ││ Reviewer Agt│
       │ (Web Scrape)││(Draft Email)││(Check Brand)│
       └─────────────┘└─────────────┘└─────────────┘
```

*   **Research Agent**: Queries search engines, extracts tech stack, scans funding news.
*   **Writer Agent**: Takes research insights and writes targeted sales copies following AIDA structures.
*   **Reviewer / Guardrail Agent**: Checks copies for tone compliance, personalization accuracy, spam trigger keywords, and outputs clean CRM records.

---

## 3. Basic AI Agent Implementation (Python Tool Calling)

```python
import json
from openai import OpenAI

client = OpenAI()

# 1. Define tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "enrich_company",
            "description": "Fetch details of a company by its domain name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "domain": {"type": "string", "description": "Company domain, e.g. stripe.com"}
                },
                "required": ["domain"]
            }
        }
    }
]

# Tool implementation mock
def enrich_company(domain):
    if "stripe" in domain:
        return {"name": "Stripe", "tech_stack": "React, Ruby, Postgres", "employee_count": 8000}
    return {"name": "Unknown", "tech_stack": "Unknown", "employee_count": 0}

# 2. Main Agent Execution
def run_agent(task_prompt):
    messages = [
        {"role": "system", "content": "You are a helpful GTM Research Agent. Use tools to find info."},
        {"role": "user", "content": task_prompt}
    ]
    
    # First request: Reason if tool is needed
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    
    if tool_calls:
        # Append assistant response to history
        messages.append(response_message)
        
        # Resolve tools
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            if function_name == "enrich_company":
                tool_output = enrich_company(function_args.get("domain"))
                
                # Append tool result to history
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": json.dumps(tool_output)
                })
                
        # Second request: Generate final answer based on tool output
        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return final_response.choices[0].message.content
        
    return response_message.content

print(run_agent("Research stripe.com and summarize their business stack."))
```
