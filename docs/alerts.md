# Alert Rules and Runbooks (UK Travel Advisor)

## 1. High latency P95 (Bắt lỗi rag_slow)
- Severity: P2
- Trigger: `latency_p95_ms > 3000 for 5m`
- Impact: Khách du lịch phải chờ lâu, gây trải nghiệm tệ khi đang di chuyển.
- First checks:
  1. Kiểm tra Langfuse để xem RAG span có bị chậm không (incident `rag_slow`).
  2. Kiểm tra kết nối đến Vector Database chứa thông tin địa danh Anh.
- Mitigation:
  - Tạm thời giới hạn độ dài câu hỏi.
  - Chuyển sang dùng bộ nhớ cache cho các câu hỏi phổ biến (như "thời tiết London").

## 2. High error rate (Bắt lỗi tool_fail)
- Severity: P1
- Trigger: `error_rate_pct > 2.0 for 5m`
- Impact: Hệ thống không thể trả lời câu hỏi, chatbot bị "đơ".
- First checks:
  1. Tra cứu logs theo `error_type` để xem lỗi tại Agent hay tại Tool (incident `tool_fail`).
  2. Kiểm tra API Key của LLM hoặc dịch vụ bản đồ/thời tiết.
- Mitigation:
  - Tạm thời tắt các công cụ bị lỗi (ví dụ: tư vấn Visa).
  - Trả về câu trả lời mặc định hướng dẫn khách liên hệ tổng đài du lịch.

## 3. Cost budget spike (Bắt lỗi cost_spike)
- Severity: P2
- Trigger: `avg_cost_usd > 1.0 for 10m`
- Impact: Chi phí vận hành tăng vọt, vượt ngân sách của nhóm.
- First checks:
  1. Kiểm tra tokens_out trong Langfuse xem AI có đang trả lời quá dài không (incident `cost_spike`).
  2. Xác định xem có User nào đang spam các câu hỏi phức tạp không.
- Mitigation:
  - Áp dụng giới hạn số lượng token tối đa cho mỗi câu trả lời.
  - Chuyển bớt các request đơn giản sang model rẻ tiền hơn.

## 4. Low quality score (Chất lượng kém)
- Severity: P2
- Trigger: `quality_avg < 0.85 for 15m`
- Impact: Thông tin tư vấn du lịch bị sai lệch hoặc không hữu ích.
- First checks:
  1. Đọc lại các câu trả lời gần nhất trong logs để xem nội dung có bị "ngáo" không.
  2. Kiểm tra độ khớp giữa câu hỏi của khách và dữ liệu hội thoại.
- Mitigation:
  - Cập nhật lại System Prompt để định hướng AI tốt hơn.
  - Bổ sung thêm dữ liệu chuẩn về du lịch Anh vào RAG.

## 5. Traffic spike (Lưu lượng tăng đột biến)
- Severity: P3
- Trigger: `traffic > 50 for 5m`
- Impact: Hệ thống có nguy cơ bị quá tải hoặc bị tấn công DDoS.
- First checks:
  1. Kiểm tra `user_id_hash` trong logs xem có dấu hiệu spam từ 1 người dùng không.
  2. Xem có sự kiện du lịch đặc biệt nào ở Anh đang diễn ra không (ví dụ: Olympic, Lễ hội).
- Mitigation:
  - Bật chế độ giới hạn tần suất yêu cầu (Rate limiting).
  - Tăng cấp server hoặc mở rộng quy mô (nếu có thể).
