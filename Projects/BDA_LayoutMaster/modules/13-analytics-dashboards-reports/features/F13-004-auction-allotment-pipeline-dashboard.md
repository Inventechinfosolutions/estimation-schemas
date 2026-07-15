# F13-004 — Auction & Allotment Pipeline Dashboard

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F13-004 |
| **Feature Name** | Auction & Allotment Pipeline Dashboard |
| **Module** | 13 — Analytics, Dashboards & Reports |

### Description
Show auction-site summary, auction case pipeline, and allotment pipeline summary for authorized operational and executive users.

### Business Objective
Provide end-to-end visibility of auction and allotment progress without replacing process workspaces.

### Actors
- Commissioner/senior authority; auction/allotment officers; Auditor

### User Journey
1. User or system initiates the configured auction & allotment pipeline dashboard activity.
2. LMS validates authorized context and processes the requested capability.
3. LMS records the outcome and exposes permitted results to authorized users.

### Functional Capabilities
- Auction site summary; auction case pipeline; allotment pipeline; configured filters; authorized drill-through.

### Inputs
- Authorized request context, source reference, configured filters or feature-specific values.

### Outputs
- Feature-specific outcome, status, and authorized operational visibility.

### Business Rules
- Scope and authoritative business decisions remain with the owning LMS modules; this feature implements only its stated responsibility.

### Validations
- Authorized user/system context, valid source references, required configured inputs, and permitted state transitions.

### Calculations
- Feature-specific counts, status totals, or source-defined values only; no independent business calculation is introduced.

### Workflow
- Initiate → validate → process → record outcome → authorized review/retry where applicable.

### Search Requirements
- Search/filter by authorized source reference, status, date, and relevant feature context.

### Documents
- Supporting operational evidence or source-linked documents where applicable.

### Reports
- Authorized feature outcome/exception visibility; packaged reporting remains within the stated module scope.

### Notifications
- Operational completion or failure alerts through Module 11 where configured.

### Security
- RBAC, protected sensitive values, auditability, and least-privilege access.

### Integrations
- Internal LMS data services.

### Dependencies
- Modules 05–06; F13-001; F13-008.

### Assumptions
- Dashboard UI is Very High (16); payment reconciliation remains outside this feature.

### Risks
- Auction scope/state changes may affect pipeline definitions.

### Non Functional Requirements
- Near-real-time operational status and KPI-to-register reconciliation.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Auction and allotment pipeline dashboard | UI | Very High | 16 |
| Pipeline KPI and drill-through operations | API | Complex | 8 |
| Pipeline aggregation support | Database | Medium | 4 |
| Pipeline dashboard tests | Testing | Complex | 8 |
| Pipeline dashboard guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. Dashboard UI is Very High (16); payment reconciliation remains outside this feature.
