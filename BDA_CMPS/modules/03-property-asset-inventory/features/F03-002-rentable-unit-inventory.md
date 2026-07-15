# F03-002 — Rentable Unit Inventory

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F03-002 |
| **Feature Name** | Rentable Unit Inventory |
| **Module** | 03 — Property & Asset Inventory |

### Description
Maintain rentable units (shops, offices, open commercial spaces) under Complex → Building → Floor hierarchy with unique identifiers, areas, and current operational status.

### Business Objective
Ensure every rentable unit is uniquely identifiable and status-tracked for allotment and occupancy reporting (M2-AC1).

### Actors
- Estate Officer, Property Manager, Data Entry Operator

### User Journey
1. Officer selects building/floor.
2. Creates unit with shop/office/open-space attributes and areas.
3. System assigns unique unit ID; initial status typically Vacant.
4. Unit appears in vacancy and allocation availability views.

### Functional Capabilities
- CRUD for Shop/Unit/Office/Open Space under hierarchy
- Unique unit identifier (system + optional BDA number)
- Carpet / built-up / rentable area
- Floor and unit numbering
- Current status display (lifecycle changes in F03-004)
- Bulk-friendly list within a building
- Search/filter/export

### Inputs
- Parent building/floor, unit number, type, areas, remarks, status

### Outputs
- Unit records
- Availability for Module 04 allotment
- Export lists

### Business Rules
- Unit ID unique system-wide.
- Unit cannot move to Occupied except via lease handover (Module 04) or controlled status API.
- Deleting units with lease history not allowed; deactivate/block instead.
- Open commercial sites supported as rentable units without building where applicable.

### Validations
- Parent hierarchy required (except stand-alone open site pattern)
- Areas ≥ 0; unique unit number within floor/building rule

### Calculations
None beyond optional area totals.

### Workflow
May inherit property approval; unit add under active building typically direct with audit (configurable).

### Search Requirements
By unit ID, shop no., building, floor, type, status, area range.

### Documents
Via F03-006.

### Reports
Unit Register; feeds occupancy/vacancy reports.

### Notifications
None mandatory.

### Security
RBAC + property data scope.

### Integrations
None.

### Dependencies
F03-001; Module 02 masters; Module 04 for occupancy transitions.

### Assumptions
- Parking bays are F03-008 (separate inventory type).
- Initial status set on create; transitions governed by F03-004.

### Risks
- Inconsistent shop numbering in legacy data.

### Non Functional Requirements
- Efficient floor-wise grids for large complexes
- Excel export

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Unit / shop / open-space list | UI | Complex | 8 |
| Unit create/edit form (floor, areas, type) | UI | Complex | 8 |
| Unit CRUD + unique ID/search | API | Complex | 8 |
| Unit inventory schema & indexes | Database | Medium | 4 |
| Unit inventory tests | Testing | Complex | 8 |
| Unit inventory guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Complex UI for building-context grids + unit form; not a dashboard.
