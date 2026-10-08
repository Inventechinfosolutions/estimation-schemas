# F03-003 — Scheduling & milestones

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-003 |
| Feature Name | Scheduling & milestones |
| Module | 03 — Campaign Management |
| Description | Define campaign calendar windows and key milestones for print run, digital flight, and outdoor display periods. |
| Business Objective | Align field PoD capture windows and compliance reporting with when advertising is supposed to be live. |
| Actors | Campaign Officer; Approver (read) |

### User Journey

- Officer opens approved campaign → Scheduling tab → sets overall start/end → adds milestones (e.g., creative lock, outdoor mount, digital go-live) → system flags PoD tasks outside active window (F03-007) → calendar view shows overlapping channels.

### Functional Capabilities

- Campaign date window editor with channel-specific sub-windows where needed
- Milestone list with type, date, owner, completion flag
- Milestone overdue indicators on campaign dashboard
- Conflict warning when outdoor milestone dates miss location availability

### Inputs

- Start/end dates, milestone name, type, due date, notes, completion status

### Outputs

- Schedule record driving PoD eligibility and reports

### Business Rules

- End date cannot precede start date
- Milestone types from configurable lookup
- Major date changes on live campaigns may require re-approval (policy flag)

### Validations

- Milestone dates within campaign window unless exception flag with comment

### Calculations

- Optional duration days display for reporting

### Workflow

- Planned milestones → completed as campaign executes

### Search Requirements

- Campaign list filter by date range overlapping window

### Documents

- None

### Reports

- Feeds Module 07 schedule compliance views

### Notifications

- Optional reminder before milestone due (Module 08)

### Security

- Update on campaign schedule per role; read for entitled viewers

### Integrations

- None

### Dependencies

- F03-001 approved campaign; F03-007 uses windows

### Assumptions

- No external calendar sync (Outlook) in baseline

### Risks

- Frequent date slips require audit of who changed windows

### Non Functional Requirements

- Calendar/list views remain usable for multi-channel campaigns

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Campaign flight calendar month view | Medium | 6 |
| UI | Channel-specific run window editor | Medium | 6 |
| UI | Milestone list with due dates | Easy | 4 |
| UI | Milestone completion toggle for coordinators | Easy | 4 |
| UI | Schedule conflict warning dialog | Simple | 2 |
| UI | Milestone overdue indicator chips | Simple | 2 |
| UI | Schedule list view (non-Gantt) | Easy | 4 |
| API | Get campaign schedule aggregate | Easy | 4 |
| API | CRUD flight windows per media channel | Medium | 6 |
| API | CRUD campaign milestones | Easy | 4 |
| API | Detect overlapping run windows | Medium | 6 |
| API | Mark milestone complete with timestamp | Easy | 4 |
| Database | Schedule window entity | Easy | 2 |
| Database | Milestone entity with campaign FK | Easy | 2 |
| Testing | Window validation (end before start) | Easy | 4 |
| Testing | Overlap detection across channels | Medium | 6 |
| Testing | Milestone overdue flag computation | Easy | 4 |
| Documentation | Campaign scheduling operations notes | Easy | 2 |
| Documentation | UAT milestone tracking walkthrough | Simple | 1 |

**Feature Total: 73 hours**

### Estimation Assumptions

- Full Gantt project management features are out of scope.
