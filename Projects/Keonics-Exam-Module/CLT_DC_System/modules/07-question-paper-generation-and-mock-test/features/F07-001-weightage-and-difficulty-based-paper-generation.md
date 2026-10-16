# F07-001 — Weightage & Difficulty-Based Paper Generation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-001 |
| Feature Name | Weightage & Difficulty-Based Paper Generation |
| Module | 07 — Question Paper Generation & Mock Test |
| Module Type | Business |
| Release | Go-live |

### Description
Automated generation of a paper set per session from the main bank: picks 60 items matching topic weightage and difficulty distribution from the session's pattern snapshot, respects exposure and cooling-off rules, avoids repeat items for re-attempting candidates where possible, assigns a typing passage, and stores the set sealed.

### Business Objective
Produce fair, comparable papers for each session automatically.

### Actors
- System
- Question Bank Administrator

### User Journey
1. **Who creates:** The system generates papers at a configured time before each session.
2. **How they create:** Generation runs by rules; the administrator can trigger it for a session.
3. **How they edit:** Regeneration is allowed until sealing with reason.
4. **How they send for approval:** Sealing needs administrator confirmation (no viewing of content).
5. **How the approver sees pending items:** The administrator sees generation status, not content.
6. **How the approver decides:** The administrator confirms seal.
7. **How the applicant / maker sees history:** Statistics (counts by topic and difficulty) are visible.
8. **How the approver / auditor sees history:** Auditors see generation logs.

### Functional Capabilities
- Constraint-based random selection
- Pattern snapshot usage
- Exposure and cooling-off
- Avoid repeats for re-attempts
- Typing passage assignment
- Generation without human view
- Statistics-only display

### UI Screens
- Paper generation status
- Generation statistics

### Logical API Operations
- Constraint-based selection engine
- Generate session set
- Validate set against blueprint
- Seal set

### Inputs
- Pattern snapshot
- Bank

### Outputs
- Sealed paper set

### Business Rules
- One set per session
- No human views set content

### Validations
- Set satisfies weightage

### Calculations
- Questions per topic and difficulty

### Workflow
Generated → Sealed → Released → Closed

### Search Requirements
- Sessions

### Documents
- None

### Reports
- Generation log

### Notifications
- Generation failure alert

### Security
- Encrypted sets

### Integrations
- None

### Dependencies
- F02-001
- F06-007
- F07-003

### Assumptions
- Bank strength sufficient

### Risks
- Insufficient items in a cell

### Non Functional Requirements
- Generation under 30 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Paper generation status | Medium | 6 |
| UI | Generation statistics | Easy | 4 |
| API | Constraint-based selection engine | Very High | 16 |
| API | Generate session set | Complex | 8 |
| API | Validate set against blueprint | Medium | 6 |
| API | Seal set | Medium | 6 |
| Database | Paper sets (encrypted) | Medium | 4 |
| Testing | Selection constraint tests | Complex | 8 |
| Testing | Randomness and fairness tests | Medium | 6 |
| Documentation | Paper generation algorithm note | Easy | 2 |

**Feature Total: 66 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 36 | 4 | 0 | 14 | 2 | **66** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Selection engine rated Very High
- No external integration channel in this feature; Integration row omitted.
