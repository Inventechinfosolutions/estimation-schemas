# F02-003 — Rental Classification Masters

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-003 |
| **Feature Name** | Rental Classification Masters |
| **Module** | 02 — Master Data & System Configuration |

### Description
Maintain Property Category, Property Type, and Lease Type masters used to classify commercial assets and lease agreements.

### Business Objective
Standardize classification for inventory, leasing, billing rules application, and MIS grouping.

### Actors
- Super Administrator, Estate Officer, Accounts Officer (as permitted)

### User Journey
1. Admin opens Rental Classification Masters.
2. Maintains Category / Type / Lease Type lists.
3. Activates/deactivates codes for controlled use in Modules 03–05.

### Functional Capabilities
- CRUD for Property Category, Property Type, Lease Type
- Optional mapping Category → allowed Types
- Activate/deactivate, search, export

### Inputs
- Code, name, description, status, parent/mapping where applicable

### Outputs
- Classification lookups
- Excel register

### Business Rules
- Deactivated codes blocked for new leases/properties; retained on history.
- Lease Type may drive which rule sets are selectable (rent/deposit/penalty).

### Validations
- Unique codes; mandatory name/code

### Calculations
None.

### Workflow
N/A (direct admin maintenance).

### Search Requirements
By code, name, status.

### Documents
None.

### Reports
Classification Register (Excel).

### Notifications
None.

### Security
RBAC + audit.

### Integrations
None.

### Dependencies
Module 01; consumed by Modules 03–05 and rule features F02-004–F02-006.

### Assumptions
Simple reference data; relationships to rules configured in rule features.

### Risks
Proliferation of ad-hoc types without governance.

### Non Functional Requirements
Standard admin UX; Excel export.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Classification master list + forms | UI | Medium | 6 |
| Classification CRUD + search | API | Medium | 6 |
| Classification master tables | Database | Easy | 2 |
| Classification master tests | Testing | Medium | 6 |
| Classification master docs | Documentation | Easy | 2 |
| **Total** | | | **22** |

### Estimation Assumptions
- Three related simple masters estimated as one Medium UI + Medium API package.
