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
1. Who creates: Approved Valuer
2. How they create: Approved Valuer installs the official app and signs in with the same Person credentials and 2FA as Claim Module 01 (F01-001 / F01-004).
3. How they edit: After login the valuer sees only assigned valuation work.
4. How they send for approval: A deactivated Person cannot start a new session. Install → sign-in → shared 2FA → assigned work only.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Android sign-in with shared Person and 2FA
- Show only assigned valuation work after login
- Block new session when Person is deactivated

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My android login on shared identity list / queue | Medium |
| Android sign-in | Medium |
| Android login on shared identity history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Device shared-identity token | Medium |
| Update android login on shared identity | Medium |
| Search android login on shared identity | Medium |
| Read android login on shared identity history | Easy |

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
|---|---|---|---|
| My android login on shared identity list / queue | UI | Medium | 6 |
| Android sign-in | UI | Medium | 6 |
| Android login on shared identity history | UI | Medium | 6 |
| Device shared-identity token | API | Medium | 6 |
| Update android login on shared identity | API | Medium | 6 |
| Search android login on shared identity | API | Medium | 6 |
| Read android login on shared identity history | API | Easy | 4 |
| Android login on shared identity persistence | DB | Medium | 4 |
| Shared IAM and 2FA on Android | Integration | Medium | 16 |
| Android login on shared identity feature tests | Testing | Complex | 8 |
| Android login on shared identity implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
