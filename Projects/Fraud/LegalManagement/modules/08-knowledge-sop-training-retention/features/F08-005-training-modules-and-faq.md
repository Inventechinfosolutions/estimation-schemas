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
1. Who creates: Administrator
2. How they create: Administrator publishes training content for Legal Research, Legal Writing, MS Word or MS Excel, and FAQ for the legal modules.
3. How they edit: A user opens the module or FAQ from the application.
4. How they send for approval: Classroom delivery is not included unless separately ordered. Publish content/FAQ → user opens from the application.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Training Module list
- FAQ browser
- Admin Publish form
- Topics: Legal Research, Legal Writing, MS Word, MS Excel; FAQ per legal modules
- Not instructor-led classroom; not a vendor LMS product

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Training Module list | Medium |
| FAQ browser | Medium |
| Admin Publish form | Medium |
| Training modules and faq history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Content publish operations | Medium |
| Update training modules and faq | Medium |
| Search training modules and faq | Medium |
| Read training modules and faq history | Easy |

### Inputs
Training content; topic; FAQ question/answer; target module; publish flag.

### Outputs
Published modules; FAQ entries.

### Business Rules
- In-application training/FAQ; classroom optional only if separately ordered.
- Per-module FAQ (Proceedings item 23).
- No generative-AI auto-FAQ.

### Validations
- Topic required; publish only with content; FAQ linked to a legal module id.

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
- Content authored by SPLOCA/vendor as agreed; not video-platform build.

### Risks
FAQ drift after feature changes.

### Non Functional Requirements
Open from the application; per-module access to FAQ.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Training Module list | UI | Medium | 6 |
| FAQ browser | UI | Medium | 6 |
| Admin Publish form | UI | Medium | 6 |
| Training modules and faq history | UI | Medium | 6 |
| Content publish operations | API | Medium | 6 |
| Update training modules and faq | API | Medium | 6 |
| Search training modules and faq | API | Medium | 6 |
| Read training modules and faq history | API | Easy | 4 |
| Training modules and faq persistence | DB | Medium | 4 |
| In-app content retrieve | Integration | Simple | 4 |
| Training modules and FAQ feature tests | Testing | Medium | 6 |
| Training modules and FAQ implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
