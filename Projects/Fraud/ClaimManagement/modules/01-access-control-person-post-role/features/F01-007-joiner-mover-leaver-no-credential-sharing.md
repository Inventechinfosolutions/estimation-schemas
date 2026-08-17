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
1. On a leaver, Administrator opens the Person, deactivates the account, and confirms the password cannot be reused.
2. Historical audit rows for that Person remain retrievable.
3. On a joiner, Administrator creates a new Person (F01-001), maps the correct Post (F01-002), and issues new credentials.
4. Administrator has no action to copy or share the previous occupant’s login with the joiner.
5. On a mover, Administrator ends the old Post mapping and creates a new mapping without transferring credentials.

### Functional Capabilities
- Deactivate a Person’s account on leave; block reuse of the old password.
- Issue new credentials only to a new Person for a joiner.
- Remap Posts for movers without credential transfer.
- Refuse any copy/share-previous-login action.
- Retain historical audit after deactivation.

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
| Joiner–mover–leaver workbench | UI | Complex | 12 |
| JML lifecycle and credential-block operations | API | Complex | 8 |
| Credential and mapping-history persistence | DB | Complex | 6 |
| Internal identity handoff | Integration | Simple | 4 |
| JML and no-share tests | Testing | Complex | 8 |
| Joiner–mover–leaver guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Person create and Post mapping screens are estimated in F01-001/F01-002; this feature estimates the JML workbench and credential-block rules.
