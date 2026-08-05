<div align="center">

  <h1>🛡️ VERITAS AI (only_Sach)</h1>
  <h3>Neural Fake News Detection & Real-Time Credibility Verification System</h3>

  <p>
    An enterprise-grade, full-stack intelligence engine built to combat misinformation, algorithmic clickbait, and unverified digital broadcasts. Powered by <b>FastAPI</b>, <b>Google Gemini 2.5 Flash</b>, and a high-performance interactive telemetry dashboard.
  </p>

<!-- Badges Header -->
<p align="center">
  <a href="https://github.com/Annugill001/only_Sach/stargazers"><img src="https://img.shields.io/github/stars/Annugill001/only_Sach?style=for-the-badge&color=7c3aed" alt="Stars"></a>
  <a href="https://github.com/Annugill001/only_Sach/network/members"><img src="https://img.shields.io/github/forks/Annugill001/only_Sach?style=for-the-badge&color=3b82f6" alt="Forks"></a>
  <a href="https://github.com/Annugill001/only_Sach/issues"><img src="https://img.shields.io/github/issues/Annugill001/only_Sach?style=for-the-badge&color=10b981" alt="Issues"></a>
  <a href="https://github.com/Annugill001/only_Sach/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Annugill001/only_Sach?style=for-the-badge&color=f59e0b" alt="License"></a>
</p>

  <br />
</div>

---

## 🚨 Problem Statement

In the modern digital information ecosystem, **misinformation spreads 6x faster than factual content**. Key challenges include:

1. **Velocity of Unverified Broadcasts:** High-volume news aggregators circulate fabricated stories faster than manual fact-checkers can verify them.
2. **Context Manipulation & Clickbait:** News items often mix partial truths with sensationalized headlines, making traditional black-and-white rule systems fail.
3. **Lack of Instant Auditability:** End-users lack a lightweight tool to instantly calculate confidence scores and review source alignment in real-time.

**VERITAS AI** addresses this gap by deploying zero-shot neural verification over structured LLM schema prompts, outputting immediate authenticity metrics and breakdown summaries.

---

## 📊 Verification Metrics & Accuracy Evaluation

The engine calculates authenticity using a probabilistic confidence scoring framework:

### 1. Confidence & Discrepancy Index
Every text input is evaluated on a $0 \text{ to } 100\%$ scale:
* **Authenticity Score ($\text{Score}_{\text{Real}}$):** Linguistic alignment with factual indices and verified corporate/press registries.
* **Discrepancy Score ($\text{Score}_{\text{Fake}}$):** Mathematical complement representing risk, bias, or fabrication:
$$\text{Score}_{\text{Fake}} = 100 - \text{Score}_{\text{Real}}$$

### 2. Evaluation Matrix

| Metric Scale | Score Range | Classification | Action Triggered |
| :--- | :--- | :--- | :--- |
| **High Credibility** | $70\% - 100\%$ | `VERIFIED / MATCHED` | Marked safe with green telemetry indicator |
| **Moderate Risk** | $40\% - 69\%$ | `UNVERIFIED / MIXED` | Flagged for contextual review (Yellow indicator) |
| **High Misinformation** | $0\% - 39\%$ | `FLAGGED MISLEADING` | High alert status (Red indicator) |

---

## 🗄️ Database & Data Handling Approach

To maintain lightweight, privacy-focused client interactions without mandatory server-side state overhead, **VERITAS AI** employs a **Hybrid Client-Isolated Session Architecture**:
