# F09-001 — Secure Test Login & Language Selection

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-001 |
| Feature Name | Secure Test Login & Language Selection |
| Module | 09 — Online Examination Engine |
| Module Type | Business |
| Release | Go-live |

### Description
Test entry flow: candidate selects Kannada or English, enters hall ticket number and session password (or OTP shown to proctor), system validates seat binding, validation status and session state, shows candidate photo and details for confirmation, then instructions with a mandatory acknowledgement before the timer starts.

### Business Objective
Start each candidate's test securely in the chosen language.

### Actors
- Candidate
- Proctor

### User Journey
1. **Who creates:** The candidate starts at the assigned terminal.
2. **How they create:** The candidate selects language, enters credentials, confirms details and accepts instructions.
3. **How they edit:** Language can be switched during the test (configurable).
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** The proctor sees login status per seat.
6. **How the approver decides:** The proctor can reset a stuck login with reason.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see login events with terminal identity.

### Functional Capabilities
- Language selection
- Hall ticket and session password
- Seat binding check
- Candidate confirmation with photo
- Instructions and acknowledgement
- Proctor login reset
- Concurrent login prevention

### UI Screens
- Language selection
- Test login
- Candidate confirmation
- Instructions and acknowledgement

### Logical API Operations
- Authenticate test login
- Validate seat, validation and session state
- Proctor login reset
- Prevent concurrent session

### Inputs
- Hall ticket number
- Password

### Outputs
- Started candidate test

### Business Rules
- Login only after proctor validation
- One active test session per candidate

### Validations
- Credentials

### Calculations
- None

### Workflow
Not Logged In → Logged In → Instructions → In Test

### Search Requirements
- None

### Documents
- None

### Reports
- Login status

### Notifications
- None

### Security
- TLS; terminal binding

### Integrations
- None

### Dependencies
- F08-003
- F08-005
- F09-007

### Assumptions
- None

### Risks
- Peak logins at session start

### Non Functional Requirements
- 2,000 logins within 2 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Language selection | Simple | 2 |
| UI | Test login | Medium | 6 |
| UI | Candidate confirmation | Easy | 4 |
| UI | Instructions and acknowledgement | Easy | 4 |
| API | Authenticate test login | Complex | 8 |
| API | Validate seat, validation and session state | Medium | 6 |
| API | Proctor login reset | Easy | 4 |
| API | Prevent concurrent session | Medium | 6 |
| Database | Test session login records | Easy | 2 |
| Testing | Test login security tests | Complex | 8 |
| Documentation | Candidate test instructions (bilingual) | Easy | 2 |

**Feature Total: 52 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 24 | 2 | 0 | 8 | 2 | **52** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Peak login handled in F17-002
- No external integration channel in this feature; Integration row omitted.
