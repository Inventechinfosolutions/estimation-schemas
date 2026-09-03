# F01-004 — Valuation web and Android on shared identity

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-004 |
| **Feature Name** | Valuation web and Android on shared identity |
| **Module** | 01 — Shared User & Access Control (consumed) |

### Description
An Office user or Approved Valuer signs in on web or Android with the same Person credentials and 2FA as the shared component. After login they see only valuation menus allowed for their Post. Signing out or deactivation ends both channels.

### Business Objective
One Person, two channels: staff web and valuer Android, with deactivation ending both.

### Actors
Office user; Approved Valuer; Administrator (shared IAM).

### User Journey
1. Who creates: Office user
2. How they create: Office user or Approved Valuer signs in on web or Android with the same Person credentials and 2FA as Claim Module 01.
3. How they edit: After login they see only valuation menus allowed for their Post (F01-002).
4. How they send for approval: Sign-out on a channel ends that channel’s session. Channel sign-in → shared 2FA → Post menus → session; deactivation → refuse new sessions both channels.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record. Deactivating the Person on the shared component blocks new web and Android sessions.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Accept the same shared credentials and 2FA on valuation web and Android
- Show only Post-allowed valuation menus on both channels
- End sessions on sign-out or shared-Person deactivation

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My valuation web and android on shared identity list / queue | Medium |
| Channel session status (web / Android) | Easy |
| Valuation web and android on shared identity history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Cross-channel session bind and revoke | Complex |
| Update valuation web and android on shared identity | Medium |
| Search valuation web and android on shared identity | Medium |
| Read valuation web and android on shared identity history | Easy |

### Inputs
Shared Person credentials; 2FA challenge; channel (web or Android); sign-out or deactivation event.

### Outputs
Channel session; ended session; blocked new session after deactivation.

### Business Rules
- Android login is the same Person as web
- Disabling a Person blocks new web and Android sessions
- Office-user Android as a separate product is out of scope (valuer Android is Module 09)

### Validations
- Channel is web or official valuer Android
- 2FA satisfies the shared component
- Person is active

### Calculations
None.

### Workflow
Channel sign-in → shared 2FA → Post menus → session; deactivation → refuse new sessions both channels.

### Search Requirements
Person, channel, session start/end, deactivation block.

### Documents
None.

### Reports
Channel session extract (web vs Android).

### Notifications
In-app session-ended message on deactivation where the channel is open.

### Security
Shared 2FA; no separate Android password store; deactivation is immediate for new sessions.

### Integrations
Shared 2FA and token validation for web and Android (auth, mapping, retry).

### Dependencies
F01-001; F01-002; F09-001 uses this identity on the device.

### Assumptions
- 2FA enrolment remains Claim Module 01
- Device GIS capture hours sit in F09-003, not here

### Risks
Stale Android tokens after deactivation if revocation is delayed.

### Non Functional Requirements
Revoke or refuse new sessions promptly after shared deactivation; HTTPS/TLS on both channels.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My valuation web and android on shared identity list / queue | UI | Medium | 6 |
| Channel session status (web / Android) | UI | Easy | 4 |
| Valuation web and android on shared identity history | UI | Medium | 6 |
| Cross-channel session bind and revoke | API | Complex | 8 |
| Update valuation web and android on shared identity | API | Medium | 6 |
| Search valuation web and android on shared identity | API | Medium | 6 |
| Read valuation web and android on shared identity history | API | Easy | 4 |
| Valuation web and android on shared identity persistence | DB | Medium | 4 |
| Shared 2FA and Android token consume | Integration | Medium | 16 |
| Valuation web and Android on shared identity feature tests | Testing | Complex | 8 |
| Valuation web and Android on shared identity implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
