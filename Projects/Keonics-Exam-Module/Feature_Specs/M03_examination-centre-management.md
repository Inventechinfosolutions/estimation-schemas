# Module 03: Examination Centre Management

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 11 (F03-006 … F03-016)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 03 Examination Centre Management

904.85 hours · 177 tasks · Business

Master management of authorised examination centres, capacity, centre users, and centre-level access configuration.

### F03-006 Authorised Examination Centre Register and Search

90.7 hours · Go-live · 18 tasks

##### Description

Provides Examination Administrators with a searchable register of all authorised examination centres showing centre identifier, name, location, approved capacity, active status, and bound invigilator count so only configured centres are visible for downstream scheduling and preference selection.

##### Business objective

Maintain a single authoritative list of department-approved examination centres and enable administrators to locate centres quickly by identifier, name, district, or operational status.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

- Display paginated authorised centre register with centre ID, name, address summary, approved capacity, active flag, and last modified timestamp
- Search centres by centre ID partial match, centre name, and city or district
- Filter register by active, inactive, or all status
- Filter register by district or region when master data exists
- Open read-only centre summary panel from register row selection
- Expose register row actions for edit, activate/deactivate, and child configuration shortcuts
- Restrict register access to Examination Administrator role
- Exclude inactive centres from downstream scheduling picklists while retaining register visibility

##### Inputs

- Search text
- Status filter value
- District or region filter
- Page number and page size
- Sort column and direction

##### Outputs

- Paginated centre register rows
- Total matching record count
- Read-only centre summary panel data
- Empty-state message when no centres match

##### Business rules

- Only Examination Administrators may view the full centre register
- Inactive centres remain visible in the register but are flagged and excluded from active scheduling picklists
- Centre ID must be displayed on every register row and is immutable after creation
- Register defaults to active centres first when no filter is applied

##### Validations

- Reject unauthenticated access to the register
- Reject page size values outside configured maximum
- Sanitise search text to prevent injection in search parameters
- Return empty result set without error when no centres match filters

##### Calculations

- Compute total matching centre count for pagination footer

##### Workflow

REGISTER_VIEWED → FILTER_APPLIED → RESULTS_DISPLAYED → ROW_SELECTED → SUMMARY_VIEWED

##### Search requirements

- Partial match on centre ID
- Partial match on centre name
- Partial match on city or district
- Exact match on active or inactive status

##### Security

- Role-gated access for Examination Administrator only
- Audit log entry when register export is invoked if export is enabled

##### Integrations

- Read centre master records from MySQL as source of truth

##### Dependencies

- F01-002 Examination Administrator Role and Organisation-Wide Permissions
- F01-005 Staff Password Authentication and Login Session

##### Assumptions

- District or region master exists or is optional text filter
- Centre register volume is moderate and server-side pagination is sufficient

##### Risks

- Large centre volumes may require additional index tuning for search responsiveness

##### Non-functional requirements

- Register search response within acceptable admin UI latency
- Accessible table headers and filter controls

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Authorised centre register list with centre ID, name, address summary, capacity, and status chips | Medium | 16 |
| UI | Centre register search bar with ID, name, and city partial match | Easy | 14 |
| UI | Centre register status filter control for active, inactive, and all | Simple | 5 |
| UI | Centre register district or region filter dropdown | Easy | 14 |
| UI | Centre register empty state when no centres match filters | Simple | 5 |
| UI | Read-only centre summary side panel opened from register row | Easy | 14 |
| UI | Centre register pagination footer with total count | Simple | 5 |
| API | List authorised centres with pagination defaults | Easy | 4 |
| API | Search authorised centres by ID, name, city, and district | Medium | 6 |
| API | Filter authorised centres by active or inactive status | Easy | 4 |
| API | Fetch single centre summary for register row detail panel | Simple | 2 |
| Database | Authorised examination centre core entity persistence | Medium | 0.3 |
| Database | Search indexes on centre ID, name, city, and active flag | Easy | 0.25 |
| Testing | Register list, search, and filter happy-path scenarios | Medium | 0.3 |
| Testing | Unauthorized role rejection for centre register access | Easy | 0.25 |
| Testing | Empty search result and invalid pagination parameter handling | Easy | 0.25 |
| Documentation | Administrator runbook for centre register search and filters | Easy | 0.25 |
| Documentation | Technical notes for centre register query and indexing | Simple | 0.1 |

### F03-007 Add Authorised Examination Centre Profile

70.95 hours · Go-live · 16 tasks

##### Description

Allows Examination Administrators to onboard a new authorised examination centre by capturing unique centre ID, centre name, full address, contact details, and initial active status as the foundation profile required by §18.1 centre-based examination access configuration.

##### Business objective

Enable controlled creation of new department-approved examination centres with unique identifiers before capacity, infrastructure, user binding, and restriction configuration.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

- Capture unique centre ID with format validation
- Capture centre name and full postal address components
- Capture optional centre contact phone and email
- Set initial active or inactive status on creation
- Validate centre ID uniqueness before persistence
- Persist new centre profile to MySQL as source of truth
- Display post-create confirmation with created centre identifier
- Emit audit record for centre creation event

##### Inputs

- Centre ID
- Centre name
- Address line
- City
- District
- State
- PIN code
- Contact phone
- Contact email
- Initial active flag

