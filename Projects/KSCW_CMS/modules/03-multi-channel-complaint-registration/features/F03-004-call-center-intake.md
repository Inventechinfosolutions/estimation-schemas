# F03-004 — Call-Center Intake

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-004 |
| Feature Name | Call-Center Intake |
| Module | 03 — Multi-Channel Complaint Registration |
| Description | Allow Operators to register complaints received via call center into the unified register. |
| Business Objective | Support phone-channel complainants through assisted entry. |
| Actors | Operator; Supervisor |

### User Journey

- Operator takes call → opens call-center intake form → enters complainant and complaint data → submits → shares acknowledgement.

### Functional Capabilities

- Assisted complaint registration form
- Operator identity stamped on record
- Channel=Call Center

### Inputs

- Complainant contact
- Narrative
- Taxonomy/location
- Operator ID

### Outputs

- Registered complaint
- Ack reference for verbal/SMS share

### Business Rules

- Operator must be authenticated
- Mandatory fields per FRS

### Validations

- Contact and narrative required as FRS

### Calculations

- None

### Workflow

- Capture → submit → ack

### Search Requirements

- Operator search own recent intakes

### Documents

- Optional attachments

### Reports

- None

### Notifications

- Ack SMS/Email via Module 06

### Security

- Operator role only for this screen

### Integrations

- None (no CTI hardware in scope)

### Dependencies

- Modules 01–02
- F03-005

### Assumptions

- No telephony hardware integration in baseline

### Risks

- CTI integration requests expand scope

### Non Functional Requirements

- Fast form for live calls

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Call-center assisted registration form | Complex | 8 |
| API | Call-center complaint create API | Medium | 6 |
| Database | Complaint write with operator/channel stamp | Easy | 2 |
| Testing | Operator intake scenarios | Medium | 6 |
| Documentation | Call-center intake notes | Easy | 2 |

**Feature Total: 24 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
