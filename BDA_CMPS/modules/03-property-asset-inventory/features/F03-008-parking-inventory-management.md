# F03-008 — Parking Inventory Management

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F03-008 |
| **Feature Name** | Parking Inventory Management |
| **Module** | 03 — Property & Asset Inventory |

### Description
Maintain parking bay inventory by complex/building with occupancy and visitor/reserved classification; support linkage references to tenant/lease while rent is handled in Modules 04–05.

### Business Objective
Track parking asset stock and usage class as part of commercial inventory.

### Actors
- Estate Officer, Property Manager, Data Entry Operator

### User Journey
1. Officer opens Parking Inventory for a complex/building.
2. Creates bays/slots with identifiers and classification (visitor/reserved/general).
3. Updates occupancy status; views summary capacity vs used.
4. Lease module later links bay allocation (reference).

### Functional Capabilities
- CRUD parking bays/slots under complex/building
- Classification: visitor, reserved, general (configurable)
- Occupancy status tracking
- Capacity summaries vs building parking capacity attribute
- Search/filter/export
- Lease/tenant linkage reference (allocation commercial terms in Modules 04–05)

### Inputs
- Bay code, location refs, classification, status, linkage refs

### Outputs
- Parking register; utilization counts

### Business Rules
- Parking rent and billing in Modules 04–05, not here.
- Reserved classification ≠ property “Reserved” status (different domain); clarify in UI labels.
- Unique bay codes within complex.

### Validations
- Parent complex/building required
- Unique bay identifier

### Calculations
- Utilization % = occupied bays / total bays (optional display)

### Workflow
N/A baseline.

### Search Requirements
By bay code, complex, classification, occupancy.

### Documents
Optional photos via F03-006 pattern.

### Reports
Parking Inventory; utilization list (feeds Module 11 parking utilization).

### Notifications
None mandatory.

### Security
RBAC + scope.

### Integrations
None.

### Dependencies
F03-001; Modules 04–05 for lease-linked allocation/rent.

### Assumptions
- Inventory-first feature; not a visitor gate-pass system.
- No ANPR/IoT in scope.

### Risks
- Confusion between parking “reserved” class and unit status Reserved — UX labeling required.

### Non Functional Requirements
- Grid suitable for large bay counts
- Excel export

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Parking inventory list/grid | UI | Complex | 8 |
| Parking bay create/edit + classification | UI | Medium | 6 |
| Parking CRUD + occupancy ops | API | Complex | 8 |
| Parking inventory schema | Database | Medium | 4 |
| Parking inventory tests | Testing | Complex | 8 |
| Parking inventory guide | Documentation | Medium | 3 |
| **Total** | | | **37** |

### Estimation Assumptions
- No payment/rent logic included.
