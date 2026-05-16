# UAT-CC-001 | Automatic Chapter Suggestion Trigger

**Requirement:** The system shall automatically suggest creating a new "Conversation Chapter" when the context window approaches its limit.

**Acceptance Criteria:**
1. At ~90% context consumption, a gentle notification must appear.
2. Notification offers "Start New Chapter" and "Not Now".
3. Selecting "Start New Chapter" saves a summary and opens a fresh Chapter 2.
4. The summary is displayed at the start of Chapter 2.

**Test Steps:**
| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Start a new chat. | Empty interface. |
| 2 | Enter: "My name is Mohamed, a Project Lead..." | Model responds. |
| 3 | Continue a very long conversation. | Conversation continues. |
| 4 | Observe the interface near the limit. | Notification appears with two options. |
| 5 | Click "Start New Chapter". | "Chapter 2" appears with a summary of Chapter 1. |
| 6 | Prompt: "Based on the summary, write the full test plan." | Model generates a coherent plan using the summary. |
| 7 | Click "Previous Chapter" button. | View returns to Chapter 1. |

**Ethical Check:**
- No dark patterns used to coerce the user.
- User is informed that a summary is being saved.
