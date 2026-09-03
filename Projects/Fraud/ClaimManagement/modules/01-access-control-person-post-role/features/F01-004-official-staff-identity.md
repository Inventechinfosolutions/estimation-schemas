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
1. Who creates: Administrator
2. How they create: Administrator opens staff provisioning for a Person (F01-001).
3. How they edit: Administrator enters official or administered email and staff identity particulars.
4. How they send for approval: If a personal consumer email is offered as the primary department identity, the system refuses it. Administrator-driven provisioning. Account remains non-Active until OTP in F01-005.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record. Provisioning cannot be completed until official identity is recorded. The staff member later uses that official identity on the login path (activation still requires F01-005 OTP).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Capture official / administered email as primary staff identity.
- Refuse personal consumer email as primary department identity.
- Block completion of staff provisioning until official identity is recorded.
- Keep official identity distinct from OOK claimant login (F01-008).

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My official staff identity list / queue | Medium |
| Staff official-identity provisioning form | Medium |
| Official staff identity history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Official-identity policy enforcement | Complex |
| Update official staff identity | Medium |
| Search official staff identity | Medium |
| Read official staff identity history | Easy |

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
| My official staff identity list / queue | UI | Medium | 6 |
| Staff official-identity provisioning form | UI | Medium | 6 |
| Official staff identity history | UI | Medium | 6 |
| Official-identity policy enforcement | API | Complex | 8 |
| Update official staff identity | API | Medium | 6 |
| Search official staff identity | API | Medium | 6 |
| Read official staff identity history | API | Easy | 4 |
| Official identity persistence | DB | Easy | 2 |
| Administered email / domain identity check | Integration | Easy | 8 |
| Official staff identity feature tests | Testing | Medium | 6 |
| Official staff identity implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **60** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
