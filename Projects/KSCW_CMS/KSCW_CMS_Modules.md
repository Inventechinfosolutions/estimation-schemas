# Karnataka State Commission for Women (KSCW) — Complaint Management System (CMS) — Module List

Source: `SoW_KSCW_CMS_Detailed.md`

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | User Access & Role Management | Shared | Users, roles (Admin / Supervisor / Operator + FRS roles), authentication | Explicit in SOW |
| 02 | Master Data & System Configuration | Shared | Taxonomy, location, SLA/escalation params, notification templates, statuses | Explicit in SOW |
| 03 | Multi-Channel Complaint Registration | Business | Web, mobile, email, call-center intake with acknowledgement & attachments | Explicit in SOW |
| 04 | Categorization, Auto-Routing & Assignment | Business | Categorize and auto-route by department / priority / location; worklists | Explicit in SOW |
| 05 | Workflow Automation, Escalation & SLA Tracking | Business | Workflow stages, escalation matrix, SLA clocks, resolution/closure | Explicit in SOW |
| 06 | Notifications & Alerts (SMS / Email) | Technical | SMS and Email dispatch with delivery logging | Explicit in SOW |
| 07 | Dashboards, Analytics, Real-time Monitoring & MIS | Business | Role dashboards, monitoring, analytics, MIS export | Explicit in SOW |

---

## Module Details

### 01. User Access & Role Management

- **Type:** Shared
- **Summary:** Secure authentication and role-based access for CMS users.
- **Source:** Explicit in document (SOW §6 Module 01; §8)
- **In Scope:**
  - User create / update / activate / deactivate
  - Role & permission assignment (Admin, Supervisor, Operator + FRS roles)
  - Authentication and session control for web and mobile
  - Access audit for privileged changes
- **Out of Scope:**
  - External IdP / SSO unless added in FRS
  - Complaint processing screens (Modules 03–05)
- **Key Actors:** Admin; (affects Supervisor, Operator)
- **Dependencies:** None (foundation)
- **Notes:** Access model is **User → Role → Permissions** per SOW.

---

### 02. Master Data & System Configuration

- **Type:** Shared
- **Summary:** Configurable masters and parameters for categorization, routing, SLA, escalation, and notifications.
- **Source:** Explicit in document (SOW §6 Module 02)
- **In Scope:**
  - Complaint taxonomy masters (category, sub-category, department, priority)
  - Location / jurisdiction masters
  - SLA & escalation configuration
  - Notification templates
  - Status & system parameter configuration
- **Out of Scope:**
  - Transactional complaints (Modules 03–05)
  - Standalone Document Management product
- **Key Actors:** Admin
- **Dependencies:** Module 01
- **Notes:** Masters feed routing, SLA, and notifications.

---

### 03. Multi-Channel Complaint Registration

- **Type:** Business
- **Summary:** Capture complaints from web, mobile, email, call center (and FRS-approved other channels) into one register.
- **Source:** Explicit in document (SOW §6 Module 03; §9)
- **In Scope:**
  - Web complaint registration
  - Mobile complaint registration
  - Email channel intake
  - Call-center intake
  - Unique acknowledgement / reference
  - Attachment / evidence capture (embedded documents)
- **Out of Scope:**
  - Routing engine (Module 04)
  - Workflow / SLA processing (Module 05)
  - Hardware for call center
- **Key Actors:** Complainant (web/mobile); Operator (call center / assisted email); Admin
- **Dependencies:** Modules 01, 02; Module 06 for acknowledgement notifications where configured
- **Notes:** Channel “etc.” only if approved in FRS.

---

### 04. Categorization, Auto-Routing & Assignment

- **Type:** Business
- **Summary:** Categorize complaints and auto-route by department, priority, and location into worklists.
- **Source:** Explicit in document (SOW §6 Module 04)
- **In Scope:**
  - Complaint categorization
  - Auto-routing rules (department / priority / location)
  - Worklist & assignment to Supervisor / Operator
  - Reassignment / reclassification with audit
