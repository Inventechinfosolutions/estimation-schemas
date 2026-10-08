# F03-002 — Campaign approval workflow

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-002 |
| Feature Name | Campaign approval workflow |
| Module | 03 — Campaign Management |
| Description | Embedded multi-stage approval with comments, reject/resubmit, and status trail for campaign go-live. |
| Business Objective | Enforce DIPR authorization before media spend and field PoD work proceed on a campaign. |
| Actors | Campaign Officer; Approver/Manager |

### User Journey

- Officer submits campaign → Approver sees Approval inbox → reviews summary, budget snapshot, and attachments → approves with comment or rejects with reason → Officer revises and resubmits → trail shows each stage timestamp and actor → approved campaigns unlock scheduling and PoD linkage.

### Functional Capabilities

- Configurable approval stages mapped to roles (not separate workflow product)
- Approval inbox and campaign-specific action panel
- Approve, reject, request clarification (hold) actions with mandatory comments on reject
- Resubmit from rejected state with visible prior comments
- Immutable approval history timeline on campaign

### Inputs

- Submit action; approver decision, comments, stage identifier

### Outputs

- Updated campaign approval status; history records; notifications

### Business Rules

- Campaign cannot enter field-eligible status without final stage approval
- Approver cannot approve own submission unless emergency override role (configurable off by default)
- Reject returns campaign to editable draft for officer

### Validations

- Comment required on reject; stage order enforced

### Calculations

- None

### Workflow

- Draft → Submitted → Stage N pending → Approved or Rejected → (resubmit loop)

### Search Requirements

- Inbox filter by stage, age, channel, officer

### Documents

- Approver views linked brief versions (F03-006)

### Reports

- None

### Notifications

- In-app/email on submit, approve, reject (Module 08)

### Security

- Approve permission distinct from update on campaign

### Integrations

- Internal notification dispatch only

### Dependencies

- F03-001 campaign record; F01-002 approve permission

### Assumptions

- Stage count configured at implementation (typically 2–3)

### Risks

- Unclear approver mapping delays UAT if DIPR org structure unset

### Non Functional Requirements

- Inbox loads pending items within interactive SLA; concurrent approver actions handled safely

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Campaign approval inbox list with SLA badges | Medium | 6 |
| UI | Inbox filters (stage, district, channel) | Easy | 4 |
| UI | Multi-stage approval action panel | Complex | 12 |
| UI | Reject reason modal with mandatory comment | Simple | 2 |
| UI | Request changes panel for campaign originator | Medium | 6 |
| UI | Approval history timeline on campaign detail | Easy | 4 |
| UI | Delegated approver assignment dialog | Medium | 6 |
| UI | Concurrent approval conflict notification | Simple | 2 |
| API | List pending approvals for current approver | Medium | 6 |
| API | Get workflow instance with stage definitions | Medium | 6 |
| API | Approve stage transition | Complex | 8 |
| API | Reject with reason and rollback stage | Complex | 8 |
| API | Resubmit campaign after rework | Medium | 6 |
| API | Record approval comments per stage | Easy | 4 |
| API | Trigger notification on stage change | Medium | 6 |
| API | Read workflow config by campaign type | Easy | 4 |
| Database | Workflow instance and stage state storage | Medium | 4 |
| Database | Approval comment and decision log | Easy | 2 |
| Database | Stage SLA timestamp fields | Simple | 1 |
| Testing | Multi-stage approve happy path | Complex | 8 |
| Testing | Reject and resubmit loop | Complex | 8 |
| Testing | Wrong role cannot approve stage | Medium | 6 |
| Testing | Concurrent approver safe handling | Medium | 6 |
| Documentation | Campaign approval configuration guide | Medium | 3 |
| Documentation | UAT multi-stage sign-off script | Easy | 2 |

**Feature Total: 130 hours**

### Estimation Assumptions

- Workflow engine embedded in campaign service, not a separate BPM module.
