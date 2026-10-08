# ChatGPT Visualization Brief — Module 10: Evaluation & Results

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 10 Evaluation & Results
**Features:** 5 (F10-001 … F10-005)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 10 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Post-submit evaluation → scoring → publication pipeline
2. Pass/fail + negative marking calculation diagram
3. Publication governance (WITHHELD → PUBLISHED) state machine
4. Candidate portal result access sequence
5. Results ERD
6. Feature relationship / dependency graph within this module and to other modules
7. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Evaluation & Results
**Purpose:** Automatic objective evaluation, scoring and pass/fail, rule alignment with Module 04 config, governed result publication, candidate portal result access.

**Actors (union across features):**
- Candidate
- Examination Administrator

**Feature list:**
- **F10-001** — Post-Submission Objective Answer Evaluation
- **F10-002** — Examination Scoring and Pass Fail Determination
- **F10-003** — Evaluation Rules Configuration Alignment
- **F10-004** — Governed Result Publication and Display Rule Enforcement
- **F10-005** — Candidate Portal Examination Result Access

### DATA MODEL (from EXAM DB design v2.1)

- `evaluation_run`
- `score_result`
- `evaluation_rule_alignment`
- `result_publication`
- `candidate_result`

### FEATURE CATALOGUE

#### F10-001 — Post-Submission Objective Answer Evaluation

**One-liner / description:** Automatically evaluates a candidate's locked objective examination responses immediately after submission by matching each recorded response against the configured answer key for the candidate's assembled question…

**Business objective:** Eliminate manual marking delay for objective examinations by producing auditable evaluation outcomes at submission time so downstream scoring, pass/fail determination, and governed publication can proceed without administrator intervention.

**Actors:** Examination Administrator; Candidate

**User journey (12 steps):**
1. Candidate completes secure examination conduct in Module 09 and submits responses, triggering response lock.
2. System receives submission-completed signal with candidate session, examination, and assembled paper version identifiers.
3. System validates that the session is in SUBMITTED state and that no prior successful evaluation exists for the same submission.
4. System loads the answer key aligned to the candidate's question paper version from Module 04 configuration.
5. System iterates each objective question on the paper and compares the candidate's selected or entered response to the configured correct answer(s).
6. System classifies each item as CORRECT, INCORRECT, or UNANSWERED according to examination evaluation rules.
7. System persists per-question evaluation outcomes and aggregate counts (correct, incorrect, unanswered).
8. System transitions evaluation status from PENDING to EVALUATED on success or to EVALUATION_FAILED on unrecoverable error.
9. Examination Administrator opens the evaluation monitoring register, filters by examination or session, and reviews evaluation status for submitted candidates.
10. Administrator opens evaluation detail to view per-question outcome summary without editing candidate responses.
11. If evaluation failed, Administrator reviews failure reason and initiates retry after underlying data issue is resolved.
12. On successful evaluation, system hands off to scoring feature for marks and pass/fail calculation.

**Functional capabilities:**
- Accept post-submission evaluation trigger only for locked objective examination sessions
- Resolve answer key for the candidate's specific assembled question paper version
- Compare single-select objective responses against configured correct option
- Compare multi-select objective responses against configured correct option set with partial-match rules from examination configuration
- Classify blank or null responses as UNANSWERED
- Classify non-blank responses that do not match the key as INCORRECT
- Persist per-question evaluation outcome with question identifier and outcome code
- Persist aggregate correct, incorrect, and unanswered counts for the submission
- Enforce idempotent evaluation so duplicate submission signals do not create duplicate evaluation records
- Record evaluation start time, completion time, and triggering submission reference
- Expose evaluation status lifecycle for administrator monitoring
- Support administrator-initiated retry for failed evaluations after corrective action

**Inputs:** Submitted examination session identifier; Candidate identifier; Examination identifier; Assembled question paper version identifier; Locked candidate response set per question; Answer key per question from examination configuration; Examination evaluation rules reference from Module 04; Submission timestamp and submission lock reference from Module 09

**Outputs:** Evaluation record with status PENDING, EVALUATED, or EVALUATION_FAILED; Per-question outcome list (CORRECT, INCORRECT, UNANSWERED); Aggregate correct count; Aggregate incorrect count; Aggregate unanswered count; Evaluation failure reason code and message when applicable; Evaluation completion timestamp

