# ChatGPT Visualization Brief — Module 04: Question Bank & Examination Configuration

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 04 Question Bank & Examination Configuration
**Features:** 7 (F04-001 … F04-007)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 04 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Question taxonomy tree + bank lifecycle
2. Bulk import pipeline flowchart
3. Selection rules → pool depth → version count calculation diagram
4. Examination config layers (master / selection / randomisation / fee / result / cert)
5. Q-Bank ERD
6. Feature relationship / dependency graph within this module and to other modules
7. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Question Bank & Examination Configuration
**Purpose:** Manage question taxonomy and bank, bulk import, examination master, random selection rules, paper version/randomisation settings, and result/certificate/fee configuration.

**Actors (union across features):**
- Examination Administrator

**Feature list:**
- **F04-001** — Question Category & Taxonomy Management
- **F04-002** — Question Bank Item Lifecycle & Answer Key Management
- **F04-003** — Question Bank Bulk Import
- **F04-004** — Examination Master Configuration
- **F04-005** — Random Question Selection Rules
- **F04-006** — Multiple Question Paper Version & Randomisation Settings
- **F04-007** — Result Display, Certificate Eligibility & Examination Fee Configuration

### DATA MODEL (from EXAM DB design v2.1)

- `question_category`
- `question`
- `question_option`
- `question_import_batch`
- `examination`
- `examination_selection_rule`
- `examination_randomisation_setting`
- `examination_lifecycle_config`
- `examination_fee_rule`
- `conduct_security_policy`

### FEATURE CATALOGUE

#### F04-001 — Question Category & Taxonomy Management

**One-liner / description:** Examination Administrators maintain a hierarchical or flat catalogue of question categories used to classify bank items and to drive category-wise question counts during paper-generation rule configuration.

**Business objective:** Provide a controlled, reusable category structure so questions can be grouped consistently and random-selection rules can allocate counts per category without manual ad hoc tagging.

**Actors:** Examination Administrator

**User journey (1 steps):**
1. Administrator opens Question Categories from the Question Bank administration menu. 2. System displays the category register with search, status filter, and parent-category filter when hierarchy is enabled. 3. Administrator clicks Add Category. 4. Administrator enters category code, display name, optional description, optional parent category, and display order. 5. System validates uniqueness of code and name within the same parent scope. 6. Administrator saves; category transitions to Active. 7. Administrator returns to the register and verifies the new category appears with Active status chip. 8. Administrator selects an existing category and opens Edit. 9. Administrator updates name, description, parent, or display order but not code after first use. 10. System warns if the category is referenced by live questions or active examination rules before allowing parent change. 11. Administrator opens Deactivate and confirms; category transitions to Inactive and is excluded from new question assignment and new rule configuration. 12. Administrator views empty register state when no categories match filters.

**Functional capabilities:**
- Display paginated question category register with text search on code and name
- Filter category register by status Active or Inactive
- Filter category register by parent category when hierarchy is used
- Create question category with code, name, description, parent, and display order
- Edit question category metadata except immutable code after first save
- Deactivate category without deleting historical references
- Block deactivation when category is required by an active examination paper rule unless administrator reassigns dependencies first
- Show empty-state guidance when no categories exist or search returns no rows
- Show inline validation errors on create and edit forms
- Expose active category lookup for downstream question and rule screens

**Inputs:** Category code; Category display name; Optional description; Optional parent category identifier; Display order integer; Status selection on deactivate

**Outputs:** Category register list rows with code, name, parent, status, question count summary; Created or updated category record; Deactivation confirmation outcome; Active category lookup results for dependent screens

**Business rules:**
- Category code must be unique within the examination tenant scope
- Category name must be unique among siblings under the same parent
- Inactive categories cannot be assigned to new questions or new examination rules
- Existing questions and historical papers retain reference to inactive categories for audit
- Parent category cannot be a descendant of the current category
- Only Examination Administrator role may create, edit, or deactivate categories

