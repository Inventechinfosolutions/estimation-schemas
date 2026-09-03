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
1. Who creates: Office user
2. How they create: Officer saves a new seized property with location (F03-001, geocoding F02-008).
3. How they edit: System issues a unique property code bound to that Google location.
4. How they send for approval: Later search by that code opens the same asset. Save new property → require location bind → issue code → searchable.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record. FE number/type/tri-lateral index is not generated here.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Issue unique seized-property code on first save
- Bind the code to the property’s Google location
- Search by that code
- Leave FE unique coding in the existing FE application

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Property-code issue confirmation | Simple |
| Search by seized-property code | Easy |
| Unique seized-property code with google location history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Unique code generator and bind | Complex |
| Update unique seized-property code with google location | Medium |
| Search unique seized-property code with google location | Medium |
| Read unique seized-property code with google location history | Easy |

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
|---|---|---|---|
| Property-code issue confirmation | UI | Simple | 2 |
| Search by seized-property code | UI | Easy | 4 |
| Unique seized-property code with google location history | UI | Medium | 6 |
| Unique code generator and bind | API | Complex | 8 |
| Update unique seized-property code with google location | API | Medium | 6 |
| Search unique seized-property code with google location | API | Medium | 6 |
| Read unique seized-property code with google location history | API | Easy | 4 |
| Unique seized-property code with google location persistence | DB | Medium | 4 |
| Geocoded-location bind consume | Integration | Easy | 8 |
| Unique seized-property code with Google location feature tests | Testing | Medium | 6 |
| Unique seized-property code with Google location implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **56** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
