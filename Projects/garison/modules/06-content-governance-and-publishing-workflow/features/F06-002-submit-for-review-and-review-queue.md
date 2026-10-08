# F06-002 — Submit for Review & Review Queue

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-002 |
| Feature Name | Submit for Review & Review Queue |
| Module | 06 — Content Governance & Publishing Workflow |
| Module Type | Business |
| Release | Go-live |

### Description
Submit products and combinations (individually or in bulk) for review with a note to the reviewer, after the completeness gate; provide reviewers with a review queue and makers with a My submissions register; allow withdrawal before decision.

### Business Objective
Implement the Draft → In Review transition with a clear work queue so multi-contributor population stays controlled.

### Actors
- Catalogue Administrator
- Content Administrator
- Catalogue Reviewer
- Super Administrator

### User Journey
1. **Who creates:** Makers (Catalogue Administrator, Content Administrator) create the submission for products or combinations they have edited.
2. **How they create:** They click Submit for review in the workspace (or select many in the register and choose Bulk submit), add an optional note, and the system runs the completeness gate.
3. **How they edit:** Before a decision they can withdraw the submission, returning the item to Draft for further editing.
4. **How they send for approval:** Submission moves the item to In Review and notifies reviewers (F06-005).
5. **How the approver sees pending items:** Reviewers see pending items in the Review queue with filters by type, category, submitter and age, and can claim items to avoid duplicate work.
6. **How the approver decides:** Reviewers decide in F06-003.
7. **How the maker sees history:** Makers see status of all their submissions in My submissions.
8. **How the approver / auditor sees history:** Reviewers and auditors see submission, withdrawal and claim events in the approval history and audit log.

### Functional Capabilities
- Single submission with note and completeness gate
- Bulk submission from register with per-item results
- Withdraw submission
- Review queue with filters, age indicator and claim
- My submissions register
- Queue counts on admin dashboard

### UI Screens
- Submit for review dialog with completeness check
- Review queue with filters and claim
- My submissions register
- Bulk submit dialog with per-item results

### Logical API Operations
- Submit item for review with completeness gate
- Bulk submit for review
- Get review queue
- Get my submissions
- Withdraw submission
- Claim or release review item

### Inputs
- Item(s) to submit, note to reviewer

### Outputs
- Items in In Review state
- Queue entries
- Notifications

### Business Rules
- Only Draft or working-draft items can be submitted
- Completeness and rights pre-checks must pass
- Withdrawal only before a reviewer decision
- A claimed item is locked to that reviewer for 24 hours unless released

### Validations
- Note max 1,000 characters
- Bulk submission max 200 items per action

### Calculations
- Queue age = now − submitted time

### Workflow
Draft → In Review (submit); In Review → Draft (withdraw)

### Search Requirements
- Queue: type, category, submitter, submitted date, claimed by

### Documents
- None

### Reports
- Queue counts by age band

### Notifications
- Reviewers notified on submission (F06-005)

### Security
- Submit permission for makers; queue visible to review permission holders

### Integrations
- None

### Dependencies
- F06-001
- F06-003
- F06-005
- F04-001
- F05-002

### Assumptions
- Single review level (no multi-stage approval)

### Risks
- Review bottleneck during population; bulk approve available in F06-003

### Non Functional Requirements
- Queue loads under 2 seconds with 1,000 pending items

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Submit for review dialog with completeness check | Medium | 6 |
| UI | Review queue with filters and claim | Complex | 12 |
| UI | My submissions register | Medium | 6 |
| UI | Bulk submit dialog with per-item results | Medium | 6 |
| API | Submit item for review with completeness gate | Complex | 8 |
| API | Bulk submit for review | Complex | 8 |
| API | Get review queue | Medium | 6 |
| API | Get my submissions | Medium | 6 |
| API | Withdraw submission | Medium | 6 |
| API | Claim or release review item | Easy | 4 |
| Database | Workflow state and transition history | Medium | 4 |
| Database | Review claim | Simple | 1 |
| Testing | Submission gates and state transitions | Complex | 8 |
| Testing | Bulk submit with partial failures | Medium | 6 |
| Testing | Queue visibility by role | Easy | 4 |
| Documentation | Submission and review guide | Easy | 2 |

**Feature Total: 93 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 38 | 5 | 0 | 18 | 2 | **93** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Bulk submit with per-item gate results drives Complex API rows
- No external integration channel in this feature; Integration row omitted.
