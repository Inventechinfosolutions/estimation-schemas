# F11-002 — Real-Time Stock Visibility

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-002 |
| **Feature Name** | Real-Time Stock Visibility |
| **Module** | 11 — Distribution, Stock Visibility and Replenishment |

### Description
Depots, Workshops, Central Stores and Central Office see stock by login scope; Central Stores can see all depot and CWS stock.

### Business Objective
FR-S-14, FR-S-15.

### Actors
User: Any Post with Stock view Role. Scope = own unit unless Central Stores/CO Role. Auditor: read-only history.

### User Journey
1. Who creates: Any Post with Stock view Role. Scope = own unit unless Central Stores/CO Role.
2. How they create: Opens Stock position, filters item/location, views on-hand, in-transit, min/reorder.
3. How they edit: Not a create feature. Saved filters optional.
4. How they send for approval: Not approval.
5. How the approver sees pending items: None.
6. How the approver decides: Not applicable.
7. How the user sees history: Optional last filters.
8. How the supervisor / auditor sees history: Auditor sees same scoped data.

### Functional Capabilities
- Authorised user creates, edits and searches stock position records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Stock position register | Medium |
| Stock position form (create and edit) | Complex |
| Stock position history | Medium |
| Stock position (all locations for Central Stores) | Very High |
| My store stock | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create stock position | Medium |
| Update stock position | Medium |
| Search stock position | Medium |
| Read stock position history | Easy |
| Query stock by location | Complex |

### Inputs
Item, location, on-hand.

### Outputs
Persisted stock position; searchable register; history.

### Business Rules
- Pre-bid: real-time means all locations update system-wide with no latency.

### Validations
- Scope enforced.

### Calculations
On-hand from receipts − issues − unacked dispatches as designed.

### Workflow
Not approval.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Stock snapshot export. Pre-bid: system-wide sync with no latency.

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
| Stock position register | UI | Medium | 6 |
| Stock position form (create and edit) | UI | Complex | 12 |
| Stock position history | UI | Medium | 6 |
| Stock position (all locations for Central Stores) | UI | Very High | 16 |
| My store stock | UI | Medium | 6 |
| Create stock position | API | Medium | 6 |
| Update stock position | API | Medium | 6 |
| Search stock position | API | Medium | 6 |
| Read stock position history | API | Easy | 4 |
| Query stock by location | API | Complex | 8 |
| Stock position record and history | DB | Medium | 4 |
| Internal identity/document hooks for stock position | Integration | Simple | 4 |
| Real-Time Stock Visibility feature tests | Testing | Complex | 8 |
| Real-Time Stock Visibility implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **95** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
