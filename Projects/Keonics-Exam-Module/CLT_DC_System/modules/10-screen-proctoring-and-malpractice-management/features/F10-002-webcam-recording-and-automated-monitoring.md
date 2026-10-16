# F10-002 — Webcam Recording & Automated Monitoring

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-002 |
| Feature Name | Webcam Recording & Automated Monitoring |
| Module | 10 — Screen Proctoring & Malpractice Management |
| Module Type | Business |
| Release | Go-live |

### Description
Webcam capture during the test with low-bitrate recording and periodic frame analysis for no face, multiple faces, face mismatch against centre photo, gaze away, and phone detection, producing flags with confidence and snapshot evidence; models run server-side or on client per capacity.

### Business Objective
Provide automated webcam monitoring as required by the RFP.

### Actors
- System
- Proctor
- EMU

### User Journey
1. **Who creates:** Webcam capture starts with the test.
2. **How they create:** Frames are analysed and flags created.
3. **How they edit:** Flags can be dismissed or confirmed by proctor / EMU.
4. **How they send for approval:** Confirmed flags feed malpractice cases.
5. **How the approver sees pending items:** Proctor and EMU see flags in real time.
6. **How the approver decides:** They dismiss or confirm.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see flags and decisions.

### Functional Capabilities
- Webcam recording
- Face presence and count
- Face match with centre photo
- Gaze away detection
- Phone / object detection
- Confidence thresholds
- Snapshot evidence

### UI Screens
- Webcam flag viewer
- Threshold configuration

### Logical API Operations
- Webcam chunk upload
- Frame analysis pipeline
- Create flag with evidence
- Threshold configuration

### Inputs
- Webcam frames

### Outputs
- Flags

### Business Rules
- Flags are advisory until confirmed by a human

### Validations
- Confidence threshold

### Calculations
- Flag rate

### Workflow
Detected → Reviewed → Confirmed / Dismissed

### Search Requirements
- Flags by session

### Documents
- Snapshots

### Reports
- Flag statistics

### Notifications
- Real-time alerts (F10-004)

### Security
- Biometric-like data restricted

### Integrations
- Vision models

### Dependencies
- F09-007
- F10-004

### Assumptions
- Webcams at all terminals

### Risks
- False positives; compute capacity

### Non Functional Requirements
- Flag within 10 seconds of event

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Webcam flag viewer | Medium | 6 |
| UI | Threshold configuration | Easy | 4 |
| API | Webcam chunk upload | Medium | 6 |
| API | Frame analysis pipeline | Very High | 16 |
| API | Create flag with evidence | Medium | 6 |
| API | Threshold configuration | Easy | 4 |
| Database | Webcam flags and snapshots | Medium | 4 |
| Integration | Computer vision model integration | Complex | 24 |
| Testing | Detection accuracy tests | Complex | 8 |
| Testing | Load tests for analysis pipeline | Complex | 8 |
| Documentation | Automated monitoring note | Easy | 2 |

**Feature Total: 88 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 32 | 4 | 24 | 16 | 2 | **88** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Analysis pipeline rated Very High
