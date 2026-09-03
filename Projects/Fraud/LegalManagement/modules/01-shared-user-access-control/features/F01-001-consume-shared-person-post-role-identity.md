# F01-001 — Consume shared Person–Post–Role identity

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Consume shared Person–Post–Role identity |
| **Module** | 01 — Shared User & Access Control (consumed) |

### Description
Wire the Legal web application to the **shared Person–Post–Role identity** already specified in Claim Management Module 01 (F01-001 Person, F01-002 Post/Role mapping, F01-004 official identity, F01-005 OTP before activation, F01-006 2FA, F01-007 joiner–mover–leaver, F01-010 forensic/login audit). An Administrator provisions Legal Cell officers and advocates **in that shared component**. Legal Management does **not** create a parallel Person master, user directory, OTP, 2FA or login-audit product. A Legal user then opens Legal web with that Person; if the Person is deactivated on the shared component, Legal login fails.

### Business Objective
Reuse Claim Management Module 01 identity so Legal Cell and advocates have one official Person without a second IAM build.

### Actors
Administrator (shared IAM); Legal Administrator (consume-only); Legal Cell; Advocate; Competent Authority (session).

### User Journey
1. Who creates: Administrator (shared IAM)
2. How they create: Administrator creates or updates the Person, Legal Cell/Advocate Post and Role **on Claim Management Module 01** (not inside Legal).
3. How they edit: Legal Administrator opens the Legal Post consumption register and confirms which shared Posts (Legal Cell, Advocate, others named by SPLOCA) may enter Legal web.
4. How they send for approval: The Person signs in to Legal web; Legal validates the session against the shared component and resolves the active Post. Shared provisioning (Claim Module 01) → Legal Post allow-list confirmation → Legal session validate → menus by Post → refuse on deactivation.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator (shared IAM) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator (shared IAM) opens history on the record. Legal menus and need-to-know follow that Post; Legal stores no independent password or Person record. If the Person is deactivated or the mapping ended on the shared component, the next Legal request is refused.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Consume shared Person, Post, Role, official identity, OTP-before-activation, 2FA, joiner–mover–leaver and login audit — **read/validate only**
- Legal Post consumption register: which shared Posts are allowed into Legal (configured on the shared component, not a second directory)
- Legal session bootstrap: resolve Person → active Post → Legal menu set
- Refuse Legal login when the shared Person is inactive or unmapped
- No create/update/delete of Person, Post, Role, OTP, 2FA or forensic audit inside Legal

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Legal Post consumption register (read-only from shared Posts) | Easy |
| Legal session bootstrap / active-Post confirmation | Medium |
| Consume shared person–post–role identity history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Shared session and Post-resolution operations | Medium |
| Update consume shared person–post–role identity | Medium |
| Search consume shared person–post–role identity | Medium |
| Read consume shared person–post–role identity history | Easy |

### Inputs
Shared Person identifier and session/2FA proof from Claim Module 01; Legal Post allow-list; active Person–Post mapping status.

### Outputs
Legal session bound to shared Person/Post; Post consumption register; login-refusal when shared identity is inactive.

### Business Rules
- There is no second user master in Legal Management.
- Person create/update, Post, Role-to-Post, Post-to-Person, official identity, OTP, 2FA, deactivation and forensic login audit remain on Claim Management Module 01.
- Legal Posts (Legal Cell, Advocate, others named by SPLOCA) are configured **on** the shared component.
- Deactivating the Person on the shared component blocks Legal web immediately.
- This feature estimates wiring and consumption only — not a full IAM rebuild.

### Validations
- Shared Person must exist and be active; active Person–Post mapping required; Post must be on the Legal allow-list; 2FA proof must be accepted by the shared component.

### Calculations
None.

### Workflow
Shared provisioning (Claim Module 01) → Legal Post allow-list confirmation → Legal session validate → menus by Post → refuse on deactivation.

### Search Requirements
Legal Post consumption register by Post name, Person display name (from shared), mapping status.

### Documents
None created here; login-audit artefacts remain on Claim Management F01-010.

### Reports
Legal Post consumption register (Excel) of shared Posts allowed into Legal.

### Notifications
Optional notice to Legal Administrator when a shared Person mapped to a Legal Post is deactivated (consumed event).

### Security
Session tokens issued only after shared 2FA; no local credential store; privileged allow-list changes audited against the shared Person.

### Integrations
Claim Management Module 01 Person–Post–Role, session, 2FA and deactivation events (Integration Complex — multi-system identity synchronisation, not a new directory).

### Dependencies
Claim Management Module 01 F01-001–F01-007 and F01-010 must be available. Legal F01-004 extends the same identity to Android.

### Assumptions
- Shared IAM is the only identity store. Legal stores session/Post cache only. Hours cover wiring, not rebuilding Person/Post/Role/OTP/2FA/audit.

### Risks
If Claim Module 01 is not ready, Legal web cannot authenticate. Incorrect Post allow-list can admit or exclude Legal users.

### Non Functional Requirements
HTTPS session; fail closed when shared identity is unreachable or deactivated; no generative AI.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Legal Post consumption register (read-only from shared Posts) | UI | Easy | 4 |
| Legal session bootstrap / active-Post confirmation | UI | Medium | 6 |
| Consume shared person–post–role identity history | UI | Medium | 6 |
| Shared session and Post-resolution operations | API | Medium | 6 |
| Update consume shared person–post–role identity | API | Medium | 6 |
| Search consume shared person–post–role identity | API | Medium | 6 |
| Read consume shared person–post–role identity history | API | Easy | 4 |
| Consume shared person–post–role identity persistence | DB | Medium | 4 |
| Claim Module 01 Person–Post–Role identity consumption | Integration | Complex | 24 |
| Consume shared Person–Post–Role identity feature tests | Testing | Complex | 8 |
| Consume shared Person–Post–Role identity implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **76** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
