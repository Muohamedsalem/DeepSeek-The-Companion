# NFT-SEC-001 | Importing a Corrupted or Malicious File
**Requirement:** The system shall gracefully reject a corrupted or malformed `.dsconv` file without crashing, and display a clear, non-technical error message to the user.

**Test Steps:**
| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Create a text file named `corrupted.dsconv` that contains random, non-JSON text (e.g., "This is not a valid file"). | File is ready. |
| 2 | Start a new chat and try to import `corrupted.dsconv`. | The UI does not crash or freeze. |
| 3 | Observe the error message. | A user-friendly error appears: "Import failed. The file appears to be corrupted or is not a valid DeepSeek conversation file." |
| 4 | Try to import a file with a `.dsconv` extension but containing a malicious script payload (e.g., `<script>alert('xss')</script>`). | The file is rejected. The script is not executed. The error message is the same user-friendly one. |
