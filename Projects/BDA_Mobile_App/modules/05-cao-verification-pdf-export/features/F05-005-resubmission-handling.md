# F05-005 — Resubmission Handling

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-005 |
| Feature Name | Resubmission Handling |
| Module | 05 — CAO Verification & PDF Export |
| Description | Allow returned applications to be corrected by engineer and resubmitted. |
| Business Objective | Close the loop when CAO returns a CDR for correction. |
| Actors | Engineer; CAO |

### User Journey

- Returned application editable by owner → engineer corrects → resubmits → returns to CAO queue as Submitted.

### Functional Capabilities

- Unlock edit on Returned
- Resubmit to CAO
- Preserve history

### Inputs

- Corrected application

### Outputs

- Resubmitted Submitted status

### Business Rules

- Only owner engineer edits returned
- Geo rules still apply

### Validations

- Same submit validations

### Calculations

- None

### Workflow

- Returned → Draft-like edit → Submitted

### Search Requirements

- Engineer sees Returned

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Owner + CAO visibility

### Integrations

- None

### Dependencies

- F05-003
- F04-008

### Assumptions

- Remarks guide correction

### Risks

- Repeated returns delay closure

### Non Functional Requirements

- History retained

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Returned application edit/resubmit mobile flow | Medium | 6 |
| API | Resubmit returned application | Medium | 6 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 22 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
