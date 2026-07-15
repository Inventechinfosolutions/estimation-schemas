# F01-003 — Post Master, Post–Role & Post–Manager Mapping

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | Post Master, Post–Role & Post–Manager Mapping |
| **Module** | 01 — User & Role Management |

### Description
Maintain the BDA **Post** master. Each Post is assigned a **Role** (permissions). Each Post may be linked to a **Manager Post** for organisational reporting. Approval workflow levels (configured in F02-004) resolve to **Posts**, not to persons.

### Business Objective
Represent BDA’s post hierarchy so authority, reporting, and approval routing follow posts consistently.

### Actors
Super Administrator; departmental administrator; Auditor (read-only).

### User Journey
1. Administrator creates a Post (code, title, section/department, status).  
2. Attaches exactly one active Role to the Post (or replaces Role with effective date if configured).  
3. Maps the Post to its Manager Post (reporting line); validates no circular manager chain.  
4. Optionally marks the Post as eligible for specific approval levels / processes (consumed by F02-004 runtime).  
5. Reviews Post register, incumbent persons (from F01-001), and manager tree.

### Functional Capabilities
- Post master CRUD, activate/deactivate, search, export  
- Post → Role assignment  
- Post → Manager Post mapping (org hierarchy)  
- Circular-reference prevention and hierarchy view  
- View current Person–Post incumbents (read-only from F01-001)  
- Post eligibility for approval-level routing (as configured)

### Inputs
Post code/title, organisation unit, Role, Manager Post, status, optional approval-level eligibility.

### Outputs
Post register, Post–Role map, Post–Manager hierarchy, exportable org view.

### Business Rules
- A Post must have an active Role before it can grant operational access to mapped persons.  
- Manager Post, if set, must be a different active Post; no cycles in the manager chain.  
- Deactivating a Post ends authority for mapped persons and blocks new mappings.  
- Approval worklists and routing identify **Posts**; the incumbent Person on that Post acts.  
- Historical Post–Role and manager changes are retained for audit.

### Validations
Unique Post code; active Role required when Post is active; manager existence; acyclic manager graph; organisation unit required as configured.

### Calculations
None (hierarchy depth display only).

### Workflow
Direct administration with audit; maker-checker if configured.

### Search Requirements
Post code/title, Role, Manager Post, department/section, status, incumbent person.

### Documents
None.

### Reports
Post Register; Post–Role Map; Post–Manager Hierarchy export.

### Notifications
Optional notice when Role or Manager Post changes on a Post.

### Security
Administrator-only edits; all Post/Role/manager changes audited.

### Integrations
Internal authorisation and workflow routing handoff (Simple).

### Dependencies
F01-002 (Roles); F01-001 (Person–Post incumbents); F02-004 (approval process levels use Posts).

### Assumptions
One Role per Post in baseline (multi-role per Post not required unless BDA extends later).  
Delegated acting charge may be modelled later as temporary Person–Post mapping.

### Risks
Wrong Manager Post or Role assignment misroutes approvals and reporting.

### Non Functional Requirements
Hierarchy view usable for large org charts; changes effective for new routing immediately.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Post register + filters | UI | Complex | 8 |
| Post create/edit + Role assignment | UI | Complex | 8 |
| Post–Manager mapping + hierarchy view | UI | Very High | 16 |
| Approval-level Post eligibility editor | UI | Medium | 6 |
| Post, Role link, manager hierarchy operations | API | Very High | 16 |
| Post/role/manager persistence + cycle constraints | Database | Complex | 6 |
| Workflow routing handoff (Post-based) | Integration | Simple | 4 |
| Post hierarchy & role attachment tests | Testing | Very High | 12 |
| Post administration guide | Documentation | Complex | 4 |
| **Total** | | | **80** |

### Estimation Assumptions
- Uses Estimation Master values only.  
- Replaces prior “approval-level user mapping”; routing is Post-based.  
- Person–Post mapping effort remains in F01-001.  
