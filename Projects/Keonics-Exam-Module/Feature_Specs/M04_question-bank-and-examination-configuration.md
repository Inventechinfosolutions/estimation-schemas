# Module 04: Question Bank & Examination Configuration

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 7 (F04-001 … F04-007)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 04 Question Bank & Examination Configuration

996.85 hours · 174 tasks · Business

Examination definition, question bank administration, and configurable rules for paper generation, scoring, and outcomes.

### F04-001 Question Category & Taxonomy Management

106.45 hours · Go-live · 20 tasks

##### Description

Examination Administrators maintain a hierarchical or flat catalogue of question categories used to classify bank items and to drive category-wise question counts during paper-generation rule configuration.

##### Business objective

Provide a controlled, reusable category structure so questions can be grouped consistently and random-selection rules can allocate counts per category without manual ad hoc tagging.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Question Categories from the Question Bank administration menu. 2. System displays the category register with search, status filter, and parent-category filter when hierarchy is enabled. 3. Administrator clicks Add Category. 4. Administrator enters category code, display name, optional description, optional parent category, and display order. 5. System validates uniqueness of code and name within the same parent scope. 6. Administrator saves; category transitions to Active. 7. Administrator returns to the register and verifies the new category appears with Active status chip. 8. Administrator selects an existing category and opens Edit. 9. Administrator updates name, description, parent, or display order but not code after first use. 10. System warns if the category is referenced by live questions or active examination rules before allowing parent change. 11. Administrator opens Deactivate and confirms; category transitions to Inactive and is excluded from new question assignment and new rule configuration. 12. Administrator views empty register state when no categories match filters.

##### Functional capabilities

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

##### Inputs

- Category code
- Category display name
- Optional description
- Optional parent category identifier
- Display order integer
- Status selection on deactivate

##### Outputs

- Category register list rows with code, name, parent, status, question count summary
- Created or updated category record
- Deactivation confirmation outcome
- Active category lookup results for dependent screens

##### Business rules

- Category code must be unique within the examination tenant scope
- Category name must be unique among siblings under the same parent
- Inactive categories cannot be assigned to new questions or new examination rules
- Existing questions and historical papers retain reference to inactive categories for audit
- Parent category cannot be a descendant of the current category
- Only Examination Administrator role may create, edit, or deactivate categories

##### Validations

- Category code required, alphanumeric with optional hyphen, 2–20 characters
- Category name required, 3–100 characters, no leading or trailing whitespace
- Description optional, maximum 500 characters
- Display order required, non-negative integer, maximum 9999
- Parent category must reference an Active category when supplied
- Reject circular parent assignment
- Reject duplicate code on create
- Reject duplicate name under same parent on create and edit
- Reject deactivation when category has Active child categories unless children are deactivated first
- Reject parent change that would orphan active examination rules referencing the category

##### Calculations

- Derived question count per category for register display
- Derived full hierarchical path label for nested categories in register and lookup

##### Workflow

Draft-on-create → Active on successful save; Active → Inactive on administrator deactivate; Inactive remains terminal for new assignments; Active → Active on successful edit

##### Search requirements

- Partial match search on category code
- Partial match search on category name
- Exact filter on status
- Exact filter on parent category

##### Security

- Restrict category administration to Examination Administrator permissions from Module 01
- Audit log entry on create, edit, and deactivate with administrator identity and timestamp
- Prevent unauthenticated access to category register and forms

##### Integrations

- Consume Module 01 authorization hooks to gate category screens and operations

##### Dependencies

- F01 — Platform Role and Permission Catalog
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Category depth is limited to a practical hierarchy of up to three levels
- Question counts shown in register are informational and refreshed on list load

##### Risks

- Late category restructuring may require re-mapping questions and active paper rules
- Large category trees may require pagination tuning in lookup dialogs used by question forms

##### Non-functional requirements

- Category register loads within acceptable enterprise UI response for up to several thousand categories
- All category mutations are persisted in MySQL as system of record
- Deactivation is logical, not physical delete

##### Notes

Prerequisite taxonomy for question bank categorisation and category-wise paper rules in later features.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Question category register with search, status filter, and parent filter | Medium | 16 |
| UI | Create question category form with parent picker and display order | Medium | 16 |
| UI | Edit question category form with code read-only after first use | Medium | 16 |
| UI | Deactivate category confirmation dialog with dependency warning | Simple | 5 |
| UI | Category register empty state when no rows match filters | Simple | 5 |
| UI | Active category lookup dialog for downstream question assignment | Easy | 14 |
| API | List and search question categories with pagination and filters | Medium | 6 |
| API | Create question category with uniqueness and hierarchy validation | Medium | 6 |
| API | Update question category metadata with parent-change guardrails | Complex | 8 |
| API | Deactivate question category without deleting historical references | Medium | 6 |
| API | Active category lookup for question and rule configuration screens | Simple | 2 |
| Database | Question category core entity with parent self-reference | Easy | 0.25 |
| Database | Category uniqueness constraints and status indexes | Complex | 0.5 |
| Database | Category change audit history records | Medium | 0.3 |
| Integration | Module 01 authorization check hook for category administration actions | Simple | 4 |
| Testing | Happy-path create, edit, list, and deactivate category scenarios | Easy | 0.25 |
| Testing | Duplicate code, duplicate sibling name, and invalid parent validation cases | Medium | 0.3 |
| Testing | Circular parent, active-child deactivation block, and authorization denial cases | Complex | 0.5 |
| Documentation | Administrator runbook for maintaining question categories | Easy | 0.25 |
| Documentation | Technical notes for category hierarchy rules and audit behaviour | Simple | 0.1 |