- **Out of Scope:**
  - Full workflow stage engine (Module 05)
  - Master definition of taxonomy (Module 02)
- **Key Actors:** Supervisor; Operator; Admin (rules)
- **Dependencies:** Modules 01, 02, 03
- **Notes:** Routing consumes Module 02 masters.

---

### 05. Workflow Automation, Escalation & SLA Tracking

- **Type:** Business
- **Summary:** Process complaints through configured stages with escalation matrix and SLA tracking to closure.
- **Source:** Explicit in document (SOW §6 Module 05)
- **In Scope:**
  - Workflow stage processing with remarks/documents
  - Escalation matrix execution
  - SLA tracking & aging
  - Resolution & closure
  - Supervisor oversight of pending / escalated / breached items
- **Out of Scope:**
  - Standalone generic workflow product
  - Notification transport (Module 06)
- **Key Actors:** Operator; Supervisor; Admin
- **Dependencies:** Modules 01–04; Module 06 for escalation/SLA alerts
- **Notes:** Workflow embedded in complaint lifecycle.

---

### 06. Notifications & Alerts (SMS / Email)

- **Type:** Technical
- **Summary:** Dispatch SMS and Email alerts for configured complaint events with delivery logging.
- **Source:** Explicit in document (SOW §6 Module 06; §10)
- **In Scope:**
  - SMS notification dispatch
  - Email notification dispatch
  - Notification log & retry support for operations/warranty
- **Out of Scope:**
  - Gateway commercial accounts (KSCW/KEONICS facilitated)
  - In-app only alerts unless added in FRS
- **Key Actors:** System; Admin (templates via Module 02)
- **Dependencies:** Modules 02–05 (event producers)
- **Notes:** Templates configured in Module 02; transport here.

---

### 07. Dashboards, Analytics, Real-time Monitoring & MIS

- **Type:** Business
- **Summary:** Role-based dashboards, near-real-time monitoring, analytics, and MIS reports with export.
- **Source:** Explicit in document (SOW §6 Module 07)
- **In Scope:**
  - Operational dashboards
  - Real-time / near-real-time monitoring
  - Analytics views
  - MIS reports & export
- **Out of Scope:**
  - BI tool procurement
  - Ad-hoc data science beyond approved dashboard design
- **Key Actors:** Admin; Supervisor; Operator (limited)
- **Dependencies:** Modules 03–05 (transactional data)
- **Notes:** Align to approved Dashboard Design document.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
| ---------- | --------- |
| Document / attachment handling | Embedded in Modules 03 and 05 |
| Workflow engine (generic product) | Embedded in Module 05 |
| Audit logging | System-wide NFR + Module 01 access audit |
| Safe-to-Host / CERT-In audits | Delivery / warranty services — not a functional module |
| Training, manuals, deployment | Delivery services — not a functional module |
| Data porting | Implementation/migration activity — not a functional module |
| Helpdesk / warranty operations | Warranty services — not a functional module |

---

## Assumptions

1. Module `{NN}` and feature `F{NN}-{SEQ}` IDs match `SoW_KSCW_CMS_Detailed.md`.
2. Final field-level scope is locked by approved FRS / UI-UX-Workflow / Dashboard designs.
3. Access model remains User → Role → Permissions unless FRS changes it.
4. Infrastructure is provided by KSCW; agency submits requirements only.
5. SMS/Email gateway credentials facilitated by KSCW / KEONICS.

---

## Risks

1. One-month delivery window may constrain depth of channel integrations (email/call center) if FRS expands late.
2. “Etc.” channels in IFQ may expand scope if not tightly controlled in FRS approval.
3. Warranty “enhancements” vs “minor changes” boundary may affect sustainment effort (commercial, not Phase-1 feature hours).
4. CERT-In Safe-to-Host findings may force remediations inside the T+30 window.
