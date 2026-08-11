# F03-005 — Complaint Acknowledgement

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-005 |
| Feature Name | Complaint Acknowledgement |
| Module | 03 — Multi-Channel Complaint Registration |
| Description | Generate unique complaint reference and acknowledge complainant as configured. |
| Business Objective | Give complainants a trackable reference and confirmation of receipt. |
| Actors | System; Complainant; Operator |

### User Journey

- Complaint submitted on any channel → system allocates unique reference → displays/sends acknowledgement.

### Functional Capabilities

- Unique reference number generation
- On-screen acknowledgement
- Trigger notification event for Module 06

### Inputs

- Submitted complaint ID
- Complainant contact channels

### Outputs

- Unique reference
- Ack content

### Business Rules

- Reference unique system-wide
- Ack channel per configuration/templates

### Validations

- Complaint must be successfully registered

### Calculations

- Reference sequence/format per FRS

### Workflow

- Register → allocate reference → ack display/notify

### Search Requirements

- Lookup by reference

### Documents

- None

### Reports

- None

### Notifications

- SMS/Email ack via Module 06

### Security

- Reference not easily guessable if FRS requires

### Integrations

- Event publish to notification module

### Dependencies

- F03-001–F03-004
- Module 06
- F02-004

### Assumptions

- Reference format approved in FRS

### Risks

- Gateway delay affects perceived ack

### Non Functional Requirements

- Idempotent reference allocation

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Acknowledgement display / print-friendly view | Easy | 4 |
| API | Reference allocation and ack event publish | Medium | 6 |
| Database | Reference sequence and ack status fields | Easy | 2 |
| Testing | Uniqueness and multi-channel ack cases | Medium | 6 |
| Documentation | Acknowledgement behaviour notes | Easy | 2 |

**Feature Total: 20 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