### F04-002 Question Bank Item Lifecycle & Answer Key Management

154.5 hours · Go-live · 26 tasks

##### Description

Examination Administrators create, edit, deactivate, and manage individual question bank items including stem text, options, marks, category assignment, difficulty metadata where applicable, and authoritative answer keys for objective items.

##### Business objective

Maintain a sufficient, quality-controlled pool of examination questions with correct marking keys so downstream random-selection and multi-version paper rules can draw from a validated bank.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Question Bank register. 2. System lists questions with search, category filter, status filter, and marks range filter. 3. Administrator clicks Add Question. 4. Administrator selects question type such as single-correct MCQ, multiple-correct MCQ, or true/false as supported by scope. 5. Administrator enters question stem, assigns category, enters marks, and optionally difficulty label. 6. Administrator adds answer options with option text and marks-as-key indicators per type rules. 7. Administrator designates correct answer key mapping for scorable types. 8. System validates minimum options, key completeness, and positive marks. 9. Administrator saves; question transitions to Active. 10. Administrator opens a question from the register in read-only preview. 11. Administrator opens Edit on an Active question, updates stem, options, marks, category, or answer key. 12. System warns if the question is referenced by active examination configurations before destructive option removal. 13. Administrator opens Deactivate, confirms, and question transitions to Inactive. 14. Inactive questions remain visible in register with Inactive chip but cannot be assigned to new paper rules. 15. Administrator views register empty state when filters yield no results.

##### Functional capabilities

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

##### Inputs

- Question type
- Question stem rich text or plain text
- Category selection
- Marks value
- Optional difficulty label
- Answer option rows with option label and text
- Correct answer key selection per question type
- Status on deactivate

##### Outputs

- Question register rows with identifier, type, category, marks, status, last modified metadata
- Created or updated question and answer key records
- Read-only preview rendering
- Deactivation outcome and dependency warnings

##### Business rules

- Each question belongs to exactly one active category at creation time
- Marks must be greater than zero for scorable questions
- Single-correct MCQ must have exactly one designated correct option in the answer key
- Multiple-correct MCQ must have at least one correct option and at least one incorrect option
- True/false questions must have exactly two options
- Inactive questions remain in bank history and prior paper definitions but are excluded from new rule pools
- Answer key is authoritative for evaluation modules; display order may differ after randomisation at runtime
- Only Examination Administrator role may manage question bank items

##### Validations

- Question stem required, minimum 10 characters, maximum configurable upper bound such as 2000 characters
- Category required and must reference Active category
- Marks required, positive numeric, maximum two decimal places, upper bound per department policy field
- Minimum option count per type: at least four for MCQ unless policy allows three
- Option text required for each option row, non-duplicate within the question
- Answer key must reference valid option identifiers for the question
- Reject save when no correct option is designated for scorable types
- Reject duplicate question stem hash within same category when duplicate detection is enabled
- Reject deactivation when it would leave an active examination rule with insufficient pool depth unless administrator acknowledges override
- Reject edit that removes options referenced by locked examination configurations

##### Calculations

- Per-question maximum obtainable marks equals assigned marks for standard items
- Register display snippet derived from stem first N characters

##### Workflow

Draft-on-create → Active on successful save; Active → Active on edit; Active → Inactive on deactivate; Inactive terminal for new pool inclusion

##### Search requirements

- Partial text search on question stem
- Exact filter on question identifier
- Exact filter on category
- Exact filter on status
- Exact filter on question type
- Numeric range filter on marks

##### Security

- Restrict question bank screens to Examination Administrator permissions
- Audit create, edit, deactivate, and answer key changes with before/after summary
- Prevent exposure of answer key in candidate-facing channels; admin-only views

##### Integrations

- Consume Module 01 authorization hooks
- Provide question and key metadata to Module 10 Evaluation & Results as downstream consumer without runtime paper generation here

##### Dependencies

- F04-001 — Question Category & Taxonomy Management
- F01 — Platform Role and Permission Catalog
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Subjective or essay question types are out of scope unless explicitly added later
- Rich text support is limited to basic formatting acceptable for examination stems

##### Risks

- Answer key errors propagate to scoring in Module 10
- Editing questions after examinations are scheduled may affect consistency unless configurations are locked elsewhere

##### Non-functional requirements

- Question register performant for banks up to tens of thousands of items with indexed search
- MySQL remains authoritative store for questions and answer keys
- Forms handle validation feedback without losing entered option rows

##### Notes

