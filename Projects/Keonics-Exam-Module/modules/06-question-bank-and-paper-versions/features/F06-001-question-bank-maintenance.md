# F06-001 — Question Bank Maintenance

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | Question Bank Maintenance |
| **Module** | 06 — Question Bank and Paper Versions |

### Description
Examination Administrators create, edit, categorise, score and activate/deactivate objective questions in the question bank, including type, marks, correct answers, difficulty and subject/topic. Bulk import is supported where required. Deactivated questions must not be selected for new papers.

### Business Objective
Maintain a governed pool of scored objective items so randomised paper generation (F06-002) can draw eligible questions without breaking answer keys.

### Actors
Maker: Examination Administrator (question authoring). Approver: none in baseline (activate is admin action). Auditor: Examination Administrator via question change history.

### User Journey
1. Who creates: Examination Administrator.
2. How they create: Question register → New → enter stem, options, correct answer(s), marks, type, difficulty, subject/topic/category → save → activate when eligible for papers; or use import wizard for bulk load.
3. How they edit: Open question → revise content/key/metadata → save; deactivate instead of delete when historically used; import corrections via controlled re-import where allowed.
4. How they send for approval: Does not apply — no maker–checker for question publish in baseline; administrator activates/deactivates directly.
5. How the approver sees pending items: No approver inbox; inactive vs active filters on the question register.
6. How the approver decides: No second-person decision; activation is the administrator’s control.
7. How the applicant / maker sees history: Administrator views question change history (who changed stem/key/status).
8. How the approver / auditor sees history: Same history supports audit of key changes and activation events.

### Functional Capabilities
- Create and edit objective questions with options and correct-answer mapping.
- Configure question type, marks, difficulty, subject/topic/category.
- Activate and deactivate questions without destroying history.
- Ensure deactivated questions are excluded from new paper generation.
- Search and filter question register by category, difficulty, status, marks.
- Import questions from approved file format when required.
- Validate import rows and report success/error summary.
- Prevent activation of incomplete questions (missing key/marks).
- Preserve answer-key integrity on edit (warn when changing keys of previously used items).
- Audit create/update/activate/deactivate and import events.
- Support categorisation needed for per-category counts in paper generation.
- Role-restrict bank maintenance to Examination Administrator.

### UI Screens
| Screen | Purpose |
|---|---|
| Question bank register | Search/filter active and inactive questions |
| Question create and edit form | Stem, options, key, marks, metadata |
| Category and topic assignment screen | Assign subject/topic/category |
| Question activate and deactivate control screen | Status change with confirmation |
| Question import wizard screen | Bulk import flow |
| Question import result summary screen | Success/error outcomes |
| Question change history screen | Audit of content and status changes |

### Logical API operations
| Operation | Purpose |
|---|---|
| Search question bank | Filtered register query |
| Create question | Persist new question with key |
| Update question | Persist edits with validation |
| Activate or deactivate question | Status change for paper eligibility |
| Import questions batch | Bulk load from approved format |
| Validate question import rows | Pre-check import file |
| Get question change history | Return audit trail |

### Inputs
Question stem; options; correct answer mapping; marks; type; difficulty; subject/topic/category; import file; activate/deactivate action; administrator identity.

### Outputs
Question records; import result summary; eligibility flags for F06-002; history events.

### Business Rules
- Deactivated questions are not selected for new papers.
- Active questions must have complete key and positive marks.
- Historical papers retain references even if source question later deactivates.
- Import must not silently overwrite keys without validation report.

### Validations
- Mandatory stem, options count, correct key, marks > 0 for activation.
- Import format and row-level field checks.
- Category must exist where masters require it.

### Calculations
None beyond import success/failure counts.

### Workflow
Create/edit → (optional import) → activate → eligible for F06-002. Deactivate removes from future selection. No checker inbox.

### Search Requirements
By text, category, topic, difficulty, marks, active/inactive, updated date.

### Documents
Import file (transient); no candidate documents.

### Reports
Bank size by category feeds Module 09 / generation readiness.

### Notifications
None required for authoring.

### Security
Administrator-only; protect correct-answer keys from centre/invigilator and candidate roles; audited key changes.

### Integrations
None (file import is application feature, not external system sync).

### Dependencies
Module 03 examination parameters (categories/marks expectations); enables F06-002; consumed by Module 07/08.

### Assumptions
- Objective MCQ/similar only in this phase (no subjective marking).
- Exact import template approved by Department.
- Hours include import wizard as Very High UI and Very High import API.

### Risks
Thin pools by category break multi-version generation; key edits after use create evaluation disputes if not versioned carefully.

### Non Functional Requirements
Key confidentiality; performant search on large banks; clear import error reports.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Question bank register | UI | Medium | 6 |
| Question create and edit form | UI | Complex | 12 |
| Category and topic assignment screen | UI | Medium | 6 |
| Question activate and deactivate control screen | UI | Easy | 4 |
| Question import wizard screen | UI | Very High | 16 |
| Question import result summary screen | UI | Medium | 6 |
| Question change history screen | UI | Easy | 4 |
| Search question bank | API | Medium | 6 |
| Create question | API | Complex | 8 |
| Update question | API | Complex | 8 |
| Activate or deactivate question | API | Medium | 6 |
| Import questions batch | API | Very High | 16 |
| Validate question import rows | API | Medium | 6 |
| Get question change history | API | Easy | 4 |
| Question bank persistence | Database | Complex | 6 |
| Question bank maintenance tests | Testing | Complex | 8 |
| Question bank maintenance documentation | Documentation | Complex | 4 |

**Feature total: 126 hours**

### Estimation Assumptions
- Import treated as Very High API (import/export class per Estimation Master).
- Random paper generation hours remain on F06-002.
