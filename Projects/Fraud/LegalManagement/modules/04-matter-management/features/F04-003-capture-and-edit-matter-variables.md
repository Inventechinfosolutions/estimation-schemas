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
1. User opens Matter Variables on the matter.
2. Edits court details, matter type, details, category and issues, opponent and lawyers.
3. Saves; dashboard and F04-007 reports use the updated values.

### Functional Capabilities
- Matter Variables form (court, type, details, category, issues)
- Opponent and Lawyer child grid
- Save and version-of-record for variables
- Dashboard and reports consume updated values

### Inputs
Court details; matter type; details; category; issues; opponent; lawyers (contacts where linked).

### Outputs
Updated matter variables; change history.

### Business Rules
- Variables are the structured fields used by reports (court-wise, CA-wise, stage-wise, etc.).
- Opponent/lawyer may reference unified contacts (Module 06) when the person is in the directory.
- Central masters (F02-005) supply type/category lists — no local fork.

### Validations
Type/category from central masters; court required; dates consistent with F04-001.

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
Stage used in reports may be derived from variables plus key dates.

### Risks
Stale opponent/lawyer data misleads CA-wise reports.

### Non Functional Requirements
Saves immediately visible on the dashboard.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Matter Variables form (court, type, category, issues) | UI | Complex | 12 |
| Opponent and Lawyer child grid | UI | Medium | 6 |
| Variables save/retrieve operations | API | Medium | 6 |
| Variable entities | Database | Medium | 4 |
| Dashboard and report consume | Integration | Simple | 4 |
| Matter variables tests | Testing | Medium | 6 |
| Matter variables guide | Documentation | Easy | 2 |
| **Total** | | | **40** |

### Estimation Assumptions
- Create Matter required fields overlap is not double-counted as a second create wizard.
