# F11-002 — Property Dashboard

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-002 |
| **Feature Name** | Property Dashboard |
| **Module** | 11 — Analytics, Dashboards & Reports |

### Description
Property dashboard showing total / occupied / vacant / under maintenance / under litigation counts and parking utilization, with drill-down.

### Business Objective
Give instant portfolio occupancy and status visibility.

### Actors
- Estate officers, executives, auditors

### User Journey
1. Open Property Dashboard with filters.
2. Review status tiles and parking utilization.
3. Drill into unit registers filtered by status.

### Functional Capabilities
- KPI tiles for each SOW status group
- Parking utilization widget
- Drill-down to Module 03 registers
- Period-as-of for status snapshot

### Inputs
- Shell filters

### Outputs
- KPI values; charts/tiles

### Business Rules
- Counts reconcile to inventory statuses for as-of date (M8-AC1 family).
- Scope applied.

### Validations
N/A beyond filters.

### Calculations
- Counts; parking utilization % = occupied bays / total bays

### Workflow
N/A.

### Search Requirements
Via drill-down registers.

### Documents
None.

### Reports
Feeds property reports; dashboard itself export optional image/PDF summary.

### Notifications
None.

### Security
Scoped.

### Integrations
None.

### Dependencies
F11-001; Module 03

### Assumptions
- Dashboard UI = Very High per Estimation Master.

### Risks
- Status definition mismatches with Module 03 — use shared status enums.

### Non Functional Requirements
- KPI load < 3s typical scoped set

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Property dashboard UI | UI | Very High | 16 |
| Property KPI query ops | API | Complex | 8 |
| Property KPI support | Database | Easy | 2 |
| Property dashboard tests | Testing | Complex | 8 |
| Property dashboard guide | Documentation | Easy | 2 |
| **Total** | | | **36** |

### Estimation Assumptions
- Single Very High dashboard UI.
