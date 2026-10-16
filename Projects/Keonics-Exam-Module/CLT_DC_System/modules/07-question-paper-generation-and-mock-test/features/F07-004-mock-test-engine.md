# F07-004 — Mock Test Engine

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-004 |
| Feature Name | Mock Test Engine |
| Module | 07 — Question Paper Generation & Mock Test |
| Module Type | Business |
| Release | Go-live |

### Description
Mock test available to booked candidates on portal and app, using the mock bank with the same interface as the real test (including a short typing practice), 25 questions in 30 minutes, unlimited attempts, active from a configurable 7–15 days before until the scheduled test, with score and review after each attempt.

### Business Objective
Familiarise candidates with the interface and pattern.

### Actors
- Candidate
- KEONICS Administrator

### User Journey
1. **Who creates:** The administrator configures mock parameters; candidates start attempts.
2. **How they create:** The candidate starts a mock test and answers.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The candidate sees past attempt scores.
8. **How the approver / auditor sees history:** Administrators see usage statistics.

### Functional Capabilities
- Mock parameters (questions, duration, window)
- Same interface as real test
- Typing practice
- Unlimited attempts
- Score and answer review
- Window enforcement

### UI Screens
- Mock test launcher
- Mock attempt history
- Mock configuration

### Logical API Operations
- Generate mock paper
- Mock window check
- Score mock attempt
- Mock statistics

### Inputs
- Mock bank

### Outputs
- Mock scores

### Business Rules
- Mock bank separate from main bank

### Validations
- Window

### Calculations
- Score

### Workflow
Started → Submitted

### Search Requirements
- None

### Documents
- None

### Reports
- Mock usage

### Notifications
- Mock availability notice

### Security
- Own attempts

### Integrations
- None

### Dependencies
- F06-007
- Module 09 interface

### Assumptions
- Reuses exam interface components

### Risks
- Load before test days

### Non Functional Requirements
- Supports 2,000 concurrent mock users

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Mock test launcher | Easy | 4 |
| UI | Mock attempt history | Easy | 4 |
| UI | Mock configuration | Easy | 4 |
| API | Generate mock paper | Medium | 6 |
| API | Mock window check | Easy | 4 |
| API | Score mock attempt | Easy | 4 |
| API | Mock statistics | Easy | 4 |
| Database | Mock attempts | Easy | 2 |
| Testing | Mock tests | Medium | 6 |
| Documentation | Mock test guide | Simple | 1 |

**Feature Total: 39 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 18 | 2 | 0 | 6 | 1 | **39** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Exam UI reused
- No external integration channel in this feature; Integration row omitted.
