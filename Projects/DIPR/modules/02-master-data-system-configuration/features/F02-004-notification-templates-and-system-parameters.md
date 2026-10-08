# F02-004 — Notification templates & system parameters

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-004 |
| Feature Name | Notification templates & system parameters |
| Module | 02 — Master Data & System Configuration |
| Description | Configure email/SMS/in-app templates and operational parameters such as retention, sync windows, and GPS accuracy thresholds once finalized. |
| Business Objective | Let DIPR tune alerts and platform behaviour without code releases for common operational changes. |
| Actors | DIPR Administrator |

### User Journey

- Administrator opens Templates register → edits approval/PoD/assignment templates with placeholders → opens System Parameters panel → updates GPS threshold, PoD retention, sync interval → saves → downstream modules read refreshed configuration.

### Functional Capabilities

- Template CRUD for email, SMS, and in-app bodies with subject/title and placeholders
- Template preview with sample campaign/PoD context
- System parameter key-value editor grouped by domain (PoD, sync, retention, MFA/SMS)
- Change log entry for parameter edits (ties to F02-005)

### Inputs

- Template content, channel, event key, active flag; parameter keys and typed values

### Outputs

- Templates for Module 08; parameters consumed by PoD validation, mobile sync, audit retention

### Business Rules

- Critical parameters (GPS accuracy) require confirmation dialog
- Templates must retain mandatory placeholders for compliance text where DIPR specifies

### Validations

- Valid placeholder syntax; numeric ranges for thresholds

### Calculations

- None

### Workflow

- Edit → Save → effective on next read/cache refresh

### Search Requirements

- Filter templates by channel and event type

### Documents

- None

### Reports

- None

### Notifications

- Templates are consumed by notification module; not sent from this screen directly

### Security

- Administrator-only write

### Integrations

- SMS gateway parameters stored here; dispatch in Module 08

### Dependencies

- F02-005 for change audit; F05-004 reads GPS parameters

### Assumptions

- DIPR supplies legal text for SMS/email footers

### Risks

- Aggressive retention reduction conflicts with audit export expectations

### Non Functional Requirements

- Parameter changes apply cluster-wide within defined refresh interval

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Notification template register by channel | Easy | 4 |
| UI | Email template editor with placeholder help | Medium | 6 |
| UI | SMS template editor with length counter | Easy | 4 |
| UI | In-app notification template editor | Easy | 4 |
| UI | System parameters form (PoD/sync/retention) | Medium | 6 |
| UI | Parameter change confirmation with impact summary | Simple | 2 |
| UI | Template preview render modal | Medium | 6 |
| API | List templates by event type | Easy | 4 |
| API | CRUD email notification template | Medium | 6 |
| API | CRUD SMS notification template | Easy | 4 |
| API | CRUD in-app notification template | Easy | 4 |
| API | CRUD system parameters with bounds validation | Medium | 6 |
| API | Preview template with sample campaign payload | Easy | 4 |
| Integration | SMTP test-send hook for template validation | Simple | 4 |
| Database | Template storage with event key | Medium | 4 |
| Database | System parameter key-value store | Easy | 2 |
| Database | Parameter change audit linkage | Simple | 1 |
| Testing | PoD threshold parameter read by downstream rules | Medium | 6 |
| Testing | Placeholder substitution in preview | Easy | 4 |
| Testing | Invalid parameter bounds rejected | Medium | 6 |
| Documentation | System parameter dictionary for operators | Easy | 2 |
| Documentation | UAT template activation checklist | Easy | 2 |

**Feature Total: 91 hours**

### Estimation Assumptions

- WhatsApp templates excluded unless DIPR adds channel later.
