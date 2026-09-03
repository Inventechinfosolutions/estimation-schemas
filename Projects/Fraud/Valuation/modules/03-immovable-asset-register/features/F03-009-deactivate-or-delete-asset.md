# F03-009 — Deactivate or delete asset

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-009 |
| **Feature Name** | Deactivate or delete asset |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
An authorised Office user or Administrator opens an asset and deactivates it (or deletes if the Authority permits hard delete), with reason. The action is history-logged. A deactivated asset cannot be newly assigned (F04-001). Officer login create/update/delete remains Claim Management Module 01, not this feature.

### Business Objective
Remove an asset from new assignment without confusing that action with Person login delete.

### Actors
Office user (authorised); Administrator.

### User Journey
1. Who creates: Office user (authorised)
2. How they create: Authorised Office user or Administrator opens an asset and deactivates it (or hard-deletes if the Authority permits), with reason.
3. How they edit: Action is history-logged.
4. How they send for approval: Deactivated asset cannot be newly assigned (F04-001). Open asset → deactivate/delete with reason → history → F04-001 excludes.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user (authorised) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user (authorised) opens history on the record. Officer login delete remains Claim Module 01.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Deactivate asset with reason and history
- Hard delete only if the Authority permits
- Block new valuer assignment on deactivated assets
- Exclude Person/login delete from this feature

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Asset deactivate confirmation | Simple |
| Deactivate reason | Easy |
| Deactivate or delete asset history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Deactivate with history | Medium |
| Update deactivate or delete asset | Medium |
| Search deactivate or delete asset | Medium |
| Read deactivate or delete asset history | Easy |

### Inputs
Asset; deactivate or delete; reason.

### Outputs
Inactive (or deleted) asset; history; assignment list exclusion.

### Business Rules
- Deactivated asset is not offered for new valuer assignment
- Login create/update/delete remains Claim Module 01
- Hard delete only if permitted

### Validations
- Authorised Post
- Reason present
- No silent delete of assignment history

### Calculations
None.

### Workflow
Open asset → deactivate/delete with reason → history → F04-001 excludes.

### Search Requirements
Include inactive when authorised; default search active only.

### Documents
None.

### Reports
Deactivated assets with reason.

### Notifications
None.

### Security
Authorised only; attributable; not a back door to delete Persons.

### Integrations
Internal assignment eligibility (F04-001).

### Dependencies
F04-001; Claim Module 01 for login lifecycle.

### Assumptions
- Authority states whether hard delete is allowed.

### Risks
Hard delete of an asset already released to Claim would orphan the pack.

### Non Functional Requirements
History retained on deactivate even if hard delete is later allowed only for never-assigned drafts.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Asset deactivate confirmation | UI | Simple | 2 |
| Deactivate reason | UI | Easy | 4 |
| Deactivate or delete asset history | UI | Medium | 6 |
| Deactivate with history | API | Medium | 6 |
| Update deactivate or delete asset | API | Medium | 6 |
| Search deactivate or delete asset | API | Medium | 6 |
| Read deactivate or delete asset history | API | Easy | 4 |
| Deactivate or delete asset persistence | DB | Medium | 4 |
| Assignment-block consume | Integration | Simple | 4 |
| Deactivate or delete asset feature tests | Testing | Easy | 4 |
| Deactivate or delete asset implementation documentation | Documentation | Simple | 1 |
| **Total** | | | **47** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
