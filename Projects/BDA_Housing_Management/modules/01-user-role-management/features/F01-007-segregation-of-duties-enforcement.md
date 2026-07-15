# F01-007 — Segregation-of-Duties Enforcement

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-007 |
| **Feature Name** | Segregation-of-Duties Enforcement |
| **Module** | 01 — User & Role Management |

### Description
Detect and prevent configured conflicts between proposing and approving responsibilities, evaluated against the acting **Person**, active **Post**, and **Role** (not free-form user roles).

### Business Objective
Reduce self-approval and incompatible-duty risk where the same person or post line would both propose and approve.

### Actors
Super Administrator; Approver (via Post); Auditor.

### User Journey
Administrator configures incompatible Role/Post/action combinations. At runtime, when a Person acting under a Post attempts a conflicted action, the system blocks it and records the event (with optional authorised exception).

### Functional Capabilities
- Conflict rule setup (Role / Post / process-action pairs)  
- Pre-action conflict check using session Person + Post + Role  
- Block or exception outcome; violation register  

### Inputs
Role/Post, process/action pair, Person, exception reason where permitted.

### Outputs
Conflict result, blocked-action message, violation register.

### Business Rules
- A Person cannot approve their own proposal where configured (same Person on the case).  
- Conflicts may also be defined between Roles or between Post and Manager Post relationships where configured.  
- Exception handling requires authorised justification and audit.

### Validations
Active Role/Post mapping required for rule targets; duplicate conflict rules blocked; exception reason mandatory when allowed.

### Calculations
None.

### Workflow
Configure conflict policy → evaluate action under session Post → block or record approved exception.

### Search Requirements
Person, Post, Role, process, action, conflict type, date range, outcome.

### Documents
None.

### Reports
SoD Violation and Exception Register.

### Notifications
Optional alert to security administrator for violations.

### Security
RBAC for policy maintenance; immutable violation evidence.

### Integrations
Internal workflow routing handoff (Simple).

### Dependencies
F01-001; F01-002; F01-003; F02-004.

### Assumptions
Baseline covers propose-versus-approve conflicts under the Post model, not a full enterprise GRC suite.

### Risks
Incomplete policy definitions may leave conflicts undetected across multi-post Persons.

### Non Functional Requirements
Low-latency checks; traceable policy and enforcement decisions.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| SoD policy register | UI | Medium | 6 |
| Conflict rule and exception review screen | UI | Complex | 8 |
| Conflict evaluation (Person/Post/Role) | API | Very High | 16 |
| SoD rule persistence | Database | Complex | 6 |
| Workflow enforcement handoff | Integration | Simple | 4 |
| SoD enforcement tests | Testing | Very High | 12 |
| SoD policy guide | Documentation | Medium | 3 |
| **Total** | | | **55** |

### Estimation Assumptions
- Uses Estimation Master values only.  
