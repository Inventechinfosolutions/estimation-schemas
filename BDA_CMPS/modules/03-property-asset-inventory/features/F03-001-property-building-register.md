# F03-001 — Property & Building Register

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F03-001 |
| **Feature Name** | Property & Building Register |
| **Module** | 03 — Property & Asset Inventory |

### Description
Maintain the system-of-record register for commercial complexes, buildings, and property headers including codes, names, type, address, areas, building facilities, and hierarchical placement under location masters.

### Business Objective
Digitize and centralize BDA commercial property and building inventory as the authoritative register for allotment, billing, and MIS.

### Actors
- Estate Officer, Property Manager, Data Entry Operator
- Approvers (per F02-009 / Commissioner as configured)
- Auditor (read-only)

### User Journey
1. Officer opens Property Register.
2. Creates a Complex/Building/Property with BDA code and attributes.
3. Captures address, classification, areas, lifts, utilities, fire safety, building age, parking capacity totals.
4. Submits for approval if configured; on approval record becomes active inventory.
5. Edits maintained with audit; hierarchical children (floors/units) managed in related features.

### Functional Capabilities
- Create/update property and building records
- System-generated and/or BDA property codes
- Link to location hierarchy and classification masters (Module 02)
- Building attributes: floors count, total shops/offices, parking capacity, lifts, utility connections, fire safety, age
- Carpet / built-up / rentable area at applicable levels
- Activate soft-retirement without hard delete
- Search, filter, Excel export of register

### Inputs
- Property code/name, complex, type, address, location refs, areas, facility attributes, status

### Outputs
- Saved property/building records
- Register list and export
- Approval task (when configured)

### Business Rules
- Unique property/unit identifiers across rentable inventory (M2-AC1 — enforced with F03-002).
- Property creation may require multi-level approval (M2-AC5 / F02-009).
- Masters from Module 02 supply lookups; this feature stores transactional inventory instances.
- Auctioned/litigation details beyond status flags are out of scope (status in F03-004).

### Validations
- Mandatory code/name/type/location
- Area values ≥ 0; built-up ≥ carpet where both present (configurable warning/error)
- Parent complex required for buildings when hierarchy mandates

### Calculations
- Optional totals rolled up from child units (floors/shops) when children exist

### Workflow
Draft → Submit → Approve/Reject (configurable) → Active inventory.

### Search Requirements
By code, name, complex, type, location, status; pagination.

### Documents
Link photos/docs via F03-006 / Module 08.

### Reports
Property Register (Excel); feeds Module 11 reports.

### Notifications
Approval requests/completions via Module 09.

### Security
RBAC + data scope (Module 01); audit all mutations.

### Integrations
None mandatory in this feature (map in F03-005).

### Dependencies
Modules 01–02; F02-009; F03-002–F03-004; Module 08/09

### Assumptions
- Boundary vs F02-002: Module 02 holds reusable master catalogues; Module 03 holds live inventory records used in operations.
- Enterprise validation, logging, unit tests included.
- Very High UI for large tabbed property/building form.

### Risks
- Duplicate modelling with F02-002 if design does not freeze boundary.
- Large legacy import volumes handled as migration service, not this feature.

### Non Functional Requirements
- List pages < 3s under agreed load
- Responsive web; Excel export
- English UI mandatory

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Property / complex / building list | UI | Complex | 8 |
| Property & building create/edit (tabs, areas, facilities) | UI | Very High | 16 |
| Property/building CRUD + search | API | Complex | 8 |
| Property create approval hooks | API | Medium | 6 |
| Property & building inventory schema | Database | Complex | 6 |
| Property register tests | Testing | Very High | 12 |
| Property & building register guide | Documentation | Medium | 3 |
| **Total** | | | **59** |

### Estimation Assumptions
- Property creation approval uses shared workflow config; runtime hooks estimated as Medium API here.
