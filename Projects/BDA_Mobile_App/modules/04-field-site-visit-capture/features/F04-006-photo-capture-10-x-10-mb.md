# F04-006 — Photo Capture (10 × 10 MB)

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-006 |
| Feature Name | Photo Capture (10 × 10 MB) |
| Module | 04 — Field Site Visit Capture |
| Description | Capture/upload up to 10 photographs with per-file max 10 MB enforcement. |
| Business Objective | Attach photographic evidence to the CDR application. |
| Actors | Engineer |

### User Journey

- Engineer captures/selects photos → size validated → preview/replace/delete before submit.

### Functional Capabilities

- Up to 10 photos
- Max 10 MB each
- Preview/replace/delete

### Inputs

- Image files

### Outputs

- Photos linked to application

### Business Rules

- Reject oversize
- Count ≤ parameter max

### Validations

- File type/size

### Calculations

- None

### Workflow

- Attach while draft

### Search Requirements

- None

### Documents

- Photos on application

### Reports

- None

### Notifications

- None

### Security

- Own application only

### Integrations

- Object/media storage

### Dependencies

- F04-001
- F02-004

### Assumptions

- Device camera available

### Risks

- Large uploads on poor network

### Non Functional Requirements

- Online upload required

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Photo capture/gallery mobile UI | Complex | 8 |
| API | Photo upload/replace/delete | Complex | 8 |
| Database | Persistence / constraints for this feature | Medium | 4 |
| Integration | External/internal integration for this feature | Easy | 8 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 39 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
