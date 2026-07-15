# F07-003 — Inspection Scheduling & Execution

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F07-003 |
| **Feature Name** | Inspection Scheduling & Execution |
| **Module** | 07 — Operations, Maintenance & Expenditure |

### Description
Manage periodic and ad-hoc inspections with checklist templates by property type, observations, photos, recommendations, closure, and ability to spawn maintenance work orders (M6-AC3).

### Business Objective
Proactively assess property condition and feed maintenance actions and vacancy make-ready.

### Actors
- Maintenance Officer, Property Manager, Inspectors, Estate Officer (readiness)

### User Journey
1. Scheduler generates due periodic inspections (or officer creates ad-hoc).
2. Inspector opens checklist, records observations/photos/recommendations.
3. Closes inspection; optionally spawns work order/complaint (F07-002).
4. Vacancy readiness may be updated for Module 03 pipeline by reference.

### Functional Capabilities
- Inspection schedules (frequency by property type)
- Checklist templates configurable
- Ad-hoc inspections
- Observation capture, photo upload, recommendations
- Closure with outcome
- Spawn work order from findings
- Due inspection lists (M6-AC3)

### Inputs
- Schedule rules, property, checklist responses, photos, recommendations

### Outputs
- Inspection records; optional WO reference; due list

### Business Rules
- Inspection schedule generates due inspections and records checklist completion (M6-AC3).
- Failed critical checklist items can force WO creation (configurable).
- Completed inspections immutable except appendendum with audit.

### Validations
- Mandatory checklist items before close
- Property in scope

### Calculations
- Next due date from schedule frequency

### Workflow
Schedule due → Execute checklist → Close → (Spawn WO).

### Search Requirements
By property, type, due/overdue, outcome, inspector.

### Documents
Photos/reports (Module 08).

### Reports
Inspection Register; overdue inspections.

### Notifications
Due/overdue inspection alerts (Module 09).

### Security
RBAC + scope; audit.

### Integrations
None beyond DMS/notifications (covered in related features' handoffs; baseline ops internal).

### Dependencies
Module 03 properties; F07-002; Module 08/09; F02 templates-ish for checklists (owned here)

### Assumptions
- Checklist template admin included in this feature (not Module 02).
- Very High UI for checklist execution with photos.

### Risks
- Template sprawl — governance of checklist versions needed.

### Non Functional Requirements
- Tablet-friendly execution; offline not baseline

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Inspection schedule calendar/list | UI | Complex | 8 |
| Checklist execution & photo UI | UI | Very High | 16 |
| Inspection schedule & execute ops | API | Complex | 8 |
| Checklist template & inspection schema | Database | Medium | 4 |
| Inspection management tests | Testing | Complex | 8 |
| Inspection management guide | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
- Scheduler job included in API complexity.
