# NFT-PERF-001 | Export Performance with Large Conversations

**Requirement:** The system shall export a conversation containing 1,000 messages in under 10 seconds, and the UI shall remain responsive during the process.

**Test Steps:**
| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Generate or upload a conversation with exactly 1,000 messages (use a script or test data file). | The conversation is loaded successfully. |
| 2 | Start a timer and click "Export" > ".dsconv". | The download prompt appears. |
| 3 | Stop the timer when the file is saved. | The total time from click to save is less than 10 seconds. |
| 4 | While the export is running, try to scroll the chat window. | The UI remains responsive; scrolling is not blocked or jittery. |
