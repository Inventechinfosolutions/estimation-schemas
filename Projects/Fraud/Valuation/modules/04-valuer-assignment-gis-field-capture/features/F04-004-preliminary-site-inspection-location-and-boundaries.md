# F04-004 — Preliminary site inspection — location and boundaries

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-004 |
| **Feature Name** | Preliminary site inspection — location and boundaries |
| **Module** | 04 — Valuer Assignment & GIS Field Capture (Data Capturing – I) |

### Description
The Valuer records or confirms location of asset (asset no, address, width and type of approach road, landmark, surrounding area) and boundaries North, South, East and West. Saving stores this as the Preliminary Site Inspection location pack with the valuer’s identity and time.

### Business Objective
Complete Data Capturing – I location and boundary particulars for the Preliminary Site Inspection Report.

### Actors
Approved Valuer.

### User Journey
1. Valuer on the assigned asset records or confirms asset no, address, width and type of approach road, landmark, surrounding area, and boundaries N/S/E/W.
2. Save stores the Preliminary Site Inspection location pack with the valuer’s identity and time.

### Functional Capabilities
- Capture/confirm location pack (asset no, address, road width/type, landmark, surrounding area)
- Capture/confirm boundaries N/S/E/W
- Stamp valuer Person and time on save

### Inputs
Asset no; address; width of approach road; type of road; landmark; surrounding area; boundaries N/S/E/W.

### Outputs
Preliminary site inspection location pack.

### Business Rules
- Office address may be confirmed, not blanked as a new invented asset
- Pack is attributable to the valuer Person

### Validations
- Assigned asset
- Mandatory location pack fields as in Data Capturing – I

### Calculations
None.

### Workflow
Open inspection → enter location/boundaries → save pack.

### Search Requirements
Asset, visit (via F04-008), inspection saved yes/no.

### Documents
Inspection pack (structured fields).

### Reports
Preliminary Site Inspection location extract.

### Notifications
None.

### Security
Assigned valuer only.

### Integrations
Internal asset basics consume.

### Dependencies
F04-002; F04-008.

### Assumptions
- Amenities/map/QR are F04-005; photos are F04-006.

### Risks
Boundaries as inspected may differ from deed boundaries (F03-002); both must remain distinguishable.

### Non Functional Requirements
Save stamps system date/time.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Preliminary site inspection pack | UI | Complex | 12 |
| Inspection location-pack save | API | Medium | 6 |
| Inspection location fields | Database | Medium | 4 |
| Asset-basics consume | Integration | Simple | 4 |
| Inspection location tests | Testing | Medium | 6 |
| Preliminary inspection guide | Documentation | Medium | 3 |
| **Total** | | | **35** |

### Estimation Assumptions
- Named screen is the Preliminary site inspection pack (location/boundaries).
