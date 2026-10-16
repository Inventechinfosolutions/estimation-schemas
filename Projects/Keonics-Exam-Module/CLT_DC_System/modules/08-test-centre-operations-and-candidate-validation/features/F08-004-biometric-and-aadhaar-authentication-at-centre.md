# F08-004 — Biometric & Aadhaar Authentication at Centre

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-004 |
| Feature Name | Biometric & Aadhaar Authentication at Centre |
| Module | 08 — Test Centre Operations & Candidate Validation |
| Module Type | Business |
| Release | Go-live |

### Description
Optional biometric authentication of candidates and proctors at the centre using STQC-certified fingerprint devices or face authentication, via Aadhaar authentication or matching against biometrics captured at registration, with logs and fallback.

### Business Objective
Meet the RFP requirement for biometric data and logs.

### Actors
- Proctor
- Candidate

### User Journey
1. **Who creates:** The proctor initiates biometric authentication for a candidate.
2. **How they create:** The candidate gives fingerprint or face; result is recorded.
3. **How they edit:** Retry up to configured limit.
4. **How they send for approval:** Failures fall back to manual validation with EMU approval.
5. **How the approver sees pending items:** EMU sees fallback requests.
6. **How the approver decides:** EMU approves fallback.
7. **How the applicant / maker sees history:** Results shown on validation console.
8. **How the approver / auditor sees history:** Auditors see biometric logs (no raw biometrics stored for Aadhaar).

### Functional Capabilities
- RD-service device integration
- Aadhaar authentication call
- Retry and fallback
- Biometric logs
- Proctor biometric attendance

### UI Screens
- Biometric capture panel
- Fallback approval

### Logical API Operations
- Capture via RD service
- Authenticate
- Fallback request
- Biometric log

### Inputs
- Biometric capture

### Outputs
- Authentication result

### Business Rules
- Raw Aadhaar biometrics not stored

### Validations
- Device certified

### Calculations
- None

### Workflow
Pending → Authenticated / Fallback

### Search Requirements
- Logs

### Documents
- None

### Reports
- Biometric success rates

### Notifications
- Fallback alerts

### Security
- UIDAI compliance

### Integrations
- Aadhaar via F15-003
- RD service

### Dependencies
- F15-003
- F08-003

### Assumptions
- Devices provided by centres

### Risks
- Device compatibility

### Non Functional Requirements
- Under 10 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Biometric capture panel | Medium | 6 |
| UI | Fallback approval | Easy | 4 |
| API | Capture via RD service | Medium | 6 |
| API | Authenticate | Medium | 6 |
| API | Fallback request | Easy | 4 |
| API | Biometric log | Easy | 4 |
| Database | Biometric authentication logs | Easy | 2 |
| Integration | RD service device driver integration | Medium | 16 |
| Testing | Biometric tests with devices | Medium | 6 |
| Documentation | Biometric SOP | Easy | 2 |

**Feature Total: 56 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 20 | 2 | 16 | 6 | 2 | **56** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Device integration rated Medium
