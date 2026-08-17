# F05-003 — Maturity and violation analytics

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-003 |
| **Feature Name** | Maturity and violation analytics |
| **Module** | 05 — Investment Portfolio Management |

### Description
The Officer opens portfolio analytics for a depositor or FE. The system flags investments whose maturity date is violated. The Officer reviews the flag list and uses it in verification or categorisation.

### Business Objective
Flag maturity-date violations for Officers to use in verification and categorisation.

### Actors
Officer.

### User Journey
1. Officer opens portfolio analytics for a depositor or imported FE.
2. The system flags investments whose maturity date is violated.
3. Officer reviews the flag list and uses it in verification (F07) or categorisation (F05-004).

### Functional Capabilities
- Portfolio analytics by depositor or FE.
- Flag maturity-date violations.
- Present a reviewable flag list.

### Inputs
Maturity dates, as-of date, depositor/FE scope.

### Outputs
Violation flag list.

### Business Rules
- Flags are assistive; they do not auto-categorise (F05-004) or auto-approve (F07).
- No generative commentary on violations.

### Validations
- Investments without maturity dates are listed as unknown, not as violated.

### Calculations
Maturity date versus as-of date / policy window.

### Workflow
Open analytics → review flags → use in later human decisions.

### Search Requirements
Depositor, FE, violation flag, maturity date.

### Documents
None.

### Reports
Maturity-violation list.

### Notifications
None.

### Security
Analytics respect Module 01 visibility.

### Integrations
None.

### Dependencies
F05-001.

### Assumptions
- Authority confirms what constitutes a violated maturity date.

### Risks
- Missing maturity dates would under-flag if treated as non-violated.

### Non Functional Requirements
Analytics screen is a staff dashboard-style list, filtered and practical.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Maturity violation analytics list | UI | Very High | 16 |
| Maturity flag operations | API | Complex | 8 |
| Flag persistence | DB | Medium | 4 |
| Maturity analytics tests | Testing | Complex | 8 |
| Maturity analytics note | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Uses Estimation Master values only.
- UI Very High is the analytics list/dashboard, not a simple popup.
