# KSAAD_HRMS — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 11,243 hours · **Go-live:** 11,243 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | Person, Post, Role & Access Governance | Shared | 8 | 938 | 8.3% |
| 02 | Master Data & System Configuration | Business | 5 | 465 | 4.1% |
| 03 | HRMS Core Personnel Management | Business | 9 | 1,146 | 10.2% |
| 04 | Deputation & Posting Management | Business | 5 | 561 | 5.0% |
| 05 | HRMS Tour, Travel & TA/DA Claims | Business | 4 | 538 | 4.8% |
| 06 | Office & Administration (Visitor, Reception and Meetings) | Business | 7 | 737 | 6.6% |
| 07 | Audit Planning & Resource Allocation | Business | 4 | 514 | 4.6% |
| 08 | Field Audit Execution & Reporting | Business | 6 | 792 | 7.0% |
| 09 | Objection, Para & Recovery Management | Business | 4 | 486 | 4.3% |
| 10 | Audit Fee, Billing and Collections | Business | 4 | 516 | 4.6% |
| 11 | Finance, Procurement & Inventory Management | Business | 7 | 955 | 8.5% |
| 12 | API Integration Hub | Technical | 4 | 650 | 5.8% |
| 13 | Document Management System (DMS) | Shared | 6 | 660 | 5.9% |
| 14 | Reporting, Dashboards & Analytics | Business | 9 | 1,075 | 9.6% |
| 15 | Knowledge Center & Learning | Business | 4 | 518 | 4.6% |
| 16 | External / Institution Interaction | Business | 6 | 692 | 6.2% |
| | **Total** | | **92** | **11,243** | **100%** |

## Indicative phasing

| Phase | Modules |
|-------|---------|
| P1 — Access, masters and identity governance | 01, 02, 13 |
| P2 — HR and office administration | 03, 04, 05, 06 |
| P3 — Audit planning and field execution | 07, 08 |
| P4 — Objections/recovery and financial operations | 09, 10, 11 |
| P5 — Integrations, reporting and knowledge | 12, 14, 15 |
| P6 — Institution interaction | 16 |

## Exclusions (not in feature hours)

- Hosting infrastructure and annual maintenance (AMC), unless separately ordered.
- Hardware purchase and deployment tickets.
- Classroom training and scanning bureau operations, unless separately ordered.


## 01 — Person, Post, Role & Access Governance (938 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Person Master | 97 | Foundational person identity directory. |
| F01-002 | Post Master and Organisational Placement | 95 | Foundational post catalogue. |
| F01-003 | Post-to-Person Mapping with Effective Dates | 129 | Explicit Person-to-Post mapping. |
| F01-004 | Role-to-Post Mapping and Permission Matrix | 119 | Role assignment is at Post level. |
| F01-005 | Authentication, Session and MFA Controls | 123 | Explicit authentication and MFA. |
| F01-006 | Institution and External Identity with Scoped Access | 119 | External access is isolated from staff Posts. |
| F01-007 | Joiner-Mover-Leaver and Post Reassignment Governance | 127 | JML and post reassignment. |
| F01-008 | Access Audit, Logging and Periodic Recertification | 129 | Logging plus recertification. |

## 02 — Master Data & System Configuration (465 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Organisation Hierarchy and Office Master | 91 | Organisation and office setup. |
| F02-002 | Department, Post and Designation Masters | 91 | Supports governance and HR processes. |
| F02-003 | Reference Data Catalogues | 91 | Shared system catalogues. |
| F02-004 | Workflow Templates and Rule Configuration | 101 | Commercial configurability of routing. |
| F02-005 | Reporting and MIS Parameters | 91 | Supports standardised reporting. |

## 03 — HRMS Core Personnel Management (1,146 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Employee Master and Service Details | 91 | Core HR employee records on the Person. |
| F03-002 | Post and Vacancy Management | 137 | Vacancy uses Post master + current mappings. |
| F03-003 | Leave Management System | 154 | Full leave create / edit / submit / approve / history. |
| F03-004 | Work Diary Submission | 119 | Work diary create / submit / acknowledge / history. |
| F03-005 | Attendance Management | 137 | Attendance capture plus exception approval. |
| F03-006 | Training and Capacity Building Management | 133 | Training nomination workflow. |
| F03-007 | Retirement and Pension Tracking | 137 | Retirement lifecycle tracking. |
| F03-008 | Rewards and Recognition Register | 119 | Rewards register with approval. |
| F03-009 | Circulars, Notifications and Internal Communication | 119 | Circular publish workflow. |

## 04 — Deputation & Posting Management (561 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | Deputation Proposal Initiation | 119 | Proposal intake. |
| F04-002 | Deputation Approval and Tenure Tracking | 125 | Approval-heavy deputation flow. |
| F04-003 | Extension and Early Repatriation | 119 | Extension and repatriation. |
| F04-004 | Post and Vacancy Updates due to Deputation | 79 | Links deputation to vacancy. |
| F04-005 | Deputation History and Hierarchy Adjustments | 119 | History and hierarchy coverage. |

## 05 — HRMS Tour, Travel & TA/DA Claims (538 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Tour Programme Planning | 131 | Tour planning. |
| F05-002 | TA/DA Claim Capture | 141 | Claim capture. |
| F05-003 | Evidence Upload and Claim Validation | 139 | Evidence and validation. |
| F05-004 | Supervisor Review, Approval and Reconciliation | 127 | Approval and reconciliation. |

