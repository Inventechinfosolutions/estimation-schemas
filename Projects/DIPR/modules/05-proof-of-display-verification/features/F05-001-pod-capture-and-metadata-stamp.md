# F05-001 — PoD capture & metadata stamp

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-001 |
| Feature Name | PoD capture & metadata stamp |
| Module | 05 — Proof-of-Display Capture & Verification |
| Description | Capture or upload image/video PoD with timestamp, GPS, and device metadata against campaign/site context. |
| Business Objective | Create tamper-evident field evidence that outdoor and other displays ran as contracted. |
| Actors | Field Personnel; Campaign Officer (web upload); PoD Verifier (read) |

### User Journey

- Field user or officer initiates PoD capture → selects campaign task/site → captures photo/video or uploads file → system extracts/stamps EXIF GPS and capture time plus device info → preview shows metadata stamp → submit queues for validation (F05-004) and verification (F05-003).

### Functional Capabilities

- Web PoD upload with campaign/site/task selection
- Display extracted timestamp, GPS, device/app identifier on preview
- Reject submit when mandatory metadata missing (per finalized rules)
- Link PoD to campaign package/asset version context when configured
- Store original file without lossy recompression for audit

### Inputs

- Media file, campaign/task/site references, optional caption

### Outputs

- PoD evidence record with metadata stamp block

### Business Rules

- GPS and timestamp requirements parameterized (F02-004, F05-004)
- PoD tied to approved campaign in schedule window (F03-007) unless override
- Gallery upload may be restricted for field roles per DIPR policy

### Validations

- File type and size; mandatory links to campaign and site when outdoor

### Calculations

- None at capture; distance checks in F05-004

### Workflow

- Capture → stamp → submit → validation → verification queue

### Search Requirements

- Find recent PoD by campaign and capture date on register (F05-006)

### Documents

- PoD media files

### Reports

- None directly

### Notifications

- Submit confirmation to field user (Module 08)

### Security

- Capture roles only; metadata visible to verifiers

### Integrations

- Mobile capture path primarily Module 06; web path here

### Dependencies

- F03-007 tasks; F02-003 sites; F05-004 rules

### Assumptions

- Device clock drift handled via server receive time as secondary signal

### Risks

- EXIF stripped photos from gallery break GPS rules

### Non Functional Requirements

- Upload tolerates moderate field bandwidth; progress indicator on web

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Single PoD capture form (photo + metadata) | Medium | 6 |
| UI | Camera EXIF auto-fill panel | Easy | 4 |
| UI | Campaign and outdoor site cascaded picker | Medium | 6 |
| UI | Capture timestamp and GPS stamp display | Easy | 4 |
| UI | Submit PoD confirmation summary | Simple | 2 |
| UI | PoD draft save for poor connectivity | Medium | 6 |
| API | Create PoD record with media attachment | Complex | 8 |
| API | Extract and validate EXIF/GPS metadata | Medium | 6 |
| API | Resolve campaign–site PoD linkage | Medium | 6 |
| API | Persist metadata stamp fields on evidence | Easy | 4 |
| Database | PoD evidence core entity | Medium | 4 |
| Database | Metadata stamp columns (GPS, time, device) | Easy | 2 |
| Testing | Happy path with valid EXIF/GPS | Medium | 6 |
| Testing | Missing GPS handling per validation rules | Medium | 6 |
| Testing | Wrong campaign–site linkage rejected | Easy | 4 |
| Documentation | PoD capture field guide for field staff | Easy | 2 |
| Documentation | UAT single PoD submission script | Easy | 2 |

**Feature Total: 78 hours**

### Estimation Assumptions

- Live camera capture UX on mobile estimated in F06; shared ingest API effort here.
