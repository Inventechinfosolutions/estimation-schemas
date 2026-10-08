# ChatGPT Visualization Brief — Module 03: Examination Centre Management

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 03 Examination Centre Management
**Features:** 11 (F03-006 … F03-016)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 03 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Centre lifecycle state machine (DRAFT/ACTIVE/INACTIVE)
2. Capacity vs per-session seat vs allocation utilisation diagram
3. Network CIDR + device whitelist enforcement handoff to Module 09
4. Centre–session eligibility mapping ERD
5. Invigilator binding many-to-many diagram
6. Feature relationship / dependency graph within this module and to other modules
7. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Examination Centre Management
**Purpose:** Maintain authorised examination centres: profile, capacity, infrastructure, session eligibility, invigilator binding, network/device restrictions, and allocation summary views.

**Actors (union across features):**
- Examination Administrator

**Feature list:**
- **F03-006** — Authorised Examination Centre Register and Search
- **F03-007** — Add Authorised Examination Centre Profile
- **F03-008** — Edit Authorised Examination Centre Profile
- **F03-009** — Activate and Deactivate Examination Centre
- **F03-010** — Centre Approved Capacity Configuration
- **F03-011** — Centre Infrastructure Details Configuration
- **F03-012** — Approved Examination Session to Centre Mapping
- **F03-013** — Centre Invigilator and Administrator User Binding
- **F03-014** — Authorised Centre Network Restriction Configuration
- **F03-015** — Authorised Centre Device and System Restriction Configuration
- **F03-016** — Centre Candidate Allocation Summary View

### DATA MODEL (from EXAM DB design v2.1)

- `exam_centre`
- `exam_centre_capacity`
- `exam_centre_infrastructure`
- `centre_session_eligibility`
- `centre_network_restriction`
- `centre_device`
- `centre_device_restriction`
- `centre_allocation_summary_cache`
- `staff_user_centre`

### FEATURE CATALOGUE

#### F03-006 — Authorised Examination Centre Register and Search

**One-liner / description:** Provides Examination Administrators with a searchable register of all authorised examination centres showing centre identifier, name, location, approved capacity, active status, and bound invigilator count so only…

**Business objective:** Maintain a single authoritative list of department-approved examination centres and enable administrators to locate centres quickly by identifier, name, district, or operational status.

**Actors:** Examination Administrator

**User journey (10 steps):**
1. Examination Administrator opens Examination Centre Management from the administration menu.
2. System displays the authorised centre register with default sort by centre name.
3. Administrator enters search text matching centre ID, centre name, or city.
4. Administrator applies status filter (Active, Inactive, All).
5. Administrator applies district or region filter when configured.
6. System refreshes the grid with matching centres and total record count.
7. Administrator clicks a centre row to open the centre detail read-only summary panel.
8. Administrator uses pagination to browse additional pages.
9. Administrator clears filters to return to the full register.
10. Administrator navigates to Add Centre or Edit Centre actions from register row actions.

**Functional capabilities:**
- Display paginated authorised centre register with centre ID, name, address summary, approved capacity, active flag, and last modified timestamp
- Search centres by centre ID partial match, centre name, and city or district
- Filter register by active, inactive, or all status
- Filter register by district or region when master data exists
- Open read-only centre summary panel from register row selection
- Expose register row actions for edit, activate/deactivate, and child configuration shortcuts
- Restrict register access to Examination Administrator role
- Exclude inactive centres from downstream scheduling picklists while retaining register visibility

**Inputs:** Search text; Status filter value; District or region filter; Page number and page size; Sort column and direction

**Outputs:** Paginated centre register rows; Total matching record count; Read-only centre summary panel data; Empty-state message when no centres match

**Business rules:**
- Only Examination Administrators may view the full centre register
- Inactive centres remain visible in the register but are flagged and excluded from active scheduling picklists
- Centre ID must be displayed on every register row and is immutable after creation
- Register defaults to active centres first when no filter is applied

**Validations:**
- Reject unauthenticated access to the register
- Reject page size values outside configured maximum
- Sanitise search text to prevent injection in search parameters
- Return empty result set without error when no centres match filters

**Workflow / states:** REGISTER_VIEWED → FILTER_APPLIED → RESULTS_DISPLAYED → ROW_SELECTED → SUMMARY_VIEWED

