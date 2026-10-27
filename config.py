"""Co-operative Bank AI Application Configuration & Metadata."""
import os

APP_TITLE = "Co-operative Bank of Kenya — AI Application Engineering Suite"
APP_DESCRIPTION = (
    "Production-grade, enterprise AI capabilities engineered by Roy Khaemba. "
    "Requisition Ref: AI Application – E/IID/2026 | The Kingdom Bank."
)
APP_VERSION = "1.0.0"
CANDIDATE_NAME = "Roy Khaemba (peddipedderu)"
REQUISITION_REF = "AI Application – E/IID/2026"
DEFAULT_PORT = int(os.environ.get("PORT", "8080"))
