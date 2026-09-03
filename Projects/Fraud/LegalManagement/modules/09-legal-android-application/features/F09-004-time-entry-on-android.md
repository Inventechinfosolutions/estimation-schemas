# F09-004 — Time entry on Android

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-004 |
| **Feature Name** | Time entry on Android |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
The user records a time entry against the matter (date, duration, activity) and saves. The matter dashboard shows the entry.

### Business Objective
Capture advocate/Legal Cell time against the matter from Android so the matter dashboard shows the entry.

### Actors
Advocate; Legal Cell.

### User Journey
1. Who creates: Advocate
2. How they create: User records a time entry against the matter (date, duration, activity) and saves.
3. How they edit: The matter dashboard (web and device) shows the entry.
4. How they send for approval: The matter dashboard (web and device) shows the entry. Enter time → save → dashboard.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Android Time-Entry form
- Time list on the matter
- Date, duration, activity against the matter
- Not payroll; not EVAL billing

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Android Time-Entry form | Complex |
| Time list on the matter | Easy |
| Time entry on android history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Time save operations | Medium |
| Update time entry on android | Medium |
| Search time entry on android | Medium |
| Read time entry on android history | Easy |

### Inputs
Matter; date; duration; activity.

### Outputs
Time entry on matter dashboard.

### Business Rules
- Time is matter-bound.
- Not a reimbursement or salary engine.

### Validations
- Matter required; duration > 0; date required.

### Calculations
Duration as entered; optional daily total on the matter.

### Workflow
Enter time → save → dashboard.

### Search Requirements
Time entries on the matter by date.

### Documents
None.

### Reports
Consumed on dashboard; formal reports remain web where specified.

### Notifications
None required.

### Security
Attributed to shared Person.

### Integrations
Matter dashboard consume (Easy).

### Dependencies
F04-002; F01-004.

### Assumptions
- Activity list from F02-005.

### Risks
Double entry from web and Android without duplicate warning.

### Non Functional Requirements
Quick capture after hearing.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Android Time-Entry form | UI | Complex | 12 |
| Time list on the matter | UI | Easy | 4 |
| Time entry on android history | UI | Medium | 6 |
| Time save operations | API | Medium | 6 |
| Update time entry on android | API | Medium | 6 |
| Search time entry on android | API | Medium | 6 |
| Read time entry on android history | API | Easy | 4 |
| Time entry on android persistence | DB | Medium | 4 |
| Matter dashboard consume | Integration | Easy | 8 |
| Time entry on Android feature tests | Testing | Easy | 4 |
| Time entry on Android implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
