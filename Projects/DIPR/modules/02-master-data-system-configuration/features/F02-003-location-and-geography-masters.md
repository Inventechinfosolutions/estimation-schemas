# F02-003 — Location & geography masters

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-003 |
| Feature Name | Location & geography masters |
| Module | 02 — Master Data & System Configuration |
| Description | Maintain districts and locations used for outdoor geotagging, PoD site association, and inventory filters. |
| Business Objective | Align field PoD and outdoor asset placement with DIPR’s administrative geography for compliance reporting. |
| Actors | DIPR Administrator; Campaign Officer (read) |

### User Journey

- Administrator maintains district hierarchy → adds outdoor sites/locations with optional boundary hints → field and asset modules pick locations from controlled lists → geotag validation (F04-003, F05-004) references same geography.

### Functional Capabilities

- District and sub-location hierarchy browser
- Location create/edit with code, name, district, optional GPS centroid or bounding hint
- Location list filters for outdoor campaign planning
- Deactivate location not deletable when tied to active PoD or assets

### Inputs

- District/location codes, names, parent district, optional coordinates, status

### Outputs

- Geography master used in geotag pickers and PoD batch association

### Business Rules

- PoD and outdoor assets should reference active locations where site-based tracking is required
- Location codes unique within district

### Validations

- Valid coordinate format when provided; mandatory district on child locations

### Calculations

- None

### Workflow

- Active location used in pickers; inactive hidden from new links

### Search Requirements

- Search by district, location name, code

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Administrator write; read for campaign and field roles

### Integrations

- None (no external GIS product)

### Dependencies

- Used by F04-003, F05-002, F05-006

### Assumptions

- DIPR provides authoritative district list; no full base-map GIS

### Risks

- Boundary data quality affects geotag validation false positives

### Non Functional Requirements

- Hierarchy navigation responsive for state-wide location counts

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | District hierarchy tree browser | Medium | 6 |
| UI | Assembly constituency list under district | Easy | 4 |
| UI | Outdoor site location create/edit form | Medium | 6 |
| UI | Latitude/longitude fields with validation hints | Easy | 4 |
| UI | Location list filter by district and site type | Easy | 4 |
| UI | Location map preview pin (read-only) | Medium | 6 |
| UI | Deactivate location confirmation dialog | Simple | 2 |
| API | Geography tree query (district → locations) | Medium | 6 |
| API | List locations with composite filters | Medium | 6 |
| API | Create location with hierarchy FK | Medium | 6 |
| API | Update location coordinates | Easy | 4 |
| API | Deactivate location with active PoD reference check | Medium | 6 |
| API | Location lookup by code for PoD capture | Easy | 4 |
| Database | District/constituency hierarchy storage | Medium | 4 |
| Database | Outdoor site location entity | Easy | 2 |
| Database | Geospatial index for proximity queries | Easy | 2 |
| Testing | Deactivate location referenced by active PoD | Easy | 4 |
| Testing | Invalid coordinate range validation | Easy | 4 |
| Testing | Hierarchy tree navigation and pagination | Easy | 4 |
| Documentation | Geography master seeding guide | Easy | 2 |
| Documentation | UAT district filter on campaign coverage | Simple | 1 |

**Feature Total: 87 hours**

### Estimation Assumptions

- Bulk GIS import from shapefiles is out of scope unless DIPR adds a data migration task.