##### Outputs

- Created centre profile record
- Success confirmation message
- Audit log entry for centre creation

##### Business rules

- Centre ID must be unique across all centres and immutable after save
- Centre name is mandatory
- Full address including city, district, state, and PIN is mandatory
- Newly created inactive centres are not offered in scheduling picklists
- Only Examination Administrators may create centres

##### Validations

- Reject duplicate centre ID on create
- Reject blank centre name
- Reject blank city, district, state, or PIN code
- Validate PIN code numeric format and length
- Validate contact email format when provided
- Validate contact phone numeric length when provided

##### Workflow

DRAFT_FORM → VALIDATED → CREATED → CONFIRMATION_DISPLAYED

##### Search requirements

- Duplicate centre ID check on blur or submit

##### Security

- Examination Administrator role required
- Audit trail for centre creation with actor and timestamp

##### Dependencies

- F03-001 Authorised Examination Centre Register and Search
- F01-002 Examination Administrator Role and Organisation-Wide Permissions

##### Assumptions

- Centre ID format rules are defined by department policy
- No bulk import of centres in this module scope

##### Risks

- Manual centre ID entry errors if format rules are not enforced strictly

##### Non-functional requirements

- Form submission completes within standard admin transaction time
- Clear inline validation messages on field blur

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Add authorised examination centre form with centre ID and name fields | Medium | 16 |
| UI | Add centre address section with city, district, state, and PIN fields | Medium | 16 |
| UI | Add centre optional contact phone and email fields | Easy | 14 |
| UI | Add centre initial active or inactive status selector | Simple | 5 |
| UI | Add centre duplicate ID inline error display | Simple | 5 |
| UI | Add centre success confirmation dialog with created centre ID | Simple | 5 |
| API | Create authorised examination centre with uniqueness validation | Medium | 6 |
| API | Lookup centre ID availability before create submit | Simple | 2 |
| Database | Authorised centre profile insert with address and contact columns | Easy | 0.25 |
| Database | Unique constraint on centre ID column | Easy | 0.25 |
| Database | Centre creation audit history record | Easy | 0.25 |
| Testing | Successful centre create with all mandatory fields happy path | Medium | 0.3 |
| Testing | Duplicate centre ID and missing address field rejection cases | Medium | 0.3 |
| Testing | Unauthorized create attempt and audit log verification | Easy | 0.25 |
| Documentation | Administrator runbook for adding a new authorised centre | Easy | 0.25 |
| Documentation | Technical notes for centre ID uniqueness and audit persistence | Simple | 0.1 |

### F03-008 Edit Authorised Examination Centre Profile

67.7 hours · Go-live · 14 tasks

##### Description

Allows Examination Administrators to update an existing authorised examination centre's name, address, and contact details while preserving immutable centre ID and maintaining audit history of profile changes.

##### Business objective

Keep authorised centre master data accurate when locations, contact points, or display names change without recreating centre records or breaking downstream allocations.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

- Load existing centre profile for edit pre-population
- Display centre ID as read-only on edit form
- Update centre name, address components, and contact details
- Validate mandatory address fields on update
- Persist profile changes to MySQL
- Record before-and-after audit history for profile edits
- Block edit of centre ID after creation

##### Inputs

- Centre record identifier
- Updated centre name
- Updated address fields
- Updated contact phone
- Updated contact email

##### Outputs

- Updated centre profile
- Profile change audit record
- Update confirmation message

##### Business rules

- Centre ID cannot be changed after creation
- Edited centres retain existing capacity, user bindings, and restriction configuration
- Profile edits do not automatically change active or inactive status
- Audit history must capture changed fields and modifying administrator

##### Validations

- Reject edit when centre record not found
- Reject blank centre name on update
- Reject blank mandatory address components
- Validate PIN code format on update
- Validate email and phone formats when provided

##### Workflow

EDIT_LOADED → MODIFIED → VALIDATED → UPDATED → CONFIRMATION_DISPLAYED

##### Security

- Examination Administrator role required
- Audit trail for each profile field change

##### Dependencies

- F03-001 Authorised Examination Centre Register and Search
- F03-002 Add Authorised Examination Centre Profile

##### Assumptions

- Concurrent edit by two administrators is rare; last-save-wins acceptable

##### Risks

- Address changes may desynchronise printed hall ticket address until hall ticket regeneration in Module 06

##### Non-functional requirements

- Edit form load within standard admin latency
- Optimistic UI feedback on save

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Edit authorised examination centre form with read-only centre ID | Medium | 16 |
| UI | Edit centre address section with validation messages | Medium | 16 |
| UI | Edit centre contact phone and email fields | Easy | 14 |
| UI | Edit centre unsaved changes navigation warning dialog | Simple | 5 |
| UI | Edit centre save success toast or confirmation banner | Simple | 5 |
| API | Fetch centre profile by identifier for edit pre-population | Easy | 4 |
| API | Update centre profile with field-level validation | Medium | 6 |
| Database | Centre profile update persistence for name, address, and contact | Easy | 0.25 |
| Database | Centre profile change audit history with before and after values | Medium | 0.3 |
| Testing | Successful profile update happy path with audit verification | Medium | 0.3 |
| Testing | Missing mandatory address field rejection on update | Easy | 0.25 |
| Testing | Centre ID immutability enforcement on edit submit | Easy | 0.25 |
| Documentation | Administrator runbook for editing centre profile details | Easy | 0.25 |
| Documentation | Technical notes for centre profile audit history | Simple | 0.1 |

