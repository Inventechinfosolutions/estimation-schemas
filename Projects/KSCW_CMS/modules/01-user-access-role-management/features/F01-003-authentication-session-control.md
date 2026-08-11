# F01-003 — Authentication & Session Control

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-003 |
| Feature Name | Authentication & Session Control |
| Module | 01 — User Access & Role Management |
| Description | Provide secure login and session handling for CMS web and mobile clients. |
| Business Objective | Ensure only authenticated, entitled users access CMS channels. |
| Actors | Admin; Supervisor; Operator; Complainant (where authenticated portal applies per FRS) |

### User Journey

- User opens web or mobile login → enters credentials → system validates → session established with timeout/logout.

### Functional Capabilities

- Web login screen
- Mobile login screen
- Session timeout and secure logout
- Failed-login handling per FRS

### Inputs

- Username / ID
- Password or FRS-approved credential
- Channel (web/mobile)

### Outputs

- Authenticated session
- Access denied message

### Business Rules

- Inactive users cannot authenticate
- Session expires after configured idle/absolute timeout
- Role permissions apply after login

### Validations

- Credentials required
- Account must be active

### Calculations

- None

### Workflow

- Login → session active → timeout/logout → re-auth

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- Optional lockout alert if FRS requires

### Security

- Credential hashing; session token handling; brute-force controls per FRS

### Integrations

- None (no external IdP unless FRS adds SSO)

### Dependencies

- F01-001
- F01-002

### Assumptions

- No SSO in baseline unless FRS adds it

### Risks

- SSO addition mid-project increases effort

### Non Functional Requirements

- HTTPS; secure cookie/token storage on clients

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Web login and logout screens | Medium | 6 |
| UI | Mobile login and session-expired handling | Medium | 6 |
| API | Authenticate, refresh/validate session, logout | Complex | 8 |
| Database | Credential and session metadata persistence | Easy | 2 |
| Testing | Login, timeout, inactive-user, and channel cases | Complex | 8 |
| Documentation | Authentication behaviour notes | Easy | 2 |

**Feature Total: 32 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
