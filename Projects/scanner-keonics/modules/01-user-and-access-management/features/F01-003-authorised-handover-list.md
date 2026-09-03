# F01-003 — Authorised Handover List

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | Authorised Handover List |
| **Module** | 01 — User and Access Management |

### Description
Maintain the IFQ list of Service Provider staff authorised to receive files and Department staff authorised to hand over and take back files, so inward/outward logs only accept those names.

### Business Objective
Custody signatures match people the Department actually authorised.

### Actors
Maker: Supervisor (SP names); Department Officer (Department names). Approver: none.

### User Journey
1. Who creates: Supervisor / Department Officer.
2. How they create: Handover list → add person from staff accounts or capture name, designation, ID → mark Receive and/or Return.
3. How they edit: Remove or change authorisation flags. History on the list.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox.
6. How the approver decides: No decision.
7. How the maker sees history: List shows current authorised people.
8. How the auditor sees history: Same list plus change trail.

### Functional Capabilities
- Authorise SP receivers
- Authorise Department handover/return officers
- Prevent unlisted names on logs (enforced with Module 02/04)

### UI Screens
| Screen | Complexity |
|---|---|
| Authorised handover list | Easy |
| Handover authorisation form | Easy |

### Logical API operations
| Operation | Complexity |
|---|---|
| Create handover authorisation | Easy |
| Update handover authorisation | Easy |
| List authorised staff | Simple |
| Search authorised staff | Easy |

### Inputs
Staff, receive/return flags.

### Outputs
Authorised set used by inward/outward logs.

### Business Rules
- Inward “collected from / collected by” must be authorised.
- Outward “returned to / returned by” must be authorised.

### Validations
- Person must exist as a project staff account.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
By name and organisation (SP vs Department).

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
Supervisor cannot add fake Department officers without a Department account.

### Integrations
None.

### Dependencies
F01-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.

### Risks
Paper log signed by someone not on this list — process must match the tool.

### Non Functional Requirements
List small (site team); simple to keep current.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Authorised handover list | UI | Easy | 4 |
| Handover authorisation form | UI | Easy | 4 |
| Create handover authorisation | API | Easy | 4 |
| Update handover authorisation | API | Easy | 4 |
| List authorised staff | API | Simple | 2 |
| Search authorised staff | API | Easy | 4 |
| Handover authorisation records | DB | Easy | 2 |
| Authorised handover list tests | Testing | Easy | 4 |
| Authorised handover list implementation documentation | Documentation | Easy | 2 |

**Feature total: 30 hours**