**Validations:**
- Category code required, alphanumeric with optional hyphen, 2–20 characters
- Category name required, 3–100 characters, no leading or trailing whitespace
- Description optional, maximum 500 characters
- Display order required, non-negative integer, maximum 9999
- Parent category must reference an Active category when supplied
- Reject circular parent assignment
- Reject duplicate code on create
- Reject duplicate name under same parent on create and edit

**Workflow / states:** Draft-on-create → Active on successful save; Active → Inactive on administrator deactivate; Inactive remains terminal for new assignments; Active → Active on successful edit

**Dependencies:**
- F01 — Platform Role and Permission Catalog
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

**Risks:** Late category restructuring may require re-mapping questions and active paper rules; Large category trees may require pagination tuning in lookup dialogs used by question forms

**Notes:** Prerequisite taxonomy for question bank categorisation and category-wise paper rules in later features.

---

#### F04-002 — Question Bank Item Lifecycle & Answer Key Management

**One-liner / description:** Examination Administrators create, edit, deactivate, and manage individual question bank items including stem text, options, marks, category assignment, difficulty metadata where applicable, and authoritative answer…

**Business objective:** Maintain a sufficient, quality-controlled pool of examination questions with correct marking keys so downstream random-selection and multi-version paper rules can draw from a validated bank.

**Actors:** Examination Administrator

**User journey (1 steps):**
1. Administrator opens Question Bank register. 2. System lists questions with search, category filter, status filter, and marks range filter. 3. Administrator clicks Add Question. 4. Administrator selects question type such as single-correct MCQ, multiple-correct MCQ, or true/false as supported by scope. 5. Administrator enters question stem, assigns category, enters marks, and optionally difficulty label. 6. Administrator adds answer options with option text and marks-as-key indicators per type rules. 7. Administrator designates correct answer key mapping for scorable types. 8. System validates minimum options, key completeness, and positive marks. 9. Administrator saves; question transitions to Active. 10. Administrator opens a question from the register in read-only preview. 11. Administrator opens Edit on an Active question, updates stem, options, marks, category, or answer key. 12. System warns if the question is referenced by active examination configurations before destructive option removal. 13. Administrator opens Deactivate, confirms, and question transitions to Inactive. 14. Inactive questions remain visible in register with Inactive chip but cannot be assigned to new paper rules. 15. Administrator views register empty state when filters yield no results.

**Functional capabilities:**
- Display paginated question bank register with text search on stem snippet and question identifier
- Filter register by category, status, question type, and marks range
- Create single-correct MCQ question with stem, options, marks, category, and answer key
- Create multiple-correct MCQ question with partial-key rules as configured
- Create true/false question with binary options and answer key
- Edit existing question content, marks, category, options, and answer key
- Read-only question preview with formatted stem and options
- Deactivate question without physical delete
- Block assignment of inactive questions to new examination paper rules
- Show dependency warning when editing questions referenced by active examinations
- Maintain authoritative answer key separate from display option order
- Show empty and error states on register and forms

**Inputs:** Question type; Question stem rich text or plain text; Category selection; Marks value; Optional difficulty label; Answer option rows with option label and text; Correct answer key selection per question type; Status on deactivate

**Outputs:** Question register rows with identifier, type, category, marks, status, last modified metadata; Created or updated question and answer key records; Read-only preview rendering; Deactivation outcome and dependency warnings

**Business rules:**
- Each question belongs to exactly one active category at creation time
- Marks must be greater than zero for scorable questions
- Single-correct MCQ must have exactly one designated correct option in the answer key
- Multiple-correct MCQ must have at least one correct option and at least one incorrect option
- True/false questions must have exactly two options
- Inactive questions remain in bank history and prior paper definitions but are excluded from new rule pools
- Answer key is authoritative for evaluation modules; display order may differ after randomisation at runtime
- Only Examination Administrator role may manage question bank items

