# F06-007 — Mock & Main Question Bank Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-007 |
| Feature Name | Mock & Main Question Bank Management |
| Module | 06 — Question Bank & Content Authoring Tool |
| Module Type | Business |
| Release | Go-live |

### Description
Management of two separate banks (mock and main), item lifecycle (active, suspended, retired), exposure control (usage count, last used session), cooling-off rules, bank strength by topic and difficulty, annual 5% growth tracking and item suspension on challenge.

### Business Objective
Keep the main bank secure and fresh, and the mock bank separate.

### Actors
- Question Bank Administrator

### User Journey
1. **Who creates:** The administrator manages approved items.
2. **How they create:** The administrator assigns items to mock or main bank.
3. **How they edit:** The administrator suspends, retires or reactivates items with reason.
4. **How they send for approval:** Retirement of many items needs committee approval.
5. **How the approver sees pending items:** Committee sees requests.
6. **How the approver decides:** Committee approves.
7. **How the applicant / maker sees history:** The administrator sees bank strength dashboards.
8. **How the approver / auditor sees history:** Auditors see item lifecycle events.

### Functional Capabilities
- Two separate banks
- Lifecycle states
- Exposure count and cooling-off
- Bank strength dashboard
- Growth tracking
- Suspension from challenges (F11-002)

### UI Screens
- Bank browser (segregated)
- Item lifecycle actions
- Bank strength dashboard

### Logical API Operations
- Assign bank
- Lifecycle change
- Exposure tracking
- Bank strength

### Inputs
- Items

### Outputs
- Bank status

### Business Rules
- Mock items never used in main tests
- Items above exposure threshold rested

### Validations
- Reason codes

### Calculations
- Exposure rate

### Workflow
Active → Suspended → Retired

### Search Requirements
- Items by metadata

### Documents
- None

### Reports
- Bank strength

### Notifications
- Low-strength alerts

### Security
- Segregated views

### Integrations
- None

### Dependencies
- F06-003
- F07-001

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Bank browser (segregated) | Medium | 6 |
| UI | Item lifecycle actions | Easy | 4 |
| UI | Bank strength dashboard | Medium | 6 |
| API | Assign bank | Easy | 4 |
| API | Lifecycle change | Easy | 4 |
| API | Exposure tracking | Medium | 6 |
| API | Bank strength | Medium | 6 |
| Database | Bank assignment and exposure | Easy | 2 |
| Testing | Bank management tests | Medium | 6 |
| Documentation | Bank management guide | Easy | 2 |

**Feature Total: 46 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 20 | 2 | 0 | 6 | 2 | **46** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
