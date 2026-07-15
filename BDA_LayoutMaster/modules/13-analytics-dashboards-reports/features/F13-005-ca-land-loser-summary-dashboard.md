# F13-005 — CA & Land Loser Summary Dashboard

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F13-005 |
| **Feature Name** | CA & Land Loser Summary Dashboard |
| **Module** | 13 — Analytics, Dashboards & Reports |

### Description
Show CA site and occupancy summaries together with Land Loser site summaries for authorized users.

### Business Objective
Give management a concise view of these distinct BDA process streams.

### Actors
- Commissioner/senior authority; CA/Land Loser officers; Auditor

### User Journey
1. User or system initiates the configured ca & land loser summary dashboard activity.
2. LMS validates authorized context and processes the requested capability.
3. LMS records the outcome and exposes permitted results to authorized users.

### Functional Capabilities
- CA site/occupancy summary; Land Loser summary; configured filters; authorized drill-through.

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
- Modules 07–08; F13-001; F13-008.

### Assumptions
- Dashboard UI is Very High (16); no process-state changes are included.

### Risks
- Historical flags may be incomplete until migration acceptance.

### Non Functional Requirements
- Near-real-time updates and reconciliation to underlying registers.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| CA and Land Loser summary dashboard | UI | Very High | 16 |
| Summary KPI and drill-through operations | API | Complex | 8 |
| Summary aggregation support | Database | Medium | 4 |
| Summary dashboard tests | Testing | Complex | 8 |
| Summary dashboard guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. Dashboard UI is Very High (16); no process-state changes are included.
