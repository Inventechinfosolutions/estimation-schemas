# F03-005 — Geo-location & Map View

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F03-005 |
| **Feature Name** | Geo-location & Map View |
| **Module** | 03 — Property & Asset Inventory |

### Description
Capture and display property geo-location (lat/long + map pin) using GIS/map services so officers can pin and view assets on a map (M2-AC4).

### Business Objective
Improve asset discoverability and field verification with authoritative map context for BDA commercial properties.

### Actors
- Estate Officer, Property Manager, Data Entry Operator
- Read-only map consumers (other roles)

### User Journey
1. Officer opens property detail → Map tab.
2. Searches address or drops pin on map; system stores lat/long.
3. Later users view pin on map with property popup summary.

### Functional Capabilities
- Capture lat/long via map click and/or manual entry
- View property pin on map
- Optional list-to-map for filtered search results (same complex/view)
- Clear/update geo with audit

### Inputs
- Map click / lat / long / accuracy remarks

### Outputs
- Saved coordinates
- Map visualization

### Business Rules
- Coordinates optional or mandatory by property type (configurable).
- Invalid coordinate ranges rejected.
- Scope-restricted map layers show only permitted properties.

### Validations
- Lat/long numeric ranges
- Permission to edit geo

### Calculations
None.

### Workflow
N/A (or follow property edit approval if geo classed as material change — configurable off by default).

### Search Requirements
Optional “has geo / missing geo” filter on inventory search.

### Documents
None.

### Reports
Properties missing geo-tag report (simple list export).

### Notifications
None mandatory.

### Security
RBAC; do not expose out-of-scope pins.

### Integrations
- GIS / Map Services — **Very High** (mandatory SOW integration). Connector shared with Module 10; consumption UX estimated here.

### Dependencies
F03-001; Module 10 GIS connector; map provider credentials via BDA.

### Assumptions
- One map provider (Google/MapmyIndia/other govt-approved) selected during implementation.
- GIS provider Very High integration hours are booked in **F10-005**. This feature retains Easy (8h) hub consumption plus map UX.
- Map UI = Very High (GIS).

### Risks
- Provider licensing/API limits.
- Reconciled: connector VH in F10-005; this feature is consumer UX + Easy integration.

### Non Functional Requirements
- Map usable on tablet for field updates
- Graceful degradation if map service unavailable (show lat/long fields)

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Map pin capture / view screen | UI | Very High | 16 |
| Geo coordinate save/retrieve | API | Medium | 6 |
| Geo fields on property | Database | Easy | 2 |
| Map service consumption (via Integration Hub) | Integration | Easy | 8 |
| Geo/map tests | Testing | Complex | 8 |
| Geo-tagging guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- GIS Integration = Easy (8h) consumption after reconciliation with F10-005.
- Map UI remains Very High (GIS/map UX).