**Dependencies:**
- F01-002 Examination Administrator Role and Organisation-Wide Permissions
- F01-005 Staff Password Authentication and Login Session

**Risks:** Large centre volumes may require additional index tuning for search responsiveness

---

#### F03-007 — Add Authorised Examination Centre Profile

**One-liner / description:** Allows Examination Administrators to onboard a new authorised examination centre by capturing unique centre ID, centre name, full address, contact details, and initial active status as the foundation profile required…

**Business objective:** Enable controlled creation of new department-approved examination centres with unique identifiers before capacity, infrastructure, user binding, and restriction configuration.

**Actors:** Examination Administrator

**User journey (11 steps):**
1. Administrator opens Add Examination Centre from the centre register.
2. System presents the add centre form with mandatory centre ID and name fields.
3. Administrator enters unique centre ID following department format rules.
4. Administrator enters centre display name.
5. Administrator enters address line, city, district, state, and PIN code.
6. Administrator enters optional contact phone and email for centre coordination.
7. Administrator selects initial status as Active or Inactive.
8. System validates uniqueness of centre ID and mandatory address fields.
9. Administrator submits the form.
10. System persists the centre profile and displays success confirmation with centre ID.
11. System redirects administrator to centre detail or offers shortcuts to capacity and restriction configuration.

**Functional capabilities:**
- Capture unique centre ID with format validation
- Capture centre name and full postal address components
- Capture optional centre contact phone and email
- Set initial active or inactive status on creation
- Validate centre ID uniqueness before persistence
- Persist new centre profile to MySQL as source of truth
- Display post-create confirmation with created centre identifier
- Emit audit record for centre creation event

**Inputs:** Centre ID; Centre name; Address line; City; District; State; PIN code; Contact phone

**Outputs:** Created centre profile record; Success confirmation message; Audit log entry for centre creation

**Business rules:**
- Centre ID must be unique across all centres and immutable after save
- Centre name is mandatory
- Full address including city, district, state, and PIN is mandatory
- Newly created inactive centres are not offered in scheduling picklists
- Only Examination Administrators may create centres

**Validations:**
- Reject duplicate centre ID on create
- Reject blank centre name
- Reject blank city, district, state, or PIN code
- Validate PIN code numeric format and length
- Validate contact email format when provided
- Validate contact phone numeric length when provided

**Workflow / states:** DRAFT_FORM → VALIDATED → CREATED → CONFIRMATION_DISPLAYED

**Dependencies:**
- F03-001 Authorised Examination Centre Register and Search
- F01-002 Examination Administrator Role and Organisation-Wide Permissions

**Risks:** Manual centre ID entry errors if format rules are not enforced strictly

---

#### F03-008 — Edit Authorised Examination Centre Profile

**One-liner / description:** Allows Examination Administrators to update an existing authorised examination centre's name, address, and contact details while preserving immutable centre ID and maintaining audit history of profile changes.

**Business objective:** Keep authorised centre master data accurate when locations, contact points, or display names change without recreating centre records or breaking downstream allocations.

**Actors:** Examination Administrator

**User journey (10 steps):**
1. Administrator locates centre in the register and selects Edit.
2. System loads edit form pre-populated with current centre profile.
3. Centre ID field is displayed read-only.
4. Administrator updates centre name if required.
5. Administrator updates address lines, city, district, state, or PIN.
6. Administrator updates contact phone or email.
7. System validates updated fields on submit.
8. Administrator saves changes.
9. System persists updates and writes audit history.
10. System displays update confirmation and returns to register or detail view.

**Functional capabilities:**
- Load existing centre profile for edit pre-population
- Display centre ID as read-only on edit form
- Update centre name, address components, and contact details
- Validate mandatory address fields on update
- Persist profile changes to MySQL
- Record before-and-after audit history for profile edits
- Block edit of centre ID after creation

**Inputs:** Centre record identifier; Updated centre name; Updated address fields; Updated contact phone; Updated contact email

**Outputs:** Updated centre profile; Profile change audit record; Update confirmation message

**Business rules:**
- Centre ID cannot be changed after creation
- Edited centres retain existing capacity, user bindings, and restriction configuration
- Profile edits do not automatically change active or inactive status
- Audit history must capture changed fields and modifying administrator

**Validations:**
- Reject edit when centre record not found
- Reject blank centre name on update
- Reject blank mandatory address components
- Validate PIN code format on update
- Validate email and phone formats when provided

