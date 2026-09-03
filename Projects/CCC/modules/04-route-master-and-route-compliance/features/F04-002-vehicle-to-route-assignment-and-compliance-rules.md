# F04-002 — Vehicle-to-Route Assignment and Compliance Rules

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Vehicle-to-Route Assignment and Compliance Rules |
| **Module** | 04 — Route Master and Route Compliance |

### Description
Administrator assigns vehicles to authorized routes and activates compliance monitoring rules used by live GPS and alerts.

### Business Objective
Vehicle–route mapping for compliance monitoring.

### Actors
Applicant: Route/Operations Officer. Approver: District/State Checker as configured.

### User Journey
1. Who creates: Operations Officer.
2. How they create: Assignment → New: vehicle, route, validity period, Save draft.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit to checker if configured; else activate on save per Department rule.
5. How the approver sees pending items: Checker assignment inbox (if used).
6. How the approver decides: Approve or reject assignment.
7. How the applicant sees history: Assignment history for vehicle/route.
8. How the approver sees history: Same for checker/auditor.

### Functional Capabilities
- Vehicle–route assignment
- Validity period
- Compliance rule flags

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Assignment register | Medium |
| Assignment form | Complex |
| Submit confirmation | Simple |
| Assignment inbox | Medium |
| Assignment decision | Easy |
| Assignment history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save assignment draft | Medium |
| Submit assignment | Complex |
| Approve assignment | Complex |
| Query assignments | Medium |
| End assignment | Easy |

### Inputs
Vehicle, route, from/to dates.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Vehicle and route must be approved.

### Validations
- Validity dates coherent.

### Calculations
None.

### Workflow
Draft → Approved (or direct activate if no checker).

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Active assignments.

### Notifications
On approve.

### Security
Operations Posts.

### Integrations
Consumed by Module 05/09.

### Dependencies
F03-001, F04-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- GPS/CCTV/RFID/ANPR field hardware supply and install are out of application-software hours unless stated otherwise.
- Hosting is on KSDC; KSDC consumption INR and AMC/O&M person-months are out of this estimate per confirmed scope.

### Risks
Incomplete vendor API documentation for VLTS, CCTV, SMART-PDS, Vahan or Sarathi would delay integration features.

### Non Functional Requirements
Screens remain usable under concurrent State CCC load; privileged actions are attributable to Person + Post.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Assignment register | UI | Medium | 6 |
| Assignment form | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Assignment inbox | UI | Medium | 6 |
| Assignment decision | UI | Easy | 4 |
| Assignment history | UI | Medium | 6 |
| Save assignment draft | API | Medium | 6 |
| Submit assignment | API | Complex | 8 |
| Approve assignment | API | Complex | 8 |
| Query assignments | API | Medium | 6 |
| End assignment | API | Easy | 4 |
| Assignment and history | DB | Medium | 4 |
| Vehicle-to-Route Assignment and Compliance Rules feature tests | Testing | Complex | 8 |
| Vehicle-to-Route Assignment and Compliance Rules implementation documentation | Documentation | Medium | 3 |

**Feature total: 83 hours**
