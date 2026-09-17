# Veridian Corp — Internal IT Support Agent

A production-grade, enterprise internal IT support agent prototype built for **Veridian Corp**. The system processes employee requests through an automated 6-stage pipeline: understanding intent, retrieving authoritative policies, checking conditional business rules, executing decisions (Resolve, Ask Clarification, Escalate, Approval Required, Waiting for Employee), generating structured sequential tickets, and maintaining an immutable audit trail.

---

## Key Highlights & Architectural Guarantees

1. **Deterministic Decision Engine**:
   - Classification, rule evaluation, department assignment, SLA calculations, and approvals are **100% deterministic and rule-based**.
   - Backed exclusively by Veridian Corp's internal knowledge base (`KB-01` through `KB-10` + `ASSET-MGMT-POLICY`).

2. **Zero-Hallucination Guardrail**:
   - If an LLM is enabled (`LLM_API_KEY`), it is used **only** as a rephraser for conversational polish.
   - Any LLM output is validated against the retrieved policy text. If the LLM invents a policy ID, modifies numbers (e.g. changing 90 days to 60 days), or alters SLAs, the output is rejected and the deterministic fallback response is delivered.

3. **Explicit Policy Conflict Handling**:
   - Detects the discrepancy between **KB-03** (3-year standard laptop replacement) and **ASSET-MGMT-POLICY** (4-year hardware lifecycle).
   - If a laptop is between 3 and 4 years old (e.g. 3.2 years in `REQ-04`), the engine flags the conflict explicitly, marks the decision as `APPROVAL_REQUIRED`, routes to **IT Asset Management**, and requests **VP approval** before proceeding.

4. **Ambiguity & Clarification Flow**:
   - When required details are missing (e.g. `REQ-15` "My system is slow"), the engine transitions into `WAITING_FOR_EMPLOYEE` and asks targeted clarification questions without hallucinating a resolution.

5. **Sequential Ticket Tracking**:
   - Seeded with historical precedent tickets `TK-1042` through `TK-1051`.
   - New tickets atomically increment from `TK-1052` onward.

6. **Full Audit Logging**:
   - Every single agent execution logs a timestamped event with raw input, classified intent, matched policies, decision outcome, routing target, SLA, and justification.

---

## System Architecture

```
[Employee Input / UI]
        │
        ▼
[1. Request Intake & Audit Log Start]
        │
        ▼
[2. Intent Classifier & Policy Retriever (TF-IDF + Rule-based)]
        │
        ▼
[3. Deterministic Decision Engine (Condition & Policy Evaluation)]
   ├── Direct Resolution: Self-service / Known KB (e.g. KB-01 Password Reset, KB-08 Monitor)
   ├── Clarification: Missing parameters -> WAITING_FOR_EMPLOYEE (e.g. REQ-15)
   ├── Policy Conflict: KB-03 vs ASSET-MGMT-POLICY -> APPROVAL_REQUIRED (VP Approval)
   ├── Approval Required: Paid software, hardware exceptions -> APPROVAL_REQUIRED
   └── Escalation: Risky, security, or hardware faults -> ESCALATE (e.g. SecOps, Desktop Support)
        │
        ▼
[4. Optional LLM Polish with Strict Validation Guardrail]
        │
        ▼
[5. Structured Ticket Creation (TK-1052+ atomic sequence)]
        │
        ▼
[6. Audit Trail Finalization & Live Dashboard Update]
```

---

## Project Structure

```
veridian-it-agent/
├── backend/
│   ├── app/
│   │   ├── agent/
│   │   │   ├── engine.py           # 12 Intent handlers, decision rules & conflict detector
│   │   │   └── llm_client.py       # LLM rephraser with strict fact guardrail
│   │   ├── database/
│   │   │   ├── db.py               # SQLite schema & thread-safe connection pool
│   │   │   └── seed.py             # Precedents TK-1042..1051 + Requests REQ-01..15
│   │   ├── policies/
│   │   │   └── kb_data.py          # Veridian KB-01..KB-10 + ASSET-MGMT-POLICY
│   │   ├── rag/
│   │   │   └── retriever.py        # Knowledge base search & policy retriever
│   │   ├── schemas/
│   │   │   └── agent.py            # Pydantic schemas, Enums, Ticket & Audit models
│   │   ├── services/
│   │   │   ├── audit_service.py    # Immutable audit logger & query filters
│   │   │   ├── request_service.py  # End-to-end request processor
│   │   │   └── ticket_service.py   # Atomic sequential ticket manager (TK-1052+)
│   │   └── main.py                 # FastAPI application with REST endpoints & docs
│   ├── tests/
│   │   └── test_decision_engine.py # Automated test suite (18 test cases)
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── PipelineVisualizer.jsx # Real-time 6-stage pipeline stepper
│   │   │   ├── Sidebar.jsx            # Enterprise navigation & system status
│   │   │   └── TicketDetailModal.jsx  # Comprehensive ticket inspector
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx          # Metrics, recent tickets, audit feeds
│   │   │   ├── NewRequest.jsx         # Live interactive agent console + pre-built test cases
│   │   │   ├── Tickets.jsx            # Searchable, filterable ticket table
│   │   │   ├── KnowledgeBase.jsx      # Policy library viewer & search
│   │   │   └── AuditTrail.jsx         # Immutable audit event log inspector
│   │   ├── services/
│   │   │   └── api.js                 # Frontend API client
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
├── run_backend.ps1                    # Windows 1-click backend launcher
├── run_frontend.ps1                   # Windows 1-click frontend launcher
├── run_all.ps1                        # Windows 1-click all-in-one launcher
└── README.md
```

