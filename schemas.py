"""Pydantic Request & Response Schemas for Co-op Bank AI Platform."""
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    message: str = Field(..., description="Customer or staff message")
    user_type: Optional[str] = Field("customer", description="customer | msme | staff")

class ChatResponse(BaseModel):
    session_id: str
    message: str
    source: str
    flagged: bool
    audit_id: str
    suggested_actions: List[str]

class RecommendRequest(BaseModel):
    age: int
    income_band: str  # low | medium | high
    has_savings: bool
    has_loan: bool
    business_owner: bool

class DocumentParseRequest(BaseModel):
    document_type: str  # statement | receipt | kyc
    raw_text: str
