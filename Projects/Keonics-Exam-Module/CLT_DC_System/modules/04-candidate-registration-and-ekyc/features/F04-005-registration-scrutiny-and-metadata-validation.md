# F04-005 — Registration Scrutiny & Metadata Validation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-005 |
| Feature Name | Registration Scrutiny & Metadata Validation |
| Module | 04 — Candidate Registration & eKYC |
| Module Type | Business |
| Release | Go-live |

### Description
Automatic validation of registration metadata (mandatory fields, photo quality, HRMS / eKYC match, duplicates, age and category rules) followed by a scrutiny queue where officers accept, reject or return for correction, with bulk actions and reason codes.

### Business Objective
Ensure only valid registrations reach booking.

### Actors
- Scrutiny Officer
- KEONICS Administrator
- Candidate

### User Journey
1. **Who creates:** Registrations enter scrutiny automatically on submission or failed auto-checks.
2. **How they create:** The system runs checks and records results for the officer.
3. **How they edit:** The officer can add remarks and request documents.
4. **How they send for approval:** Returned registrations go back to the candidate; accepted ones are released for booking.
5. **How the approver sees pending items:** The officer sees a queue filtered by district, category and check results.
6. **How the approver decides:** The officer accepts, rejects or returns with reason codes; bulk accept for clean records.
7. **How the applicant / maker sees history:** The candidate sees decision and reasons.
8. **How the approver / auditor sees history:** Auditors see check results and decisions.

### Functional Capabilities
- Rule-based metadata checks
- Scrutiny queue with filters
- Check results panel
- Accept / reject / return with reasons
- Bulk accept
- Ageing and escalation

### UI Screens
- Scrutiny queue
- Registration review with check results
- Decision dialog
- Bulk accept

### Logical API Operations
- Run metadata checks
- Scrutiny queue
- Record decision
- Bulk decision
- Escalate ageing items

### Inputs
- Registrations

### Outputs
- Accepted / rejected registrations

### Business Rules
- Only accepted registrations can book
- Rejection needs reason

### Validations
- Reason codes

### Calculations
- Ageing days

### Workflow
Under Scrutiny → Accepted / Rejected / Returned

### Search Requirements
- By status, district, category

### Documents
- None

### Reports
- Scrutiny statistics

### Notifications
- Decision SMS / e-mail

### Security
- District scope

### Integrations
- None

### Dependencies
- F04-002
- F04-003
- F04-004

### Assumptions
- Scrutiny staff provided by KEONICS

### Risks
- Backlog before sessions

### Non Functional Requirements
- Queue loads under 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Scrutiny queue | Medium | 6 |
| UI | Registration review with check results | Complex | 12 |
| UI | Decision dialog | Easy | 4 |
| UI | Bulk accept | Easy | 4 |
| API | Run metadata checks | Complex | 8 |
| API | Scrutiny queue | Medium | 6 |
| API | Record decision | Medium | 6 |
| API | Bulk decision | Medium | 6 |
| API | Escalate ageing items | Easy | 4 |
| Database | Check results and scrutiny decisions | Easy | 2 |
| Testing | Scrutiny workflow and rule tests | Medium | 6 |
| Documentation | Scrutiny guide | Easy | 2 |

**Feature Total: 66 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 30 | 2 | 0 | 6 | 2 | **66** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard workflow
- No external integration channel in this feature; Integration row omitted.
