# F06-002 — Backup and Restore Verification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Backup and Restore Verification |
| **Module** | 06 — e-Office Upload, Backup and Progress MIS |

### Description
Log daily incremental backup of scanned documents to secure external storage and record periodic restore tests. Data-loss events that force rescan are recorded (rescan cost remains commercial/zero extra).

### Business Objective
IFQ backup/restore obligations are demonstrable to the Department.

### Actors
Maker: Supervisor. Approver: none.

### User Journey
1. Who creates: Supervisor at end of day (backup) and on the restore-test schedule.
2. How they create: Backup log → record backup date, media, operator, file-count snapshot → Save. Restore test form → record test date, sample IDs, pass/fail.
3. How they edit: Correct notes; cannot delete a day’s backup log.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox. Missing backup days visible to Department Officer.
6. How the approver decides: No decision.
7. How the maker sees history: Backup calendar.
8. How the auditor sees history: Same.

### Functional Capabilities
- Daily backup log
- Restore test log
- Flag missing backup day
- Record data-loss/rescan event

### UI Screens
| Screen | Complexity |
|---|---|
| Backup log | Easy |
| Restore test form | Easy |

### Logical API operations
| Operation | Complexity |
|---|---|
| Record backup | Medium |
| Record restore test | Medium |
| Search backup logs | Easy |

### Inputs
Date, media identity, counts, restore sample result.

### Outputs
Attributable backup/restore trail.

### Business Rules
- Daily backup required during production.
- Restore tests periodic as agreed with Department.
- Confidentiality of backup media.

### Validations
- Backup date unique per day unless increment batches.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
By date, fail restore.

### Documents
Backup media (physical/process).

### Reports
Backup compliance on MIS.

### Notifications
None.

### Security
Supervisor only to record; Department Officer views.

### Integrations
None (external disk, not a cloud product).

### Dependencies
F03-002.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Not building a backup appliance.

### Risks
Backup skipped on busy days.

### Non Functional Requirements
One-minute end-of-day recording.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Backup log | UI | Easy | 4 |
| Restore test form | UI | Easy | 4 |
| Record backup | API | Medium | 6 |
| Record restore test | API | Medium | 6 |
| Search backup logs | API | Easy | 4 |
| Backup records | DB | Easy | 2 |
| Backup and restore verification tests | Testing | Medium | 6 |
| Backup and restore verification implementation documentation | Documentation | Easy | 2 |

**Feature total: 34 hours**
