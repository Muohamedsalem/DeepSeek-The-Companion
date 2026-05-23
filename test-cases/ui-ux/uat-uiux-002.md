# UAT-UIUX-002: Usability & Accessibility Metrics

| Field | Value |
|-------|-------|
| **Scenario ID** | UAT-UIUX-002 |
| **Title** | Measure Time-to-Click and Error Rate for Button Access |
| **Test Type** | UX / Performance |
| **Severity** | Medium |

## Test Steps (Compare Old vs New Position)

| Step | Action | Old Position (Baseline) | New Position (Test) |
|------|--------|------------------------|---------------------|
| 1 | Measure time from "finish typing" to "clicking Deep Think" | ___ seconds | ___ seconds |
| 2 | Measure time from "finish typing" to "clicking Search" | ___ seconds | ___ seconds |
| 3 | Attempt to click buttons while side panel is open | Success? (Y/N) | Success? (Y/N) |
| 4 | Rate visual clarity (1-5 scale) | ___ /5 | ___ /5 |

## RTL-Specific Test

| Step | Action (Arabic Interface) | Expected Result |
|------|--------------------------|------------------|
| 1 | Set interface language to Arabic (RTL) | Buttons mirror to top-right? Or stay top-left? |
| 2 | Verify buttons do not overlap with logo or menu | Clear separation |
| 3 | Click buttons and send Arabic prompts | Buttons activate correctly |

## Acceptance Criteria

| Level | Description |
|-------|-------------|
| ✅ Pass | Time-to-click reduced by ≥20% OR user rates clarity ≥4/5; RTL layout is clean |
| ⚠️ Partial | Time unchanged but user prefers new position |
| ❌ Fail | Time increased or RTL layout breaks |
