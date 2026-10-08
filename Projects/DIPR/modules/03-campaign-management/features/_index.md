# Feature Index — Ultra Detailed
## 03 — Campaign Management

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Line items | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|-----------:|-------|
| F03-001 | Campaign create & maintain | 42 | 46 | 10 | 0 | 20 | 5 | 123 | 24 |  |
| F03-002 | Campaign approval workflow | 42 | 48 | 7 | 0 | 28 | 5 | 130 | 25 |  |
| F03-003 | Scheduling & milestones | 28 | 24 | 4 | 0 | 14 | 3 | 73 | 19 |  |
| F03-004 | Budget & spend tracking | 36 | 30 | 8 | 0 | 16 | 4 | 94 | 19 |  |
| F03-005 | Vendor assignment | 24 | 26 | 4 | 0 | 16 | 2 | 72 | 16 |  |
| F03-006 | Campaign version control | 32 | 24 | 6 | 0 | 16 | 2 | 80 | 15 |  |
| F03-007 | Campaign–PoD linkage | 28 | 22 | 6 | 0 | 12 | 2 | 70 | 14 |  |

**Module Total:** **642 hours** · **132 artefact line items**

### Module estimation line-item roll-up

| Area | Hours |
|------|------:|
| UI | 232 |
| API | 220 |
| Database | 45 |
| Integration | 0 |
| Testing | 122 |
| Documentation | 23 |

