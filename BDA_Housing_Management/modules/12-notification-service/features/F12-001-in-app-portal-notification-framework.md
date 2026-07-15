# F12-001 — In-app & Portal Notification Framework

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F12-001 |
| **Feature Name** | In-app & Portal Notification Framework |
| **Module** | 12 — Notification Service |

### Description
Provide a persistent portal notification centre for citizens and officers, with read status and permitted preference controls.
### Business Objective
Keep users informed of BHMS events within their authenticated channel.
### Actors
- System; Citizen; BDA officers; Super Administrator
### User Journey
1. A BHMS event creates an in-app notification. 2. The authorized recipient views it in the portal. 3. Read status and delivery outcome are retained.
### Functional Capabilities
- Notification inbox, read/unread state, source links, role/citizen recipient resolution, and permitted preferences.
### Inputs
- Event, recipient, message/template reference, and source link.
### Outputs
- Authorized notification list, unread count, and source navigation.
### Business Rules
- Recipients are resolved by the owning process; portal alerts do not replace mandatory SMS/email alerts.
### Validations
- Recipient ownership, active source reference, and permitted channel preference.
### Calculations
- Source-defined notification counts and delivery statuses only.
### Workflow
- Event created → notification available → read/archived.
### Search Requirements
- By recipient, source process, date, read status, and notification type.
### Documents
- Source-linked letters, receipts, or notices when the recipient is permitted.
### Reports
- Notification volume and unread/failed-delivery visibility.
### Notifications
- In-app delivery confirmation; Module 12 handles related external-channel alerts.
### Security
- RBAC, protected recipient contact details, citizen ownership isolation, and auditable operational access.
### Integrations
- Internal BHMS event sources and templates.
### Dependencies
- Modules 01–02 and 03–11; F12-005/F12-006.
### Assumptions
- Templates are maintained in Module 02.
### Risks
- Poor event configuration can result in missed portal notifications.
### Non Functional Requirements
- Asynchronous delivery, responsive portal access, and durable notification history.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Notification centre and preferences | UI | Complex | 8 |
| Notification retrieval and preference operations | API | Complex | 8 |
| Notification and preference state | Database | Medium | 4 |
| Notification framework tests | Testing | Complex | 8 |
| Notification framework guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. Templates are maintained in Module 02.