**Workflow / states:** EDIT_LOADED → MODIFIED → VALIDATED → UPDATED → CONFIRMATION_DISPLAYED

**Dependencies:**
- F03-001 Authorised Examination Centre Register and Search
- F03-002 Add Authorised Examination Centre Profile

**Risks:** Address changes may desynchronise printed hall ticket address until hall ticket regeneration in Module 06

---

#### F03-009 — Activate and Deactivate Examination Centre

**One-liner / description:** Provides Examination Administrators with controlled activate and deactivate actions on authorised examination centres so only active centres appear in scheduling, preference selection, and allocation workflows while…

**Business objective:** Allow departments to temporarily or permanently withdraw centres from operational use without deleting master data or breaking audit and allocation history.

**Actors:** Examination Administrator

**User journey (9 steps):**
1. Administrator opens centre register and locates target centre.
2. Administrator selects Activate or Deactivate action based on current status.
3. System displays confirmation dialog explaining downstream impact.
4. For deactivate, dialog warns that centre will be removed from scheduling picklists and new allocations.
5. Administrator confirms action.
6. System updates centre active flag.
7. System records status change audit entry.
8. Register refreshes showing updated status chip.
9. If centre has future scheduled sessions, system displays advisory warning listing affected session count without blocking unless policy requires.

**Functional capabilities:**
- Activate inactive centre to make it available for scheduling picklists
- Deactivate active centre to exclude from new scheduling and preferences
- Display confirmation dialog before status change
- Show advisory warning when deactivating centre with future approved session mappings
- Persist active flag change with audit history
- Reflect status change immediately in centre register

**Inputs:** Centre record identifier; Target active or inactive status; Administrator confirmation

**Outputs:** Updated centre active flag; Status change audit record; Confirmation message; Advisory warning for future session mappings when applicable

**Business rules:**
- Deactivated centres remain in register with inactive status
- Only active centres are offered in candidate preference and scheduling picklists
- Deactivation does not delete centre profile, capacity, or restriction configuration
- Reactivation restores centre to active picklists without data loss
- Existing candidate allocations to a deactivated centre are not auto-migrated in this module

**Validations:**
- Reject activate when centre is already active
- Reject deactivate when centre is already inactive
- Require explicit administrator confirmation before status change
- Reject status change by unauthorized roles

**Workflow / states:** ACTIVE ↔ INACTIVE via ADMIN_CONFIRMED_STATUS_CHANGE

**Dependencies:**
- F03-001 Authorised Examination Centre Register and Search
- F03-007 Approved Examination Session to Centre Mapping

**Risks:** Deactivating centres with pending allocations may require manual intervention in scheduling module

---

#### F03-010 — Centre Approved Capacity Configuration

**One-liner / description:** Allows Examination Administrators to configure approved candidate capacity and per-session seat limits for each authorised examination centre as required by §17 and §18.1 approved capacity attributes supporting…

**Business objective:** Define how many candidates each centre can accommodate overall and per examination session so scheduling and allocation modules enforce capacity limits.

**Actors:** Examination Administrator

**User journey (9 steps):**
1. Administrator opens centre detail and selects Capacity Configuration.
2. System displays current approved total capacity and per-session capacity values.
3. Administrator enters approved total candidate capacity for the centre.
4. Administrator enters default maximum seats per examination session at the centre.
5. Administrator optionally enters concurrent session capacity limit if multiple parallel sessions are supported.
6. System validates capacity values are positive integers and per-session capacity does not exceed total capacity.
7. Administrator saves capacity configuration.
8. System persists values and displays confirmation.
9. System shows current allocated candidate count versus capacity for awareness.

**Functional capabilities:**
- Configure approved total candidate capacity per centre
- Configure default maximum seats per examination session at centre
- Configure concurrent session capacity limit when applicable
- Display current allocated candidate count against configured capacity
- Validate capacity values against business rules before save
- Persist capacity configuration to MySQL
- Expose capacity values to scheduling and allocation modules

**Inputs:** Centre record identifier; Approved total capacity; Per-session seat capacity; Concurrent session limit; Effective date optional

**Outputs:** Updated capacity configuration; Capacity utilisation summary display; Audit record for capacity changes

