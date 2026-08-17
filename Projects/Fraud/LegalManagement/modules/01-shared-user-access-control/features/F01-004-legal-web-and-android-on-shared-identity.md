# F01-004 — Legal web and Android on shared identity

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-004 |
| **Feature Name** | Legal web and Android on shared identity |
| **Module** | 01 — Shared User & Access Control (consumed) |

### Description
An Advocate or Legal Cell user signs in on web or Android with the same Person credentials and 2FA as the shared component. After login they see only Legal menus allowed for their Post. Signing out or deactivation ends both channels.

### Business Objective
One Person, two official channels (Legal web and Legal Android) with the same 2FA and Post-scoped menus.

### Actors
Advocate; Legal Cell; Administrator (channel enrolment against shared identity).

### User Journey
1. User opens Legal web or the Legal Android app and authenticates with the shared Person and 2FA.
2. Legal Web Shell shows only menus allowed for the active Post.
3. Android Login/Session screens apply the same Person; no second login directory.
4. User signs out on one channel; that channel session ends; deactivation on the shared component ends **both** web and Android.
5. Menus never expose Claim settlement or eValueI functions.

### Functional Capabilities
- Legal Web Shell / Post-scoped menu
- Android Login and Session screens on shared 2FA
- Same Person credentials for web and Android
- Sign-out or shared deactivation ends both channels
- No second credential store on the device or in Legal

### Inputs
Shared Person credentials and 2FA proof; channel (web/Android); device enrolment token where used.

### Outputs
Web session; Android session; Post-scoped menu set; dual-channel revocation on deactivation.

### Business Rules
- Web and Android use the same shared Person; there is no Android-only user list.
- After login the user sees only Legal menus allowed for their Post.
- Disabling the Person on the shared component blocks new web and Android sessions immediately.
- IP of the Legal applications remains with SPLOCA; this feature does not include Play Store licensing (F09-008).
- iOS is out of scope.

### Validations
Shared 2FA required as configured; device enrolment only for Persons with Legal Posts; expired session cannot call Legal APIs.

### Calculations
None.

### Workflow
Authenticate via shared component → issue Legal channel session → render Post menus → revoke both channels on sign-out or deactivation.

### Search Requirements
Active Legal sessions by Person, channel (web/Android), Post, last activity (administration).

### Documents
None.

### Reports
Legal channel session register (web vs Android).

### Notifications
Optional notice when a session is revoked by deactivation.

### Security
Tokens bound to shared Person; Android stores no password; HTTPS; fail closed on shared IAM outage.

### Integrations
Shared identity and 2FA for web and Android (Medium — auth, mapping, retry).

### Dependencies
F01-001; Module 09 screens consume this session. Play Store distribution is F09-008 only.

### Assumptions
Android feature screens (contacts, tasks, etc.) are estimated in Module 09; this feature is identity and shell only.

### Risks
Cached Android session after deactivation if revocation is delayed; dual-channel sign-out must be explicit.

### Non Functional Requirements
Court-day availability; session timeout per shared policy; AES-256 in transit.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Legal Web Shell / Post-scoped menu | UI | Complex | 12 |
| Android Login and Session screens | UI | Complex | 12 |
| Dual-channel session and menu-resolution operations | API | Complex | 8 |
| Channel session and device-enrolment tokens | Database | Easy | 2 |
| Shared identity and 2FA for web and Android | Integration | Medium | 16 |
| Dual-channel session tests | Testing | Complex | 8 |
| Legal web and Android login guide | Documentation | Medium | 3 |
| **Total** | | | **61** |

### Estimation Assumptions
- Does not estimate Android matter/task/document screens (Module 09).
- Does not estimate Play Store licensing (F09-008).
- 2FA implementation remains on Claim Module 01; Legal consumes it.
