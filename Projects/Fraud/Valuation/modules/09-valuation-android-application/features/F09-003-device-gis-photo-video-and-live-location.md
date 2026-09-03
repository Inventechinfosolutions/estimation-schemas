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
1. Who creates: Approved Valuer
2. How they create: On site the Valuer captures at least four photographs, each at least 5 MB, with GIS tag and date on the photograph, optional video, captured date/time, and live location with system date/time.
3. How they edit: Live GIS is reverse-geocoded to a readable address (F02-008 / F04-007).
4. How they send for approval: Submission without that set is refused (F09-005). Capture media and live GIS → reverse geocode → store on draft package → submit gated.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Device capture of qualifying GIS photographs and video
- Date printed on the photograph
- Live location with reverse-geocoded address
- Refuse submit without the set

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My device gis photo, video and live location list / queue | Medium |
| Device GIS capture | Very High |
| Device gis photo, video and live location history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Device media and location ingest | Very High |
| Update device gis photo, video and live location | Medium |
| Search device gis photo, video and live location | Medium |
| Read device gis photo, video and live location history | Easy |

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
|---|---|---|---|
| My device gis photo, video and live location list / queue | UI | Medium | 6 |
| Device GIS capture | UI | Very High | 16 |
| Device gis photo, video and live location history | UI | Medium | 6 |
| Device media and location ingest | API | Very High | 16 |
| Update device gis photo, video and live location | API | Medium | 6 |
| Search device gis photo, video and live location | API | Medium | 6 |
| Read device gis photo, video and live location history | API | Easy | 4 |
| Device gis photo, video and live location persistence | DB | Medium | 4 |
| Android GIS/camera/location pipeline | Integration | Very High | 40 |
| Device GIS photo, video and live location feature tests | Testing | Very High | 12 |
| Device GIS photo, video and live location implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **120** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
