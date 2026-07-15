# F01-009 — Login History & User Activity Logs

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-009 |
| **Feature Name** | Login History & User Activity Logs |
| **Module** | 01 — User & Role Management |

### Description
Capture and provide searchable login history and access-related user activity logs for security monitoring and audit, as required by SOW audit & compliance expectations.

### Business Objective
Provide accountability for who accessed CPMS, when, and what privileged access-admin actions were performed.

### Actors
- Super Administrator
- Auditor
- Security-responsible officers (read permission)

### User Journey
1. Auditor opens Access Logs.
2. Filters by user, date range, event type, IP/browser (if captured), success/failure.
3. Drills into login events or admin activity events.
4. Exports results for audit evidence.

### Functional Capabilities
- Login success/failure history
- Logout and session timeout events
- User admin activity events (create/update user, role/matrix change, scope change, SoD override, credential issue/revoke)
- Search, filter, pagination
- Excel export
- Read-only retention per policy

### Inputs
- Filter criteria (user, dates, event type, status)

### Outputs
- Log list
- Export file
- Event detail view

### Business Rules
- Logs are append-only from application perspective (no edit/delete in UI).
- Retention period configurable; archival beyond retention is operational.
- Auditors have read-only access; cannot mute logging.

### Validations
- Date range required limits (e.g., max 90 days per query) to protect performance

### Calculations
None.

### Workflow
N/A.

### Search Requirements
- By user, login ID, event type, result, date/time, IP address
- Sort by time descending

### Documents
Exported audit extracts.

### Reports
Login Failure Report; Privileged Access Change Report.

### Notifications
Optional alert on repeated failures / privileged matrix changes (ties to F01-003/F01-005).

### Security
- Access to logs restricted
- Logs themselves must not store plaintext passwords or OTP codes
- PII minimized in log payloads

### Integrations
None (application-level logs only; not full SIEM).

### Dependencies
- F01-001 through F01-008 event producers
- Module 01 permissions for log viewers

### Assumptions
- Business transaction audit trails inside finance modules remain those modules’ responsibility; this feature focuses on identity/access administration and login events.
- SIEM shipping out of scope.
- Medium complexity list UIs with export.

### Risks
- High-volume logs without range limits may degrade performance.
- Incomplete event instrumentation leaves audit gaps — checklist required in testing.

### Non Functional Requirements
- Query performance acceptable within configured date windows
- Export to Excel
- High integrity / append-only behaviour

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: dual viewers (login + activity), filters/export, append-only retention behaviour, instrumentation across Module 01 events.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Login history list | UI | Medium | 6 |
| User activity log viewer | UI | Medium | 6 |
| Export confirmation / download | UI | Simple | 2 |
| Log query & export operations | API | Medium | 6 |
| Login & activity log storage | Database | Medium | 4 |
| Access log tests | Testing | Medium | 6 |
| Audit log viewing guide | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- Does not include centralized SIEM or infrastructure log pipelines.
