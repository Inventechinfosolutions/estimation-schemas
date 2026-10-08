# F04-002 — Asset versioning

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-002 |
| Feature Name | Asset versioning |
| Module | 04 — Creative Asset Inventory |
| Description | Maintain version history and current-version designation for each creative asset. |
| Business Objective | Support audit questions about which creative was approved when outdoor or digital displays changed mid-campaign. |
| Actors | Asset Manager; Campaign Officer; Approver (read) |

### User Journey

- Manager uploads revision to existing asset → new version row created → designates as current → prior version remains viewable → campaign package version (F03-006) can pin linked asset version → PoD verification compares against current unless historical PoD locked to earlier version.

### Functional Capabilities

- Version history panel with number, uploader, timestamp, notes
- Upload new version under same asset identity
- Designate current version with single active pointer
- Read-only access to superseded versions
- Roll-forward note when campaign brief references specific version

### Inputs

- New file, version notes, current-version flag

### Outputs

- Version chain; updated current pointer

### Business Rules

- Cannot delete versions; only supersede
- Current version used as default in PoD side-by-side unless task pinned
- Version increment automatic

### Validations

- Notes mandatory on version upload; file type consistent with asset channel policy

### Calculations

- None

### Workflow

- v1 upload → v2 upload → promote current → repeat

### Search Requirements

- Inventory shows current version number; filter assets with pending non-current uploads

### Documents

- Each version stored as separate binary

### Reports

- Version history in Module 07 audit exports

### Notifications

- Optional alert on new current version (Module 08)

### Security

- Version upload requires asset update permission

### Integrations

- None

### Dependencies

- F04-001; F03-006 campaign package links

### Assumptions

- Binary diff not required; side-by-side preview manual

### Risks

- Operators forget to promote current, causing PoD mismatch

### Non Functional Requirements

- Version list paginated for long-lived digital campaigns

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Asset version history stack panel | Easy | 4 |
| UI | Upload new creative version dialog | Medium | 6 |
| UI | Version compare preview (image/PDF) | Medium | 6 |
| UI | Mark version approved for PoD reference | Easy | 4 |
| UI | Superseded version banner on detail | Simple | 2 |
| API | List asset versions in lineage | Easy | 4 |
| API | Create new version in lineage | Medium | 6 |
| API | Set active approved version for PoD | Easy | 4 |
| API | Stream version binary for preview | Easy | 4 |
| Database | Version chain FK on asset | Easy | 2 |
| Database | Approved-for-PoD version flag | Simple | 1 |
| Testing | Only approved version used in PoD compare | Medium | 6 |
| Testing | Version rollback blocked after PoD link | Easy | 4 |
| Documentation | Creative version policy notes | Easy | 2 |

**Feature Total: 55 hours**

### Estimation Assumptions

- Branching/merging version trees not required.