Core question bank administration excluding bulk import handled in F04-003.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Question bank register with search, category filter, type filter, marks range, and status chips | Medium | 16 |
| UI | Create single-correct MCQ question form with dynamic option rows and answer key picker | Complex | 18 |
| UI | Create multiple-correct MCQ question form with multi-select answer key | Complex | 18 |
| UI | Create true/false question form with fixed two-option layout | Easy | 14 |
| UI | Edit question form reusing type-specific layouts with dependency warning banner | Complex | 18 |
| UI | Read-only question preview panel with stem and shuffled-safe option display | Easy | 14 |
| UI | Deactivate question confirmation dialog with pool-depth warning | Simple | 5 |
| UI | Question register empty state when no items match filters | Simple | 5 |
| UI | Question form server-side validation error summary panel | Simple | 5 |
| API | List and search questions with pagination and multi-filter support | Medium | 6 |
| API | Retrieve single question with options and answer key for admin views | Easy | 4 |
| API | Create question with type-specific option and answer key validation | Complex | 8 |
| API | Update question content, marks, category, options, and answer key with dependency checks | Complex | 8 |
| API | Deactivate question without deleting historical references | Medium | 6 |
| API | Question preview payload for read-only rendering | Simple | 2 |
| Database | Question core entity linked to category and type | Medium | 0.3 |
| Database | Question option rows with ordering metadata | Easy | 0.25 |
| Database | Answer key mapping entity separate from display order | Medium | 0.3 |
| Database | Question status indexes and stem search support | Complex | 0.5 |
| Database | Question and answer key change audit history | Medium | 0.3 |
| Integration | Module 01 authorization hook for question bank mutations | Simple | 4 |
| Testing | Happy-path create, edit, preview, list, and deactivate for each supported question type | Complex | 0.5 |
| Testing | Missing stem, invalid marks, insufficient options, and missing answer key rejection cases | Medium | 0.3 |
| Testing | Inactive category assignment block, dependency warning on edit, and answer key exposure security cases | Complex | 0.5 |
| Documentation | Administrator runbook for question authoring and answer key maintenance | Medium | 0.3 |
| Documentation | Technical notes on question types, key storage, and deactivation semantics | Easy | 0.25 |

### F04-003 Question Bank Bulk Import

132.95 hours · Go-live · 25 tasks

##### Description

Examination Administrators import batches of questions from a structured file template into the question bank with pre-commit validation, row-level error reporting, and controlled activation of successfully validated rows.

##### Business objective

Accelerate establishment of a deep question pool required for randomisation and multiple paper versions while preserving data quality through validation before commit.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Question Bank Import from the administration menu. 2. System displays import history register with batch status, uploaded by, row counts, and timestamps. 3. Administrator clicks New Import. 4. Administrator downloads the approved import template reference document link shown on screen. 5. Administrator uploads completed file selecting target default category and question type constraints if applicable. 6. System parses file and transitions batch to Validating. 7. Administrator views validation preview grid listing each row with pass/fail indicator and error messages. 8. Administrator filters preview to failed rows only. 9. Administrator corrects source file offline and re-uploads or excludes failed rows per policy. 10. Administrator clicks Commit Valid Rows when at least one row passed validation. 11. System creates Active questions and answer keys for valid rows and marks batch Committed. 12. Administrator downloads error report file for failed rows. 13. Administrator opens a committed batch detail read-only view showing created question identifiers. 14. Administrator views empty import history state on first use.

##### Functional capabilities

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

##### Inputs

- Import file in approved template format
- Optional default category for rows missing explicit category code
- Optional default question type when uniform per file
- Commit confirmation action
- Re-upload replacement file for same draft batch when supported

##### Outputs

- Import batch record with status Validating, Committed, or Failed
- Row-level validation results
- Created question identifiers for committed rows
- Downloadable error report artifact
- Import history register rows

##### Business rules

- Only validated rows are persisted as Active questions on commit
- Failed rows never partially create question records
- Category codes in file must resolve to Active categories
- Duplicate question stems within the same import batch are rejected
- Committed batches are immutable; corrections require new import or manual edit via F04-002
- Maximum row count per batch governed by configured enterprise limit
- Import does not auto-link questions to examination rules; administrator configures rules separately

##### Validations

- File format must match approved template columns and encoding
- Reject empty file upload
- Row-level stem required and length within limits
- Row-level category code must exist and be Active
- Row-level marks must be positive numeric
- Row-level options must meet minimum count for declared type
- Row-level answer key must map to provided option labels
- Reject rows referencing inactive categories
- Reject commit when batch status is not ValidationComplete with at least one valid row
- Reject upload exceeding configured maximum file size or row count

##### Calculations

- Valid row count, failed row count, and committed row count per batch
- Batch progress percentage during validation preview

##### Workflow

Uploaded → Validating → ValidationComplete → Committed; Uploaded or Validating → Failed on fatal parse error; Committed is terminal

##### Search requirements

- Filter import history by batch status
- Filter import history by upload date range
- Text search on batch identifier or uploading administrator

##### Documents

- Downloadable question import template specification reference

##### Reports

- Row-level import error report export per batch

##### Security

- Restrict import screens and commit action to Examination Administrator role
- Audit file upload, validation, and commit events with batch identifier
- Scan or restrict file types to approved template formats only

##### Integrations

- Module 01 authorization hook for import operations
- Resolve category codes against F04-001 category catalogue

##### Dependencies

- F04-001 — Question Category & Taxonomy Management
- F04-002 — Question Bank Item Lifecycle & Answer Key Management
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Template format is agreed CSV or Excel variant documented to administrators
- Large imports may run asynchronously with progress polling on preview screen

##### Risks

- Bulk import of incorrect answer keys affects scoring at scale
- Very large files may require batch size tuning for validation performance

##### Non-functional requirements

- Validation preview returns within acceptable time for batches up to configured row limit
- Imported questions persisted in MySQL with traceability to import batch
- Error report generation available immediately after validation completes

##### Notes

