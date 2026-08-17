# F07-003 — Search attendance and expense

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | Search attendance and expense |
| **Module** | 07 — Court Attendance & Expense Management |

### Description
The user searches by date, court, matter, person or category and opens the matching attendance or expense record.

### Business Objective
Quick retrieval of attendance and expense rows by date, court, matter, person or category.

### Actors
Advocate; Legal Cell; supervisor/CA (read).

### User Journey
1. User opens Attendance/Expense Search.
2. Searches by date, court, matter, person or category.
3. Opens the matching attendance or expense record.

### Functional Capabilities
- Attendance/Expense Search
- Result detail
- Filters: date, court, matter, person, category
- Open record

### Inputs
Date range; court; matter; person; expense category.

### Outputs
Match list; opened record.

### Business Rules
- An attendance row is retrievable by date, court, matter or person and shows cause-list upload.
- Visibility follows matter rights.

### Validations
At least one filter or text as configured; results scoped to visible matters.

### Calculations
None.

### Workflow
Enter filters → results → open.

### Search Requirements
This feature.

### Documents
Cause list and vouchers on the opened record.

### Reports
Search export optional.

### Notifications
None.

### Security
No cross-matter leak.

### Integrations
Internal (Simple).

### Dependencies
F07-001; F07-002; F04-001.

### Assumptions
Not Boolean library search.

### Risks
Person filter must use shared Person, not a local name spelling fork.

### Non Functional Requirements
Quick search as Annexure-I.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Attendance/Expense Search | UI | Medium | 6 |
| Result detail | UI | Easy | 4 |
| Search operations | API | Medium | 6 |
| Search indexes | Database | Easy | 2 |
| Internal retrieve | Integration | Simple | 4 |
| Attendance/expense search tests | Testing | Easy | 4 |
| Attendance and expense search guide | Documentation | Easy | 2 |
| **Total** | | | **28** |

### Estimation Assumptions
- Submit UIs are F07-001/F07-002.
