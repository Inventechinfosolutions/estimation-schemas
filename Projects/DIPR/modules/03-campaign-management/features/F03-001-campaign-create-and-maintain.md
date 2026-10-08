# F03-001 — Campaign create & maintain

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-001 |
| Feature Name | Campaign create & maintain |
| Module | 03 — Campaign Management |
| Description | Create and edit campaign profiles across print, digital, and outdoor with channel-specific media attributes and DIPR ownership metadata. |
| Business Objective | Establish the authoritative campaign record that drives approvals, assets, vendor work, field PoD tasks, and compliance roll-ups. |
| Actors | Campaign Officer; DIPR Administrator |

### User Journey

- Campaign Officer opens Campaign register → filters by channel and status → creates campaign with type, dates placeholder, districts, and media attributes → saves draft → updates as planning progresses → views summary tabs for linked vendors, assets, and PoD status (read-only links).

### Functional Capabilities

- Campaign register with filters (channel, type, status, district, officer)
- Multi-section campaign form: core profile, print attributes, digital attributes, outdoor site list references
- Draft vs submitted states before approval workflow (F03-002)
- Campaign detail dashboard with status badge and key dates
- Edit restrictions when campaign locked post-approval except via controlled amend path

### Inputs

- Campaign name, code, type, channels, districts, description, media-specific fields, owning officer, planned dates (refined in F03-003)

### Outputs

- Campaign record driving downstream modules

### Business Rules

- Valid campaign type/status from masters (F02-001)
- Cannot mark live without passing approval gates (F03-002)
- Outdoor campaigns require at least one location reference when channel includes outdoor

### Validations

- Mandatory name, type, channel selection; date coherence when both start/end entered

### Calculations

- None at create (budget in F03-004)

### Workflow

- Draft → Submitted for approval → (workflow F03-002) → Approved states

### Search Requirements

- Name, code, channel, status, vendor, district, date range

### Documents

- Attach brief document reference (stored with version feature F03-006)

### Reports

- None directly

### Notifications

- Triggers on submit via Module 08 (workflow events)

### Security

- Create/update per role matrix; vendors read only assigned campaigns

### Integrations

- None

### Dependencies

- F01, F02 masters; feeds F03-002–F03-007, F04, F05

### Assumptions

- Media buying execution outside AMT

### Risks

- Channel-specific attribute sprawl if DIPR adds many custom fields late

### Non Functional Requirements

- Large register pagination; form autosave for drafts optional per UX decision

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Campaign register with channel/status filters | Medium | 6 |
| UI | Campaign create wizard step 1 (identity, dates) | Medium | 6 |
| UI | Wizard step 2 multi-channel attribute panels | Complex | 12 |
| UI | Wizard step 3 district coverage and budget head | Medium | 6 |
| UI | Campaign detail summary tabs (overview, channels) | Easy | 4 |
| UI | Draft save and resume banner | Simple | 2 |
| UI | Duplicate campaign from existing dialog | Medium | 6 |
| API | List campaigns with filters and pagination | Medium | 6 |
| API | Create campaign draft | Medium | 6 |
| API | Update campaign profile and channel attributes | Complex | 8 |
| API | Promote draft to valid pre-approval state | Medium | 6 |
| API | Get campaign detail aggregate | Medium | 6 |
| API | Clone campaign from existing template | Medium | 6 |
| API | Validate print/digital/outdoor mandatory attributes | Complex | 8 |
| Database | Campaign core entity | Easy | 2 |
| Database | Per-channel attribute extension storage | Medium | 4 |
| Database | District coverage junction | Easy | 2 |
| Database | Draft status and version pointer | Easy | 2 |
| Testing | Print/digital/outdoor attribute validation matrix | Medium | 6 |
| Testing | Draft to pre-approval transition rules | Medium | 6 |
| Testing | Duplicate campaign data integrity | Easy | 4 |
| Testing | Register filter and pagination combinations | Easy | 4 |
| Documentation | Campaign setup playbook for DIPR staff | Easy | 2 |
| Documentation | UAT multi-channel campaign creation script | Medium | 3 |

**Feature Total: 123 hours**

### Estimation Assumptions

- Separate DMS product not introduced; brief attachments handled in F03-006 versioning.
