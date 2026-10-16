# F04-004 — Centre-Assisted Registration & Photo Capture

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-004 |
| Feature Name | Centre-Assisted Registration & Photo Capture |
| Module | 04 — Candidate Registration & eKYC |
| Module Type | Business |
| Release | Go-live |

### Description
Registration console for designated registration centres where prospective candidates register: operator logs in, searches or creates the candidate, completes eKYC or HRMS lookup on the candidate's behalf with consent, captures a live webcam photograph, scans documents, and attests the registration.

### Business Objective
Meet the RFP rule that prospective candidates register through designated centres where the photograph is taken.

### Actors
- Registration Centre Operator
- Candidate
- District Coordinator

### User Journey
1. **Who creates:** The operator starts a centre registration for a walk-in candidate.
2. **How they create:** The operator verifies the candidate's mobile OTP, completes the registration form with eKYC, captures a live photo and scans documents.
3. **How they edit:** The operator can correct entries until submission.
4. **How they send for approval:** Submission attests the registration and routes it to scrutiny.
5. **How the approver sees pending items:** The District Coordinator sees centre registrations for the district.
6. **How the approver decides:** Scrutiny decides as per F04-005.
7. **How the applicant / maker sees history:** The candidate receives an acknowledgement and sees the registration in their account.
8. **How the approver / auditor sees history:** Auditors see operator, centre and device for each registration.

### Functional Capabilities
- Operator console restricted to centre IPs
- Candidate OTP consent
- Live webcam photo capture with guidelines overlay
- Document scanning
- Operator attestation
- Daily centre registration register
- Acknowledgement printout

### UI Screens
- Centre registration console
- Live photo capture
- Document scan and upload
- Acknowledgement print
- Centre daily register

### Logical API Operations
- Start assisted registration with candidate OTP
- Capture and store photo
- Attest registration
- Centre daily register

### Inputs
- Candidate details
- Live photo
- Scans

### Outputs
- Attested registration
- Acknowledgement

### Business Rules
- Only from registered centre IPs
- Candidate OTP mandatory
- Photo must be live, not uploaded

### Validations
- Photo quality

### Calculations
- None

### Workflow
Started → Attested → Under Scrutiny

### Search Requirements
- Centre registrations by date

### Documents
- Acknowledgement

### Reports
- Centre-wise registrations

### Notifications
- Acknowledgement SMS

### Security
- IP restriction
- Operator audit

### Integrations
- Webcam device APIs

### Dependencies
- F04-003
- F02-002

### Assumptions
- Centres have webcams and scanners

### Risks
- Device variety

### Non Functional Requirements
- Photo capture within 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Centre registration console | Medium | 6 |
| UI | Live photo capture | Medium | 6 |
| UI | Document scan and upload | Easy | 4 |
| UI | Acknowledgement print | Easy | 4 |
| UI | Centre daily register | Easy | 4 |
| API | Start assisted registration with candidate OTP | Medium | 6 |
| API | Capture and store photo | Easy | 4 |
| API | Attest registration | Easy | 4 |
| API | Centre daily register | Easy | 4 |
| Database | Assisted registration and attestation fields | Easy | 2 |
| Testing | Centre registration tests | Medium | 6 |
| Documentation | Registration centre operator manual | Easy | 2 |

**Feature Total: 52 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 24 | 18 | 2 | 0 | 6 | 2 | **52** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Reuses F04-003 services
- No external integration channel in this feature; Integration row omitted.
