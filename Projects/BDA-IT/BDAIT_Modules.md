# BDA IT Asset Request and Helpdesk — Module List

Source: SoW_BDAIT_Detailed.md

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | User Account and Access Management | Shared | Admin creates employee and contractor logins; username and password managed by Admin only; User and Admin roles. | Explicit in SOW |
| 02 | Dropdown Values | Business | Admin creates the values shown in the asset-type and ticket-category dropdowns. | Explicit in SOW (simplified from original master-maintenance intent) |
| 03 | Asset Request Management | Business | User raises and tracks own asset requests; Admin processes all requests and updates status. | Explicit in SOW |
| 04 | Ticket Management | Business | User raises and tracks own IT tickets; Admin processes all tickets and updates status. | Explicit in SOW |
| 05 | Admin Dashboard | Business | Simple Admin view of request and ticket volumes, open work, and filters. | Explicit in SOW |

***Module Details***

### 01. User Account and Access Management

- **Type:** Shared
- **Summary:** Admin creates employee and contractor logins; username and password managed by Admin only; User and Admin roles.
- **Source:** Explicit in SOW
- **In Scope:** Employee accounts with mandatory unique employee number; contractor accounts without employee number; Admin-set username and password (create, change, reset); login with role session; enable and disable without deleting history.
- **Out of Scope:** Person master, post/position, person-to-post mapping, self-registration, self-service password, forgot-password, OTP/2FA, SSO/AD/LDAP.
- **Key Actors:** Admin (creates and controls accounts); User and Admin (sign in).
- **Dependencies:** None. Foundation for all other modules.
- **Notes:** Access model is user → role (User or Admin). No organisational hierarchy.

### 02. Dropdown Values

- **Type:** Business
- **Summary:** Admin creates the values shown in the asset-type and ticket-category dropdowns.
- **Source:** Explicit in SOW (user confirmed: create dropdown values only — no catalogue)
- **In Scope:** Admin adds values for two dropdowns (Asset type, Ticket category); list those values on the Admin screen and on raise forms.
- **Out of Scope:** Catalogue / item master, edit, deactivate, master history, inventory, stock, barcode, procurement catalogues, SLA catalogues.
- **Key Actors:** Admin creates values; User selects from dropdowns on raise forms.
- **Dependencies:** Module 01 (Admin role).
- **Notes:** One feature. Create-only.

### 03. Asset Request Management

- **Type:** Business
- **Summary:** User raises and tracks own asset requests; Admin processes all requests and updates status.
- **Source:** Explicit in SOW
- **In Scope:** Raise request using asset-type dropdown, description, optional attachment; user list/detail of own requests; Admin register, remark, and status (Open / In progress / Closed / Rejected).
- **Out of Scope:** Fixed-asset register, allocation, return/scrap, purchase/tender, maker–checker approval, email/SMS.
- **Key Actors:** User (raise and track own); Admin (see all, update status).
- **Dependencies:** Modules 01 and 02 (F02-001).
- **Notes:** Status workflow and optional attachment are embedded. No separate DMS or workflow engine.

### 04. Ticket Management

- **Type:** Business
- **Summary:** User raises and tracks own IT tickets; Admin processes all tickets and updates status.
- **Source:** Explicit in SOW
- **In Scope:** Raise ticket using ticket-category dropdown, description, optional attachment; user list/detail of own tickets; Admin register, remark, and status (Open / In progress / Closed).
- **Out of Scope:** Telephony, SLA clocks, escalation matrix, knowledge base, email/SMS, maker–checker.
- **Key Actors:** User (raise and track own); Admin (see all, update status).
- **Dependencies:** Modules 01 and 02 (F02-001).
- **Notes:** Status workflow and optional attachment are embedded.

### 05. Admin Dashboard

- **Type:** Business
- **Summary:** Simple Admin view of request and ticket volumes, open work, and filters.
- **Source:** Explicit in SOW
- **In Scope:** Counts by status for requests and tickets; short list of recent/open items with drill-through; filter by type, status, and date. Admin only.
- **Out of Scope:** User-facing dashboard, GIS, executive analytics, scheduled PDF/Excel MIS packs, citizen KPIs.
- **Key Actors:** Admin.
- **Dependencies:** Modules 01, 03, and 04.
- **Notes:** Users track status via their own lists in modules 03 and 04, not this dashboard.

***Excluded / Embedded Capabilities***

| Capability | Treatment |
|------------|-----------|
| Login / identity | Covered in Module 01; not a separate identity product |
| Document management | Embedded as optional attachment on request and ticket |
| Workflow / approval | Embedded as Admin status change; no maker–checker module |
| Audit of create/change | Embedded on users, dropdown values, requests, tickets, and status |
| Search / filter | Part of registers and the Admin dashboard |
| Notifications (email/SMS) | Out of scope per SOW |
| API / integration hub | Out of scope — no external systems in Phase 1 |
| Reporting / MIS engine | Not a separate module; dashboard is Module 05 |
| Data migration | Out of scope |

***Assumptions***

1. SOW module numbers `{NN}` and feature IDs `F{NN}-{SEQ}` are reused without renumbering.
2. One Admin role covers helpdesk processing; no separate agent role.
3. Hosting, SSL, and backup operations are not application modules.

***Risks***

1. If BDA later requires HR validation of employee number, Module 01 grows and an integration module may be needed.
2. If BDA later requires email/SMS status alerts, a notification module would be added; it is not implied now.
3. Treating this product as an asset inventory or purchase system would expand Module 03 beyond the SOW.
