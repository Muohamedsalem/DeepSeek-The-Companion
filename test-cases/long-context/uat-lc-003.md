# UAT-LC-003: 50 Repetitions of the Same Question – Stability Test

| Field | Value |
|-------|-------|
| **Scenario ID** | UAT-LC-003 |
| **Title** | 50 Repetitions of the Same Question – Robustness & Consistency |
| **Test Type** | Long Context / Robustness |
| **V-Model Phase** | Acceptance |
| **Severity** | High |
| **Assigned To** | Mohamed Salem |
| **Status** | Pending |

## Fixed Question (to be repeated 50 times)

> "Based on everything we discussed earlier about UAT and V-Model, what is the single most important step to ensure user acceptance testing quality?"

## Execution Steps

1. Start a new conversation or continue from a context containing summaries from UAT-LC-001 and results from UAT-LC-002.
2. Ask the fixed question above.
3. Record answer #1.
4. Repeat the **exact same question** (copy-paste) 49 more times.
5. Do **not** provide any intermediate summaries during repetition (raw endurance test).
6. Every 10 repetitions, note whether the answer changed significantly.

## Acceptance Criteria

| Level | Description |
|-------|-------------|
| **✅ Excellent** | Answers are logically varied (adding new angles), no contradictions, relevant even at repetition 50 |
| **⚠️ Acceptable** | 30–49 answers are verbatim or very similar, but no crash |
| **❌ Fail** | Complete crash before repetition 40 (illogical answers, error message, or stop) |

## Answer Log Template

| Repetition | Answer Summary | Varied? (Y/N) |
|------------|----------------|----------------|
| 1 | | |
| 10 | | |
| 20 | | |
| 30 | | |
| 40 | | |
| 50 | | |

## Notes

- The model may get bored and repeat the same phrase – this is expected. Real failure is loss of meaning or going off-topic.
