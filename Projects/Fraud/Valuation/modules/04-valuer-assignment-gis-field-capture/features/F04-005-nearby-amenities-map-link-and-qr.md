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
1. Valuer is on the inspection page for the geocoded location.
2. Application fetches distances to school/college, hospital, malls, places of worship, police station, bus stand, railway station, airport, offices, markets, cinemas, auto/taxi and metro.
3. Page shows Map link, QR of that link, and map marker (F02-008).
4. Valuer proceeds only when auto-fetched fields are populated or an authorised fetch-failed exception is recorded.

### Functional Capabilities
- Auto-fetch amenity distances including Form V-1 civic/transport rows
- Show Google Map link, QR of the link, and map marker
- Block proceed unless populated or authorised exception

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
|---|---|---|---:|
| Amenities map and QR pack | UI | Very High | 16 |
| Amenity fetch and QR issue | API | Complex | 8 |
| Amenity distances and Map/QR store | Database | Medium | 4 |
| Map/places and geocoding amenity fetch | Integration | Very High | 40 |
| Amenity and QR tests | Testing | Very High | 12 |
| Amenities and Map/QR guide | Documentation | Complex | 4 |
| **Total** | | | **84** |

### Estimation Assumptions
- UI Very High 16 and Integration Very High 40 justified for GIS/map/places.
