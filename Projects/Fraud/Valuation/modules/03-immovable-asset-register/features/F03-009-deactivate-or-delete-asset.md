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
1. Authorised Office user or Administrator opens an asset and deactivates it (or hard-deletes if the Authority permits), with reason.
2. Action is history-logged.
3. Deactivated asset cannot be newly assigned (F04-001).
4. Officer login delete remains Claim Module 01.

### Functional Capabilities
- Deactivate asset with reason and history
- Hard delete only if the Authority permits
- Block new valuer assignment on deactivated assets
- Exclude Person/login delete from this feature

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
|---|---|---|---:|
| Asset deactivate confirmation | UI | Simple | 2 |
| Deactivate reason | UI | Easy | 4 |
| Deactivate with history | API | Medium | 6 |
| Asset active flag and history | Database | Easy | 2 |
| Assignment-block consume | Integration | Simple | 4 |
| Deactivate tests | Testing | Easy | 4 |
| Asset deactivate note | Documentation | Simple | 1 |
| **Total** | | | **23** |

### Estimation Assumptions
- Does not include IAM user delete hours.