**Business rules:**
- Approved total capacity must be a positive integer
- Per-session seat capacity must not exceed approved total capacity
- Capacity configuration applies only to active centres for new allocations
- Reducing capacity below current allocated count displays warning but does not auto-reallocate
- Capacity values are used by Module 06 allocation engine as constraints

**Validations:**
- Reject zero or negative capacity values
- Reject non-integer capacity entries
- Reject per-session capacity greater than total approved capacity
- Reject capacity update for non-existent centre

**Workflow / states:** CAPACITY_VIEWED → VALUES_ENTERED → VALIDATED → SAVED → UTILISATION_DISPLAYED

**Dependencies:**
- F03-002 Add Authorised Examination Centre Profile
- F06-002 Candidate Centre and Session Allocation

**Risks:** Capacity reduction after allocations may cause scheduling conflicts requiring manual resolution

---

#### F03-011 — Centre Infrastructure Details Configuration

**One-liner / description:** Allows Examination Administrators to record centre infrastructure attributes such as number of examination rooms, computer terminals, backup power, internet connectivity, and accessibility features supporting…

**Business objective:** Capture structured infrastructure metadata for each authorised centre to support capacity planning, centre approval reviews, and operational readiness assessment.

**Actors:** Examination Administrator

**User journey (11 steps):**
1. Administrator navigates to centre detail Infrastructure tab.
2. System displays current infrastructure profile or empty state for new centres.
3. Administrator enters number of examination rooms.
4. Administrator enters total authorised computer terminals available.
5. Administrator selects backup power availability yes or no.
6. Administrator selects internet connectivity type and bandwidth category.
7. Administrator enters accessibility and special facility notes.
8. Administrator enters optional infrastructure remarks for audit reviewers.
9. System validates numeric fields and mandatory selections.
10. Administrator saves infrastructure profile.
11. System persists configuration and shows confirmation.

**Functional capabilities:**
- Capture number of examination rooms per centre
- Capture total authorised computer terminal count
- Record backup power availability flag
- Record internet connectivity type and bandwidth category
- Capture accessibility and facility notes as free text
- Capture infrastructure remarks for administrative review
- Validate terminal count against per-session capacity when both configured
- Persist infrastructure profile linked to centre master

**Inputs:** Centre record identifier; Examination room count; Computer terminal count; Backup power flag; Internet connectivity type; Bandwidth category; Accessibility notes; Infrastructure remarks

**Outputs:** Updated centre infrastructure profile; Infrastructure validation warnings; Audit record for infrastructure changes

**Business rules:**
- Computer terminal count should not be less than per-session seat capacity when both are configured
- Infrastructure details are informational for administration and do not enforce runtime access
- All infrastructure fields may be updated independently of centre active status
- Empty infrastructure profile is allowed for newly created centres

**Validations:**
- Reject negative room or terminal counts
- Reject non-integer room and terminal counts
- Warn when terminal count is less than configured per-session capacity
- Validate connectivity type against allowed enumeration

**Workflow / states:** INFRASTRUCTURE_VIEWED → FIELDS_ENTERED → VALIDATED → SAVED

**Dependencies:**
- F03-002 Add Authorised Examination Centre Profile
- F03-005 Centre Approved Capacity Configuration

**Risks:** Stale infrastructure data if centres upgrade hardware without admin update

---

#### F03-012 — Approved Examination Session to Centre Mapping

**One-liner / description:** Allows Examination Administrators to define which examination sessions each authorised centre is approved to host, fulfilling §17 map examination sessions to centres and §18.1 approved examination sessions…

**Business objective:** Establish explicit approval matrix between centres and examination sessions preventing unapproved centre-session combinations during scheduling and allocation.

**Actors:** Examination Administrator

**User journey (10 steps):**
1. Administrator opens centre detail Approved Sessions tab.
2. System lists examination sessions currently approved for the centre.
3. Administrator clicks Add Approved Session.
4. System displays searchable list of available examination sessions from examination master excluding already mapped sessions.
5. Administrator selects one or more sessions to approve for the centre.
6. System validates centre is active and session is open for scheduling.
7. Administrator confirms mapping.
8. System persists centre-session approval records.
9. Administrator may remove an approved session mapping via remove action with confirmation.
10. Removed mappings no longer appear in scheduling picklists for that centre.

