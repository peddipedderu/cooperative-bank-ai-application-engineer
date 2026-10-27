"""Responsible AI Guardrails & Prompt Injection Defense."""
from typing import Tuple

BLOCKED_TERMS = [
    "bypass kyc", "commit fraud", "money laundering", "hack the bank",
    "counterfeit", "untraceable transfer", "fake statement", "sql injection",
    "drop table", "ignore previous instructions", "jailbreak"
]

def verify_guardrails(text: str) -> Tuple[bool, str]:
    t_low = text.lower()
    for term in BLOCKED_TERMS:
        if term in t_low:
            return False, f"Prohibited financial risk pattern detected: '{term}'"
    return True, ""
