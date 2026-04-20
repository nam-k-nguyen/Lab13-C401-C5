# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: C401 - C5
- [REPO_URL]: https://github.com/nam-k-nguyen/Lab13-C401-C5
- [MEMBERS]:
  - Member A: [Nguyễn khánh Nam]| Role: Logging & PII
  - Member B: [Lê Hữu Hưng] | Role: Tracing &  tags
  - Member C: [Nguyễn Minh Hiếu]| Role: SLO & Alerts
  - Member D: [Chu Minh Quân] | Role: load test + incident injection
  - Member E: [Đỗ Minh Phúc] | Role: dashboard + evidence
  - Member F: [Lê Tú Nam] | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 20
- [PII_LEAKS_FOUND]: None

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT] <br><img src="screenshots/correlation_id.png" alt="EVIDENCE_CORRELATION_ID_SCREENSHOT" width=400/>
- [EVIDENCE_PII_REDACTION_SCREENSHOT] <br><img src="screenshots/pii_log.png" alt="EVIDENCE_PII_REDACTION_SCREENSHOT" width=400/>
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: docs/screenshots/trace_waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: The single "run" span (L0, 150ms) captures the full agent pipeline: RAG retrieval + LLM generation. Metadata shows quality_score=0.8, doc_count=1, and query_preview with PII already redacted before logging.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: screenshots/dashboard_full.png

[SLO_TABLE]:

| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | [Xem Dashboard] |
| Error Rate | < 2.0% | 28d | [Xem Dashboard] |
| Daily Cost | < $20.0 | 28d | [Xem Dashboard] |
| Quality Score | > 0.85 | 28d | [Xem Dashboard] |

### 3.3 Alerts & Runbook
[ALERT_RULES_SCREENSHOT]: screenshots/alert_rules.png
[SAMPLE_RUNBOOK_LINK]: [docs/alerts.md#1-high-latency-p95](file:///e:/Lab13-C401-C5/docs/alerts.md#L3)

[ALERTS_LIST]:

1. **High Latency P95**: [Runbook](file:///e:/Lab13-C401-C5/docs/alerts.md#L3)
2. **High Error Rate**: [Runbook](file:///e:/Lab13-C401-C5/docs/alerts.md#L14)
3. **Cost Budget Spike**: [Runbook](file:///e:/Lab13-C401-C5/docs/alerts.md#L25)
4. **Low Quality Score**: [Runbook](file:///e:/Lab13-C401-C5/docs/alerts.md#L36)
5. **Traffic Spike**: [Runbook](file:///e:/Lab13-C401-C5/docs/alerts.md#L47)

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: (e.g., rag_slow)
- [SYMPTOMS_OBSERVED]: 
- [ROOT_CAUSE_PROVED_BY]: (List specific Trace ID or Log Line)
- [FIX_ACTION]: 
- [PREVENTIVE_MEASURE]: 

---

## 5. Individual Contributions & Evidence

### Nguyễn Khánh Nam
- [TASKS_COMPLETED]:
  - Implemented and registered PII scrubbing patterns in pii.py and logging_config.py
  - Added/updated regex for Vietnamese passport, address, DOB, etc.
  - Ensured PII scrubber is active in the logging pipeline
  - Updated and fixed correlation ID propagation in middleware.py
  - Ensured contextvars are cleared per request in middleware
- [EVIDENCE_LINK]:
  - [523efe0](https://github.com/nam-k-nguyen/Lab13-C401-C5/commit/523efe055f4a067aeeabf5cc43af77953c567466)
  - [17cca4e](https://github.com/nam-k-nguyen/Lab13-C401-C5/commit/17cca4e001146f7b03b3dcac494c58e838abac59)
  - [af68ea4](https://github.com/nam-k-nguyen/Lab13-C401-C5/commit/af68ea4d93c5c268d3d833fd2ded3eb0433d761e)

### Lê Hữu Hưng
- [TASKS_COMPLETED]: Rewrote app/tracing.py to use Langfuse v4 API (observe, get_client, propagate_attributes). Updated app/agent.py to propagate tags (lab/qa/summary/model/env) and log metadata/usage per generation. Updated mock_rag.py corpus and sample_queries.jsonl for UK Travel Advisor theme. Verified 20 traces in Langfuse with correct tags and structure.
- [EVIDENCE_LINK]: - https://github.com/nam-k-nguyen/Lab13-C401-C5/commit/7bf2caa

### Nguyen Minh Hieu
- [TASKS_COMPLETED]: 
    - Defined and configured Service Level Objectives (SLO) for the UK Travel Advisor system in `config/slo.yaml`.
    - Implemented 5 critical alert rules (High Latency, Error Rate, Cost Spike, Low Quality, and Traffic Spike) in `config/alert_rules.yaml`.
    - Authored comprehensive operational runbooks for incident mitigation in `docs/alerts.md`.
    - Synchronized monitoring thresholds with SLO targets to ensure high system observability.
- [EVIDENCE_LINK]: [Branch hieu-slo-alert | Commit c0b1257](https://github.com/nam-k-nguyen/Lab13-C401-C5/pull/new/hieu-slo-alert)

### Chu Minh Quan
- [TASKS_COMPLETED]: Tweak scripts to run any scenario from data/incidents.json and allow to test other test case files by modifying the script. Run tests with different incident injections and verify the results on dashboard.  
- [EVIDENCE_LINK]: https://github.com/nam-k-nguyen/Lab13-C401-C5/commit/040a253895977f86560429fa9d48ab801f530d7f/


### Đỗ Minh Phúc
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 
### LÊ TÚ NAM
- GROUP REPORT
- https://github.com/nam-k-nguyen/Lab13-C401-C5/edit/main/docs/blueprint-template.md
---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: (Description + Evidence)
- [BONUS_AUDIT_LOGS]: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]: (Description + Evidence)
