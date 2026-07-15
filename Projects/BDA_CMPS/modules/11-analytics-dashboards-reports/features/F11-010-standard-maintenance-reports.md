# F11-010 — Standard Maintenance Reports

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-010 |
| **Feature Name** | Standard Maintenance Reports |
| **Module** | 11 — Analytics, Dashboards & Reports |

### Description
Maintenance report pack: Complaint, Work Order, Vendor Performance, AMC—with filters and PDF/Excel export.

### Business Objective
Operational MIS for maintenance leadership and vendor oversight.

### Actors
- Maintenance Officer, Chief Engineer, Auditor

### User Journey
Select maintenance report → filter → preview → export.

### Functional Capabilities
- Four named reports
- SLA/status filters for complaints/WO
- Vendor performance and AMC expiry views
- PDF/Excel export

### Inputs
- Report type, filters

### Outputs
- Preview/exports

### Business Rules
- M8-AC2 for this group.
- Data from Module 07.

### Validations
Filter rules.

### Calculations
- SLA breach counts; basic vendor score aggregates

### Workflow
N/A.

### Search Requirements
Preview.

### Documents
Exports.

### Reports
This feature.

### Notifications
None.

### Security
Scoped RBAC.

### Integrations
None.

### Dependencies
F11-001; Module 07

### Assumptions
- Complex (not Very High) API—smaller pack than financial.

### Risks
- Performance score methodology—keep basic as Module 07.

### Non Functional Requirements
- Exportable; scoped

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Maintenance report runner UI | UI | Complex | 8 |
| Maintenance report query ops (4 reports) | API | Complex | 8 |
| Maintenance report support | Database | Easy | 2 |
| PDF/Excel export ops | API | Medium | 6 |
| Maintenance reports tests | Testing | Complex | 8 |
| Maintenance reports guide | Documentation | Medium | 3 |
| **Total** | | | **35** |

### Estimation Assumptions
- Four reports as one pack.
