# F11-002 — Answer Key Challenge

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-002 |
| Feature Name | Answer Key Challenge |
| Module | 11 — Evaluation, Results & Digital Certification |
| Module Type | Business |
| Release | Go-live |

### Description
After a session, candidates may challenge specific question keys within a configured window (with optional fee), see their question and response only, submit reasons; challenges are grouped by item and reviewed by SMEs and the Technical Committee; accepted challenges correct or drop the item and trigger re-computation for all affected candidates.

### Business Objective
Implement the candidate challenge of answer keys while keeping re-evaluation out of scope.

### Actors
- Candidate
- SME Reviewer
- Technical Committee
- Result Officer

### User Journey
1. **Who creates:** Candidates raise challenges in the window.
2. **How they create:** The candidate selects questions and gives reasons.
3. **How they edit:** The candidate edits until the window closes.
4. **How they send for approval:** Challenges go to item review.
5. **How the approver sees pending items:** Reviewers see challenges grouped by item.
6. **How the approver decides:** Committee accepts (correct / drop) or rejects.
7. **How the applicant / maker sees history:** Candidates see outcomes.
8. **How the approver / auditor sees history:** Auditors see decisions and re-computations.

### Functional Capabilities
- Challenge window
- Question view limited to own items
- Grouping by item
- Committee decision
- Key correction or item drop
- Re-computation trigger
- Item suspension in bank

### UI Screens
- Candidate challenge form
- Challenge review by item
- Committee decision
- Challenge outcome

### Logical API Operations
- Raise challenge
- Group challenges
- Committee decision
- Apply key change

### Inputs
- Challenges

### Outputs
- Key corrections

### Business Rules
- Re-evaluation of responses not permitted
- Dropped items award marks to all or none per rule

### Validations
- Window

### Calculations
- Affected candidates

### Workflow
Raised → Reviewed → Accepted / Rejected

### Search Requirements
- By item

### Documents
- None

### Reports
- Challenge summary

### Notifications
- Outcome notice

### Security
- Limited item exposure

### Integrations
- None

### Dependencies
- F11-001
- F06-007

### Assumptions
- Challenge policy confirmed in FRS

### Risks
- Item exposure

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Candidate challenge form | Medium | 6 |
| UI | Challenge review by item | Medium | 6 |
| UI | Committee decision | Easy | 4 |
| UI | Challenge outcome | Easy | 4 |
| API | Raise challenge | Easy | 4 |
| API | Group challenges | Medium | 6 |
| API | Committee decision | Medium | 6 |
| API | Apply key change | Medium | 6 |
| Database | Challenges and decisions | Easy | 2 |
| Testing | Challenge tests | Medium | 6 |
| Documentation | Challenge guide | Easy | 2 |

**Feature Total: 52 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 22 | 2 | 0 | 6 | 2 | **52** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
