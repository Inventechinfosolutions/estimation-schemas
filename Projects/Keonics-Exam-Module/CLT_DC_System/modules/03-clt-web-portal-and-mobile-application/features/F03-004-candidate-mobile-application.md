# F03-004 — Candidate Mobile Application

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-004 |
| Feature Name | Candidate Mobile Application |
| Module | 03 — CLT Web Portal & Mobile Application |
| Module Type | Business |
| Release | Go-live |

### Description
Cross-platform mobile application (Android and iOS) for candidates covering OTP login, registration, eKYC hand-off, photo capture, booking, payment, hall ticket download, rescheduling, notifications (push), mock test access, results and certificate download, published on Play Store and App Store under KEONICS accounts.

### Business Objective
Provide a faster registration channel as required by RFP 4.5.5.3.

### Actors
- Candidate
- KEONICS (store account owner)

### User Journey
1. **Who creates:** Candidates install the app and create their account through OTP.
2. **How they create:** Candidates register and book through native screens reusing portal services.
3. **How they edit:** Candidates edit profile and booking per the same rules as the portal.
4. **How they send for approval:** Approval steps are the same as on the portal (scrutiny, payment).
5. **How the approver sees pending items:** Not applicable for candidates.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Candidates see status, history and documents in the app.
8. **How the approver / auditor sees history:** Auditors see app actions in the common audit trail.

### Functional Capabilities
- OTP login
- Registration with camera photo capture
- Booking and payment through gateway SDK / web view
- Hall ticket and certificate download
- Push notifications
- Mock test launch
- Bilingual UI
- Store publication and updates
- App version enforcement

### UI Screens
- App onboarding and login
- Registration flow (mobile)
- Slot booking (mobile)
- Payment hand-off and result
- Hall ticket and documents
- Notifications inbox
- Results and certificate
- Profile and settings

### Logical API Operations
- Mobile session and device registration
- Push notification service
- App version check

### Inputs
- Candidate inputs

### Outputs
- Registrations and bookings

### Business Rules
- Same business rules as portal

### Validations
- Same as portal

### Calculations
- None

### Workflow
Same as portal flows

### Search Requirements
- Bookings

### Documents
- Hall ticket, certificate

### Reports
- App usage

### Notifications
- Push notifications

### Security
- Certificate pinning; no sensitive data cached

### Integrations
- FCM / APNs

### Dependencies
- Modules 04, 05, 07, 11

### Assumptions
- KEONICS provides store accounts

### Risks
- Store review delays

### Non Functional Requirements
- Supports Android 9+ and iOS 15+

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | App onboarding and login | Medium | 6 |
| UI | Registration flow (mobile) | Complex | 12 |
| UI | Slot booking (mobile) | Medium | 6 |
| UI | Payment hand-off and result | Medium | 6 |
| UI | Hall ticket and documents | Easy | 4 |
| UI | Notifications inbox | Easy | 4 |
| UI | Results and certificate | Easy | 4 |
| UI | Profile and settings | Easy | 4 |
| API | Mobile session and device registration | Medium | 6 |
| API | Push notification service | Medium | 6 |
| API | App version check | Easy | 4 |
| Database | Device and push token store | Easy | 2 |
| Integration | Push notification service (FCM / APNs) | Medium | 16 |
| Testing | Mobile functional testing on device matrix | Complex | 8 |
| Testing | Store compliance and release testing | Medium | 6 |
| Documentation | Mobile app user guide (bilingual) | Easy | 2 |
| Documentation | Store release runbook | Easy | 2 |

**Feature Total: 98 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 46 | 16 | 2 | 16 | 14 | 4 | **98** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Business services reused; mobile screens billed separately
