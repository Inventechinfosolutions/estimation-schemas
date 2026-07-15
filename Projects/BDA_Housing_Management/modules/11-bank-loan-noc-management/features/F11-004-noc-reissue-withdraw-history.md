# F11-004 — NOC Reissue, Withdraw & History

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F11-004 |
| **Feature Name** | NOC Reissue, Withdraw & History |
| **Module** | 11 — Bank / Loan NOC Management |

### Description
Manage authorized NOC reissue and withdrawal actions while retaining a complete, chronological record of every request, decision, issue, and status change.
### Business Objective
Protect the legal and operational validity of issued NOCs while allowing controlled correction or withdrawal when required.
### Actors
- NOC Desk officer, authorized approver, Citizen, Auditor
### User Journey
1. Authorized officer locates an issued or active NOC case and selects reissue or withdrawal.
2. BHMS captures the reason and enforces configured authorization.
3. The action is recorded, affected document availability is updated, and permitted parties are notified.
### Functional Capabilities
- Reissue request and reason; withdrawal action; superseded-document marking; chronological case history; authorized audit view.
### Inputs
- NOC reference, requested action, reason, approver remarks where configured.
### Outputs
- Reissued NOC reference or withdrawn status, supersession indicator, and immutable history.
### Business Rules
- A withdrawn NOC cannot be downloaded as active.
- Reissue preserves the prior issuance record and identifies the current valid issued copy.
### Validations
- Eligible source status, authorized actor, mandatory reason, and configured approval requirement.
### Calculations
- Reissue and withdrawal counts.
### Workflow
- Issued → Reissue Requested → Reissued, or Issued → Withdrawal Requested → Withdrawn.
### Search Requirements
- Search/filter by original/current NOC number, action, reason, date, applicant, bank, and status.
### Documents
- Prior and current issued NOC copies, withdrawal evidence where supplied.
### Reports
- Reissue/withdrawal register and complete NOC case history.
### Notifications
- Reissue and withdrawal notifications through Module 12.
### Security
- Restricted corrective actions, citizen visibility limited to the current valid record, full audit trail.
### Integrations
- Internal document and notification capabilities.
### Dependencies
- Modules 01–02 and 12; F11-003.
### Assumptions
- BDA defines authorized roles and whether withdrawal requires an approval action.
### Risks
- Incorrect withdrawal can disrupt a valid citizen loan process; reason and audit controls are mandatory.
### Non Functional Requirements
- Accurate status propagation, immutable history, and prompt revocation of withdrawn-document access.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Reissue, withdrawal, and history workspace | UI | Complex | 8 |
| Reissue/withdrawal control operations | API | Complex | 8 |
| Version, supersession, and action history | Database | Medium | 4 |
| Reissue and withdrawal tests | Testing | Complex | 8 |
| Corrective-action guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- Reissue reuses the approved NOC template; a new request is required when underlying eligibility changes.
