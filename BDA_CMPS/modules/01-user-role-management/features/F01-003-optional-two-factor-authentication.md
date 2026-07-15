# F01-003 — Optional Two-Factor Authentication

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-003 |
| **Feature Name** | Optional Two-Factor Authentication |
| **Module** | 01 — User & Role Management |

### Description
Provide optional second-factor verification (OTP via SMS/email) after primary password authentication, configurable at system and/or role/user level.

### Business Objective
Strengthen access control for privileged officer accounts handling financial and approval actions, per SOW optional 2FA requirement.

### Actors
- Super Administrator (policy: enable optional/mandatory by role)
- Officer users enrolling or challenged for 2FA
- Tenant (optional; typically off unless mandated)
- System

### User Journey
1. User completes primary login (F01-001).
2. If 2FA required/enabled, system prompts for OTP.
3. User receives OTP on registered mobile/email and submits it.
4. On success, session is fully established; on failure/expiry, access denied.
5. User (or admin policy) can enroll/disable 2FA where policy allows.

### Functional Capabilities
- System/role flag: 2FA Off / Optional / Mandatory
- User enrollment of 2FA channel (SMS/email on file)
- OTP generation, validation, resend with cooldown
- Bypass list not allowed except break-glass admin procedure (documented)

### Inputs
- OTP code
- Resend request
- Enrollment preferences

### Outputs
- 2FA challenge success/failure
- Enrollment status on user profile

### Business Rules
- Mandatory 2FA roles cannot complete login without successful OTP.
- OTP is single-use and time-bound.
- Maximum resend and validation attempts enforced.
- Disabling 2FA for mandatory roles requires Super Administrator override + audit.

### Validations
- OTP format/length
- Expiry and attempt counters
- Channel contact must exist before enrollment

### Calculations
- OTP expiry countdown
- Resend cooldown timer

### Workflow
Password OK → 2FA challenge → OTP validate → full session.

### Search Requirements
Admin filter users by 2FA status (on user list — F01-004).

### Documents
None.

### Reports
Optional compliance list of users without 2FA for mandatory roles (can be simple export from user list).

### Notifications
OTP message via Module 09.

### Security
- OTPs hashed at rest where stored; short TTL
- Rate limiting on validate/resend
- Audit of enrollment and failures

### Integrations
- Notification Service OTP dispatch (REST API — Easy)

### Dependencies
- F01-001, F01-002/F01-004 (contacts)
- Module 09 / 10 for SMS/email delivery

### Assumptions
- 2FA channel is SMS and/or email OTP only (no hardware token/app TOTP unless later added).
- Feature is optional at program level but implementable and switchable.
- Enterprise-grade controls included in estimate.

### Risks
- SMS delivery dependency may block login for mandatory roles during outage; needs fallback SOP.
- Tenants may lack reliable mobile numbers.

### Non Functional Requirements
- OTP challenge usable on mobile browsers
- OTP dispatch and validate path performant under login spikes

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: policy by role, OTP lifecycle, notification integration, mandatory enforcement.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| 2FA enrollment / settings screen | UI | Medium | 6 |
| OTP challenge screen | UI | Easy | 4 |
| Enable / verify / disable 2FA operations | API | Complex | 8 |
| 2FA preference & OTP challenge state | Database | Easy | 2 |
| OTP dispatch via SMS/email (REST to notification) | Integration | Easy | 8 |
| 2FA security tests | Testing | Complex | 8 |
| 2FA admin & user guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- OTP provider connectivity estimated as Easy REST to Notification Service; gateway itself in Module 10.
