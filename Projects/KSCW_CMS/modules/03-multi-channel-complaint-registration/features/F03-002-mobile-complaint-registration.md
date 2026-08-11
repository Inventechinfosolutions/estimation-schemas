# F03-002 — Mobile Complaint Registration

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-002 |
| Feature Name | Mobile Complaint Registration |
| Module | 03 — Multi-Channel Complaint Registration |
| Description | Capture complaints via mobile application into the same unified register. |
| Business Objective | Extend intake to mobile users. |
| Actors | Complainant; Operator (if assisted mobile per FRS) |

### User Journey

- User opens mobile app complaint flow → enters details → submits → sees acknowledgement.

### Functional Capabilities

- Mobile complaint intake screens
- Master lookups on mobile
- Submit to unified register

### Inputs

- Complainant details
- Complaint narrative
- Taxonomy/location
- Channel=Mobile

### Outputs

- Registered complaint
- Acknowledgement reference

### Business Rules

- Same core mandatory rules as web unless FRS differs
- Channel stamped Mobile

### Validations

- Mandatory fields
- Connectivity/error handling

### Calculations

- None

### Workflow

- Fill → validate → submit → ack

### Search Requirements

- Track by reference on mobile if provided

### Documents

- Attachments via F03-006

### Reports

- None

### Notifications

- Ack via Module 06 when configured

### Security

- Secure mobile session; PII protection

### Integrations

- None direct

### Dependencies

- Modules 01–02
- F01-003
- F03-005

### Assumptions

- Single mobile app scope per IFQ/FRS

### Risks

- Offline capture expansion not in baseline

### Non Functional Requirements

- Usable on common Android/iOS per FRS

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Mobile complaint intake screens and navigation | Very High | 16 |
| API | Mobile complaint create/submit endpoints | Complex | 8 |
| Database | Complaint register write for mobile channel | Easy | 2 |
| Testing | Mobile intake device/flow scenarios | Complex | 8 |
| Documentation | Mobile registration notes | Medium | 3 |

**Feature Total: 37 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
