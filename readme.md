<div align="center">

  <h1>🛡️ VERITAS AI</h1>
  <h3>Real-Time News Credibility & Neural Verification Engine</h3>

  <p>
    An enterprise-grade, full-stack intelligence engine built to combat misinformation, fake news, and algorithmic clickbait. Powered by <b>FastAPI</b>, <b>Google Gemini 2.5 Flash</b>, and an ultra-responsive dark UI telemetry dashboard.
  </p>

<!-- Badges Header -->
<p align="center">
  <a href="https://github.com/your-username/your-repo-name/stargazers"><img src="https://img.shields.io/github/stars/your-username/your-repo-name?style=for-the-badge&color=7c3aed" alt="Stars"></a>
  <a href="https://github.com/your-username/your-repo-name/network/members"><img src="https://img.shields.io/github/forks/your-username/your-repo-name?style=for-the-badge&color=3b82f6" alt="Forks"></a>
  <a href="https://github.com/your-username/your-repo-name/issues"><img src="https://img.shields.io/github/issues/your-username/your-repo-name?style=for-the-badge&color=10b981" alt="Issues"></a>
  <a href="https://github.com/your-username/your-repo-name/blob/main/LICENSE"><img src="https://img.shields.io/github/license/your-username/your-repo-name?style=for-the-badge&color=f59e0b" alt="License"></a>
</p>

  <br />
</div>

---

## ⚡ Technical Highlights

- **🤖 LLM Verification Pipeline:** Leverages Google's `gemini-2.5-flash` model via structured JSON schema enforcement for sub-second, multi-variable truth index assessments.
- **📰 Live Telemetry Stream:** Synchronizes in real-time with the Hacker News Firebase API to fetch and render raw open-source network broadcasts.
- **📊 Metric Discrepancy Gauge:** Dynamic percentage-based graphical meters mapping Real vs. Fake likelihood scores with linguistic rationale summaries.
- **🛡️ Multi-Session Audit Logging:** Profile-isolated audit history tracking stored dynamically via client storage with base64 encoded re-testing triggers.
- **🎨 Futuristic Dark Telemetry UI:** Handcrafted dashboard using utility-first **Tailwind CSS**, dynamic state switching, and non-blocking DOM operations.

---

## 🏗️ Architecture & Data Flow

```mermaid
graph TD
    A[User / Live HN API] -->|News Snippet / Text| B[Frontend Dashboard]
    B -->|POST /api/verify-news| C[FastAPI Gateway]
    C -->|Environment Check & Prompt Formatting| D[Google Gemini 2.5 Flash API]
    D -->|Structured JSON Response| C
    C -->|Credibility Payload| B
    B -->|Save Session Payload| E[Browser Local Storage Logs]
    B -->|Render Dashboard| F[Telemetry UI Gauge & Index Cards]
