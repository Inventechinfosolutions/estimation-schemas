# F05-002 — Stores Issue and Fitment Recording

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Stores Issue and Fitment Recording |
| **Module** | 05 — Digital Job Card and Fitment |

### Description
Store Clerk records issue to mechanic (Item ID, vehicle, qty, mechanic); stock reduces. Mechanical Clerk records fitment (bus, schedule, mechanic, item, KM, date/time), including workshop body/FC work.

### Business Objective
FR-M-01 to 04 and FR-X-02 real-time stock reduction on issue against job card.

### Actors
User: Store Clerk issues. Mechanical Clerk records fitment against the job card. Auditor: read-only history.

### User Journey
1. Who creates: Store Clerk issues. Mechanical Clerk records fitment against the job card.
2. How they create: From job card → Issue: Store Clerk selects item, qty, mechanic, Save. Fitment: Mechanical Clerk enters position, KM, date/time, Save.
3. How they edit: Draft issue/fitment editable until job card completed.
4. How they send for approval: Issue confirmation reduces depot store stock immediately. Fitment is saved to the job card; no separate CA approval.
5. How the approver sees pending items: No approver inbox. Supervisor sees issues on the job card.
6. How the approver decides: Not a separate approval. Invalid issue is reversed with reason (stock restore).
7. How the user sees history: Issue and fitment lines on the job card and item lifecycle.
8. How the supervisor / auditor sees history: Supervisor/auditor see the same lines.

### Functional Capabilities
- Authorised user creates, edits and searches fitment entry records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Fitment entry register | Medium |
| Fitment entry form (create and edit) | Complex |
| Fitment entry history | Medium |
| Issue against job card | Complex |
| Fitment line entry | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create fitment entry | Medium |
| Update fitment entry | Medium |
| Search fitment entry | Medium |
| Read fitment entry history | Easy |
| Issue item and reduce stock | Complex |
| Record fitment | Medium |

### Inputs
Item ID, qty, mechanic, vehicle, KM, position, date/time.

### Outputs
Persisted fitment entry; searchable register; history.

### Business Rules
- Paper job cards are not accepted as the system of record.

### Validations
- Item must exist.
- Qty ≤ available depot stock.
- Job card must be Open/In Progress/Pending Spares.

### Calculations
Stock on hand decreases by issued qty.

### Workflow
Issue confirmation reduces depot store stock immediately. Fitment is saved to the job card; no separate CA approval.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Items issued by vehicle.

### Notifications
On-screen confirmation. Optional notice to the user on save failure.

### Security
Need-to-know by Post. Actions attributed to Person acting in a Post.

### Integrations
Module 01 identity. Document store if attachments are used.

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

### Assumptions
- Hours use Estimation Master values only, at capability grain (not one billed row per screen).

### Risks
Unscoped access would expose records outside the user's office.

### Non Functional Requirements
Register and history remain searchable during office hours.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Fitment entry register | UI | Medium | 6 |
| Fitment entry form (create and edit) | UI | Complex | 12 |
| Fitment entry history | UI | Medium | 6 |
| Issue against job card | UI | Complex | 12 |
| Fitment line entry | UI | Medium | 6 |
| Create fitment entry | API | Medium | 6 |
| Update fitment entry | API | Medium | 6 |
| Search fitment entry | API | Medium | 6 |
| Read fitment entry history | API | Easy | 4 |
| Issue item and reduce stock | API | Complex | 8 |
| Record fitment | API | Medium | 6 |
| Fitment entry record and history | DB | Medium | 4 |
| Internal identity/document hooks for fitment entry | Integration | Simple | 4 |
| Stores Issue and Fitment Recording feature tests | Testing | Complex | 8 |
| Stores Issue and Fitment Recording implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **97** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