Bulk load path for initial bank population; does not include runtime paper generation.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Question import history register with status and count columns | Easy | 14 |
| UI | New import upload screen with template link and default category selector | Medium | 16 |
| UI | Import validation preview grid with pass/fail indicators per row | Complex | 18 |
| UI | Failed-rows-only filter control on validation preview | Simple | 5 |
| UI | Commit valid rows confirmation dialog with row count summary | Simple | 5 |
| UI | Committed batch detail read-only view with created question identifiers | Easy | 14 |
| UI | Import history empty state on first use | Simple | 5 |
| UI | Import fatal parse error screen with retry guidance | Simple | 5 |
| API | List import batches with filters and pagination | Easy | 4 |
| API | Upload import file and create batch in Uploaded state | Medium | 6 |
| API | Validate import batch rows and return row-level results | Complex | 8 |
| API | Commit validated rows into Active questions and answer keys | Very high | 12 |
| API | Retrieve import batch detail with created question cross-references | Easy | 4 |
| API | Export import error report for failed rows | Medium | 6 |
| Database | Import batch header entity with status and counts | Easy | 0.25 |
| Database | Import row staging entity with validation messages | Medium | 0.3 |
| Database | Batch-to-created-question linkage for traceability | Easy | 0.25 |
| Database | Import audit history for upload, validate, and commit events | Medium | 0.3 |
| Integration | Category code resolution against active taxonomy during validation | Simple | 4 |
| Integration | Module 01 authorization hook for import upload and commit | Simple | 4 |
| Testing | Happy-path upload, validate, preview, commit, and history list scenarios | Complex | 0.5 |
| Testing | Invalid file format, missing columns, bad category code, and bad answer key row rejection cases | Complex | 0.5 |
| Testing | Zero valid rows commit block, duplicate stem in batch, and authorization denial edge cases | Medium | 0.3 |
| Documentation | Administrator runbook for template preparation and import commit | Medium | 0.3 |
| Documentation | Technical notes for batch states, staging cleanup, and error report format | Easy | 0.25 |

### F04-004 Examination Master Configuration

123.5 hours · Go-live · 22 tasks

##### Description

Examination Administrators define and maintain examination master records specifying examination identity, duration, total marks structure reference, passing criteria, negative marking policy, and candidate-facing instructions used by downstream scheduling, conduct, and evaluation modules.

##### Business objective

Centralise authoritative examination parameters so registration, scheduling, secure conduct, and evaluation consume consistent duration, marking, and pass rules.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens Examination Master register. 2. System lists examinations with search, status filter, and code filter. 3. Administrator clicks Create Examination. 4. Administrator enters examination code, name, description, duration in minutes, total marks, passing marks or passing percentage mode, negative marking enabled flag, negative mark deduction value, and instructions text. 5. System validates numeric relationships between total and passing marks. 6. Administrator saves; examination transitions to Draft. 7. Administrator reviews Draft examination in read-only summary. 8. Administrator clicks Activate; examination transitions to Active when mandatory fields are complete. 9. Downstream modules may reference Active examinations only. 10. Administrator opens Edit on Draft or Active examination to adjust instructions or marking parameters subject to lock rules. 11. Administrator deactivates examination when retires; transitions to Inactive. 12. Administrator sees empty register state when no examinations exist.

##### Functional capabilities

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

##### Inputs

- Examination code
- Examination name
- Optional description
- Duration minutes
- Total marks
- Passing marks or passing percentage according to selected mode
- Negative marking enabled flag
- Negative mark deduction value per wrong answer when enabled
- Examination instructions text
- Activate or deactivate action

##### Outputs

- Examination master register rows
- Draft, Active, or Inactive examination records
- Read-only summary for confirmation
- Active examination lookup results

##### Business rules

- Examination code unique within tenant scope
- Passing threshold cannot exceed total marks
- Negative marking deduction applies only when negative marking enabled
- Inactive examinations cannot be selected for new schedules or registrations
- Historical schedules retain reference to examination version effective at activation time
- Instructions text published to candidate-facing artefacts by downstream modules
- Only Examination Administrator may manage examination master records

##### Validations

- Examination code required, unique, alphanumeric 3–20 characters
- Examination name required, 5–150 characters
- Duration required, positive integer minutes within configured maximum
- Total marks required, positive numeric with up to two decimals
- Passing marks required when mode is absolute marks and must be less than or equal to total marks
- Passing percentage required when mode is percentage and must be between 1 and 100
- Negative deduction value required and positive when negative marking enabled
- Instructions optional, maximum length per policy such as 4000 characters
- Reject activation when any mandatory field fails validation
- Reject deactivation when open future schedules exist unless force-confirm override policy applies

##### Calculations

- Derived passing marks from percentage mode using total marks
- Effective maximum negative deduction exposure informational display based on question count from linked rules in later features

##### Workflow

Draft on create → Active on activate; Active → Active on edit where permitted; Active → Inactive on deactivate; Draft → Inactive on cancel draft if supported

##### Search requirements

- Partial search on examination code and name
- Exact filter on status Draft Active Inactive
- Sort by name, code, and last modified date

##### Security

- Examination master administration restricted to Examination Administrator role
- Audit activation, deactivation, and changes to passing and negative marking parameters
- Prevent unauthenticated register access

##### Integrations

- Module 01 authorization hooks
- Provide Active examination metadata to Module 05 Candidate Registration and Module 06 Examination Scheduling as consumers

##### Dependencies

- F01 — Platform Role and Permission Catalog
- F01 — Examination Administrator Account Lifecycle
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Examination master does not embed question lists; paper rules are configured in F04-005 and F04-006
- Locking edits after schedules exist may be enforced in Module 06 rather than here with warning-only in this module

