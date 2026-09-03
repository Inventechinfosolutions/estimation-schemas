# F04-005 — Nearby amenities, Map link and QR

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-005 |
| **Feature Name** | Nearby amenities, Map link and QR |
| **Module** | 04 — Valuer Assignment & GIS Field Capture (Data Capturing – I) |

### Description
When the Valuer is on the inspection page, the application fetches distances for that location to: school/college, hospital, malls, places of worship, police station, bus stand, railway station, airport, offices, markets, cinemas, auto/taxi and metro (Form V-1 items 10–11 plus Data Capturing – I). It shows a Map link, a QR code of that link, and a map marker (F02-008). The valuer can proceed only when those auto-fetched fields are populated or an authorised exception (fetch failed) is recorded.

### Business Objective
Auto-populate nearby amenity distances and provide Map link, QR and marker for the inspection report.

### Actors
Approved Valuer.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer is on the inspection page for the geocoded location.
3. How they edit: Application fetches distances to school/college, hospital, malls, places of worship, police station, bus stand, railway station, airport, offices, markets, cinemas, auto/taxi and metro.
4. How they send for approval: Page shows Map link, QR of that link, and map marker (F02-008). Open inspection → fetch amenities → show map/QR/marker → proceed or record exception.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record. Valuer proceeds only when auto-fetched fields are populated or an authorised fetch-failed exception is recorded.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Auto-fetch amenity distances including Form V-1 civic/transport rows
- Show Google Map link, QR of the link, and map marker
- Block proceed unless populated or authorised exception

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My nearby amenities, map link and qr list / queue | Medium |
| Amenities map and QR pack | Very High |
| Nearby amenities, map link and qr history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Amenity fetch and QR issue | Complex |
| Update nearby amenities, map link and qr | Medium |
| Search nearby amenities, map link and qr | Medium |
| Read nearby amenities, map link and qr history | Easy |

### Inputs
Asset/inspection location (F02-008); optional fetch-failed exception with reason.

### Outputs
Amenity distance set; Map link; QR; marker; exception record if used.

### Business Rules
- Distances are fetched automatically, not invented by generative AI
- Exception is explicit when fetch fails
- Depends on Authority-approved map/places capability at runtime

### Validations
- Location present
- All named amenity rows present or exception recorded

### Calculations
Distance from inspection location to each amenity as returned by the approved places capability (not a custom routing product).

### Workflow
Open inspection → fetch amenities → show map/QR/marker → proceed or record exception.

### Search Requirements
Asset; amenities complete yes/no; exception used.

### Documents
QR of the Map link stored with the inspection pack.

### Reports
Inspection amenity pack (feeds Form V-1).

### Notifications
In-app fetch failure.

### Security
Assigned valuer; map link does not publish the pack to the public website.

### Integrations
Map/places amenity fetch plus geocoding/map marker (GIS Very High), consuming F02-008 markers.

### Dependencies
F02-008; F04-004; Form V-1 (F05-007) consumes rows.

### Assumptions
- Authority-approved places/map capability is available; this is a known SOW dependency/risk.

### Risks
Places outage blocks proceed without exception process. Incorrect POI matching.

### Non Functional Requirements
Fetch on web; Android inspection uses the same rules (Module 09).

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My nearby amenities, map link and qr list / queue | UI | Medium | 6 |
| Amenities map and QR pack | UI | Very High | 16 |
| Nearby amenities, map link and qr history | UI | Medium | 6 |
| Amenity fetch and QR issue | API | Complex | 8 |
| Update nearby amenities, map link and qr | API | Medium | 6 |
| Search nearby amenities, map link and qr | API | Medium | 6 |
| Read nearby amenities, map link and qr history | API | Easy | 4 |
| Nearby amenities, map link and qr persistence | DB | Medium | 4 |
| Map/places and geocoding amenity fetch | Integration | Very High | 40 |
| Nearby amenities, Map link and QR feature tests | Testing | Very High | 12 |
| Nearby amenities, Map link and QR implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **112** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
