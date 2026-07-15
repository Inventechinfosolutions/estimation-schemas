# F10-005 — GIS / Map Services Connector

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F10-005 |
| **Feature Name** | GIS / Map Services Connector |
| **Module** | 10 — API / Integration Hub |

### Description
GIS/map provider connector for tiles/JavaScript map SDK config, geocoding (optional), reverse geocode, and secure key proxying to support property geo-tagging and map views (Module 03).

### Business Objective
Enable authoritative map pin capture/display without embedding provider secrets in clients unsafely.

### Actors
- Tech admin, Module 03 property UI

### User Journey
1. Admin configures map provider keys/restrictions.
2. Module 03 map UI requests tiles/SDK token via hub patterns.
3. Optional geocode APIs resolve addresses to coordinates.

### Functional Capabilities
- Provider configuration (MapmyIndia/Google/other govt-approved)
- Key restriction / token proxy patterns
- Optional geocode & reverse geocode APIs
- Usage quota monitoring hooks
- Fallback / degraded mode signals

### Inputs
- Address query / lat-long / map session needs

### Outputs
- Map access tokens/config; geocode results

### Business Rules
- Map UX estimated in F03-005.
- **CRITICAL RECONCILE:** F03-005 currently includes Integration Very High (40h). At commercial roll-up, **deduct 40h from F03-005** (or reduce F03-005 Integration to Easy 8 consumption) so GIS Very High is counted **once** here.

### Validations
- Key present; referrer restrictions

### Calculations
None.

### Workflow
N/A.

### Search Requirements
N/A.

### Documents
Provider licensing notes.

### Reports
Quota usage extracts if API provides.

### Notifications
Quota near-limit alerts.

### Security
Do not expose unrestricted server keys to browsers; use proxy/restricted keys.

### Integrations
GIS/Map Services — **Very High (40)**.

### Dependencies
F10-001; Module 03 consumer

### Assumptions
- One map provider at go-live.
- Licensing/procurement outside engineering estimate.

### Risks
- Double-count with F03-005 if not reconciled.
- Provider ToS limits batch geocoding.

### Non Functional Requirements
- Map tile performance; graceful failure when provider down

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Map service config / key management UI | UI | Medium | 6 |
| Geocode/map tile/static map facades | API | Complex | 8 |
| Geo provider config entities | Database | Easy | 2 |
| GIS / Map Services integration | Integration | Very High | 40 |
| GIS connector tests | Testing | Very High | 12 |
| GIS connector guide | Documentation | Complex | 4 |
| **Total** | | | **72** |

### Estimation Assumptions
- Book full GIS VH here; adjust Module 03 at roll-up.
