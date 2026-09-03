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
1. Who creates: Advocate
2. How they create: User opens Attendance/Expense Search.
3. How they edit: Searches by date, court, matter, person or category.
4. How they send for approval: Opens the matching attendance or expense record. Enter filters → results → open.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Attendance/Expense Search
- Result detail
- Filters: date, court, matter, person, category
- Open record

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Attendance/Expense Search | Medium |
| Result detail | Easy |
| Search attendance and expense history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search operations | Medium |
| Update search attendance and expense | Medium |
| Search search attendance and expense | Medium |
| Read search attendance and expense history | Easy |

### Inputs
Date range; court; matter; person; expense category.

### Outputs
Match list; opened record.

### Business Rules
- An attendance row is retrievable by date, court, matter or person and shows cause-list upload.
- Visibility follows matter rights.

### Validations
- At least one filter or text as configured; results scoped to visible matters.

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
- Not Boolean library search.

### Risks
Person filter must use shared Person, not a local name spelling fork.

### Non Functional Requirements
Quick search as Annexure-I.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Attendance/Expense Search | UI | Medium | 6 |
| Result detail | UI | Easy | 4 |
| Search attendance and expense history | UI | Medium | 6 |
| Search operations | API | Medium | 6 |
| Update search attendance and expense | API | Medium | 6 |
| Search search attendance and expense | API | Medium | 6 |
| Read search attendance and expense history | API | Easy | 4 |
| Search attendance and expense persistence | DB | Medium | 4 |
| Internal retrieve | Integration | Simple | 4 |
| Search attendance and expense feature tests | Testing | Easy | 4 |
| Search attendance and expense implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