## 06 — Office & Administration (Visitor, Reception and Meetings) (737 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | Employee Movement Register | 75 | Movement register. |
| F06-002 | Visitor Registration and Access | 93 | Visitor intake. |
| F06-003 | Meeting Scheduling and Participant Management | 125 | Meeting setup. |
| F06-004 | Minutes of Meeting Recording | 119 | MoM capture. |
| F06-005 | Meeting Action Item Tracking | 119 | Action tracking. |
| F06-006 | Grants and Financial Allocation Management | 125 | Grants/allocation. |
| F06-007 | Digitised Office Registers and Administrative Logs | 81 | Office register digitisation. |

## 07 — Audit Planning & Resource Allocation (514 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F07-001 | Auditee Institution and Financial Data Setup | 109 | Auditee setup. |
| F07-002 | Annual Audit Plan Management | 143 | Plan workflow. |
| F07-003 | Auditor Resource Allocation | 125 | Resource allocation. |
| F07-004 | Gram Panchayat Adhoc and Non-Adhoc Committee Tracking | 137 | GP committee tracking. |

## 08 — Field Audit Execution & Reporting (792 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F08-001 | Field Audit Execution Workflow | 123 | Core field workflow. |
| F08-002 | Observation Recording and Evidence Capture | 125 | Observation capture. |
| F08-003 | Audit Report Drafting | 155 | Drafting stage. |
| F08-004 | Audit Report Review and Approval | 145 | Review/approval stage. |
| F08-005 | Audit Report Issuance | 123 | Issuance stage. |
| F08-006 | Timeline, Reminder and Escalation Monitoring | 121 | Reminder/escalation. |

## 09 — Objection, Para & Recovery Management (486 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F09-001 | Para Intake and Tracking | 119 | Para intake. |
| F09-002 | Objection and Representation Reply Workflow | 119 | Objection/reply workflow. |
| F09-003 | Recovery Action Tracking | 129 | Recovery monitoring. |
| F09-004 | Recovery Closure and Evidence Finalisation | 119 | Recovery closure. |

## 10 — Audit Fee, Billing and Collections (516 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F10-001 | Audit Fee Assessment | 135 | Assessment stage. |
| F10-002 | Billing Generation | 123 | Billing generation. |
| F10-003 | Invoice Dispatch and Status Tracking | 119 | Dispatch stage. |
| F10-004 | Collections Reconciliation | 139 | Collection reconciliation. |

## 11 — Finance, Procurement & Inventory Management (955 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F11-001 | Office Expense Management | 119 | Expense control. |
| F11-002 | Budget Allocation and Utilisation Tracking | 133 | Budget utilisation. |
| F11-003 | Indent Management | 131 | Indent workflow. |
| F11-004 | Purchase Order and Vendor Management | 149 | Purchase/vendor. |
| F11-005 | Inventory Management | 151 | Inventory. |
| F11-006 | Asset Register Management | 137 | Asset register. |
| F11-007 | Payment Tracking | 135 | Payment tracking. |

## 12 — API Integration Hub (650 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F12-001 | Integration Framework and Authentication Mapping | 175 | Framework. |
| F12-002 | Data Exchange Orchestration | 201 | Orchestration. |
| F12-003 | Integration Target Adapters | 153 | Target adapters. |
| F12-004 | Monitoring, Logs and Retry Controls | 121 | Monitoring. |

## 13 — Document Management System (DMS) (660 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F13-001 | Document Upload and Classification | 89 | Document intake. |
| F13-002 | Document Version Control | 81 | Version control. |
| F13-003 | Role-Scoped Access and Sharing | 149 | Document ACL. |
| F13-004 | Document Search and Retrieval | 93 | Search/retrieval. |
| F13-005 | Retention and Document Audit Logging | 163 | Retention and audit. |
| F13-006 | Evidence Pack Compilation | 85 | Evidence packs. |

## 14 — Reporting, Dashboards & Analytics (1,075 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F14-001 | Audit Reports and Outputs | 97 | audit operational report outputs. |
| F14-002 | Objection, Para and Recovery Reports | 97 | para/recovery report outputs. |
| F14-003 | Fee Collection Reports | 97 | fee collection report outputs. |
| F14-004 | HRMS Reports | 97 | HRMS report outputs. |
| F14-005 | Administrative Reports | 97 | administration report outputs. |
| F14-006 | Procurement and Financial Reports | 97 | procurement/finance report outputs. |
| F14-007 | Dashboards and Drilldown Views | 191 | Dashboards. |
| F14-008 | Advanced Analytics, MIS and Compliance Reporting | 151 | Analytics/MIS. |
| F14-009 | Custom Exports, Scheduling, Secure Sharing and Alerts | 151 | Export/schedule/share. |

## 15 — Knowledge Center & Learning (518 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F15-001 | Knowledge Repository and Articles | 131 | Knowledge articles. |
| F15-002 | SOP, Policy and Circular Library | 143 | Policy library. |
| F15-003 | Learning Content and Catalogue | 119 | Learning catalogue. |
| F15-004 | Training Completion and Acknowledgement Tracking | 125 | Completion tracking. |

## 16 — External / Institution Interaction (692 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F16-001 | Institution Portal Workspace | 101 | Portal workspace. |
| F16-002 | AFS and Supporting Document Upload | 137 | AFS upload. |
| F16-003 | Submission of Replies to Audit Paras and Objections | 137 | Institution response. |
| F16-004 | View and Download Issued Audit Reports | 87 | Issued report visibility. |
| F16-005 | Audit Fee Assessment and Status Visibility | 77 | Fee visibility. |
| F16-006 | Controlled External Integration Touchpoints | 153 | External touchpoints. |
