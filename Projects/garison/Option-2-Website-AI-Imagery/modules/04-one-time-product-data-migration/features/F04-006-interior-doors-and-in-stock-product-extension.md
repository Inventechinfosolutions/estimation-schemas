# F04-006 — Interior Doors & In-Stock Product Extension

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-006 |
| Feature Name | Interior Doors & In-Stock Product Extension |
| Module | 04 — One-time Product Data Migration |
| Module Type | Technical |
| Release | Optional |

### Description
Optional extension applying the same extraction, preparation and page approach to the Interior Doors (Stock, Classic, Modern, Transitional, French) and In-Stock (MDF, Plywood, Frogboard) sections, which have different attributes from mouldings.

### Business Objective
Let Garrison show doors and sheet goods too, using the same process.

### Actors
- Delivery developer
- Garrison catalogue owner (review)
- Visitor

### User Journey
1. **Who creates:** The delivery developer extracts and prepares door and sheet-goods products.
2. **How they create:** Adapters write records into an extended dataset; Garrison reviews them in the same workbook.
3. **How they edit:** Corrections follow the same review rounds as mouldings.
4. **How they send for approval:** Approval follows the review workbook sign-off (F04-004).
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's sign-off email is the decision.
7. **How the maker sees history:** Garrison sees the change log.
8. **How the approver / auditor sees history:** The delivery lead keeps the review records.

### Functional Capabilities
- Extraction adapters for doors and in-stock sections
- Attribute mapping for doors and sheet goods
- Listing and detail templates

### UI Screens
- Doors and sheet goods listing template
- Doors and sheet goods detail template

### Logical API Operations
- Extract doors and in-stock products
- Map door and sheet-goods attributes
- Generate doors and sheet goods data files

### Inputs
- Doors and in-stock catalogue sections

### Outputs
- Extended dataset and pages

### Business Rules
- Same rights, review and build rules as mouldings

### Validations
- Same validation as mouldings plus section-specific attributes

### Calculations
- None

### Workflow
Same as mouldings

### Search Requirements
- Included in catalogue search

### Documents
- None

### Reports
- Included in reconciliation

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- Source catalogue (via F04-001)

### Dependencies
- F04-001
- F04-003
- F04-005
- F03-002
- F03-003

### Assumptions
- Per-product verification for these items charged at the per-product rate

### Risks
- Door products may have richer configuration than can be shown simply

### Non Functional Requirements
- Same as moulding pages

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Doors and sheet goods listing template | Complex | 12 |
| UI | Doors and sheet goods detail template | Medium | 6 |
| API | Extract doors and in-stock products | Medium | 6 |
| API | Map door and sheet-goods attributes | Easy | 4 |
| API | Generate doors and sheet goods data files | Easy | 4 |
| Database | Extended attributes for doors and sheet goods | Easy | 2 |
| Testing | Doors and sheet goods extraction and display | Medium | 6 |
| Documentation | Extension notes | Simple | 1 |

**Feature Total: 41 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 14 | 2 | 0 | 6 | 1 | **41** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Reuses the moulding tooling; adapters and two templates are new
- No external integration channel in this feature; Integration row omitted.
