# F03-007 — Campaign–PoD linkage

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-007 |
| Feature Name | Campaign–PoD linkage |
| Module | 03 — Campaign Management |
| Description | Link campaigns to field PoD tasks and roll up verification status for compliance visibility on the campaign record. |
| Business Objective | Let DIPR see at a glance whether proof-of-display evidence is complete and verified for each active campaign and site. |
| Actors | Campaign Officer; PoD Verifier; Manager |

### User Journey

- Officer defines PoD task plan on campaign (sites/locations, expected capture count) → field captures PoD (Module 05/06) → verification progresses → campaign dashboard shows rollup percent verified/rejected → drill-down opens PoD evidence register filtered to campaign.

### Functional Capabilities

- Define PoD task lines tied to campaign, location/site, and schedule window
- Expected vs submitted vs verified counts per task line
- Rollup status widget on campaign (compliant, partial, non-compliant)
- Drill-down navigation to F05-006 register with campaign filter pre-applied
- Eligibility rules using F03-003 schedule (capture outside window flagged)

### Inputs

- Task definition: location, expected captures, due date, channel

### Outputs

- Task linkage records; rollup metrics on campaign

### Business Rules

- PoD tasks only on approved campaigns in active schedule window unless override role
- Rejected PoD counts reduce compliance until rework verified
- Third-party verification status included in rollup when present (F05-005)

### Validations

- Location must exist in geography master; expected count positive integer

### Calculations

- Compliance percentage = verified eligible / expected (DIPR-tuned formula documented in UAT)

### Workflow

- Task defined → capture → verification → rollup refresh

### Search Requirements

- Campaign list sort by compliance status

### Documents

- None

### Reports

- Campaign compliance summary in Module 07

### Notifications

- Alert when compliance falls below threshold (Module 08)

### Security

- Task definition requires campaign update; rollup read per role

### Integrations

- Reads PoD status from Module 05 (internal)

### Dependencies

- F03-001, F03-003; F05-001–F05-006; F02-003 locations

### Assumptions

- Task generation may be manual per campaign rather than auto-generated for all sites

### Risks

- Rollup formula disputes if expected counts not maintained

### Non Functional Requirements

- Rollup recalculates incrementally on verification events

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Campaign PoD coverage planner grid | Medium | 6 |
| UI | Link outdoor sites to campaign PoD slots | Medium | 6 |
| UI | Expected PoD count per site indicator | Easy | 4 |
| UI | PoD linkage status dashboard strip | Medium | 6 |
| UI | Bulk link sites from district filter | Medium | 6 |
| API | List PoD plan slots for campaign | Medium | 6 |
| API | Link or unlink site to PoD plan | Medium | 6 |
| API | Compute expected vs submitted PoD counts | Medium | 6 |
| API | Validate outdoor site geotag present | Easy | 4 |
| Database | Campaign–site PoD plan junction | Medium | 4 |
| Database | Expected capture schedule linkage | Easy | 2 |
| Testing | Counts update when PoD submitted | Medium | 6 |
| Testing | Unlink blocked when verified PoD exists | Medium | 6 |
| Documentation | PoD linkage planning guide for coordinators | Easy | 2 |

**Feature Total: 70 hours**

### Estimation Assumptions

- Mobile task inbox detail estimated in Module 06; this feature is web campaign-side linkage.
