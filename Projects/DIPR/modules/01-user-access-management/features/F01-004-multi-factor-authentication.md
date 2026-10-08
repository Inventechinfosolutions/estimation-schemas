# F01-004 — Multi-factor authentication

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-004 |
| Feature Name | Multi-factor authentication |
| Module | 01 — User & Access Management |
| Description | Enforce MFA for configured roles and channels (web; mobile session policy aligned) using TOTP and/or SMS as DIPR confirms. |
| Business Objective | Reduce account takeover risk for privileged campaign approvers, PoD verifiers, and administrators. |
| Actors | DIPR Administrator; All authenticated users subject to policy |

### User Journey

- Administrator sets MFA policy by role → User logs in with password or SSO → prompted to enroll authenticator or verify OTP → on success, session issued → subsequent logins require second factor until device trust expires (if enabled).

### Functional Capabilities

- MFA policy configuration by role and channel
- TOTP enrollment (QR) and verification
- SMS OTP send and verify when gateway configured
- Backup/recovery codes generation and one-time use
- Admin reset of MFA enrollment for locked users
- MFA challenge step on login and sensitive actions (optional policy)

### Inputs

- Policy flags per role, OTP codes, phone for SMS, recovery codes

### Outputs

- MFA enrollment status on user; successful/failed challenge audit

### Business Rules

- Roles marked MFA-mandatory cannot obtain full session without completed enrollment
- Failed attempts lock step temporarily per security policy
- SMS MFA depends on Module 02/08 gateway parameters

### Validations

- Valid TOTP window; SMS rate limits; recovery code single use

### Calculations

- None

### Workflow

- Login step 1 → MFA challenge → Active session

### Search Requirements

- Admin view users with MFA enrolled / pending

### Documents

- None

### Reports

- None

### Notifications

- SMS OTP via notification infrastructure when enabled

### Security

- Secrets hashed; no OTP in logs; lockout after repeated failures

### Integrations

- SMS gateway (optional, via platform notification path)

### Dependencies

- F01-001, F01-002; notification/SMS parameters (F02-004)

### Assumptions

- TOTP is baseline; SMS optional pending DIPR gateway

### Risks

- SMS delivery delays in field areas affect login UX

### Non Functional Requirements

- MFA step adds minimal latency; accessible challenge UI

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | MFA enrollment wizard with TOTP QR | Medium | 6 |
| UI | Login MFA TOTP challenge screen | Easy | 4 |
| UI | Login MFA SMS OTP challenge screen | Easy | 4 |
| UI | Admin MFA policy toggles by role | Medium | 6 |
| UI | Backup codes generate and confirm modal | Simple | 2 |
| UI | Admin force-reset MFA for user dialog | Simple | 2 |
| UI | MFA lockout user messaging panel | Simple | 2 |
| API | Enroll TOTP secret and confirm enrollment | Complex | 8 |
| API | Verify MFA challenge at login | Medium | 6 |
| API | Send and verify SMS OTP | Medium | 6 |
| API | Admin read/update MFA policy by role | Medium | 6 |
| API | Generate and invalidate backup codes | Easy | 4 |
| API | Admin reset MFA enrollment for user | Easy | 4 |
| Integration | SMS gateway OTP dispatch (provision) | Easy | 8 |
| Database | MFA enrollment secrets (encrypted) | Medium | 4 |
| Database | MFA policy flags per role | Easy | 2 |
| Database | Backup codes hash storage | Easy | 2 |
| Testing | MFA policy enforced per role | Complex | 8 |
| Testing | Lockout after failed attempts | Medium | 6 |
| Testing | Backup code one-time use | Medium | 6 |
| Testing | TOTP clock skew tolerance | Easy | 4 |
| Documentation | MFA operations guide for administrators | Medium | 3 |
| Documentation | UAT MFA enrollment and recovery scripts | Easy | 2 |

**Feature Total: 105 hours**

### Estimation Assumptions

- Hardware security keys are out of scope unless DIPR adds later.
- Mobile app reuses same MFA policy with channel-appropriate UX (detail in Module 06).
