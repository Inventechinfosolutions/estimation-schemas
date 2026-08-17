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
1. Administrator opens the Post catalogue and creates a Post (for example Officer, Competent Authority desk, Administrator).
2. Administrator opens the Role-to-Post assignment and attaches one or more Roles (permission sets) to that Post.
3. Administrator searches a Person and maps the Person to the Post with an effective-from date.
4. When the occupant changes, Administrator sets effective-to on the old mapping and creates a new Post-to-Person row.
5. Staff logging in see only Posts currently mapped to their Person; expired mappings remain in history.

### Functional Capabilities
- Post catalogue create, update, view and search.
- Role-to-Post assignment of one or more Roles per Post.
- Post-to-Person mapping with effective-from and effective-to.
- Complete mapping history: who changed, when, before/after.
- Staff session resolves only currently effective Posts.

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
| Mapping and history operations | API | Very High | 16 |
| Mapping history persistence | DB | Complex | 6 |
| Mapping and occupancy tests | Testing | Very High | 12 |
| Post and mapping administration guide | Documentation | Complex | 4 |
| **Total** | | | **78** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Menu composition and need-to-know enforcement are estimated in F01-003.
- Dynamic Role-to-Post matrix is estimated as UI Very High (not UI Complex 8).
