# F03-004 — Examination Parameter Configuration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-004 |
| **Feature Name** | Examination Parameter Configuration |
| **Module** | 03 — Examination, Centre and Fee Masters |

### Description
Examination Administrators configure per-examination parameters without code change for approved rule sets: examination duration, question counts, marks, passing criteria, negative marking (if applicable), randomisation flags, paper versions (e.g. A/B/C/D), candidate instructions, and result and certificate eligibility rules. Parameters attach to an examination in the catalogue (F03-001). These settings drive later question-paper generation (Module 06), CBT timer and interface (Module 07), evaluation (Module 08), and certificate issuance eligibility. Opening an examination for registration may depend on parameters being complete per Department readiness rules.

### Business Objective
Allow Department-approved examination behaviour (duration, scoring, randomisation, versions, instructions, result/certificate eligibility) to be configured per examination so operations do not require software changes for each exam cycle.

### Actors
Examination Administrator (parameter owner); downstream modules (consume parameters); Auditor (read-only parameter history).

### User Journey
1. Who creates: Examination Administrator with examination-parameter privilege opens an existing catalogue examination and creates its parameter pack.
2. How they create: Open Examination parameter workspace for selected examination → enter duration, total questions, marks per question/total marks, pass marks/percentage, negative marking flag and value → set randomisation flags and allowed versions → enter instructions → set result publication and certificate eligibility rules → save Draft → Mark Ready/Active for use.
3. How they edit: Re-open parameter workspace → revise values before papers are generated or as Department allows post-lock rules → save; locked parameters after paper generation or live session may be restricted to non-breaking fields only.
4. How they send for approval: Submit/approval does not apply by default; Administrator marks parameters Ready. No candidate approval.
5. How the approver sees pending items: There is no approver inbox; Incomplete vs Ready parameter status appears on the parameter workspace and catalogue readiness indicators.
6. How the approver decides: There is no separate approval decision; Ready is an administrative completeness mark. Result publication timing decisions at exam cycle may be operated later in Module 08 using these rules.
7. How the applicant / maker sees history: Administrator opens parameter change history (who changed duration, pass rules, randomisation, eligibility, when).
8. How the approver / auditor sees history: Auditor opens the same history to verify that evaluation and certificate outcomes matched the configured rules.

### Functional Capabilities
- Configure examination duration (minutes) used by CBT timer.
- Configure question counts (total and per category/section if required).
- Configure marks scheme and total marks.
- Configure passing criteria (marks and/or percentage).
- Configure negative marking applicability and per-wrong deduction if enabled.
- Configure randomisation flags (question order, option order) without breaking answer-key mapping expectations for Module 06.
- Configure allowed paper versions (A/B/C/D or Department set).
- Maintain candidate-facing instructions text for hall ticket/CBT as applicable.
- Configure result publication field rules and certificate eligibility (e.g. pass-only).
- Validate parameter consistency (e.g. question count × marks aligns to total where required).
- Mark parameter pack Ready/Incomplete; block dependent generation when Incomplete if configured.
- Provide parameter summary view for quick operational check before opening registration or scheduling.
- Audit all parameter changes with before/after values.
- Prevent unsafe edits after papers generated / session live except Department-allowed fields.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Examination parameter workspace (tabbed) | Very High |
| Duration, questions, marks and pass criteria form | Complex |
| Negative marking and scoring options panel | Medium |
| Randomisation and version flags panel | Medium |
| Instructions editor | Medium |
| Result and certificate eligibility rules | Complex |
| Parameter readiness summary | Easy |
| Parameter change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save examination parameters | Complex |
| Configure randomisation and version flags | Complex |
| Configure result and certificate eligibility | Complex |
| Validate parameter consistency | Medium |
| Mark parameters Ready or Incomplete | Medium |
| Load parameters by examination | Medium |
| Enforce parameter edit lock rules | Medium |
| Read parameter change history | Easy |

### Inputs
Examination reference; duration; question counts; marks; pass criteria; negative marking flag/value; randomisation flags; version list; instructions text; result field publication rules; certificate eligibility rules; readiness status; remarks.

### Outputs
Persisted parameter pack; Ready/Incomplete status; consistency validation results; parameter summary; change history; configuration consumed by Modules 06–08.

