# F01-005 — Citizen Credential Linkage

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-005 |
| **Feature Name** | Citizen Credential Linkage |
| **Module** | 01 — User & Role Management |

### Description
Link a verified citizen identity from the portal to the shared access-control record without duplicating profile management.

### Business Objective
Give eligible citizens secure credentials while preserving a single identity linkage.

### Actors
Citizen; Super Administrator; Auditor (read-only).

### User Journey
After Module 06 verifies registration, the system links the citizen profile to a credential, enables or disables access as authorised, and retains linkage history.

### Functional Capabilities
Link/unlink credential; activation status; credential recovery handoff; linkage history; exception review.

### Inputs
Citizen reference, verified mobile status, credential status, administrator reason where applicable.

### Outputs
Citizen credential linkage record and status.

### Business Rules
Only OTP-verified citizen profiles may receive active linkage; a credential maps to one citizen; profile capture remains Module 06.

### Validations
Verified mobile required; one active linkage per citizen; inactive/duplicate credentials blocked.

### Calculations
None.

### Workflow
Module 06 verification completes → shared linkage is created or updated → access event is audited.

### Search Requirements
Citizen reference, mobile, linkage status, date range.

### Documents
None.

### Reports
Citizen Credential Linkage Register.

### Notifications
Credential activation/recovery notice via portal notification service.

### Security
Citizen ownership isolation; restricted administrative overrides; audit.

### Integrations
Citizen portal identity handoff (Simple).

### Dependencies
Module 06 citizen registration; F01-004.

### Assumptions
OTP delivery and citizen profile screens are estimated in Module 06.

### Risks
Unresolved duplicate mobile records can prevent legitimate credential activation.

### Non Functional Requirements
Privacy-aware handling; reliable linkage under concurrent registration.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Credential linkage exception register | UI | Medium | 6 |
| Citizen linkage review screen | UI | Medium | 6 |
| Credential linkage operations | API | Complex | 8 |
| Credential linkage persistence | Database | Medium | 4 |
| Citizen portal identity handoff | Integration | Simple | 4 |
| Credential linkage tests | Testing | Complex | 8 |
| Credential linkage guide | Documentation | Easy | 2 |
| **Total** | | | **38** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
