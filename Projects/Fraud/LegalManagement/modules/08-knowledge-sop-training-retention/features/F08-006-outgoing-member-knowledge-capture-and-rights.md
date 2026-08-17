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
1. Before or when a member leaves, authorised user captures designated knowledge assets (title, author, date).
2. Person is later deactivated on Claim Module 01.
3. Those documents remain searchable; sensitive items stay under controlled sharing.

### Functional Capabilities
- Outgoing-Member Knowledge Capture form
- Rights/share after deactivation
- Docket with title, author, date; word search
- Knowledge remains after Person deactivation on shared IAM
- Sensitive items Limited/controlled
- Does not keep the leaver’s login alive

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
Person identified; assets listed; title/author/date on docket; sensitive flag requires share list.

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
Joiner–mover–leaver process remains on Claim Module 01; Legal consumes the deactivation event.

### Risks
Failure to capture before the member leaves; over-retaining personal drafts that should have been Limited.

### Non Functional Requirements
Searchable after deactivation; rights persist.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Outgoing-Member Knowledge Capture form | UI | Complex | 12 |
| Rights/share after deactivation | UI | Medium | 6 |
| Capture and retain operations | API | Complex | 8 |
| Knowledge docket entities | Database | Medium | 4 |
| Shared IAM deactivation consume | Integration | Medium | 16 |
| Knowledge retention tests | Testing | Complex | 8 |
| Outgoing-member knowledge retention guide | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- Does not re-implement joiner–mover–leaver (Claim F01-007).
- Does not keep a parallel Person master.
