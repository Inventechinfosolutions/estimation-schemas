# F04-001 — Candidate OTP Login & Account

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-001 |
| Feature Name | Candidate OTP Login & Account |
| Module | 04 — Candidate Registration & eKYC |
| Module Type | Business |
| Release | Go-live |

### Description
Candidate account creation and login on portal and mobile app using mobile number and OTP (e-mail OTP fallback), with DPDP consent capture, profile page, change of mobile / e-mail with dual OTP, duplicate prevention by mobile, KGID and Aadhaar reference, and session controls.

### Business Objective
Give every candidate a single secure account that carries registration, bookings, attempts, results and certificates.

### Actors
- Candidate
- Helpdesk Executive (view)

### User Journey
1. **Who creates:** The candidate creates an account from the portal or mobile app.
2. **How they create:** The candidate enters mobile and e-mail, verifies both OTPs, accepts the consent notice in the chosen language and lands on My Dashboard.
3. **How they edit:** The candidate updates contact details with OTP to old and new contact; other details change only through registration correction.
4. **How they send for approval:** No approval; the account is active after OTP verification.
5. **How the approver sees pending items:** Helpdesk sees account status when assisting candidates.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The candidate sees registration, bookings, attempts and documents on My Dashboard.
8. **How the approver / auditor sees history:** Auditors see login and contact change events.

### Functional Capabilities
- Mobile OTP login with e-mail fallback
- Consent notice and versioned consent record
- My Dashboard with registration, booking, attempt and document status
- Contact change with dual OTP
- One account per person (mobile, KGID, Aadhaar reference checks)
- Session timeout and device logout
- OTP throttling and CAPTCHA

### UI Screens
- Candidate sign-up
- OTP login
- Consent notice
- My Dashboard
- Contact change with OTP

### Logical API Operations
- Create candidate account
- Issue and verify OTP
- Record consent
- Dashboard summary
- Change contact with dual OTP
- Duplicate account check
- Candidate session management

### Inputs
- Mobile, e-mail
- OTP
- Consent

### Outputs
- Candidate account

### Business Rules
- One account per mobile and per KGID / Aadhaar reference
- Consent required before registration
- OTP valid 5 minutes, 3 attempts

### Validations
- Indian mobile format
- E-mail format

### Calculations
- None

### Workflow
Created → Active → Locked → Active

### Search Requirements
- Helpdesk search by mobile / registration number

### Documents
- None

### Reports
- Account statistics

### Notifications
- OTP SMS / e-mail
- Contact change alert

### Security
- Masked contact display
- Rate limiting

### Integrations
- OTP via F14-002

### Dependencies
- F14-002
- F16-004

### Assumptions
- OTP-only login for candidates

### Risks
- SMS delivery delays during peak booking

### Non Functional Requirements
- OTP issued within 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Candidate sign-up | Medium | 6 |
| UI | OTP login | Medium | 6 |
| UI | Consent notice | Easy | 4 |
| UI | My Dashboard | Complex | 12 |
| UI | Contact change with OTP | Medium | 6 |
| API | Create candidate account | Medium | 6 |
| API | Issue and verify OTP | Medium | 6 |
| API | Record consent | Easy | 4 |
| API | Dashboard summary | Medium | 6 |
| API | Change contact with dual OTP | Medium | 6 |
| API | Duplicate account check | Medium | 6 |
| API | Candidate session management | Easy | 4 |
| Database | Candidate account, consent and session store | Medium | 4 |
| Testing | Account, OTP and duplicate tests | Medium | 6 |
| Testing | Candidate session security tests | Medium | 6 |
| Documentation | Candidate account guide (bilingual) | Easy | 2 |

**Feature Total: 90 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 34 | 38 | 4 | 0 | 12 | 2 | **90** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Shared OTP service
- No external integration channel in this feature; Integration row omitted.
