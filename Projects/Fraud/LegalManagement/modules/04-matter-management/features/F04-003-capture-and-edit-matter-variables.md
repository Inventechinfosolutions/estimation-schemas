# F04-003 — Capture and edit matter variables

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | Capture and edit matter variables |
| **Module** | 04 — Matter Management |

### Description
The user edits court details, matter type, details, category and issues, opponent and lawyers, and saves. The dashboard and reports use the updated values.

### Business Objective
Keep matter variables (court, type, category, issues, opponent and lawyers) current so the dashboard and reports stay accurate.

### Actors
Legal Cell; Advocate.

### User Journey
1. Who creates: Legal Cell
2. How they create: User opens Matter Variables on the matter.
3. How they edit: Edits court details, matter type, details, category and issues, opponent and lawyers.
4. How they send for approval: Saves; dashboard and F04-007 reports use the updated values. Open variables → edit → save → dashboard/reports refresh.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Matter Variables form (court, type, details, category, issues)
- Opponent and Lawyer child grid
- Save and version-of-record for variables
- Dashboard and reports consume updated values

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Matter Variables form (court, type, category, issues) | Complex |
| Opponent and Lawyer child grid | Medium |
| Capture and edit matter variables history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Variables save/retrieve operations | Medium |
| Update capture and edit matter variables | Medium |
| Search capture and edit matter variables | Medium |
| Read capture and edit matter variables history | Easy |

### Inputs
Court details; matter type; details; category; issues; opponent; lawyers (contacts where linked).

### Outputs
Updated matter variables; change history.

### Business Rules
- Variables are the structured fields used by reports (court-wise, CA-wise, stage-wise, etc.).
- Opponent/lawyer may reference unified contacts (Module 06) when the person is in the directory.
- Central masters (F02-005) supply type/category lists — no local fork.

### Validations
- Type/category from central masters; court required; dates consistent with F04-001.

### Calculations
None.

### Workflow
Open variables → edit → save → dashboard/reports refresh.

### Search Requirements
Via matter search on updated court, type, opponent.

### Documents
None.

### Reports
Consumed by F04-007.

### Notifications
None required.

### Security
Edit restricted to Posts allowed on the matter.

### Integrations
Dashboard/report consume (Simple); contact lookup optional.

### Dependencies
F04-001; F04-002; F02-005; F06.

### Assumptions
- Stage used in reports may be derived from variables plus key dates.

### Risks
Stale opponent/lawyer data misleads CA-wise reports.

### Non Functional Requirements
Saves immediately visible on the dashboard.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Matter Variables form (court, type, category, issues) | UI | Complex | 12 |
| Opponent and Lawyer child grid | UI | Medium | 6 |
| Capture and edit matter variables history | UI | Medium | 6 |
| Variables save/retrieve operations | API | Medium | 6 |
| Update capture and edit matter variables | API | Medium | 6 |
| Search capture and edit matter variables | API | Medium | 6 |
| Read capture and edit matter variables history | API | Easy | 4 |
| Capture and edit matter variables persistence | DB | Medium | 4 |
| Dashboard and report consume | Integration | Simple | 4 |
| Capture and edit matter variables feature tests | Testing | Medium | 6 |
| Capture and edit matter variables implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
