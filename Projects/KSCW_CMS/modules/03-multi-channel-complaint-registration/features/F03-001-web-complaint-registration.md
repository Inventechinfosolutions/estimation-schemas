# F03-001 — Web Complaint Registration

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-001 |
| Feature Name | Web Complaint Registration |
| Module | 03 — Multi-Channel Complaint Registration |
| Description | Capture complaints from citizens/users via the web channel into the unified complaint register. |
| Business Objective | Enable convenient digital intake without visiting office. |
| Actors | Complainant; Admin (oversight) |

### User Journey

- Complainant opens web form → enters complaint details and taxonomy/location → submits → receives acknowledgement reference.

### Functional Capabilities

- Web complaint intake form with master dropdowns
- Draft/save if FRS allows
- Submit into unified register

### Inputs

- Complainant details
- Complaint narrative
- Category/location fields
- Channel=Web

### Outputs

- Registered complaint
- Acknowledgement reference

### Business Rules

- Mandatory fields per FRS
- Channel stamped as Web

### Validations

- Mandatory fields
- Master value validity

### Calculations

- None

### Workflow

- Fill → validate → submit → ack (F03-005)

### Search Requirements

- Complainant may track by reference if FRS provides portal

### Documents

- Optional attachments via F03-006

### Reports

- None

### Notifications

- Acknowledgement via Module 06 when configured

### Security

- Abuse/rate controls per FRS; PII protection

### Integrations

- None direct

### Dependencies

- Modules 01–02
- F03-005
- F03-006

### Assumptions

- FRS/UI-UX locks field set

### Risks

- Spam/fake complaints without CAPTCHA/OTP if FRS omits

### Non Functional Requirements

- Responsive web; accessibility baseline

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Web complaint registration multi-section form | Very High | 16 |
| API | Web complaint create/submit with validation | Complex | 8 |
| Database | Complaint register write for web channel | Medium | 4 |
| Testing | Web intake and validation scenarios | Complex | 8 |
| Documentation | Web registration feature notes | Medium | 3 |

**Feature Total: 39 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
