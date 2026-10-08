# F03-006 — Campaign version control

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-006 |
| Feature Name | Campaign version control |
| Module | 03 — Campaign Management |
| Description | Version campaign packages/briefs and link to creative asset versions for audit of what was approved and displayed. |
| Business Objective | Preserve evidence of creative and brief changes across long outdoor and digital campaigns. |
| Actors | Campaign Officer; Approver; Asset Manager |

### User Journey

- Officer uploads new brief package → system increments version → links selected asset versions from inventory → approver reviews version in approval or amend flow → field PoD references current approved package version at capture time.

### Functional Capabilities

- Version list on campaign with upload timestamp and author
- Upload new brief/document package with notes
- Link/unlink asset inventory versions to campaign package version
- Mark current approved version; read-only prior versions
- Compare metadata between two versions (dates, linked assets, uploader)

### Inputs

- File upload, version notes, linked asset version IDs

### Outputs

- Version chain on campaign; linkage to F04-002 asset versions

### Business Rules

- Only one current approved package version active for new PoD tasks
- Version delete disallowed; supersede only
- Large files subject to platform size limits (Module 10)

### Validations

- Mandatory notes on version upload; linked assets must belong to same campaign

### Calculations

- None

### Workflow

- Upload → (optional approval amend) → current version pointer updated

### Search Requirements

- Filter versions by date and author on campaign

### Documents

- Brief packages stored as campaign documents

### Reports

- Version history export via Module 07 audit views

### Notifications

- Notify approver on material version change (Module 08)

### Security

- Upload restricted; download per asset access rules (F04-005)

### Integrations

- None

### Dependencies

- F03-001, F04-002; approval F03-002 for amend policy

### Assumptions

- Virus scan handled at platform layer

### Risks

- Large video briefs affect storage planning

### Non Functional Requirements

- Version list remains responsive with chunked uploads

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Campaign version history list | Easy | 4 |
| UI | Compare versions side-by-side diff panel | Complex | 12 |
| UI | Create new version from approved baseline | Medium | 6 |
| UI | Version label and change summary form | Easy | 4 |
| UI | Read-only approved snapshot view | Medium | 6 |
| API | List campaign versions for lineage | Easy | 4 |
| API | Snapshot campaign state as new version | Complex | 8 |
| API | Get version diff metadata | Medium | 6 |
| API | Promote version to current editable draft | Medium | 6 |
| Database | Version snapshot storage | Medium | 4 |
| Database | Version lineage foreign key | Easy | 2 |
| Testing | Snapshot captures channel attributes | Medium | 6 |
| Testing | Compare highlights changed fields | Medium | 6 |
| Testing | Approved version immutability | Easy | 4 |
| Documentation | Campaign version control user notes | Easy | 2 |

**Feature Total: 80 hours**

### Estimation Assumptions

- Binary diff of creative files is out of scope; metadata compare only.
