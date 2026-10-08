# F05-001 — Access Credential Generation

| Field | Value |
|-------|-------|
| Feature ID | F05-001 |
| Feature Name | Access Credential Generation |
| Module | 05 — Access Credentials & Guest Check-in |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Generates a QR code or unique booking identifier for each confirmed booking.

### Business Objective
Provide a unique, usable access credential tied to the confirmed stay.

### Actors
- System
- Employee Guest

### User Journey
1. System generates credential when booking is confirmed/allocated.
2. Credential displayed on confirmation and stored for check-in.
3. Regeneration via admin/support path invalidates prior active credential when policy requires.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Employee sees current credential on booking; history of regenerated ids if any.
8. Auditor sees credential issuance/regeneration log (not QR secret extras).

### Functional Capabilities
- Generate unique booking identifier
- Generate QR representation
- Regenerate with invalidation
- Bind credential to booking dates

### UI Screens
- Credential display on confirmation
- Regenerate credential admin dialog

### Logical API Operations
- Generate credential
- Regenerate credential
- Get active credential

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- One active credential per confirmed booking
- Unique identifier globally/booking-scoped per policy
- QR encodes identifier securely

### Validations
- Booking must be Confirmed/Allocated

### Calculations
- None beyond display counters

### Workflow
Confirmed → CredentialActive → Regenerated/Invalidated

### Search Requirements
Lookup booking by credential id for ops

### Documents
QR image artefact

### Reports
None

### Notifications
Triggers delivery feature

### Security
- Prevent credential enumeration
- Audit regenerations

### Integrations
None

### Dependencies
- F03-005

### Assumptions
- QR and/or code string both acceptable

### Risks
- Screenshot sharing of QR

### Non Functional Requirements
- Generation immediate on confirm

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Credential display on confirmation | Medium | 6 |
| UI | Regenerate credential admin dialog | Easy | 4 |
| API | Generate credential | Complex | 8 |
| API | Regenerate credential | Complex | 8 |
| API | Get active credential | Easy | 4 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 44 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: QR and/or code string both acceptable / Screenshot sharing of QR.
