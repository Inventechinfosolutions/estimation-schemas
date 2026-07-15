# F05-008 — Arrears, Ageing & Defaulter Notices

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F05-008 |
| **Feature Name** | Arrears, Ageing & Defaulter Notices |
| **Module** | 05 — Revenue Billing & Collections |

### Description
Provide arrears ageing buckets (0–30, 31–60, 61–90, 90+), defaulter lists for escalation, and rent due/overdue notice batch generation with delivery logging.

### Business Objective
Drive recovery actions and transparency on overdue portfolios.

### Actors
- Revenue Officer, Accounts Officer, Estate Officer (escalation)

### User Journey
1. Officer opens Ageing dashboard/workspace.
2. Filters by complex, bucket, amount.
3. Selects defaulters → generate due/overdue notices from templates.
4. Dispatch via Module 09; archive PDFs; track delivery.

### Functional Capabilities
- Ageing buckets as per SOW
- Defaulter lists with drill-down to demands
- Rent due and overdue notice batches
- Escalation flags/lists for follow-up
- Export Excel for field recovery

### Inputs
- As-of date, filters, notice type, template/channel

### Outputs
- Ageing views; notice instances; exports

### Business Rules
- Ageing based on due date vs as-of date on outstanding balances after credits/payments.
- Must reconcile to ledgers (M4-AC5).
- Lease expiry notices remain Module 04; this owns rent due/overdue.

### Validations
- Cohort preview before send
- Contact channel availability

### Calculations
- Bucket assignment; totals by bucket/complex

### Workflow
Analyze → Select → Preview notices → Send → Log.

### Search Requirements
Defaulters by bucket, location, lease, amount.

### Documents
Notice PDFs (Module 08).

### Reports
Ageing Report; Defaulter List (Module 11 overlap OK as source).

### Notifications
Module 09 SMS/email/in-app.

### Security
RBAC + data scope; audit batches.

### Integrations
Notification Service (Simple).

### Dependencies
F05-001/007; F02-010; Modules 08–09; Module 03 scope

### Assumptions
- Workspace UI = Very High (dashboard-like ageing).
- Penalty posting still from F05-001 using rules; this feature is visibility + notices.

### Risks
- Notice fatigue if batches too frequent — configure cadence.

### Non Functional Requirements
- Ageing compute acceptable for portfolio; async for heavy runs

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Ageing & defaulter workspace | UI | Very High | 16 |
| Overdue notice batch UI | UI | Complex | 8 |
| Ageing compute & notice trigger ops | API | Complex | 8 |
| Ageing snapshot support | Database | Medium | 4 |
| Notification handoff | Integration | Simple | 4 |
| Arrears/defaulter tests | Testing | Complex | 8 |
| Arrears & notices guide | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- Legal eviction notices primarily Module 04 templates; rent overdue here.
