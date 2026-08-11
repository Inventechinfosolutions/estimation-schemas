# KSCW CMS — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 1012 hours · **Go-live:** 1012 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | User Access & Role Management | Shared | 4 | 114 | 11.3% |
| 02 | Master Data & System Configuration | Shared | 5 | 135 | 13.3% |
| 03 | Multi-Channel Complaint Registration | Business | 6 | 192 | 19.0% |
| 04 | Categorization, Auto-Routing & Assignment | Business | 4 | 127 | 12.5% |
| 05 | Workflow Automation, Escalation & SLA Tracking | Business | 5 | 176 | 17.4% |
| 06 | Notifications & Alerts (SMS / Email) | Technical | 3 | 103 | 10.2% |
| 07 | Dashboards, Analytics, Real-time Monitoring & MIS | Business | 4 | 165 | 16.3% |
| | **Total** | | **31** | **1012** | **100%** |

## 01 — User Access & Role Management (114 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | User Lifecycle Management | 26 | Create, update, activate / deactivate CMS users |
| F01-002 | Role & Permission Assignment | 34 | Configure Admin, Supervisor, Operator and FRS-defined roles/permissions |
| F01-003 | Authentication & Session Control | 32 | Secure login and session handling for web and mobile |
| F01-004 | Access Audit | 22 | Record privileged user/role changes for audit |

## 02 — Master Data & System Configuration (135 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Complaint Taxonomy Masters | 26 | Categories, sub-categories, departments, priorities |
| F02-002 | Location / Jurisdiction Masters | 28 | Location hierarchy used for routing and reporting |
| F02-003 | SLA & Escalation Configuration | 39 | Configurable SLA timers and escalation matrix parameters |
| F02-004 | Notification Templates | 24 | SMS/Email templates and trigger mapping |
| F02-005 | Status & Parameter Configuration | 18 | Complaint statuses and system parameters |

## 03 — Multi-Channel Complaint Registration (192 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Web Complaint Registration | 39 | Citizen / user complaint intake on web |
| F03-002 | Mobile Complaint Registration | 37 | Complaint intake on mobile application |
| F03-003 | Email Channel Intake | 44 | Register / ingest email-originated complaints |
| F03-004 | Call-Center Intake | 24 | Operator registration of call-center complaints |
| F03-005 | Complaint Acknowledgement | 20 | Unique reference and acknowledgement to complainant as configured |
| F03-006 | Attachment / Evidence Capture | 28 | Upload and link supporting documents/media as configured |

## 04 — Categorization, Auto-Routing & Assignment (127 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | Complaint Categorization | 22 | Apply / update category and related classification |
| F04-002 | Auto-Routing Engine | 41 | Route by department, priority, location rules |
| F04-003 | Worklist & Assignment | 38 | Present routed items to Supervisor / Operator queues |
| F04-004 | Reassignment / Reclassification | 26 | Controlled transfer with history |

## 05 — Workflow Automation, Escalation & SLA Tracking (176 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Workflow Stage Processing | 45 | Action complaints through configured stages |
| F05-002 | Escalation Matrix Execution | 28 | Auto / manual escalation per configured matrix |
| F05-003 | SLA Tracking & Aging | 41 | Track SLA timers, breaches, and aging views |
| F05-004 | Resolution & Closure | 28 | Close / resolve with reasons and evidence as configured |
| F05-005 | Supervisor Oversight | 34 | Monitor pending, escalated, and breached items |

## 06 — Notifications & Alerts (SMS / Email) (103 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | SMS Notification Dispatch | 40 | Send SMS alerts for configured complaint events |
| F06-002 | Email Notification Dispatch | 32 | Send Email alerts for configured complaint events |
| F06-003 | Notification Log & Retry Support | 31 | Track delivery status for support/warranty operations |

## 07 — Dashboards, Analytics, Real-time Monitoring & MIS (165 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F07-001 | Operational Dashboards | 39 | Role-based operational dashboard views |
| F07-002 | Real-time Monitoring | 46 | Live/near-live monitoring of intake, pending, SLA, escalations |
| F07-003 | Analytics Views | 41 | Analytical summaries per approved dashboard design |
| F07-004 | MIS Reports & Export | 39 | Standard MIS reports with export |

## Effort profile

### By module type

| Type | Hours |
|---|---:|
| Business | 660 |
| Shared | 249 |
| Technical | 103 |

### Top features by hours

| Hours | Feature ID | Name | Module |
|---:|---|---|---|
| 46 | F07-002 | Real-time Monitoring | Dashboards, Analytics, Real-time Monitoring & MIS |
| 45 | F05-001 | Workflow Stage Processing | Workflow Automation, Escalation & SLA Tracking |
| 44 | F03-003 | Email Channel Intake | Multi-Channel Complaint Registration |
| 41 | F04-002 | Auto-Routing Engine | Categorization, Auto-Routing & Assignment |
| 41 | F05-003 | SLA Tracking & Aging | Workflow Automation, Escalation & SLA Tracking |
| 41 | F07-003 | Analytics Views | Dashboards, Analytics, Real-time Monitoring & MIS |
| 40 | F06-001 | SMS Notification Dispatch | Notifications & Alerts (SMS / Email) |
| 39 | F02-003 | SLA & Escalation Configuration | Master Data & System Configuration |
| 39 | F03-001 | Web Complaint Registration | Multi-Channel Complaint Registration |
| 39 | F07-001 | Operational Dashboards | Dashboards, Analytics, Real-time Monitoring & MIS |

## Indicative phasing

- **Phase 1 (go-live / ~1-month SOW window):** Modules 01–07 — full feature estimate above.
- **Warranty (3 years):** Helpdesk, CERT-In/Safe-to-Host support, training delivery, and warranty operations are **commercial/delivery services** — **not** included in feature hours.
- **Phase 2 / optional:** Additional channels or enhancements only if approved in FRS (not estimated).

## Exclusions (not in feature hours)

- Training delivery and end-user manuals beyond feature documentation hours
- CERT-In / Safe-to-Host audits and remediation campaigns as delivery services
- 3-year warranty / helpdesk / AMC operations
- Infrastructure procurement and hosting (KSCW-provided)
- SMS/Email gateway commercial fees and accounts
- Hardware for call center / CTI
- Data porting / migration as a separate implementation activity
- Standalone BI tool procurement
