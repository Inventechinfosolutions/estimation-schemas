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
1. On an asset or assignment the Officer selects FE name/code and CA name/code from the programme reference used by Claim Management (imported FE identity / existing FE application).
2. The Officer cannot create a new FE dossier here.
3. Later valuation reports show the same FE/CA labels as claims.

### Functional Capabilities
- Select FE and CA from programme references
- Refuse new FE dossier create in this application
- Show the same labels on valuation reports as on claims

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
|---|---|---|---:|
| FE/CA programme lookup | UI | Easy | 4 |
| FE/CA reference select | API | Easy | 4 |
| Cached FE/CA reference keys | Database | Easy | 2 |
| Claim / existing FE programme reference | Integration | Complex | 24 |
| FE/CA reference tests | Testing | Medium | 6 |
| FE/CA reference note | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- Multi-system reference (Claim + existing FE app) is Integration Complex 24, not a new FE product.
