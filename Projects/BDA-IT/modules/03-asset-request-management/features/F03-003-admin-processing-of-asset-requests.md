# F03-003 — Admin Processing of Asset Requests

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Admin Processing of Asset Requests |
| **Module** | 03 — Asset Request Management |

### Description
Admin reviews **all** asset requests, adds an internal remark, and updates status (Open, In progress, Closed, Rejected) so the requester’s tracking view can change.

### Business Objective
IT can work the asset-request queue and leave an auditable status and remark.

### Actors
Maker: Admin. Applicant: User (requester, view-only via F03-002). Approver: none.

### User Journey
1. Who creates: Admin does not raise the request here; they act on requests already submitted.
2. How they create: All asset requests register → open a request → add remark if needed → set status → confirm.
3. How they edit: Admin may change status again (for example Open → In progress → Closed) and add further remarks. Users cannot edit.
4. How they send for approval: Submit/approval does not apply. Admin’s status change is the operational decision, not a second checker.
5. How the approver sees pending items: There is no checker inbox. Admin uses this register (and Module 05) as the work list.
6. How the approver decides: There is no separate approver. Admin sets In progress, Closed, or Rejected.
7. How the applicant / maker sees history: The requester sees the new status under F03-002. Admin sees remarks and status history on the admin detail.
8. How the approver / auditor sees history: Admin uses the same admin detail and status history.

### Functional Capabilities
- Search all requests by status and date
- Open any request including attachment
- Add internal remark
- Update status among Open, In progress, Closed, Rejected
- Record who changed status and when

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| All asset requests register | Medium |
| Admin asset request detail | Medium |
| Status change confirmation | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search all asset requests | Medium |
| Update asset request status | Complex |
| Add internal remark | Easy |
| Read asset request for admin | Easy |

### Inputs
Status, date range, remark, new status.

### Outputs
Updated request status; remark; history visible to Admin and (status only) to the requester.

### Business Rules
- Only Admin changes status.
- Rejected is available for asset requests.
- Remarks are Admin-facing; requester sees status (and may see a short public remark if stored on the request — internal remark remains Admin-only).

### Validations
- New status must be one of the allowed values.
- Status change requires confirmation.

### Calculations
None.

### Workflow
Admin status change only. No maker–checker.

### Search Requirements
Filter all requests by status, date, requester name, asset type.

### Documents
View the requester’s optional attachment; Admin does not replace it in this phase.

### Reports
None on this feature (counts are Module 05).

### Notifications
None.

### Security
Admin only for all-records and status change. User cannot open this register.

### Integrations
None.

### Dependencies
F03-001; F01-003 (Admin role).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Internal remark is not a threaded chat; it is a short Admin note with history.
- Dashboard counts are Module 05.

### Risks
Without a second Admin, mistaken Rejected/Closed is corrected only by another Admin status change.

### Non Functional Requirements
Status changes attributable to the Admin account; register usable for typical BDA IT volumes.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| All asset requests register | UI | Medium | 6 |
| Admin asset request detail | UI | Medium | 6 |
| Status change confirmation | UI | Simple | 2 |
| Search all asset requests | API | Medium | 6 |
| Update asset request status | API | Complex | 8 |
| Add internal remark | API | Easy | 4 |
| Read asset request for admin | API | Easy | 4 |
| Request status history records | DB | Easy | 2 |
| Admin processing of asset requests tests | Testing | Medium | 6 |
| Admin processing of asset requests implementation documentation | Documentation | Easy | 2 |

**Feature total: 46 hours**
