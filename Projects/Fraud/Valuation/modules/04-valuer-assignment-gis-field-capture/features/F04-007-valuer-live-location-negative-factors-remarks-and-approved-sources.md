# F04-007 — Valuer live location, negative factors, remarks and approved sources

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-007 |
| **Feature Name** | Valuer live location, negative factors, remarks and approved sources |
| **Module** | 04 — Valuer Assignment & GIS Field Capture (Data Capturing – I) |

### Description
While inspecting, the application captures the valuer’s real-time GIS with system date and time and reverse-geocodes it to a readable address stored beside the coordinates (F02-008). The Valuer enters negative factors affecting the property and overall observation. The Valuer may retrieve remaining particulars from approved secure sources named by the Authority; the system records which source was used. Generative AI shall not invent site remarks.

### Business Objective
Bind the inspection to the valuer’s live location and human-entered remarks, with an audit of approved sources.

### Actors
Approved Valuer.

### User Journey
1. While inspecting, the application captures the valuer’s real-time GIS with system date and time and reverse-geocodes it to a readable address (F02-008).
2. Valuer enters negative factors affecting the property and overall observation.
3. Valuer may retrieve remaining particulars from approved secure sources named by the Authority; the system records which source was used.
4. Generative AI is not offered to invent site remarks.

### Functional Capabilities
- Capture valuer real-time GIS with system date/time and reverse-geocoded address
- Capture negative factors and overall observation
- Record approved secure source used for remaining particulars
- Prohibit generative AI for remarks

### Inputs
Device/web live coordinates; negative factors; overall observation; selected approved source.

### Outputs
Live location + readable address; remarks; source-used log.

### Business Rules
- Remarks are entered by the valuer, not generated
- Approved sources are a named list from the Authority
- Reverse geocode consumes F02-008

### Validations
- Live GIS captured with system date/time
- Source id is on the approved list when retrieval is used

### Calculations
None.

### Workflow
Capture live GIS → reverse geocode → enter remarks → optional approved-source retrieve with log.

### Search Requirements
Asset, capture time, source used.

### Documents
None.

### Reports
Live-location and source-use extract.

### Notifications
In-app if live GIS or reverse geocode fails.

### Security
Location retained with the inspection pack; source access per Authority list.

### Integrations
Reverse geocoding consume from F02-008; optional approved-source retrieve (mapping and retry).

### Dependencies
F02-008; F09-003; Authority named source list.

### Assumptions
- SPLOCA supplies the named list of approved secure sources.

### Risks
Poor GPS; unapproved source use; attempts to add generative drafting.

### Non Functional Requirements
No generative AI; live GIS stored with system date/time.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Live GIS and remarks pack | UI | Very High | 16 |
| Live location and approved-source log | API | Complex | 8 |
| Live location and remarks store | Database | Medium | 4 |
| Reverse-geocode consume and source retrieve | Integration | Medium | 16 |
| Live location and remarks tests | Testing | Complex | 8 |
| Live location and sources guide | Documentation | Medium | 3 |
| **Total** | | | **55** |

### Estimation Assumptions
- Geocoding service hours remain in F02-008; this feature consumes reverse geocode (Integration Medium 16) with GIS UI Very High 16.
