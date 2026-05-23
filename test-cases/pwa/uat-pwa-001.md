# UAT-PWA-001: Progressive Web App Installation & Core Functionality

| Field | Value |
|-------|-------|
| **Scenario ID** | UAT-PWA-001 |
| **Title** | PWA Installation, Offline Support, and Basic Chat Continuity |
| **Test Type** | Functional / Offline / Installation |
| **V-Model Phase** | Acceptance |
| **Severity** | Critical |
| **Assigned To** | Mohamed Salem |
| **Status** | Ready for Execution |

## Related Requirements (Hypothetical for DeepSeek Chat PWA)
- REQ-PWA-01: The platform must be installable as a PWA on desktop and mobile browsers.
- REQ-PWA-02: The app must load a cached offline page when network is unavailable.
- REQ-PWA-03: User conversations must persist after restarting the app and when coming back online.

## Test Environment
- Browser: Chrome / Edge / Safari (iOS) / Firefox
- OS: Windows 11, macOS, Android 13, iOS 16+
- Network: Online → Airplane mode → Online

## Test Steps

| Step | Action | Expected Result |
|------|--------|------------------|
| 1 | Open DeepSeek Chat in a supported browser | Page loads normally |
| 2 | Click "Install" from the browser’s address bar or menu | PWA installation prompt appears |
| 3 | Complete installation and launch the standalone PWA | App opens without browser toolbar, shows correct name and icon |
| 4 | Start a new conversation and send at least 5 messages | Messages appear and are saved |
| 5 | Enable airplane mode (disconnect internet) | App does not crash. Shows a friendly offline message or cached page |
| 6 | Type a message while offline | Message is queued or shows "offline – will send when online" |
| 7 | Disable airplane mode (reconnect) | Queued message is sent automatically. Conversation history intact |
| 8 | Close the PWA completely and reopen it | Previous conversation is still present |
| 9 | In the PWA, start a new conversation and send 3 messages, then hard refresh (Ctrl+F5) | Conversation should survive refresh (service worker cache) |

## Acceptance Criteria

| Level | Description |
|-------|-------------|
| **✅ Full Pass** | All steps work as expected; offline queue and persistence flawless |
| **⚠️ Partial Pass** | Installation works, but offline queue fails or history lost after refresh |
| **❌ Fail** | Cannot install PWA, or app crashes on offline step |

## Notes
- On iOS, PWA installation is done via "Share" → "Add to Home Screen".
- Service worker updates should be tested later in UAT-PWA-002.
- This test focuses on installation and basic offline/online transition.

## Related Issues
- GitHub Issue #618: [Turn DeepSeek Chat into a PWA](https://github.com/deepseek-ai/awesome-deepseek-integration/issues/618)
