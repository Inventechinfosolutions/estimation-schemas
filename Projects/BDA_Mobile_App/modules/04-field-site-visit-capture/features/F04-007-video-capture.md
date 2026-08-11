# F04-007 — Video Capture

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-007 |
| Feature Name | Video Capture |
| Module | 04 — Field Site Visit Capture |
| Description | Capture/upload one video per application within configured max size. |
| Business Objective | Attach a site video to the CDR application. |
| Actors | Engineer |

### User Journey

- Engineer records/selects one video → size validated → preview/replace/delete.

### Functional Capabilities

- One video per application
- Max size from parameters
- Preview/replace/delete

### Inputs

- Video file

### Outputs

- Video linked to application

### Business Rules

- Single video only
- Reject oversize

### Validations

- File type/size

### Calculations

- None

### Workflow

- Attach while draft

### Search Requirements

- None

### Documents

- Video on application

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

- Default max 50 MB unless changed

### Risks

- Upload failures on weak network

### Non Functional Requirements

- Online upload

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Video capture mobile UI | Complex | 8 |
| API | Video upload/replace/delete | Complex | 8 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Integration | External/internal integration for this feature | Easy | 8 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 36 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
