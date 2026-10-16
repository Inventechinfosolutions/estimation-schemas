# F04-003 — Prospective Candidate & Non-KGID Registration with eKYC

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-003 |
| Feature Name | Prospective Candidate & Non-KGID Registration with eKYC |
| Module | 04 — Candidate Registration & eKYC |
| Module Type | Business |
| Release | Go-live |

### Description
Registration path for prospective candidates (newly appointed, probationers, board and corporation staff) and employees without KGID: Aadhaar OTP eKYC prefills name, date of birth, gender, address and eKYC photo; candidate adds father's and mother's names, contact, appointment letter, signature and category; Aadhaar stored only as reference token.

### Business Objective
Verify identity of candidates who are not in HRMS and block fake or duplicate registrations.

### Actors
- Prospective candidate
- Employee without KGID
- Registration Centre Operator
- Scrutiny Officer

### User Journey
1. **Who creates:** The candidate (or the centre operator for prospective candidates, F04-004) creates the registration.
2. **How they create:** The candidate consents, completes Aadhaar OTP eKYC, reviews prefilled data, adds parents' names, contact, appointment letter and signature, and submits.
3. **How they edit:** Before scrutiny the candidate edits non-eKYC fields and replaces documents.
4. **How they send for approval:** Submission routes the registration to scrutiny.
5. **How the approver sees pending items:** The Scrutiny Officer sees the registration with eKYC data and documents.
6. **How the approver decides:** The Scrutiny Officer accepts, rejects or asks for correction.
7. **How the applicant / maker sees history:** The candidate sees status and remarks.
8. **How the approver / auditor sees history:** Auditors see eKYC transaction reference and scrutiny decisions.

### Functional Capabilities
- Aadhaar consent and OTP eKYC
- Prefill from eKYC with photo
- Aadhaar reference token instead of number
- Appointment letter and signature upload
- Parents' names, address, category
- Duplicate check by Aadhaar token
- Category: prospective / employee without KGID
- Correction loop

### UI Screens
- Aadhaar consent and eKYC
- Prospective registration form
- Document upload (appointment letter, signature)
- Review and submit
- Correction response

### Logical API Operations
- Initiate and verify eKYC
- Save prospective registration
- Document upload with scan
- Duplicate check by Aadhaar token
- Correction cycle
- Submit for scrutiny

### Inputs
- Aadhaar OTP
- Parents' names, contact
- Appointment letter, signature

### Outputs
- Registration under scrutiny

### Business Rules
- Aadhaar number never stored in clear; token / vault reference only
- Prospective candidates register only at designated centres (F04-004) unless KEONICS enables online registration
- One registration per Aadhaar token

### Validations
- Documents PDF / JPG up to 2 MB
- Signature image format

### Calculations
- Age from eKYC date of birth

### Workflow
Draft → Submitted → Under Scrutiny → Accepted / Rejected / Correction

### Search Requirements
- Registrations by name, category, centre

### Documents
- Appointment letter
- Signature
- eKYC photo

### Reports
- Prospective registrations

### Notifications
- Acknowledgement and decision SMS / e-mail

### Security
- Aadhaar data vault (F16-004)
- eKYC data masked

### Integrations
- Aadhaar eKYC via F15-003

### Dependencies
- F15-003
- F16-004
- F04-005

### Assumptions
- KEONICS arranges AUA / KUA access

### Risks
- eKYC failure rates; offline fallback at centres

### Non Functional Requirements
- eKYC completes within 10 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Aadhaar consent and eKYC | Complex | 12 |
| UI | Prospective registration form | Complex | 12 |
| UI | Document upload (appointment letter, signature) | Medium | 6 |
| UI | Review and submit | Easy | 4 |
| UI | Correction response | Medium | 6 |
| API | Initiate and verify eKYC | Medium | 6 |
| API | Save prospective registration | Medium | 6 |
| API | Document upload with scan | Medium | 6 |
| API | Duplicate check by Aadhaar token | Medium | 6 |
| API | Correction cycle | Easy | 4 |
| API | Submit for scrutiny | Easy | 4 |
| Database | Prospective registration and eKYC snapshot | Medium | 4 |
| Testing | eKYC registration tests | Complex | 8 |
| Testing | Duplicate and document tests | Medium | 6 |
| Documentation | Prospective candidate registration guide | Easy | 2 |

**Feature Total: 92 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 40 | 32 | 4 | 0 | 14 | 2 | **92** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- eKYC connector in F15-003
- No external integration channel in this feature; Integration row omitted.