**Validations:**
- Question stem required, minimum 10 characters, maximum configurable upper bound such as 2000 characters
- Category required and must reference Active category
- Marks required, positive numeric, maximum two decimal places, upper bound per department policy field
- Minimum option count per type: at least four for MCQ unless policy allows three
- Option text required for each option row, non-duplicate within the question
- Answer key must reference valid option identifiers for the question
- Reject save when no correct option is designated for scorable types
- Reject duplicate question stem hash within same category when duplicate detection is enabled

**Workflow / states:** Draft-on-create → Active on successful save; Active → Active on edit; Active → Inactive on deactivate; Inactive terminal for new pool inclusion

**Dependencies:**
- F04-001 — Question Category & Taxonomy Management
- F01 — Platform Role and Permission Catalog
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

**Risks:** Answer key errors propagate to scoring in Module 10; Editing questions after examinations are scheduled may affect consistency unless configurations are locked elsewhere

**Notes:** Core question bank administration excluding bulk import handled in F04-003.

---

#### F04-003 — Question Bank Bulk Import

**One-liner / description:** Examination Administrators import batches of questions from a structured file template into the question bank with pre-commit validation, row-level error reporting, and controlled activation of successfully validated…

**Business objective:** Accelerate establishment of a deep question pool required for randomisation and multiple paper versions while preserving data quality through validation before commit.

**Actors:** Examination Administrator

**User journey (1 steps):**
1. Administrator opens Question Bank Import from the administration menu. 2. System displays import history register with batch status, uploaded by, row counts, and timestamps. 3. Administrator clicks New Import. 4. Administrator downloads the approved import template reference document link shown on screen. 5. Administrator uploads completed file selecting target default category and question type constraints if applicable. 6. System parses file and transitions batch to Validating. 7. Administrator views validation preview grid listing each row with pass/fail indicator and error messages. 8. Administrator filters preview to failed rows only. 9. Administrator corrects source file offline and re-uploads or excludes failed rows per policy. 10. Administrator clicks Commit Valid Rows when at least one row passed validation. 11. System creates Active questions and answer keys for valid rows and marks batch Committed. 12. Administrator downloads error report file for failed rows. 13. Administrator opens a committed batch detail read-only view showing created question identifiers. 14. Administrator views empty import history state on first use.

**Functional capabilities:**
- Display import batch history register with status and counts
- Upload structured import file against template constraints
- Parse and validate each row for required fields, category reference, marks, options, and answer key
- Show validation preview grid with row numbers and error messages
- Filter validation preview to failed rows
- Commit only validated rows into Active questions
- Generate downloadable error report for failed rows
- Show import batch detail with created question cross-reference
- Prevent commit when zero rows pass validation
- Record importing administrator and batch metadata for audit

**Inputs:** Import file in approved template format; Optional default category for rows missing explicit category code; Optional default question type when uniform per file; Commit confirmation action; Re-upload replacement file for same draft batch when supported

**Outputs:** Import batch record with status Validating, Committed, or Failed; Row-level validation results; Created question identifiers for committed rows; Downloadable error report artifact; Import history register rows

**Business rules:**
- Only validated rows are persisted as Active questions on commit
- Failed rows never partially create question records
- Category codes in file must resolve to Active categories
- Duplicate question stems within the same import batch are rejected
- Committed batches are immutable; corrections require new import or manual edit via F04-002
- Maximum row count per batch governed by configured enterprise limit
- Import does not auto-link questions to examination rules; administrator configures rules separately

**Validations:**
- File format must match approved template columns and encoding
- Reject empty file upload
- Row-level stem required and length within limits
- Row-level category code must exist and be Active
- Row-level marks must be positive numeric
- Row-level options must meet minimum count for declared type
- Row-level answer key must map to provided option labels
- Reject rows referencing inactive categories

**Workflow / states:** Uploaded → Validating → ValidationComplete → Committed; Uploaded or Validating → Failed on fatal parse error; Committed is terminal

**Dependencies:**
- F04-001 — Question Category & Taxonomy Management
- F04-002 — Question Bank Item Lifecycle & Answer Key Management
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

**Risks:** Bulk import of incorrect answer keys affects scoring at scale; Very large files may require batch size tuning for validation performance

