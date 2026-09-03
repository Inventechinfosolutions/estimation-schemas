# F13-001 — Barcode and QR Generation and Scanning

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-001 |
| **Feature Name** | Barcode and QR Generation and Scanning |
| **Module** | 13 — Barcode, QR, Notifications and External Integrations |

### Description
Generate and scan QR/barcode for receipt, issue and stock verification at Central Stores and Depot Stores. RFP requires demonstration for materials at depot, workshop and central purchase. Hardware cost is not BMTC's (excluded from hours).

### Business Objective
FR-X-08 and QR technical requirements.

### Actors
User: Store Clerk scans. Administrator prints labels. Auditor: read-only history.

### User Journey
1. Who creates: Store Clerk scans. Administrator prints labels.
2. How they create: Print labels for items. Scan on receipt/issue/PV: camera, handheld or fixed scanner; validate and post the business event.
3. How they edit: Failed scans retried. Successful scan not silently deleted; reversal is a business reversal.
4. How they send for approval: Scan posts the linked receipt/issue/PV line. No separate checker for the scan itself.
5. How the approver sees pending items: None for scan. Failed scan list for the clerk.
6. How the approver decides: Not applicable.
7. How the user sees history: Scan log (generate/scan, time, Person, Post).
8. How the supervisor / auditor sees history: Auditor scan log.

### Functional Capabilities
- Authorised user creates, edits and searches scan event records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Scan event register | Medium |
| Scan event form (create and edit) | Complex |
| Scan event history | Medium |
| Label print | Medium |
| Scan capture | Complex |
| Scan log | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create scan event | Medium |
| Update scan event | Medium |
| Search scan event | Medium |
| Read scan event history | Easy |
| Generate QR/barcode | Complex |
| Validate scan | Complex |

### Inputs
Item, location, device type, timestamp.

### Outputs
Persisted scan event; searchable register; history.

### Business Rules
- Hardware and scanner purchase remain out of hours (RFP: hardware cost not paid by BMTC).

### Validations
- Prevent duplicate/unauthorised reuse where configured.
- Time-bound validity where applicable.

### Calculations
None beyond scan timestamp.

### Workflow
Scan posts the linked receipt/issue/PV line. No separate checker for the scan itself.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Scan volume.

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
| Scan event register | UI | Medium | 6 |
| Scan event form (create and edit) | UI | Complex | 12 |
| Scan event history | UI | Medium | 6 |
| Label print | UI | Medium | 6 |
| Scan capture | UI | Complex | 12 |
| Scan log | UI | Medium | 6 |
| Create scan event | API | Medium | 6 |
| Update scan event | API | Medium | 6 |
| Search scan event | API | Medium | 6 |
| Read scan event history | API | Easy | 4 |
| Generate QR/barcode | API | Complex | 8 |
| Validate scan | API | Complex | 8 |
| Scan event record and history | DB | Medium | 4 |
| Internal identity/document hooks for scan event | Integration | Simple | 4 |
| Barcode and QR Generation and Scanning feature tests | Testing | Very High | 12 |
| Barcode and QR Generation and Scanning implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **109** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
