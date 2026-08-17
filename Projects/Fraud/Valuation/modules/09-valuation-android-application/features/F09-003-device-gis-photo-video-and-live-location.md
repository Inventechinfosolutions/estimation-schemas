# F09-003 — Device GIS photo, video and live location

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-003 |
| **Feature Name** | Device GIS photo, video and live location |
| **Module** | 09 — Valuation Android Application (Approved Valuers) |

### Description
On site the Valuer captures the Module 04 media set (minimum four photographs, each at least 5 MB, GIS tag, date on photo, video, captured date/time) and the valuer’s real-time location with system date and time, using the device. The live GIS is reverse-geocoded to a readable address (F02-008 / F04-007). Submission without that set is refused.

### Business Objective
Perform GIS field capture on the official Android app to the same evidence rules as Data Capturing – I.

### Actors
Approved Valuer.

### User Journey
1. On site the Valuer captures at least four photographs, each at least 5 MB, with GIS tag and date on the photograph, optional video, captured date/time, and live location with system date/time.
2. Live GIS is reverse-geocoded to a readable address (F02-008 / F04-007).
3. Submission without that set is refused (F09-005).

### Functional Capabilities
- Device capture of qualifying GIS photographs and video
- Date printed on the photograph
- Live location with reverse-geocoded address
- Refuse submit without the set

### Inputs
Device camera/GPS; optional video.

### Outputs
Inspection media and live location on the field package.

### Business Rules
- Minimum four photographs, each at least 5 MB, GIS-tagged, date on photo
- Generative AI shall not invent media
- Same business rules as F04-006 / F04-007 on device

### Validations
- Count, size, GIS tag, date on photo, live GIS + reverse address

### Calculations
Qualifying photo count and size checks.

### Workflow
Capture media and live GIS → reverse geocode → store on draft package → submit gated.

### Search Requirements
On-device draft completeness.

### Documents
Photographs; video.

### Reports
None on device (web MIS is Module 07).

### Notifications
In-app refuse if set incomplete.

### Security
Media stored for official use; need-to-know after sync.

### Integrations
Device GIS/camera/location plus geocoding/reverse geocoding (GIS Very High).

### Dependencies
F02-008; F04-006; F04-007; F09-005.

### Assumptions
- Device supports overlay date-on-photo and geotag; Authority-approved geocoding available on Android (FRS).

### Risks
Low GPS; files under 5 MB; overlay failure.

### Non Functional Requirements
Captured date/time stored; HTTPS on sync.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Device GIS capture | UI | Very High | 16 |
| Device media and location ingest | API | Very High | 16 |
| Device media queue | Database | Medium | 4 |
| Android GIS/camera/location pipeline | Integration | Very High | 40 |
| Device GIS capture tests | Testing | Very High | 12 |
| Android GIS field guide | Documentation | Complex | 4 |
| **Total** | | | **92** |

### Estimation Assumptions
- UI Very High 16 and Integration Very High 40 justified for Android GIS/photos.
