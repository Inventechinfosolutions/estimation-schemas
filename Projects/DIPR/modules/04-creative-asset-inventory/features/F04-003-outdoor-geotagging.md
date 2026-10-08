# F04-003 — Outdoor geotagging

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-003 |
| Feature Name | Outdoor geotagging |
| Module | 04 — Creative Asset Inventory |
| Description | Capture and display geotags for outdoor assets and sites linked to geography masters. |
| Business Objective | Tie outdoor creative placement to map coordinates and district locations for PoD validation and compliance maps. |
| Actors | Asset Manager; Campaign Officer; Field Personnel (read on mobile via Module 06) |

### User Journey

- Manager opens outdoor asset → Geotag tab → picks location from master or places pin on map → saves coordinates → map thumbnail on asset detail → PoD validation compares capture GPS to site geotag tolerance (F05-004).

### Functional Capabilities

- Map picker for latitude/longitude with district context
- Manual coordinate entry fallback when map unavailable
- Link geotag to F02-003 location/site record
- Map preview on asset detail and inventory list indicator
- Validate coordinates fall within district tolerance when configured

### Inputs

- Latitude, longitude, location master reference, accuracy notes

### Outputs

- Geotag fields on asset/site; map display data

### Business Rules

- Geotag required for outdoor channel assets marked site-specific
- Coordinates immutable after PoD verified against site unless admin override with audit

### Validations

- Coordinate range checks; location district consistency

### Calculations

- Distance check helper for PoD rules (shared logic with F05-004)

### Workflow

- Add geotag at upload or edit → used in PoD and search filters

### Search Requirements

- Filter inventory by district and geotagged-only

### Documents

- None

### Reports

- Outdoor site map exports via Module 07 (read geotag data)

### Notifications

- None

### Security

- Geotag edit requires asset update; precise coordinates may be restricted for vendor roles

### Integrations

- None (embedded map tiles assumed via platform config, not full GIS product)

### Dependencies

- F02-003; F04-001; F05-004 validation

### Assumptions

- Map provider and tile usage comply with government hosting policy

### Risks

- GPS inaccuracy in hilly districts drives false PoD failures without tuned thresholds

### Non Functional Requirements

- Map interaction usable on standard DIPR desktops; mobile read in Module 06

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Outdoor geotag map picker (site pin drop) | Very High | 16 |
| UI | Manual latitude/longitude fallback form | Medium | 6 |
| UI | District boundary overlay toggle on map | Medium | 6 |
| UI | Geotag accuracy radius slider | Easy | 4 |
| UI | Geotag summary card on asset detail | Easy | 4 |
| UI | Immutable geotag lock indicator after PoD | Simple | 2 |
| API | Save geotag coordinates on outdoor asset | Medium | 6 |
| API | Validate coordinates against district master | Medium | 6 |
| API | Assist reverse geocode for pin placement | Easy | 4 |
| API | Enforce geotag immutability after PoD link | Medium | 6 |
| Integration | Base map tile / GIS provider hook | Easy | 8 |
| Database | Geotag columns on outdoor asset | Easy | 2 |
| Database | District FK validation constraint | Easy | 2 |
| Testing | District mismatch rejection | Medium | 6 |
| Testing | Immutability after PoD submission | Medium | 6 |
| Testing | Map picker pin drag accuracy | Easy | 4 |
| Documentation | Outdoor geotag capture guidelines | Easy | 2 |
| Documentation | UAT outdoor site pin placement script | Easy | 2 |

**Feature Total: 92 hours**

### Estimation Assumptions

- No offline map caching in web; mobile offline maps in Module 06 if required.
