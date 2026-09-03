# F02-008 — Geocoding, reverse geocoding and map markers

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-008 |
| **Feature Name** | Geocoding, reverse geocoding and map markers |
| **Module** | 02 — Valuation Masters, Property Coding & References |

### Description
An Office user entering an asset address (F03-001) obtains latitude/longitude or a Place ID and sees a marker on the map. A Valuer capturing live GIS (F04-007) obtains a human-readable address stored beside those coordinates. The same behaviour is available on web and Android. This SOW does not specify interface contracts.

### Business Objective
Provide secure geocoding and reverse geocoding with map markers as a named business capability for office create and field capture.

### Actors
Office user; Approved Valuer.

### User Journey
1. Who creates: Office user
2. How they create: Office user entering an asset address (F03-001) obtains latitude/longitude or a Place ID and sees a marker on the map.
3. How they edit: Valuer capturing live GIS (F04-007 / F09-003) obtains a human-readable address stored beside those coordinates.
4. How they send for approval: The same behaviour is available on web and Android. Enter address or capture coordinates → geocode or reverse geocode → store pair + marker.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Convert address to coordinates / Place ID for map markers
- Reverse geocode coordinates / Place ID to a readable address
- Show map markers on host PC web and Android
- Support unique property-code bind (F02-003) and amenity/map pack (F04-005)

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My geocoding, reverse geocoding and map markers list / queue | Medium |
| Geocoding map-marker workspace | Very High |
| Geocoding, reverse geocoding and map markers history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Geocode and reverse-geocode operations | Very High |
| Update geocoding, reverse geocoding and map markers | Medium |
| Search geocoding, reverse geocoding and map markers | Medium |
| Read geocoding, reverse geocoding and map markers history | Easy |

### Inputs
Address text; or coordinates / Place ID from map or device GPS.

### Outputs
Latitude/longitude or Place ID; readable address; map marker.

### Business Rules
- Geocoding is a named capability inside Module 02, not a standalone technical module
- Interface contracts are not specified in this SOW (FRS platform constraint: secure geocoding on host PC and Android)
- Generative AI shall not invent addresses

### Validations
- Address or coordinates present
- Returned marker is shown before save where the flow requires a bind

### Calculations
None (vendor geocoding service returns coordinates/address).

### Workflow
Enter address or capture coordinates → geocode or reverse geocode → store pair + marker.

### Search Requirements
Place ID, coordinates, readable address on the asset/inspection.

### Documents
None.

### Reports
Assets missing location bind.

### Notifications
In-app when geocoding fails so the user can retry or record authorised exception where a later feature allows it.

### Security
Approved/secure geocoding only; coordinates stored with the asset/inspection; HTTPS.

### Integrations
Secure geocoding / reverse geocoding / map-marker service on web and Android (GIS Very High).

### Dependencies
F03-001; F04-005; F04-007; F09-003 consume this capability.

### Assumptions
- Authority-approved map/geocoding capability is available at runtime
- This feature owns the geocoding service hours; consumers do not rebuild it

### Risks
Provider outage blocks address bind and live reverse geocode. Nearby amenity auto-fetch (F04-005) depends on an approved places capability.

### Non Functional Requirements
Available on web and Android; no unsupervised address invention; AES-256 in transit as programme NFR.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My geocoding, reverse geocoding and map markers list / queue | UI | Medium | 6 |
| Geocoding map-marker workspace | UI | Very High | 16 |
| Geocoding, reverse geocoding and map markers history | UI | Medium | 6 |
| Geocode and reverse-geocode operations | API | Very High | 16 |
| Update geocoding, reverse geocoding and map markers | API | Medium | 6 |
| Search geocoding, reverse geocoding and map markers | API | Medium | 6 |
| Read geocoding, reverse geocoding and map markers history | API | Easy | 4 |
| Geocoding, reverse geocoding and map markers persistence | DB | Medium | 4 |
| Secure geocoding and map-marker service | Integration | Very High | 40 |
| Geocoding, reverse geocoding and map markers feature tests | Testing | Very High | 12 |
| Geocoding, reverse geocoding and map markers implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **120** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
