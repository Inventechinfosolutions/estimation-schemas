# F03-005 — Attendance Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-005 |
| **Feature Name** | Attendance Management |
| **Module** | 03 — HRMS Core Personnel Management |

### Description
Attendance is recorded (manual mark or imported punch). The staff member or HR raises exceptions; the supervisor decides. Everyone sees history.

### Business Objective
Keep an attributable attendance register with exception workflow.

### Actors
User: HR/office clerk records or imports daily attendance. Staff member raises an exception (missed punch, on-duty). Supervisor decides exceptions. Auditor: read-only history.

### User Journey
1. Who creates: HR/office clerk records or imports daily attendance. Staff member raises an exception (missed punch, on-duty). Supervisor decides exceptions.
2. How they create: Clerk opens Attendance register for a date/office, marks Present/Absent/On leave (leave comes from approved leave) or runs import. Staff member opens My Attendance → Raise exception for a date, states reason, Save draft.
3. How they edit: Clerk can correct a day's mark only before freeze. Exception drafts can be edited. Frozen days require an exception request.
4. How they send for approval: Staff submits the exception to the supervising Post. Clerk freeze of a day may require HR Checker if configured.
5. How the approver sees pending items: Supervisor opens Attendance exception inbox.
6. How the approver decides: Supervisor Approve exception (updates the day's mark) or Reject with remarks.
7. How the user sees history: Staff opens My Attendance calendar and drill-down history of marks and exceptions.
8. How the supervisor / auditor sees history: Supervisor sees team attendance and exception decisions. Auditor sees freeze and exception log.

### Functional Capabilities
- Authorised user creates, edits and searches attendance exception records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Attendance exception register | Medium |
| Attendance exception form (create and edit) | Complex |
| Attendance exception history | Medium |
| Attendance register (day/office grid) | Complex |
| My Attendance calendar | Medium |
| Exception form | Medium |
| Exception inbox | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create attendance exception | Medium |
| Update attendance exception | Medium |
| Search attendance exception | Medium |
| Read attendance exception history | Easy |
| Save daily attendance mark | Medium |
| Import attendance file | Very High |
| Submit attendance exception | Complex |
| Decide exception | Complex |

### Inputs
Date, Person, mark, exception reason, remarks.

### Outputs
Persisted attendance exception; searchable register; history.

### Business Rules
- Approved leave automatically marks On leave for those dates.
- Frozen attendance is not silently overwritten.

### Validations
- One mark per Person per date.
- Exception requires a date and reason.

### Calculations
None beyond counts of present/absent in the register.

### Workflow
Staff submits the exception to the supervising Post. Clerk freeze of a day may require HR Checker if configured.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Optional duty order for on-duty exception.

### Reports
Daily attendance by office; exception register.

### Notifications
On-screen confirmation. Optional notice to the user on save failure.

### Security
Need-to-know by Post. Actions attributed to Person acting in a Post.

### Integrations
Module 01 identity. Document store if attachments are used.

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

### Assumptions
- Hours use Estimation Master values only, at capability grain (not one billed row per screen).

### Risks
Unscoped access would expose records outside the user's office.

### Non Functional Requirements
Register and history remain searchable during office hours.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Attendance exception register | UI | Medium | 6 |
| Attendance exception form (create and edit) | UI | Complex | 12 |
| Attendance exception history | UI | Medium | 6 |
| Attendance register (day/office grid) | UI | Complex | 12 |
| My Attendance calendar | UI | Medium | 6 |
| Exception form | UI | Medium | 6 |
| Exception inbox | UI | Medium | 6 |
| Create attendance exception | API | Medium | 6 |
| Update attendance exception | API | Medium | 6 |
| Search attendance exception | API | Medium | 6 |
| Read attendance exception history | API | Easy | 4 |
| Save daily attendance mark | API | Medium | 6 |
| Import attendance file | API | Very High | 16 |
| Submit attendance exception | API | Complex | 8 |
| Decide exception | API | Complex | 8 |
| Attendance exception record and history | DB | Medium | 4 |
| Internal identity/document hooks for attendance exception | Integration | Simple | 4 |
| Attendance Management feature tests | Testing | Very High | 12 |
| Attendance Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **137** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
