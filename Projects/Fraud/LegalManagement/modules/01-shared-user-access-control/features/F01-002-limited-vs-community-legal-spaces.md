# F01-002 — Limited vs Community legal spaces

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Limited vs Community legal spaces |
| **Module** | 01 — Shared User & Access Control (consumed) |

### Description
An authorised Legal Cell user creates a Limited space, adds named Persons, and shares a matter folder only with them. A Person not named cannot open that folder. For Community, the user publishes to all authorised Legal community members. Hierarchy / need-to-know from the shared RBAC still applies.

### Business Objective
Enforce need-to-know collaboration: named Limited membership versus Community publication, without rebuilding IAM.

### Actors
Legal Cell (space owner); Advocate (member); Competent Authority (where named); Administrator (space type policy).

### User Journey
1. Authorised Legal Cell user opens Legal Spaces and chooses Limited or Community.
2. For Limited: names Persons (from shared identity) and attaches a matter folder.
3. A Person not on the named list is refused when opening that folder.
4. For Community: publishes the space to all authorised Legal community members; shared hierarchy still filters visibility.
5. Owner later adds or removes named members; membership history is retained.

### Functional Capabilities
- Limited Space Create/Members screen: named Persons only
- Community Publish screen: authorised Legal community
- Matter-folder attachment to a space
- Refuse open for non-members of Limited spaces
- Membership add/remove with audit against shared Person

### Inputs
Space type (Limited/Community); named Person list (shared identifiers); matter folder reference; owner Post.

### Outputs
Legal space record; membership list; folder-access decisions; membership audit.

### Business Rules
- Limited = explicit named members only.
- Community = all authorised users of that Legal community, still subject to shared hierarchy / need-to-know.
- A Person outside a Limited space cannot open that space or its documents.
- Spaces do not create Persons; members are shared-identity Persons only.
- Need-to-know from Claim Module 01 RBAC is never bypassed by Community publish.

### Validations
Owner Post must be allowed to create spaces; named members must be active shared Persons; matter folder must exist; Community publish requires community-eligible Post.

### Calculations
None.

### Workflow
Create space → add named members or publish Community → attach folder → enforce on every open → membership change audited.

### Search Requirements
Space name, type (Limited/Community), owner, named member, linked matter.

### Documents
Matter folders shared into the space; no new document types.

### Reports
Limited space membership register; Community publication log.

### Notifications
Named member added/removed; Community publish notice to eligible Posts.

### Security
Folder open evaluated against space membership + shared Post hierarchy; non-members receive no listing.

### Integrations
Shared Person lookup for named members (Simple); matter folder identity from Module 04.

### Dependencies
F01-001 (shared Person); F01-003 (document rights on open); F04-004 / F05-006 consume spaces.

### Assumptions
Community membership is the set of Posts SPLOCA marks as Legal community on the shared component.

### Risks
Mis-tagging Community can over-expose a matter folder; omitted named member blocks legitimate Limited work.

### Non Functional Requirements
Access check on every folder open; membership changes effective immediately.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Limited Space Create/Members screen | UI | Complex | 12 |
| Community Publish screen | UI | Medium | 6 |
| Space membership and folder-attach operations | API | Complex | 8 |
| Space and membership entities | Database | Medium | 4 |
| Shared Person lookup for named members | Integration | Simple | 4 |
| Limited/Community access tests | Testing | Complex | 8 |
| Limited vs Community space guide | Documentation | Medium | 3 |
| **Total** | | | **45** |

### Estimation Assumptions
- Does not rebuild Person/Post; members are shared Persons.
- Document view/download/edit rights remain F01-003.
