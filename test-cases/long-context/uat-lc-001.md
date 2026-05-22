# UAT-LC-001: Testing Long Conversation Handling Using Periodic Summaries

| Field | Value |
|-------|-------|
| **Scenario ID** | UAT-LC-001 |
| **Title** | Bypassing "Conversation Length" Message via Periodic Summaries & Static File |
| **Test Type** | Long Context / Functional |
| **V-Model Phase** | Acceptance |
| **Severity** | High |
| **Assigned To** | Mohamed Salem |
| **Status** | In Progress |
| **Date Created** | 2026-05-22 |
| **DeepSeek Version** | V4 (100k token context) |

---

## 📌 Related Requirements
- **REQ-LC-01**: The platform must support continuous conversations of at least 150 replies without a "conversation length" error.
- **REQ-LC-02**: Response accuracy must remain acceptable (≥80% meaning retention) after merging summaries.

---

## 🧪 Test Environment
- Browser: Chrome / Edge (latest)
- DeepSeek Account: Active
- Static side file: `summary-storage.json` (saved locally)
- Tracking tool: GitHub Projects

---

## 📝 Execution Steps

| Step | Action | Expected Result |
|------|--------|------------------|
| 1 | Start a new conversation on DeepSeek | Welcome message appears |
| 2 | Send first 10 messages (simulate long discussion about UAT & V-Model) | Normal conversation flow |
| 3 | After every 10 replies, tester asks: "Summarize the last 10 replies in 5 bullet points" | Model provides clear summary |
| 4 | Copy summary and save it into `summary-storage.json` with timestamp | File updates successfully |
| 5 | Repeat steps 2–4 until reaching 100 replies | No error message appears |
| 6 | At reply 101, tester enters: "Continue based only on the last summary (ignore older details)" | Model responds smoothly |
| 7 | Continue conversation until 150 replies | Performance remains stable |

---

## ✅ Acceptance Criteria

| Level | Description |
|-------|-------------|
| **✅ Full Pass** | Reach 150 replies without any "conversation length" message or unexpected halt |
| **⚠️ Partial Pass** | Reach 100 replies with only one warning message |
| **❌ Fail** | "Conversation length" message appears before 100 replies, or replies stop completely |

---

## 📊 Execution Log

| Date | Status | Notes |
|------|--------|-------|
| 2026-05-22 | In Progress | Test environment ready |

---

## 🐛 Potential Issues & Suggested Fixes
- **Issue**: Warning message at 80 replies  
  **Fix**: Reduce each summary to 3 bullet points only.

- **Issue**: Drop in response accuracy after merging  
  **Fix**: Add mandatory instruction: "Confirm your understanding before answering."

---

## 📎 References
- [Long Context Strategies – Internal Documentation]
- [V-Model in Acceptance Testing]
