# F05-003 — Manual verification workflow

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-003 |
| Feature Name | Manual verification workflow |
| Module | 05 — Proof-of-Display Capture & Verification |
| Description | Accept, reject, or send PoD for rework with comments and full status history for DIPR verifiers. |
| Business Objective | Human judgment on whether displayed creative matches approved assets and site context. |
| Actors | PoD Verifier; Campaign Officer (read/rework submit); Manager (read) |

### User Journey

- Verifier opens work queue → selects PoD → views side-by-side creative vs field photo with metadata stamp → accepts, rejects, or marks rework with comments → field user resubmits → history shows each decision → campaign rollup updates (F03-007).

### Functional Capabilities

- Verifier queue sorted by priority, age, campaign
- Side-by-side PoD image and linked creative preview
- Actions: accept, reject, rework with mandatory comments on reject/rework
- Status history timeline with actor and timestamp
- Reassignment of queue item to another verifier (supervisor)

### Inputs

- Decision, comments, optional rework due date

### Outputs

- Verification status on PoD; history rows; notifications

### Business Rules

- Verify permission required distinct from capture
- Accepted PoD locks core metadata immutability unless admin exception
- Rework returns item to submitter’s pending list

### Validations

- Comment length minimum on negative decisions

### Calculations

- None

### Workflow

- Pending validation → pending verification → accepted / rejected / rework → (resubmit loop)

### Search Requirements

- Queue filters by campaign, district, status, verifier

### Documents

- None

### Reports

- Verification throughput in Module 07

### Notifications

- Outcomes to field user and campaign officer (Module 08)

### Security

- Verifiers cannot verify PoD they captured if conflict policy enabled

### Integrations

- Internal links to asset preview (F04-005)

### Dependencies

- F05-001, F05-004; F04-005 preview; F01 verify permission

### Assumptions

- AI auto-accept is out of scope; all decisions manual unless third-party score in F05-005

### Risks

- Queue backlog if verifier staffing insufficient

### Non Functional Requirements

- Side-by-side viewer responsive for large images

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | PoD verifier work queue with priority sort | Medium | 6 |
| UI | Side-by-side creative vs PoD review screen | Complex | 12 |
| UI | Zoom and pan controls on PoD image | Medium | 6 |
| UI | Accept/reject/rework action panel | Medium | 6 |
| UI | Reject reason code picker modal | Simple | 2 |
| UI | Rework instructions comment box | Easy | 4 |
| UI | Verification status history timeline | Easy | 4 |
| UI | Conflict-of-interest self-declare checkbox | Simple | 2 |
| API | List pending PoD verification queue | Medium | 6 |
| API | Get PoD with linked approved creative asset | Medium | 6 |
| API | Record verifier accept decision | Complex | 8 |
| API | Record reject or rework with reason | Complex | 8 |
| API | Reassign queue item to another verifier | Easy | 4 |
| Database | Verification decision and reason codes | Medium | 4 |
| Database | Verifier assignment log | Easy | 2 |
| Testing | Rework loop until accept | Complex | 8 |
| Testing | Verifier cannot verify own submission | Medium | 6 |
| Testing | Reject reason mandatory validation | Easy | 4 |
| Documentation | Verifier desk procedures | Medium | 3 |
| Documentation | UAT manual verification desk script | Easy | 2 |

**Feature Total: 103 hours**

### Estimation Assumptions

- Video PoD review uses frame snapshot compare, not frame-by-frame editing tools.
