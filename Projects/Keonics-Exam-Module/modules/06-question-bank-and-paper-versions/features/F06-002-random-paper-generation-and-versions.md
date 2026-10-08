# F06-002 — Random Paper Generation and Versions

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Random Paper Generation and Versions |
| **Module** | 06 — Question Bank and Paper Versions |

### Description
Generate examination papers by randomly selecting the required count of questions from the eligible active pool according to examination configuration (including per-category counts if required), and produce multiple versions (A/B/C/D) with randomised question order and answer-option order while preserving correct-answer mapping for evaluation.

### Business Objective
Deliver fair, non-identical paper versions for centre-based CBT without breaking scoring integrity.

### Actors
Maker: Examination Administrator (generate/publish papers). Approver: none in baseline (publish is admin action). Auditor: Examination Administrator via generation history. Downstream: Module 07 consumes published versions; Module 08 evaluates using preserved keys.

### User Journey
1. Who creates: Examination Administrator for a configured examination/schedule paper set.
2. How they create: Paper generation config → set required counts (overall and per-category if required) and version set (A/B/C/D) → confirm run → system selects random eligible questions → builds versions with shuffled order/options → preview → validate answer-key integrity → publish for exam use.
3. How they edit: Regenerating creates a new paper set version; published sets used in live sessions are not silently mutated; withdraw/replace follows controlled republish with audit.
4. How they send for approval: Does not apply — no checker inbox for paper publish in baseline.
5. How the approver sees pending items: No approver inbox; generated papers register shows draft vs published sets.
6. How the approver decides: No second-person decision; administrator publishes after integrity check.
7. How the applicant / maker sees history: Administrator views paper generation history and version previews; candidates never see bank keys — they only see their assigned version in Module 07.
8. How the approver / auditor sees history: Generation history retains parameters, version identifiers, actor and integrity-check outcomes.

### Functional Capabilities
- Read examination configuration for required question counts and versioning rules (Module 03 parameters).
- Select randomly from eligible **active** questions only.
- Honour per-category counts when configured.
- Generate multiple versions A/B/C/D (or configured set).
- Randomise question order per version.
- Randomise answer-option order per question per version.
- Preserve correct-answer mapping through all shuffles.
- Preview versions for administrative review (keys protected).
- Run answer-key integrity validation before publish.
- Publish paper set for examination conduct consumption.
- Block generation when pool is insufficient for requested counts.
- Prevent deactivated questions from selection.
- Audit generation parameters, outputs and publish events.
- Register of generated paper sets searchable by examination/schedule.

### UI Screens
| Screen | Purpose |
|---|---|
| Paper generation configuration screen | Counts, categories, version set |
| Paper generation run confirmation screen | Confirm before random draw |
| Multi-version paper preview screen (A/B/C/D) | Admin preview of shuffled versions |
| Answer-key integrity check view | Confirm mapping preserved |
| Generated papers register | List paper sets and publish state |
| Paper generation history screen | Parameters and outcomes audit |

### Logical API operations
| Operation | Purpose |
|---|---|
| Configure paper generation parameters | Persist/run configuration for a set |
| Generate randomised paper versions | Select questions and build A/B/C/D |
| Preview paper version | Return admin preview payload |
| Validate answer-key mapping integrity | Verify keys after shuffle |
| Publish papers for examination | Make set available to Module 07 |
| Get paper generation history | Return generation/publish audit |

### Inputs
Examination configuration; required counts; category constraints; version labels; eligible active question pool; publish action; administrator identity.

### Outputs
Generated paper versions with shuffled items/options; preserved answer keys; integrity result; published set reference; history events.

### Business Rules
- Generated paper must match configured number of questions and marks.
- Different versions present different orders while preserving scoring correctness.
- Deactivated questions are never selected for new papers.
- Live published sets are immutable; replacement is a new generation/publish cycle.
- Candidates receive only their assigned version at conduct time (Module 07).

### Validations
- Pool sufficiency per category and overall.
- Version count within configured maximum.
- Integrity check must pass before publish.
- Only active questions eligible.

### Calculations
Total marks of generated paper; remaining pool counts; shuffle permutation mapping for keys.

### Workflow
Configure → generate → preview → integrity validate → publish → available to Module 07. No checker inbox.

### Search Requirements
By examination, schedule, generation date, publish status, version label.

### Documents
None (paper artefacts are system-generated content packages).

### Reports
Generation sufficiency / version publish status feed Module 09.

### Notifications
Optional admin alert on insufficient pool; candidate-facing none.

### Security
Answer keys never exposed to candidates, centre users or invigilators; admin preview tightly authorised; audited access to key integrity views.

### Integrations
None.

### Dependencies
F06-001 question bank; Module 03 examination parameters; consumed by Modules 07 and 08.

### Assumptions
- Version set defaults to A/B/C/D unless Department configures fewer/more within design limits.
- Randomisation algorithm quality is enterprise-grade; seeded auditability included in Very High generation API/DB.
- Hours vary from F06-001; each screen/API independently estimated.

### Risks
Insufficient category pools force repeated failed generation; weak key mapping bugs cause mass scoring errors.

### Non Functional Requirements
Deterministic audit of shuffle mapping; strong key confidentiality; generation performance for full bank scans; integrity validation mandatory before publish.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Paper generation configuration screen | UI | Complex | 12 |
| Paper generation run confirmation screen | UI | Medium | 6 |
| Multi-version paper preview screen (A/B/C/D) | UI | Very High | 16 |
| Answer-key integrity check view | UI | Complex | 12 |
| Generated papers register | UI | Medium | 6 |
| Paper generation history screen | UI | Easy | 4 |
| Configure paper generation parameters | API | Medium | 6 |
| Generate randomised paper versions | API | Very High | 16 |
| Preview paper version | API | Medium | 6 |
| Validate answer-key mapping integrity | API | Complex | 8 |
| Publish papers for examination | API | Complex | 8 |
| Get paper generation history | API | Easy | 4 |
| Paper version and answer-key mapping persistence | Database | Very High | 10 |
| Random paper generation and versions tests | Testing | Very High | 12 |
| Random paper generation and versions documentation | Documentation | Complex | 4 |

**Feature total: 130 hours**

### Estimation Assumptions
- Generate randomised paper versions API billed Very High (workflow/engine class).
- DB Very High for versioned shuffle maps and key integrity structures.
- Live exam delivery UI remains Module 07.
