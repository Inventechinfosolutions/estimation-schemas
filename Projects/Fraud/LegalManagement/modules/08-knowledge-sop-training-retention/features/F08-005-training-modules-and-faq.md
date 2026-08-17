# F08-005 — Training modules and FAQ

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-005 |
| **Feature Name** | Training modules and FAQ |
| **Module** | 08 — Knowledge, SOP, Training & Retention |

### Description
An Administrator publishes training content for Legal Research, Legal Writing, MS Word or MS Excel, and FAQ for the legal modules. A user opens the module or FAQ from the application. Classroom delivery is out of scope unless separately ordered.

### Business Objective
Deliver in-app training (Legal Research, Legal Writing, MS Word, MS Excel) and per-module FAQ — not classroom LMS.

### Actors
Administrator; Legal Cell; Advocate.

### User Journey
1. Administrator publishes training content for Legal Research, Legal Writing, MS Word or MS Excel, and FAQ for the legal modules.
2. A user opens the module or FAQ from the application.
3. Classroom delivery is not included unless separately ordered.

### Functional Capabilities
- Training Module list
- FAQ browser
- Admin Publish form
- Topics: Legal Research, Legal Writing, MS Word, MS Excel; FAQ per legal modules
- Not instructor-led classroom; not a vendor LMS product

### Inputs
Training content; topic; FAQ question/answer; target module; publish flag.

### Outputs
Published modules; FAQ entries.

### Business Rules
- In-application training/FAQ; classroom optional only if separately ordered.
- Per-module FAQ (Proceedings item 23).
- No generative-AI auto-FAQ.

### Validations
Topic required; publish only with content; FAQ linked to a legal module id.

### Calculations
None.

### Workflow
Publish content/FAQ → user opens from the application.

### Search Requirements
FAQ by module, keyword; training by topic.

### Documents
Training materials.

### Reports
Published training/FAQ inventory.

### Notifications
Optional new-FAQ notice.

### Security
Admin publish only; users read.

### Integrations
Internal (Simple).

### Dependencies
F01-001; all modules for FAQ targets.

### Assumptions
Content authored by SPLOCA/vendor as agreed; not video-platform build.

### Risks
FAQ drift after feature changes.

### Non Functional Requirements
Open from the application; per-module access to FAQ.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Training Module list | UI | Medium | 6 |
| FAQ browser | UI | Medium | 6 |
| Admin Publish form | UI | Medium | 6 |
| Content publish operations | API | Medium | 6 |
| Content entities | Database | Medium | 4 |
| In-app content retrieve | Integration | Simple | 4 |
| Training/FAQ tests | Testing | Medium | 6 |
| Training modules and FAQ guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- No classroom delivery hours.
