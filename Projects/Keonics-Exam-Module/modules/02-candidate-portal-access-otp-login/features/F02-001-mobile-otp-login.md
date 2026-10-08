# F02-001 — Mobile OTP Login

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Mobile OTP Login |
| **Module** | 02 — Candidate Portal Access (OTP Login) |

### Description
Candidates enter the Examination Module candidate portal using a mobile number and a one-time password (OTP) delivered by SMS. The candidate opens the portal login, enters a valid Indian mobile number, requests OTP, receives the SMS, enters the OTP, and on successful verification receives a portal session for registration and post-registration services (status, hall ticket, result, certificate as later modules provide). This feature covers the login path itself—mobile capture, OTP send, OTP verify and session open. Detailed security policy controls (expiry windows, retry limits, resend cooldown, failed-attempt lock, idle timeout configuration) are owned by F02-002 and applied during this login path. Examination Login ID/Password used at the centre CBT is out of scope here.

### Business Objective
Provide secure, password-less candidate portal access via registered mobile number and OTP so candidates can register and later retrieve examination services without a separate password account.

### Actors
Candidate (portal user); SMS gateway (delivery channel); Examination Administrator (views login health only via later audit/dashboard features, not as login maker).

### User Journey
1. Who creates: The candidate initiates a portal login session by entering their mobile number (no staff creates the candidate login credential).
2. How they create: Candidate opens candidate portal → enters 10-digit mobile → requests OTP → system validates mobile format → sends OTP via SMS gateway → candidate enters OTP on the verify screen → system validates OTP → opens portal session and lands on portal home / continue registration.
3. How they edit: Candidate may correct the mobile on the entry screen before OTP is sent; after OTP send, changing mobile starts a new OTP request for the new number (subject to F02-002 controls).
4. How they send for approval: Submit/approval does not apply; OTP verification is the authentication gate, not an administrative approval.
5. How the approver sees pending items: There is no approver inbox; failed or blocked attempts are tracked for security (F02-002) and audit, not for staff approval.
6. How the approver decides: There is no approval decision on login; success is solely valid OTP within policy.
7. How the applicant / maker sees history: Candidate sees last login success on portal home where shown; detailed attempt history is not a candidate self-service register beyond current session messaging.
8. How the approver / auditor sees history: Auditor / Administrator reviews OTP login attempt and session events through audit capabilities (Module 09), not through an approval inbox on this feature.

### Functional Capabilities
- Present candidate portal mobile entry for OTP login.
- Validate mobile number format before OTP dispatch.
- Generate OTP and send via SMS gateway to the entered mobile.
- Capture OTP entry and verify against the outstanding challenge.
- On success, establish a candidate portal session bound to the mobile identity.
- Route the candidate to portal home or continue-registration entry after login.
- Support logout / end session from the portal.
- Surface clear success, invalid OTP, and delivery-failure messages without exposing OTP values.
- Distinguish portal OTP login from centre examination credentials (system Login ID/Password).
- Invoke F02-002 security controls (expiry, retries, resend, lock, session timeout) during send and verify.
- Record login success/failure events for audit consumption.
- Allow the same mobile to re-login for post-registration services after earlier registration.
- Handle SMS gateway soft failures with candidate-visible retry guidance (without bypassing OTP).

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Candidate mobile number entry | Easy |
| OTP entry and verify | Medium |
| Portal home after successful OTP login | Medium |
| Login failure and blocked-state messages | Simple |
| Session ended / re-login prompt | Easy |
| Candidate logout confirmation | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Validate mobile and initiate OTP send | Medium |
| Verify OTP and create portal session | Complex |
| Resend OTP request handoff | Medium |
| End portal session / logout | Easy |
| Read current login challenge status | Easy |
| Record portal login attempt event | Medium |

### Inputs
Candidate mobile number; OTP value; resend request; device/browser session context as available for audit; logout request.

