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
1. Who creates: Legal Cell (space owner)
2. How they create: Authorised Legal Cell user opens Legal Spaces and chooses Limited or Community.
3. How they edit: For Limited: names Persons (from shared identity) and attaches a matter folder.
4. How they send for approval: A Person not on the named list is refused when opening that folder. Create space → add named members or publish Community → attach folder → enforce on every open → membership change audited.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell (space owner) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell (space owner) opens history on the record. For Community: publishes the space to all authorised Legal community members; shared hierarchy still filters visibility. Owner later adds or removes named members; membership history is retained.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Limited Space Create/Members screen: named Persons only
- Community Publish screen: authorised Legal community
- Matter-folder attachment to a space
- Refuse open for non-members of Limited spaces
- Membership add/remove with audit against shared Person

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Limited Space Create/Members screen | Complex |
| Community Publish screen | Medium |
| Limited vs community legal spaces history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Space membership and folder-attach operations | Complex |
| Update limited vs community legal spaces | Medium |
| Search limited vs community legal spaces | Medium |
| Read limited vs community legal spaces history | Easy |

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
- Owner Post must be allowed to create spaces; named members must be active shared Persons; matter folder must exist; Community publish requires community-eligible Post.

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
- Community membership is the set of Posts SPLOCA marks as Legal community on the shared component.

### Risks
Mis-tagging Community can over-expose a matter folder; omitted named member blocks legitimate Limited work.

### Non Functional Requirements
Access check on every folder open; membership changes effective immediately.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Limited Space Create/Members screen | UI | Complex | 12 |
| Community Publish screen | UI | Medium | 6 |
| Limited vs community legal spaces history | UI | Medium | 6 |
| Space membership and folder-attach operations | API | Complex | 8 |
| Update limited vs community legal spaces | API | Medium | 6 |
| Search limited vs community legal spaces | API | Medium | 6 |
| Read limited vs community legal spaces history | API | Easy | 4 |
| Limited vs community legal spaces persistence | DB | Medium | 4 |
| Shared Person lookup for named members | Integration | Simple | 4 |
| Limited vs Community legal spaces feature tests | Testing | Complex | 8 |
| Limited vs Community legal spaces implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
