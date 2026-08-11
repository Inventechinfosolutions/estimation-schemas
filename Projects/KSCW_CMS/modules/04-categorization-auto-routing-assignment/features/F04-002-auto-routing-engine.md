# F04-002 — Auto-Routing Engine

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-002 |
| Feature Name | Auto-Routing Engine |
| Module | 04 — Categorization, Auto-Routing & Assignment |
| Description | Automatically route complaints using department, priority, and location rules. |
| Business Objective | Reduce manual assignment delay and bias. |
| Actors | System; Admin (rules); Supervisor |

### User Journey

- Complaint registered/categorized → routing engine evaluates rules → assigns queue/owner → appears in worklist.

### Functional Capabilities

- Rule evaluation on department/priority/location
- Fallback when no rule matches
- Admin rule maintenance UI

### Inputs

- Complaint attributes
- Routing rules

### Outputs

- Assigned queue/owner
- Routing decision log

### Business Rules

- First matching rule wins unless FRS defines priority among rules
- Unmatched → Supervisor unassigned queue

### Validations

- Rule completeness
- Target queue exists

### Calculations

- None

### Workflow

- Event → evaluate → assign → log

### Search Requirements

- Review routing log by complaint

### Documents

- None

### Reports

- None

### Notifications

- Optional assignment alert via Module 06

### Security

- Admin maintains rules; runtime system

### Integrations

- None

### Dependencies

- F02-001
- F02-002
- Module 03
- F04-001

### Assumptions

- Rule set approved before go-live

### Risks

- Conflicting rules cause misroutes

### Non Functional Requirements

- Deterministic routing; decision audit

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Routing rules maintenance screen | Complex | 8 |
| API | Routing evaluation engine and rule CRUD | Very High | 16 |
| Database | Routing rules and decision log | Complex | 6 |
| Testing | Rule match, conflict, and fallback scenarios | Complex | 8 |
| Documentation | Auto-routing engine notes | Medium | 3 |

**Feature Total: 41 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
