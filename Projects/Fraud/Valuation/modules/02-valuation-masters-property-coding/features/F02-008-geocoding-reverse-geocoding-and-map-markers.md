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
1. Office user entering an asset address (F03-001) obtains latitude/longitude or a Place ID and sees a marker on the map.
2. Valuer capturing live GIS (F04-007 / F09-003) obtains a human-readable address stored beside those coordinates.
3. The same behaviour is available on web and Android.

### Functional Capabilities
- Convert address to coordinates / Place ID for map markers
- Reverse geocode coordinates / Place ID to a readable address
- Show map markers on host PC web and Android
- Support unique property-code bind (F02-003) and amenity/map pack (F04-005)

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
|---|---|---|---:|
| Geocoding map-marker workspace | UI | Very High | 16 |
| Geocode and reverse-geocode operations | API | Very High | 16 |
| Coordinate / Place ID / address store | Database | Medium | 4 |
| Secure geocoding and map-marker service | Integration | Very High | 40 |
| Geocoding and marker tests | Testing | Very High | 12 |
| Geocoding operations guide | Documentation | Complex | 4 |
| **Total** | | | **92** |

### Estimation Assumptions
- UI Very High 16 and Integration Very High 40 are justified for GIS/geocoding
- Amenity distances and QR are F04-005; unique code issue is F02-003
