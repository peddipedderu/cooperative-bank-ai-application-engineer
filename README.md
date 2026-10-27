# Co-operative Bank of Kenya — AI Application Engineering Suite
**Target Position:** AI Application Engineer  
**Job Reference:** `AI Application – E/IID/2026`  
**Candidate:** **Roy Khaemba** (`peddipedderu`)  
**Live Production URL (Fly.io):** [https://coopbank-ai-engineer.fly.dev](https://coopbank-ai-engineer.fly.dev)  
**Interactive API Documentation:** [https://coopbank-ai-engineer.fly.dev/docs](https://coopbank-ai-engineer.fly.dev/docs)  
**GitHub Repository:** [https://github.com/peddipedderu/cooperative-bank-ai-application-engineer](https://github.com/peddipedderu/cooperative-bank-ai-application-engineer)

---

## 🏛️ Executive Summary & Architectural Vision

This repository showcases production-grade, enterprise-ready AI application capabilities specifically engineered for **Co-operative Bank of Kenya ("The Kingdom Bank")**. 

In strict adherence to the **AI Application Engineer (Ref: AI Application – E/IID/2026)** role specification, this platform bridges the critical divide between raw machine learning models developed by Data Scientists and secure, high-throughput banking channels (MCo-op Cash, Internet Banking, USSD \*667#, Omnichannel CRMs, and Core Banking Systems).

### Core Differentiator: Separation of Concerns
```
┌────────────────────────────────────────────────────────┐
│     Customer Channels (MCo-op Cash, Web, USSD, RM)     │
└──────────────────────────┬─────────────────────────────┘
                           │ HTTPS / TLS 1.3 / OAuth 2.0
┌──────────────────────────▼─────────────────────────────┐
│       AI Application Engineering Layer (This Suite)    │
│  - FastAPI Microservices & Asynchronous Gateway        │
│  - Prompt Engineering & Dynamic Context Assembly        │
│  - Responsible AI Guardrails & Injection Defense       │
│  - Tool-Calling Autonomous Agent Orchestration         │
│  - Immutable Audit Ledger & Explainability Telemetry   │
└──────────────┬──────────────────────────┬──────────────┘
               │                          │
┌──────────────▼────────────┐ ┌───────────▼──────────────┐
│  Data Science & ML Models │ │  Core Banking & Payments │
│  - RAG Vector Store       │ │  - Core Banking (T24)    │
│  - Credit Risk Models     │ │  - M-PESA B2C/C2B Engine │
│  - Fine-Tuned LLMs        │ │  - CRB & Fraud Screening │
└───────────────────────────┘ └──────────────────────────┘
```

---

## 🚀 Key Functional Capabilities

### 1. 🤖 Grounded Conversational RAG Assistant (`/api/chat`)
- Grounded on Co-operative Bank lending products, account opening guidelines, and MCo-op Cash transaction rules.
- Prevents hallucinations through strict retrieval grounding and confidence threshold gating.
- Dynamic output formatting with actionable next steps (e.g., links to loan pre-qualification, branch routing, or mobile money initiation).

### 2. 🛡️ Responsible AI Guardrails & Zero-Trust Defense
- Aligned with **Central Bank of Kenya (CBK)** Prudential Guidelines and the **Kenya Data Protection Act (2019)**.
- Pre-execution input sanitization detecting prompt injections, jailbreaks, and adversarial attacks.
- Output compliance verification blocking illicit financial advice or unregulated promises.
- Immutable, cryptographically traceable audit records logged via `/api/audit-trail`.

### 3. 📄 Intelligent Document Processing (IDP) (`/api/parse-document`)
- Automated parsing and entity extraction for bank statements, M-PESA payment receipts, and national KYC identification documents.
- Extracts opening/closing balances, transaction frequency, turnover velocity, and credit-worthiness signals.

### 4. ⚙️ Autonomous AI Agent Tool-Calling Workflows (`/api/agent/tools`)
- Multi-step reasoning pipeline enabling banking agents to invoke approved backend tools:
  - `check_balance`: Authenticated balance inquiry with OAuth2 token scoping.
  - `apply_for_loan`: Automated pre-fill from profile and credit telemetry.
  - `fraud_alert`: Anomaly-triggered emergency debit freeze.
  - `escalate_human`: Human-in-the-loop escalation workflow for transactions exceeding digital ceilings (KES 300,000+).

### 5. 💡 Hyper-Personalized Banking Product Recommender (`/api/recommend`)
- Real-time recommendation engine taking into account customer age, turnover band, existing credit facilities, and business registration status to suggest Co-op Bank products (e.g., MCo-op Cash Salary Advance, Biashara Loans, Asset Finance, CIC MMF).

---

## 🛠️ Technology Stack & Engineering Standards

- **Runtime & Language:** Python 3.11+, FastAPI (Async ASGI)
- **Containerization & Deployment:** Docker, Fly.io edge deployment (isolated custom port 8080)
- **Validation & Serialization:** Pydantic v2
- **Testing & Quality Assurance:** Pytest, HTTPX TestClient, 100% endpoint test coverage
- **Security & Observability:** OWASP API Top 10 mitigation, Structured Logging, Traceable UUID Session IDs, Append-Only Compliance Auditing

---

## 🏃 Running Locally & Testing

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/peddipedderu/cooperative-bank-ai-application-engineer.git
cd cooperative-bank-ai-application-engineer

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the Development Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```
Open [http://localhost:8080](http://localhost:8080) in your browser.

### 3. Run Automated Tests
```bash
pytest tests/ -v
```

---

## 🌐 Live Cloud Deployment (Fly.io)

This application is deployed and running live on Fly.io:
- **Web Interface:** [https://coopbank-ai-engineer.fly.dev](https://coopbank-ai-engineer.fly.dev)
- **Swagger Documentation:** [https://coopbank-ai-engineer.fly.dev/docs](https://coopbank-ai-engineer.fly.dev/docs)
- **Health Check:** [https://coopbank-ai-engineer.fly.dev/health](https://coopbank-ai-engineer.fly.dev/health)

---

## 👤 Candidate Profile & Competitive Differentiators

- **Name:** Roy Khaemba (peddipedderu)
- **Role:** AI Application Engineer & Cybersecurity Specialist
- **Education:** B.Sc. in Actuarial Science (Dedan Kimathi University of Technology) — Quantitative Risk Modeling, Financial Statistics, and Algorithmic Logic
- **Competitive Rankings:** HackTheBox Hero, HackerOne Bug Hunter, Active Hugging Face & Kaggle Creator
- **Professional Profiles:**
  - **GitHub:** [https://github.com/peddipedderu](https://github.com/peddipedderu)
  - **Hugging Face:** [https://huggingface.co/peddipedderu](https://huggingface.co/peddipedderu)
  - **Kaggle:** [https://www.kaggle.com/peddipedderu](https://www.kaggle.com/peddipedderu)
  - **Portfolio:** [https://digitalfundi.co.ke](https://digitalfundi.co.ke)
  - **Email:** [roykhaemba00@gmail.com](mailto:roykhaemba00@gmail.com)
  - **Phone:** +254 743 192 968