### F03-009 Activate and Deactivate Examination Centre

44.5 hours · Go-live · 14 tasks

##### Description

Provides Examination Administrators with controlled activate and deactivate actions on authorised examination centres so only active centres appear in scheduling, preference selection, and allocation workflows while preserving historical centre records.

##### Business objective

Allow departments to temporarily or permanently withdraw centres from operational use without deleting master data or breaking audit and allocation history.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre register and locates target centre.
2. Administrator selects Activate or Deactivate action based on current status.
3. System displays confirmation dialog explaining downstream impact.
4. For deactivate, dialog warns that centre will be removed from scheduling picklists and new allocations.
5. Administrator confirms action.
6. System updates centre active flag.
7. System records status change audit entry.
8. Register refreshes showing updated status chip.
9. If centre has future scheduled sessions, system displays advisory warning listing affected session count without blocking unless policy requires.

##### Functional capabilities

- Activate inactive centre to make it available for scheduling picklists
- Deactivate active centre to exclude from new scheduling and preferences
- Display confirmation dialog before status change
- Show advisory warning when deactivating centre with future approved session mappings
- Persist active flag change with audit history
- Reflect status change immediately in centre register

##### Inputs

- Centre record identifier
- Target active or inactive status
- Administrator confirmation

##### Outputs

- Updated centre active flag
- Status change audit record
- Confirmation message
- Advisory warning for future session mappings when applicable

##### Business rules

- Deactivated centres remain in register with inactive status
- Only active centres are offered in candidate preference and scheduling picklists
- Deactivation does not delete centre profile, capacity, or restriction configuration
- Reactivation restores centre to active picklists without data loss
- Existing candidate allocations to a deactivated centre are not auto-migrated in this module

##### Validations

- Reject activate when centre is already active
- Reject deactivate when centre is already inactive
- Require explicit administrator confirmation before status change
- Reject status change by unauthorized roles

##### Calculations

- Count future approved session mappings for deactivate advisory warning

##### Workflow

ACTIVE ↔ INACTIVE via ADMIN_CONFIRMED_STATUS_CHANGE

##### Security

- Examination Administrator role required
- Audit log for every activate and deactivate action

##### Dependencies

- F03-001 Authorised Examination Centre Register and Search
- F03-007 Approved Examination Session to Centre Mapping

##### Assumptions

- Policy allows deactivation with existing future mappings subject to manual rescheduling in Module 06

##### Risks

- Deactivating centres with pending allocations may require manual intervention in scheduling module

##### Non-functional requirements

- Status change reflected in register within one refresh cycle

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Deactivate examination centre confirmation dialog with impact summary | Simple | 5 |
| UI | Activate examination centre confirmation dialog | Simple | 5 |
| UI | Centre status chip toggle refresh on register row after action | Simple | 5 |
| UI | Future session mapping advisory warning panel on deactivate | Easy | 14 |
| API | Activate authorised examination centre status flag | Easy | 4 |
| API | Deactivate authorised examination centre status flag | Easy | 4 |
| API | Fetch future session mapping count for deactivate advisory | Medium | 6 |
| Database | Centre active flag update persistence | Simple | 0.1 |
| Database | Centre status change audit history record | Easy | 0.25 |
| Testing | Activate and deactivate happy-path status transitions | Medium | 0.3 |
| Testing | Duplicate activate or deactivate rejection cases | Easy | 0.25 |
| Testing | Unauthorized status change attempt rejection | Easy | 0.25 |
| Documentation | Administrator runbook for centre activation and deactivation policy | Easy | 0.25 |
| Documentation | Technical notes for centre status flag downstream picklist exclusion | Simple | 0.1 |

### F03-010 Centre Approved Capacity Configuration

80.95 hours · Go-live · 14 tasks

##### Description

Allows Examination Administrators to configure approved candidate capacity and per-session seat limits for each authorised examination centre as required by §17 and §18.1 approved capacity attributes supporting allocation and scheduling constraints.

##### Business objective

Define how many candidates each centre can accommodate overall and per examination session so scheduling and allocation modules enforce capacity limits.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre detail and selects Capacity Configuration.
2. System displays current approved total capacity and per-session capacity values.
3. Administrator enters approved total candidate capacity for the centre.
4. Administrator enters default maximum seats per examination session at the centre.
5. Administrator optionally enters concurrent session capacity limit if multiple parallel sessions are supported.
6. System validates capacity values are positive integers and per-session capacity does not exceed total capacity.
7. Administrator saves capacity configuration.
8. System persists values and displays confirmation.
9. System shows current allocated candidate count versus capacity for awareness.

##### Functional capabilities

- Configure approved total candidate capacity per centre
- Configure default maximum seats per examination session at centre
- Configure concurrent session capacity limit when applicable
- Display current allocated candidate count against configured capacity
- Validate capacity values against business rules before save
- Persist capacity configuration to MySQL
- Expose capacity values to scheduling and allocation modules

##### Inputs