##### Risks

- Changing passing or negative marking after registrations may affect candidate expectations
- Missing instructions content impacts hall ticket and conduct modules

##### Non-functional requirements

- Examination register responsive for typical catalogue sizes
- MySQL authoritative storage for examination master
- Activation action is atomic

##### Notes

Examination definition master only; scheduling, conduct, and registration flows are out of module scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination master register with search and status filters | Medium | 16 |
| UI | Create examination master form with duration, marks, pass mode, and negative marking section | Complex | 18 |
| UI | Edit examination master form with state-aware field restrictions | Complex | 18 |
| UI | Examination master read-only summary panel | Easy | 14 |
| UI | Activate examination confirmation dialog | Simple | 5 |
| UI | Deactivate examination confirmation dialog with schedule dependency warning | Simple | 5 |
| UI | Examination register empty state | Simple | 5 |
| API | List and search examination masters with pagination | Medium | 6 |
| API | Create examination master in Draft with field validation | Complex | 8 |
| API | Update examination master with pass and negative marking validation | Complex | 8 |
| API | Activate examination master when mandatory fields complete | Medium | 6 |
| API | Deactivate examination master without deleting history | Medium | 6 |
| API | Active examination lookup for downstream registration and scheduling | Simple | 2 |
| Database | Examination master core entity with status lifecycle | Medium | 0.3 |
| Database | Examination code uniqueness and status indexes | Easy | 0.25 |
| Database | Examination master change audit history | Medium | 0.3 |
| Integration | Module 01 authorization hook for examination master mutations | Simple | 4 |
| Testing | Happy-path create, edit, activate, list, and deactivate examination master flows | Medium | 0.3 |
| Testing | Pass marks greater than total, invalid duration, and negative marking missing deduction validation cases | Medium | 0.3 |
| Testing | Activation gating, deactivation with schedule dependency warning, and authorization denial edge cases | Complex | 0.5 |
| Documentation | Administrator runbook for examination master setup and activation | Medium | 0.3 |
| Documentation | Technical notes on examination status lifecycle and downstream consumption | Easy | 0.25 |

### F04-005 Random Question Selection Rules

162.2 hours · Go-live · 27 tasks

##### Description

Examination Administrators configure per-examination random question selection rules specifying total questions to draw, category-wise question counts, eligible difficulty filters if used, and minimum pool depth checks against the active question bank.

##### Business objective

Ensure each examination has explicit, validated rules for drawing questions randomly from the bank by category so sufficient pool depth exists for multi-version randomisation downstream.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens an Active examination from the master register and navigates to Question Selection Rules. 2. System shows existing rule set status Draft or Active or displays empty state prompting first configuration. 3. Administrator clicks Configure Rules. 4. Administrator enters total question count for the paper. 5. Administrator adds category allocation rows specifying category, required count, and optional difficulty filter. 6. System live-calculates sum of category counts versus total and available pool per category from Active questions. 7. System flags insufficient pool depth when available Active questions in a category are less than required count multiplied by configured version multiplier from F04-006 when linked. 8. Administrator adjusts counts or adds bank questions until validation passes. 9. Administrator saves rules as Draft. 10. Administrator reviews read-only rule summary with pool depth indicators. 11. Administrator activates rules; status transitions to Active. 12. Administrator edits Draft rules or creates new Draft superseding prior Active per policy. 13. Administrator deactivates rules when examination retires.

##### Functional capabilities

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

##### Inputs

- Examination identifier
- Total question count
- Category allocation rows with category, count, optional difficulty
- Draft save action
- Activate action
- Deactivate action

##### Outputs

- Rule set with Draft or Active status
- Category allocation table
- Pool depth validation results
- Active rule set consumable by secure conduct module
- Administrator warnings for insufficient pool

##### Business rules

- Sum of category counts must equal total question count
- Only Active questions in referenced categories count toward pool depth
- Inactive categories cannot appear in allocation rows
- Active rule set required before examination can be scheduled with random papers
- Pool depth must meet or exceed required count times paper version count configured in F04-006
- One Active rule set per examination at a time
- Editing Active rules creates new Draft superseding on activation unless direct edit permitted in Draft only

##### Validations

- Total question count required, positive integer, within examination policy maximum
- Each allocation row category required and must be Active
- Each allocation count required, positive integer
- Sum of allocation counts must equal total question count exactly
- Reject duplicate category row with same difficulty filter combination
- Reject activation when any category pool depth insufficient
- Reject allocation referencing category with zero Active questions
- Optional difficulty filter must match allowed enumeration when provided
- Reject deactivate when future scheduled sessions depend on Active rules unless confirmed

##### Calculations

- Sum of category allocation counts
- Available pool count per category from Active questions minus optional difficulty filter
- Required pool depth equals allocation count multiplied by paper version count from linked settings
- Remaining pool margin per category for administrator guidance

##### Workflow

NoRules → Draft on first save → Active on activate; Active → Draft on new draft creation; Active → Inactive on deactivate

##### Search requirements

- Not applicable beyond examination context navigation
- Category lookup search within allocation row picker

##### Security

- Restrict rule configuration to Examination Administrator role
- Audit rule activation and material count changes
- Read-only view of pool counts without exposing answer keys

##### Integrations

