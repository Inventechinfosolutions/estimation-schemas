# F03-006 — CAD / layout upload for maintenance and security

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-006 |
| **Feature Name** | CAD / layout upload for maintenance and security |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
An authorised Officer uploads a dimensioned site plan or CAD / digital layout to the asset. Another authorised officer opens it for maintenance and security. The file remains with the asset for CA and field use; this is not a separate drawing product.

### Business Objective
Keep CAD/layout with the valuation asset for maintenance, security and later CA review.

### Actors
Office user (authorised); Competent Authority (view in F07-005).

### User Journey
1. Who creates: Office user (authorised)
2. How they create: Authorised Officer uploads a dimensioned site plan or CAD/digital layout to the asset.
3. How they edit: Another authorised officer opens it for maintenance and security.
4. How they send for approval: File remains with the asset for CA (F07-005) and field use. Upload → store on asset → authorised open; CA opens in F07-005.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user (authorised) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user (authorised) opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Upload digital layout / CAD to the asset
- Open for authorised officers
- Keep the file with the asset (not a separate CAD product)

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My cad / layout upload for maintenance and security list / queue | Medium |
| CAD / layout upload and view | Medium |
| Cad / layout upload for maintenance and security history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| CAD attach | Easy |
| Update cad / layout upload for maintenance and security | Medium |
| Search cad / layout upload for maintenance and security | Medium |
| Read cad / layout upload for maintenance and security history | Easy |

### Inputs
CAD/layout file; optional description.

### Outputs
Stored layout on the asset.

### Business Rules
- Not a standalone drawing product
- Absence is visible on CA review; does not by itself block Accept unless the Authority marks CAD mandatory for that category (F07-005)

### Validations
- Authorised Post
- File stored against the asset

### Calculations
None.

### Workflow
Upload → store on asset → authorised open; CA opens in F07-005.

### Search Requirements
Asset, has-CAD yes/no.

### Documents
CAD / digital layout / dimensioned site plan.

### Reports
Assets missing CAD (informational).

### Notifications
None.

### Security
Authorised officers only; need-to-know with the asset.

### Integrations
Internal document storage.

### Dependencies
F03-001; F07-005.

### Assumptions
- Authoring CAD in a drawing tool is outside this application.

### Risks
Large CAD files; formats the viewer cannot open.

### Non Functional Requirements
File remains retrievable with the asset.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My cad / layout upload for maintenance and security list / queue | UI | Medium | 6 |
| CAD / layout upload and view | UI | Medium | 6 |
| Cad / layout upload for maintenance and security history | UI | Medium | 6 |
| CAD attach | API | Easy | 4 |
| Update cad / layout upload for maintenance and security | API | Medium | 6 |
| Search cad / layout upload for maintenance and security | API | Medium | 6 |
| Read cad / layout upload for maintenance and security history | API | Easy | 4 |
| Cad / layout upload for maintenance and security persistence | DB | Medium | 4 |
| Internal file storage | Integration | Simple | 4 |
| CAD / layout upload for maintenance and security feature tests | Testing | Easy | 4 |
| CAD / layout upload for maintenance and security implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