**Notes:** Bulk load path for initial bank population; does not include runtime paper generation.

---

#### F04-004 — Examination Master Configuration

**One-liner / description:** Examination Administrators define and maintain examination master records specifying examination identity, duration, total marks structure reference, passing criteria, negative marking policy, and candidate-facing…

**Business objective:** Centralise authoritative examination parameters so registration, scheduling, secure conduct, and evaluation consume consistent duration, marking, and pass rules.

**Actors:** Examination Administrator

**User journey (1 steps):**
1. Administrator opens Examination Master register. 2. System lists examinations with search, status filter, and code filter. 3. Administrator clicks Create Examination. 4. Administrator enters examination code, name, description, duration in minutes, total marks, passing marks or passing percentage mode, negative marking enabled flag, negative mark deduction value, and instructions text. 5. System validates numeric relationships between total and passing marks. 6. Administrator saves; examination transitions to Draft. 7. Administrator reviews Draft examination in read-only summary. 8. Administrator clicks Activate; examination transitions to Active when mandatory fields are complete. 9. Downstream modules may reference Active examinations only. 10. Administrator opens Edit on Draft or Active examination to adjust instructions or marking parameters subject to lock rules. 11. Administrator deactivates examination when retires; transitions to Inactive. 12. Administrator sees empty register state when no examinations exist.

**Functional capabilities:**
- Display examination master register with search and status filters
- Create examination master with duration, marks, pass criteria, negative marking, and instructions
- Edit examination master fields with state-aware restrictions
- Read-only examination summary view
- Activate examination when configuration is complete
- Deactivate examination without deleting historical reference
- Enforce negative marking parameters only when feature enabled
- Show validation errors for inconsistent marks configuration
- Expose Active examination lookup to downstream modules
- Show empty register state

**Inputs:** Examination code; Examination name; Optional description; Duration minutes; Total marks; Passing marks or passing percentage according to selected mode; Negative marking enabled flag; Negative mark deduction value per wrong answer when enabled

**Outputs:** Examination master register rows; Draft, Active, or Inactive examination records; Read-only summary for confirmation; Active examination lookup results

**Business rules:**
- Examination code unique within tenant scope
- Passing threshold cannot exceed total marks
- Negative marking deduction applies only when negative marking enabled
- Inactive examinations cannot be selected for new schedules or registrations
- Historical schedules retain reference to examination version effective at activation time
- Instructions text published to candidate-facing artefacts by downstream modules
- Only Examination Administrator may manage examination master records

**Validations:**
- Examination code required, unique, alphanumeric 3–20 characters
- Examination name required, 5–150 characters
- Duration required, positive integer minutes within configured maximum
- Total marks required, positive numeric with up to two decimals
- Passing marks required when mode is absolute marks and must be less than or equal to total marks
- Passing percentage required when mode is percentage and must be between 1 and 100
- Negative deduction value required and positive when negative marking enabled
- Instructions optional, maximum length per policy such as 4000 characters

**Workflow / states:** Draft on create → Active on activate; Active → Active on edit where permitted; Active → Inactive on deactivate; Draft → Inactive on cancel draft if supported

**Dependencies:**
- F01 — Platform Role and Permission Catalog
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

**Risks:** Changing passing or negative marking after registrations may affect candidate expectations; Missing instructions content impacts hall ticket and conduct modules

**Notes:** Examination definition master only; scheduling, conduct, and registration flows are out of module scope.

---

#### F04-005 — Random Question Selection Rules

**One-liner / description:** Examination Administrators configure per-examination random question selection rules specifying total questions to draw, category-wise question counts, eligible difficulty filters if used, and minimum pool depth…

**Business objective:** Ensure each examination has explicit, validated rules for drawing questions randomly from the bank by category so sufficient pool depth exists for multi-version randomisation downstream.

**Actors:** Examination Administrator