---

## Quickstart Guide (Local Windows Environment)

### Prerequisites
- Python 3.10+
- Node.js 18+ and npm

### Option A: One-Click Launch (Recommended)

Run the master script in PowerShell:
```powershell
.\run_all.ps1
```
This script will:
1. Start the FastAPI backend on `http://127.0.0.1:8000`
2. Run database migrations & seed historical tickets (`TK-1042`..`TK-1051`)
3. Launch the Vite frontend on `http://localhost:5173`

---

### Option B: Manual Step-by-Step

#### 1. Backend Setup
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m app.database.seed
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
- API is live at: `http://127.0.0.1:8000`
- Interactive Swagger docs: `http://127.0.0.1:8000/docs`

#### 2. Frontend Setup
In a separate PowerShell terminal:
```powershell
cd frontend
npm install
npm run dev
```
- Open browser at: `http://localhost:5173`

---

## Running with Docker

You can run the entire system with Docker Compose:
```bash
docker-compose up --build
```
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- Swagger Docs: `http://localhost:8000/docs`

---

## Environment Variables (Optional)

The application is fully operational out-of-the-box in 100% deterministic mode. If you wish to enable optional LLM response rephrasing:

```env
# Optional LLM Config (OpenAI-compatible)
LLM_API_KEY=sk-...
LLM_API_BASE=https://api.openai.com/v1
LLM_MODEL=gpt-4o-mini
```

*Note: All core classification, policy evaluation, conflict detection, routing, and ticket generation remain completely deterministic even when an LLM key is configured.*

---

## Running the Automated Test Suite

To run all automated verification tests:
```powershell
cd backend
python -m pytest -v tests/test_decision_engine.py
```

---

## Evaluator Walkthrough & Demo Script

Open `http://localhost:5173` in your browser and click on **"Submit Request"** in the sidebar. You will find interactive preset buttons for key test cases:

### Scenario 1: Self-Service Resolution (`REQ-01`)
- **Query**: "How do I reset my password? I forgot it."
- **Expected Decision**: `RESOLVE`
- **Policy**: `KB-01`
- **Routing**: Directly resolved via self-service portal (https://verify.veridian.internal).
- **Ticket**: Resolves immediately with low priority.

### Scenario 2: Software Approval Workflow (`REQ-03`)
- **Query**: "I need a license for Figma Professional for UI design."
- **Expected Decision**: `APPROVAL_REQUIRED`
- **Policy**: `KB-02`
- **Routing**: Routed to Department Manager; Cost center required ($15/mo).

### Scenario 3: Policy Conflict Detection (`REQ-04`)
- **Query**: "My laptop is 3.2 years old and running slowly. Can I get a replacement?"
- **Expected Decision**: `APPROVAL_REQUIRED`
- **Policies**: `KB-03` AND `ASSET-MGMT-POLICY`
- **Conflict Note**: Explicitly states `KB-03` specifies 3-year standard refresh while `ASSET-MGMT-POLICY` specifies 4-year lifecycle. Requires VP approval.
- **Routing**: Routed to IT Asset Management.

### Scenario 4: Security Incident Escalation (`REQ-06`)
- **Query**: "I received a suspicious email asking for my credentials with an urgent deadline."
- **Expected Decision**: `ESCALATE`
- **Policy**: `KB-06`
- **Routing**: High priority escalation to Security Operations (SecOps), SLA: 15 minutes.

### Scenario 5: Ambiguous Query Clarification (`REQ-15`)
- **Query**: "My system is slow."
- **Expected Decision**: `WAITING_FOR_EMPLOYEE`
- **Policy**: `KB-05`
- **Behavior**: Does not hallucinate an answer or close the ticket. Prompts employee: *"Is your internet connection slow, your computer freezing, or a specific application lagging?"*

---

## API Documentation Summary

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | Healthcheck and LLM status |
| `POST` | `/api/agent/analyze` | Run 6-stage decision pipeline on an employee request |
| `GET` | `/api/requests` | List all processed requests with filters |
| `GET` | `/api/requests/{id}` | Retrieve request details and generated ticket |
| `GET` | `/api/tickets` | List all tickets with status and priority filters |
| `GET` | `/api/tickets/{id}` | Retrieve specific ticket with audit history |
| `PATCH` | `/api/tickets/{id}/resolve` | Resolve an open ticket with notes |
| `GET` | `/api/audit` | Query immutable audit log with filters |
| `GET` | `/api/knowledge-base` | Search or inspect internal policies (KB-01..10 + Asset) |
| `GET` | `/api/dashboard/summary` | Dashboard metrics, ticket breakdown, and recent activity |
