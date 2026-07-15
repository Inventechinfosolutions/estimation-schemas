# F12-005 — Process Event Alert Orchestration

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F12-005 |
| **Feature Name** | Process Event Alert Orchestration |
| **Module** | 12 — Notification Service |

### Description
Route configured BHMS lifecycle alerts—registration, application, booking, payment, letters, cancellation, refund, auto-cancellation, and NOC—to the appropriate channels.
### Business Objective
Keep participants and approvers informed without blocking source-business workflows.
### Actors
- System; process owners; approvers; Citizen; BDA officers
### User Journey
1. An owning module publishes a process event. 2. The orchestration resolves template, recipients, and channels. 3. Dispatch is initiated and outcome correlated to the source event.
### Functional Capabilities
- Event-to-template mapping, recipient/role resolution, channel selection, source traceability, and retry initiation.
### Inputs
- Event type, source reference, workflow/action status, recipient context, and merge values.
### Outputs
- Channel-dispatch requests and correlated operational status.
### Business Rules
- The source module remains authoritative for business status; notification failure does not reverse a completed transaction.
### Validations
- Configured event mapping, valid source reference, recipient availability, and permitted channels.
### Calculations
- Event raised → mapped → queued for channels → outcome logged → retry where allowed.
### Workflow
- By event type, source record, recipient, channel, date, and result.
### Search Requirements
- Source-linked acknowledgement or action document where applicable.
### Documents
- Event-dispatch exception and volume view.
### Reports
- Coordinates F12-001 to F12-003; delivery logging is in F12-006.
### Notifications
- F12-001–F12-003, F12-006, and Modules 03–11.
### Security
- One configured dispatch policy per business event at go-live.
### Integrations
- Incomplete recipient setup can suppress a critical alert.
### Dependencies
- Asynchronous, retry-safe processing with no source-workflow blocking.
### Assumptions
- [('Alert mapping and delivery status view', 'UI', 'Easy', 4), ('Event routing and recipient-resolution operations', 'API', 'Complex', 8), ('Event-dispatch correlation state', 'Database', 'Medium', 4), ('Channel dispatch coordination', 'Integration', 'Easy', 8), ('Process-alert tests', 'Testing', 'Complex', 8), ('Process-alert guide', 'Documentation', 'Medium', 3)]
### Risks
- 
### Non Functional Requirements
- 

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Alert mapping and delivery status view | UI | Easy | 4 |
| Event routing and recipient-resolution operations | API | Complex | 8 |
| Event-dispatch correlation state | Database | Medium | 4 |
| Channel dispatch coordination | Integration | Easy | 8 |
| Process-alert tests | Testing | Complex | 8 |
| Process-alert guide | Documentation | Medium | 3 |
| **Total** | | | **35** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. [('Alert mapping and delivery status view', 'UI', 'Easy', 4), ('Event routing and recipient-resolution operations', 'API', 'Complex', 8), ('Event-dispatch correlation state', 'Database', 'Medium', 4), ('Channel dispatch coordination', 'Integration', 'Easy', 8), ('Process-alert tests', 'Testing', 'Complex', 8), ('Process-alert guide', 'Documentation', 'Medium', 3)]
