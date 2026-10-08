# F07-006 — Role-based report views

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-006 |
| Feature Name | Role-based report views |
| Module | 07 — Reporting & Analytics |
| Description | Restrict dashboards/reports by role and organisational scope |
| Business Objective | Ensure users see only dashboards and reports aligned to their role and org unit. |
| Actors | Admin; All report consumers |

### User Journey

- Admin maps report/dashboard catalogue to roles and org scopes → user login → catalogue filtered → unauthorized routes blocked.

### Functional Capabilities

- Entitlement matrix for dashboards and standard reports
- Org-unit scoping of data in views
- Default landing dashboard per role
- Deny-by-default for unmapped artefacts

### Inputs

Role; org unit; entitlement configuration

### Outputs

Filtered navigation and query scoping

### Business Rules

Entitlements inherit from Module 01 RBAC with report-specific overrides where needed

### Validations

- N/A

### Calculations

- None

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

- None

### Dependencies

Module 01; F07-001–F07-005

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Report catalogue entitlement matrix admin grid | Medium | 6 |
| UI | Preview report as role simulator panel | Easy | 4 |
| API | List reports with effective entitlement | Medium | 6 |
| API | Save role-to-report mapping updates | Easy | 4 |
| API | Enforce entitlement on report render requests | Medium | 6 |
| Database | Role-report mapping table | Easy | 2 |
| Testing | Cross-role visibility negative tests | Easy | 4 |
| Testing | Verifier vs admin catalogue diff | Easy | 4 |
| Documentation | Report RBAC configuration notes | Easy | 2 |

**Feature Total: 38 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