**Business rules:**
- Evaluation runs automatically immediately after submission wherever the examination type is objective and auto-evaluation is enabled in examination configuration
- Subjective or manually marked items are out of scope and must not be auto-evaluated
- Each submission produces at most one successful evaluation record; retries replace or supersede failed attempts per policy without duplicating successful outcomes
- UNANSWERED applies when no response is recorded for a mandatory objective item
- Evaluation must use the answer key tied to the candidate's paper version, not a generic examination-level key
- Evaluation cannot proceed if submission locking from Module 09 is incomplete

**Validations:**
- Submission session must exist and be in SUBMITTED state
- Response lock flag must be true before evaluation starts
- Assembled paper version identifier must be present and resolvable
- Answer key must exist for every objective question on the paper
- Question type must be objective; non-objective items are skipped or cause controlled failure based on examination configuration flag
- Duplicate evaluation request for an already EVALUATED submission must be rejected
- Retry is permitted only when current evaluation status is EVALUATION_FAILED

**Workflow / states:** Submission SUBMITTED → Evaluation PENDING → Evaluation EVALUATED on success; Submission SUBMITTED → Evaluation PENDING → Evaluation EVALUATION_FAILED on error; Evaluation EVALUATION_FAILED → Evaluation PENDING on administrator retry → Evaluation EVALUATED or EVALUATION_FAILED

**Dependencies:**
- F09 — Secure Examination Conduct: Examination Submission and Response Locking
- F04 — Question Bank and Examination Configuration: Question Bank Item Lifecycle and Answer Key Management
- F04 — Question Bank and Examination Configuration: Multiple Question Paper Version and Randomisation Settings
- F04 — Question Bank and Examination Configuration: Examination Master Configuration
- F01 — User and Role Management: Downstream Module Authorization Integration Hooks

**Risks:** Paper version mismatch between assembled paper and answer key could cause incorrect classification; High concurrent submission volume at session end may require queueing not described in source document; Partial multi-select scoring nuances depend on Module 04 rule completeness

**Notes:** Triggers immediately after examination submission from Module 09 wherever applicable; objective-type items only.

---

#### F10-002 — Examination Scoring and Pass Fail Determination

**One-liner / description:** Calculates marks awarded per question, applies negative marking and examination-level scoring rules from configuration, derives total score, maximum marks, percentage, and pass or fail status for each evaluated…

**Business objective:** Provide consistent, rule-driven scoring and pass/fail outcomes aligned to each examination's configured marking scheme so results reflect department policy without manual calculation.

**Actors:** Examination Administrator; Candidate

**User journey (12 steps):**
1. System receives evaluation-completed event with per-question CORRECT, INCORRECT, and UNANSWERED outcomes.
2. System loads examination scoring configuration including per-question marks, negative mark value, and pass threshold from Module 04.
3. For each question, system applies marks for CORRECT responses per configured weight.
4. For each INCORRECT response where negative marking is enabled, system deducts configured negative marks floored at zero total per question policy.
5. For UNANSWERED responses, system applies zero marks unless configuration specifies alternate treatment.
6. System sums awarded marks and deducts aggregate negative marks to produce total score.
7. System calculates maximum attainable marks from the objective paper configuration.
8. System calculates percentage as total score divided by maximum marks rounded per configuration precision.
9. System compares percentage or absolute score against configured pass threshold to set PASS or FAIL status.
10. System persists score summary linked to the evaluation record.
11. Examination Administrator opens score summary on evaluation detail to review marks breakdown and pass/fail outcome.
12. Score summary becomes input to result publication when display rules include marks or pass/fail fields.

**Functional capabilities:**
- Load per-question mark weight from examination configuration
- Apply full marks for CORRECT outcomes per question weight
- Apply zero marks for UNANSWERED outcomes unless alternate rule configured
- Apply configured negative mark deduction for INCORRECT outcomes when negative marking enabled
- Enforce per-question floor preventing negative question score where configured
- Sum total score across all evaluated objective questions
- Calculate maximum marks from configured question weights on the paper
- Calculate percentage with configured decimal precision
- Determine PASS or FAIL against configured cut-off threshold
- Persist score summary linked to evaluation record
- Expose read-only score breakdown to authorized administrators
- Block scoring when evaluation status is not EVALUATED

**Inputs:** Evaluation record with EVALUATED status; Per-question outcome codes from evaluation; Per-question mark weight from examination configuration; Negative marking enabled flag and negative mark value; Pass threshold percentage or absolute score from examination configuration; Percentage rounding precision from examination configuration

