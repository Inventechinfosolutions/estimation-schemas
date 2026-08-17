# F01-004 — Official staff identity

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-004 |
| **Feature Name** | Official staff identity |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
An Administrator provisions a department user on an official or administered email and staff identity. The sign-up / login path does not accept a personal consumer email as the primary department identity. The user cannot complete staff provisioning until that official identity is recorded.

### Business Objective
Stop personal consumer email being used as the primary department identity for staff who will verify, approve or pay claims.

### Actors
Administrator; staff member being provisioned.

### User Journey
1. Administrator opens staff provisioning for a Person (F01-001).
2. Administrator enters official or administered email and staff identity particulars.
3. If a personal consumer email is offered as the primary department identity, the system refuses it.
4. Provisioning cannot be completed until official identity is recorded.
5. The staff member later uses that official identity on the login path (activation still requires F01-005 OTP).

### Functional Capabilities
- Capture official / administered email as primary staff identity.
- Refuse personal consumer email as primary department identity.
- Block completion of staff provisioning until official identity is recorded.
- Keep official identity distinct from OOK claimant login (F01-008).

### Inputs
Person, official email, administered staff identity markers, optional secondary contact.

### Outputs
Provisioned staff identity bound to the Person; incomplete provisioning remaining Inactive.

### Business Rules
- Personal consumer email is not the primary registration path for department users.
- Staff identity is bound to a Person; it is not a shared mailbox login for a Post.
- OOK claimants are not provisioned through this official staff path.

### Validations
- Primary email must match the Authority’s official / administered pattern.
- Person must exist before provisioning.
- Duplicate official email across Persons is refused.

### Calculations
None.

### Workflow
Administrator-driven provisioning. Account remains non-Active until OTP in F01-005.

### Search Requirements
Official email, Person name/ID, provisioning status.

### Documents
None.

### Reports
Staff identity provision list for administrators.

### Notifications
None until OTP send in F01-005.

### Security
Only Administrator Posts provision staff identity. Changes to primary email are audited.

### Integrations
Administered email / official-identity check (domain or directory rule as the Authority provides).

### Dependencies
F01-001 Person master.

### Assumptions
- The Authority confirms allowed official / administered email domains.
- SSO is out of scope unless later ordered.

### Risks
- Accepting personal email would recreate the website-review identity gap.
- Shared Post mailboxes used as login would break Person attribution.

### Non Functional Requirements
This is the programme-wide identity product consumed by Legal Management and GIS field valuation; staff screens must remain usable during claim windows; privileged actions are attributable to a named Person acting in a Post; primary official hosting identity is an approved government domain, not .org.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Staff official-identity provisioning form | UI | Medium | 6 |
| Official-identity policy enforcement | API | Complex | 8 |
| Official identity persistence | DB | Easy | 2 |
| Administered email / domain identity check | Integration | Easy | 8 |
| Official identity tests | Testing | Medium | 6 |
| Staff identity provisioning note | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- Uses Estimation Master values only.
- OTP-before-activation is estimated in F01-005.
- 2FA enrolment is estimated in F01-006.