**Functional capabilities:**
- List approved examination sessions for a selected centre
- Search available examination sessions for approval mapping
- Add approved session mapping between centre and examination session
- Remove approved session mapping with confirmation
- Validate centre active status before new mapping
- Exclude already mapped sessions from add picker
- Expose approved session list to scheduling module picklists
- Audit all mapping add and remove actions

**Inputs:** Centre record identifier; Examination session identifier; Mapping effective date optional; Remove mapping confirmation

**Outputs:** Centre-session approval mapping list; Updated mapping after add or remove; Mapping change audit records

**Business rules:**
- Only active centres may receive new session approvals
- A centre-session pair may be mapped only once
- Removed mappings do not delete historical scheduling records
- Approved sessions determine which sessions appear when scheduling at this centre
- Examination session master originates from Module 04 and Module 06

**Validations:**
- Reject duplicate centre-session mapping
- Reject mapping to inactive centre
- Reject mapping when examination session not found or closed
- Require confirmation before removing mapping with future scheduled instances

**Workflow / states:** MAPPING_LIST_VIEWED → SESSION_SELECTED → MAPPING_CREATED → MAPPING_LIST_UPDATED; MAPPING_REMOVED via ADMIN_CONFIRMED_REMOVE

**Dependencies:**
- F03-001 Authorised Examination Centre Register and Search
- F04-004 Examination Master Configuration
- F06-001 Examination Schedule Creation and Maintenance

**Risks:** Removing approval for sessions with existing schedules may cause scheduling inconsistencies

---

#### F03-013 — Centre Invigilator and Administrator User Binding

**One-liner / description:** Allows Examination Administrators to bind centre invigilator and centre administrator users to a specific authorised examination centre fulfilling §17 configure centre-specific users and §18.1 centre administrator or…

**Business objective:** Ensure each authorised centre has designated invigilator and administrator users who receive centre-scoped access for centre operations while user account creation remains in User and Role Management.

**Actors:** Examination Administrator

**User journey (10 steps):**
1. Administrator opens centre detail Centre Users tab.
2. System lists currently bound invigilator and administrator users for the centre.
3. Administrator clicks Bind User.
4. System opens searchable picker of existing centre invigilator role users from user register.
5. Administrator selects user and assigns binding role type as Invigilator or Centre Administrator.
6. System validates user is active and not already bound to the same centre with same role.
7. Administrator confirms binding.
8. System persists centre-user binding record.
9. Administrator may unbind a user via remove action with confirmation when no active centre-day session dependency exists.
10. Bound users gain centre-scoped visibility per access model in Module 01.

**Functional capabilities:**
- List centre-bound invigilator and administrator users for a centre
- Search existing centre invigilator role users for binding picker
- Bind user to centre with Invigilator or Centre Administrator role type
- Unbind user from centre with confirmation
- Prevent duplicate binding of same user to same centre
- Validate bound user account is active in user register
- Expose binding data to centre-scoped access enforcement in Module 01 and Module 08
- Audit bind and unbind actions

**Inputs:** Centre record identifier; User account identifier; Binding role type Invigilator or Centre Administrator; Unbind confirmation

**Outputs:** Centre-user binding list; New or removed binding records; Binding change audit entries

**Business rules:**
- User account must exist in centre invigilator user register before binding
- A user may be bound to multiple centres if policy allows
- Same user cannot have duplicate binding role at same centre
- At least one invigilator binding is recommended before centre activation for operations
- Unbinding does not delete user account in Module 01

**Validations:**
- Reject binding inactive or locked user accounts
- Reject duplicate centre-user-role binding
- Reject binding users without centre invigilator role assignment
- Warn on unbind when user has scheduled centre-day duties

**Workflow / states:** BINDING_LIST_VIEWED → USER_SELECTED → BINDING_CREATED → BINDING_LIST_UPDATED; BINDING_REMOVED via ADMIN_CONFIRMED_UNBIND

**Dependencies:**
- F01-003 Centre Invigilator Role and Centre-Scoped Access Model
- F01-007 Centre Invigilator User Register Centre Binding and Lifecycle
- F03-002 Add Authorised Examination Centre Profile

**Risks:** Unbinding sole invigilator before examination day may block centre operations

---

#### F03-014 — Authorised Centre Network Restriction Configuration

**One-liner / description:** Allows Examination Administrators to configure authorised network identifiers such as IP ranges or network tags for each examination centre as part of §18.1 authorised systems, devices, and network configuration,…

