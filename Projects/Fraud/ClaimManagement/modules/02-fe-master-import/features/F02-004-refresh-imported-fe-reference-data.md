# F02-004 — Refresh imported FE reference data

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-004 |
| **Feature Name** | Refresh imported FE reference data |
| **Module** | 02 — FE Master Import (from existing application) |

### Description
An authorised Officer or Administrator triggers a refresh from the existing FE application. The system updates FE details, Directors, Promoters and schemes already imported, without creating duplicate FE identities. Claim screens then show the refreshed name, scheme list and people references.

### Business Objective
Keep claim work on current FE name, people and scheme lists without duplicating FE identities.

### Actors
Officer; Administrator.

### User Journey
1. Officer or Administrator opens refresh and selects imported FE records (or a bulk refresh).
2. The system pulls current FE details, Directors, Promoters and schemes from the existing application.
3. Existing identities are updated; no second FE unique ID is created.
4. Officer reviews the delta (name, scheme list, people) on the refresh result.
5. Claim screens thereafter show the refreshed references.

### Functional Capabilities
- Trigger refresh of already-imported FE, directors/promoters and schemes.
- Update in place without duplicate FE identities.
- Show refresh delta for authorised review.

### Inputs
Refresh scope (FE(s)), source current values.

### Outputs
Updated references; refresh run log with inserted/updated/unchanged counts.

### Business Rules
- Refresh must not create a duplicate FE identity for the same source unique ID.
- In-flight claim packs keep the FE unique ID; displayed name/scheme list follows the refresh.

### Validations
- Refresh is refused if the source unique ID cannot be matched to an imported FE.
- Partial failure (schemes fail, FE name succeeds) is reported; it does not silently half-apply without a log.

### Calculations
Inserted / updated / unchanged / failed counts.

### Workflow
Authorised trigger → source pull → match on unique ID → update → claim screens consume new values.

### Search Requirements
Refresh runs by date, user, FE unique ID, result status.

### Documents
None.

### Reports
Refresh run log.

### Notifications
On-screen result; optional failure notice to the triggering user.

### Security
Authorised Posts only. Refresh is a privileged action audited in F01-010.

### Integrations
Existing FE Management application — refresh of FE details, people and schemes.

### Dependencies
F02-001, F02-002, F02-003.

### Assumptions
- Source unique IDs are stable. If the existing application reissues IDs, the Authority must confirm a match rule.

### Risks
- Unmatched IDs could either skip updates or, if mishandled, create duplicates.

### Non Functional Requirements
Refresh is auditable. Claim dropdowns show refreshed names without a second FE code.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Refresh trigger and delta review | UI | Complex | 12 |
| Refresh and de-duplication operations | API | Very High | 16 |
| Reference versioning persistence | DB | Complex | 6 |
| Existing FE application refresh sync | Integration | Complex | 24 |
| Refresh tests | Testing | Very High | 12 |
| FE refresh notes | Documentation | Medium | 3 |
| **Total** | | | **73** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Refresh is a second integration/sync slice (Complex 24) because it must update three reference types without duplicates.
