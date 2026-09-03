# F05-006 — Property specification proforma

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-006 |
| **Feature Name** | Property specification proforma |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
The Valuer completes the specification sheet (foundation, superstructure, fittings, flooring, roofing, finishing, sanitary, electrical, external services, facilities, special items) for residential and/or non-residential as applicable, floor by floor as in the FRS. Empty mandatory blocks block form issue.

### Business Objective
Complete the FRS reporting-format specification proforma before statutory form issue.

### Actors
Approved Valuer.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer completes foundation through facilities and special items for residential and/or non-residential as applicable, floor by floor.
3. How they edit: Empty mandatory blocks block form issue (F05-007/F05-008).
4. How they send for approval: Empty mandatory blocks block form issue (F05-007/F05-008). Complete spec sheet → validate mandatory blocks → allow form issue.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Specification proforma residential and/or non-residential
- Floor-by-floor entry as in the FRS
- Block statutory form issue while mandatory blocks are empty

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My property specification proforma list / queue | Medium |
| Specification proforma (floor by floor) | Complex |
| Property specification proforma history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Spec save and mandatory-block gate | Medium |
| Update property specification proforma | Medium |
| Search property specification proforma | Medium |
| Read property specification proforma history | Easy |

### Inputs
Specification blocks (foundation, superstructure, fittings, flooring, roofing, finishing, sanitary, electrical, external services, facilities, special items) per floor.

### Outputs
Completed specification sheet on the working.

### Business Rules
- Empty mandatory blocks block form issue
- Residential vs non-residential as applicable

### Validations
- Mandatory blocks complete before issue

### Calculations
None.

### Workflow
Complete spec sheet → validate mandatory blocks → allow form issue.

### Search Requirements
Asset, spec complete yes/no.

### Documents
Specification proforma.

### Reports
Specification sheet.

### Notifications
In-app block listing empty mandatory blocks.

### Security
Assigned valuer.

### Integrations
Internal gate to F05-007/F05-008.

### Dependencies
F05-001; F05-007.

### Assumptions
- FRS reporting format field list is supplied as the form template.

### Risks
Partial specs issued if the gate is only client-side.

### Non Functional Requirements
Server-side mandatory-block check.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My property specification proforma list / queue | UI | Medium | 6 |
| Specification proforma (floor by floor) | UI | Complex | 12 |
| Property specification proforma history | UI | Medium | 6 |
| Spec save and mandatory-block gate | API | Medium | 6 |
| Update property specification proforma | API | Medium | 6 |
| Search property specification proforma | API | Medium | 6 |
| Read property specification proforma history | API | Easy | 4 |
| Property specification proforma persistence | DB | Medium | 4 |
| Internal form-issue gate | Integration | Simple | 4 |
| Property specification proforma feature tests | Testing | Medium | 6 |
| Property specification proforma implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
