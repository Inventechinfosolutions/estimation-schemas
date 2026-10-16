# F08-001 — Proctor Management, Authentication & Attendance

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-001 |
| Feature Name | Proctor Management, Authentication & Attendance |
| Module | 08 — Test Centre Operations & Candidate Validation |
| Module Type | Business |
| Release | Go-live |

### Description
Register of proctors designated by the Deputy Commissioner and KEONICS with order references, assignment to sessions and centres, conflict checks, proctor login with OTP and photo / biometric verification at the centre, attendance marking and replacement handling.

### Business Objective
Ensure every session has a designated, authenticated proctor.

### Actors
- KEONICS Administrator
- District Coordinator
- Proctor

### User Journey
1. **Who creates:** District coordinators or administrators register proctors and assign sessions.
2. **How they create:** They enter details and order references and assign proctors to sessions.
3. **How they edit:** Assignments can be changed with reason until session start.
4. **How they send for approval:** Assignments need administrator confirmation.
5. **How the approver sees pending items:** The administrator sees pending assignments.
6. **How the approver decides:** The administrator confirms.
7. **How the applicant / maker sees history:** Proctors see their assigned sessions.
8. **How the approver / auditor sees history:** Auditors see proctor authentication and attendance.

### Functional Capabilities
- Proctor register
- Designation order reference
- Session assignment and conflict check
- Proctor OTP login at centre IP
- Photo / biometric verification
- Attendance
- Replacement

### UI Screens
- Proctor register
- Session assignment
- Proctor login and verification
- Proctor attendance

### Logical API Operations
- Maintain proctor
- Assign proctor to session
- Proctor authentication
- Mark attendance
- Replacement

### Inputs
- Proctor details
- Orders

### Outputs
- Assigned, authenticated proctors

### Business Rules
- No session starts without authenticated proctor
- Proctor cannot be a candidate in same session

### Validations
- Order reference

### Calculations
- None

### Workflow
Registered → Assigned → Present

### Search Requirements
- Proctors by district

### Documents
- Designation order

### Reports
- Proctor attendance

### Notifications
- Assignment notice

### Security
- Centre IP restriction

### Integrations
- Biometric device via F08-004

### Dependencies
- F02-002
- F08-002

### Assumptions
- Proctors nominated by Deputy Commissioners

### Risks
- Late changes

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Proctor register | Medium | 6 |
| UI | Session assignment | Medium | 6 |
| UI | Proctor login and verification | Medium | 6 |
| UI | Proctor attendance | Easy | 4 |
| API | Maintain proctor | Easy | 4 |
| API | Assign proctor to session | Medium | 6 |
| API | Proctor authentication | Medium | 6 |
| API | Mark attendance | Easy | 4 |
| API | Replacement | Easy | 4 |
| Database | Proctor and assignment store | Easy | 2 |
| Testing | Proctor flow tests | Medium | 6 |
| Documentation | Proctor manual | Medium | 3 |

**Feature Total: 57 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 24 | 2 | 0 | 6 | 3 | **57** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