**User journey (1 steps):**
1. Administrator opens an Active examination from the master register and navigates to Question Selection Rules. 2. System shows existing rule set status Draft or Active or displays empty state prompting first configuration. 3. Administrator clicks Configure Rules. 4. Administrator enters total question count for the paper. 5. Administrator adds category allocation rows specifying category, required count, and optional difficulty filter. 6. System live-calculates sum of category counts versus total and available pool per category from Active questions. 7. System flags insufficient pool depth when available Active questions in a category are less than required count multiplied by configured version multiplier from F04-006 when linked. 8. Administrator adjusts counts or adds bank questions until validation passes. 9. Administrator saves rules as Draft. 10. Administrator reviews read-only rule summary with pool depth indicators. 11. Administrator activates rules; status transitions to Active. 12. Administrator edits Draft rules or creates new Draft superseding prior Active per policy. 13. Administrator deactivates rules when examination retires.

**Functional capabilities:**
- Display question selection rule summary per examination
- Configure total question count for examination paper
- Add and edit category-wise question count allocation rows
- Optional per-row difficulty filter when bank items carry difficulty metadata
- Live sum validation of category counts against total
- Pool depth check against Active questions per category
- Cross-check pool depth against multiple version count when version settings exist
- Save rules in Draft status
- Activate rules for downstream paper generation consumers
- Deactivate rules without deleting audit history
- Show insufficient pool warning panel with counts required versus available
- Empty state when examination has no rules configured

**Inputs:** Examination identifier; Total question count; Category allocation rows with category, count, optional difficulty; Draft save action; Activate action; Deactivate action

**Outputs:** Rule set with Draft or Active status; Category allocation table; Pool depth validation results; Active rule set consumable by secure conduct module; Administrator warnings for insufficient pool

**Business rules:**
- Sum of category counts must equal total question count
- Only Active questions in referenced categories count toward pool depth
- Inactive categories cannot appear in allocation rows
- Active rule set required before examination can be scheduled with random papers
- Pool depth must meet or exceed required count times paper version count configured in F04-006
- One Active rule set per examination at a time
- Editing Active rules creates new Draft superseding on activation unless direct edit permitted in Draft only

**Validations:**
- Total question count required, positive integer, within examination policy maximum
- Each allocation row category required and must be Active
- Each allocation count required, positive integer
- Sum of allocation counts must equal total question count exactly
- Reject duplicate category row with same difficulty filter combination
- Reject activation when any category pool depth insufficient
- Reject allocation referencing category with zero Active questions
- Optional difficulty filter must match allowed enumeration when provided

**Workflow / states:** NoRules → Draft on first save → Active on activate; Active → Draft on new draft creation; Active → Inactive on deactivate

**Dependencies:**
- F04-001 — Question Category & Taxonomy Management
- F04-002 — Question Bank Item Lifecycle & Answer Key Management
- F04-004 — Examination Master Configuration
- F04-006 — Multiple Question Paper Version & Randomisation Settings
- F01 — Downstream Module Authorization Integration Hooks

**Risks:** Insufficient pool discovered late blocks scheduling until bank is expanded; Category rebalancing requires coordinated updates with bank content

**Notes:** Configures selection rules and pool depth validation only; candidate-specific paper assembly at exam time is out of scope.

---

#### F04-006 — Multiple Question Paper Version & Randomisation Settings

**One-liner / description:** Examination Administrators configure the number of distinct question paper versions per examination and define randomisation rules for question order and answer-option order applied when papers are materialised…

**Business objective:** Reduce collusion risk and satisfy examination integrity requirements by supporting multiple paper versions with configurable shuffling behaviour while keeping configuration separate from live conduct.

**Actors:** Examination Administrator

