# Study Notes - Day 005: Market Segmentation & Positioning

Today's studies focused on analyzing TAM, SAM, and SOM, and segmenting markets based on firmographic (company characteristics), technographic (technology used), and geographic attributes.

---

## 1. TAM, SAM, and SOM (The Market Layers)

To understand how much money a business can potentially make, we divide its target market into three nesting layers. 

Think of it like looking at a target board:

```
┌─────────────────────────────────────────────────────────┐
│              TAM (Total Addressable Market)             │
│   e.g., All Private K-12 Schools & Coaching Globally    │
│   ┌─────────────────────────────────────────────────┐   │
│   │         SAM (Serviceable Addressable Market)    │   │
│   │   e.g., Private Schools & Coaching in India     │   │
│   │   ┌─────────────────────────────────────────┐   │   │
│   │   │       SOM (Serviceable Obtainable Market)│   │   │
│   │   │ e.g., Test-Prep Centers in South/West IN│   │   │
│   │   └─────────────────────────────────────────┘   │   │
│   └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

1.  **TAM (Total Addressable Market)**: The absolute maximum amount of money your company could make if *every single potential customer* in the world bought your product. For our product, **SmartStudy Classrooms**, this includes all private schools, high schools, and test-prep centers globally.
2.  **SAM (Serviceable Addressable Market)**: The chunk of the TAM that you can actually serve with your current product capabilities and region limits. For example, since our platform is customized for CBSE, ICSE, and Indian state syllabus structures, our SAM consists of private schools and test-prep institutes located in India.
3.  **SOM (Serviceable Obtainable Market)**: The specific, narrow subset of the SAM you can realistically win *right now* with your current budget, sales team, and direct marketing campaigns. For instance, we might focus first on coaching centers in metropolitan hubs (Mumbai, Bengaluru, Pune) that already use online portals/LMS software, as they are the easiest to get on board.

---

## 2. Deep-Dive: How to Segment a Database

As a Go-To-Market (GTM) Engineer, you will write computer scripts to sort thousands of potential business leads into segments. We do this using six main criteria:

### 1. Industry Niche (What do they do?)
*   **Definition**: The specific sub-type of educational organization (e.g., a *K-12 Private Boarding School* vs. an *IIT-JEE Coaching Center* vs. a *Language Tuition Class*).
*   **GTM Application**: An IIT-JEE coaching center cares about mock entrance exams, while a primary school cares about interactive creative homework. We send them completely different marketing emails.

### 2. Size / Student Count (How big are they?)
*   **Definition**: Categorizing leads by scale (e.g., small local classes < 100 students, mid-size schools 100–1,000, mega coaching chains > 1,000 students).
*   **GTM Application**: Small classes can sign up automatically with a credit card (Self-Serve). Mega coaching chains need human sales executives to negotiate custom enterprise contracts.

### 3. Revenue (How much budget do they have?)
*   **Definition**: Segmenting schools by their annual tuition budgets or fees collected.
*   **GTM Application**: Helps us figure out if a school can afford a premium tier or if we should pitch them a lower-cost entry package.

### 4. Country & Syllabus (Where are they, and what do they teach?)
*   **Definition**: Organizing leads by geographic borders and the educational boards they follow.
*   **GTM Application**: A school in India needs CBSE/ICSE integration, while a school in the US needs AP (Advanced Placement) or SAT-aligned worksheets. Leads are automatically routed to sales reps who understand those local exams.

### 5. Technology / Technographics (What tools do they already use?)
*   **Definition**: Checking what software the school already uses for digital learning (e.g., Google Classroom, Moodle, Canvas, or nothing at all).
*   **GTM Application**: If a coaching center already uses Moodle, we can pitch our app as an "instant plugin." If they use paper files only, we have to teach them how to go digital first (which takes longer to sell).

### 6. Intent (How interested are they?)
*   **Definition**: Scoring leads based on their activity (e.g., High Intent: visited our pricing page three times; Low Intent: only downloaded one free physics sheet).
*   **GTM Application**: Our sales team spends their time calling the High Intent leads immediately, while sending automated, low-pressure weekly tips to the Low Intent leads.
