# F02-001 — Syllabus, Marks & Weightage Configuration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-001 |
| Feature Name | Syllabus, Marks & Weightage Configuration |
| Module | 02 — Examination Configuration & Masters |
| Module Type | Business |
| Release | Go-live |

### Description
Versioned configuration of the examination pattern: Part 1 topics (12 topics totalling 60 marks), Part 2 typing tests (English 20, Kannada 20), marks per question, weightage, difficulty mix, duration (90 minutes), qualifying percentage (50%), negative marking flag, with approval and a snapshot attached to every test session.

### Business Objective
Allow DPAR / KEONICS to change syllabus and weightage without code changes while preserving the pattern used in each past session.

### Actors
- KEONICS Administrator
- Approving Authority

### User Journey
1. **Who creates:** The KEONICS Administrator creates a pattern version; the RFP pattern is seeded.
2. **How they create:** The administrator edits topics, marks, weightage, difficulty mix, typing test parameters, duration and qualifying marks, and saves a draft with effective date.
3. **How they edit:** The administrator edits the draft; totals and question bank sufficiency are checked live.
4. **How they send for approval:** The draft is submitted for approval.
5. **How the approver sees pending items:** The Approving Authority sees the version with comparison.
6. **How the approver decides:** The Approving Authority approves or returns.
7. **How the applicant / maker sees history:** The administrator sees versions and sessions using each.
8. **How the approver / auditor sees history:** Auditors see the snapshot stored on each session.

### Functional Capabilities
- Topic list with marks and weightage
- Part 2 typing test configuration (language, duration, passage length, marks)
- Difficulty distribution per topic
- Duration, qualifying %, negative marking flag and value
- Bank sufficiency check (enough approved questions per topic and difficulty)
- Effective-dated versions with approval
- Immutable snapshot per session

### UI Screens
- Pattern versions
- Topic, marks and weightage editor
- Typing test parameters
- Bank sufficiency check
- Version comparison and approval

### Logical API Operations
- Save pattern draft
- Validate totals and weightage
- Check bank sufficiency
- Approve / return pattern
- Snapshot pattern to session
- Resolve active pattern

### Inputs
- Topics, marks, weightage
- Typing parameters
- Duration, qualifying %

### Outputs
- Approved pattern
- Session snapshots

### Business Rules
- Weightage totals 100%
- Pattern changes never alter past sessions
- Activation blocked if bank is insufficient

### Validations
- Positive marks
- Totals

### Calculations
- Questions per topic = 60 × topic weightage / Part 1 weightage
- Qualifying marks = total × qualifying %

### Workflow
Draft → Approved → Active → Superseded

### Search Requirements
- Versions

### Documents
- DPAR order reference

### Reports
- Pattern history

### Notifications
- Approval requests

### Security
- Admin edits; approver approves

### Integrations
- None

### Dependencies
- Module 06
- F07-001

### Assumptions
- RFP pattern is the starting version

### Risks
- Pattern changes close to sessions

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Pattern versions | Easy | 4 |
| UI | Topic, marks and weightage editor | Complex | 12 |
| UI | Typing test parameters | Medium | 6 |
| UI | Bank sufficiency check | Medium | 6 |
| UI | Version comparison and approval | Medium | 6 |
| API | Save pattern draft | Medium | 6 |
| API | Validate totals and weightage | Medium | 6 |
| API | Check bank sufficiency | Complex | 8 |
| API | Approve / return pattern | Easy | 4 |
| API | Snapshot pattern to session | Medium | 6 |
| API | Resolve active pattern | Easy | 4 |
| Database | Pattern, topics and versions | Medium | 4 |
| Database | Session pattern snapshot | Easy | 2 |
| Testing | Pattern validation and snapshot tests | Medium | 6 |
| Testing | Sufficiency check tests | Medium | 6 |
| Documentation | Pattern configuration guide | Easy | 2 |

**Feature Total: 88 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 34 | 34 | 6 | 0 | 12 | 2 | **88** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Sufficiency check rated Complex
- No external integration channel in this feature; Integration row omitted.
