# UAT-MRG-001 | Manual Merging of Multiple Conversations (The Blend)
**Requirement:** The system shall allow users to import multiple .dsconv files into a new session, creating a custom blend of contexts.
**Acceptance Criteria:**
1. Users can upload multiple .dsconv files into one conversation.
2. Model retains context from all files without confusion.
3. Model can synthesize information across imported files.
**Test Steps:**
| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Start new empty chat. | Blank. |
| 2 | Upload first file: `Project_Alpha.dsconv`. | Context imported. |
| 3 | Upload second file: `Meeting_Notes.dsconv`. | Multiple contexts recognized. |
| 4 | Prompt: "Unify test strategy from both files." | Response blends both contexts accurately. |
| 5 | Ask specific cross-file question. | Model pulls correct details from each. |
**Ethical Check:**
- Conflict resolution if files contradict.
- Clear source attribution for information.
- Ability to remove one file's context without affecting others.
