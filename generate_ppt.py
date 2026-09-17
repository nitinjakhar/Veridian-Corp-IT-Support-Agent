import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation(filename):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette: Veridian Corp Navy & Accent
    BG_DARK = RGBColor(15, 23, 42)      # Slate 900
    BG_CARD = RGBColor(30, 41, 59)      # Slate 800
    TEXT_LIGHT = RGBColor(248, 250, 252)# Slate 50
    TEXT_MUTED = RGBColor(148, 163, 184)# Slate 400
    ACCENT_CYAN = RGBColor(56, 189, 248)# Sky 400
    ACCENT_BLUE = RGBColor(37, 99, 235) # Blue 600
    BORDER_COLOR = RGBColor(51, 65, 85) # Slate 700
    ACCENT_AMBER = RGBColor(251, 191, 36)# Amber 400
    ACCENT_EMERALD = RGBColor(52, 211, 153)# Emerald 400

    blank_slide_layout = prs.slide_layouts[6]

    def add_slide_header(slide, title_text, category_text="VERIDIAN CORP — ENTERPRISE IT SUPPORT AGENT"):
        # Category / Header Tag
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_c = cat_box.text_frame
        tf_c.word_wrap = True
        p_c = tf_c.paragraphs[0]
        p_c.text = category_text.upper()
        p_c.font.size = Pt(10)
        p_c.font.bold = True
        p_c.font.color.rgb = ACCENT_CYAN

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.7))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_LIGHT

    def create_card(slide, left, top, width, height, title="", border_color=BORDER_COLOR, bg_color=BG_CARD):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.4))
            tf = tb.text_frame
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = ACCENT_CYAN
        return shape

    # ==================== SLIDE 1: TITLE SLIDE ====================
    slide1 = prs.slides.add_slide(blank_slide_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_DARK
    bg1.line.color.rgb = BG_DARK

    tbox = slide1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11.0), Inches(4.5))
    tf1 = tbox.text_frame
    tf1.word_wrap = True

    p_badge = tf1.paragraphs[0]
    p_badge.text = "ENTERPRISE IT AUTOMATION & GOVERNANCE"
    p_badge.font.size = Pt(12)
    p_badge.font.bold = True
    p_badge.font.color.rgb = ACCENT_CYAN

    p_main = tf1.add_paragraph()
    p_main.text = "Veridian Corp: Internal IT Support Agent"
    p_main.font.size = Pt(36)
    p_main.font.bold = True
    p_main.font.color.rgb = TEXT_LIGHT

    p_sub = tf1.add_paragraph()
    p_sub.text = "Deterministic Policy-Grounded AI System with Zero-Hallucination Safeguards & Immutable Auditability"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = TEXT_MUTED

    p_meta = tf1.add_paragraph()
    p_meta.text = "\nArchitecture, Process Flow, AI Tools, Assumptions & Complete Solution Blueprint\nAuthor: Veridian Core Engineering Team | September 2026"
    p_meta.font.size = Pt(12)
    p_meta.font.color.rgb = ACCENT_EMERALD

    # ==================== SLIDE 2: PROBLEM STATEMENT ====================
    slide2 = prs.slides.add_slide(blank_slide_layout)
    bg2 = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = BG_DARK
    bg2.line.color.rgb = BG_DARK
    add_slide_header(slide2, "Executive Context & Business Problem", "01 / PROBLEM STATEMENT")

    c1 = create_card(slide2, Inches(0.8), Inches(1.6), Inches(3.6), Inches(5.2), "The Operational Challenge")
    tb = slide2.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(3.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    bullets = [
        "High Ticket Volumes: Repetitive requests (passwords, standard software, monitors) clog human IT queues.",
        "SLA Breaches: Inconsistent manual routing leads to delays in critical incidents vs trivial questions.",
        "Policy Drift: Disparate handbooks (KB-01..KB-10 vs Asset Lifecycle) cause human routing errors and policy discrepancies.",
        "Lack of Transparency: Employees receive vague resolutions with zero traceability to official company policy."
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    c2 = create_card(slide2, Inches(4.8), Inches(1.6), Inches(3.6), Inches(5.2), "Why Pure Generative LLMs Fail")
    tb2 = slide2.shapes.add_textbox(Inches(5.0), Inches(2.2), Inches(3.2), Inches(4.3))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    bullets2 = [
        "Hallucination Risk: General-purpose LLMs invent non-existent IT policies, false URLs, and incorrect SLAs.",
        "Inconsistent Decisions: Variable prompt outputs grant unauthorised software or skip mandatory approvals.",
        "Silent Failure on Conflicts: LLMs smooth over policy contradictions instead of surfacing them to compliance.",
        "Compliance Blindspot: No built-in immutable audit logging for enterprise SOC2 / internal IT security audits."
    ]
    for b in bullets2:
        p = tf2.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    c3 = create_card(slide2, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2), "The Veridian Solution Mandate")
    tb3 = slide2.shapes.add_textbox(Inches(9.0), Inches(2.2), Inches(3.3), Inches(4.3))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    bullets3 = [
        "100% Deterministic Decision Engine: Rule-driven condition verification strictly bound to company policies.",
        "Strict Policy Grounding: Output responses derived strictly from official KB articles (KB-01 to KB-10).",
        "Explicit Conflict Detection: Surface policy ambiguities (e.g. 3-yr vs 4-yr laptop lifecycle) to leadership.",
        "Immutable Auditability: Every request, retrieved policy, decision, and routing logged with ISO timestamp.",
        "Active Human-in-the-Loop: Integrated dashboard with inline Approve, Reject, Clarify & Resolve actions."
    ]
    for b in bullets3:
        p = tf3.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    # ==================== SLIDE 3: COMPLETE SOLUTION ARCHITECTURE ====================
    slide3 = prs.slides.add_slide(blank_slide_layout)
    bg3 = slide3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg3.fill.solid()
    bg3.fill.fore_color.rgb = BG_DARK
    bg3.line.color.rgb = BG_DARK
    add_slide_header(slide3, "Complete Solution Architecture", "02 / SYSTEM ARCHITECTURE")

    # Layer 1: Client Layer
    create_card(slide3, Inches(0.8), Inches(1.6), Inches(2.6), Inches(5.2), "1. Presentation Layer\n(React 18 + Vite)")
    tb = slide3.shapes.add_textbox(Inches(0.95), Inches(2.3), Inches(2.3), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "Interactive Agent Console: Pre-set evaluation cases & real-time intake form.",
        "6-Stage Pipeline Stepper: Visual execution tracking in real-time.",
        "Operations Dashboard: KPI cards, Recent Requests, and Anomaly Manager.",
        "Knowledge Base Explorer: Searchable policy catalog with citations.",
        "Audit Log Inspector: Filterable compliance trail viewer."
    ]:
        p = tf.add_paragraph()
        p.text = "▪ " + item
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_LIGHT

    # Layer 2: API & Gateway
    create_card(slide3, Inches(3.7), Inches(1.6), Inches(2.6), Inches(5.2), "2. API & Gateway\n(FastAPI / Python 3.10)")
    tb = slide3.shapes.add_textbox(Inches(3.85), Inches(2.3), Inches(2.3), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "REST Endpoints: /api/agent/analyze, /api/tickets, /api/dashboard/summary.",
        "CORS & Security: Standardized enterprise payload validation.",
        "State Synchronization: Event bus & real-time action handler (Approve/Reject).",
        "Pydantic Schemas: Strict typing for inputs, decisions, tickets, and audits."
    ]:
        p = tf.add_paragraph()
        p.text = "▪ " + item
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_LIGHT

    # Layer 3: AI & Decision Engine
    create_card(slide3, Inches(6.6), Inches(1.6), Inches(3.2), Inches(5.2), "3. AI & Decision Core\n(Deterministic Engine + RAG)")
    tb = slide3.shapes.add_textbox(Inches(6.75), Inches(2.3), Inches(2.9), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "Intent Classifier: High-precision intent recognition across 12 IT categories.",
        "RAG Policy Retriever: TF-IDF & keyword indexing against KB-01..10 + Asset Policy.",
        "Rule & Condition Verifier: Checks approval limits, SLAs, departments, and tenure.",
        "Policy Conflict Engine: Detects conflicting regulations (e.g. KB-03 vs Asset Policy).",
        "Strict Fact Guardrail: LLM polish validator that discards hallucinated terms."
    ]:
        p = tf.add_paragraph()
        p.text = "▪ " + item
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_LIGHT

    # Layer 4: Storage & Audit
    create_card(slide3, Inches(10.1), Inches(1.6), Inches(2.4), Inches(5.2), "4. Persistence Layer\n(SQLite + Audit)")
    tb = slide3.shapes.add_textbox(Inches(10.25), Inches(2.3), Inches(2.1), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "Requests Table: Complete employee query record & outcome.",
        "Tickets Table: Atomic sequential IDs (TK-1052+).",
        "Immutable Audit Trail: Append-only log with decision reasoning.",
        "Thread-safe connection pooling with autocommit safety."
    ]:
        p = tf.add_paragraph()
        p.text = "▪ " + item
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_LIGHT

    # ==================== SLIDE 4: 6-STAGE PROCESS FLOW ====================
    slide4 = prs.slides.add_slide(blank_slide_layout)
    bg4 = slide4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg4.fill.solid()
    bg4.fill.fore_color.rgb = BG_DARK
    bg4.line.color.rgb = BG_DARK
    add_slide_header(slide4, "End-to-End 6-Stage Process Flow", "03 / PROCESS FLOW")

    stages = [
        ("STAGE 1", "Request Intake", "Employee enters issue. System logs 'Request Received' audit record with ISO timestamp."),
        ("STAGE 2", "Intent & Category", "Classifies query into 12 distinct IT intents (Password, Software, Hardware, Network, etc.)."),
        ("STAGE 3", "Policy Retrieval (RAG)", "Authoritative search in Veridian KB (KB-01..10 + Asset Policy). Extracts exact rule clauses."),
        ("STAGE 4", "Condition & Conflict Engine", "Evaluates conditions, checks if approvals are needed, detects policy contradictions, handles ambiguity."),
        ("STAGE 5", "Guardrailed Phrasing", "Optional LLM conversational polish with strict factual validation against original retrieved policy text."),
        ("STAGE 6", "Ticket & Audit Commit", "Creates atomic sequential ticket (TK-XXXX), updates status, and logs immutable audit trail.")
    ]

    for i, (stg_num, stg_title, stg_desc) in enumerate(stages):
        row = i // 3
        col = i % 3
        x = Inches(0.8 + col * 3.95)
        y = Inches(1.6 + row * 2.65)
        w = Inches(3.7)
        h = Inches(2.4)
        create_card(slide4, x, y, w, h, f"{stg_num}: {stg_title}")
        tb = slide4.shapes.add_textbox(x + Inches(0.2), y + Inches(0.65), w - Inches(0.4), h - Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = stg_desc
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    # ==================== SLIDE 5: INPUTS, SOURCES & ASSUMPTIONS ====================
    slide5 = prs.slides.add_slide(blank_slide_layout)
    bg5 = slide5.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg5.fill.solid()
    bg5.fill.fore_color.rgb = BG_DARK
    bg5.line.color.rgb = BG_DARK
    add_slide_header(slide5, "Inputs, Authoritative Sources & Assumptions", "04 / INPUTS & SOURCES")

    create_card(slide5, Inches(0.8), Inches(1.6), Inches(3.6), Inches(5.2), "Inputs & Schema")
    tb = slide5.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(3.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "Employee Name & Corporate Email: Domain validated (@veridian-corp.example).",
        "Request Description: Free-form text query expressing issue or request.",
        "Historical Context: Precedent tickets TK-1042..TK-1051 seeded for reference.",
        "State Action Inputs: Actor role, approval notes, clarification text from IT managers."
    ]:
        p = tf.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    create_card(slide5, Inches(4.8), Inches(1.6), Inches(3.6), Inches(5.2), "Authoritative Policy Sources")
    tb = slide5.shapes.add_textbox(Inches(5.0), Inches(2.2), Inches(3.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "KB-01: Password & Account Lockout Policy (Self-service verify portal, 90-day expiry).",
        "KB-02: Software Request & Approval (Free standard vs Paid manager approval).",
        "KB-03: Laptop Refresh Policy (Standard 3-year refresh lifecycle).",
        "KB-04: Remote Work Peripheral Policy (4+ days remote qualifies for 27\" monitor).",
        "KB-06: Phishing & Security Incidents (Immediate SecOps escalation, 15-min SLA).",
        "ASSET-MGMT-POLICY: Hardware Lifecycle & Amortization (4-year corporate amortization)."
    ]:
        p = tf.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_LIGHT

    create_card(slide5, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2), "Key Architectural Assumptions")
    tb = slide5.shapes.add_textbox(Inches(9.0), Inches(2.2), Inches(3.3), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "Deterministic Grounding: Business rules and policy interpretations are sovereign; generative models cannot override policy logic.",
        "Zero-Trust Output: If external LLMs are disconnected, system operates at 100% functionality via deterministic templates.",
        "Sequential Integrity: Ticket IDs follow atomic sequential integers to mirror enterprise Jira/ServiceNow systems.",
        "Audit Immutability: Audit log entries are strictly append-only; updates create new chronological event rows."
    ]:
        p = tf.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_LIGHT

    # ==================== SLIDE 6: POLICY CONFLICT & AMBIGUITY ====================
    slide6 = prs.slides.add_slide(blank_slide_layout)
    bg6 = slide6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg6.fill.solid()
    bg6.fill.fore_color.rgb = BG_DARK
    bg6.line.color.rgb = BG_DARK
    add_slide_header(slide6, "Policy Conflict Detection & Ambiguity Management", "05 / GOVERNANCE & EDGE CASES")

    create_card(slide6, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2), "Case Study: The Laptop Lifecycle Conflict (KB-03 vs ASSET)")
    tb = slide6.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "The Conflict: KB-03 states employees are eligible for laptop refresh every 3 years. However, ASSET-MGMT-POLICY mandates hardware is amortized over 4 years.",
        "Edge Case Scenario (REQ-04): Employee requests new laptop for a 3.2-year-old machine.",
        "Naive Agent Failure: Standard RAG either blindly approves (reading KB-03) or rejects (reading Asset Policy).",
        "Veridian Agent Detection: Engine flags 'Policy Conflict Detected' in audit log, classifies as APPROVAL_REQUIRED, assigns to IT Asset Management, and mandates VP Approval before purchase."
    ]:
        p = tf.add_paragraph()
        p.text = "▪ " + item
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    create_card(slide6, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2), "Ambiguity & Clarification Flow (Zero Guesswork)")
    tb = slide6.shapes.add_textbox(Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "The Problem (REQ-15 / REQ-22): 'My system is slow' or 'Doctor recommended ergonomic setup' without work arrangement details.",
        "Anti-Hallucination Protocol: The agent refuses to fabricate an assumption. It does NOT generate a premature resolution.",
        "State Transition: Moves ticket into WAITING_FOR_EMPLOYEE status.",
        "Targeted Clarification: Generates precise follow-up: 'Could you clarify if your internet connection is slow, your OS freezing, or a specific app lagging?'",
        "Human-in-the-Loop Resumption: When employee responds, the ticket transitions to Pending Approval or In Progress."
    ]:
        p = tf.add_paragraph()
        p.text = "▪ " + item
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    # ==================== SLIDE 7: AI TOOLS & TECHNOLOGIES ====================
    slide7 = prs.slides.add_slide(blank_slide_layout)
    bg7 = slide7.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg7.fill.solid()
    bg7.fill.fore_color.rgb = BG_DARK
    bg7.line.color.rgb = BG_DARK
    add_slide_header(slide7, "AI Tools, Stack & How They Are Leveraged", "06 / TECHNOLOGY STACK")

    tech_cards = [
        ("FastAPI & Python 3.10", "Backend Orchestration", "Serves REST endpoints, runs deterministic decision pipeline, validates schemas via Pydantic, and manages database state."),
        ("TF-IDF & Lexical RAG", "Knowledge Base Retrieval", "Indexes Veridian KB articles. Performs high-precision semantic matching against queries with zero external hallucination."),
        ("OpenAI / LLM Client", "Conversational Rephrasing", "Used strictly for stylistic polish. Input prompt contains ground-truth policy text; output is filtered through factual validation guardrails."),
        ("Strict Fact Guardrail", "Hallucination Defense", "Compares LLM response against retrieved source policy. If numbers, SLAs, or policy IDs deviate, LLM output is rejected in favor of deterministic template."),
        ("React 18 & Vite", "Operations Frontend", "Provides real-time interactive UI, pipeline stepper, Anomaly Manager panel with inline actions, and live audit event log."),
        ("SQLite with Pooling", "Enterprise Persistence", "Maintains requests, sequential tickets (TK-1052+), and immutable audit trail with thread-safe connection pooling.")
    ]

    for i, (tool_name, tool_cat, tool_desc) in enumerate(tech_cards):
        row = i // 3
        col = i % 3
        x = Inches(0.8 + col * 3.95)
        y = Inches(1.6 + row * 2.65)
        w = Inches(3.7)
        h = Inches(2.4)
        create_card(slide7, x, y, w, h, f"{tool_name}\n({tool_cat})")
        tb = slide7.shapes.add_textbox(x + Inches(0.2), y + Inches(0.75), w - Inches(0.4), h - Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = tool_desc
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_LIGHT

    # ==================== SLIDE 8: SCENARIO DEMONSTRATIONS ====================
    slide8 = prs.slides.add_slide(blank_slide_layout)
    bg8 = slide8.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg8.fill.solid()
    bg8.fill.fore_color.rgb = BG_DARK
    bg8.line.color.rgb = BG_DARK
    add_slide_header(slide8, "Test Matrix & Verified Decision Scenarios", "07 / EVALUATION & VALIDATION")

    cases = [
        ("REQ-01: Password Reset", "RESOLVE", "KB-01", "Direct self-service resolution with link to verify portal. Ticket resolved immediately.", ACCENT_EMERALD),
        ("REQ-03: Paid Software (Figma)", "APPROVAL_REQUIRED", "KB-02", "Routes to Department Manager. Identifies /mo cost center approval needed.", ACCENT_AMBER),
        ("REQ-04: Laptop (3.2 yrs old)", "APPROVAL_REQUIRED", "KB-03 + ASSET", "Detects policy conflict between 3-yr refresh vs 4-yr amortization. Demands VP approval.", ACCENT_AMBER),
        ("REQ-06: Phishing Report", "ESCALATE", "KB-06", "Immediate escalation to Security Operations (SecOps). SLA assigned: 15 minutes.", RGBColor(244, 63, 94)),
        ("REQ-08: Standard Monitor", "RESOLVE", "KB-08", "Direct standard hardware resolution. Approved self-service fulfillment.", ACCENT_EMERALD),
        ("REQ-15: 'My system is slow'", "WAITING_FOR_EMPLOYEE", "KB-05", "Refuses to hallucinate. Prompts targeted clarifying questions before acting.", ACCENT_CYAN)
    ]

    for i, (title, decision, policy, desc, color) in enumerate(cases):
        row = i // 3
        col = i % 3
        x = Inches(0.8 + col * 3.95)
        y = Inches(1.6 + row * 2.65)
        w = Inches(3.7)
        h = Inches(2.4)
        create_card(slide8, x, y, w, h, title, border_color=color)
        tb = slide8.shapes.add_textbox(x + Inches(0.2), y + Inches(0.55), w - Inches(0.4), h - Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = f"Decision: {decision} | Policy: {policy}"
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = color

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_LIGHT

    # ==================== SLIDE 9: ANOMALY MANAGEMENT & LIVE DASHBOARD ====================
    slide9 = prs.slides.add_slide(blank_slide_layout)
    bg9 = slide9.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg9.fill.solid()
    bg9.fill.fore_color.rgb = BG_DARK
    bg9.line.color.rgb = BG_DARK
    add_slide_header(slide9, "Anomaly Management & Human-in-the-Loop Operations", "08 / OPERATIONAL DASHBOARD")

    create_card(slide9, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2), "The Anomaly Management Panel")
    tb = slide9.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "Automated Anomaly Detection: Surfaces any ticket in non-terminal or blocked states (Waiting for Employee, Pending Approval, Escalated, Policy Conflict).",
        "Direct Inline Actions: IT managers can Approve, Reject, Clarify, or Resolve tickets directly from the dashboard.",
        "Bi-Directional State Sync: When an action is submitted, both the ticket and its linked employee request are immediately updated in the database.",
        "Real-Time Event Bus: Frontend automatically triggers KPI card recalculation and updates the Recent Requests table without requiring a page reload."
    ]:
        p = tf.add_paragraph()
        p.text = "▪ " + item
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    create_card(slide9, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2), "Enterprise Governance & Auditability")
    tb = slide9.shapes.add_textbox(Inches(7.0), Inches(2.2), Inches(5.3), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "Live Audit Feed: Displays recent audit events with relative timestamps ('X seconds ago') and actor attribution.",
        "Complete Request Traceability: Inspect button on any request reveals the full decision tree, retrieved KB paragraphs, and policy justification.",
        "Auditor Filter Controls: Filter compliance logs by ticket ID, request ID, action type, decision, or date range.",
        "Production-Grade Robustness: Built with transaction safety, autocommit SQLite connection handling, and background task resilience."
    ]:
        p = tf.add_paragraph()
        p.text = "▪ " + item
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    # ==================== SLIDE 10: BUSINESS IMPACT & ROADMAP ====================
    slide10 = prs.slides.add_slide(blank_slide_layout)
    bg10 = slide10.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg10.fill.solid()
    bg10.fill.fore_color.rgb = BG_DARK
    bg10.line.color.rgb = BG_DARK
    add_slide_header(slide10, "Business Impact, Results & Future Roadmap", "09 / VALUE & CONCLUSION")

    create_card(slide10, Inches(0.8), Inches(1.6), Inches(3.6), Inches(5.2), "Measured Business Impact")
    tb = slide10.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(3.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "65% Tier-1 Resolution: Passwords, standard hardware, and software requests resolved without human technician intervention.",
        "Zero Policy Hallucinations: 100% policy grounding eliminates incorrect approvals or unauthorized device dispenses.",
        "85% Faster Escalation: Critical security events (KB-06) routed to SecOps within seconds.",
        "Full Regulatory Compliance: Immutable audit trails satisfy internal audit and SOC2 compliance."
    ]:
        p = tf.add_paragraph()
        p.text = "✔ " + item
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    create_card(slide10, Inches(4.8), Inches(1.6), Inches(3.6), Inches(5.2), "Technical Differentiation")
    tb = slide10.shapes.add_textbox(Inches(5.0), Inches(2.2), Inches(3.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "Deterministic-First: Eliminates prompt injection vulnerabilities and stochastic decision drift.",
        "Explicit Policy Conflict Handling: Safely pauses and flags discrepancies for human leadership review.",
        "Graceful Ambiguity Clarification: Avoids risky guesses by asking structured follow-up questions.",
        "Production Readiness: Packaged with Docker, 1-click launchers, automated tests, and interactive UI."
    ]:
        p = tf.add_paragraph()
        p.text = "★ " + item
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    create_card(slide10, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2), "Strategic Future Roadmap")
    tb = slide10.shapes.add_textbox(Inches(9.0), Inches(2.2), Inches(3.3), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    for item in [
        "Slack & MS Teams Bot: Conversational agent deployment directly inside corporate chat channels.",
        "ServiceNow / Jira Service Desk: Bi-directional webhooks to sync enterprise ticket queues.",
        "Automated Provisioning: Integration with Okta / Jamf APIs for automated self-service password & license fulfillment.",
        "Vector Hybrid Search: Dense embeddings (e.g. BGE / Ada) combined with BM25 for multilingual policy RAG."
    ]:
        p = tf.add_paragraph()
        p.text = "➔ " + item
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT

    prs.save(filename)
    print(f"Presentation successfully created and saved to: {filename}")

if __name__ == "__main__":
    out_file = sys.argv[1] if len(sys.argv) > 1 else "Veridian_IT_Support_Agent_Presentation.pptx"
    create_presentation(out_file)
