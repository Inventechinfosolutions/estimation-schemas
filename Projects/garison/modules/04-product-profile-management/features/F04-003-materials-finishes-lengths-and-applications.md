# F04-003 — Materials, Finishes, Lengths & Applications

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-003 |
| Feature Name | Materials, Finishes, Lengths & Applications |
| Module | 04 — Product Profile Management |
| Module Type | Business |
| Release | Go-live |

### Description
Capture materials/species, finish options, available lengths (list of standard lengths such as 8', 12', 16' and/or random length range), minimum order quantity, special-order indicator, availability notes and applications (for example Doors, Windows, Ceilings, Walls) for each product.

### Business Objective
Tell customers what each profile is made of, how it is finished and how it is supplied, as shown in the existing Garrison catalogue.

### Actors
- Catalogue Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator records availability details for a product.
2. **How they create:** In the Materials & Availability tab they select materials and finishes from masters (with swatches), enter standard lengths or a random length range, minimum quantity, special-order flag and applications.
3. **How they edit:** They edit these while the product is in Draft, Changes Requested or a working draft.
4. **How they send for approval:** Details are submitted with the product through Submit for review; template-required items block submission if missing.
5. **How the approver sees pending items:** Reviewers see these sections in the review workspace.
6. **How the approver decides:** Reviewers approve or request changes.
7. **How the maker sees history:** The maker sees comments and history.
8. **How the approver / auditor sees history:** Auditors see changes in the audit log.

### Functional Capabilities
- Multi-select materials and finishes with swatches
- Standard length list and random length range (min–max) with unit
- Minimum quantity and unit (pieces/linear feet)
- Special-order indicator and availability note
- Applications master and multi-select
- Conditional mandatory per template

### UI Screens
- Materials and finishes selector with swatches
- Available lengths editor
- Commercial availability panel
- Applications selector

### Logical API Operations
- Save product materials
- Save product finishes
- Save available lengths with validation
- Save availability and applications
- Get selector lookup values

### Inputs
- Materials, finishes, standard lengths, random length min/max, minimum quantity, special-order flag, availability note, applications

### Outputs
- Availability data shown on product detail and used by filters

### Business Rules
- At least one material when template requires
- Random length min < max
- Special-order products show 'Available by special order' publicly

### Validations
- Lengths positive and within 1–20 feet
- Minimum quantity positive integer

### Calculations
- Length display formatting (feet/inches)

### Workflow
Edited within product workflow

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Create/edit products permission

### Integrations
- None

### Dependencies
- F02-003
- F04-001
- F08-003
- F09-003

### Assumptions
- No pricing or stock levels are shown

### Risks
- Garrison length conventions differ by category; validated at discovery

### Non Functional Requirements
- Selectors responsive with up to 100 master values

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Materials and finishes selector with swatches | Medium | 6 |
| UI | Available lengths editor | Medium | 6 |
| UI | Commercial availability panel | Easy | 4 |
| UI | Applications selector | Easy | 4 |
| API | Save product materials | Easy | 4 |
| API | Save product finishes | Easy | 4 |
| API | Save available lengths with validation | Medium | 6 |
| API | Save availability and applications | Easy | 4 |
| API | Get selector lookup values | Simple | 2 |
| Database | Product-material and product-finish links | Easy | 2 |
| Database | Product available lengths | Easy | 2 |
| Database | Applications master and product links | Easy | 2 |
| Testing | Material, finish and length combinations and display | Medium | 6 |
| Testing | Conditional mandatory when template requires | Easy | 4 |
| Documentation | Availability data guide | Simple | 1 |

**Feature Total: 57 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 20 | 6 | 0 | 10 | 1 | **57** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Length editor supports both list and range modes
- No external integration channel in this feature; Integration row omitted.
