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
1. Valuer captures at least four photographs, each at least 5 MB, with GIS tag and the date printed on the photograph, and may upload video.
2. Each item stores captured date and time.
3. A submission with fewer than four qualifying photographs is rejected until the valuer adds them.

### Functional Capabilities
- Ingest minimum four photographs, each at least 5 MB
- Require GIS tag and date on the photograph
- Allow video upload with captured date/time
- Reject inspection submit until four qualifying photographs exist

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
|---|---|---|---:|
| GIS photo/video capture pack | UI | Very High | 16 |
| Media ingest with GIS/size/date rules | API | Very High | 16 |
| Media metadata store | Database | Medium | 4 |
| GIS photograph pipeline | Integration | Very High | 40 |
| GIS media tests | Testing | Very High | 12 |
| GIS photo/video field guide | Documentation | Complex | 4 |
| **Total** | | | **92** |

### Estimation Assumptions
- UI Very High 16 and Integration Very High 40 justified for GIS/photos. Device UX also in F09-003.
