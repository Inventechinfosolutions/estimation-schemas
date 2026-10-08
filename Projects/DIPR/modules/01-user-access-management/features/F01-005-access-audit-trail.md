# F01-005 — Access audit trail

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-005 |
| Feature Name | Access audit trail |
| Module | 01 — User & Access Management |
| Description | Record authentication events and permission changes for compliance review and correlation with Module 07 audit exports. |
| Business Objective | Give DIPR auditors evidence of who accessed AMT, from where, and how privileges changed over time. |
| Actors | DIPR Administrator; Auditor (read-only) |

### User Journey

- Administrator or Auditor opens Access Audit register → filters by date, user, event type (login, logout, failed login, role change, MFA event) → opens event detail → exports filtered slice for review.

### Functional Capabilities

- Capture login success/failure, logout, session timeout, SSO events
- Capture role assignment and permission matrix changes with before/after snapshot
- Capture MFA enrollment and reset events
- Searchable register with date range and user filters
- Read-only detail view with IP/user agent/channel where available

### Inputs

- System-generated events from auth and admin actions

### Outputs

- Immutable audit event stream; filtered register views; export file

### Business Rules

- Audit records cannot be edited or deleted by operators
- Retention period driven by system parameter (F02-004)
- Auditors see access events but cannot change users

### Validations

- None on read path

### Calculations

- None

### Workflow

- Event emitted on action → stored → visible in register after indexing

### Search Requirements

- Filter by user, event type, date range, channel (web/mobile/API)

### Documents

- CSV export of filtered audit slice

### Reports

- Feeds Module 07 compliance exports (by reference)

### Notifications

- None

### Security

- Read access limited to Administrator and Auditor roles; tamper-evident storage approach per platform module 10

### Integrations

- None

### Dependencies

- F01-001–F01-004 as event sources

### Assumptions

- Clock synchronization via infrastructure NTP

### Risks

- High volume login events require pagination and archive strategy

### Non Functional Requirements

- Register queries remain responsive with indexed time-series; export capped to configured row limits

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Access audit register with actor/action filters | Medium | 6 |
| UI | Audit event detail drawer (before/after snapshot) | Easy | 4 |
| UI | Quick date-range presets (today/7d/30d) | Simple | 2 |
| UI | Export filtered audit slice to CSV dialog | Easy | 4 |
| UI | Login failure spike filter chip | Simple | 2 |
| API | Ingest authentication login/logout/failure events | Medium | 6 |
| API | Ingest privilege change events (users/roles) | Medium | 6 |
| API | Query audit register with filters and pagination | Medium | 6 |
| API | Export filtered audit register | Easy | 4 |
| Database | Append-only access audit event storage | Medium | 4 |
| Database | Time-series indexes on actor and timestamp | Easy | 2 |
| Testing | Events on login and permission matrix change | Medium | 6 |
| Testing | Filter combinations and export correctness | Easy | 4 |
| Testing | Append-only immutability enforcement | Easy | 4 |
| Documentation | Access audit register user guide | Easy | 2 |
| Documentation | UAT: trace administrator role change | Simple | 1 |

**Feature Total: 63 hours**

### Estimation Assumptions

- Operational business audit (campaign/PoD actions) is separate under respective modules and Module 07.
