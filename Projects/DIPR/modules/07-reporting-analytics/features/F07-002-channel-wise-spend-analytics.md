# F07-002 — Channel-wise spend analytics

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-002 |
| Feature Name | Channel-wise spend analytics |
| Module | 07 — Reporting & Analytics |
| Description | Views and reports of spend by print/digital/outdoor and campaign |
| Business Objective | Support financial oversight of advertisement spend across channels and campaigns. |
| Actors | Campaign Manager; Finance-oriented DIPR roles; Admin |

### User Journey

- User opens spend analytics → selects channel and campaign filters → views charts/tables → exports snapshot if entitled.

### Functional Capabilities

- Spend breakdown by print, digital, outdoor, and campaign
- Trend views by period
- Comparison of planned budget vs recorded spend where captured in masters
- Tabular detail with totals

### Inputs

Campaign budget/spend fields; channel classification; date range

### Outputs

Spend analytics views and export datasets

### Business Rules

Spend figures reconcile to campaign master and booking data
Entitlements enforced via F07-006

### Validations

- N/A

### Calculations

Channel totals, campaign roll-ups, variance where budget exists

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

Spend analytics screen and exportable tabular report

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

- None

### Dependencies

Module 03 Campaign Management; Module 02 masters; F07-006

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Spend analytics filter bar (channel, period, campaign) | Medium | 6 |
| UI | Channel spend bar/column chart panel | Complex | 12 |
| UI | Drill-down spend detail grid | Complex | 12 |
| UI | Export current view trigger | Simple | 2 |
| API | Channel spend summary aggregation | Complex | 8 |
| API | Spend detail paginated fetch | Medium | 6 |
| API | Channel master join for labels | Easy | 4 |
| Database | Spend roll-up summary store | Medium | 4 |
| Database | Analytics period partition helpers | Easy | 2 |
| Testing | Spend totals reconciliation sample | Complex | 8 |
| Testing | Unknown channel edge handling | Easy | 4 |
| Testing | Drill-down permission bounds | Medium | 6 |
| Documentation | Spend metric definitions | Medium | 3 |
| Documentation | Reconciliation with campaign budget notes | Easy | 2 |

**Feature Total: 79 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
