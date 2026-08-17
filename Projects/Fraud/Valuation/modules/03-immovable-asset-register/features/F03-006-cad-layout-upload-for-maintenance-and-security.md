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
1. Authorised Officer uploads a dimensioned site plan or CAD/digital layout to the asset.
2. Another authorised officer opens it for maintenance and security.
3. File remains with the asset for CA (F07-005) and field use.

### Functional Capabilities
- Upload digital layout / CAD to the asset
- Open for authorised officers
- Keep the file with the asset (not a separate CAD product)

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
|---|---|---|---:|
| CAD / layout upload and view | UI | Medium | 6 |
| CAD attach | API | Easy | 4 |
| CAD file metadata | Database | Easy | 2 |
| Internal file storage | Integration | Simple | 4 |
| CAD upload tests | Testing | Easy | 4 |
| CAD upload note | Documentation | Easy | 2 |
| **Total** | | | **22** |

### Estimation Assumptions
- CA-side open is F07-005; no CAD authoring tool.
