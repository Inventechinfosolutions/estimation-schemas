# F06-005 — Citizen Downloads & Status Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-005 |
| **Feature Name** | Citizen Downloads & Status Tracking |
| **Module** | 06 — Citizen Registration Portal |

### Description
Present a citizen’s own application, booking, payment, allotment, deed, registration, possession, cancellation, and refund status with links to released documents.

### Business Objective
Reduce citizen follow-up while providing a single transparent view of the housing journey.

### Actors
Citizen; Housing Officer; Accounts Officer; Auditor.

### User Journey
A logged-in citizen opens My Housing, selects a personal application or booking, views its current milestone and history, downloads released artefacts, and follows available next actions such as payment or clarification response.

### Functional Capabilities
- Personal case list, milestone timeline, status detail, and action prompts.
- Controlled download list for receipts, allotment letters, deed drafts/registered deed, possession letters, and cancellation/refund artefacts when released.
- Download history and unavailable-document explanation.

### Inputs
Citizen-owned transaction references, process histories, released document metadata, and current status.

### Outputs
Status timeline, downloadable artefacts, citizen action link, and download audit entry.

### Business Rules
Only documents formally released by their owning process are visible; citizen sees only own cases; status wording reflects the latest completed process event and does not expose internal approver remarks.

### Validations
Record ownership, document release status, valid document version, and permitted current action.

### Calculations
Milestone completion indicator and due-date countdown for actionable payment/clarification items.

### Workflow
My Housing → select own record → review timeline → download released document or follow next action.

### Search Requirements
Own application number, booking number, project, unit, status, and date range.

### Documents
Application acknowledgement, booking confirmation, receipts, allotment letter, approved deed draft, registered deed, possession letter, cancellation/refund communications.

### Reports
Citizen download history and status-access audit register.

### Notifications
Status-change notices originate from Module 12; this feature displays their related records.

### Security
Strict ownership filtering, released-version-only downloads, watermark/access policy where configured, and download audit.

### Integrations
Status and document-metadata consumption from Modules 07–10 and Module 12 (Medium).

### Dependencies
F06-004; Modules 07–10; Module 12.

### Assumptions
Document generation/versioning is embedded in the owning business process; no separate document repository interface is included.

### Risks
Premature release of an artefact could expose an unapproved document.

### Non Functional Requirements
Timely timeline refresh, downloadable files on mobile, and secure retrieval of sensitive documents.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| My Housing list, timeline, and downloads UI | UI | Very High | 16 |
| Owned status and release access processing | API | Complex | 8 |
| Download access audit persistence | Database | Medium | 4 |
| Process status and document handoffs | Integration | Medium | 16 |
| Tracking and download isolation tests | Testing | Complex | 8 |
| Citizen tracking guide | Documentation | Medium | 3 |
| **Total** | | | **55** |

### Estimation Assumptions
This feature consumes process statuses and released document metadata; generation of the artefacts is estimated in Modules 07–10.