- Centre record identifier
- Approved total capacity
- Per-session seat capacity
- Concurrent session limit
- Effective date optional

##### Outputs

- Updated capacity configuration
- Capacity utilisation summary display
- Audit record for capacity changes

##### Business rules

- Approved total capacity must be a positive integer
- Per-session seat capacity must not exceed approved total capacity
- Capacity configuration applies only to active centres for new allocations
- Reducing capacity below current allocated count displays warning but does not auto-reallocate
- Capacity values are used by Module 06 allocation engine as constraints

##### Validations

- Reject zero or negative capacity values
- Reject non-integer capacity entries
- Reject per-session capacity greater than total approved capacity
- Reject capacity update for non-existent centre

##### Calculations

- Compute remaining capacity as approved total minus current allocated count
- Compute utilisation percentage for display

##### Workflow

CAPACITY_VIEWED → VALUES_ENTERED → VALIDATED → SAVED → UTILISATION_DISPLAYED

##### Security

- Examination Administrator role required
- Audit log for capacity configuration changes

##### Integrations

- Read current allocated candidate count from scheduling allocation data

##### Dependencies

- F03-002 Add Authorised Examination Centre Profile
- F06-002 Candidate Centre and Session Allocation

##### Assumptions

- Allocated count is read-only summary sourced from Module 06
- Concurrent session limit is optional based on centre infrastructure

##### Risks

- Capacity reduction after allocations may cause scheduling conflicts requiring manual resolution

##### Non-functional requirements

- Capacity save transaction is atomic
- Utilisation summary refreshes on save

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre approved total capacity configuration form | Medium | 16 |
| UI | Centre per-session seat capacity configuration field | Easy | 14 |
| UI | Centre concurrent session capacity limit field | Easy | 14 |
| UI | Centre capacity utilisation summary bar showing allocated versus approved | Medium | 16 |
| UI | Capacity reduction below allocated count warning dialog | Simple | 5 |
| API | Fetch centre capacity configuration and utilisation summary | Medium | 6 |
| API | Update centre approved total and per-session capacity with validation | Complex | 8 |
| Database | Centre capacity configuration entity with total and session limits | Medium | 0.3 |
| Database | Centre capacity change audit history | Easy | 0.25 |
| Testing | Capacity save happy path with utilisation display refresh | Medium | 0.3 |
| Testing | Per-session capacity exceeding total capacity rejection | Medium | 0.3 |
| Testing | Zero and negative capacity value rejection cases | Easy | 0.25 |
| Documentation | Administrator runbook for centre capacity configuration rules | Easy | 0.25 |
| Documentation | Technical notes for capacity constraint handoff to allocation module | Medium | 0.3 |

### F03-011 Centre Infrastructure Details Configuration

65.7 hours · Go-live · 14 tasks

##### Description

Allows Examination Administrators to record centre infrastructure attributes such as number of examination rooms, computer terminals, backup power, internet connectivity, and accessibility features supporting operational planning and centre approval decisions per §17 infrastructure detail configuration.

##### Business objective

Capture structured infrastructure metadata for each authorised centre to support capacity planning, centre approval reviews, and operational readiness assessment.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

- Capture number of examination rooms per centre
- Capture total authorised computer terminal count
- Record backup power availability flag
- Record internet connectivity type and bandwidth category
- Capture accessibility and facility notes as free text
- Capture infrastructure remarks for administrative review
- Validate terminal count against per-session capacity when both configured
- Persist infrastructure profile linked to centre master

##### Inputs

- Centre record identifier
- Examination room count
- Computer terminal count
- Backup power flag
- Internet connectivity type
- Bandwidth category
- Accessibility notes
- Infrastructure remarks

##### Outputs

- Updated centre infrastructure profile
- Infrastructure validation warnings
- Audit record for infrastructure changes

##### Business rules

- Computer terminal count should not be less than per-session seat capacity when both are configured
- Infrastructure details are informational for administration and do not enforce runtime access
- All infrastructure fields may be updated independently of centre active status
- Empty infrastructure profile is allowed for newly created centres

##### Validations

- Reject negative room or terminal counts
- Reject non-integer room and terminal counts
- Warn when terminal count is less than configured per-session capacity
- Validate connectivity type against allowed enumeration

##### Calculations

- Compute advisory ratio of terminals to per-session capacity

##### Workflow

INFRASTRUCTURE_VIEWED → FIELDS_ENTERED → VALIDATED → SAVED

##### Security

- Examination Administrator role required
- Audit log for infrastructure profile changes

##### Dependencies

- F03-002 Add Authorised Examination Centre Profile
- F03-005 Centre Approved Capacity Configuration

##### Assumptions

- Connectivity and bandwidth categories are configurable enumerations
- Infrastructure data supports admin review not runtime enforcement

##### Risks

- Stale infrastructure data if centres upgrade hardware without admin update

##### Non-functional requirements

