# F05-003 — Task completion report and team schedule

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-003 |
| **Feature Name** | Task completion report and team schedule |
| **Module** | 05 — Tasks, Collaboration & Communication |

### Description
The assignee marks the task complete, attaches the completion report, and publishes. A supervisor opens the team member task schedule and status view for the period.

### Business Objective
Close tasks with an attached completion report and give supervisors a team-member schedule and status view.

### Actors
Assignee; supervisor; Legal Cell.

### User Journey
1. Assignee marks the task complete, attaches the completion report, and publishes.
2. Supervisor opens Team Member Task Schedule and status view for the period.
3. Completed tasks show report attached; incomplete remain on the schedule.

### Functional Capabilities
- Task Completion Report attach screen
- Team Member Task Schedule and status view
- Publish completion with attachment
- Period filter for supervisor

### Inputs
Completion flag; completion report file; period for schedule; team member.

### Outputs
Completed task; attached report; schedule view.

### Business Rules
- Completion requires the completion report attachment as specified.
- Schedule is team-member-wise for the selected period.
- Not payroll timesheets (time entry on Android is F09-004).

### Validations
Complete blocked without attachment if configured mandatory; period required for schedule.

### Calculations
None beyond status counts on the schedule.

### Workflow
Attach report → mark complete → publish → supervisor schedule.

### Search Requirements
Schedule by Person, period, status, matter.

### Documents
Completion report attachment.

### Reports
Team member task schedule/status.

### Notifications
Completion notice to assigner/supervisor.

### Security
Schedule scoped to Posts the supervisor may see.

### Integrations
Internal matter/task (Simple).

### Dependencies
F05-001; F05-002; F04-002.

### Assumptions
Attachment is the completion report, not an expense voucher (Module 07).

### Risks
Marking complete without a usable report if validation is skipped.

### Non Functional Requirements
Schedule view for a typical Legal Cell team size.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Task Completion Report attach screen | UI | Medium | 6 |
| Team Member Task Schedule | UI | Complex | 12 |
| Complete and schedule operations | API | Complex | 8 |
| Completion and schedule entities | Database | Medium | 4 |
| Internal task/matter handoff | Integration | Simple | 4 |
| Completion and schedule tests | Testing | Medium | 6 |
| Completion report and team schedule guide | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- Android mark-complete is F09-002 consuming this API.
