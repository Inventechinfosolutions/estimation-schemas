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
1. Office user or Approved Valuer signs in on web or Android with the same Person credentials and 2FA as Claim Module 01.
2. After login they see only valuation menus allowed for their Post (F01-002).
3. Sign-out on a channel ends that channel’s session.
4. Deactivating the Person on the shared component blocks new web and Android sessions.

### Functional Capabilities
- Accept the same shared credentials and 2FA on valuation web and Android
- Show only Post-allowed valuation menus on both channels
- End sessions on sign-out or shared-Person deactivation

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
|---|---|---|---:|
| Channel session status (web / Android) | UI | Easy | 4 |
| Cross-channel session bind and revoke | API | Complex | 8 |
| Web and Android session tokens | Database | Medium | 4 |
| Shared 2FA and Android token consume | Integration | Medium | 16 |
| Cross-channel session tests | Testing | Complex | 8 |
| Web and Android identity note | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Not full IAM hours; 2FA product remains Claim F01-006
- Play Store distribution is F09-006
