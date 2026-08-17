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
1. Administrator creates or updates the Person, Legal Cell/Advocate Post and Role **on Claim Management Module 01** (not inside Legal).
2. Legal Administrator opens the Legal Post consumption register and confirms which shared Posts (Legal Cell, Advocate, others named by SPLOCA) may enter Legal web.
3. The Person signs in to Legal web; Legal validates the session against the shared component and resolves the active Post.
4. Legal menus and need-to-know follow that Post; Legal stores no independent password or Person record.
5. If the Person is deactivated or the mapping ended on the shared component, the next Legal request is refused.

### Functional Capabilities
- Consume shared Person, Post, Role, official identity, OTP-before-activation, 2FA, joiner–mover–leaver and login audit — **read/validate only**
- Legal Post consumption register: which shared Posts are allowed into Legal (configured on the shared component, not a second directory)
- Legal session bootstrap: resolve Person → active Post → Legal menu set
- Refuse Legal login when the shared Person is inactive or unmapped
- No create/update/delete of Person, Post, Role, OTP, 2FA or forensic audit inside Legal

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
Shared Person must exist and be active; active Person–Post mapping required; Post must be on the Legal allow-list; 2FA proof must be accepted by the shared component.

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
Shared IAM is the only identity store. Legal stores session/Post cache only. Hours cover wiring, not rebuilding Person/Post/Role/OTP/2FA/audit.

### Risks
If Claim Module 01 is not ready, Legal web cannot authenticate. Incorrect Post allow-list can admit or exclude Legal users.

### Non Functional Requirements
HTTPS session; fail closed when shared identity is unreachable or deactivated; no generative AI.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Legal Post consumption register (read-only from shared Posts) | UI | Easy | 4 |
| Legal session bootstrap / active-Post confirmation | UI | Medium | 6 |
| Shared session and Post-resolution operations | API | Medium | 6 |
| Legal session and Post allow-list cache | Database | Easy | 2 |
| Claim Module 01 Person–Post–Role identity consumption | Integration | Complex | 24 |
| Shared-identity wiring tests | Testing | Complex | 8 |
| Shared identity consumption guide | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours are Estimation Master values only.
- Integration Complex (24) is wiring to shared IAM — not a second Person master.
- Person CRUD, OTP, 2FA and forensic audit hours belong to Claim Management Module 01, not this feature.
- Android dual-channel session is estimated in F01-004.
