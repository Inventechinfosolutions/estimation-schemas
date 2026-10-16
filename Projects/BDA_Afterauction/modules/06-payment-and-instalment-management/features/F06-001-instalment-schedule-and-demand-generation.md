# F06-001 — Instalment Schedule & Demand Generation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-001 |
| Feature Name | Instalment Schedule & Demand Generation |
| Module | 06 — Payment & Instalment Management |
| Module Type | Business |
| Release | Go-live |

### Description
Generation of the instalment schedule for each awarded site from the rule version stamped at award: first 25% within 4 days of intimation (less EMD where configured), second 50% within 90 days, final 25% after draft sale deed approval, with demand notices per instalment, revision on approved extensions and a site-level schedule view.

### Business Objective
Compute accurate dues and due dates automatically for every site and create the basis for collection, reminders and defaults.

### Actors
- System
- Finance Officer
- Successful Bidder (view)

### User Journey
1. **Who creates:** The system creates the schedule automatically at result approval.
2. **How they create:** The schedule is computed using the stamped rule version and intimation date; each instalment gets a demand number.
3. **How they edit:** Schedules are not edited manually; revisions happen through extensions (F06-007) or rule-based re-computation approved by the Finance Officer.
4. **How they send for approval:** Manual re-computation requests go to the Finance Officer.
5. **How the approver sees pending items:** The Finance Officer sees pending schedule revisions.
6. **How the approver decides:** The Finance Officer approves or rejects the revision.
7. **How the applicant / maker sees history:** The bidder sees the schedule and demand notices in the portal.
8. **How the approver / auditor sees history:** Auditors see all schedule versions with reason.

### Functional Capabilities
- Rule-based schedule with EMD adjustment
- Event-based instalments (final 25% raised on draft deed approval through F08-004)
- Demand notice generation per instalment (bilingual PDF)
- Schedule versioning on extension or correction
- Schedule view for officials and bidders

### UI Screens
- Site schedule view
- Schedule revision request and approval
- Demand notice preview

### Logical API Operations
- Generate schedule from rule
- Create demand
- Generate demand notice
- Revise schedule with version
- Approve schedule revision
- Get schedule

### Inputs
- Bid amount
- EMD
- Rule version
- Intimation date
- Trigger events

### Outputs
- Schedule
- Demands
- Demand notices

### Business Rules
- Schedule uses the rule version stamped at award
- Total of instalments equals bid amount less EMD as per rule
- Due dates falling on holidays move to next working day (configurable)

### Validations
- Rule exists
- Amounts positive

### Calculations
- Instalment = bid × % − EMD adjustment
- Due date = trigger date + due days

### Workflow
Generated → Active → Revised (new version)

### Search Requirements
- Schedules by site, bidder, due date

### Documents
- Demand notices

### Reports
- Dues by period

### Notifications
- Demand issued notice to bidder

### Security
- Only Finance Officer approves revisions

### Integrations
- None

### Dependencies
- F02-001
- F05-003
- F08-004

### Assumptions
- Rules confirmed by BDA

### Risks
- Rounding disputes; rounding rule documented

### Non Functional Requirements
- Schedule generation under 1 second

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Site schedule view | Medium | 6 |
| UI | Schedule revision request and approval | Medium | 6 |
| UI | Demand notice preview | Easy | 4 |
| API | Generate schedule from rule | Complex | 8 |
| API | Create demand | Medium | 6 |
| API | Generate demand notice | Medium | 6 |
| API | Revise schedule with version | Medium | 6 |
| API | Approve schedule revision | Easy | 4 |
| API | Get schedule | Easy | 4 |
| Database | Instalment schedule and demand store with versions | Medium | 4 |
| Testing | Schedule calculation tests with EMD and rounding | Complex | 8 |
| Testing | Revision and versioning tests | Medium | 6 |
| Documentation | Schedule computation reference | Easy | 2 |

**Feature Total: 70 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 34 | 4 | 0 | 14 | 2 | **70** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Calculation rated Complex
- No external integration channel in this feature; Integration row omitted.
