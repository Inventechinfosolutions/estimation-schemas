# F04-001 — Site Visit Application Create & Draft

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-001 |
| Feature Name | Site Visit Application Create & Draft |
| Module | 04 — Field Site Visit Capture |
| Description | Create and save draft CDR/site-visit applications on mobile within geo rules. |
| Business Objective | Allow engineers to start and pause capture before submit. |
| Actors | Engineer |

### User Journey

- Engineer creates application → system stamps engineer/geo → saves draft online.

### Functional Capabilities

- Create application
- Save draft
- Auto-stamp engineer and geo

### Inputs

- Application header fields

### Outputs

- Draft application number

### Business Rules

- Online only
- Geo rules apply

### Validations

- Mandatory header fields for draft as configured

### Calculations

- System-generated application number

### Workflow

- Create → Draft

### Search Requirements

- List own drafts

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Own applications only

### Integrations

- None

### Dependencies

- F03-002
- F03-004

### Assumptions

- Online connectivity

### Risks

- Lost connectivity mid-draft

### Non Functional Requirements

- Draft recoverable when online

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Create/draft application mobile screens | Medium | 6 |
| API | Create/update draft application | Medium | 6 |
| Database | Persistence / constraints for this feature | Medium | 4 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 24 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
