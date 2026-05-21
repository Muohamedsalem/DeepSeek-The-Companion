# UAT-CC-002 | Manual Chapter Creation & User-Initiated Control
**Requirement:** The system shall allow users to manually create a new conversation chapter at any point, independent of the automatic context-window trigger.
**User Story:** As a user who anticipates a complex new topic, I want to manually start a new chapter, so I can organize my conversation history proactively and keep my workflow clean.
**Preconditions:** An active conversation with at least 10 exchanged messages.
**Test Steps:**
| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | In an active conversation, click the conversation options menu (three dots). | A menu appears with an option: "Start New Chapter". |
| 2 | Select "Start New Chapter". | A dialog box appears: "Name this chapter (optional)" with a suggested name and a text field. |
| 3 | Enter a custom name: "Research Phase - Q3" and confirm. | The chat window refreshes. The header now reads: "Chapter 2: Research Phase - Q3". |
| 4 | Notice a system message at the top. | A message states: "Previous chapter summarized. You can review it by clicking 'Previous Chapter'." |
| 5 | Type a new prompt: "Let's begin a completely new analysis of UAT methodologies." | The model responds without pulling any specific details from Chapter 1, treating this as a fresh start. |
| 6 | Click the "Previous Chapter" button. | The view smoothly transitions back to the end of Chapter 1, displaying the last messages from it. |

**Postconditions:** The conversation now has two distinct, navigable chapters.

**Ethical Check:** Does the user clearly understand that the new chapter starts fresh? Is there an option to pull specific context from a previous chapter if needed?
