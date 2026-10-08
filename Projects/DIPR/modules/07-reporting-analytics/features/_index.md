# Feature Index — Ultra Detailed
## 07 — Reporting & Analytics

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Line items | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|-----------:|-------|
| F07-001 | Campaign KPI dashboards | 46 | 24 | 6 | 0 | 22 | 5 | 103 | 17 |  |
| F07-002 | Channel-wise spend analytics | 32 | 18 | 6 | 0 | 18 | 5 | 79 | 14 |  |
| F07-003 | Compliance & PoD reports | 28 | 20 | 6 | 0 | 20 | 5 | 79 | 13 |  |
| F07-004 | Audit log export | 12 | 16 | 2 | 0 | 10 | 2 | 42 | 10 |  |
| F07-005 | Scheduled & exportable reports | 40 | 34 | 8 | 8 | 22 | 5 | 117 | 16 |  |
| F07-006 | Role-based report views | 10 | 16 | 2 | 0 | 8 | 2 | 38 | 9 |  |

**Module Total:** **458 hours** · **79 artefact line items**

### Module estimation line-item roll-up

| Area | Hours |
|------|------:|
| UI | 168 |
| API | 128 |
| Database | 30 |
| Integration | 8 |
| Testing | 100 |
| Documentation | 24 |

### Ultra-detailed artefact catalogue

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F07-001 | UI | Executive KPI dashboard shell with date/campaign filters | Very High | 16 |
| F07-001 | UI | Campaign status KPI card strip | Medium | 6 |
| F07-001 | UI | PoD verification progress KPI cards | Medium | 6 |
| F07-001 | UI | Field completion funnel chart panel | Complex | 12 |
| F07-001 | UI | Drill-down to campaign list from KPI click | Easy | 4 |
| F07-001 | UI | Role-scoped dashboard empty state | Simple | 2 |
| F07-001 | API | Campaign count aggregates by status | Medium | 6 |
| F07-001 | API | PoD submitted/verified/rejected KPI aggregates | Complex | 8 |
| F07-001 | API | Field task completion rate aggregate | Medium | 6 |
| F07-001 | API | Dashboard filter metadata (campaigns, regions) | Easy | 4 |
| F07-001 | Database | KPI aggregate materialized summary support | Medium | 4 |
| F07-001 | Database | Dashboard query indexes on campaign dates | Easy | 2 |
| F07-001 | Testing | Role-scoped KPI visibility | Complex | 8 |
| F07-001 | Testing | Filter combination accuracy | Medium | 6 |
| F07-001 | Testing | KPI numbers vs source module sample | Complex | 8 |
| F07-001 | Documentation | KPI definition dictionary | Medium | 3 |
| F07-001 | Documentation | Dashboard user interpretation guide | Easy | 2 |
| F07-002 | UI | Spend analytics filter bar (channel, period, campaign) | Medium | 6 |
| F07-002 | UI | Channel spend bar/column chart panel | Complex | 12 |
| F07-002 | UI | Drill-down spend detail grid | Complex | 12 |
| F07-002 | UI | Export current view trigger | Simple | 2 |
| F07-002 | API | Channel spend summary aggregation | Complex | 8 |
| F07-002 | API | Spend detail paginated fetch | Medium | 6 |
| F07-002 | API | Channel master join for labels | Easy | 4 |
| F07-002 | Database | Spend roll-up summary store | Medium | 4 |
| F07-002 | Database | Analytics period partition helpers | Easy | 2 |
| F07-002 | Testing | Spend totals reconciliation sample | Complex | 8 |
| F07-002 | Testing | Unknown channel edge handling | Easy | 4 |
| F07-002 | Testing | Drill-down permission bounds | Medium | 6 |
| F07-002 | Documentation | Spend metric definitions | Medium | 3 |
| F07-002 | Documentation | Reconciliation with campaign budget notes | Easy | 2 |
| F07-003 | UI | Compliance report parameter form | Complex | 12 |
| F07-003 | UI | PoD outcome results grid with status badges | Complex | 12 |
| F07-003 | UI | Report run progress indicator | Easy | 4 |
| F07-003 | API | Build compliance report dataset | Complex | 8 |
| F07-003 | API | PoD verification outcome query | Medium | 6 |
| F07-003 | API | Report export file generation trigger | Medium | 6 |
| F07-003 | Database | Compliance report query views support | Medium | 4 |
| F07-003 | Database | Verification outcome indexed lookups | Easy | 2 |
| F07-003 | Testing | Compliance figures vs PoD source UAT | Complex | 8 |
| F07-003 | Testing | Parameter validation negative cases | Medium | 6 |
| F07-003 | Testing | Large result set pagination | Medium | 6 |
| F07-003 | Documentation | Compliance report field dictionary | Medium | 3 |
| F07-003 | Documentation | Auditor usage notes | Easy | 2 |
| F07-004 | UI | Audit log filter panel (actor, entity, date range) | Medium | 6 |
| F07-004 | UI | Export format and column picker dialog | Easy | 4 |
| F07-004 | UI | Export job status toast/list | Simple | 2 |
| F07-004 | API | Audit log search with pagination | Medium | 6 |
| F07-004 | API | Generate audit export file job | Medium | 6 |
| F07-004 | API | Export download entitlement check | Easy | 4 |
| F07-004 | Database | Audit log range query indexes | Easy | 2 |
| F07-004 | Testing | Export completeness vs filter | Medium | 6 |
| F07-004 | Testing | Unauthorized export negative | Easy | 4 |
| F07-004 | Documentation | Audit export usage notes | Easy | 2 |
| F07-005 | UI | Report catalogue picker for export | Medium | 6 |
| F07-005 | UI | On-demand export dialog (format, filters) | Complex | 12 |
| F07-005 | UI | Schedule configuration wizard steps | Very High | 16 |
| F07-005 | UI | Scheduled job list with next-run display | Medium | 6 |
| F07-005 | API | Render report to PDF/Excel job | Very High | 16 |
| F07-005 | API | Create/update report schedule | Complex | 8 |
| F07-005 | API | Cancel/pause scheduled report job | Easy | 4 |
| F07-005 | API | Fetch report job status and download link | Medium | 6 |
| F07-005 | Integration | Scheduled completion email via Module 08 | Easy | 8 |
| F07-005 | Database | Report job queue persistence | Medium | 4 |
| F07-005 | Database | Schedule recurrence rule storage | Medium | 4 |
| F07-005 | Testing | One-off export format validation | Complex | 8 |
| F07-005 | Testing | Scheduled cron fire mock | Complex | 8 |
| F07-005 | Testing | Failed job retry notification | Medium | 6 |
| F07-005 | Documentation | Report scheduling admin guide | Medium | 3 |
| F07-005 | Documentation | Supported formats matrix | Easy | 2 |
| F07-006 | UI | Report catalogue entitlement matrix admin grid | Medium | 6 |
| F07-006 | UI | Preview report as role simulator panel | Easy | 4 |
| F07-006 | API | List reports with effective entitlement | Medium | 6 |
| F07-006 | API | Save role-to-report mapping updates | Easy | 4 |
| F07-006 | API | Enforce entitlement on report render requests | Medium | 6 |
| F07-006 | Database | Role-report mapping table | Easy | 2 |
| F07-006 | Testing | Cross-role visibility negative tests | Easy | 4 |
| F07-006 | Testing | Verifier vs admin catalogue diff | Easy | 4 |
| F07-006 | Documentation | Report RBAC configuration notes | Easy | 2 |
