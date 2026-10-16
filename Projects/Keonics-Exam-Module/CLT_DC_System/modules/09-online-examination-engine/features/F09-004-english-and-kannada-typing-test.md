# F09-004 — English & Kannada Typing Test

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-004 |
| Feature Name | English & Kannada Typing Test |
| Module | 09 — Online Examination Engine |
| Module Type | Business |
| Release | Go-live |

### Description
Typing test module after the MCQ section: separate English and Kannada tests with passage display, typing area, configured duration, Kannada input through configured layout (Nudi / KGP or InScript Unicode), backspace and paste controls, keystroke capture, gross and net words per minute, accuracy, and marks per configured scale (20 each).

### Business Objective
Deliver the 40-mark Part 2 assessment within the same test session.

### Actors
- Candidate

### User Journey
1. **Who creates:** The typing section opens after MCQ submission (or as configured).
2. **How they create:** The candidate types the passage within the time.
3. **How they edit:** Edits allowed per configured backspace rule.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The candidate sees typing results with the score.
8. **How the approver / auditor sees history:** Auditors see keystroke summaries.

### Functional Capabilities
- Passage display with highlighting
- Kannada Unicode input via configured layout
- Paste and copy blocked
- Backspace rules
- Keystroke capture
- Speed and accuracy computation
- Marks scale
- Auto-submit at time end

### UI Screens
- English typing test
- Kannada typing test
- Typing result summary

### Logical API Operations
- Fetch passage
- Capture keystroke stream
- Compute speed and accuracy
- Score typing test

### Inputs
- Typed text

### Outputs
- Typing score

### Business Rules
- Marks per configured WPM / accuracy bands
- Paste disabled

### Validations
- Keystroke stream integrity

### Calculations
- Gross WPM = characters / 5 / minutes; Net WPM = gross − errors / minutes; accuracy %

### Workflow
Not Started → Typing → Submitted

### Search Requirements
- None

### Documents
- None

### Reports
- Typing statistics

### Notifications
- None

### Security
- Keystroke anomaly flags

### Integrations
- None

### Dependencies
- F06-008
- F02-001

### Assumptions
- Kannada layout fixed in FRS

### Risks
- Kannada input method support across OS

### Non Functional Requirements
- No input lag

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | English typing test | Complex | 12 |
| UI | Kannada typing test | Complex | 12 |
| UI | Typing result summary | Easy | 4 |
| API | Fetch passage | Easy | 4 |
| API | Capture keystroke stream | Complex | 8 |
| API | Compute speed and accuracy | Complex | 8 |
| API | Score typing test | Medium | 6 |
| Database | Typing attempts and metrics | Easy | 2 |
| Testing | Typing engine tests including Kannada input | Complex | 8 |
| Documentation | Typing test rules | Easy | 2 |

**Feature Total: 66 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 26 | 2 | 0 | 8 | 2 | **66** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Kannada input and scoring rated Complex
- No external integration channel in this feature; Integration row omitted.
