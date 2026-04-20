# Demo Guide — Day 13 Observability Lab

> Domain: **UK Travel Agent**. Tổng thời gian demo: 5-7 phút.

## 1. Setup trước demo (T-5 phút)

```bash
git pull origin main
pip install -r requirements.txt
cp .env.example .env          # điền LANGFUSE_PUBLIC_KEY + SECRET_KEY
rm -f data/logs.jsonl         # xóa log cũ cho sạch
uvicorn app.main:app --reload
```

Mở sẵn 3 tab browser:

1. <http://127.0.0.1:8000/dashboard> — dashboard 6 panels
2. <https://cloud.langfuse.com> — trace list
3. IDE mở `data/logs.jsonl` để show logs

## 2. Kịch bản demo chi tiết

### Phút 0:00 · SETUP (trước khi giảng viên vào)

```bash
rm -f data/logs.jsonl              # log sạch
# Restart uvicorn để reset metrics in-memory
```

Mở sẵn: dashboard, Langfuse, `data/logs.jsonl` trong IDE.

### Phút 0:00-0:30 · INTRO (Demo lead)

> "Nhóm em xây **UK Travel Advisor** — chatbot tư vấn du lịch Anh cho khách VN. Demo sẽ chứng minh 3 pillars observability: **Logs / Metrics / Traces** — dùng để debug incident live trong production."

### Phút 0:30-1:00 · BASELINE

```bash
python scripts/load_test.py --concurrency 5
```

Đợi ~40s cho bucket mới hiện lên dashboard. Chỉ vào 6 panels: "Đây là trạng thái bình thường."

### Phút 1:00-1:45 · PII + LOGS — Member A

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":"u01","session_id":"s01","feature":"qa","message":"What are the top attractions in London? My email is student@vinuni.edu.vn"}'
```

Mở `data/logs.jsonl` → chỉ vào:

- `correlation_id: req-xxxxxxxx` (unique mỗi request)
- `user_id_hash` (đã hash SHA-256, không phải raw ID)
- `[REDACTED_EMAIL]` trong payload thay vì email thật

### Phút 1:45-2:30 · TRACES — Member B

Mở Langfuse → click trace gần nhất → show:

- Waterfall span `LabAgent.run` bao trọn pipeline
- Metadata: `quality_score`, `latency_ms`, `doc_count`, `query_preview`
- Usage: `input_tokens`, `output_tokens`
- Tags: `lab`, `qa`, `claude-sonnet-4-5`, `dev`

### Phút 2:30-3:00 · SLO + ALERTS — Member C

Mở [config/slo.yaml](config/slo.yaml) + [config/alert_rules.yaml](config/alert_rules.yaml):

- 4 SLI: latency P95 < 3000ms · error < 2% · cost < $20/day · quality > 0.85
- 5 alert rules, mỗi rule có runbook link
- Click link runbook alert đầu → nhảy sang [docs/alerts.md](docs/alerts.md)

### Phút 3:00-4:30 · INCIDENT LIVE — Member D + E

**Đoạn quan trọng nhất — 10đ Incident Response.**

```bash
python scripts/inject_incident.py --scenario rag_slow
python scripts/load_test.py --concurrency 5
```

Đợi 30-40s cho dashboard refresh.

### Phút 4:30-5:15 · FLOW DEBUG 3-PILLAR (cả nhóm)

1. **METRICS** — chỉ Panel 1 dashboard: P95 vượt dashed line vàng 3000ms
2. **TRACES** — mở Langfuse, filter `latency > 3000ms`, click trace chậm nhất → show span `retrieve` chậm bất thường
3. **LOGS** — copy `correlation_id` từ trace → grep trong logs:

   ```bash
   grep "<correlation_id>" data/logs.jsonl
   ```

   → Confirm root cause = incident `rag_slow` đang bật.

### Phút 5:15-5:45 · FIX + RECOVERY

```bash
python scripts/inject_incident.py --scenario rag_slow --disable
python scripts/load_test.py --concurrency 5
```

Đợi 30s → dashboard P95 tụt về baseline.

### Phút 5:45-6:30 · VALIDATE + KẾT LUẬN

```bash
python scripts/validate_logs.py
```

Show output: "Score X/100 — schema PASS, correlation PASS, enrichment PASS, PII PASS."

> "Observability không chỉ là cài thêm tool — là kỷ luật kết nối **logs-metrics-traces qua correlation_id** để debug incident trong **phút** chứ không phải **giờ**."

## 3. Nếu demo hỏng

1. Dùng screenshots đã chụp trước trong `docs/screenshots/`
2. Show `data/logs.jsonl` có sẵn (grep correlation_id, REDACTED)
3. Chạy `python scripts/validate_logs.py` để show score

## 4. Checklist cuối cùng

- [ ] `validate_logs.py` ≥ 80/100
- [ ] Langfuse ≥ 10 traces
- [ ] Dashboard 6 panels có SLO line
- [ ] 6 screenshots trong `docs/screenshots/`
- [ ] [docs/blueprint-template.md](docs/blueprint-template.md) điền đủ tag `[...]`
- [ ] Mỗi thành viên có commit evidence
- [ ] `.env` KHÔNG commit
