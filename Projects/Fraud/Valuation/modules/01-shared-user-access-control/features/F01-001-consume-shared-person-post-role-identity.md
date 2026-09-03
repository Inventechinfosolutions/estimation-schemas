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
1. Who creates: Administrator (shared IAM)
2. How they create: Administrator provisions the Person and Post on Claim Management Module 01 (OTP before activation and 2FA as specified there).
3. How they edit: The Person opens valuation web and signs in with that same official identity.
4. How they send for approval: Valuation resolves the shared Person identifier and Post; no local user master row is created. Sign-in → shared-identity handshake → bind Person/Post to valuation session → allow or refuse.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator (shared IAM) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator (shared IAM) opens history on the record. If the Person is deactivated on the shared component, the next valuation sign-in is refused.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Authenticate valuation web against the shared Person–Post–Role store
- Refuse sign-in when the shared Person is inactive or not mapped to a valuation-usable Post
- Display a clear identity-source failure when the shared component is unreachable
- Do not expose Person create/update, OTP enrolment, 2FA enrolment or credential lifecycle in this application

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My consume shared person–post–role identity list / queue | Medium |
| Valuation web sign-in against shared identity | Easy |
| Consume shared person–post–role identity history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Shared-identity session handshake | Easy |
| Update consume shared person–post–role identity | Medium |
| Search consume shared person–post–role identity | Medium |
| Read consume shared person–post–role identity history | Easy |

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
|---|---|---|---|
| My consume shared person–post–role identity list / queue | UI | Medium | 6 |
| Valuation web sign-in against shared identity | UI | Easy | 4 |
| Consume shared person–post–role identity history | UI | Medium | 6 |
| Shared-identity session handshake | API | Easy | 4 |
| Update consume shared person–post–role identity | API | Medium | 6 |
| Search consume shared person–post–role identity | API | Medium | 6 |
| Read consume shared person–post–role identity history | API | Easy | 4 |
| Consume shared person–post–role identity persistence | DB | Medium | 4 |
| Claim Module 01 IAM consume (auth, mapping, retry) | Integration | Medium | 16 |
| Consume shared Person–Post–Role identity feature tests | Testing | Easy | 4 |
| Consume shared Person–Post–Role identity implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