### Outputs
OTP SMS dispatch; verified portal session for the mobile identity; success landing on portal home; failure/blocked messages; login attempt events for audit.

### Business Rules
- Login succeeds only after a valid OTP within expiry and retry limits (limits enforced via F02-002).
- Portal session represents candidate mobile identity for registration and post-exam portal services.
- Examination CBT credentials are not issued or accepted on this portal login path.
- OTP values are not displayed in the UI after send and are not recoverable from logs in clear form.
- SMS is the delivery channel for OTP in this feature (email OTP for candidates is out of default scope unless later configured).

### Validations
- Mobile number mandatory and valid format (10-digit / Department-approved pattern).
- OTP mandatory on verify; reject empty or malformed OTP.
- Reject verify when no outstanding OTP challenge exists for the mobile.
- Reject verify when OTP does not match the outstanding challenge.
- Apply F02-002 lock and expiry before accepting verify.

### Calculations
OTP generation (secure random within configured length); remaining validity window display if shown to candidate (driven by F02-002 policy).

### Workflow
Mobile entry → OTP send (SMS) → OTP verify → portal session → portal home. No maker–checker. Logout returns to mobile entry. Idle/expired session requires fresh OTP login (F02-002).

### Search Requirements
Not a candidate search feature. Operational search of login attempts is via audit (Module 09), not this login UI.

### Documents
None.

### Reports
None owned by this feature; login volumes may appear on Module 09 dashboards.

### Notifications
SMS OTP message to the candidate mobile on each successful send/resend allowed by policy.

### Security
OTP not stored in recoverable clear text; session established only after verify; channel is candidate portal only; staff Administrator login is separate (Module 01); brute-force and expiry controls delegated to F02-002 but must be invoked here.

### Integrations
SMS gateway for OTP delivery (Medium complexity: auth to gateway, template mapping, send, delivery status/retry handling).

### Dependencies
F02-002 OTP Security Controls (policy enforcement). Consumed by Module 04 registration and later candidate portal services.

### Assumptions
- Department-approved SMS gateway credentials and OTP SMS template are available.
- Candidates use the web portal (not a native exam mobile app) for OTP login.
- Hours use Estimation Master; SMS Integration estimated at Medium.
- Each named screen and logical API is billed independently.

### Risks
- SMS delivery delay or gateway outage blocks candidate registration windows.
- Weak mobile validation could allow OTP spam to unintended numbers.
- Confusion with examination credentials could lead candidates to attempt portal OTP on centre machines incorrectly (mitigated by clear UX copy).

### Non Functional Requirements
OTP send and verify must complete within operational windows suitable for registration peaks; SMS integration must support retry and failure surfacing; portal session establishment must be secure (HTTPS assumed at platform level); login attempt events must be attributable for audit.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Candidate mobile number entry | UI | Easy | 4 |
| OTP entry and verify | UI | Medium | 6 |
| Portal home after successful OTP login | UI | Medium | 6 |
| Login failure and blocked-state messages | UI | Simple | 2 |
| Session ended / re-login prompt | UI | Easy | 4 |
| Candidate logout confirmation | UI | Simple | 2 |
| Validate mobile and initiate OTP send | API | Medium | 6 |
| Verify OTP and create portal session | API | Complex | 8 |
| Resend OTP request handoff | API | Medium | 6 |
| End portal session / logout | API | Easy | 4 |
| Read current login challenge status | API | Easy | 4 |
| Record portal login attempt event | API | Medium | 6 |
| Candidate OTP login and session persistence | DB | Medium | 4 |
| SMS gateway OTP delivery | Integration | Medium | 16 |
| Mobile OTP login feature tests | Testing | Complex | 8 |
| Mobile OTP login implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **89** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- SMS Integration is Medium (auth + mapping + retry) as required for OTP delivery.
- F02-002 owns policy configuration UI; this feature invokes those controls at send/verify time.
- Logical APIs are business operations, not REST endpoints.
