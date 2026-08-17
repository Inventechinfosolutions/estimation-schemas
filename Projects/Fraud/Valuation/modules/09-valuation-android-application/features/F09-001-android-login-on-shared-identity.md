# F09-001 — Android login on shared identity

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-001 |
| **Feature Name** | Android login on shared identity |
| **Module** | 09 — Valuation Android Application (Approved Valuers) |

### Description
An Approved Valuer installs the official app and signs in with the same Person credentials and 2FA as Claim Module 01. After login the valuer sees only assigned valuation work. A deactivated Person cannot start a new session.

### Business Objective
Authenticate the valuer Android app on the shared Person identity, not a second Android directory.

### Actors
Approved Valuer.

### User Journey
1. Approved Valuer installs the official app and signs in with the same Person credentials and 2FA as Claim Module 01 (F01-001 / F01-004).
2. After login the valuer sees only assigned valuation work.
3. A deactivated Person cannot start a new session.

### Functional Capabilities
- Android sign-in with shared Person and 2FA
- Show only assigned valuation work after login
- Block new session when Person is deactivated

### Inputs
Shared credentials; 2FA; install of official app.

### Outputs
Android session; assigned-work home; refused session if deactivated.

### Business Rules
- Same Person as web
- Not a public consumer app
- Office-user Android as a separate product is out of scope

### Validations
- Person is Approved Valuer Post
- 2FA as shared component
- Person active

### Calculations
None.

### Workflow
Install → sign-in → shared 2FA → assigned work only.

### Search Requirements
None on device beyond assigned list (F09-002).

### Documents
None.

### Reports
None (session extract remains F01-004).

### Notifications
In-app refuse on deactivation.

### Security
Shared 2FA; no local Android user master; IP of the app with SPLOCA (F09-006).

### Integrations
Shared IAM/2FA consume on device (auth, mapping, retry) — not full IAM rebuild.

### Dependencies
F01-001; F01-004; F01-002.

### Assumptions
- Claim Module 01 reachable from the field network SPLOCA approves.

### Risks
Offline login after deactivation if tokens are long-lived — must refuse new sessions.

### Non Functional Requirements
TLS; no second password store on device.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android sign-in | UI | Medium | 6 |
| Device shared-identity token | API | Medium | 6 |
| Device session | Database | Easy | 2 |
| Shared IAM and 2FA on Android | Integration | Medium | 16 |
| Android login tests | Testing | Complex | 8 |
| Android identity guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- Wiring only; Person/OTP/2FA products remain Claim Module 01. GIS capture is F09-003.
