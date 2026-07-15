# F02-001 — Location Hierarchy Masters

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-001 |
| **Feature Name** | Location Hierarchy Masters |
| **Module** | 02 — Master Data & System Configuration |

### Description
Maintain BDA location hierarchy masters: Zone → Division → Circle → Ward → Layout → Survey Number, with activate/deactivate, search, and export for use across property and scoping modules.

### Business Objective
Provide a stable geographic/administrative reference structure for property placement, user data scoping, and reporting filters.

### Actors
- Super Administrator
- Estate Officer / Data Entry Operator (as permitted)
- All modules (consumers of location lookups)

### User Journey
1. Admin opens Location Masters.
2. Navigates hierarchy tree or level lists.
3. Creates/edits a node under its parent (e.g., Ward under Circle).
4. Activates or deactivates nodes without deleting history.
5. Exports location register as needed.

### Functional Capabilities
- CRUD for Zone, Division, Circle, Ward, Layout, Survey Number
- Parent–child hierarchy enforcement
- Codes, names, status, effective optional attributes
- Activate/deactivate with historical retention
- Search, filter, Excel export
- Lookup APIs for dependent dropdowns in other modules

### Inputs
- Level type, code, name, parent reference, status, remarks

### Outputs
- Saved location nodes
- Hierarchy tree / lists
- Export file

### Business Rules
- Child cannot be created without active parent (configurable exception for migration).
- Deactivated nodes cannot be selected for **new** transactions; remain visible on historical records.
- Unique code within level (or globally — configurable).
- Moving a node in hierarchy requires validation of descendant impact.

### Validations
- Mandatory code/name/parent (except root Zone)
- No circular parent references
- Cannot deactivate node with active children unless cascade policy approved

### Calculations
None.

### Workflow
Optional approval for hierarchy structural changes (if configured in F02-009). Baseline: authorized admin direct save with audit.

### Search Requirements
- By code, name, level, parent, status
- Tree expand/collapse and breadcrumbs

### Documents
None.

### Reports
Location Register (Excel).

### Notifications
None mandatory.

### Security
- Configure permission from Module 01
- All changes audited

### Integrations
None.

### Dependencies
- Module 01 permissions
- Consumed by F01-006, Module 03, reporting

### Assumptions
- Six-level hierarchy as listed in SOW is sufficient.
- GIS coordinates for locations are optional; property geo is Module 03.
- Enterprise CRUD with validation and logging included.

### Risks
- Legacy survey numbers may not fit clean hierarchy; migration mapping needed.
- Over-deep trees hurt UX without search-as-you-type.

### Non Functional Requirements
- Responsive admin UI
- Lookup performance suitable for dependent dropdowns
- English UI mandatory

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: multi-level hierarchy, integrity constraints, soft deactivate, tree UX.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Location hierarchy list (tree / level views) | UI | Complex | 8 |
| Location node create / edit form | UI | Medium | 6 |
| Activate / deactivate confirmation | UI | Simple | 2 |
| Location CRUD + hierarchy search | API | Complex | 8 |
| Location hierarchy entities & constraints | Database | Complex | 6 |
| Hierarchy integrity tests | Testing | Complex | 8 |
| Location master guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- One reusable hierarchical master pattern applied across six levels, not six fully independent apps.
