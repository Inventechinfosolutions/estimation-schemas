# F02-003 — Unique seized-property code with Google location

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-003 |
| **Feature Name** | Unique seized-property code with Google location |
| **Module** | 02 — Valuation Masters, Property Coding & References |

### Description
When an Officer saves a new seized property, the system issues a unique property code bound to that property’s Google location. A later search by that code opens the same asset. This code is not the FE unique code (FE number, type, tri-lateral index), which stays in the existing FE application.

### Business Objective
Identify each seized property uniquely and bind the code to its Google location.

### Actors
Office user.

### User Journey
1. Officer saves a new seized property with location (F03-001, geocoding F02-008).
2. System issues a unique property code bound to that Google location.
3. Later search by that code opens the same asset.
4. FE number/type/tri-lateral index is not generated here.

### Functional Capabilities
- Issue unique seized-property code on first save
- Bind the code to the property’s Google location
- Search by that code
- Leave FE unique coding in the existing FE application

### Inputs
New asset save; geocoded location / Place ID from F02-008.

### Outputs
Unique property code; location binding; search hit.

### Business Rules
- Code is distinct from FE unique code
- Code is bound to Google location, not issued without a location bind
- Code does not change because an address label is reverse-geocoded later

### Validations
- Location/Place ID present
- Code unique across seized properties

### Calculations
Code issue per Authority numbering convention (format supplied by SPLOCA; not designed here).

### Workflow
Save new property → require location bind → issue code → searchable.

### Search Requirements
Unique property code; location label.

### Documents
None.

### Reports
Seized-property code register.

### Notifications
None.

### Security
Code issue attributable to the Office user Person.

### Integrations
Consume geocoded location from F02-008 (not a second geocoding product).

### Dependencies
F02-008; F03-001.

### Assumptions
- SPLOCA confirms code format; FE coding remains in the existing FE app.

### Risks
Saving without a stable Place ID would weaken the location bind.

### Non Functional Requirements
Uniqueness enforced; bind retained if the map marker is later adjusted with audit.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Property-code issue confirmation | UI | Simple | 2 |
| Search by seized-property code | UI | Easy | 4 |
| Unique code generator and bind | API | Complex | 8 |
| Code and location-bind store | Database | Easy | 2 |
| Geocoded-location bind consume | Integration | Easy | 8 |
| Unique-code tests | Testing | Medium | 6 |
| Seized-property code note | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- Full geocoding service hours are in F02-008, not duplicated here.
