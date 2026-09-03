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
1. Who creates: Officer
2. How they create: Officer or Administrator opens refresh and selects imported FE records (or a bulk refresh).
3. How they edit: The system pulls current FE details, Directors, Promoters and schemes from the existing application.
4. How they send for approval: Existing identities are updated; no second FE unique ID is created. Authorised trigger → source pull → match on unique ID → update → claim screens consume new values.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Officer reviews the delta (name, scheme list, people) on the refresh result. Claim screens thereafter show the refreshed references.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Trigger refresh of already-imported FE, directors/promoters and schemes.
- Update in place without duplicate FE identities.
- Show refresh delta for authorised review.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My refresh imported fe reference data list / queue | Medium |
| Refresh trigger and delta review | Complex |
| Refresh imported fe reference data history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Refresh and de-duplication operations | Very High |
| Update refresh imported fe reference data | Medium |
| Search refresh imported fe reference data | Medium |
| Read refresh imported fe reference data history | Easy |

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
| My refresh imported fe reference data list / queue | UI | Medium | 6 |
| Refresh trigger and delta review | UI | Complex | 12 |
| Refresh imported fe reference data history | UI | Medium | 6 |
| Refresh and de-duplication operations | API | Very High | 16 |
| Update refresh imported fe reference data | API | Medium | 6 |
| Search refresh imported fe reference data | API | Medium | 6 |
| Read refresh imported fe reference data history | API | Easy | 4 |
| Reference versioning persistence | DB | Complex | 6 |
| Existing FE application refresh sync | Integration | Complex | 24 |
| Refresh imported FE reference data feature tests | Testing | Very High | 12 |
| Refresh imported FE reference data implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **101** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
