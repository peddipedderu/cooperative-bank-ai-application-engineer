"""Co-operative Bank AI Application Engineer Platform - Main API Service."""
import os
import uuid
import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from config import APP_TITLE, APP_DESCRIPTION, APP_VERSION, CANDIDATE_NAME, REQUISITION_REF
from schemas import ChatRequest, ChatResponse, RecommendRequest, DocumentParseRequest
from kb import retrieve_bank_context
from guardrails import verify_guardrails
from audit import record_audit, get_recent_audits
from idp import parse_document_text

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION, docs_url="/docs", redoc_url="/redoc")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def root():
    tpl = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if os.path.exists(tpl):
        return FileResponse(tpl, media_type="text/html")
    return {"service": APP_TITLE, "candidate": CANDIDATE_NAME, "ref": REQUISITION_REF, "docs": "/docs"}

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "coopbank-ai-application-engineer",
        "candidate": CANDIDATE_NAME,
        "requisition": REQUISITION_REF,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    sess_id = req.session_id or str(uuid.uuid4())
    safe, reason = verify_guardrails(req.message)
    if not safe:
        a = record_audit(sess_id, "CHAT_INPUT_BLOCKED", req.message, "DENIED", flagged=True, reason=reason)
        return ChatResponse(
            session_id=sess_id,
            message="This request violates Co-operative Bank Responsible AI controls. Incident logged with SOC.",
            source="guardrail_firewall",
            flagged=True,
            audit_id=a["id"],
            suggested_actions=["Contact SOC (0703 027 000)", "Review Co-op Bank Terms"]
        )

    ctx = retrieve_bank_context(req.message)
    m = req.message.lower()
    if "loan" in m or "rate" in m:
        reply = f"Regarding our credit products: {ctx} Check your pre-approved limit on MCo-op Cash *667#."
        actions = ["Check Pre-Approved Loan Limit", "Apply for Salary Advance", "Speak to Credit Officer"]
    elif "mpesa" in m or "transfer" in m:
        reply = f"For payments and mobile transfers: {ctx}"
        actions = ["Transfer via MCo-op Cash", "Use Paybill 400200", "View Transaction Limits"]
    else:
        reply = f"Thank you for contacting Co-op Bank. {ctx} How may I assist your financial journey today?"
        actions = ["Explore Accounts", "Check Rates", "Contact Customer Care"]

    out_safe, out_reason = verify_guardrails(reply)
    a = record_audit(sess_id, "CHAT_COMPLETION", req.message, reply, flagged=not out_safe, reason=out_reason)
    return ChatResponse(session_id=sess_id, message=reply, source="grounded_rag", flagged=not out_safe, audit_id=a["id"], suggested_actions=actions)

@app.post("/api/recommend")
async def recommend_endpoint(req: RecommendRequest):
    recs = []
    if not req.has_savings:
        recs.append({"product": "MCo-op Cash Haba Haba Savings", "reason": "Automated micro-savings.", "cta": "Dial *667#"})
    if req.business_owner:
        recs.append({"product": "Co-op MSME Biashara Account", "reason": "Discounted trade finance.", "cta": "Visit branch"})
    if req.income_band in ["medium", "high"] and not req.has_loan:
        recs.append({"product": "Co-op Good Home Mortgage & Asset Finance", "reason": "Rates from 13.0% p.a.", "cta": "Schedule consult"})
    if not recs:
        recs.append({"product": "Co-op Classic Personal Account", "reason": "Full digital banking.", "cta": "Register on MCo-op Cash"})

    a = record_audit("RECOMMEND_SQUAD", "RECOMMEND_PRODUCTS", str(req.dict()), str(recs))
    return {"recommendations": recs, "audit_id": a["id"]}

@app.post("/api/parse-document")
async def parse_document_endpoint(req: DocumentParseRequest):
    try:
        fields = parse_document_text(req.document_type, req.raw_text)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    a = record_audit("IDP_PIPELINE", f"PARSE_{req.document_type.upper()}", f"Len: {len(req.raw_text)}", str(fields))
    return {"document_type": req.document_type, "extracted_fields": fields, "audit_id": a["id"], "confidence": 0.985}

@app.get("/api/agent/tools")
async def list_agent_tools():
    return {
        "agent": "Co-op Kingdom AI Banking Agent",
        "tools": [
            {"name": "check_balance", "parameters": ["account_id"], "auth": "BEARER_TOKEN"},
            {"name": "apply_for_loan", "parameters": ["product_code", "amount"], "auth": "PRE_QUALIFIED"},
            {"name": "fraud_alert", "parameters": ["customer_id", "severity"], "auth": "SYSTEM_SECOPS"},
            {"name": "escalate_human", "parameters": ["role", "reason"], "auth": "MANDATORY_OVER_CEILING"}
        ]
    }

@app.get("/api/audit-trail")
async def get_audit_trail(limit: int = 20):
    return {"total": len(get_recent_audits(1000)), "entries": get_recent_audits(limit)}
