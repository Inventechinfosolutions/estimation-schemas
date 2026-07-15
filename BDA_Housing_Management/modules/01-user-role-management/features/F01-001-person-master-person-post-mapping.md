# F01-001 — Person Master & Person–Post Mapping

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Person Master & Person–Post Mapping |
| **Module** | 01 — User & Role Management |

### Description
Maintain BDA officer/person records and map each person to one or more organisational **Posts**. Access rights are not assigned directly to the person; they are derived from the Post’s Role (see F01-002 / F01-003).

### Business Objective
Establish the BDA staffing model where a person occupies a post, and operational authority follows the post.

### Actors
Super Administrator; departmental administrator; Auditor (read-only).

### User Journey
1. Administrator creates or updates a Person (employee identity, contact, status).  
2. Opens Person–Post Mapping and assigns the person to an active Post with effective-from / effective-to (where used).  
3. Marks primary/active post when a person holds multiple posts.  
4. Activates or releases the mapping; person retains history when unmapped.

### Functional Capabilities
- Person master: create, update, view, activate/deactivate, search, export  
- Person–Post mapping: one person to one or many posts over time  
- Primary / current post selection for session authority  
- Prevent overlapping invalid mappings as configured  
- Person and mapping audit history  

### Inputs
Person identity (name, employee reference, contact), login linkage, status, Post reference(s), mapping effective dates, primary flag.

### Outputs
Person record, Person–Post mapping register, exportable staff register.

### Business Rules
- Permissions are never attached directly to a Person.  
- A Person gains operational access only through an active Person–Post mapping to an active Post that has an active Role.  
- Deactivating a Person closes future login while retaining history.  
- Ending a Person–Post mapping removes authority from that Post immediately for new actions.  
- Citizen portal users are out of this feature (F01-005 / Module 06).

### Validations
Unique person/login identifiers; active Post required for new mappings; no conflicting primary post; date range validity.

### Calculations
None.

### Workflow
Direct administration with audit; maker-checker only if configured.

### Search Requirements
Person name, employee ID, login ID, Post, Role (via Post), mapping status, active status.

### Documents
None.

### Reports
Person Register; Person–Post Mapping Register (Excel).

### Notifications
Optional notice when a person is mapped/unmapped to a post.

### Security
RBAC for administrators; privileged mapping changes audited.

### Integrations
Internal authorisation handoff (Simple).

### Dependencies
F01-003 (Post master); F01-002 (Role permissions via Post); F01-004 (login resolves via active post).

### Assumptions
A person may hold more than one post; session uses configured primary/active post unless the user is allowed to switch posts.

### Risks
Incorrect Person–Post mapping grants or removes authority unexpectedly.

### Non Functional Requirements
Responsive admin UI; auditable mapping changes; agreed response targets.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Person register + search/filters | UI | Complex | 8 |
| Person create/edit form | UI | Complex | 8 |
| Person–Post mapping UI (multi-post, primary, dates) | UI | Very High | 16 |
| Person and mapping lifecycle operations | API | Complex | 8 |
| Person, mapping entities and constraints | Database | Complex | 6 |
| Internal authorisation handoff | Integration | Simple | 4 |
| Person/post mapping tests | Testing | Very High | 12 |
| Person & mapping administration guide | Documentation | Medium | 3 |
| **Total** | | | **65** |

### Estimation Assumptions
- Uses Estimation Master values only.  
- Role/permission matrix remains in F01-002; Post definition in F01-003.  