- Read Active question counts from F04-002 bank
- Read paper version count from F04-006 when present for depth calculation
- Module 01 authorization hooks
- Expose Active rule set metadata to Module 09 Secure Examination Conduct as consumer without performing runtime selection here

##### Dependencies

- F04-001 — Question Category & Taxonomy Management
- F04-002 — Question Bank Item Lifecycle & Answer Key Management
- F04-004 — Examination Master Configuration
- F04-006 — Multiple Question Paper Version & Randomisation Settings
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Random selection algorithm execution occurs in Module 09; this feature defines rules only
- Difficulty filter is optional and ignored when questions lack difficulty metadata

##### Risks

- Insufficient pool discovered late blocks scheduling until bank is expanded
- Category rebalancing requires coordinated updates with bank content

##### Non-functional requirements

- Pool depth checks perform within interactive UI tolerance using indexed counts
- Rule sets stored in MySQL with version identifier for audit
- Activation validates atomically

##### Notes

Configures selection rules and pool depth validation only; candidate-specific paper assembly at exam time is out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination question selection rule summary panel with status chip | Easy | 14 |
| UI | Configure selection rules form with total count and category allocation grid | Complex | 18 |
| UI | Category allocation row add and inline edit controls | Medium | 16 |
| UI | Live pool depth indicator panel per category row | Medium | 16 |
| UI | Insufficient pool depth warning banner with required versus available counts | Easy | 14 |
| UI | Rule set read-only review screen before activation | Easy | 14 |
| UI | Activate rule set confirmation dialog | Simple | 5 |
| UI | Deactivate rule set confirmation dialog | Simple | 5 |
| UI | No rules configured empty state on examination rules tab | Simple | 5 |
| API | Retrieve question selection rule set for an examination | Easy | 4 |
| API | Save Draft question selection rule set with allocation rows | Complex | 8 |
| API | Validate category allocation sums and pool depth for an examination | Complex | 8 |
| API | Activate question selection rule set with sufficiency checks | Complex | 8 |
| API | Deactivate question selection rule set | Medium | 6 |
| API | Category pool availability counts for allocation picker | Medium | 6 |
| Database | Question selection rule set header linked to examination | Medium | 0.3 |
| Database | Category allocation line entities with counts and optional difficulty | Easy | 0.25 |
| Database | Rule set status indexes and activation uniqueness constraints | Complex | 0.5 |
| Database | Rule set change audit history | Medium | 0.3 |
| Integration | Active question bank count aggregation by category for pool depth | Simple | 4 |
| Integration | Read paper version count from examination version settings for depth multiplier | Simple | 4 |
| Integration | Module 01 authorization hook for rule set mutations | Simple | 4 |
| Testing | Happy-path draft save, pool display, activate, and retrieve active rules scenarios | Complex | 0.5 |
| Testing | Allocation sum mismatch, duplicate category row, and zero-count category rejection cases | Medium | 0.3 |
| Testing | Insufficient pool activation block, version multiplier depth check, and authorization denial edge cases | Complex | 0.5 |
| Documentation | Administrator runbook for category allocation and pool depth planning | Medium | 0.3 |
| Documentation | Technical notes on rule set lifecycle and downstream consumption contract | Easy | 0.25 |

### F04-006 Multiple Question Paper Version & Randomisation Settings

131.3 hours · Go-live · 23 tasks

##### Description

Examination Administrators configure the number of distinct question paper versions per examination and define randomisation rules for question order and answer-option order applied when papers are materialised downstream.

##### Business objective

Reduce collusion risk and satisfy examination integrity requirements by supporting multiple paper versions with configurable shuffling behaviour while keeping configuration separate from live conduct.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens an Active examination and navigates to Paper Version Settings. 2. System displays current version count, question order randomisation flag, and answer option randomisation flag or empty defaults. 3. Administrator enters desired number of paper versions as a positive integer. 4. Administrator toggles randomise question order within each version according to policy. 5. Administrator toggles randomise answer option order for applicable objective question types. 6. System recalculates required minimum pool depth using active selection rules from F04-005 multiplied by version count. 7. System shows warning if pool depth is insufficient for requested versions. 8. Administrator saves settings as Draft. 9. Administrator reviews read-only summary of version and randomisation settings. 10. Administrator activates settings; status becomes Active. 11. Administrator edits Draft settings before activation or creates superseding Draft from Active. 12. Administrator deactivates settings when examination retires.

##### Functional capabilities

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

##### Inputs

- Examination identifier
- Paper version count
- Question order randomisation enabled flag
- Answer option randomisation enabled flag
- Draft save action
- Activate action
- Deactivate action

##### Outputs

- Draft or Active version settings record
- Pool depth requirement summary
- Activation warnings
- Settings metadata for Module 09 paper materialisation

##### Business rules

- Paper version count must be at least one
- Increasing version count increases required pool depth defined by F04-005 allocations
- Answer option randomisation applies only to question types with multiple options
- One Active settings record per examination
- Inactive examinations cannot activate new version settings
- Runtime paper generation and candidate-specific assembly remain out of scope in this module

##### Validations

- Version count required, integer between 1 and configured policy maximum such as 20
- Reject activation when linked selection rules are not Active
- Reject activation when pool depth check fails for version count multiplied by per-category allocations
- Question order randomisation flag required boolean
- Answer option randomisation flag required boolean
- Reject version count reduction below already generated version inventory in downstream module when lock signal present
- Reject settings for Inactive examination

##### Calculations

