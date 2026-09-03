# F09-006 — Attendance and expense on Android

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-006 |
| **Feature Name** | Attendance and expense on Android |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
The user submits court attendance or an expense line with voucher photo/upload from the device, linked to the matter, as on web.

### Business Objective
Capture court attendance and expense lines on Android with voucher photo, always linked to the matter as on web.

### Actors
Advocate; Legal Cell.

### User Journey
1. Who creates: Advocate
2. How they create: User submits court attendance or an expense line with voucher photo/upload from the device.
3. How they edit: Linked to the matter, as on web (F07).
4. How they send for approval: Cause list photo may accompany attendance. Capture on device → sync → web matter dashboard.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Android Attendance form + cause list photo
- Android Expense + voucher camera/upload
- Mandatory matter link as F07-005
- Parity with web submit
- Not EVAL valuer billing

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Android Attendance form + cause list photo | Complex |
| Android Expense + voucher camera/upload | Complex |
| Attendance and expense on android history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Attendance/expense submit operations | Complex |
| Update attendance and expense on android | Medium |
| Search attendance and expense on android | Medium |
| Read attendance and expense on android history | Easy |

### Inputs
Attendance fields as F07-001; expense categories as F07-002; photos.

### Outputs
Attendance/expense rows on web matter.

### Business Rules
- Linked to the matter as on web.
- Unlinked personal notes refused.
- Bill compile/review may remain web (F07-004).

### Validations
- Same as web; photo size limits; matter required.

### Calculations
Duration if times entered.

### Workflow
Capture on device → sync → web matter dashboard.

### Search Requirements
After sync, F07-003 on web; device list of own drafts.

### Documents
Cause list and voucher images.

### Reports
None on device.

### Notifications
Sync failure.

### Security
Photos not stored in an unprotected gallery export; attributed Person.

### Integrations
Web attendance/expense (Medium).

### Dependencies
F07-001; F07-002; F07-005; F01-004.

### Assumptions
- Camera permissions; offline draft then sync.

### Risks
Unreadable voucher photo.

### Non Functional Requirements
Court-precinct capture; retry upload.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Android Attendance form + cause list photo | UI | Complex | 12 |
| Android Expense + voucher camera/upload | UI | Complex | 12 |
| Attendance and expense on android history | UI | Medium | 6 |
| Attendance/expense submit operations | API | Complex | 8 |
| Update attendance and expense on android | API | Medium | 6 |
| Search attendance and expense on android | API | Medium | 6 |
| Read attendance and expense on android history | API | Easy | 4 |
| Attendance and expense on android persistence | DB | Medium | 4 |
| Web attendance and expense backend | Integration | Medium | 16 |
| Attendance and expense on Android feature tests | Testing | Complex | 8 |
| Attendance and expense on Android implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **85** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
