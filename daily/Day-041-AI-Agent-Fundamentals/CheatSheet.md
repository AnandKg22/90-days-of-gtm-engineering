# Cheat Sheet - AI Agent Fundamentals

This cheat sheet compiles agent execution patterns, function schemas, and terminology definitions.

---

## 1. Key Terminology

*   **ReAct (Reasoning + Acting)**: The loop of generating thought processes followed by executable action payloads, repeating until the goal is achieved.
*   **Tool (Function Binding)**: An external function wrapped in a JSON description schema that the LLM is authorized to request.
*   **Context Window Memory**: The short-term memory block containing historical thoughts and observations within the current LLM token window.
*   **Sensory Memory**: Raw, unparsed observations before filtering (e.g. raw HTML returned from scraper tool).

---

## 2. LLM Function Calling Schema Example (JSON)

To register a tool for function calling, supply the LLM with this JSON Schema:
```json
{
  "name": "search_web",
  "description": "Searches the web for company firmographics and technographics.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query (e.g., 'Wayne Enterprises tech stack')."
      }
    },
    "required": ["query"]
  }
}
```

---

## 3. Python ReAct Loop Skeleton

A lightweight execution loop running inside an agent wrapper:
```python
def run_agent_loop(agent_goal, max_steps=5):
    state = {"goal": agent_goal, "facts": {}, "memory": []}
    
    for step in range(1, max_steps + 1):
        # 1. Ask LLM for Thought + Action
        llm_response = call_llm(prompt_with_state(state))
        thought = llm_response.get("thought")
        tool_to_call = llm_response.get("action")
        arg = llm_response.get("argument")
        
        print(f"[{step}] Thought: {thought}")
        
        if not tool_to_call:
            print("Goal achieved. Stopping loop.")
            break
            
        # 2. Execute Local Tool
        observation = execute_tool(tool_to_call, arg)
        print(f"[{step}] Observation: {observation}")
        
        # 3. Log into Memory
        state["memory"].append({
            "step": step, 
            "thought": thought, 
            "tool": tool_to_call, 
            "observation": observation
        })
        
    return synthesize_report(state)
```
---

## 4. Native API Function Dispatcher Map
Mapping LLM action strings to executable functions dynamically:
```python
tool_dispatcher = {
    "search_web": search_web_function,
    "fetch_pricing": fetch_pricing_function
}

# Invoke dynamic tool
tool_name = "search_web"
argument = "Stark Industries"
output = tool_dispatcher[tool_name](argument)
```