**Outputs:** Per-question marks awarded; Per-question negative marks deducted where applicable; Total score; Maximum marks; Percentage score; Pass or fail status flag; Scoring completion timestamp

**Business rules:**
- Scoring executes automatically immediately after successful objective evaluation
- Negative marks apply only when negative marking is enabled for the examination
- Total score cannot fall below zero for the examination unless configuration explicitly allows
- Pass/fail uses examination-configured threshold; absent threshold defaults to policy defined in Module 04 configuration
- UNANSWERED items score zero marks in default configuration
- Scoring uses only objective items evaluated in F10-001

**Validations:**
- Evaluation must be in EVALUATED status before scoring starts
- Per-question mark weight must be non-negative numeric
- Negative mark value must be non-negative when negative marking enabled
- Pass threshold must be within valid percentage range 0–100 when percentage-based
- Maximum marks must be greater than zero for percentage calculation
- Duplicate scoring request for already scored evaluation must return existing summary without recalculation unless administrator override defined out of scope

**Workflow / states:** Evaluation EVALUATED → Scoring PENDING → Scoring COMPLETED with PASS or FAIL outcome; Scoring blocked when evaluation not EVALUATED

**Dependencies:**
- F10-001 — Post-Submission Objective Answer Evaluation
- F04 — Question Bank and Examination Configuration: Examination Master Configuration
- F04 — Question Bank and Examination Configuration: Result Display, Certificate Eligibility and Examination Fee Configuration

**Risks:** Configuration change after evaluation could cause inconsistency if scores are not snapshotted at evaluation time; Floating-point rounding discrepancies may affect borderline pass/fail unless fixed precision enforced

**Notes:** Consumes evaluation outcomes from F10-001; applies marks and pass rules from Module 04 examination configuration.

---

#### F10-003 — Evaluation Rules Configuration Alignment

**One-liner / description:** Ensures automatic evaluation and scoring in Module 10 honour examination-specific evaluation rules configured in Module 04, including auto-evaluation eligibility, negative marking parameters, unanswered handling,…

**Business objective:** Guarantee that post-submission evaluation behaviour matches each examination's approved configuration so departments can vary policies per examination without code changes.

**Actors:** Examination Administrator

**User journey (11 steps):**
1. Examination submission triggers evaluation pre-flight check.
2. System loads evaluation rules bundle for the examination from Module 04 configuration.
3. System verifies auto-evaluation is enabled for the examination type.
4. System verifies required scoring parameters exist including mark weights and pass threshold.
5. System applies unanswered-handling rule when classifying responses during evaluation handoff.
6. System applies partial-match rule flag for multi-select items during answer comparison handoff.
7. System applies negative marking enabled flag during scoring handoff.
8. System records configuration rule version or snapshot identifier on evaluation record for traceability.
9. If any mandatory rule is missing, system marks evaluation as EVALUATION_FAILED with configuration error reason.
10. Administrator views configuration alignment status on evaluation detail showing rule snapshot summary.
11. Administrator resolves missing configuration in Module 04 and retries failed evaluation from F10-001.

**Functional capabilities:**
- Load evaluation rules bundle by examination identifier at evaluation time
- Validate auto-evaluation enabled flag before starting evaluation
- Validate presence of answer key mapping for paper version before evaluation
- Validate presence of mark weights and pass threshold before scoring
- Apply unanswered handling rule during outcome classification
- Apply multi-select partial-match rule during answer comparison
- Apply negative marking enabled flag and value during scoring
- Persist configuration snapshot identifier on evaluation and score records
- Surface configuration misalignment errors to administrator on evaluation detail
- Reject evaluation when examination configuration is incomplete for objective auto-evaluation

**Inputs:** Examination identifier; Evaluation rules bundle from Module 04; Auto-evaluation enabled flag; Negative marking parameters; Unanswered handling rule; Multi-select partial-match rule; Pass threshold and mark weights

**Outputs:** Resolved rule set applied to evaluation and scoring pipeline; Configuration snapshot identifier stored on evaluation record; Configuration validation error codes when pre-flight fails

**Business rules:**
- Evaluation rules are read-only at evaluation time; changes occur only in Module 04
- Examination without auto-evaluation enabled must not enter objective auto-evaluation pipeline
- Rule snapshot reference must be stored with each evaluation for audit
- Missing mandatory scoring parameters block scoring and surface administrator-actionable errors

