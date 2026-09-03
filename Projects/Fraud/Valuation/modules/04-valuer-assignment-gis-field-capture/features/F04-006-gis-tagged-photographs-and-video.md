# F04-006 — GIS-tagged photographs and video

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-006 |
| **Feature Name** | GIS-tagged photographs and video |
| **Module** | 04 — Valuer Assignment & GIS Field Capture (Data Capturing – I) |

### Description
The Valuer captures at least four photographs, each at least 5 MB, with GIS tag and the date printed on the photograph, and may upload video. Each item stores captured date and time. A submission with fewer than four qualifying photographs is rejected until the valuer adds them.

### Business Objective
Store field-truth photographs and optional video that meet SPLOCA GIS, size and date-on-photo rules.

### Actors
Approved Valuer.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer captures at least four photographs, each at least 5 MB, with GIS tag and the date printed on the photograph, and may upload video.
3. How they edit: Each item stores captured date and time.
4. How they send for approval: A submission with fewer than four qualifying photographs is rejected until the valuer adds them. Capture/upload → validate GIS/size/date → store; submit blocked if < 4 qualifying.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Ingest minimum four photographs, each at least 5 MB
- Require GIS tag and date on the photograph
- Allow video upload with captured date/time
- Reject inspection submit until four qualifying photographs exist

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My gis-tagged photographs and video list / queue | Medium |
| GIS photo/video capture pack | Very High |
| Gis-tagged photographs and video history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Media ingest with GIS/size/date rules | Very High |
| Update gis-tagged photographs and video | Medium |
| Search gis-tagged photographs and video | Medium |
| Read gis-tagged photographs and video history | Easy |

### Inputs
Photographs; optional video; device/web capture metadata.

### Outputs
Qualifying media set on the inspection pack; reject reason if short.

### Business Rules
- Minimum four photographs, each at least 5 MB, GIS-tagged, date on photo
- Generative AI shall not invent photographs
- Android capture behaviour is also F09-003; this feature is the inspection media rule and web-side store

### Validations
- Count ≥ 4
- Each photo ≥ 5 MB
- GIS tag present
- Date on photo present
- Captured date/time stored

### Calculations
Count of qualifying photographs; per-file size check.

### Workflow
Capture/upload → validate GIS/size/date → store; submit blocked if < 4 qualifying.

### Search Requirements
Asset, media count, captured date.

### Documents
Photographs; video.

### Reports
Inspection media completeness.

### Notifications
In-app reject until four qualifying photos.

### Security
Need-to-know (F01-003); media retained with the inspection pack.

### Integrations
GIS photo pipeline (geotag, date-on-photo, size) — GIS/photos Very High.

### Dependencies
F02-008; F09-003; F05-009 tagging; F07-003 picker.

### Assumptions
- Date printed on the photograph is produced at capture (device overlay or equivalent), not only EXIF in a sidecar.

### Risks
Device cameras producing files under 5 MB; missing GIS in poor signal.

### Non Functional Requirements
Retain GIS photographs with the pack; HTTPS; AES-256 as programme NFR.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My gis-tagged photographs and video list / queue | UI | Medium | 6 |
| GIS photo/video capture pack | UI | Very High | 16 |
| Gis-tagged photographs and video history | UI | Medium | 6 |
| Media ingest with GIS/size/date rules | API | Very High | 16 |
| Update gis-tagged photographs and video | API | Medium | 6 |
| Search gis-tagged photographs and video | API | Medium | 6 |
| Read gis-tagged photographs and video history | API | Easy | 4 |
| Gis-tagged photographs and video persistence | DB | Medium | 4 |
| GIS photograph pipeline | Integration | Very High | 40 |
| GIS-tagged photographs and video feature tests | Testing | Very High | 12 |
| GIS-tagged photographs and video implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **120** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