- Required pool depth per category equals allocation count multiplied by version count
- Total distinct paper slots equals version count for scheduling guidance display

##### Workflow

Unset → Draft on save → Active on activate; Active → Draft on superseding draft; Active → Inactive on deactivate

##### Security

- Restrict version settings to Examination Administrator role
- Audit activation and changes to version count and randomisation flags

##### Integrations

- Read Active selection rules from F04-005 for depth calculation
- Module 01 authorization hooks
- Expose Active settings to Module 09 Secure Examination Conduct

##### Dependencies

- F04-004 — Examination Master Configuration
- F04-005 — Random Question Selection Rules
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Downstream module stores materialised version catalog; this feature stores configuration intent only
- Randomisation seed strategy is owned by conduct module

##### Risks

- High version counts exhaust category pools quickly
- Changing randomisation flags after papers materialised may cause inconsistency without downstream lock rules

##### Non-functional requirements

- Pool depth recalculation responsive on settings form change
- Settings persisted in MySQL with examination foreign key
- Activation is atomic with validation

##### Notes

Configures version count and randomisation flags only; runtime paper assembly is out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Paper version settings summary panel with version count and randomisation flags | Easy | 14 |
| UI | Configure paper version count and randomisation toggles form | Medium | 16 |
| UI | Pool depth requirement recap panel driven by version count change | Medium | 16 |
| UI | Insufficient pool for version count warning banner | Easy | 14 |
| UI | Version settings read-only review screen before activation | Easy | 14 |
| UI | Activate version settings confirmation dialog | Simple | 5 |
| UI | Deactivate version settings confirmation dialog | Simple | 5 |
| UI | Unset version settings empty state defaults | Simple | 5 |
| API | Retrieve paper version and randomisation settings for an examination | Easy | 4 |
| API | Save Draft paper version and randomisation settings | Medium | 6 |
| API | Validate pool sufficiency for configured version count against active selection rules | Complex | 8 |
| API | Activate paper version and randomisation settings | Complex | 8 |
| API | Deactivate paper version and randomisation settings | Medium | 6 |
| Database | Paper version settings entity linked to examination with randomisation flags | Medium | 0.3 |
| Database | Active settings uniqueness and status indexes per examination | Easy | 0.25 |
| Database | Version settings change audit history | Medium | 0.3 |
| Integration | Selection rule allocation read for pool depth multiplier calculation | Simple | 4 |
| Integration | Module 01 authorization hook for version settings mutations | Simple | 4 |
| Testing | Happy-path save, pool recap update, activate, and retrieve active settings flows | Medium | 0.3 |
| Testing | Invalid version count bounds and missing active selection rules rejection cases | Medium | 0.3 |
| Testing | Insufficient pool activation block and authorization denial edge cases | Complex | 0.5 |
| Documentation | Administrator runbook for choosing version counts and randomisation options | Easy | 0.25 |
| Documentation | Technical notes on randomisation flags and conduct module handoff | Simple | 0.1 |

### F04-007 Result Display, Certificate Eligibility & Examination Fee Configuration

185.95 hours · Go-live · 31 tasks

##### Description

Examination Administrators configure per-examination rules governing how results are displayed to candidates, minimum outcomes required for certificate eligibility, and administrator-maintained examination fee amounts referenced by candidate registration flows by category and attempt type.

##### Business objective

Allow the department to tune candidate-facing result presentation and certificate thresholds without code changes and to maintain authoritative fee amounts consumed by registration without implementing payment processing in this module.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens an Active examination and navigates to Outcome & Fee Settings. 2. System shows tabs or sections for Result Display Rules, Certificate Eligibility Rules, and Examination Fee Amounts. 3. Under Result Display Rules, administrator chooses whether to show numeric score, pass/fail status, sectional breakdown if applicable, and immediate versus delayed display flag as supported. 4. Administrator saves result display Draft. 5. Under Certificate Eligibility Rules, administrator sets minimum pass requirement reference aligned with examination passing criteria and optional minimum score threshold for certificate issuance. 6. Administrator toggles certificate eligibility requires pass only or pass plus minimum score. 7. Administrator saves eligibility Draft. 8. Under Examination Fee Amounts, administrator opens fee rule list showing candidate category such as government employee first attempt, government employee subsequent attempt, and other organisation candidate. 9. Administrator clicks Add Fee Rule and selects category, attempt type first or subsequent, currency, and amount. 10. System validates non-negative amount and unique category-plus-attempt combination per examination. 11. Administrator edits existing fee rule amounts. 12. Administrator deactivates obsolete fee rule row. 13. Administrator reviews combined read-only summary. 14. Administrator activates all outcome and fee settings as a bundle or per section per policy. 15. Module 05 registration consumes Active fee amounts; Module 10 and Module 11 consume eligibility and display rules.

##### Functional capabilities

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
- Show read-only combined summary for examination outcome settings
- Empty states for examinations without fee rules or outcome settings

##### Inputs

- Examination identifier
- Show numeric score flag
- Show pass fail flag
- Immediate display flag
- Certificate eligibility pass required flag
- Optional certificate minimum score
- Fee rule candidate category
- Fee rule attempt type first or subsequent
- Fee amount currency and value
- Activate and deactivate actions

##### Outputs

- Active result display rule set
- Active certificate eligibility rule set
- Active fee rule rows exposed to registration
- Draft settings per section where applicable
- Administrator confirmation summaries

##### Business rules

