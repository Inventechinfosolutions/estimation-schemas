# F02-006 — Reference Masters

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-006 |
| Feature Name | Reference Masters |
| Module | 02 — Examination Configuration & Masters |
| Module Type | Business |
| Release | Go-live |

### Description
Generic maintenance of reference data: departments, boards and corporations, designations, districts and taluks, document types, rejection reasons, malpractice categories, incident types and holiday calendar, with import / export.

### Business Objective
Consistent lists for forms, rules and reports.

### Actors
- KEONICS Administrator

### User Journey
1. **Who creates:** The administrator creates master entries.
2. **How they create:** Entries are added with code and bilingual names, or imported.
3. **How they edit:** Entries are edited or deactivated.
4. **How they send for approval:** No approval needed.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Users see active entries.
8. **How the approver / auditor sees history:** Auditors see changes.

### Functional Capabilities
- Generic master framework
- Bilingual names
- Import / export
- Holiday calendar

### UI Screens
- Master selector and list
- Entry form
- Import result

### Logical API Operations
- Generic master CRUD
- Import / export
- Lookup service

### Inputs
- Entries

### Outputs
- Lists

### Business Rules
- In-use entries deactivated, not deleted

### Validations
- Unique codes

### Calculations
- None

### Workflow
Active ↔ Inactive

### Search Requirements
- Entries

### Documents
- None

### Reports
- Exports

### Notifications
- None

### Security
- Admin only

### Integrations
- Departments may be seeded from HRMS

### Dependencies
- All modules

### Assumptions
- Initial data from KEONICS

### Risks
- None

### Non Functional Requirements
- Look-ups under 200 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Master selector and list | Easy | 4 |
| UI | Entry form | Easy | 4 |
| UI | Import result | Easy | 4 |
| API | Generic master CRUD | Medium | 6 |
| API | Import / export | Medium | 6 |
| API | Lookup service | Easy | 4 |
| Database | Generic master store | Easy | 2 |
| Testing | Master tests | Easy | 4 |
| Documentation | Masters guide | Simple | 1 |

**Feature Total: 35 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 16 | 2 | 0 | 4 | 1 | **35** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Generic framework
- No external integration channel in this feature; Integration row omitted.
