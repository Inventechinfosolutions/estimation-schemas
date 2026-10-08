# F08-004 — QR Code and Public Certificate Verification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-004 |
| **Feature Name** | QR Code and Public Certificate Verification |
| **Module** | 08 — Evaluation, Results and Certificates |

### Description
Bind each issued certificate to a unique QR code / verification token and URL, and provide a public verification page that returns valid/genuine, invalid/not found, or cancelled/revoked status while displaying only Department-approved public fields — without requiring a staff or candidate login for the verifier.

### Business Objective
Allow third parties to confirm certificate authenticity and revocation status without exposing non-approved personal data.

### Actors
- Public verifier (no account required)
- Examination Administrator (token/QR oversight, cancellation linkage)
- System (token generation at issue; status resolution)
- Auditor (verification attempt logs)

### User Journey
1. Who creates: The system creates a unique verification token and QR payload when a certificate is issued (F08-003); administrators do not manually invent tokens. Public verifiers create verification attempts by scanning QR or entering token/URL.
2. How they create: On issue → generate token/QR → embed on certificate. Verifier opens public page → scan/enter token → system resolves certificate → show status and approved public fields only.
3. How they edit: Tokens are not edited. On cancellation/revocation, token remains resolvable but status becomes cancelled/revoked; re-issue may mint a new token under policy.
4. How they send for approval: Does not apply — public verification is a read of authenticity status, not an approval workflow.
5. How the approver sees pending items: No approver inbox. Administrators may review verification attempt logs and token binding views.
6. How the approver decides: No decision; status is derived from certificate record (issued vs cancelled vs not found).
7. How the applicant / maker sees history: Candidates see QR on their certificate download; they do not manage the public page. Administrators see token binding and attempt logs.
8. How the approver / auditor sees history: Auditors see verification attempts (time, result status class, token reference) without storing unnecessary verifier personal data.

### Functional Capabilities
- Unique verification token and QR linked to certificate
- Public verification landing page (no login)
- Verification result display for valid/genuine certificates with approved public fields only
- Cancelled/revoked status display when cancellation is enabled
- Invalid/not found display for unknown or tampered tokens
- Administrator QR/token binding view
- Log public verification attempts for abuse monitoring
- Invalidate or status-switch token behaviour on cancellation
- Prevent disclosure of non-approved personal or internal fields on the public page

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| QR and token binding admin view | Medium |
| Public verification landing | Medium |
| Verification result display (valid) | Medium |
| Cancelled or revoked status display | Easy |
| Invalid or not found display | Easy |
| Public verification attempt log | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Generate verification token and QR payload | Complex |
| Resolve token to certificate | Complex |
| Return approved public disclosure fields | Complex |
| Return cancelled or revoked status | Medium |
| Log public verification attempt | Medium |
| Apply token status on cancellation | Medium |
| Search verification attempt log | Medium |

### Inputs
Certificate issue event, public token/QR scan or typed token, cancellation events.

### Outputs
QR payload for certificate render, public status response, attempt log entries.

### Business Rules
- QR verification returns correct status for valid and cancelled certificates.
- Public page does not disclose non-approved personal data.
- Not found/invalid for unknown tokens; do not leak whether a similar certificate number exists beyond approved messaging.
- No staff account required for public verifier.
- Token uniqueness enforced.

### Validations
- Token format checks on public entry
- Rate limiting / abuse controls as approved
- Only approved field set in public response

### Calculations
None.

### Workflow
Issue → token/QR → public resolve → status display. Cancel → status cancelled on same or updated token policy. No approval.

### Search Requirements
Admin: token/certificate number; verification logs by date/status class.

### Documents
QR printed/embedded on certificate from F08-003 render.

### Reports
Verification attempt volumes may feed Module 09 operational reports if required.

### Notifications
None to public verifiers; optional admin alert on abuse spikes via F09-003.

### Security
Public endpoint hardened; minimal data disclosure; attempt logging; token unguessable.

### Integrations
None (public page is part of this application).

### Dependencies
F08-003 certificate issue and cancel.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Public verifier identity capture beyond optional rate-limit signals is out of scope.

### Risks
Token enumeration if entropy is weak.
Over-disclosure if field approval list is poorly configured.

### Non Functional Requirements
Public page available independently of candidate portal login; responds under burst verification traffic (e.g. after result day).

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| QR and token binding admin view | UI | Medium | 6 |
| Public verification landing | UI | Medium | 6 |
| Verification result display (valid) | UI | Medium | 6 |
| Cancelled or revoked status display | UI | Easy | 4 |
| Invalid or not found display | UI | Easy | 4 |
| Public verification attempt log | UI | Medium | 6 |
| Generate verification token and QR payload | API | Complex | 8 |
| Resolve token to certificate | API | Complex | 8 |
| Return approved public disclosure fields | API | Complex | 8 |
| Return cancelled or revoked status | API | Medium | 6 |
| Log public verification attempt | API | Medium | 6 |
| Apply token status on cancellation | API | Medium | 6 |
| Search verification attempt log | API | Medium | 6 |
| Verification token entities | DB | Medium | 4 |
| QR code and public certificate verification tests | Testing | Complex | 8 |
| QR code and public certificate verification implementation documentation | Documentation | Medium | 3 |

**Feature total: 95 hours**