- Infrastructure tab loads independently of restriction configuration tabs

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre infrastructure details tab with room and terminal count fields | Medium | 16 |
| UI | Centre backup power and internet connectivity selection controls | Easy | 14 |
| UI | Centre accessibility notes and infrastructure remarks text areas | Easy | 14 |
| UI | Terminal count versus session capacity advisory warning banner | Simple | 5 |
| UI | Centre infrastructure empty state for unconfigured centres | Simple | 5 |
| API | Fetch centre infrastructure profile by centre identifier | Easy | 4 |
| API | Update centre infrastructure profile with numeric validation | Medium | 6 |
| Database | Centre infrastructure details entity linked to centre master | Medium | 0.3 |
| Database | Centre infrastructure change audit history | Easy | 0.25 |
| Testing | Infrastructure profile save happy path with all field types | Medium | 0.3 |
| Testing | Negative room count and invalid connectivity enum rejection | Easy | 0.25 |
| Testing | Terminal count below session capacity advisory trigger case | Easy | 0.25 |
| Documentation | Administrator runbook for centre infrastructure data capture | Easy | 0.25 |
| Documentation | Technical notes for infrastructure profile persistence model | Simple | 0.1 |

### F03-012 Approved Examination Session to Centre Mapping

77.95 hours · Go-live · 16 tasks

##### Description

Allows Examination Administrators to define which examination sessions each authorised centre is approved to host, fulfilling §17 map examination sessions to centres and §18.1 approved examination sessions requirement so scheduling only assigns sessions to approved centre pairings.

##### Business objective

Establish explicit approval matrix between centres and examination sessions preventing unapproved centre-session combinations during scheduling and allocation.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

- List approved examination sessions for a selected centre
- Search available examination sessions for approval mapping
- Add approved session mapping between centre and examination session
- Remove approved session mapping with confirmation
- Validate centre active status before new mapping
- Exclude already mapped sessions from add picker
- Expose approved session list to scheduling module picklists
- Audit all mapping add and remove actions

##### Inputs

- Centre record identifier
- Examination session identifier
- Mapping effective date optional
- Remove mapping confirmation

##### Outputs

- Centre-session approval mapping list
- Updated mapping after add or remove
- Mapping change audit records

##### Business rules

- Only active centres may receive new session approvals
- A centre-session pair may be mapped only once
- Removed mappings do not delete historical scheduling records
- Approved sessions determine which sessions appear when scheduling at this centre
- Examination session master originates from Module 04 and Module 06

##### Validations

- Reject duplicate centre-session mapping
- Reject mapping to inactive centre
- Reject mapping when examination session not found or closed
- Require confirmation before removing mapping with future scheduled instances

##### Calculations

- Count approved sessions per centre for summary display

##### Workflow

MAPPING_LIST_VIEWED → SESSION_SELECTED → MAPPING_CREATED → MAPPING_LIST_UPDATED; MAPPING_REMOVED via ADMIN_CONFIRMED_REMOVE

##### Search requirements

- Search examination sessions by name and date for approval picker

##### Security

- Examination Administrator role required
- Audit log for mapping add and remove

##### Integrations

- Read examination session master from examination configuration module

##### Dependencies

- F03-001 Authorised Examination Centre Register and Search
- F04-004 Examination Master Configuration
- F06-001 Examination Schedule Creation and Maintenance

##### Assumptions

- Examination session records exist before centre approval mapping
- Mapping is many-to-many between centres and session templates

##### Risks

- Removing approval for sessions with existing schedules may cause scheduling inconsistencies

##### Non-functional requirements

- Session picker search returns results within admin UI latency

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre approved examination session mapping list grid | Medium | 16 |
| UI | Add approved session lookup dialog with session search | Medium | 16 |
| UI | Remove approved session mapping confirmation dialog | Simple | 5 |
| UI | Approved session mapping empty state when no sessions mapped | Simple | 5 |
| UI | Future scheduled instance warning on session mapping removal | Easy | 14 |
| API | List approved examination sessions for a centre | Easy | 4 |
| API | Search available examination sessions for centre approval picker | Medium | 6 |
| API | Create centre to examination session approval mapping | Medium | 6 |
| API | Remove centre to examination session approval mapping | Easy | 4 |
| Database | Centre session approval mapping entity with unique centre-session constraint | Medium | 0.3 |
| Database | Centre session mapping change audit history | Easy | 0.25 |
| Testing | Add and remove session mapping happy-path flows | Medium | 0.3 |
| Testing | Duplicate mapping and inactive centre mapping rejection | Medium | 0.3 |
| Testing | Remove mapping with future schedule advisory display case | Easy | 0.25 |
| Documentation | Administrator runbook for centre session approval mapping | Easy | 0.25 |
| Documentation | Technical notes for approved session picklist integration with scheduling | Medium | 0.3 |

### F03-013 Centre Invigilator and Administrator User Binding

85.2 hours · Go-live · 18 tasks

##### Description

Allows Examination Administrators to bind centre invigilator and centre administrator users to a specific authorised examination centre fulfilling §17 configure centre-specific users and §18.1 centre administrator or invigilator user assignment, integrating with the shared user register without duplicating user lifecycle management.

##### Business objective

Ensure each authorised centre has designated invigilator and administrator users who receive centre-scoped access for centre operations while user account creation remains in User and Role Management.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

- List centre-bound invigilator and administrator users for a centre
- Search existing centre invigilator role users for binding picker
- Bind user to centre with Invigilator or Centre Administrator role type
- Unbind user from centre with confirmation
- Prevent duplicate binding of same user to same centre
- Validate bound user account is active in user register
- Expose binding data to centre-scoped access enforcement in Module 01 and Module 08
- Audit bind and unbind actions

