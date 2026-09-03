# F01-007 — Joiner–mover–leaver; no credential sharing

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-007 |
| **Feature Name** | Joiner–mover–leaver; no credential sharing |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
When an official leaves, the Administrator deactivates that Person’s account; the old password cannot be reused. When a new official joins, the Administrator creates a new Person, maps the correct Post, and issues new credentials. The Administrator has no supported action to copy or share the previous occupant’s login with the joiner. Historical audit rows remain after deactivation.

### Business Objective
Stop credential sharing on post handover so joiners never inherit a leaver’s login.

### Actors
Administrator; joiner; leaver (subject of deactivation); auditor.

### User Journey
1. Who creates: Administrator
2. How they create: On a leaver, Administrator opens the Person, deactivates the account, and confirms the password cannot be reused.
3. How they edit: Historical audit rows for that Person remain retrievable.
4. How they send for approval: On a joiner, Administrator creates a new Person (F01-001), maps the correct Post (F01-002), and issues new credentials. Leaver deactivation; mover remapping; joiner new Person + mapping + credentials. No shared-mailbox handover.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record. Administrator has no action to copy or share the previous occupant’s login with the joiner. On a mover, Administrator ends the old Post mapping and creates a new mapping without transferring credentials.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Deactivate a Person’s account on leave; block reuse of the old password.
- Issue new credentials only to a new Person for a joiner.
- Remap Posts for movers without credential transfer.
- Refuse any copy/share-previous-login action.
- Retain historical audit after deactivation.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My joiner–mover–leaver; no credential sharing list / queue | Medium |
| Joiner–mover–leaver workbench | Complex |
| Joiner–mover–leaver; no credential sharing history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| JML lifecycle and credential-block operations | Complex |
| Update joiner–mover–leaver; no credential sharing | Medium |
| Search joiner–mover–leaver; no credential sharing | Medium |
| Read joiner–mover–leaver; no credential sharing history | Easy |

### Inputs
Person, JML action (joiner / mover / leaver), Post mapping, new credentials for joiners.

### Outputs
Deactivated or newly credentialed Person; updated mappings; retained audit history.

### Business Rules
- Credential sharing is prohibited.
- Each Person has a unique account; relieved staff are deactivated.
- New joiners receive new accounts mapped to the correct Post/Role.
- Deactivation shall not delete historical audit records.

### Validations
- Deactivation requires an Administrator Post.
- Joiner credentials cannot equal the previous occupant’s stored credential.
- Leaver mapping is ended (effective-to) as part of deactivation.

### Calculations
None.

### Workflow
Leaver deactivation; mover remapping; joiner new Person + mapping + credentials. No shared-mailbox handover.

### Search Requirements
Person, credential status, last JML action, Post occupancy.

### Documents
None.

### Reports
Joiner–mover–leaver activity extract for administrators.

### Notifications
Optional notice that an account was deactivated or that new credentials were issued (to official identity only).

### Security
No supported credential-copy. Deactivation immediately blocks staff login (including 2FA). Audit retained.

### Integrations
Internal identity / credential store.

### Dependencies
F01-001, F01-002, F01-004, F01-005, F01-006.

### Assumptions
- Break-glass emergency access, if ever required, is a separate Authority policy and is not a shared-password procedure.

### Risks
- Informal password handover outside the application would bypass this control.
- Failing to set effective-to on the leaver Post would leave menu access theoretically mapped.

### Non Functional Requirements
This is the programme-wide identity product consumed by Legal Management and GIS field valuation; staff screens must remain usable during claim windows; privileged actions are attributable to a named Person acting in a Post; primary official hosting identity is an approved government domain, not .org. Deactivation must take effect immediately for staff sessions.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My joiner–mover–leaver; no credential sharing list / queue | UI | Medium | 6 |
| Joiner–mover–leaver workbench | UI | Complex | 12 |
| Joiner–mover–leaver; no credential sharing history | UI | Medium | 6 |
| JML lifecycle and credential-block operations | API | Complex | 8 |
| Update joiner–mover–leaver; no credential sharing | API | Medium | 6 |
| Search joiner–mover–leaver; no credential sharing | API | Medium | 6 |
| Read joiner–mover–leaver; no credential sharing history | API | Easy | 4 |
| Credential and mapping-history persistence | DB | Complex | 6 |
| Internal identity handoff | Integration | Simple | 4 |
| Joiner–mover–leaver; no credential sharing feature tests | Testing | Complex | 8 |
| Joiner–mover–leaver; no credential sharing implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **69** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
