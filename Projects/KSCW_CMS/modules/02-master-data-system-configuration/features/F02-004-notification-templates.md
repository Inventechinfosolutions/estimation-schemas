# F02-004 — Notification Templates

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-004 |
| Feature Name | Notification Templates |
| Module | 02 — Master Data & System Configuration |
| Description | Maintain SMS and Email notification templates and map them to complaint event triggers. |
| Business Objective | Standardize complainant and staff messaging language. |
| Actors | Admin |

### User Journey

- Admin edits SMS/Email template → maps placeholders and trigger event → activates template.

### Functional Capabilities

- Template create/edit for SMS and Email
- Trigger-event mapping
- Activate/deactivate templates

### Inputs

- Channel
- Subject (email)
- Body with placeholders
- Trigger event
- Status

### Outputs

- Active templates for Module 06 dispatch

### Business Rules

- Only one active template per event+channel unless FRS allows variants
- Placeholders limited to approved token list

### Validations

- Body required
- Valid trigger event

### Calculations

- None

### Workflow

- Edit template → map trigger → Module 06 uses at event

### Search Requirements

- By channel, event, status

### Documents

- None

### Reports

- None

### Notifications

- N/A (defines content for notifications)

### Security

- Admin only

### Integrations

- None

### Dependencies

- Module 01

### Assumptions

- Gateway credentials separate; templates only here

### Risks

- Unapproved content delays go-live messaging

### Non Functional Requirements

- Preview of rendered sample if FRS requires

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | SMS/Email template editor with placeholder tokens | Complex | 8 |
| API | Template CRUD and trigger mapping | Medium | 6 |
| Database | Template and trigger mapping store | Easy | 2 |
| Testing | Template CRUD and mapping cases | Medium | 6 |
| Documentation | Notification template admin notes | Easy | 2 |

**Feature Total: 24 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