##### Inputs

- Centre record identifier
- User account identifier
- Binding role type Invigilator or Centre Administrator
- Unbind confirmation

##### Outputs

- Centre-user binding list
- New or removed binding records
- Binding change audit entries

##### Business rules

- User account must exist in centre invigilator user register before binding
- A user may be bound to multiple centres if policy allows
- Same user cannot have duplicate binding role at same centre
- At least one invigilator binding is recommended before centre activation for operations
- Unbinding does not delete user account in Module 01

##### Validations

- Reject binding inactive or locked user accounts
- Reject duplicate centre-user-role binding
- Reject binding users without centre invigilator role assignment
- Warn on unbind when user has scheduled centre-day duties

##### Calculations

- Count bound invigilators and administrators per centre

##### Workflow

BINDING_LIST_VIEWED → USER_SELECTED → BINDING_CREATED → BINDING_LIST_UPDATED; BINDING_REMOVED via ADMIN_CONFIRMED_UNBIND

##### Search requirements

- Search users by name, employee ID, and mobile for binding picker

##### Security

- Examination Administrator role required
- Binding changes audited
- Bound users receive centre-scoped permissions via Module 01 access model

##### Integrations

- Read centre invigilator user register from User and Role Management module

##### Dependencies

- F01-003 Centre Invigilator Role and Centre-Scoped Access Model
- F01-007 Centre Invigilator User Register Centre Binding and Lifecycle
- F03-002 Add Authorised Examination Centre Profile

##### Assumptions

- User creation and password lifecycle remain in Module 01
- Binding role types are Invigilator and Centre Administrator only

##### Risks

- Unbinding sole invigilator before examination day may block centre operations

##### Non-functional requirements

- User picker search responsive for large user registers

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre bound user list grid with role type and status columns | Medium | 16 |
| UI | Bind centre user lookup dialog with user search | Medium | 16 |
| UI | Centre user binding role type selector for invigilator or administrator | Simple | 5 |
| UI | Unbind centre user confirmation dialog | Simple | 5 |
| UI | Centre user binding empty state when no users bound | Simple | 5 |
| UI | Scheduled centre-day duty warning on user unbind attempt | Easy | 14 |
| API | List centre-bound invigilator and administrator users | Easy | 4 |
| API | Search eligible centre invigilator role users for binding picker | Medium | 6 |
| API | Create centre to user binding with role type validation | Medium | 6 |
| API | Remove centre to user binding with dependency check | Medium | 6 |
| Database | Centre user binding entity with centre, user, and role type | Medium | 0.3 |
| Database | Unique constraint preventing duplicate centre-user-role binding | Easy | 0.25 |
| Database | Centre user binding change audit history | Easy | 0.25 |
| Testing | Bind and unbind centre user happy-path flows | Medium | 0.3 |
| Testing | Duplicate binding and inactive user binding rejection | Medium | 0.3 |
| Testing | Unbind user without centre invigilator role rejection case | Easy | 0.25 |
| Documentation | Administrator runbook for centre invigilator binding procedures | Easy | 0.25 |
| Documentation | Technical notes for centre-scoped access binding handoff to Module 01 | Medium | 0.3 |

### F03-014 Authorised Centre Network Restriction Configuration

82 hours · Go-live · 16 tasks

##### Description

Allows Examination Administrators to configure authorised network identifiers such as IP ranges or network tags for each examination centre as part of §18.1 authorised systems, devices, and network configuration, storing restriction data consumed at runtime by Secure Examination Conduct without implementing enforcement in this module.

##### Business objective

Capture centre-specific authorised network parameters so examination access can be restricted to approved centre networks during secure examination conduct.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

- List authorised network restriction entries per centre
- Add single IP, IP range, or CIDR network restriction entry
- Edit network entry label and value
- Deactivate network entry without deleting audit history
- Validate IP address and CIDR format on entry
- Prevent overlapping duplicate network entries for same centre
- Expose active network restriction set to Secure Examination Conduct module
- Audit network configuration changes

##### Inputs

- Centre record identifier
- Restriction type
- IP address or range or CIDR value
- Descriptive label
- Active flag

##### Outputs

- Centre network restriction entry list
- Validated network configuration records
- Network configuration audit entries

##### Business rules

- Network restriction configuration is stored here and enforced at runtime in Module 09
- At least one active network entry is recommended before centre examination conduct
- Inactive network entries are retained for audit but excluded from enforcement handoff
- Network configuration is centre-specific and not shared across centres
- Final technical mechanism may combine network with device restrictions per client infrastructure

##### Validations

- Validate IPv4 address format for single IP entries
- Validate CIDR notation format and prefix length bounds
- Validate IP range start is less than or equal to range end
- Reject duplicate identical network entry for same centre
- Reject blank network value

##### Workflow

NETWORK_LIST_VIEWED → ENTRY_ADDED → VALIDATED → SAVED → ACTIVE_FOR_ENFORCEMENT_HANDOFF; ENTRY_DEACTIVATED via ADMIN_ACTION

##### Security

- Examination Administrator role required
- Network configuration changes fully audited
- Restriction values visible only to authorised administrators

