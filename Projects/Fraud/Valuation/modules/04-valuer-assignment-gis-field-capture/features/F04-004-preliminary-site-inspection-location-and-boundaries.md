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
1. Who creates: Approved Valuer
2. How they create: Valuer on the assigned asset records or confirms asset no, address, width and type of approach road, landmark, surrounding area, and boundaries N/S/E/W.
3. How they edit: Save stores the Preliminary Site Inspection location pack with the valuer’s identity and time.
4. How they send for approval: Save stores the Preliminary Site Inspection location pack with the valuer’s identity and time. Open inspection → enter location/boundaries → save pack.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Capture/confirm location pack (asset no, address, road width/type, landmark, surrounding area)
- Capture/confirm boundaries N/S/E/W
- Stamp valuer Person and time on save

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My preliminary site inspection — location and boundaries list / queue | Medium |
| Preliminary site inspection pack | Complex |
| Preliminary site inspection — location and boundaries history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Inspection location-pack save | Medium |
| Update preliminary site inspection — location and boundaries | Medium |
| Search preliminary site inspection — location and boundaries | Medium |
| Read preliminary site inspection — location and boundaries history | Easy |

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
|---|---|---|---|
| My preliminary site inspection — location and boundaries list / queue | UI | Medium | 6 |
| Preliminary site inspection pack | UI | Complex | 12 |
| Preliminary site inspection — location and boundaries history | UI | Medium | 6 |
| Inspection location-pack save | API | Medium | 6 |
| Update preliminary site inspection — location and boundaries | API | Medium | 6 |
| Search preliminary site inspection — location and boundaries | API | Medium | 6 |
| Read preliminary site inspection — location and boundaries history | API | Easy | 4 |
| Preliminary site inspection — location and boundaries persistence | DB | Medium | 4 |
| Asset-basics consume | Integration | Simple | 4 |
| Preliminary site inspection — location and boundaries feature tests | Testing | Medium | 6 |
| Preliminary site inspection — location and boundaries implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