**User journey (1 steps):**
1. Administrator opens an Active examination and navigates to Paper Version Settings. 2. System displays current version count, question order randomisation flag, and answer option randomisation flag or empty defaults. 3. Administrator enters desired number of paper versions as a positive integer. 4. Administrator toggles randomise question order within each version according to policy. 5. Administrator toggles randomise answer option order for applicable objective question types. 6. System recalculates required minimum pool depth using active selection rules from F04-005 multiplied by version count. 7. System shows warning if pool depth is insufficient for requested versions. 8. Administrator saves settings as Draft. 9. Administrator reviews read-only summary of version and randomisation settings. 10. Administrator activates settings; status becomes Active. 11. Administrator edits Draft settings before activation or creates superseding Draft from Active. 12. Administrator deactivates settings when examination retires.

**Functional capabilities:**
- Display paper version and randomisation settings summary per examination
- Configure number of distinct paper versions
- Toggle question order randomisation per examination
- Toggle answer option order randomisation per examination
- Recalculate and display pool depth requirement based on version count and F04-005 rules
- Save settings in Draft status
- Activate settings for downstream consumers
- Deactivate settings preserving audit trail
- Block activation when pool depth insufficient for configured versions
- Show empty defaults state before first configuration

**Inputs:** Examination identifier; Paper version count; Question order randomisation enabled flag; Answer option randomisation enabled flag; Draft save action; Activate action; Deactivate action

**Outputs:** Draft or Active version settings record; Pool depth requirement summary; Activation warnings; Settings metadata for Module 09 paper materialisation

**Business rules:**
- Paper version count must be at least one
- Increasing version count increases required pool depth defined by F04-005 allocations
- Answer option randomisation applies only to question types with multiple options
- One Active settings record per examination
- Inactive examinations cannot activate new version settings
- Runtime paper generation and candidate-specific assembly remain out of scope in this module

**Validations:**
- Version count required, integer between 1 and configured policy maximum such as 20
- Reject activation when linked selection rules are not Active
- Reject activation when pool depth check fails for version count multiplied by per-category allocations
- Question order randomisation flag required boolean
- Answer option randomisation flag required boolean
- Reject version count reduction below already generated version inventory in downstream module when lock signal present
- Reject settings for Inactive examination

**Workflow / states:** Unset → Draft on save → Active on activate; Active → Draft on superseding draft; Active → Inactive on deactivate

**Dependencies:**
- F04-004 — Examination Master Configuration
- F04-005 — Random Question Selection Rules
- F01 — Downstream Module Authorization Integration Hooks

**Risks:** High version counts exhaust category pools quickly; Changing randomisation flags after papers materialised may cause inconsistency without downstream lock rules

**Notes:** Configures version count and randomisation flags only; runtime paper assembly is out of scope.

---

#### F04-007 — Result Display, Certificate Eligibility & Examination Fee Configuration

**One-liner / description:** Examination Administrators configure per-examination rules governing how results are displayed to candidates, minimum outcomes required for certificate eligibility, and administrator-maintained examination fee…

**Business objective:** Allow the department to tune candidate-facing result presentation and certificate thresholds without code changes and to maintain authoritative fee amounts consumed by registration without implementing payment processing in this module.

**Actors:** Examination Administrator

**User journey (1 steps):**
1. Administrator opens an Active examination and navigates to Outcome & Fee Settings. 2. System shows tabs or sections for Result Display Rules, Certificate Eligibility Rules, and Examination Fee Amounts. 3. Under Result Display Rules, administrator chooses whether to show numeric score, pass/fail status, sectional breakdown if applicable, and immediate versus delayed display flag as supported. 4. Administrator saves result display Draft. 5. Under Certificate Eligibility Rules, administrator sets minimum pass requirement reference aligned with examination passing criteria and optional minimum score threshold for certificate issuance. 6. Administrator toggles certificate eligibility requires pass only or pass plus minimum score. 7. Administrator saves eligibility Draft. 8. Under Examination Fee Amounts, administrator opens fee rule list showing candidate category such as government employee first attempt, government employee subsequent attempt, and other organisation candidate. 9. Administrator clicks Add Fee Rule and selects category, attempt type first or subsequent, currency, and amount. 10. System validates non-negative amount and unique category-plus-attempt combination per examination. 11. Administrator edits existing fee rule amounts. 12. Administrator deactivates obsolete fee rule row. 13. Administrator reviews combined read-only summary. 14. Administrator activates all outcome and fee settings as a bundle or per section per policy. 15. Module 05 registration consumes Active fee amounts; Module 10 and Module 11 consume eligibility and display rules.

