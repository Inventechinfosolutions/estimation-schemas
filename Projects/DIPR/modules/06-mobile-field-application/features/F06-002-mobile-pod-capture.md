# F06-002 — Mobile PoD capture

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-002 |
| Feature Name | Mobile PoD capture |
| Module | 06 — Mobile Field Application |
| Description | Capture PoD from mobile with GPS/timestamp/device metadata |
| Business Objective | Collect tamper-evident PoD evidence on site with location and device context. |
| Actors | Field Personnel; System |

### User Journey

- From an assigned task, field user launches PoD capture → captures photo (camera or gallery if allowed) → confirms GPS/timestamp → submits (online or queued offline).

### Functional Capabilities

- Camera and gallery capture per policy
- Auto-capture GPS coordinates, timestamp, and device identifier metadata
- Preview and retake before submit
- Associate capture with campaign, site, and task context

### Inputs

Image/media; GPS reading; device metadata; task/campaign context

### Outputs

PoD submission entering verification queue (Module 05)

### Business Rules

Gallery upload only when enabled in configuration
GPS required when policy mandates outdoor geotagged sites

### Validations

Minimum image quality/size checks
GPS accuracy threshold when required

### Calculations

- None

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

Device GPS and camera capabilities; PoD verification module

### Dependencies

F06-001; Module 05 PoD verification; F06-003 for offline queue

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | PoD capture launcher from task context | Simple | 2 |
| UI | Camera live preview with capture controls | Complex | 12 |
| UI | Gallery picker when policy enabled | Easy | 4 |
| UI | GPS/timestamp/device metadata read-only panel | Medium | 6 |
| UI | Image preview retake and quality warning dialog | Medium | 6 |
| UI | Submit confirmation with connectivity/queue status | Easy | 4 |
| API | Initiate mobile PoD capture session with context | Easy | 4 |
| API | Upload PoD media multipart with checksum | Complex | 8 |
| API | Attach GPS/timestamp/device attestation metadata | Medium | 6 |
| API | Finalize PoD submit to verification queue | Complex | 8 |
| Database | Mobile PoD staging record | Medium | 4 |
| Database | Capture metadata extension fields | Easy | 2 |
| Integration | Device GPS location service bridge | Simple | 4 |
| Integration | Device camera and gallery capability bridge | Easy | 8 |
| Testing | Happy path camera capture with GPS | Complex | 8 |
| Testing | Gallery disabled policy negative | Easy | 4 |
| Testing | GPS accuracy threshold failure | Medium | 6 |
| Testing | Media size/quality validation | Medium | 6 |
| Documentation | Mobile PoD field capture SOP | Medium | 3 |
| Documentation | Metadata attestation notes for verifiers | Easy | 2 |

**Feature Total: 107 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
