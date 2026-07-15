# F01-002 — Password Policy & Account Recovery

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-002 |
| **Feature Name** | Password Policy & Account Recovery |
| **Module** | 01 — User & Role Management |

### Description
Enforce configurable password complexity and expiry rules, allow authenticated password change, and support forgot-password / admin-assisted recovery for officer and tenant users.

### Business Objective
Reduce credential compromise risk and ensure users can safely recover access without helpdesk password sharing.

### Actors
- All authenticated users (change password)
- Unauthenticated user (forgot password)
- Super Administrator (admin reset trigger where allowed)
- System

### User Journey
1. **Change password:** User opens profile/security settings → enters current and new password → system validates policy → confirms success → optional forced re-login.
2. **Forgot password:** User requests reset via login ID/email/mobile on file → receives one-time reset link/OTP via Notification Service → sets new password → returns to login.
3. **Admin reset:** Administrator initiates reset for a locked/forgotten account → user completes reset via notified channel.

### Functional Capabilities
- Configurable password policy (length, complexity, history reuse ban, expiry)
- Authenticated change password
- Forgot-password self-service with time-bound token/OTP
- Admin-initiated reset
- Force password change on first login / after admin reset

### Inputs
- Current password (change flow)
- New password + confirm
- Login ID / registered email or mobile (reset request)
- Reset token or OTP

### Outputs
- Password updated confirmation
- Reset notification dispatched
- Policy validation errors

### Business Rules
- New password must meet active password policy.
- Password history prevents reuse of last N passwords (configurable).
- Reset tokens expire after configured TTL and are single-use.
- First login after provisioning/admin reset requires password change before accessing modules.
- Tenant and officer policies may share the same engine with optional stricter officer settings.

### Validations
- New password ≠ current password
- Confirm password match
- Token/OTP validity and attempt limits
- User must be Active to complete self-service reset

### Calculations
- Password age / days to expiry (if expiry enabled)
- Token TTL remaining

### Workflow
Reset request → notify → validate token/OTP → set password → invalidate token → audit log.

### Search Requirements
Admin may search users to initiate reset (uses F01-004 list).

### Documents
None.

### Reports
None.

### Notifications
Password reset link/OTP and password-changed alert via Module 09 (Notification Service).

### Security
- Reset tokens stored hashed; rate-limited requests
- No disclosure whether login ID exists (generic response)
- Password never returned in APIs/UI
- All reset events audited (F01-009)

### Integrations
- Internal Notification Service for email/SMS (Simple internal service)

### Dependencies
- F01-001 (login)
- F01-004 (user contact fields)
- Module 09 Notification Service
- Module 02 system parameters (policy values) — defaults allowed

### Assumptions
- Email and/or mobile available on user profile for self-service reset.
- SMS/email gateways available through Module 09/10 by integration time; this feature estimates only the internal notification handoff.
- Enterprise validation, logging, and unit tests included.

### Risks
- Users without valid email/mobile cannot self-recover; admin reset path required.
- OTP delivery delays may increase support load.

### Non Functional Requirements
- Reset completion path usable on mobile browsers
- Reset token TTL and attempt limits configurable
- English UI mandatory

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: policy engine, secure token/OTP reset, notification handoff, first-login force change.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Change password form | UI | Easy | 4 |
| Forgot / reset password wizard | UI | Medium | 6 |
| Change password operation | API | Medium | 6 |
| Reset request & confirm operations | API | Complex | 8 |
| Password history & reset token entities | Database | Easy | 2 |
| Email/SMS reset handoff (internal notification) | Integration | Simple | 4 |
| Password policy & reset tests | Testing | Complex | 8 |
| Password policy documentation | Documentation | Easy | 2 |
| **Total** | | | **40** |

### Estimation Assumptions
- Forgot/reset treated as Medium UI (multi-step) and Complex API (token lifecycle + policy).
- External SMS/email gateway connector effort belongs to Modules 09/10, not duplicated here.
