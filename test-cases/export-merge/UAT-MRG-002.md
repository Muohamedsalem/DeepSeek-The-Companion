# UAT-MRG-002 | Merging Conversations with Conflicting Information
**Requirement:** When merging two or more `.dsconv` files with contradictory instructions, the system shall identify the conflict and ask the user for guidance instead of silently choosing or failing.
**User Story:** As a project manager merging meeting notes from two different teams, I want the model to flag when the two meetings made conflicting decisions, so I can resolve the conflict consciously.
**Preconditions:**
- `Project_TeamA.dsconv`: A conversation where the agreed deadline for a task is "June 15th".
- `Project_TeamB.dsconv`: A conversation where the agreed deadline for the *same* task is "July 1st".

**Test Steps:**
| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Start a new empty chat session. | The chat interface is blank. |
| 2 | Import both `Project_TeamA.dsconv` and `Project_TeamB.dsconv`. | Notification: "Two context files imported. Analyzing for consistency..." |
| 3 | Wait for the analysis to complete. | A system message appears: "Conflict Detected: The deadline for [Task Name] is recorded as 'June 15th' in one source and 'July 1st' in another. Which one should I use?" with options for each, or "Ask me later". |
| 4 | Select "Use July 1st". | The model confirms: "Context updated. Deadline for [Task Name] set to July 1st." |
| 5 | Now ask: "What is the final deadline for [Task Name]?" | The model correctly responds: "July 1st." It does not mention the conflict anymore, proving it was resolved. |

**Ethical Check:** The model must never resolve a factual conflict on its own without explicit user direction. The user must be clearly shown that two different "truths" existed.