### Business Rules
- Examination parameters are configurable without code change for approved rule sets.
- Randomisation flags must never imply that correct-answer mapping can be broken (Module 06 preserves keys).
- Certificate eligibility rules here define who may receive certificates (e.g. pass only); issuance is Module 08.
- Duration drives CBT timer; changing duration after live sessions start is restricted.
- Incomplete parameter packs may block Open for registration or paper generation when readiness policy is enabled.
- One Active parameter pack per examination version/cycle as Department defines (default one current pack per examination).

### Validations
- Duration > 0; question counts > 0; marks and pass criteria within sensible bounds.
- If negative marking enabled, deduction value mandatory and ≥ 0.
- At least one paper version when multi-version flag enabled.
- Instructions mandatory before Ready if Department requires.
- Consistency: configured question counts and marks must satisfy total-marks rule where defined.
- Certificate eligibility cannot reference undefined pass rule.

### Calculations
Derived total marks from question count × mark per question when that model is used; pass percentage from pass marks / total marks; readiness checklist score (complete/incomplete counts).

### Workflow
Select examination → configure parameter sections → validate consistency → Mark Ready → consumed by paper generation, CBT, evaluation, certificates. No maker–checker inbox by default. Edit lock after generation/live as configured.

### Search Requirements
Load by examination code/name; history by date and actor; filter examinations with Incomplete parameters.

### Documents
Instructions may be stored as rich text; no separate document upload required in SOW for parameters.

### Reports
Parameter readiness report (examinations Incomplete vs Ready) for Administrator go-live checks.

### Notifications
Optional alert to Administrators when parameters marked Ready or when Incomplete blocks open registration (Module 09); not mandatory for core configuration.

### Security
Only parameter-privileged Administrators may mutate; read access for other Administrators as needed; candidates never edit parameters; all changes audited; edit locks prevent tampering after paper/session freeze points.

### Integrations
None for this feature.

### Dependencies
F03-001 Examination Catalogue (examination must exist). Consumed by Module 06 (random paper/versions), Module 07 (timer/interface), Module 08 (evaluation, results, certificates).

### Assumptions
- Subjective marking remains out of scope; parameters target objective CBT.
- Approved rule sets mean Department-agreed fields above—not arbitrary scripting.
- Hours use Estimation Master; parameter workspace is Very High (tabbed multi-section configuration).
- Each named screen and logical API billed independently.

### Risks
- Inconsistent marks vs question counts cause evaluation errors.
- Changing randomisation or versions after papers issued could invalidate answer keys if edit locks are weak.
- Missing certificate eligibility rules could issue certificates to ineligible candidates in Module 08.

### Non Functional Requirements
Parameter load for CBT start must be fast and reliable; configuration UI usable for Administrators under exam-cycle pressure; audit history complete for scoring disputes; consistency validation must run before Ready.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Examination parameter workspace (tabbed) | UI | Very High | 16 |
| Duration, questions, marks and pass criteria form | UI | Complex | 12 |
| Negative marking and scoring options panel | UI | Medium | 6 |
| Randomisation and version flags panel | UI | Medium | 6 |
| Instructions editor | UI | Medium | 6 |
| Result and certificate eligibility rules | UI | Complex | 12 |
| Parameter readiness summary | UI | Easy | 4 |
| Parameter change history | UI | Medium | 6 |
| Save examination parameters | API | Complex | 8 |
| Configure randomisation and version flags | API | Complex | 8 |
| Configure result and certificate eligibility | API | Complex | 8 |
| Validate parameter consistency | API | Medium | 6 |
| Mark parameters Ready or Incomplete | API | Medium | 6 |
| Load parameters by examination | API | Medium | 6 |
| Enforce parameter edit lock rules | API | Medium | 6 |
| Read parameter change history | API | Easy | 4 |
| Examination parameter persistence | DB | Complex | 6 |
| Examination parameter feature tests | Testing | Very High | 12 |
| Examination parameter implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **142** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- No Integration row — no external channel.
- Testing is Very High due to scoring, randomisation, readiness and edit-lock combinations.
- Downstream paper generation and evaluation effort remain in Modules 06 and 08.
