# F03-007 — Building Occupancy Percentage

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F03-007 |
| **Feature Name** | Building Occupancy Percentage |
| **Module** | 03 — Property & Asset Inventory |

### Description
Automatically compute and display building occupancy percentage from child unit statuses (M2-AC2).

### Business Objective
Give managers real-time occupancy health without manual spreadsheets.

### Actors
- Estate Officer, Property Manager, executives (dashboards later Module 11)

### User Journey
1. User opens building summary.
2. Sees occupancy % derived from units (e.g., Occupied / total rentable units).
3. Value refreshes when unit statuses change.

### Functional Capabilities
- Define formula (default: Occupied units ÷ active rentable units × 100)
- Exclude Blocked/non-rentable from denominator if configured
- Show on building header and list columns
- Recalculate on status change events

### Inputs
- Unit statuses (system)

### Outputs
- Occupancy % on building
- Optional last-calculated timestamp

### Business Rules
- Updates automatically from unit statuses (M2-AC2).
- Parking bays may be excluded from building shop occupancy formula (configurable).
- Manual override not allowed (display-only computed).

### Validations
- Denominator zero → show N/A

### Calculations
- occupancy_pct = occupied_count / eligible_unit_count × 100

### Workflow
N/A (event-driven recompute).

### Search Requirements
Filter buildings by occupancy range (optional).

### Documents
None.

### Reports
Feeds Module 11 occupancy report.

### Notifications
None mandatory (thresholds could alert later).

### Security
Read per property scope.

### Integrations
None.

### Dependencies
F03-001, F03-002, F03-004.

### Assumptions
- Simple count-based formula baseline; area-weighted occupancy optional later.

### Risks
- Misconfigured exclusions skew KPIs.

### Non Functional Requirements
- Recalculation near-real-time after status change

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Occupancy % display on building views | UI | Easy | 4 |
| Occupancy computation operations | API | Medium | 6 |
| Occupancy snapshot/cache fields | Database | Easy | 2 |
| Occupancy calculation tests | Testing | Medium | 6 |
| Occupancy metric notes | Documentation | Simple | 1 |
| **Total** | | | **19** |

### Estimation Assumptions
- Lightweight derived metric; not a full analytics dashboard (Module 11).
