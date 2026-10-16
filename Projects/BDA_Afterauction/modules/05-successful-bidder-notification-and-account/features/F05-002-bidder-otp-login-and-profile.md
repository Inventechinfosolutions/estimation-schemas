# F05-002 — Bidder OTP Login & Profile

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-002 |
| Feature Name | Bidder OTP Login & Profile |
| Module | 05 — Successful Bidder Notification & Account |
| Module Type | Business |
| Release | Go-live |

### Description
Password-less login for successful bidders with OTP to the registered mobile and / or e-mail, CAPTCHA, throttling and session control, and a profile page to view details, update e-mail and communication address (with OTP), and set language and notification preferences.

### Business Objective
Provide simple and secure access for bidders, consistent with the RFP requirement of OTP login.

### Actors
- Successful Bidder

### User Journey
1. **Who creates:** Accounts are created by F05-001; the bidder signs in here.
2. **How they create:** The bidder enters the registered mobile or e-mail, completes CAPTCHA, receives an OTP and logs in to My Sites.
3. **How they edit:** The bidder updates e-mail, address and preferences from Profile; changes to e-mail need OTP on the new e-mail.
4. **How they send for approval:** No approval for profile changes except mobile change, which goes through the Auction Admin (F05-001).
5. **How the approver sees pending items:** Not applicable for bidder self-service changes.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The bidder sees login history and current sessions on Profile.
8. **How the approver / auditor sees history:** Auditors see bidder logins and profile changes.

### Functional Capabilities
- OTP login by mobile or e-mail with CAPTCHA
- OTP throttling and lockout after repeated failures
- Session timeout and logout
- Profile view and update with OTP verification
- Language preference (Kannada / English)
- Notification preferences (WhatsApp opt-in)
- Login history

### UI Screens
- Bidder login page
- OTP verification page
- Bidder profile
- Login history

### Logical API Operations
- Request bidder OTP
- Verify OTP and create session
- Get / update profile
- Verify OTP for contact change
- Logout
- Login history

### Inputs
- Mobile or e-mail
- OTP
- Profile changes

### Outputs
- Bidder session
- Updated profile

### Business Rules
- OTP valid 5 minutes; 3 attempts; 5 OTP requests per hour
- Bidders see only their own sites
- WhatsApp messages only with opt-in

### Validations
- Registered identity exists
- CAPTCHA passed

### Calculations
- None

### Workflow
OTP requested → Verified → Session active → Logged out / expired

### Search Requirements
- None

### Documents
- None

### Reports
- Bidder login statistics (through F11)

### Notifications
- OTP SMS / e-mail

### Security
- No user enumeration
- Rate limiting
- Secure cookies

### Integrations
- OTP delivery through F12-003

### Dependencies
- F05-001
- F12-003
- F14-003

### Assumptions
- Bidders have access to registered mobile

### Risks
- Bidder changed mobile; correction path in F05-001

### Non Functional Requirements
- Login within 2 seconds excluding OTP delivery

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Bidder login page | Medium | 6 |
| UI | OTP verification page | Easy | 4 |
| UI | Bidder profile | Medium | 6 |
| UI | Login history | Simple | 2 |
| API | Request bidder OTP | Medium | 6 |
| API | Verify OTP and create session | Medium | 6 |
| API | Get / update profile | Easy | 4 |
| API | Verify OTP for contact change | Easy | 4 |
| API | Logout | Simple | 2 |
| API | Login history | Simple | 2 |
| Database | Bidder session and OTP store | Easy | 2 |
| Database | Bidder preferences | Simple | 1 |
| Testing | OTP login and throttling tests | Medium | 6 |
| Testing | Profile change tests | Easy | 4 |
| Documentation | Bidder login help (bilingual) | Easy | 2 |

**Feature Total: 57 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 24 | 3 | 0 | 10 | 2 | **57** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Reuses OTP components from F01-001
- No external integration channel in this feature; Integration row omitted.
