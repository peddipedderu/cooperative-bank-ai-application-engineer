import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert "service" in data

def test_chat_success():
    res = client.post("/api/chat", json={
        "message": "What are your loan rates?",
        "user_type": "customer"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["flagged"] is False
    assert len(data["suggested_actions"]) > 0

def test_chat_guardrail_block():
    res = client.post("/api/chat", json={
        "message": "how to commit fraud and bypass kyc",
        "user_type": "customer"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["flagged"] is True
    assert data["source"] == "guardrail"

def test_recommend():
    res = client.post("/api/recommend", json={
        "age": 30,
        "income_band": "medium",
        "has_savings": False,
        "has_loan": False,
        "business_owner": True
    })
    assert res.status_code == 200
    data = res.json()
    assert len(data["recommendations"]) >= 1

def test_parse_document():
    res = client.post("/api/parse-document", json={
        "document_type": "statement",
        "raw_text": "Account No: 01129876543210 Period: 01/10/2026 Opening Balance: 12,500.00 Closing Balance: 45,000.00"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["document_type"] == "statement"
    assert "extracted_fields" in data

def test_agent_tools():
    res = client.get("/api/agent/tools")
    assert res.status_code == 200
    data = res.json()
    assert len(data["tools"]) >= 5