**Validations:**
- Auto-evaluation flag must be true for pipeline to proceed
- Mark weight must exist for every objective question on paper
- Pass threshold must be present when pass/fail determination is enabled
- Negative mark value required when negative marking flag is true
- Partial-match rule enum must be recognised value when multi-select questions present

**Workflow / states:** Configuration LOADED → Configuration VALIDATED → Evaluation PROCEED; Configuration LOADED → Configuration VALIDATION_FAILED → Evaluation EVALUATION_FAILED

**Dependencies:**
- F04 — Question Bank and Examination Configuration: Examination Master Configuration
- F04 — Question Bank and Examination Configuration: Result Display, Certificate Eligibility and Examination Fee Configuration
- F10-001 — Post-Submission Objective Answer Evaluation
- F10-002 — Examination Scoring and Pass Fail Determination

**Risks:** Undocumented rule combinations in Module 04 may not map cleanly to evaluation pipeline; Configuration drift between paper assembly and rule bundle could cause failures at scale

**Notes:** Applies evaluation and scoring rules authored in Module 04; does not duplicate configuration editing screens.

---

#### F10-004 — Governed Result Publication and Display Rule Enforcement

**One-liner / description:** Governs when evaluated examination results become visible to candidates by applying result publication controls and Module 04 display rules, including field-level masking of marks, counts, percentage, and pass/fail…

**Business objective:** Allow departments to control result release timing and visible content per examination policy while ensuring candidates see only approved fields after publication.

**Actors:** Examination Administrator; Candidate

**User journey (12 steps):**
1. System marks result record as EVALUATED_NOT_PUBLISHED after scoring completes.
2. Examination Administrator opens result publication register filtered by examination and publication status.
3. Administrator selects one or more evaluated results and reviews display rule preview for the examination.
4. Administrator confirms publish action for selected results.
5. System loads result display rules from Module 04 for the examination.
6. System snapshots applicable display rules onto the result publication record.
7. System transitions result status from EVALUATED_NOT_PUBLISHED to PUBLISHED and records publisher and timestamp.
8. Candidate portal result queries return published results only with fields masked per snapshotted display rules.
9. Administrator may select published results and confirm withhold action when policy allows retraction before certificate issuance.
10. System transitions result status from PUBLISHED to WITHHELD and records reason.
11. Candidate previously seeing result now receives not-published empty state on refresh.
12. Administrator may re-publish withheld result through publish action returning status to PUBLISHED.

**Functional capabilities:**
- Maintain result publication status separate from evaluation completion
- List evaluated results with publication status for administrator
- Publish individual evaluated result with display rule snapshot
- Bulk publish multiple results for an examination session
- Withhold published result with reason capture
- Load result display field visibility rules from Module 04
- Snapshot display rules at publish time for immutable candidate view
- Mask marks counts percentage pass/fail fields not enabled in display rules
- Block candidate access to unpublished results
- Record publication and withhold audit trail with actor and timestamp
- Preview effective candidate-visible fields before publish

**Inputs:** Evaluation and score summary from F10-002; Result display rules from Module 04; Administrator publish or withhold action; Withhold reason text when applicable; Examination and session filters for register

**Outputs:** Result publication record with status EVALUATED_NOT_PUBLISHED, PUBLISHED, or WITHHELD; Display rule snapshot attached to publication record; Publication timestamp and publishing administrator identifier; Withhold timestamp reason and actor when applicable; Candidate-visible field subset per display rules

**Business rules:**
- Candidates cannot view results until status is PUBLISHED
- Display rules configured in Module 04 determine which score fields appear after publication
- Display rule snapshot at publish time governs candidate view even if Module 04 rules later change
- Withhold removes candidate visibility but retains evaluation data for administrators
- Bulk publish limited to results in EVALUATED_NOT_PUBLISHED status
- Departmental report exports are out of scope

**Validations:**
- Publish permitted only when evaluation status is EVALUATED and scoring is complete
- Publish rejected when result already PUBLISHED unless idempotent acknowledge
- Withhold permitted only when current status is PUBLISHED
- Withhold reason required when department policy flag mandates
- Bulk publish selection must reject mixed examinations without confirmation per examination batch
- Display rules must resolve at least one visible field for candidate result view

**Workflow / states:** Result EVALUATED_NOT_PUBLISHED → PUBLISHED on administrator publish; Result PUBLISHED → WITHHELD on administrator withhold; Result WITHHELD → PUBLISHED on administrator re-publish

