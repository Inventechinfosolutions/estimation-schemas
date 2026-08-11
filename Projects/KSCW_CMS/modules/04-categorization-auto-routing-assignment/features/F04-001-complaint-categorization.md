# F04-001 — Complaint Categorization

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-001 |
| Feature Name | Complaint Categorization |
| Module | 04 — Categorization, Auto-Routing & Assignment |
| Description | Apply or update complaint category and related classification fields. |
| Business Objective | Ensure complaints are correctly classified for routing and SLA. |
| Actors | Operator; Supervisor |

### User Journey

- User opens complaint → sets/updates category, sub-category, priority, department as allowed → saves.

### Functional Capabilities

- Categorization panel on complaint
- Dependent dropdowns from taxonomy masters

### Inputs

- Category
- Sub-category
- Priority
- Department

### Outputs

- Updated classification on complaint

### Business Rules

- Only permitted roles may change after certain stages per FRS
- Changes may trigger re-route (F04-004)

### Validations

- Valid master combinations

### Calculations

- None

### Workflow

- Open → classify → save → optional route

### Search Requirements

- Filter worklists by category/priority

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Role-gated edit

### Integrations

- None

### Dependencies

- F02-001
- Module 03

### Assumptions

- Taxonomy complete before go-live

### Risks

- Misclassification delays resolution

### Non Functional Requirements

- Audit classification changes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Complaint categorization panel with dependent dropdowns | Medium | 6 |
| API | Update classification with validation | Medium | 6 |
| Database | Classification fields and change history hooks | Easy | 2 |
| Testing | Dependent master and permission cases | Medium | 6 |
| Documentation | Categorization notes | Easy | 2 |

**Feature Total: 22 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
