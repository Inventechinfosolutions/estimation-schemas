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
1. Who creates: Approved Valuer
2. How they create: While inspecting, the application captures the valuer’s real-time GIS with system date and time and reverse-geocodes it to a readable address (F02-008).
3. How they edit: Valuer enters negative factors affecting the property and overall observation.
4. How they send for approval: Valuer may retrieve remaining particulars from approved secure sources named by the Authority; the system records which source was used. Capture live GIS → reverse geocode → enter remarks → optional approved-source retrieve with log.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record. Generative AI is not offered to invent site remarks.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Capture valuer real-time GIS with system date/time and reverse-geocoded address
- Capture negative factors and overall observation
- Record approved secure source used for remaining particulars
- Prohibit generative AI for remarks

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My valuer live location, negative factors, remarks and approved sources list / queue | Medium |
| Live GIS and remarks pack | Very High |
| Valuer live location, negative factors, remarks and approved sources history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Live location and approved-source log | Complex |
| Update valuer live location, negative factors, remarks and approved sources | Medium |
| Search valuer live location, negative factors, remarks and approved sources | Medium |
| Read valuer live location, negative factors, remarks and approved sources history | Easy |

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
|---|---|---|---|
| My valuer live location, negative factors, remarks and approved sources list / queue | UI | Medium | 6 |
| Live GIS and remarks pack | UI | Very High | 16 |
| Valuer live location, negative factors, remarks and approved sources history | UI | Medium | 6 |
| Live location and approved-source log | API | Complex | 8 |
| Update valuer live location, negative factors, remarks and approved sources | API | Medium | 6 |
| Search valuer live location, negative factors, remarks and approved sources | API | Medium | 6 |
| Read valuer live location, negative factors, remarks and approved sources history | API | Easy | 4 |
| Valuer live location, negative factors, remarks and approved sources persistence | DB | Medium | 4 |
| Reverse-geocode consume and source retrieve | Integration | Medium | 16 |
| Valuer live location, negative factors, remarks and approved sources feature tests | Testing | Complex | 8 |
| Valuer live location, negative factors, remarks and approved sources implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **83** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
