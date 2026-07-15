# F11-007 — Standard Property Reports

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-007 |
| **Feature Name** | Standard Property Reports |
| **Module** | 11 — Analytics, Dashboards & Reports |

### Description
Standard property report pack: Property Register, Vacancy, Occupancy, Property-wise Revenue, Property-wise Expense—with filters and PDF/Excel export (M8-AC2).

### Business Objective
Operational and statutory-style MIS extracts for estate and accounts.

### Actors
- Estate, Accounts, Auditor

### User Journey
1. Select report type and filters.
2. Preview grid.
3. Export PDF/Excel.

### Functional Capabilities
- Five named reports
- Scoped filters
- PDF & Excel export
- Column sets frozen per report definition

### Inputs
- Report type, filters

### Outputs
- Preview; PDF/Excel files

### Business Rules
- All listed standard reports available with filters and Excel/PDF (M8-AC2).
- Scope enforced.

### Validations
- Mandatory filters per report

### Calculations
- Report-specific totals

### Workflow
N/A.

### Search Requirements
Within preview grids.

### Documents
Generated exports (optional DMS archive).

### Reports
This feature.

### Notifications
None.

### Security
RBAC + scope.

### Integrations
None.

### Dependencies
F11-001; Modules 03–07

### Assumptions
- Very High API reflecting multi-report pack.
- Pixel-perfect legal formats beyond these = CR.

### Risks
- Layout iteration in UAT—freeze templates early.

### Non Functional Requirements
- Export completes for portfolio-sized datasets (async if large)

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Property report runner UI | UI | Complex | 8 |
| Property report query ops (5 reports) | API | Very High | 16 |
| Report definition support | Database | Medium | 4 |
| PDF/Excel export engine use | API | Medium | 6 |
| Property reports tests | Testing | Very High | 12 |
| Property reports guide | Documentation | Medium | 3 |
| **Total** | | | **49** |

### Estimation Assumptions
- Five reports estimated as one pack with Very High API.
