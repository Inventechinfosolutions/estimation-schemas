# F07-001 — Notification Template Catalogue

| Field | Value |
|-------|-------|
| Feature ID | F07-001 |
| Feature Name | Notification Template Catalogue |
| Module | 07 — Notification Service |
| Type | Technical |
| Notes | Go-live |

## Feature Specification

### Description
Administrator maintains SMS/email templates for OTP, booking confirmation, and access credentials.

### Business Objective
Standardise outbound message content with controllable templates.

### Actors
- Platform Administrator

### User Journey
1. Administrator creates/edits templates by event type and channel.
2. Sets subject/body with placeholders; activates template.
3. Edits create new effective version; prior retained.
4. Approval does not apply in Phase 1.
5. No approver inbox.
6. No approver decision.
7. Administrator sees template version history.
8. Auditor views template change history.

### Functional Capabilities
- CRUD templates
- Placeholders
- Activate/deactivate
- Version history
- Channel selection SMS/email

### UI Screens
- Template catalogue register
- Template editor form
- Template preview dialog
- Activate template confirmation

### Logical API Operations
- List templates
- Save template
- Activate template
- Preview template
- Get template versions

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- One active template per event+channel
- Placeholders validated

### Validations
- Body mandatory
- Known placeholder names only

### Calculations
- None beyond display counters

### Workflow
Draft → Active → Inactive

### Search Requirements
Filter by event/channel

### Documents
None

### Reports
None

### Notifications
N/A (defines notifications)

### Security
- Admin only
- Prevent script injection in templates

### Integrations
None

### Dependencies
- F01-004

### Assumptions
- SMS length constraints handled in preview

### Risks
- Wrong template active sends bad credentials text

### Non Functional Requirements
- Preview instant

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Template catalogue register | Medium | 6 |
| UI | Template editor form | Complex | 12 |
| UI | Template preview dialog | Easy | 4 |
| UI | Activate template confirmation | Simple | 2 |
| API | List templates | Easy | 4 |
| API | Save template | Medium | 6 |
| API | Activate template | Easy | 4 |
| API | Preview template | Easy | 4 |
| API | Get template versions | Easy | 4 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 56 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: SMS length constraints handled in preview / Wrong template active sends bad credentials text.
