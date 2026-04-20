# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: C401 - C5
- [REPO_URL]: https://github.com/nam-k-nguyen/Lab13-C401-C5
- [MEMBERS]:
  - Member A: [Name] | Role: Logging & PII
  - Member B: Lê Hữu Hưng | Role: Tracing & Enrichment
  - Member C: [Name] | Role: SLO & Alerts
  - Member D: [Name] | Role: Load Test & Dashboard
  - Member E: [Name] | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: /100
- [TOTAL_TRACES_COUNT]: 20
- [PII_LEAKS_FOUND]: 

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: [Path to image]
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: [Path to image]
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: docs/screenshots/trace_waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: The single "run" span (L0, 150ms) captures the full agent pipeline: RAG retrieval + LLM generation. Metadata shows quality_score=0.8, doc_count=1, and query_preview with PII already redacted before logging.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: [Path to image]
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | |
| Error Rate | < 2% | 28d | |
| Cost Budget | < $2.5/day | 1d | |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: [Path to image]
- [SAMPLE_RUNBOOK_LINK]: [docs/alerts.md#L...]

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: (e.g., rag_slow)
- [SYMPTOMS_OBSERVED]: 
- [ROOT_CAUSE_PROVED_BY]: (List specific Trace ID or Log Line)
- [FIX_ACTION]: 
- [PREVENTIVE_MEASURE]: 

---

## 5. Individual Contributions & Evidence

### [MEMBER_A_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: (Link to specific commit or PR)

### Lê Hữu Hưng
- [TASKS_COMPLETED]: Rewrote app/tracing.py to use Langfuse v4 API (observe, get_client, propagate_attributes). Updated app/agent.py to propagate tags (lab/qa/summary/model/env) and log metadata/usage per generation. Updated mock_rag.py corpus and sample_queries.jsonl for UK Travel Advisor theme. Verified 20 traces in Langfuse with correct tags and structure.
- [EVIDENCE_LINK]: - https://github.com/nam-k-nguyen/Lab13-C401-C5/commit/7bf2caa

### [MEMBER_C_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

### [MEMBER_D_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

### [MEMBER_E_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: (Description + Evidence)
- [BONUS_AUDIT_LOGS]: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]: (Description + Evidence)
