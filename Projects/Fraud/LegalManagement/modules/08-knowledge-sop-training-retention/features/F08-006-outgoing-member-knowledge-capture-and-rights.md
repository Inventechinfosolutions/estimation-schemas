# F08-006 — Outgoing-member knowledge capture and rights

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-006 |
| **Feature Name** | Outgoing-member knowledge capture and rights |
| **Module** | 08 — Knowledge, SOP, Training & Retention |

### Description
Before or when a member leaves, an authorised user captures that member’s designated knowledge assets into the repository (title, author, date). After the Person is deactivated on the shared component, those documents remain searchable. Sensitive items stay under controlled sharing.

### Business Objective
Retain outgoing members’ designated knowledge after shared-IAM deactivation, with title/author/date docket and controlled sharing.

### Actors
Authorised knowledge owner; Administrator; Legal Cell (search after leaver).

### User Journey
1. Who creates: Authorised knowledge owner
2. How they create: Before or when a member leaves, authorised user captures designated knowledge assets (title, author, date).
3. How they edit: Person is later deactivated on Claim Module 01.
4. How they send for approval: Those documents remain searchable; sensitive items stay under controlled sharing. Capture assets → docket → deactivation on shared IAM → search still works → ACL holds.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Authorised knowledge owner works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Authorised knowledge owner opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Outgoing-Member Knowledge Capture form
- Rights/share after deactivation
- Docket with title, author, date; word search
- Knowledge remains after Person deactivation on shared IAM
- Sensitive items Limited/controlled
- Does not keep the leaver’s login alive

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Outgoing-Member Knowledge Capture form | Complex |
| Rights/share after deactivation | Medium |
| Outgoing-member knowledge capture and rights history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Capture and retain operations | Complex |
| Update outgoing-member knowledge capture and rights | Medium |
| Search outgoing-member knowledge capture and rights | Medium |
| Read outgoing-member knowledge capture and rights history | Easy |

### Inputs
Leaving Person (shared id); assets to capture; title; author; date; sensitivity/share list.

### Outputs
Retained knowledge docket; still searchable post-deactivation; controlled ACL.

### Business Rules
- After the Person is deactivated on the shared component, captured documents remain searchable.
- Sensitive items stay under controlled sharing.
- This is not a second user directory and does not reverse deactivation.
- Systemized aggregation of outgoing member’s proprietary knowledge (Annexure-I).

### Validations
- Person identified; assets listed; title/author/date on docket; sensitive flag requires share list.

### Calculations
None.

### Workflow
Capture assets → docket → deactivation on shared IAM → search still works → ACL holds.

### Search Requirements
Title, author, date, word search on retained docket.

### Documents
Captured knowledge assets.

### Reports
Outgoing-member capture register.

### Notifications
Reminder to capture before known leaver date (if HR/IAM event consumed).

### Security
Login ends on shared deactivation; documents do not become public; F01-003 still applies.

### Integrations
Shared IAM deactivation consume (Medium — mapping of Person inactive to retain-content, not rebuild IAM).

### Dependencies
F01-001; F01-002; F01-003; F08-001–F08-004.

### Assumptions
- Joiner–mover–leaver process remains on Claim Module 01; Legal consumes the deactivation event.

### Risks
Failure to capture before the member leaves; over-retaining personal drafts that should have been Limited.

### Non Functional Requirements
Searchable after deactivation; rights persist.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Outgoing-Member Knowledge Capture form | UI | Complex | 12 |
| Rights/share after deactivation | UI | Medium | 6 |
| Outgoing-member knowledge capture and rights history | UI | Medium | 6 |
| Capture and retain operations | API | Complex | 8 |
| Update outgoing-member knowledge capture and rights | API | Medium | 6 |
| Search outgoing-member knowledge capture and rights | API | Medium | 6 |
| Read outgoing-member knowledge capture and rights history | API | Easy | 4 |
| Outgoing-member knowledge capture and rights persistence | DB | Medium | 4 |
| Shared IAM deactivation consume | Integration | Medium | 16 |
| Outgoing-member knowledge capture and rights feature tests | Testing | Complex | 8 |
| Outgoing-member knowledge capture and rights implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **79** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
