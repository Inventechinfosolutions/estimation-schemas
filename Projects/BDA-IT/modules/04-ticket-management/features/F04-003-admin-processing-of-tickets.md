# F04-003 — Admin Processing of Tickets

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | Admin Processing of Tickets |
| **Module** | 04 — Ticket Management |

### Description
Admin reviews **all** tickets, adds an internal remark, and updates status (Open, In progress, Closed) so the requester’s tracking view can change. Tickets do not use Rejected.

### Business Objective
IT can work the helpdesk queue and leave an auditable status and remark.

### Actors
Maker: Admin. Applicant: User (requester, view-only via F04-002). Approver: none.

### User Journey
1. Who creates: Admin acts on tickets already submitted.
2. How they create: All tickets register → open a ticket → add remark if needed → set status → confirm.
3. How they edit: Admin may change status again (Open → In progress → Closed) and add further remarks.
4. How they send for approval: Submit/approval does not apply. Admin’s status change is the operational decision.
5. How the approver sees pending items: There is no checker inbox. Admin uses this register (and Module 05) as the work list.
6. How the approver decides: There is no separate approver. Admin sets In progress or Closed.
7. How the applicant / maker sees history: The requester sees the new status under F04-002. Admin sees remarks and status history on the admin detail.
8. How the approver / auditor sees history: Admin uses the same admin detail and status history.

### Functional Capabilities
- Search all tickets by status and date
- Open any ticket including attachment
- Add internal remark
- Update status among Open, In progress, Closed
- Record who changed status and when

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| All tickets register | Medium |
| Admin ticket detail | Medium |
| Status change confirmation | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search all tickets | Medium |
| Update ticket status | Medium |
| Add internal remark | Easy |
| Read ticket for admin | Easy |

### Inputs
Status, date range, remark, new status.

### Outputs
Updated ticket status; remark; history.

### Business Rules
- Only Admin changes status.
- Allowed statuses: Open, In progress, Closed (no Rejected).
- Internal remark is Admin-only.

### Validations
- New status must be one of the allowed ticket values.
- Status change requires confirmation.

### Calculations
None.

### Workflow
Admin status change only. No maker–checker.

### Search Requirements
Filter all tickets by status, date, requester name, category.

### Documents
View the requester’s optional attachment.

### Reports
None on this feature (counts are Module 05).

### Notifications
None.

### Security
Admin only for all-records and status change.

### Integrations
None.

### Dependencies
F04-001; F01-003 (Admin role).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Status update is Medium (three statuses, no Rejected) versus Complex on asset-request processing.
- Dashboard counts are Module 05.

### Risks
Without SLA clocks, Admin must rely on Open/In progress lists to avoid stale tickets.

### Non Functional Requirements
Status changes attributable to the Admin account.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| All tickets register | UI | Medium | 6 |
| Admin ticket detail | UI | Medium | 6 |
| Status change confirmation | UI | Simple | 2 |
| Search all tickets | API | Medium | 6 |
| Update ticket status | API | Medium | 6 |
| Add internal remark | API | Easy | 4 |
| Read ticket for admin | API | Easy | 4 |
| Ticket status history records | DB | Easy | 2 |
| Admin processing of tickets tests | Testing | Medium | 6 |
| Admin processing of tickets implementation documentation | Documentation | Easy | 2 |

**Feature total: 44 hours**