- Certificate eligibility cannot require score below examination passing threshold
- Fee amount zero explicitly represents free registration for matching category and attempt
- First-time government employee registration fee defaults to zero per SOW unless administrator overrides
- Subsequent attempt and other organisation categories use administrator-configured positive or zero amounts
- Inactive fee rules are ignored by registration fee lookup
- Only one Active fee rule per examination category and attempt type combination
- Result display and eligibility rules apply to Module 10 publication behaviour; certificate layout remains Module 11
- Payment processing and fee collection are out of scope; only amount configuration is in scope

##### Validations

- At least one result display element must be selected when result display section activated
- Certificate minimum score when provided must be numeric and greater than or equal to passing marks and less than or equal to total marks
- Fee amount required, non-negative numeric with two decimal places
- Candidate category required from controlled enumeration matching registration module categories
- Attempt type required as first or subsequent enumeration
- Reject duplicate fee rule for same examination category and attempt type when Active
- Reject eligibility activation when examination master is not Active
- Reject negative fee amounts
- Currency code required from allowed list

##### Calculations

- Effective registration fee lookup key equals examination plus category plus attempt type
- Certificate eligibility evaluation uses max of passing threshold and optional minimum score threshold

##### Workflow

Per section Draft → Active on activate; Active fee row → Inactive on deactivate; Active outcome section → Draft on superseding edit

##### Search requirements

- Filter fee rules by candidate category
- Filter fee rules by attempt type
- Filter fee rules by Active or Inactive status

##### Security

- Restrict outcome and fee configuration to Examination Administrator role
- Audit fee amount changes and eligibility threshold changes
- Fee configuration readable by registration service accounts through authorized integration only

##### Integrations

- Expose Active fee amounts to Module 05 Candidate Registration fee calculation
- Expose result display and certificate eligibility rules to Module 10 Evaluation & Results and Module 11 Certificate Management
- Module 01 authorization hooks

##### Dependencies

- F04-004 — Examination Master Configuration
- F05 — Candidate Registration examination selection and fee flows
- F10 — Evaluation & Results publication behaviour
- F11 — Certificate Management eligibility enforcement
- F01 — Downstream Module Authorization Integration Hooks

##### Assumptions

- Candidate category enumerations align with Module 05 registration categories
- Delayed result display scheduling is enforced in Module 10; this module stores the flag only
- Certificate layout and QR embedding are not configured here

##### Risks

- Fee misconfiguration affects registration revenue or blocks valid registrations
- Eligibility threshold misalignment with passing criteria causes certificate disputes
- Changing fee amounts mid-registration window may require effective-date policy outside this scope

##### Non-functional requirements

- Fee lookup by examination category attempt returns within registration flow tolerance
- All settings stored in MySQL as authoritative configuration
- Activation of fee rules is atomic per row

##### Notes

Configures display and eligibility rules and fee amounts only; result publication UI, certificate layout, and payment processing are out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination outcome and fee settings landing tabbed layout | Medium | 16 |
| UI | Result display rules form with score, pass/fail, and immediate display toggles | Medium | 16 |
| UI | Certificate eligibility rules form with pass requirement and optional minimum score | Medium | 16 |
| UI | Examination fee rule register list with category and attempt type filters | Medium | 16 |
| UI | Create examination fee rule form with category, attempt type, currency, and amount | Medium | 16 |
| UI | Edit examination fee rule amount form | Easy | 14 |
| UI | Deactivate fee rule confirmation dialog | Simple | 5 |
| UI | Combined outcome and fee settings read-only summary panel | Easy | 14 |
| UI | Activate outcome settings confirmation dialog | Simple | 5 |
| UI | Fee rules empty state when no rows configured | Simple | 5 |
| API | Retrieve result display rules for an examination | Easy | 4 |
| API | Save and activate result display rules with validation | Medium | 6 |
| API | Retrieve certificate eligibility rules for an examination | Easy | 4 |
| API | Save and activate certificate eligibility rules with pass alignment validation | Complex | 8 |
| API | List examination fee rules with category and attempt filters | Medium | 6 |
| API | Create examination fee rule with uniqueness validation | Medium | 6 |
| API | Update examination fee rule amount | Easy | 4 |
| API | Deactivate examination fee rule row | Easy | 4 |
| API | Registration fee lookup by examination category and attempt type | Medium | 6 |
| Database | Result display rules entity linked to examination | Easy | 0.25 |
| Database | Certificate eligibility rules entity linked to examination | Easy | 0.25 |
| Database | Examination fee rule entity with category attempt uniqueness | Medium | 0.3 |
| Database | Outcome and fee configuration change audit history | Medium | 0.3 |
| Integration | Registration module fee lookup consumption hook | Simple | 4 |
| Integration | Results and certificate modules eligibility and display rule consumption hook | Simple | 4 |
| Integration | Module 01 authorization hook for outcome and fee mutations | Simple | 4 |
| Testing | Happy-path configure and activate result display, eligibility, and fee rules plus lookup scenarios | Complex | 0.5 |
| Testing | Minimum score below pass, duplicate fee rule, and negative fee amount rejection cases | Medium | 0.3 |
| Testing | Inactive examination block, fee lookup returns zero free rule, and unauthorized access edge cases | Complex | 0.5 |
| Documentation | Administrator runbook for result display, certificate eligibility, and fee maintenance | Medium | 0.3 |
| Documentation | Technical notes for registration fee lookup and downstream rule consumption | Easy | 0.25 |
