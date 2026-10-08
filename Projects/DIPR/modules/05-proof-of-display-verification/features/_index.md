# Feature Index — Ultra Detailed
## 05 — Proof-of-Display Capture & Verification

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Line items | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|-----------:|-------|
| F05-001 | PoD capture & metadata stamp | 28 | 24 | 6 | 0 | 16 | 4 | 78 | 17 |  |
| F05-002 | Batch PoD upload | 34 | 34 | 6 | 0 | 20 | 4 | 98 | 17 |  |
| F05-003 | Manual verification workflow | 42 | 32 | 6 | 0 | 18 | 5 | 103 | 20 |  |
| F05-004 | PoD validation rules engine | 38 | 32 | 8 | 0 | 26 | 5 | 109 | 18 |  |
| F05-005 | Third-party verification provision | 28 | 32 | 6 | 16 | 20 | 3 | 105 | 17 | OPTIONAL |
| F05-006 | PoD evidence register | 28 | 22 | 6 | 0 | 16 | 2 | 74 | 16 |  |

**Module Total:** **567 hours** · **105 artefact line items**

### Module estimation line-item roll-up

| Area | Hours |
|------|------:|
| UI | 198 |
| API | 176 |
| Database | 38 |
| Integration | 16 |
| Testing | 116 |
| Documentation | 23 |

