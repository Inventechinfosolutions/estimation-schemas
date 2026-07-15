# F02-002 — Property Structure & Asset Masters

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-002 |
| **Feature Name** | Property Structure & Asset Masters |
| **Module** | 02 — Master Data & System Configuration |

### Description
Maintain property structure and asset reference masters: Commercial Complex, Building, Floor, Shop/Unit, Parking Area, Open Space, Utility Meter Master, and Asset Master, with linkage fields and activate/deactivate behaviour.

### Business Objective
Establish configurable structural catalogues that underpin inventory (Module 03), leasing, utilities, and expenditure without code changes for new master entries.

### Actors
- Super Administrator
- Estate Officer, Data Entry Operator
- Downstream modules (consumers)

### User Journey
1. Admin selects master type (e.g., Building Master).
2. Searches existing records; creates or edits attributes and parent links.
3. Links meters/assets to property/unit references where applicable.
4. Deactivates obsolete entries; system blocks new selection but keeps history.

### Functional Capabilities
- CRUD for Complex, Building, Floor, Shop/Unit, Parking Area, Open Space
- Utility Meter Master and Asset Master with property/unit linkage fields
- Hierarchical navigation aids (Complex → Building → Floor → Unit)
- Activate/deactivate; search/filter/export per master type
- Prevent orphaned new references when parent inactive

### Inputs
- Codes, names, parent references, type attributes, meter identifiers, asset attributes, status

### Outputs
- Saved master records
- Lookup lists for Module 03+ 
- Excel exports

### Business Rules
- Deactivated masters not selectable for new transactions; visible on historical records (M1-AC5).
- Unit/Shop belongs to Floor/Building/Complex chain as designed.
- Meter/Asset masters require valid parent property/unit reference when linkage is mandatory.
- **Boundary with Module 03:** Full transactional inventory (status lifecycle, geo photos, vacancy KPIs) is Module 03; this feature covers master/setup records and structural catalogues defined in SOW Module 1.

### Validations
- Unique codes per master type
- Parent must exist and be active for new children
- Mandatory fields by master type

### Calculations
None significant at master level.

### Workflow
Optional approval for create of Complex/Building (if F02-009 configured). Baseline admin save + audit.

### Search Requirements
- By code, name, parent, status, type
- Cross-type search optional via global master search

### Documents
Optional attachment of reference sketches — not mandatory; DMS linkage via Module 08 if used.

### Reports
Master registers per type (Excel).

### Notifications
None mandatory.

### Security
- RBAC configure permissions
- Audit trail on create/update/status change

### Integrations
None.

### Dependencies
- F02-001 (location attributes may be referenced)
- Module 01
- Consumed heavily by Module 03

### Assumptions
- Grouped into one feature (SOW intentional grouping); not one feature file per table.
- If BDA later decides Complex/Building live only in Module 03, effort should be reallocated—not double-counted.
- Enterprise quality included.

### Risks
- Overlap confusion with Module 03 inventory may cause duplicate data models if boundaries are not locked in design.
- Large volume of shops/units may need import tooling (migration is separate project activity).

### Non Functional Requirements
- Paginated lists for large unit counts
- Dependent dropdown performance
- Excel export

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: multiple related master types, hierarchy, meter/asset linkage, deactivate reference rules, volume testing.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Property/asset master list screens (multi-type) | UI | Complex | 8 |
| Complex / Building / Floor / Unit forms | UI | Complex | 8 |
| Parking / Open Space / Meter / Asset forms | UI | Medium | 6 |
| Master CRUD + hierarchical lookups | API | Complex | 8 |
| Activate / deactivate & reference checks | API | Medium | 6 |
| Property structure & asset master schema | Database | Complex | 6 |
| Master CRUD & reference tests | Testing | Very High | 12 |
| Property/asset master guide | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- Shared master framework reused across types; forms estimated as grouped Complex UI bundles, not 8 fully separate product UIs.
- Testing Very High due to cross-type reference matrix.
