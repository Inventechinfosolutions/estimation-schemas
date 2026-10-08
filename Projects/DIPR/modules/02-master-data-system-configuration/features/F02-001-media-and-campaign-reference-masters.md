# F02-001 — Media & campaign reference masters

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-001 |
| Feature Name | Media & campaign reference masters |
| Module | 02 — Master Data & System Configuration |
| Description | Maintain media types, campaign types, statuses, and related lookups used when creating campaigns and classifying assets. |
| Business Objective | Standardize print, digital, and outdoor channel vocabulary so campaigns and creatives remain comparable across DIPR reporting. |
| Actors | DIPR Administrator; Campaign Officer (read) |

### User Journey

- Administrator opens Reference Masters hub → selects Media type or Campaign type/status → adds or edits values with codes and display labels → activates/deactivates obsolete values → campaign forms immediately offer only active lookups.

### Functional Capabilities

- CRUD for media channel types (print, digital, outdoor sub-types as configured)
- CRUD for campaign types and lifecycle statuses
- Optional budget head / cost category lookups when DIPR confirms list
- Multilingual display labels for key values where UI requires
- Prevent delete when referenced; allow deactivate

### Inputs

- Code, name, labels, sort order, active flag, optional parent for hierarchies

### Outputs

- Updated lookup sets consumed by Campaign and Asset modules

### Business Rules

- Campaign creation blocked if required status/type master missing
- Inactive values hidden on new records but retained on historical campaigns

### Validations

- Unique codes within master type; mandatory name

### Calculations

- None

### Workflow

- Draft value → Active → Inactive

### Search Requirements

- Filter by master category and active flag

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Administrator write; entitled roles read-only

### Integrations

- None

### Dependencies

- F01-002 permissions

### Assumptions

- Initial master seed from DIPR spreadsheet at go-live

### Risks

- Frequent status renames confuse historical reports if codes change

### Non Functional Requirements

- Lookup cache refresh without redeploy when parameters designed as configuration

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Media channel type maintenance list | Easy | 4 |
| UI | Media channel create/edit form | Easy | 4 |
| UI | Campaign type maintenance list | Easy | 4 |
| UI | Campaign type bilingual label editor | Medium | 6 |
| UI | Campaign status lifecycle lookup screen | Easy | 4 |
| UI | Budget head / scheme code lookup screen | Easy | 4 |
| UI | Deactivate master in-use warning modal | Simple | 2 |
| API | List media channels with filters | Simple | 2 |
| API | CRUD media channel master | Easy | 4 |
| API | List campaign types | Simple | 2 |
| API | CRUD campaign type with localized labels | Medium | 6 |
| API | List and CRUD campaign status with ordering | Easy | 4 |
| API | List and CRUD budget head master | Easy | 4 |
| API | Referential guard on master deactivate | Medium | 6 |
| Database | Media channel entity | Simple | 1 |
| Database | Campaign type entity with i18n labels | Easy | 2 |
| Database | Campaign status and budget head entities | Easy | 2 |
| Database | Cross-master referential guard indexes | Medium | 4 |
| Testing | Deactivate when referenced by active campaign | Medium | 6 |
| Testing | Multilingual label validation | Easy | 4 |
| Testing | Status ordering and code uniqueness | Easy | 4 |
| Documentation | Reference master seeding checklist | Easy | 2 |
| Documentation | UAT reference master walkthrough | Easy | 2 |

**Feature Total: 83 hours**

### Estimation Assumptions

- Hierarchies limited to one optional parent level unless DIPR expands scope.
