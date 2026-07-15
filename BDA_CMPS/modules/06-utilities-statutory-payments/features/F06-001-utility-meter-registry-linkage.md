# F06-001 — Utility Meter Registry & Linkage

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F06-001 |
| **Feature Name** | Utility Meter Registry & Linkage |
| **Module** | 06 — Utilities & Statutory Payments |

### Description
Maintain utility meter instances linked to properties/units for Electricity, Water, DG, CAM, Sewage, and other configurable utility types, using Module 02 meter/type masters.

### Business Objective
Establish the metering spine required for readings, bills, and tenant recoveries.

### Actors
- Utility Officer, Property Manager, Data Entry Operator

### User Journey
1. Officer opens Meter Registry.
2. Creates meter with type, meter number, property/unit link, status.
3. Activates meter for reading entry.

### Functional Capabilities
- CRUD meter instances by utility type
- Link to property/unit (and complex/building context)
- Meter number uniqueness rules
- Active/inactive; search/export
- Support non-metered utility tracking flags where type allows informational bills only

### Inputs
- Utility type, meter no., property/unit refs, install date, status, remarks

### Outputs
- Meter register; lookup for readings

### Business Rules
- Meter master definitions from Module 02; instances live here.
- Inactive meters cannot receive new readings.
- External utility-company auto-fetch out of scope.

### Validations
- Unique meter number per type/scope rule
- Property/unit must exist and be in scope

### Calculations
None.

### Workflow
N/A.

### Search Requirements
By meter no., type, property, unit, status.

### Documents
Optional meter photos via Module 08.

### Reports
Meter Register (Excel).

### Notifications
None.

### Security
RBAC + property data scope.

### Integrations
None.

### Dependencies
Module 02 utility types/meter masters; Module 03 property/unit

### Assumptions
- CAM/Sewage may be non-metered charge types still listed under utilities for bill tracking.

### Risks
- Duplicate meter numbers from legacy data.

### Non Functional Requirements
- Scoped lists performant; Excel export

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Meter registry list + filters | UI | Medium | 6 |
| Meter create/edit & property/unit link form | UI | Complex | 8 |
| Meter CRUD + linkage ops | API | Medium | 6 |
| Meter instance schema | Database | Medium | 4 |
| Meter registry tests | Testing | Medium | 6 |
| Meter registry guide | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- Master types not rebuilt here (Module 02).
