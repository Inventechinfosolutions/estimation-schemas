# F03-003 — Hierarchy Navigation & Search

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F03-003 |
| **Feature Name** | Hierarchy Navigation & Search |
| **Module** | 03 — Property & Asset Inventory |

### Description
Provide hierarchical navigation Complex → Building → Floor → Unit/Shop/Parking/Open space and advanced search/filter across the property inventory.

### Business Objective
Help estate staff quickly locate assets across BDA’s multi-complex portfolio for operations and allotment.

### Actors
- Estate Officer, Property Manager, Data Entry Operator, Approvers (read)

### User Journey
1. User opens Inventory Explorer.
2. Expands hierarchy or uses search criteria (code, location, status, type, area).
3. Opens selected property/unit detail.

### Functional Capabilities
- Tree/breadcrumb hierarchy navigator
- Cross-level search and filters
- Respect data scope from Module 01
- Deep link to detail screens (F03-001/002/008)
- Save optional filter presets (nice-to-have; baseline = session filters)

### Inputs
- Navigation clicks; search criteria

### Outputs
- Scoped result sets; selected entity context

### Business Rules
- Users only see in-scope locations/properties.
- Inactive/hidden records appear only when filter allows.

### Validations
- Search date/range limits if used; pagination required

### Calculations
None.

### Workflow
N/A.

### Search Requirements
Full inventory finder: code, name, location, type, status, vacant-since, parking class.

### Documents
None.

### Reports
Search results export (Excel).

### Notifications
None.

### Security
Server-side scope enforcement.

### Integrations
None.

### Dependencies
F03-001, F03-002, F03-008; Module 01 scope.

### Assumptions
- Very High UI for hierarchy explorer + contextual panes.
- Global enterprise search service not a separate module.

### Risks
- Performance on large trees without lazy load — must lazy-load children.

### Non Functional Requirements
- Lazy loading; search < 3s typical
- Mobile-friendly browse for field staff

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Hierarchy navigator (Complex→Unit) | UI | Very High | 16 |
| Advanced property search panel | UI | Medium | 6 |
| Hierarchy & search query operations | API | Complex | 8 |
| Hierarchy query support/indexes | Database | Medium | 4 |
| Navigation/search tests | Testing | Complex | 8 |
| Navigation & search guide | Documentation | Easy | 2 |
| **Total** | | | **44** |

### Estimation Assumptions
- Hierarchy UX classified Very High (dynamic UI).
