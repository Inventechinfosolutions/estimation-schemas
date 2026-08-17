# F01-001 — Consume shared Person–Post–Role identity

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Consume shared Person–Post–Role identity |
| **Module** | 01 — Shared User & Access Control (consumed) |

### Description
Valuation web authenticates against the Claim Management Module 01 Person–Post–Role store. The Valuation Administrator does not create a parallel user directory. Person create/update, Post, Role-to-Post, Post-to-Person, official identity, OTP before activation, 2FA, joiner–mover–leaver and forensic/login audit remain Claim features F01-001–F01-007 and F01-010. If the Person is deactivated on the shared component, valuation login fails.

### Business Objective
Give eValueI/eValueM a single official identity with Claims and Legal, without rebuilding IAM.

### Actors
Administrator (shared IAM); Office user; Approved Valuer; Competent Authority.

### User Journey
1. Administrator provisions the Person and Post on Claim Management Module 01 (OTP before activation and 2FA as specified there).
2. The Person opens valuation web and signs in with that same official identity.
3. Valuation resolves the shared Person identifier and Post; no local user master row is created.
4. If the Person is deactivated on the shared component, the next valuation sign-in is refused.

### Functional Capabilities
- Authenticate valuation web against the shared Person–Post–Role store
- Refuse sign-in when the shared Person is inactive or not mapped to a valuation-usable Post
- Display a clear identity-source failure when the shared component is unreachable
- Do not expose Person create/update, OTP enrolment, 2FA enrolment or credential lifecycle in this application

### Inputs
Shared Person credentials; session challenge from Claim Module 01 (OTP/2FA as already specified there).

### Outputs
Valuation session bound to the shared Person and Post; refused login with reason when identity is inactive or unknown.

### Business Rules
- There is no second user master inside eValueI/eValueM
- Person, Post, Role, official identity, OTP, 2FA, joiner–mover–leaver and login audit are not re-implemented here
- Deactivation on the shared component blocks valuation login immediately

### Validations
- Shared Person exists and is active
- At least one active Post mapping usable for valuation
- Session handshake with the shared component succeeds before menus load

### Calculations
None.

### Workflow
Sign-in → shared-identity handshake → bind Person/Post to valuation session → allow or refuse.

### Search Requirements
Administrators may look up whether a shared Person currently has a valuation session (Person id, outcome, time). Person search/create remains on Claim Module 01.

### Documents
None. Identity artefacts live on the shared component.

### Reports
Valuation login outcome extract (Person id, Post, success/fail, timestamp) — not a forensic login product (Claim F01-010).

### Notifications
In-app refusal message only. Credential and OTP notices remain on the shared component.

### Security
No local password store. Session is attributable to the shared Person. HTTPS.

### Integrations
Claim Management Module 01 identity consume (authentication, Person/Post resolution, deactivation status) with mapping and retry. Not a full IAM rebuild.

### Dependencies
Claim Management F01-001–F01-007 and F01-010. This feature is wiring only.

### Assumptions
- Claim Module 01 is available to valuation web at go-live
- Hours cover consume/handshake only — not Person master, OTP product, 2FA product or audit product

### Risks
Shared IAM unavailability blocks all valuation users. Duplicate local accounts would violate the SOW if introduced later.

### Non Functional Requirements
Secure handshake; no plaintext credentials stored locally; clear failure when the shared store is down.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Valuation web sign-in against shared identity | UI | Easy | 4 |
| Shared-identity session handshake | API | Easy | 4 |
| Local session binding to shared Person id | Database | Simple | 1 |
| Claim Module 01 IAM consume (auth, mapping, retry) | Integration | Medium | 16 |
| Shared-identity login tests | Testing | Easy | 4 |
| Shared-identity consume note | Documentation | Easy | 2 |
| **Total** | | | **31** |

### Estimation Assumptions
- Integration is consume-only (Medium 16), not GIS/ERP Very High 40 and not a second IAM product
- Android channel session is estimated in F01-004 / F09-001