**Functional capabilities:**
- Configure result display flags for numeric score visibility
- Configure result display flags for pass/fail visibility
- Configure immediate versus delayed result display policy flag
- Configure certificate eligibility requires pass aligned to examination master
- Configure optional minimum score threshold for certificate eligibility
- Maintain examination fee amount rules by candidate category and attempt type
- Create fee rule row with category, attempt type, and amount
- Edit fee rule amount
- Deactivate fee rule row without deleting history
- List fee rules with filters by category and attempt type
- Activate outcome and fee configuration for downstream consumption
- Validate fee rule uniqueness per examination category and attempt combination

**Inputs:** Examination identifier; Show numeric score flag; Show pass fail flag; Immediate display flag; Certificate eligibility pass required flag; Optional certificate minimum score; Fee rule candidate category; Fee rule attempt type first or subsequent

**Outputs:** Active result display rule set; Active certificate eligibility rule set; Active fee rule rows exposed to registration; Draft settings per section where applicable; Administrator confirmation summaries

**Business rules:**
- Certificate eligibility cannot require score below examination passing threshold
- Fee amount zero explicitly represents free registration for matching category and attempt
- First-time government employee registration fee defaults to zero per SOW unless administrator overrides
- Subsequent attempt and other organisation categories use administrator-configured positive or zero amounts
- Inactive fee rules are ignored by registration fee lookup
- Only one Active fee rule per examination category and attempt type combination
- Result display and eligibility rules apply to Module 10 publication behaviour; certificate layout remains Module 11
- Payment processing and fee collection are out of scope; only amount configuration is in scope

**Validations:**
- At least one result display element must be selected when result display section activated
- Certificate minimum score when provided must be numeric and greater than or equal to passing marks and less than or equal to total marks
- Fee amount required, non-negative numeric with two decimal places
- Candidate category required from controlled enumeration matching registration module categories
- Attempt type required as first or subsequent enumeration
- Reject duplicate fee rule for same examination category and attempt type when Active
- Reject eligibility activation when examination master is not Active
- Reject negative fee amounts

**Workflow / states:** Per section Draft → Active on activate; Active fee row → Inactive on deactivate; Active outcome section → Draft on superseding edit

**Dependencies:**
- F04-004 — Examination Master Configuration
- F05 — Candidate Registration examination selection and fee flows
- F10 — Evaluation & Results publication behaviour
- F11 — Certificate Management eligibility enforcement
- F01 — Downstream Module Authorization Integration Hooks

**Risks:** Fee misconfiguration affects registration revenue or blocks valid registrations; Eligibility threshold misalignment with passing criteria causes certificate disputes; Changing fee amounts mid-registration window may require effective-date policy outside this scope

**Notes:** Configures display and eligibility rules and fee amounts only; result publication UI, certificate layout, and payment processing are out of scope.

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 04 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 04 Question Bank & Examination Configuration** (7 features).
> Features: F04-001 Question Category & Taxonomy Management; F04-002 Question Bank Item Lifecycle & Answer Key Management; F04-003 Question Bank Bulk Import; F04-004 Examination Master Configuration; F04-005 Random Question Selection Rules; F04-006 Multiple Question Paper Version & Randomisation Settings; F04-007 Result Display, Certificate Eligibility & Examination Fee Configuration.
> Purpose: Manage question taxonomy and bank, bulk import, examination master, random selection rules, paper version/randomisation settings, and result/certificate/fee configuration.
> Draw: Question taxonomy tree + bank lifecycle; Bulk import pipeline flowchart; Selection rules → pool depth → version count calculation diagram; Examination config layers (master / selection / randomisation / fee / result / cert); ERD for `question_category`, `question`, `question_option`, `question_import_batch`, `examination`, `examination_selection_rule`.
