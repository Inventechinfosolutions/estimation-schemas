# Feature Index — Ultra Detailed
## 06 — Mobile Field Application

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Line items | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|-----------:|-------|
| F06-001 | Field task & checklist inbox | 40 | 28 | 4 | 0 | 16 | 4 | 92 | 19 |  |
| F06-002 | Mobile PoD capture | 34 | 26 | 6 | 12 | 24 | 5 | 107 | 20 |  |
| F06-003 | Offline mode & local queue | 16 | 40 | 10 | 0 | 32 | 5 | 103 | 17 |  |
| F06-004 | Sync & conflict resolution | 20 | 46 | 6 | 40 | 28 | 5 | 145 | 19 |  |
| F06-005 | Mobile secure session | 12 | 18 | 1 | 24 | 16 | 2 | 73 | 15 |  |

**Module Total:** **520 hours** · **90 artefact line items**

### Module estimation line-item roll-up

| Area | Hours |
|------|------:|
| UI | 122 |
| API | 158 |
| Database | 27 |
| Integration | 76 |
| Testing | 116 |
| Documentation | 21 |

### Ultra-detailed artefact catalogue

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F06-001 | UI | AMT Field Home with sync badge and assignment summary | Easy | 4 |
| F06-001 | UI | Field task inbox list with campaign/site/status filters | Complex | 12 |
| F06-001 | UI | Task detail header with due date and campaign context | Medium | 6 |
| F06-001 | UI | Checklist step panel with mandatory item markers | Medium | 6 |
| F06-001 | UI | Checklist item capture (yes/no, notes, optional photo gate) | Medium | 6 |
| F06-001 | UI | PoD launch shortcut from task when configured | Simple | 2 |
| F06-001 | UI | Pull-to-refresh and empty-state offline hint panel | Easy | 4 |
| F06-001 | API | List assigned field tasks with filters | Medium | 6 |
| F06-001 | API | Fetch task detail and checklist definition | Easy | 4 |
| F06-001 | API | Submit checklist item responses batch | Medium | 6 |
| F06-001 | API | Mark task in-progress/completed transitions | Easy | 4 |
| F06-001 | API | Validate mandatory checklist before PoD eligibility | Complex | 8 |
| F06-001 | Database | Checklist response progress store | Easy | 2 |
| F06-001 | Database | Task status transition audit fields | Easy | 2 |
| F06-001 | Testing | Assigned-only visibility and filter scenarios | Medium | 6 |
| F06-001 | Testing | Mandatory checklist negative before PoD | Medium | 6 |
| F06-001 | Testing | Checklist completion happy path | Easy | 4 |
| F06-001 | Documentation | Field inbox operator guide | Easy | 2 |
| F06-001 | Documentation | Checklist completion business rules appendix | Easy | 2 |
| F06-002 | UI | PoD capture launcher from task context | Simple | 2 |
| F06-002 | UI | Camera live preview with capture controls | Complex | 12 |
| F06-002 | UI | Gallery picker when policy enabled | Easy | 4 |
| F06-002 | UI | GPS/timestamp/device metadata read-only panel | Medium | 6 |
| F06-002 | UI | Image preview retake and quality warning dialog | Medium | 6 |
| F06-002 | UI | Submit confirmation with connectivity/queue status | Easy | 4 |
| F06-002 | API | Initiate mobile PoD capture session with context | Easy | 4 |
| F06-002 | API | Upload PoD media multipart with checksum | Complex | 8 |
| F06-002 | API | Attach GPS/timestamp/device attestation metadata | Medium | 6 |
| F06-002 | API | Finalize PoD submit to verification queue | Complex | 8 |
| F06-002 | Database | Mobile PoD staging record | Medium | 4 |
| F06-002 | Database | Capture metadata extension fields | Easy | 2 |
| F06-002 | Integration | Device GPS location service bridge | Simple | 4 |
| F06-002 | Integration | Device camera and gallery capability bridge | Easy | 8 |
| F06-002 | Testing | Happy path camera capture with GPS | Complex | 8 |
| F06-002 | Testing | Gallery disabled policy negative | Easy | 4 |
| F06-002 | Testing | GPS accuracy threshold failure | Medium | 6 |
| F06-002 | Testing | Media size/quality validation | Medium | 6 |
| F06-002 | Documentation | Mobile PoD field capture SOP | Medium | 3 |
| F06-002 | Documentation | Metadata attestation notes for verifiers | Easy | 2 |
| F06-003 | UI | Global offline banner and connectivity badge | Easy | 4 |
| F06-003 | UI | Queued items list with type and retry status | Medium | 6 |
| F06-003 | UI | Queue item detail with error reason dialog | Easy | 4 |
| F06-003 | UI | Storage quota warning dialog | Simple | 2 |
| F06-003 | API | Connectivity state observer hook | Simple | 2 |
| F06-003 | API | Enqueue PoD media and checklist delta operations | Very High | 16 |
| F06-003 | API | Dequeue and mark-in-flight queue operations | Complex | 8 |
| F06-003 | API | Queue deduplication key validation | Medium | 6 |
| F06-003 | API | Encrypted local persistence read/write layer | Complex | 8 |
| F06-003 | Database | On-device queue entity store | Complex | 6 |
| F06-003 | Database | Staged media blob index | Medium | 4 |
| F06-003 | Testing | App restart queue survival | Complex | 8 |
| F06-003 | Testing | Duplicate enqueue prevention | Medium | 6 |
| F06-003 | Testing | Disk quota handling | Medium | 6 |
| F06-003 | Testing | Offline PoD then online drain smoke | Very High | 12 |
| F06-003 | Documentation | Offline operations field runbook | Medium | 3 |
| F06-003 | Documentation | Queue encryption and retention notes | Easy | 2 |
| F06-004 | UI | Sync progress modal with batch counters | Medium | 6 |
| F06-004 | UI | Background sync status chip on field home | Easy | 4 |
| F06-004 | UI | Conflict resolution choice dialog (server/client/manual) | Medium | 6 |
| F06-004 | UI | Sync failure detail with retry action | Easy | 4 |
| F06-004 | API | Start sync batch with auth gate | Medium | 6 |
| F06-004 | API | Upload queued PoD media chunks | Complex | 8 |
| F06-004 | API | Upload checklist/task delta batch | Complex | 8 |
| F06-004 | API | Server version compare for conflict detection | Complex | 8 |
| F06-004 | API | Apply conflict resolution rule outcome | Very High | 16 |
| F06-004 | Integration | Mobile-to-server delta sync orchestration | Complex | 24 |
| F06-004 | Integration | Exponential backoff retry scheduler | Medium | 16 |
| F06-004 | Database | Sync cursor per device | Easy | 2 |
| F06-004 | Database | Conflict audit and resolution log | Medium | 4 |
| F06-004 | Testing | Server-wins conflict scenario | Complex | 8 |
| F06-004 | Testing | Client-wins with notes merge | Complex | 8 |
| F06-004 | Testing | Auth expiry mid-sync recovery | Medium | 6 |
| F06-004 | Testing | Media integrity failure retry | Medium | 6 |
| F06-004 | Documentation | Sync and conflict DIPR rules matrix | Medium | 3 |
| F06-004 | Documentation | Support troubleshooting guide | Easy | 2 |
| F06-005 | UI | Mobile login screen aligned to AMT branding | Easy | 4 |
| F06-005 | UI | Session timeout warning modal | Simple | 2 |
| F06-005 | UI | Re-authentication prompt on policy violation | Easy | 4 |
| F06-005 | UI | Secure logout confirmation clearing cache | Simple | 2 |
| F06-005 | API | Mobile login and token issuance | Medium | 6 |
| F06-005 | API | Token refresh on idle boundary | Easy | 4 |
| F06-005 | API | Device registration label submit | Easy | 4 |
| F06-005 | API | Secure logout and session revoke | Easy | 4 |
| F06-005 | Integration | Module 01 identity and MFA handoff | Medium | 16 |
| F06-005 | Integration | Optional SSO deep-link return handling | Easy | 8 |
| F06-005 | Database | Device session registration record | Simple | 1 |
| F06-005 | Testing | Session expiry and re-auth flow | Medium | 6 |
| F06-005 | Testing | Failed login throttle alignment | Medium | 6 |
| F06-005 | Testing | Logout clears sensitive local cache | Easy | 4 |
| F06-005 | Documentation | Mobile session policy notes | Easy | 2 |
