# F02-005 — Master Activate, Deactivate & Export

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-005 |
| **Feature Name** | Master Activate, Deactivate & Export |
| **Module** | 02 — Master Data & System Configuration |

### Description
Provide common controlled lifecycle actions, search, and exports for configured master records.

### Business Objective
Keep reference data usable, traceable, and reportable across BHMS.

### Actors
Super Administrator; section administrator; Auditor.

### User Journey
Authorised administrator searches a master register, reviews dependencies, activates/deactivates a value, and exports filtered results.

### Functional Capabilities
Cross-master status actions; dependency warning; register filters; Excel/PDF export where applicable; status history.

### Inputs
Master type, record, requested status, reason where required.

### Outputs
Status outcome, dependency warning, filtered export.

### Business Rules
Historical transactions retain inactive values; records with prohibited dependencies cannot be removed; deactivation reason may be mandatory by policy.

### Validations
Active user and permitted master required; valid status transition; date range for broad export.

### Calculations
None.

### Workflow
Search → review impact → status action → audit and export availability.

### Search Requirements
Master type, code/name, status, modified date, modified by.

### Documents
None.

### Reports
Master Status Change and Master Register exports.

### Notifications
Optional alert to relevant administrators for critical deactivation.

### Security
RBAC, impact warning, full configuration audit.

### Integrations
None.

### Dependencies
F02-001 through F02-004.

### Assumptions
Feature supplies shared lifecycle controls; individual master fields remain in owning features.

### Risks
Improper deactivation can interrupt new transaction entry.

### Non Functional Requirements
Consistent behaviour across master registers; export performance.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Master lifecycle action dialog | UI | Medium | 6 |
| Unified master search and export screen | UI | Complex | 8 |
| Status and export operations | API | Complex | 8 |
| Status history persistence | Database | Medium | 4 |
| Master lifecycle tests | Testing | Complex | 8 |
| Master lifecycle guide | Documentation | Easy | 2 |
| **Total** | | | **36** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