##### Integrations

- Publish active network restriction set for Module 09 runtime validation handoff

##### Dependencies

- F03-002 Add Authorised Examination Centre Profile
- F09-002 Authorised Centre Device and Network Enforcement

##### Assumptions

- IPv4 is primary; IPv6 support depends on client infrastructure decision
- Enforcement logic resides entirely in Module 09

##### Risks

- Incorrect IP or CIDR entry may block all centre candidates at examination time

##### Non-functional requirements

- Network entry validation provides immediate inline feedback

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre authorised network restriction entry list grid | Medium | 16 |
| UI | Add network restriction entry form with type selector | Medium | 16 |
| UI | Edit network restriction entry form | Medium | 16 |
| UI | Deactivate network restriction entry confirmation dialog | Simple | 5 |
| UI | Invalid IP or CIDR format inline validation display | Simple | 5 |
| API | List centre network restriction entries with active flag | Easy | 4 |
| API | Create centre network restriction entry with format validation | Complex | 8 |
| API | Update centre network restriction entry label and value | Medium | 6 |
| API | Deactivate centre network restriction entry | Easy | 4 |
| Database | Centre network restriction entry entity with type and value columns | Medium | 0.3 |
| Database | Centre network restriction change audit history | Easy | 0.25 |
| Testing | Add single IP and CIDR network entry happy-path cases | Medium | 0.3 |
| Testing | Invalid IP format and duplicate network entry rejection | Medium | 0.3 |
| Testing | Deactivate network entry exclusion from enforcement handoff case | Easy | 0.25 |
| Documentation | Administrator runbook for centre network restriction setup | Medium | 0.3 |
| Documentation | Technical notes for network restriction handoff to secure conduct module | Medium | 0.3 |

### F03-015 Authorised Centre Device and System Restriction Configuration

117.55 hours · Go-live · 19 tasks

##### Description

Allows Examination Administrators to register authorised examination devices or system identifiers such as hostname, MAC address, or asset tag for each centre per §18.1 authorised systems and devices configuration, providing whitelist data for runtime device enforcement elsewhere.

##### Business objective

Maintain a centre-specific authorised device inventory so candidates can attempt examinations only from approved centre computers.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

- List authorised device entries per centre with status
- Register single device with MAC, hostname, or asset tag identifier
- Edit device label and seat or room assignment
- Deactivate device entry preserving audit history
- Bulk import device identifiers from approved file format
- Validate MAC address and hostname formats
- Prevent duplicate device identifier within same centre
- Expose active device whitelist to Secure Examination Conduct module

##### Inputs

- Centre record identifier
- Device identifier type
- Identifier value
- Seat or room label
- Bulk import file
- Active flag

##### Outputs

- Centre device register list
- Imported device registration results summary
- Device configuration audit records

##### Business rules

- Device restriction configuration is stored here and enforced at runtime in Module 09
- Device identifier must be unique within a centre
- Deactivated devices are excluded from enforcement whitelist
- Bulk import validates each row and reports failures without partial silent skip
- Device count should align with infrastructure terminal count for operational readiness

##### Validations

- Validate MAC address format XX:XX:XX:XX:XX:XX or equivalent
- Validate hostname length and allowed character set
- Reject duplicate device identifier at same centre
- Validate bulk import file format and row-level identifier formats
- Reject blank identifier value

##### Calculations

- Count active authorised devices versus infrastructure terminal count for advisory

##### Workflow

DEVICE_LIST_VIEWED → DEVICE_REGISTERED → VALIDATED → SAVED; BULK_IMPORT_SUBMITTED → ROWS_VALIDATED → IMPORT_COMPLETED; DEVICE_DEACTIVATED

##### Search requirements

- Search devices by identifier, label, or seat within centre device list

##### Documents

- Bulk device import template file for administrator download

##### Security

- Examination Administrator role required
- Device whitelist changes audited
- Bulk import file scanned for size and type limits

##### Integrations

- Publish active device whitelist for Module 09 runtime validation handoff

##### Dependencies

- F03-002 Add Authorised Examination Centre Profile
- F03-006 Centre Infrastructure Details Configuration
- F09-002 Authorised Centre Device and Network Enforcement

##### Assumptions

- Device fingerprint mechanism at runtime is defined in Module 09
- Bulk import template format is CSV with defined columns

##### Risks

- Incorrect MAC or hostname entries may deny legitimate centre devices at examination time

##### Non-functional requirements

- Bulk import processes moderate device lists within acceptable admin wait time

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre authorised device register list with search and status filter | Medium | 16 |
| UI | Register single authorised device form with identifier type selector | Medium | 16 |
| UI | Edit authorised device label and seat assignment form | Easy | 14 |
| UI | Deactivate authorised device confirmation dialog | Simple | 5 |
| UI | Bulk device import upload dialog with template download link | Medium | 16 |
| UI | Bulk device import result summary with row error listing | Medium | 16 |
| API | List centre authorised devices with search and status filter | Medium | 6 |
| API | Create single centre authorised device with format validation | Medium | 6 |
| API | Update centre authorised device label and seat assignment | Easy | 4 |
| API | Deactivate centre authorised device entry | Easy | 4 |
| API | Bulk import centre authorised devices with row-level validation | Very high | 12 |
| Database | Centre authorised device entity with identifier type and value | Medium | 0.3 |
| Database | Unique constraint on centre plus device identifier value | Easy | 0.25 |
| Database | Centre device configuration and bulk import audit history | Medium | 0.3 |
| Testing | Single device register and deactivate happy-path flows | Medium | 0.3 |
| Testing | Invalid MAC format and duplicate device identifier rejection | Medium | 0.3 |
| Testing | Bulk import partial failure row error reporting cases | Complex | 0.5 |
| Documentation | Administrator runbook for centre device whitelist management | Medium | 0.3 |
| Documentation | Technical notes for device whitelist handoff and bulk import format | Medium | 0.3 |

