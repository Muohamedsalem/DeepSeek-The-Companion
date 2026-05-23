# UAT-UIUX-001: Relocation of 'Deep Think' & 'Search' Buttons

| Field | Value |
|-------|-------|
| **Scenario ID** | UAT-UIUX-001 |
| **Title** | Verify Functionality After Moving Buttons to Top-Left |
| **Test Type** | UI / Functional |
| **V-Model Phase** | Acceptance |
| **Severity** | High |
| **Assigned To** | Mohamed Salem |

## Test Steps

| Step | Action | Expected Result |
|------|--------|------------------|
| 1 | Locate 'Deep Think' button at top-left of chat interface | Button is visible and clearly labeled |
| 2 | Click 'Deep Think' button before typing a message | Button highlights to indicate activation |
| 3 | Send a complex analytical question | Model response shows deep reasoning (takes longer, shows thinking steps) |
| 4 | Locate 'Search' button at top-left | Button is visible next to 'Deep Think' |
| 5 | Click 'Search' button and ask a question about recent events | Model indicates it is searching the web |
| 6 | Open side panel (e.g., history) and repeat steps 2-5 | Buttons remain visible and functional, not obscured |

## Acceptance Criteria

| Level | Description |
|-------|-------------|
| ✅ Pass | All buttons functional, visible, and not obscured by side panels |
| ❌ Fail | Any button is hidden, non-functional, or loses its state after panel opens |
