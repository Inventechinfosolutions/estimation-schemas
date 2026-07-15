# F01-006 — User Data Scope Mapping

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-006 |
| **Feature Name** | User Data Scope Mapping |
| **Module** | 01 — User & Role Management |

### Description
Map users to organizational location hierarchy and/or properties so list/search/dashboard data is restricted to authorized scope (Zone → Division → Circle → Ward → Layout and property/complex level).

### Business Objective
Enforce data-level authorization required by SOW (module + action + data-scope controls) for multi-location BDA operations.

### Actors
- Super Administrator
- Estate / Property administrators (if delegated)
- All scoped users (consumers)
- Auditor (read-only)

### User Journey
1. Admin opens a user record.
2. Assigns one or more location nodes and/or specific properties/complexes.
3. Saves scope.
4. At runtime, queries in business modules filter to effective scope (including child locations when a parent is granted).

### Functional Capabilities
- Assign location hierarchy scope
- Assign explicit property/complex scope
- “All locations” flag for headquarters roles (Commissioner/Super Admin)
- View effective scope resolution (inherited children)
- Prevent save with empty scope for non-global roles (configurable)

### Inputs
- User ID
- Location node IDs
- Property/complex IDs
- Global scope flag

### Outputs
- Saved scope mapping
- Effective scope set used by authorization/query filters

### Business Rules
- Parent location grant implies access to descendant locations unless explicitly restricted.
- Explicit property grants add to location grants.
- Global scope only for roles permitted to have it.
- Tenant portal users scoped implicitly to own tenant/leases (not admin hierarchy mapping).

### Validations
- Referenced locations/properties must be active
- Non-global users require at least one scope node when policy demands
- Cannot assign properties outside admin’s own scope (delegated admin)

### Calculations
- Effective scope expansion (parent → children)

### Workflow
N/A beyond save + audit. Optional approval for granting global scope.

### Search Requirements
- Find users by assigned location/property
- From location/property, list users with access (admin support)

### Documents
None.

### Reports
User–Scope matrix export (Excel) for access reviews.

### Notifications
Optional notification when scope widened significantly.

### Security
- Scope enforced server-side on data queries
- Scope changes audited
- Privilege to grant global scope tightly controlled

### Integrations
None (uses Master/Property data from Modules 02/03).

### Dependencies
- F01-004, F01-005
- Module 02 location masters
- Module 03 property register (for property-level grants)
- All business modules must apply scope filters

### Assumptions
- Location hierarchy exists as in SOW.
- Property-level grants supported in addition to location nodes.
- Complex UI justified by hierarchical multi-select and effective-scope preview.
- Until Module 03 is live, location-only scoping may be used.

### Risks
- Incorrect hierarchy expansion may over/under-expose data.
- Performance risk if effective scope expansion is naive on large trees.

### Non Functional Requirements
- Scope resolution efficient enough for list queries under agreed load
- Admin UI responsive for large location trees (search-as-you-type)

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: hierarchy inheritance, property grants, effective scope preview, server-side enforcement patterns.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Data scope assignment UI (hierarchy multi-select) | UI | Complex | 8 |
| Scope assign / resolve operations | API | Complex | 8 |
| User–scope mapping entities | Database | Medium | 4 |
| Data scope enforcement tests | Testing | Complex | 8 |
| Data scoping guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- Business module query filter plumbing is lightly accounted in API complexity here as shared resolve APIs; deep per-module filter work remains in respective modules.
