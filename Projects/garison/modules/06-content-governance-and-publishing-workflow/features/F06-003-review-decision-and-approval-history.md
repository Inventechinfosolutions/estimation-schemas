# F06-003 — Review Decision & Approval History

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-003 |
| Feature Name | Review Decision & Approval History |
| Module | 06 — Content Governance & Publishing Workflow |
| Module Type | Business |
| Release | Go-live |

### Description
Review workspace where the Catalogue Reviewer sees the item's data, preview and changes since the last published version, then approves or requests changes with general and field-level comments; full approval history per item, plus bulk approve for population batches.

### Business Objective
Provide maker-checker control over all catalogue content with an auditable decision record.

### Actors
- Catalogue Reviewer
- Super Administrator
- Catalogue Administrator (maker)

### User Journey
1. **Who creates:** This feature has no maker creation; reviewers act on items submitted through F06-002.
2. **How they create:** Not applicable — reviewers do not create items here; makers create and submit through F04/F05/F06-002.
3. **How they edit:** Makers address field-level comments by editing the item after it returns to Draft (Changes Requested).
4. **How they send for approval:** The decision is the approval step itself; Approve moves the item to Approved, Request changes returns it to Draft.
5. **How the approver sees pending items:** Reviewers open the item from the Review queue (F06-002) into the Review workspace.
6. **How the approver decides:** The reviewer compares data, preview and changes since last publication, then clicks Approve (optional comment) or Request changes (mandatory comment, optional field-level comments); bulk approve is available for selected queue items.
7. **How the maker sees history:** Makers see decisions and comments in the Reviewer comments panel and approval history timeline.
8. **How the approver / auditor sees history:** Reviewers and auditors see the full approval history (submit, claim, decision, comment, publish) per item and in the audit log.

### Functional Capabilities
- Review workspace: data view, preview, changes since last published version
- Approve with optional comment
- Request changes with mandatory comment and field-level comments
- Bulk approve from queue (population batches)
- Maker-checker: reviewer cannot approve their own last edit (Super Administrator override setting)
- Approval history timeline
- Comment resolution by maker

### UI Screens
- Review workspace with data, preview and change comparison
- Approve dialog
- Request changes dialog with field-level comments
- Approval history timeline
- Reviewer comments panel for maker

### Logical API Operations
- Approve item
- Bulk approve items
- Request changes with comments
- Get changes since last published version
- Get approval history
- Resolve reviewer comment

### Inputs
- Decision, comments, field-level comments, selected items for bulk approve

### Outputs
- Approved or Draft (changes requested) state
- Decision records and comments
- Notifications to makers

### Business Rules
- Request changes requires a comment
- Reviewer cannot approve an item they last edited unless override enabled
- Approval does not publish; publishing is a separate permission (F06-004)
- Bulk approve applies the same checks per item

### Validations
- Item must be In Review
- Comment length max 2,000 characters

### Calculations
- Field-level change comparison against last published snapshot

### Workflow
In Review → Approved; In Review → Changes Requested → Draft

### Search Requirements
- History filters by decision, reviewer, date

### Documents
- None

### Reports
- Approval history per item
- Reviewer throughput (count by reviewer per week)

### Notifications
- Maker notified on approval or changes requested (F06-005)

### Security
- Review permission; maker-checker enforced server-side

### Integrations
- None

### Dependencies
- F06-002
- F04-007
- F06-004
- F06-005
- F01-004

### Assumptions
- One reviewer decision is sufficient

### Risks
- Superficial bulk approvals; mitigated by completeness gate and dashboard

### Non Functional Requirements
- Change comparison renders within 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Review workspace with data, preview and change comparison | Very High | 16 |
| UI | Approve dialog | Simple | 2 |
| UI | Request changes dialog with field-level comments | Medium | 6 |
| UI | Approval history timeline | Medium | 6 |
| UI | Reviewer comments panel for maker | Easy | 4 |
| API | Approve item | Complex | 8 |
| API | Bulk approve items | Complex | 8 |
| API | Request changes with comments | Complex | 8 |
| API | Get changes since last published version | Complex | 8 |
| API | Get approval history | Medium | 6 |
| API | Resolve reviewer comment | Easy | 4 |
| Database | Review decisions and comments | Easy | 2 |
| Database | Published version snapshot for comparison | Medium | 4 |
| Testing | Maker-checker enforcement and override | Medium | 6 |
| Testing | Changes-requested round trip | Medium | 6 |
| Testing | Approval history completeness | Easy | 4 |
| Documentation | Reviewer guide | Easy | 2 |

**Feature Total: 100 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 34 | 42 | 6 | 0 | 16 | 2 | **100** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Review workspace with side-by-side comparison is a Very High UI
- Snapshot comparison drives Complex API rows
- No external integration channel in this feature; Integration row omitted.
