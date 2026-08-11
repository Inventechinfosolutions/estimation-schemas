# F04-003 — Check Bandi Capture

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-003 |
| Feature Name | Check Bandi Capture |
| Module | 04 — Field Site Visit Capture |
| Description | Capture Check Bandi date, number, acknowledgement (optional remarks) on the application. |
| Business Objective | Record Check Bandi as part of the CDR field visit. |
| Actors | Engineer |

### User Journey

- Engineer enters Check Bandi date → system number → optional remarks → acknowledges done at site.

### Functional Capabilities

- Check Bandi date
- System number / optional BDA ref
- Remarks
- Site acknowledgement

### Inputs

- Date
- Remarks
- Acknowledgement

### Outputs

- Check Bandi section on application

### Business Rules

- Acknowledgement mandatory at submit

### Validations

- Date required

### Calculations

- System-generated Check Bandi number

### Workflow

- Part of draft/submit

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Engineer

### Integrations

- None

### Dependencies

- F04-001

### Assumptions

- Check Bandi means site verification record

### Risks

- Missing acknowledgement blocks submit

### Non Functional Requirements

- Online capture

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Check Bandi mobile section | Easy | 4 |
| API | Save Check Bandi data | Easy | 4 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Easy | 4 |
| Documentation | Feature documentation | Simple | 1 |

**Feature Total: 15 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
