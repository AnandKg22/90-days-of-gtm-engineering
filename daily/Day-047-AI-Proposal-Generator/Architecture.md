# GTM Architecture - Day 047: AI Proposal Generator

This document details the proposal compiler pipelines, pricing engines, and discount compliance routing supporting proposal generation.

---

## 🔄 Proposal Generation Pipeline

The diagram below details the pipeline, showing how customer variables are processed to compile a structured, compliant sales proposal:

```mermaid
graph TD
    Data[Input: Customer Discovery Data] -->|1. Ingest| Ingestor[Context Ingestor]
    
    subgraph CPQ Billing Engine
        Ingestor -->|2. Check Tier| CPQ[CPQ Pricing Calculator]
        CPQ -->|Calculate Subtotal| DiscountGate{Check Discount}
        DiscountGate -->|Apply %| FinalTCV[Calculate Total Contract Value]
    end
    
    subgraph ROI Value Modeler
        Ingestor -->|2. Pull Hours & Rates| ROI[ROI Calculator]
        ROI -->|Calculate Losses| PainCost[Annual Operational Loss]
        PainCost -->|Compare with Total Contract Value| NetSavings[Year 1 Net Savings]
        NetSavings -->|Savings / Contract Value| ROIPercent[ROI Percentage]
    end
    
    subgraph SOW & Tech Mapping
        Ingestor -->|2. Pull Tech Stack| SOWCompiler[SOW Compiler]
    end
    
    subgraph Compliance Approval Gate
        FinalTCV -->|Check Limits| ApprovalRoute{Is Discount > 20%?}
        ApprovalRoute -->|Yes| Pending[Route: PENDING VP APPROVAL]
        ApprovalRoute -->|No| Approved[Route: DIRECTOR APPROVED / AUTO]
    end
    
    FinalTCV -->|3. Assemble| Renderer[Document Renderer]
    ROIPercent -->|3. Assemble| Renderer
    SOWCompiler -->|3. Assemble| Renderer
    Pending -->|3. Assemble| Renderer
    Approved -->|3. Assemble| Renderer
    
    Renderer -->|4. Output Document| PDF[Final GTM Proposal PDF]
```

---

## ⚙️ Core Architecture Components

1.  **Context Ingestor**: Reads raw parameters (company name, size, technology stack, pain points, wasted hours, labor rate, discount) from the CRM opportunity file.
2.  **CPQ Pricing Calculator**: Maps segment tiers (SMB vs MM vs Enterprise) to baseline software licensing and implementation setup fee matrices, applying discounts.
3.  **ROI Value Modeler**: Compiles the customer's cost of pain and savings percentages, providing a quantitative value argument for sales calls.
4.  **SOW Compiler**: Dynamically writes phased integration steps based on the customer's technology stack.
5.  **Approval Route Controller**: Evaluates discount compliance levels, routing the proposal's status based on discount thresholds.
6.  **Document Renderer**: Combines all sections and formats them as markdown files, ready for PDF compilation.