**Business objective:** Capture centre-specific authorised network parameters so examination access can be restricted to approved centre networks during secure examination conduct.

**Actors:** Examination Administrator

**User journey (10 steps):**
1. Administrator opens centre detail Network Restrictions tab.
2. System lists configured network entries for the centre.
3. Administrator clicks Add Network Entry.
4. Administrator selects restriction type as single IP, IP range, or CIDR block.
5. Administrator enters network value and optional descriptive label.
6. System validates IP and CIDR format.
7. Administrator saves network entry.
8. System persists entry linked to centre.
9. Administrator may deactivate or delete a network entry with confirmation.
10. Configured entries are flagged as active or inactive for downstream enforcement handoff.

**Functional capabilities:**
- List authorised network restriction entries per centre
- Add single IP, IP range, or CIDR network restriction entry
- Edit network entry label and value
- Deactivate network entry without deleting audit history
- Validate IP address and CIDR format on entry
- Prevent overlapping duplicate network entries for same centre
- Expose active network restriction set to Secure Examination Conduct module
- Audit network configuration changes

**Inputs:** Centre record identifier; Restriction type; IP address or range or CIDR value; Descriptive label; Active flag

**Outputs:** Centre network restriction entry list; Validated network configuration records; Network configuration audit entries

**Business rules:**
- Network restriction configuration is stored here and enforced at runtime in Module 09
- At least one active network entry is recommended before centre examination conduct
- Inactive network entries are retained for audit but excluded from enforcement handoff
- Network configuration is centre-specific and not shared across centres
- Final technical mechanism may combine network with device restrictions per client infrastructure

**Validations:**
- Validate IPv4 address format for single IP entries
- Validate CIDR notation format and prefix length bounds
- Validate IP range start is less than or equal to range end
- Reject duplicate identical network entry for same centre
- Reject blank network value

**Workflow / states:** NETWORK_LIST_VIEWED → ENTRY_ADDED → VALIDATED → SAVED → ACTIVE_FOR_ENFORCEMENT_HANDOFF; ENTRY_DEACTIVATED via ADMIN_ACTION

**Dependencies:**
- F03-002 Add Authorised Examination Centre Profile
- F09-002 Authorised Centre Device and Network Enforcement

**Risks:** Incorrect IP or CIDR entry may block all centre candidates at examination time

---

#### F03-015 — Authorised Centre Device and System Restriction Configuration

**One-liner / description:** Allows Examination Administrators to register authorised examination devices or system identifiers such as hostname, MAC address, or asset tag for each centre per §18.1 authorised systems and devices configuration,…

**Business objective:** Maintain a centre-specific authorised device inventory so candidates can attempt examinations only from approved centre computers.

**Actors:** Examination Administrator

**User journey (11 steps):**
1. Administrator opens centre detail Authorised Devices tab.
2. System lists registered devices for the centre with identifier, label, and status.
3. Administrator clicks Register Device.
4. Administrator selects device identifier type as MAC address, hostname, or asset tag.
5. Administrator enters identifier value and optional seat or room label.
6. System validates identifier format based on type.
7. Administrator saves device entry.
8. System persists device record linked to centre.
9. Administrator may bulk import device list via file upload when many terminals exist.
10. Administrator may deactivate device entry when hardware is retired.
11. Active device list is available for Module 09 enforcement handoff.

**Functional capabilities:**
- List authorised device entries per centre with status
- Register single device with MAC, hostname, or asset tag identifier
- Edit device label and seat or room assignment
- Deactivate device entry preserving audit history
- Bulk import device identifiers from approved file format
- Validate MAC address and hostname formats
- Prevent duplicate device identifier within same centre
- Expose active device whitelist to Secure Examination Conduct module

**Inputs:** Centre record identifier; Device identifier type; Identifier value; Seat or room label; Bulk import file; Active flag

**Outputs:** Centre device register list; Imported device registration results summary; Device configuration audit records

**Business rules:**
- Device restriction configuration is stored here and enforced at runtime in Module 09
- Device identifier must be unique within a centre
- Deactivated devices are excluded from enforcement whitelist
- Bulk import validates each row and reports failures without partial silent skip
- Device count should align with infrastructure terminal count for operational readiness

**Validations:**
- Validate MAC address format XX:XX:XX:XX:XX:XX or equivalent
- Validate hostname length and allowed character set
- Reject duplicate device identifier at same centre
- Validate bulk import file format and row-level identifier formats
- Reject blank identifier value

