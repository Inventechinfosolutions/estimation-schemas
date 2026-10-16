# F04-002 — Government Employee Registration with KGID & HRMS Validation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-002 |
| Feature Name | Government Employee Registration with KGID & HRMS Validation |
| Module | 04 — Candidate Registration & eKYC |
| Module Type | Business |
| Release | Go-live |

### Description
Registration path for state government employees: candidate enters KGID, system fetches name, department, posting, designation, date of birth and contact from HRMS, candidate confirms, uploads a photograph meeting specifications, adds missing details and submits a declaration. Attempt history is computed from earlier CLT records including ported data.

### Business Objective
Register employees with authoritative HRMS data so that identity is validated and results can be pushed back to HRMS.

### Actors
- Government employee candidate
- Scrutiny Officer

### User Journey
1. **Who creates:** The employee creates the registration after logging in.
2. **How they create:** The employee enters KGID and date of birth, the system fetches HRMS data, the employee confirms, uploads a photograph and submits the declaration.
3. **How they edit:** Before scrutiny the employee can edit non-HRMS fields; HRMS fields are read-only and corrected at HRMS.
4. **How they send for approval:** Submission routes the registration to scrutiny when HRMS data mismatches or photo checks fail; otherwise it is auto-accepted.
5. **How the approver sees pending items:** The Scrutiny Officer sees registrations needing review.
6. **How the approver decides:** The Scrutiny Officer accepts or rejects with reason (F04-005).
7. **How the applicant / maker sees history:** The employee sees registration status, HRMS data used and attempt count.
8. **How the approver / auditor sees history:** Auditors see HRMS responses stored against each registration.

### Functional Capabilities
- KGID + date of birth lookup in HRMS
- Pre-filled read-only HRMS fields
- Photo upload with size, format, face-detect and background checks
- Mismatch handling (HRMS name vs entered)
- Declaration and consent
- Attempt history from current and ported records
- Auto-accept or route to scrutiny
- Registration number generation

### UI Screens
- KGID lookup and HRMS confirmation
- Employee registration form
- Photo upload with quality checks
- Declaration and submission
- Registration status

### Logical API Operations
- Fetch employee from HRMS by KGID
- Save employee registration
- Photo quality checks (size, face detection)
- Compute attempt history
- Auto-accept or route to scrutiny
- Generate registration number

### Inputs
- KGID, date of birth
- Photograph
- Declaration

### Outputs
- Registration with HRMS snapshot
- Registration number

### Business Rules
- KGID must exist and be active in HRMS
- One active registration per KGID
- First attempt free for government employees (F02-004)
- HRMS fields not editable

### Validations
- Photo JPG / PNG, 20–200 KB, face detected
- KGID format

### Calculations
- Attempt number = previous attempts + 1

### Workflow
Draft → Submitted → Accepted / Under Scrutiny → Accepted / Rejected

### Search Requirements
- Registrations by KGID, name, department

### Documents
- Photograph

### Reports
- Employee registrations by department

### Notifications
- Registration acknowledgement SMS / e-mail

### Security
- HRMS data shown only to owner and authorised staff

### Integrations
- HRMS via F15-002

### Dependencies
- F04-001
- F15-002
- F18-001
- F02-004

### Assumptions
- HRMS provides lookup API by KGID

### Risks
- HRMS data quality and availability

### Non Functional Requirements
- HRMS lookup under 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | KGID lookup and HRMS confirmation | Complex | 12 |
| UI | Employee registration form | Medium | 6 |
| UI | Photo upload with quality checks | Medium | 6 |
| UI | Declaration and submission | Easy | 4 |
| UI | Registration status | Easy | 4 |
| API | Fetch employee from HRMS by KGID | Medium | 6 |
| API | Save employee registration | Medium | 6 |
| API | Photo quality checks (size, face detection) | Complex | 8 |
| API | Compute attempt history | Medium | 6 |
| API | Auto-accept or route to scrutiny | Medium | 6 |
| API | Generate registration number | Easy | 4 |
| Database | Candidate registration with HRMS snapshot | Medium | 4 |
| Database | Photo and document references | Easy | 2 |
| Testing | Employee registration tests with HRMS scenarios | Complex | 8 |
| Testing | Photo check tests | Medium | 6 |
| Documentation | Employee registration guide | Easy | 2 |

**Feature Total: 90 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 36 | 6 | 0 | 14 | 2 | **90** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- HRMS connector built in F15-002
- No external integration channel in this feature; Integration row omitted.