### Ultra-detailed artefact catalogue

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F03-001 | UI | Campaign register with channel/status filters | Medium | 6 |
| F03-001 | UI | Campaign create wizard step 1 (identity, dates) | Medium | 6 |
| F03-001 | UI | Wizard step 2 multi-channel attribute panels | Complex | 12 |
| F03-001 | UI | Wizard step 3 district coverage and budget head | Medium | 6 |
| F03-001 | UI | Campaign detail summary tabs (overview, channels) | Easy | 4 |
| F03-001 | UI | Draft save and resume banner | Simple | 2 |
| F03-001 | UI | Duplicate campaign from existing dialog | Medium | 6 |
| F03-001 | API | List campaigns with filters and pagination | Medium | 6 |
| F03-001 | API | Create campaign draft | Medium | 6 |
| F03-001 | API | Update campaign profile and channel attributes | Complex | 8 |
| F03-001 | API | Promote draft to valid pre-approval state | Medium | 6 |
| F03-001 | API | Get campaign detail aggregate | Medium | 6 |
| F03-001 | API | Clone campaign from existing template | Medium | 6 |
| F03-001 | API | Validate print/digital/outdoor mandatory attributes | Complex | 8 |
| F03-001 | Database | Campaign core entity | Easy | 2 |
| F03-001 | Database | Per-channel attribute extension storage | Medium | 4 |
| F03-001 | Database | District coverage junction | Easy | 2 |
| F03-001 | Database | Draft status and version pointer | Easy | 2 |
| F03-001 | Testing | Print/digital/outdoor attribute validation matrix | Medium | 6 |
| F03-001 | Testing | Draft to pre-approval transition rules | Medium | 6 |
| F03-001 | Testing | Duplicate campaign data integrity | Easy | 4 |
| F03-001 | Testing | Register filter and pagination combinations | Easy | 4 |
| F03-001 | Documentation | Campaign setup playbook for DIPR staff | Easy | 2 |
| F03-001 | Documentation | UAT multi-channel campaign creation script | Medium | 3 |
| F03-002 | UI | Campaign approval inbox list with SLA badges | Medium | 6 |
| F03-002 | UI | Inbox filters (stage, district, channel) | Easy | 4 |
| F03-002 | UI | Multi-stage approval action panel | Complex | 12 |
| F03-002 | UI | Reject reason modal with mandatory comment | Simple | 2 |
| F03-002 | UI | Request changes panel for campaign originator | Medium | 6 |
| F03-002 | UI | Approval history timeline on campaign detail | Easy | 4 |
| F03-002 | UI | Delegated approver assignment dialog | Medium | 6 |
| F03-002 | UI | Concurrent approval conflict notification | Simple | 2 |
| F03-002 | API | List pending approvals for current approver | Medium | 6 |
| F03-002 | API | Get workflow instance with stage definitions | Medium | 6 |
| F03-002 | API | Approve stage transition | Complex | 8 |
| F03-002 | API | Reject with reason and rollback stage | Complex | 8 |
| F03-002 | API | Resubmit campaign after rework | Medium | 6 |
| F03-002 | API | Record approval comments per stage | Easy | 4 |
| F03-002 | API | Trigger notification on stage change | Medium | 6 |
| F03-002 | API | Read workflow config by campaign type | Easy | 4 |
| F03-002 | Database | Workflow instance and stage state storage | Medium | 4 |
| F03-002 | Database | Approval comment and decision log | Easy | 2 |
| F03-002 | Database | Stage SLA timestamp fields | Simple | 1 |
| F03-002 | Testing | Multi-stage approve happy path | Complex | 8 |
| F03-002 | Testing | Reject and resubmit loop | Complex | 8 |
| F03-002 | Testing | Wrong role cannot approve stage | Medium | 6 |
| F03-002 | Testing | Concurrent approver safe handling | Medium | 6 |
| F03-002 | Documentation | Campaign approval configuration guide | Medium | 3 |
| F03-002 | Documentation | UAT multi-stage sign-off script | Easy | 2 |
| F03-003 | UI | Campaign flight calendar month view | Medium | 6 |
| F03-003 | UI | Channel-specific run window editor | Medium | 6 |
| F03-003 | UI | Milestone list with due dates | Easy | 4 |
| F03-003 | UI | Milestone completion toggle for coordinators | Easy | 4 |
| F03-003 | UI | Schedule conflict warning dialog | Simple | 2 |
| F03-003 | UI | Milestone overdue indicator chips | Simple | 2 |
| F03-003 | UI | Schedule list view (non-Gantt) | Easy | 4 |
| F03-003 | API | Get campaign schedule aggregate | Easy | 4 |
| F03-003 | API | CRUD flight windows per media channel | Medium | 6 |
| F03-003 | API | CRUD campaign milestones | Easy | 4 |
| F03-003 | API | Detect overlapping run windows | Medium | 6 |
| F03-003 | API | Mark milestone complete with timestamp | Easy | 4 |
| F03-003 | Database | Schedule window entity | Easy | 2 |
| F03-003 | Database | Milestone entity with campaign FK | Easy | 2 |
| F03-003 | Testing | Window validation (end before start) | Easy | 4 |
| F03-003 | Testing | Overlap detection across channels | Medium | 6 |
| F03-003 | Testing | Milestone overdue flag computation | Easy | 4 |
| F03-003 | Documentation | Campaign scheduling operations notes | Easy | 2 |
| F03-003 | Documentation | UAT milestone tracking walkthrough | Simple | 1 |
| F03-004 | UI | Campaign budget header summary panel | Medium | 6 |
| F03-004 | UI | Budget line-item spend entry grid | Complex | 12 |
| F03-004 | UI | Spend vs budget variance summary card | Easy | 4 |
| F03-004 | UI | Vendor-wise spend breakdown chart | Medium | 6 |
| F03-004 | UI | Budget revision request form | Medium | 6 |
| F03-004 | UI | Spend locked after campaign closed banner | Simple | 2 |
| F03-004 | API | Get budget and spend summary for campaign | Medium | 6 |
| F03-004 | API | CRUD budget line items | Medium | 6 |
| F03-004 | API | Record actual spend entry with validation | Complex | 8 |
| F03-004 | API | Calculate variance and burn rate | Medium | 6 |
| F03-004 | API | Enforce spend lock on closed campaign | Easy | 4 |
| F03-004 | Database | Budget header and line-item storage | Medium | 4 |
| F03-004 | Database | Spend transaction log | Easy | 2 |
| F03-004 | Database | Budget revision history | Easy | 2 |
| F03-004 | Testing | Over-budget warning rules | Medium | 6 |
| F03-004 | Testing | Closed campaign spend entry blocked | Easy | 4 |
| F03-004 | Testing | Line-item totals reconciliation | Medium | 6 |
| F03-004 | Documentation | Budget tracking notes for finance liaison | Easy | 2 |
| F03-004 | Documentation | UAT variance spot-check script | Easy | 2 |
| F03-005 | UI | Campaign vendor assignment panel | Medium | 6 |
| F03-005 | UI | Vendor picker with channel capability filter | Medium | 6 |
| F03-005 | UI | Assignment scope matrix (district/channel) | Medium | 6 |
| F03-005 | UI | Remove vendor assignment confirmation | Simple | 2 |
| F03-005 | UI | Vendor assignment change history list | Easy | 4 |
| F03-005 | API | List vendor assignments for campaign | Easy | 4 |
| F03-005 | API | Assign vendor with district/channel scope | Medium | 6 |
| F03-005 | API | Update assignment scope | Medium | 6 |
| F03-005 | API | Remove assignment with active PoD guard | Easy | 4 |
| F03-005 | API | Validate vendor active and channel-capable | Medium | 6 |
| F03-005 | Database | Campaign–vendor assignment junction | Easy | 2 |
| F03-005 | Database | District and channel scope flags | Easy | 2 |
| F03-005 | Testing | Inactive vendor blocked on assign | Medium | 6 |
| F03-005 | Testing | Outdoor capability mismatch rejected | Medium | 6 |
| F03-005 | Testing | Duplicate assignment prevented | Easy | 4 |
| F03-005 | Documentation | Campaign vendor assignment guide | Easy | 2 |
| F03-006 | UI | Campaign version history list | Easy | 4 |
| F03-006 | UI | Compare versions side-by-side diff panel | Complex | 12 |
| F03-006 | UI | Create new version from approved baseline | Medium | 6 |
| F03-006 | UI | Version label and change summary form | Easy | 4 |
| F03-006 | UI | Read-only approved snapshot view | Medium | 6 |
| F03-006 | API | List campaign versions for lineage | Easy | 4 |
| F03-006 | API | Snapshot campaign state as new version | Complex | 8 |
| F03-006 | API | Get version diff metadata | Medium | 6 |
| F03-006 | API | Promote version to current editable draft | Medium | 6 |
| F03-006 | Database | Version snapshot storage | Medium | 4 |
| F03-006 | Database | Version lineage foreign key | Easy | 2 |
| F03-006 | Testing | Snapshot captures channel attributes | Medium | 6 |
| F03-006 | Testing | Compare highlights changed fields | Medium | 6 |
| F03-006 | Testing | Approved version immutability | Easy | 4 |
| F03-006 | Documentation | Campaign version control user notes | Easy | 2 |
| F03-007 | UI | Campaign PoD coverage planner grid | Medium | 6 |
| F03-007 | UI | Link outdoor sites to campaign PoD slots | Medium | 6 |
| F03-007 | UI | Expected PoD count per site indicator | Easy | 4 |
| F03-007 | UI | PoD linkage status dashboard strip | Medium | 6 |
| F03-007 | UI | Bulk link sites from district filter | Medium | 6 |
| F03-007 | API | List PoD plan slots for campaign | Medium | 6 |
| F03-007 | API | Link or unlink site to PoD plan | Medium | 6 |
| F03-007 | API | Compute expected vs submitted PoD counts | Medium | 6 |
| F03-007 | API | Validate outdoor site geotag present | Easy | 4 |
| F03-007 | Database | Campaign–site PoD plan junction | Medium | 4 |
| F03-007 | Database | Expected capture schedule linkage | Easy | 2 |
| F03-007 | Testing | Counts update when PoD submitted | Medium | 6 |
| F03-007 | Testing | Unlink blocked when verified PoD exists | Medium | 6 |
| F03-007 | Documentation | PoD linkage planning guide for coordinators | Easy | 2 |
