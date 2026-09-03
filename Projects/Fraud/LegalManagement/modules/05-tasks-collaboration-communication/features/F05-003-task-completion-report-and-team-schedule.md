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
1. Who creates: Assignee
2. How they create: Assignee marks the task complete, attaches the completion report, and publishes.
3. How they edit: Supervisor opens Team Member Task Schedule and status view for the period.
4. How they send for approval: Completed tasks show report attached; incomplete remain on the schedule. Attach report → mark complete → publish → supervisor schedule.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Assignee works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Assignee opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Task Completion Report attach screen
- Team Member Task Schedule and status view
- Publish completion with attachment
- Period filter for supervisor

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Task Completion Report attach screen | Medium |
| Team Member Task Schedule | Complex |
| Task completion report and team schedule history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Complete and schedule operations | Complex |
| Update task completion report and team schedule | Medium |
| Search task completion report and team schedule | Medium |
| Read task completion report and team schedule history | Easy |

### Inputs
Completion flag; completion report file; period for schedule; team member.

### Outputs
Completed task; attached report; schedule view.

### Business Rules
- Completion requires the completion report attachment as specified.
- Schedule is team-member-wise for the selected period.
- Not payroll timesheets (time entry on Android is F09-004).

### Validations
- Complete blocked without attachment if configured mandatory; period required for schedule.

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
- Attachment is the completion report, not an expense voucher (Module 07).

### Risks
Marking complete without a usable report if validation is skipped.

### Non Functional Requirements
Schedule view for a typical Legal Cell team size.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Task Completion Report attach screen | UI | Medium | 6 |
| Team Member Task Schedule | UI | Complex | 12 |
| Task completion report and team schedule history | UI | Medium | 6 |
| Complete and schedule operations | API | Complex | 8 |
| Update task completion report and team schedule | API | Medium | 6 |
| Search task completion report and team schedule | API | Medium | 6 |
| Read task completion report and team schedule history | API | Easy | 4 |
| Task completion report and team schedule persistence | DB | Medium | 4 |
| Internal task/matter handoff | Integration | Simple | 4 |
| Task completion report and team schedule feature tests | Testing | Medium | 6 |
| Task completion report and team schedule implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **64** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
