# F01-002 — Post, Role-to-Post and Post-to-Person mapping

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Post, Role-to-Post and Post-to-Person mapping |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
An Administrator creates a Post (for example Officer or Competent Authority desk), assigns one or more Roles to that Post, then maps a Person to the Post with an effective-from date. When the mapping changes, the Administrator records effective-to, and the system keeps the previous mapping in history (who changed it, when, before/after). Staff see only the Posts currently mapped to them. This mapping is the shared authorisation model for Claim, Legal and Valuation.

### Business Objective
Attach permissions to Posts, occupy Posts with named Persons for dated periods, and retain complete mapping history for audit.

### Actors
Administrator; staff member (sees own current Posts); auditor (mapping history).

### User Journey
1. Who creates: Administrator
2. How they create: Administrator opens the Post catalogue and creates a Post (for example Officer, Competent Authority desk, Administrator).
3. How they edit: Administrator opens the Role-to-Post assignment and attaches one or more Roles (permission sets) to that Post.
4. How they send for approval: Administrator searches a Person and maps the Person to the Post with an effective-from date. Administrator maintains catalogue and mappings. History is append-only. No claimant participation.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record. When the occupant changes, Administrator sets effective-to on the old mapping and creates a new Post-to-Person row. Staff logging in see only Posts currently mapped to their Person; expired mappings remain in history.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Post catalogue create, update, view and search.
- Role-to-Post assignment of one or more Roles per Post.
- Post-to-Person mapping with effective-from and effective-to.
- Complete mapping history: who changed, when, before/after.
- Staff session resolves only currently effective Posts.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Post catalogue screen | Complex |
| Role-to-Post assignment matrix | Very High |
| Post-to-Person mapping with effective dates | Complex |
| Post, role-to-post and post-to-person mapping history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Mapping and history operations | Very High |
| Update post, role-to-post and post-to-person mapping | Medium |
| Search post, role-to-post and post-to-person mapping | Medium |
| Read post, role-to-post and post-to-person mapping history | Easy |

### Inputs
Post name, Role set, Person, effective-from, effective-to, change remarks.

### Outputs
Current Post occupancy; Role-to-Post assignments; append-only mapping history used by F09-007 reports.

### Business Rules
- Permissions attach to the Post via Roles, not directly to the Person.
- A Person may occupy one or more Posts; only currently effective mappings grant access.
- Closing a mapping records effective-to; the previous row is retained, not overwritten silently.
- There is no supported action to copy another occupant’s credentials (F01-007).

### Validations
- Post and at least one Role are required before mapping a Person.
- Effective-from is mandatory; effective-to must be on or after effective-from when set.
- Person must exist in F01-001.
- Overlapping mappings for the same Person and Post are refused or closed per policy.

### Calculations
Current-Post resolution from effective date ranges at session start.

### Workflow
Administrator maintains catalogue and mappings. History is append-only. No claimant participation.

### Search Requirements
Post name, Role, Person name/ID, mapping status (current / historical), effective dates.

### Documents
None.

### Reports
Current and historical mapping extracts (full operational report is F09-007).

### Notifications
Optional notice to the mapped Person when a Post is assigned or ended.

### Security
Only Administrator Posts maintain mappings. Mapping changes are privileged actions with actor, timestamp and before/after. Staff cannot alter their own Post occupancy.

### Integrations
Internal authorisation consumed by Claim, Legal and Valuation session/menu composition (F01-003).

### Dependencies
F01-001 Person master.

### Assumptions
- Example Posts include Officer, Competent Authority desk and Administrator; the Authority confirms the catalogue.
- Legal and Valuation do not rebuild Post/Role administration.

### Risks
- Incorrect Role-to-Post assignment can expose claim packs, KYC or payment records.
- Missing effective-to on a leaver mapping would leave access open.

### Non Functional Requirements
This is the programme-wide identity product consumed by Legal Management and GIS field valuation; staff screens must remain usable during claim windows; privileged actions are attributable to a named Person acting in a Post; primary official hosting identity is an approved government domain, not .org. Mapping history must be retrievable for access audit without granting access.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Post catalogue screen | UI | Complex | 12 |
| Role-to-Post assignment matrix | UI | Very High | 16 |
| Post-to-Person mapping with effective dates | UI | Complex | 12 |
| Post, role-to-post and post-to-person mapping history | UI | Medium | 6 |
| Mapping and history operations | API | Very High | 16 |
| Update post, role-to-post and post-to-person mapping | API | Medium | 6 |
| Search post, role-to-post and post-to-person mapping | API | Medium | 6 |
| Read post, role-to-post and post-to-person mapping history | API | Easy | 4 |
| Mapping history persistence | DB | Complex | 6 |
| Post, Role-to-Post and Post-to-Person mapping feature tests | Testing | Very High | 12 |
| Post, Role-to-Post and Post-to-Person mapping implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **100** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