### Ultra-detailed artefact catalogue

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F05-001 | UI | Single PoD capture form (photo + metadata) | Medium | 6 |
| F05-001 | UI | Camera EXIF auto-fill panel | Easy | 4 |
| F05-001 | UI | Campaign and outdoor site cascaded picker | Medium | 6 |
| F05-001 | UI | Capture timestamp and GPS stamp display | Easy | 4 |
| F05-001 | UI | Submit PoD confirmation summary | Simple | 2 |
| F05-001 | UI | PoD draft save for poor connectivity | Medium | 6 |
| F05-001 | API | Create PoD record with media attachment | Complex | 8 |
| F05-001 | API | Extract and validate EXIF/GPS metadata | Medium | 6 |
| F05-001 | API | Resolve campaign–site PoD linkage | Medium | 6 |
| F05-001 | API | Persist metadata stamp fields on evidence | Easy | 4 |
| F05-001 | Database | PoD evidence core entity | Medium | 4 |
| F05-001 | Database | Metadata stamp columns (GPS, time, device) | Easy | 2 |
| F05-001 | Testing | Happy path with valid EXIF/GPS | Medium | 6 |
| F05-001 | Testing | Missing GPS handling per validation rules | Medium | 6 |
| F05-001 | Testing | Wrong campaign–site linkage rejected | Easy | 4 |
| F05-001 | Documentation | PoD capture field guide for field staff | Easy | 2 |
| F05-001 | Documentation | UAT single PoD submission script | Easy | 2 |
| F05-002 | UI | Batch PoD upload wizard — file selection step | Medium | 6 |
| F05-002 | UI | Batch wizard — column mapping grid | Complex | 12 |
| F05-002 | UI | Batch wizard — validation preview with errors | Medium | 6 |
| F05-002 | UI | Batch progress and per-row status table | Medium | 6 |
| F05-002 | UI | Download batch error report CSV | Easy | 4 |
| F05-002 | API | Initiate batch PoD ingest job | Complex | 8 |
| F05-002 | API | Map spreadsheet rows to PoD entities | Complex | 8 |
| F05-002 | API | Row-level validation before commit | Medium | 6 |
| F05-002 | API | Commit batch with partial success policy | Complex | 8 |
| F05-002 | API | Export batch error report | Easy | 4 |
| F05-002 | Database | Batch job header and row status | Medium | 4 |
| F05-002 | Database | Batch ingest staging table | Easy | 2 |
| F05-002 | Testing | All-valid rows commit successfully | Medium | 6 |
| F05-002 | Testing | Partial failure and rollback policy | Complex | 8 |
| F05-002 | Testing | Column mapping errors surfaced pre-commit | Medium | 6 |
| F05-002 | Documentation | Batch PoD upload template specification | Easy | 2 |
| F05-002 | Documentation | UAT batch ingest script | Easy | 2 |
| F05-003 | UI | PoD verifier work queue with priority sort | Medium | 6 |
| F05-003 | UI | Side-by-side creative vs PoD review screen | Complex | 12 |
| F05-003 | UI | Zoom and pan controls on PoD image | Medium | 6 |
| F05-003 | UI | Accept/reject/rework action panel | Medium | 6 |
| F05-003 | UI | Reject reason code picker modal | Simple | 2 |
| F05-003 | UI | Rework instructions comment box | Easy | 4 |
| F05-003 | UI | Verification status history timeline | Easy | 4 |
| F05-003 | UI | Conflict-of-interest self-declare checkbox | Simple | 2 |
| F05-003 | API | List pending PoD verification queue | Medium | 6 |
| F05-003 | API | Get PoD with linked approved creative asset | Medium | 6 |
| F05-003 | API | Record verifier accept decision | Complex | 8 |
| F05-003 | API | Record reject or rework with reason | Complex | 8 |
| F05-003 | API | Reassign queue item to another verifier | Easy | 4 |
| F05-003 | Database | Verification decision and reason codes | Medium | 4 |
| F05-003 | Database | Verifier assignment log | Easy | 2 |
| F05-003 | Testing | Rework loop until accept | Complex | 8 |
| F05-003 | Testing | Verifier cannot verify own submission | Medium | 6 |
| F05-003 | Testing | Reject reason mandatory validation | Easy | 4 |
| F05-003 | Documentation | Verifier desk procedures | Medium | 3 |
| F05-003 | Documentation | UAT manual verification desk script | Easy | 2 |
| F05-004 | UI | PoD validation rules admin register | Medium | 6 |
| F05-004 | UI | Rule condition builder editor | Complex | 12 |
| F05-004 | UI | Rule priority ordering drag list | Medium | 6 |
| F05-004 | UI | Rule outcome badges on PoD detail view | Easy | 4 |
| F05-004 | UI | Test rule against sample PoD panel | Medium | 6 |
| F05-004 | UI | Rule publish/activate toggle | Easy | 4 |
| F05-004 | API | CRUD PoD validation rule definitions | Medium | 6 |
| F05-004 | API | Evaluate rules on PoD ingest | Very High | 16 |
| F05-004 | API | Re-evaluate rules on demand for PoD | Medium | 6 |
| F05-004 | API | List evaluation results for PoD | Easy | 4 |
| F05-004 | Database | Rule definition storage | Medium | 4 |
| F05-004 | Database | Per-PoD per-rule evaluation result | Medium | 4 |
| F05-004 | Testing | GPS drift distance fail rule | Complex | 8 |
| F05-004 | Testing | Capture timestamp conflict fail | Medium | 6 |
| F05-004 | Testing | Mandatory metadata fail paths | Medium | 6 |
| F05-004 | Testing | Rule priority ordering outcomes | Medium | 6 |
| F05-004 | Documentation | Validation rules catalog for DIPR sign-off | Easy | 2 |
| F05-004 | Documentation | UAT rule pack regression set notes | Medium | 3 |
| F05-005 | UI | Third-party verifier organisation register | Medium | 6 |
| F05-005 | UI | API credential issue and revoke panel | Medium | 6 |
| F05-005 | UI | Outbound PoD queue for external verification | Easy | 4 |
| F05-005 | UI | External status webhook monitor dashboard | Medium | 6 |
| F05-005 | UI | Manual reconcile external decision screen | Medium | 6 |
| F05-005 | API | Register third-party verifier client | Medium | 6 |
| F05-005 | API | Push PoD package to external verifier | Complex | 8 |
| F05-005 | API | Receive callback/webhook verification decision | Complex | 8 |
| F05-005 | API | Reconcile conflicting internal/external decisions | Medium | 6 |
| F05-005 | API | Rotate third-party API credentials | Easy | 4 |
| F05-005 | Integration | External verifier REST adapter (auth, mapping) | Medium | 16 |
| F05-005 | Database | External verifier client registry | Easy | 2 |
| F05-005 | Database | Outbound/inbound integration message log | Medium | 4 |
| F05-005 | Testing | Push and callback happy path | Complex | 8 |
| F05-005 | Testing | Auth failure and retry behaviour | Medium | 6 |
| F05-005 | Testing | Reconcile with internal manual verify | Medium | 6 |
| F05-005 | Documentation | Third-party verification integration runbook | Medium | 3 |
| F05-006 | UI | PoD evidence register with status filters | Medium | 6 |
| F05-006 | UI | Evidence detail with metadata stamp panel | Medium | 6 |
| F05-006 | UI | Chain-of-custody timeline on evidence | Easy | 4 |
| F05-006 | UI | Bulk verification status filter chips | Easy | 4 |
| F05-006 | UI | Register export for audit evidence pack | Medium | 6 |
| F05-006 | UI | Tamper/rule-fail indicator column | Simple | 2 |
| F05-006 | API | Search PoD evidence register | Medium | 6 |
| F05-006 | API | Get evidence detail with media references | Medium | 6 |
| F05-006 | API | Export register slice for audit | Medium | 6 |
| F05-006 | API | Append custody event on evidence access | Easy | 4 |
| F05-006 | Database | Evidence register denormalized view | Medium | 4 |
| F05-006 | Database | Custody event append log | Easy | 2 |
| F05-006 | Testing | Filter by campaign and verification status | Medium | 6 |
| F05-006 | Testing | Export cap and field mask by role | Medium | 6 |
| F05-006 | Testing | Custody events recorded on download | Easy | 4 |
| F05-006 | Documentation | PoD evidence register audit guide | Easy | 2 |