### F03-016 Centre Candidate Allocation Summary View

121.65 hours · Go-live · 18 tasks

##### Description

Provides Examination Administrators with read-only visibility of candidate allocation summaries per authorised examination centre including allocated candidate counts by examination and session as required by §17 view candidate allocation for each centre, sourcing allocation data from scheduling without executing allocation in this module.

##### Business objective

Enable administrators to monitor how candidates are distributed across centres for operational planning without performing allocation actions in the centre management module.

##### Actors

- Examination Administrator

##### User journey

1. Administrator opens centre detail Allocation Summary tab or selects View Allocations from register.
2. System displays summary cards with total allocated candidates, upcoming session count, and capacity utilisation.
3. Administrator selects examination filter to narrow summary.
4. System refreshes allocation grid showing examination name, session date, allocated count, and remaining seats.
5. Administrator clicks a session row to expand candidate count breakdown by category if available.
6. Administrator exports allocation summary to spreadsheet when required.
7. Administrator navigates to scheduling module via link for allocation changes.
8. Summary reflects latest allocation state from scheduling module data.

##### Functional capabilities

- Display total allocated candidate count per centre
- Display allocation breakdown by examination and session
- Show remaining seat capacity per session against centre capacity configuration
- Filter allocation summary by examination and date range
- Expand session row for category-wise allocated count when data available
- Export allocation summary to approved spreadsheet format
- Provide deep link to scheduling module for allocation management
- Refresh summary from current scheduling allocation records

##### Inputs

- Centre record identifier
- Examination filter
- Date range filter
- Export format selection

##### Outputs

- Centre allocation summary cards
- Session-wise allocation grid
- Category breakdown when available
- Exported allocation summary file

##### Business rules

- Allocation summary is read-only in this module
- Allocation execution and changes occur in Module 06
- Utilisation compares allocated count to centre capacity from Module 03 configuration
- Only allocated candidates for active and scheduled sessions appear
- Summary excludes candidates with only preferences not yet allocated

##### Validations

- Reject access by non-administrator roles
- Validate date range filter start precedes end
- Return empty grid without error when no allocations exist for centre

##### Calculations

- Compute remaining seats as session capacity minus allocated count
- Compute centre utilisation percentage across upcoming sessions

##### Workflow

SUMMARY_LOADED → FILTER_APPLIED → GRID_DISPLAYED → ROW_EXPANDED → EXPORT_GENERATED

##### Search requirements

- Filter allocations by examination name
- Filter allocations by session date range

##### Reports

- Centre-wise candidate allocation summary export

##### Security

- Examination Administrator role required
- Read-only access; no allocation mutation in this feature

##### Integrations

- Read candidate allocation records from Examination Scheduling and Allocation module

##### Dependencies

- F03-005 Centre Approved Capacity Configuration
- F06-002 Candidate Centre and Session Allocation

##### Assumptions

- Allocation records include examination, session, and candidate category fields
- Export format is Excel or CSV per department standard

##### Risks

- Summary staleness if allocation changes occur during viewing; refresh on tab focus mitigates

##### Non-functional requirements

- Summary grid loads within acceptable time for centres with high candidate volume

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre allocation summary dashboard cards for total allocated and utilisation | Medium | 16 |
| UI | Centre session-wise allocation grid with examination and date columns | Medium | 16 |
| UI | Allocation summary examination and date range filter controls | Easy | 14 |
| UI | Session row expandable category allocation breakdown panel | Medium | 16 |
| UI | Allocation summary empty state when no candidates allocated | Simple | 5 |
| UI | Deep link button to scheduling module allocation management | Simple | 5 |
| UI | Allocation summary export action with format selection | Easy | 14 |
| API | Fetch centre allocation summary totals and utilisation metrics | Medium | 6 |
| API | List centre session-wise allocation rows with filters | Medium | 6 |
| API | Fetch session category-wise allocated count breakdown | Medium | 6 |
| API | Export centre allocation summary to spreadsheet format | Complex | 8 |
| Database | Read-only query access to allocation summary aggregate views | Medium | 0.3 |
| Integration | Read candidate allocation records from scheduling module data store | Easy | 8 |
| Testing | Allocation summary display and filter happy-path scenarios | Medium | 0.3 |
| Testing | Empty allocation and invalid date range filter handling | Easy | 0.25 |
| Testing | Unauthorized access rejection for allocation summary view | Easy | 0.25 |
| Documentation | Administrator runbook for interpreting centre allocation summary | Easy | 0.25 |
| Documentation | Technical notes for read-only allocation data integration | Medium | 0.3 |
