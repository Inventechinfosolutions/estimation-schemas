# F02-001 — Housing Structure Masters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Housing Structure Masters |
| **Module** | 02 — Master Data & System Configuration |

### Description
Maintain the configurable layout and housing attribute masters used by projects and units.

### Business Objective
Keep project and unit classification consistent without code changes.

### Actors
Super Administrator; section administrator; Auditor (read-only).

### User Journey
Administrator selects a master, maintains active values and their hierarchy where applicable, then makes approved values available to project and unit forms.

### Functional Capabilities
Maintain layouts, project/property types, towers, blocks, floors, BHK, facing, amenities; activate/deactivate; dependent selections.

### Inputs
Master value, code, description, parent context, status.

### Outputs
Active master values for business forms and exportable registers.

### Business Rules
Inactive values are unavailable for new use but retained on historical records; hierarchy selections must be valid.

### Validations
Unique codes per master; required parent for dependent values; active parent required.

### Calculations
None.

### Workflow
Direct maintenance with audit.

### Search Requirements
Master type, code, name, parent, active status.

### Documents
None.

### Reports
Housing Master Registers export.

### Notifications
None by default.

### Security
Administrator-only maintenance; audit all changes.

### Integrations
None.

### Dependencies
Module 01.

### Assumptions
No GIS or spatial platform is included.

### Risks
Inconsistent hierarchy setup can impair project/unit entry.

### Non Functional Requirements
Responsive administration; reliable lookup performance.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Housing master register + filters | UI | Complex | 8 |
| Hierarchy master editor | UI | Complex | 8 |
| Master maintenance operations | API | Complex | 8 |
| Master hierarchy persistence | Database | Complex | 6 |
| Master data tests | Testing | Complex | 8 |
| Housing master guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