**Dependencies:**
- F10-002 — Examination Scoring and Pass Fail Determination
- F04 — Question Bank and Examination Configuration: Result Display, Certificate Eligibility and Examination Fee Configuration
- F01 — User and Role Management: Examination Administrator Account Lifecycle
- F07 — Notification Service: Examination Lifecycle Event Subscription and Template Routing

**Risks:** Accidental bulk publish without review could release results prematurely; Display rule snapshot divergence from live Module 04 rules may confuse administrators

**Notes:** Display field catalog configured in Module 04; this feature governs publication state and candidate-visible field masking.

---

#### F10-005 — Candidate Portal Examination Result Access

**One-liner / description:** Provides candidates authenticated through the candidate portal with a register and detail view of their published examination results, honouring Module 04 display rules for visible fields, and clear empty and error…

**Business objective:** Enable candidates to self-service view official examination outcomes online immediately after department publication without administrator manual distribution.

**Actors:** Candidate

**User journey (10 steps):**
1. Candidate logs into candidate portal using registered mobile OTP from platform login.
2. Candidate navigates to My Examination Results section from portal home.
3. System lists candidate's examinations with published results showing examination name, date, and pass/fail or summary per display rules.
4. Candidate selects one examination result row to open detail view.
5. System loads published result for authenticated candidate only.
6. System applies snapshotted display rules to show permitted fields such as total score, percentage, correct count, or pass/fail only.
7. Candidate reviews result detail and returns to list.
8. If result is evaluated but not yet published, list shows examination row with not published status and detail shows not available empty state.
9. If result was withheld after prior publication, detail shows result unavailable message.
10. If no examinations completed, list shows no results empty state.

**Functional capabilities:**
- List published examination results for authenticated candidate only
- Show examination name schedule date and high-level outcome per display rules in list
- Open result detail for selected published examination
- Render detail fields masked per snapshotted display rules from publication
- Show not published status for evaluated but unpublished examinations
- Show result unavailable state for withheld publications
- Show empty state when candidate has no completed examinations
- Prevent cross-candidate result access
- Support read-only mobile-friendly result layouts for candidate portal web access

**Inputs:** Authenticated candidate session; Published result records for candidate; Display rule snapshot from publication record; Examination metadata name and date from scheduling module

**Outputs:** Candidate result list with publication-aware status labels; Candidate result detail with field-level masked score summary; Empty and not available user messages

**Business rules:**
- Candidate may view only own results
- Unpublished evaluated results show status label but not score fields
- Withheld results behave as unavailable to candidate
- Field visibility strictly follows publication snapshot not live Module 04 edits
- Certificate download links are out of scope in this module

**Validations:**
- Candidate session must be valid and active
- Result detail request must match authenticated candidate identifier
- Non-published result detail requests return not available without score leakage
- Unknown examination identifier returns not found without revealing other candidates' data

**Workflow / states:** Candidate authenticated → Result list LOADED → Detail VIEW when PUBLISHED; Evaluated not published → NOT_AVAILABLE view; Withheld → UNAVAILABLE view

**Dependencies:**
- F10-004 — Governed Result Publication and Display Rule Enforcement
- F05 — Candidate Registration: candidate portal authentication context
- F06 — Examination Scheduling and Allocation: examination schedule metadata
- F04 — Question Bank and Examination Configuration: Result Display, Certificate Eligibility and Examination Fee Configuration

**Risks:** Overly permissive display rules could expose more detail than department intends; Candidate confusion when immediate evaluation occurs but publication delayed without clear not published messaging

**Notes:** Candidate OTP portal from registration module; shows only published results per F10-004 display rules.

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 10 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 10 Evaluation & Results** (5 features).
> Features: F10-001 Post-Submission Objective Answer Evaluation; F10-002 Examination Scoring and Pass Fail Determination; F10-003 Evaluation Rules Configuration Alignment; F10-004 Governed Result Publication and Display Rule Enforcement; F10-005 Candidate Portal Examination Result Access.
> Purpose: Automatic objective evaluation, scoring and pass/fail, rule alignment with Module 04 config, governed result publication, candidate portal result access.
> Draw: Post-submit evaluation → scoring → publication pipeline; Pass/fail + negative marking calculation diagram; Publication governance (WITHHELD → PUBLISHED) state machine; Candidate portal result access sequence; ERD for `evaluation_run`, `score_result`, `evaluation_rule_alignment`, `result_publication`, `candidate_result`.
