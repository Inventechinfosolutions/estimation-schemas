# F09-004 — Possession Letter & Handover

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-004 |
| **Feature Name** | Possession Letter & Handover |
| **Module** | 09 — Allotment Sale Deed Registration Possession |

### Description
Verify possession readiness after registration, issue the possession letter, capture handover acknowledgement, and mark the unit as possession issued.

### Business Objective
Complete the housing lifecycle with a controlled, evidence-backed handover record.

### Actors
Possession Section; Housing Officer; Citizen; Auditor.

### User Journey
A possession officer opens a registration-completed case, reviews full-payment, registration, document, and readiness checks, generates the possession letter, records the handover date and acknowledgement, and confirms completion.

### Functional Capabilities
- Possession-pending queue, readiness checklist, letter preview/issue, acknowledgement upload, and handover register.
- Controlled holds/deficiency reasons and completion status transition.
- Citizen release of possession letter and acknowledgement view where applicable.

### Inputs
Registration-completed case, payment status, readiness checklist, possession date, letter template, acknowledgement, and officer remarks.

### Outputs
Possession letter, handover record, acknowledgement, possession-issued unit status, and process history.

### Business Rules
Possession cannot be issued until configured full-payment, registration, registered-deed, and readiness conditions are met; one current completed possession record applies per allotment; cancellation handling is outside this feature.

### Validations
Registration completion, mandatory readiness checks, authorised issuer, required possession date, acknowledgement/document where configured, and no duplicate handover.

### Calculations
Days from registration completion to possession and pending-handover ageing.

### Workflow
Registration completed → possession readiness review → letter issued → handover acknowledged → possession issued.

### Search Requirements
Possession letter number, booking/allotment, citizen, project, unit, readiness status, handover date, and completion status.

### Documents
Possession letter, readiness evidence, signed acknowledgement, and handover correspondence.

### Reports
Possession register, pending-handover ageing, and readiness-deficiency report.

### Notifications
Possession letter availability and handover completion through Module 12.

### Security
Possession-role access, citizen-owned letter visibility, immutable completion audit, and restricted acknowledgement access.

### Integrations
Registration/payment status consumption (Medium) and notification handoff (Easy).

### Dependencies
F09-003; Modules 07, 08, 12; Module 04 inventory status.

### Assumptions
Field inspection scheduling is not a separate feature; readiness evidence follows BDA checklist.

### Risks
Incomplete readiness documentation or missing acknowledgement may delay final completion.

### Non Functional Requirements
Responsive field-reference experience, reproducible letters, secure acknowledgements, and accurate status reflection.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Possession queue, readiness, and handover UI | UI | Very High | 16 |
| Readiness validation, issue, and completion processing | API | Very High | 16 |
| Possession and acknowledgement persistence | Database | Complex | 6 |
| Registration/payment/status and notification handoffs | Integration | Medium | 16 |
| Possession lifecycle tests | Testing | Very High | 12 |
| Possession handover guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
Payment and registration validation sources are consumed from existing modules; no external handover/mobile app is included.
