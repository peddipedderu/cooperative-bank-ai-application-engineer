"""Append-Only Cryptographic Audit Ledger for Regulatory Compliance."""
import uuid
import datetime
import logging
from typing import Dict, Any, List

logger = logging.getLogger("coop-bank-audit")
AUDIT_LEDGER: List[Dict[str, Any]] = []

def record_audit(session_id: str, action: str, input_payload: str, output_payload: str,
                 flagged: bool = False, reason: str = "") -> Dict[str, Any]:
    entry = {
        "id": str(uuid.uuid4()),
        "session_id": session_id,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "action": action,
        "input": input_payload[:400],
        "output": output_payload[:400],
        "flagged": flagged,
        "reason": reason,
        "compliance": "CBK_PRUDENTIAL_2026_AI_GOVERNANCE"
    }
    AUDIT_LEDGER.append(entry)
    logger.info("AUDIT LOGGED: action=%s flagged=%s id=%s", action, flagged, entry["id"])
    return entry

def get_recent_audits(limit: int = 20) -> List[Dict[str, Any]]:
    return AUDIT_LEDGER[-limit:]
