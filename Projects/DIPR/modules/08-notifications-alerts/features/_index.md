# Feature Index — Ultra Detailed
## 08 — Notifications & Alerts

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Line items | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|-----------:|-------|
| F08-001 | In-app notification centre | 28 | 18 | 6 | 0 | 16 | 3 | 71 | 17 |  |
| F08-002 | Email notification dispatch | 10 | 18 | 3 | 24 | 16 | 4 | 75 | 14 |  |
| F08-003 | SMS notification provision | 14 | 14 | 2 | 24 | 14 | 4 | 72 | 14 | OPTIONAL |
| F08-004 | Notification preference & delivery log | 24 | 16 | 8 | 0 | 16 | 3 | 67 | 12 |  |

**Module Total:** **285 hours** · **57 artefact line items**

### Module estimation line-item roll-up

| Area | Hours |
|------|------:|
| UI | 76 |
| API | 66 |
| Database | 19 |
| Integration | 48 |
| Testing | 62 |
| Documentation | 14 |

### Ultra-detailed artefact catalogue

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F08-001 | UI | Web notification bell with unread badge | Easy | 4 |
| F08-001 | UI | Web notification centre drawer with list | Complex | 12 |
| F08-001 | UI | Notification detail/read expand row | Easy | 4 |
| F08-001 | UI | Mobile field in-app notification feed | Medium | 6 |
| F08-001 | UI | Mark all read action bar | Simple | 2 |
| F08-001 | API | Create in-app notification on platform events | Medium | 6 |
| F08-001 | API | List notifications with pagination | Easy | 4 |
| F08-001 | API | Mark single notification read | Simple | 2 |
| F08-001 | API | Mark all read for user | Simple | 2 |
| F08-001 | API | Unread count aggregate | Easy | 4 |
| F08-001 | Database | In-app notification entity store | Medium | 4 |
| F08-001 | Database | Per-user read state index | Easy | 2 |
| F08-001 | Testing | Event-to-in-app delivery mapping | Medium | 6 |
| F08-001 | Testing | Unread badge accuracy | Easy | 4 |
| F08-001 | Testing | Mobile feed parity | Medium | 6 |
| F08-001 | Documentation | In-app notification event catalogue | Easy | 2 |
| F08-001 | Documentation | Badge polling behaviour notes | Simple | 1 |
| F08-002 | UI | Email template preview panel in admin | Medium | 6 |
| F08-002 | UI | Test send dialog with recipient override | Easy | 4 |
| F08-002 | API | Render notification to email body merge | Complex | 8 |
| F08-002 | API | Queue email dispatch attempt | Medium | 6 |
| F08-002 | API | Record delivery status callback handler | Easy | 4 |
| F08-002 | Integration | SMTP/email gateway connector | Easy | 8 |
| F08-002 | Integration | TLS credential vault binding | Medium | 16 |
| F08-002 | Database | Email dispatch attempt log | Easy | 2 |
| F08-002 | Database | Template version reference fields | Simple | 1 |
| F08-002 | Testing | Template merge with sample events | Medium | 6 |
| F08-002 | Testing | Gateway failure retry behaviour | Medium | 6 |
| F08-002 | Testing | Invalid recipient negative | Easy | 4 |
| F08-002 | Documentation | Email dispatch event list | Easy | 2 |
| F08-002 | Documentation | DIPR SMTP setup checklist | Easy | 2 |
| F08-003 | UI | SMS channel enablement toggle admin | Easy | 4 |
| F08-003 | UI | SMS test send panel | Easy | 4 |
| F08-003 | UI | Provider credential masked form | Medium | 6 |
| F08-003 | API | SMS message render from template | Easy | 4 |
| F08-003 | API | SMS dispatch submit operation | Easy | 4 |
| F08-003 | API | Opt-out flag enforcement check | Medium | 6 |
| F08-003 | Integration | SMS gateway REST connector | Medium | 16 |
| F08-003 | Integration | Credential vault and rate limit | Easy | 8 |
| F08-003 | Database | SMS dispatch attempt log | Easy | 2 |
| F08-003 | Testing | Mock gateway send success | Medium | 6 |
| F08-003 | Testing | Opt-out suppression negative | Easy | 4 |
| F08-003 | Testing | Invalid MSISDN validation | Easy | 4 |
| F08-003 | Documentation | SMS provision checklist for DIPR | Easy | 2 |
| F08-003 | Documentation | Template length and encoding notes | Easy | 2 |
| F08-004 | UI | User notification preference settings screen | Complex | 12 |
| F08-004 | UI | Channel opt-in/opt-out per event category | Medium | 6 |
| F08-004 | UI | Delivery log viewer with filters | Medium | 6 |
| F08-004 | API | Fetch user notification preferences | Easy | 4 |
| F08-004 | API | Save preference updates with policy bounds | Medium | 6 |
| F08-004 | API | Query delivery log paginated | Medium | 6 |
| F08-004 | Database | User preference persistence | Medium | 4 |
| F08-004 | Database | Delivery log append-only store | Medium | 4 |
| F08-004 | Testing | Policy bounds on mandatory alerts | Medium | 6 |
| F08-004 | Testing | Delivery log accuracy vs dispatch | Medium | 6 |
| F08-004 | Testing | Preference change audit | Easy | 4 |
| F08-004 | Documentation | Notification preference policy guide | Medium | 3 |
