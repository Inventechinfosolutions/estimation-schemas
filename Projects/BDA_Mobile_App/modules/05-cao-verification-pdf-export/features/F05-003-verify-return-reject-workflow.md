# F05-003 — Verify / Return / Reject Workflow

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-003 |
| Feature Name | Verify / Return / Reject Workflow |
| Module | 05 — CAO Verification & PDF Export |
| Description | Perform verification decisions with remarks and status update. |
| Business Objective | Complete CAO verification of CDR applications. |
| Actors | CAO; Engineer (on return) |

### User Journey

- CAO chooses Verify / Return / Reject → remarks mandatory on return/reject → status updates; return unlocks engineer edit.

### Functional Capabilities

- Verify
- Return with remarks
- Reject with remarks
- Record verifier and timestamp

### Inputs

- Decision
- Remarks

### Outputs

- Updated status

### Business Rules

- Remarks mandatory on return/reject
- Verified cannot be edited by engineer

### Validations

- Decision required

### Calculations

- None

### Workflow

- Submitted → Verified | Returned | Rejected

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- CAO only for decision

### Integrations

- None

### Dependencies

- F05-002

### Assumptions

- Labels finalized with BDA

### Risks

- Wrong reject hard to undo

### Non Functional Requirements

- Auditable decisions

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | CAO decision action panel | Complex | 8 |
| API | Apply verification decision workflow | Complex | 8 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 29 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
