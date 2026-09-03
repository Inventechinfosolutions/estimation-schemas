# F01-008 — Constrained OOK claimant access

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-008 |
| **Feature Name** | Constrained OOK claimant access |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
An out-of-Karnataka claimant logs in only to the constrained submission path, only while a claim window is open, and only sees their own pack. They cannot open staff menus, other claimants’ packs, or file after the window closes. In-Karnataka claimants are not given this self-service account.

### Business Objective
Provide a tightly scoped OOK login that cannot become a mass public portal or a staff session.

### Actors
OOK claimant; Administrator (enable constrained access); Officer (does not use this path for in-KA intake).

### User Journey
1. Who creates: OOK claimant
2. How they create: OOK claimant authenticates to the constrained path (not staff 2FA enrolment).
3. How they edit: The system checks that a claim window is open (F06-001) for the relevant FE/scheme.
4. How they send for approval: The claimant sees only their own pack and the submit path (F06-003). Authenticate → window check → own pack → submit path (F06-003). No staff workflow.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. OOK claimant works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: OOK claimant opens history on the record. Staff menus, other claimants’ packs, and filing after window close are refused. In-Karnataka claimants are not issued this self-service account; they attend the counter (F06-002).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Constrained OOK authentication distinct from staff Person/Post login.
- Window-gated access: refuse file after close.
- Own-pack visibility only.
- Block staff menus for OOK sessions.
- Do not issue this account type to in-KA claimants.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| OOK login and constrained shell | Complex |
| Own-pack list (OOK) | Easy |
| Constrained ook claimant access history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Window-gated own-pack access operations | Complex |
| Update constrained ook claimant access | Medium |
| Search constrained ook claimant access | Medium |
| Read constrained ook claimant access history | Easy |

### Inputs
OOK claimant identity token/credentials as Authority-approved; open window; own pack reference.

### Outputs
Constrained session; own-pack list; access denials for staff or third-party packs.

### Business Rules
- OOK claimant is not a department Person/Post.
- Access only during an open claim window and only for own pack.
- In-KA claimants do not receive unrestricted self-service filing accounts.

### Validations
- Session without an open window cannot submit.
- Pack identifiers not owned by the claimant are refused.
- Staff URL/menu access from an OOK session is refused.

### Calculations
Window open/closed against notification period.

### Workflow
Authenticate → window check → own pack → submit path (F06-003). No staff workflow.

### Search Requirements
OOK claimant sees only own pack; no cross-claimant search.

### Documents
Own claim pack only, subject to F06 document rules.

### Reports
None for the claimant. Administrator may see constrained-access event counts via F01-010.

### Notifications
Optional window-open/close notices if the Authority later requires them; not a marketing portal.

### Security
Channel separation: staff web versus constrained OOK. Need-to-know is own pack only. No staff 2FA enrolment on this path.

### Integrations
None beyond internal window status (F06-001) and pack records (F06-003).

### Dependencies
F06-001 claim window; F06-003 submit path. Distinct from F01-006 staff 2FA.

### Assumptions
- Existing limited online access outcomes are F06-005, not a second mass portal.
- Citizen mass portal accounts for in-KA claimants remain out of scope.

### Risks
- Relaxing OOK to a public portal would change Module 06 statutory split.
- Issuing OOK accounts to in-KA claimants would bypass BSA 2023 originals at the counter.

### Non Functional Requirements
OOK path is limited and simple. Staff web remains the official work channel. Primary official domain is not .org.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| OOK login and constrained shell | UI | Complex | 12 |
| Own-pack list (OOK) | UI | Easy | 4 |
| Constrained ook claimant access history | UI | Medium | 6 |
| Window-gated own-pack access operations | API | Complex | 8 |
| Update constrained ook claimant access | API | Medium | 6 |
| Search constrained ook claimant access | API | Medium | 6 |
| Read constrained ook claimant access history | API | Easy | 4 |
| OOK session and pack-scope persistence | DB | Medium | 4 |
| Constrained OOK claimant access feature tests | Testing | Complex | 8 |
| Constrained OOK claimant access implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **61** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
