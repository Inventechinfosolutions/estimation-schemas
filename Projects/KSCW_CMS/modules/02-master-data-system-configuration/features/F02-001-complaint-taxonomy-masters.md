# F02-001 — Complaint Taxonomy Masters

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-001 |
| Feature Name | Complaint Taxonomy Masters |
| Module | 02 — Master Data & System Configuration |
| Description | Maintain complaint taxonomy masters: category, sub-category, department, and priority. |
| Business Objective | Provide configurable classification used by routing and reporting. |
| Actors | Admin |

### User Journey

- Admin opens taxonomy masters → maintains category/sub-category/department/priority → activates/deactivates codes.

### Functional Capabilities

- CRUD for category, sub-category, department, priority
- Link sub-category to category
- Activate/deactivate without breaking history

### Inputs

- Code
- Name
- Parent category (for sub-category)
- Status

### Outputs

- Taxonomy master records for intake and routing

### Business Rules

- Inactive codes not offered on new complaints
- Historical complaints retain prior labels

### Validations

- Unique codes per master type
- Mandatory name

### Calculations

- None

### Workflow

- Create/update master → available to transactional modules

### Search Requirements

- Search/filter by code, name, status

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Admin only

### Integrations

- None

### Dependencies

- Module 01

### Assumptions

- Initial taxonomy list provided by KSCW

### Risks

- Frequent taxonomy churn after go-live

### Non Functional Requirements

- Fast lookup for intake dropdowns

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Taxonomy master screens (category/sub-category/department/priority) | Complex | 8 |
| API | Taxonomy CRUD and dependent lookups | Medium | 6 |
| Database | Taxonomy entities and parent–child links | Medium | 4 |
| Testing | Master CRUD and inactive-code behaviour | Medium | 6 |
| Documentation | Taxonomy admin notes | Easy | 2 |

**Feature Total: 26 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
