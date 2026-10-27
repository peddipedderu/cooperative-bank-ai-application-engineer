"""Grounded Banking Knowledge Base & Context Retrieval Subsystem."""

BANK_KB = {
    "loan_rates": (
        "Co-operative Bank personal loan interest rates start from 13.0% p.a. on reducing balance with flexible "
        "repayment tenors up to 72 months. Salary advances are available via MCo-op Cash up to KES 200,000 instantly. "
        "MSME Biashara loans are available up to KES 10,000,000 subject to turnover assessment."
    ),
    "account_opening": (
        "Opening an account with Co-operative Bank requires: Valid Kenyan National ID / Passport, "
        "KRA PIN Certificate, and passport-size photo. Self-onboarding can be "
        "completed instantly via the MCo-op Cash App or by dialing USSD code *667#."
    ),
    "mpesa_daraja": (
        "Co-op Bank supports real-time two-way integration with Safaricom M-PESA via Paybill 400200. "
        "Maximum daily transaction limit via digital channels is KES 300,000 in accordance with CBK prudential limits."
    ),
    "security_hotline": (
        "For suspicious transactions or security alerts, contact our 24/7 Security Operations Center (SOC) "
        "at 0703 027 000 or email security@co-opbank.co.ke."
    )
}

def retrieve_bank_context(query: str) -> str:
    q_low = query.lower()
    for topic, text in BANK_KB.items():
        if any(w in q_low for w in topic.split("_")):
            return text
    return "Co-operative Bank of Kenya ('The Kingdom Bank') offers personal, business, and cooperative banking. Call 0703 027 000 for support."
