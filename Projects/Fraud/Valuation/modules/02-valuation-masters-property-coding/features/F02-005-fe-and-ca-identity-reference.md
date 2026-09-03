# F02-005 — FE and CA identity reference

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-005 |
| **Feature Name** | FE and CA identity reference |
| **Module** | 02 — Valuation Masters, Property Coding & References |

### Description
On an asset or assignment, the Officer selects FE name/code and CA name/code from the programme reference used by Claim Management (imported FE identity). The Officer cannot create a new FE dossier here. Later valuation reports show the same FE/CA labels as claims.

### Business Objective
Reuse programme FE/CA identity so valuation reports match claims without a second FE dossier.

### Actors
Office user.

### User Journey
1. Who creates: Office user
2. How they create: On an asset or assignment the Officer selects FE name/code and CA name/code from the programme reference used by Claim Management (imported FE identity / existing FE application).
3. How they edit: The Officer cannot create a new FE dossier here.
4. How they send for approval: Later valuation reports show the same FE/CA labels as claims. Lookup programme reference → select → store on asset/assignment → reports reuse labels.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Select FE and CA from programme references
- Refuse new FE dossier create in this application
- Show the same labels on valuation reports as on claims

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My fe and ca identity reference list / queue | Medium |
| FE/CA programme lookup | Easy |
| Fe and ca identity reference history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| FE/CA reference select | Easy |
| Update fe and ca identity reference | Medium |
| Search fe and ca identity reference | Medium |
| Read fe and ca identity reference history | Easy |

### Inputs
FE/CA lookup query; selected FE code; selected CA code.

### Outputs
FE/CA references stored on asset/assignment; consistent labels on reports.

### Business Rules
- Unique FE code (FE number, type, tri-lateral index) is not created in this SOW
- FE/CA on an asset is a selection, not a free duplicate dossier

### Validations
- Selected FE/CA exists in the programme reference
- Allotted-FE scope (F03-008) still applies on create

### Calculations
None.

### Workflow
Lookup programme reference → select → store on asset/assignment → reports reuse labels.

### Search Requirements
FE name/code, CA name/code.

### Documents
None.

### Reports
Assets by FE/CA (labels from this reference).

### Notifications
None.

### Security
Cannot invent FE identity. RBAC on lookup as on Claim import.

### Integrations
Claim import / existing FE application programme reference (mapping and retry). Not an FE Management rebuild.

### Dependencies
Claim FE import / existing FE application; F03-008 allotted-FE filter on create.

### Assumptions
- Programme FE/CA reference is available to valuation at go-live.

### Risks
Stale import would mismatch claim labels until refresh.

### Non Functional Requirements
Read-only dossier; no FE unique-code generation.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My fe and ca identity reference list / queue | UI | Medium | 6 |
| FE/CA programme lookup | UI | Easy | 4 |
| Fe and ca identity reference history | UI | Medium | 6 |
| FE/CA reference select | API | Easy | 4 |
| Update fe and ca identity reference | API | Medium | 6 |
| Search fe and ca identity reference | API | Medium | 6 |
| Read fe and ca identity reference history | API | Easy | 4 |
| Fe and ca identity reference persistence | DB | Medium | 4 |
| Claim / existing FE programme reference | Integration | Complex | 24 |
| FE and CA identity reference feature tests | Testing | Medium | 6 |
| FE and CA identity reference implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **72** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
