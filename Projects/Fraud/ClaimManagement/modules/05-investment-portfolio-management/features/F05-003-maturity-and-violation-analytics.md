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
1. Who creates: Officer
2. How they create: Officer opens portfolio analytics for a depositor or imported FE.
3. How they edit: The system flags investments whose maturity date is violated.
4. How they send for approval: Officer reviews the flag list and uses it in verification (F07) or categorisation (F05-004). Open analytics → review flags → use in later human decisions.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Portfolio analytics by depositor or FE.
- Flag maturity-date violations.
- Present a reviewable flag list.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My maturity and violation analytics list / queue | Medium |
| Maturity violation analytics list | Very High |
| Maturity and violation analytics history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Maturity flag operations | Complex |
| Update maturity and violation analytics | Medium |
| Search maturity and violation analytics | Medium |
| Read maturity and violation analytics history | Easy |

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
| My maturity and violation analytics list / queue | UI | Medium | 6 |
| Maturity violation analytics list | UI | Very High | 16 |
| Maturity and violation analytics history | UI | Medium | 6 |
| Maturity flag operations | API | Complex | 8 |
| Update maturity and violation analytics | API | Medium | 6 |
| Search maturity and violation analytics | API | Medium | 6 |
| Read maturity and violation analytics history | API | Easy | 4 |
| Flag persistence | DB | Medium | 4 |
| Maturity and violation analytics feature tests | Testing | Complex | 8 |
| Maturity and violation analytics implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
