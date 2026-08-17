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
1. Valuer completes foundation through facilities and special items for residential and/or non-residential as applicable, floor by floor.
2. Empty mandatory blocks block form issue (F05-007/F05-008).

### Functional Capabilities
- Specification proforma residential and/or non-residential
- Floor-by-floor entry as in the FRS
- Block statutory form issue while mandatory blocks are empty

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
|---|---|---|---:|
| Specification proforma (floor by floor) | UI | Complex | 12 |
| Spec save and mandatory-block gate | API | Medium | 6 |
| Specification blocks | Database | Medium | 4 |
| Internal form-issue gate | Integration | Simple | 4 |
| Specification tests | Testing | Medium | 6 |
| Specification proforma guide | Documentation | Medium | 3 |
| **Total** | | | **35** |

### Estimation Assumptions
- Not GIS; photographs remain Module 04 / F05-009.