**Workflow / states:** DEVICE_LIST_VIEWED → DEVICE_REGISTERED → VALIDATED → SAVED; BULK_IMPORT_SUBMITTED → ROWS_VALIDATED → IMPORT_COMPLETED; DEVICE_DEACTIVATED

**Dependencies:**
- F03-002 Add Authorised Examination Centre Profile
- F03-006 Centre Infrastructure Details Configuration
- F09-002 Authorised Centre Device and Network Enforcement

**Risks:** Incorrect MAC or hostname entries may deny legitimate centre devices at examination time

---

#### F03-016 — Centre Candidate Allocation Summary View

**One-liner / description:** Provides Examination Administrators with read-only visibility of candidate allocation summaries per authorised examination centre including allocated candidate counts by examination and session as required by §17…

**Business objective:** Enable administrators to monitor how candidates are distributed across centres for operational planning without performing allocation actions in the centre management module.

**Actors:** Examination Administrator

**User journey (8 steps):**
1. Administrator opens centre detail Allocation Summary tab or selects View Allocations from register.
2. System displays summary cards with total allocated candidates, upcoming session count, and capacity utilisation.
3. Administrator selects examination filter to narrow summary.
4. System refreshes allocation grid showing examination name, session date, allocated count, and remaining seats.
5. Administrator clicks a session row to expand candidate count breakdown by category if available.
6. Administrator exports allocation summary to spreadsheet when required.
7. Administrator navigates to scheduling module via link for allocation changes.
8. Summary reflects latest allocation state from scheduling module data.

**Functional capabilities:**
- Display total allocated candidate count per centre
- Display allocation breakdown by examination and session
- Show remaining seat capacity per session against centre capacity configuration
- Filter allocation summary by examination and date range
- Expand session row for category-wise allocated count when data available
- Export allocation summary to approved spreadsheet format
- Provide deep link to scheduling module for allocation management
- Refresh summary from current scheduling allocation records

**Inputs:** Centre record identifier; Examination filter; Date range filter; Export format selection

**Outputs:** Centre allocation summary cards; Session-wise allocation grid; Category breakdown when available; Exported allocation summary file

**Business rules:**
- Allocation summary is read-only in this module
- Allocation execution and changes occur in Module 06
- Utilisation compares allocated count to centre capacity from Module 03 configuration
- Only allocated candidates for active and scheduled sessions appear
- Summary excludes candidates with only preferences not yet allocated

**Validations:**
- Reject access by non-administrator roles
- Validate date range filter start precedes end
- Return empty grid without error when no allocations exist for centre

**Workflow / states:** SUMMARY_LOADED → FILTER_APPLIED → GRID_DISPLAYED → ROW_EXPANDED → EXPORT_GENERATED

**Dependencies:**
- F03-005 Centre Approved Capacity Configuration
- F06-002 Candidate Centre and Session Allocation

**Risks:** Summary staleness if allocation changes occur during viewing; refresh on tab focus mitigates

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 03 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 03 Examination Centre Management** (11 features).
> Features: F03-006 Authorised Examination Centre Register and Search; F03-007 Add Authorised Examination Centre Profile; F03-008 Edit Authorised Examination Centre Profile; F03-009 Activate and Deactivate Examination Centre; F03-010 Centre Approved Capacity Configuration; F03-011 Centre Infrastructure Details Configuration; F03-012 Approved Examination Session to Centre Mapping; F03-013 Centre Invigilator and Administrator User Binding; F03-014 Authorised Centre Network Restriction Configuration; F03-015 Authorised Centre Device and System Restriction Configuration; F03-016 Centre Candidate Allocation Summary View.
> Purpose: Maintain authorised examination centres: profile, capacity, infrastructure, session eligibility, invigilator binding, network/device restrictions, and allocation summary views.
> Draw: Centre lifecycle state machine (DRAFT/ACTIVE/INACTIVE); Capacity vs per-session seat vs allocation utilisation diagram; Network CIDR + device whitelist enforcement handoff to Module 09; Centre–session eligibility mapping ERD; ERD for `exam_centre`, `exam_centre_capacity`, `exam_centre_infrastructure`, `centre_session_eligibility`, `centre_network_restriction`, `centre_device`.
