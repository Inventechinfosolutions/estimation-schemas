# Advertisement Monitoring Tool (AMT) — Module List

Source: `SoW_AMT_Detailed.md` (from DIPR E-Tender DIPR/DD(P)/E-Tender/AMT/2026-27/ and Inventech pre-bid queries)

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | User & Access Management | Shared | Users, roles, permissions, optional SSO, MFA, access audit | Explicit (tender §II) |
| 02 | Master Data & System Configuration | Business | Media/campaign/vendor/location masters, templates, parameters | Derived (needed by campaigns/PoD/reports) |
| 03 | Campaign Management | Business | Campaign create, approvals, schedule, budget, vendors, versions, PoD linkage | Explicit (tender §II) |
| 04 | Creative Asset Inventory | Business | Creative repository with metadata, versioning, outdoor geotag, search | Explicit (tender §II) |
| 05 | Proof-of-Display Capture & Verification | Business | PoD capture, batch upload, validation, verification workflow, third-party provision | Explicit (tender §II) |
| 06 | Mobile Field Application | Business | Field tasks, mobile PoD, offline queue, sync/conflict, secure session | Explicit (tender §II) |
| 07 | Reporting & Analytics | Business | KPI dashboards, spend, compliance, audit export, schedules, role views | Explicit (tender §II) |
| 08 | Notifications & Alerts | Shared | In-app, email, optional SMS for approvals, assignments, PoD outcomes | Added for implementation (workflow support) |
| 09 | Integration Hub | Technical | Secure REST APIs, DIPR connectors, third-party analytics, reconciliation | Explicit (tender §II) |
| 10 | Platform Security & Compliance Controls | Technical | Encryption, retention, OWASP hardening, WCAG/multilingual, VAPT remediation | Explicit (tender §II Security & Compliance) |

---

## Module Details

### 01. User & Access Management

- **Type:** Shared
- **Slug:** `user-access-management`
- **Summary:** Authenticate users and enforce RBAC across web, mobile, and APIs with optional SSO, MFA, and access audit trails.
- **Source:** Explicit in tender Section II — User & Access Management; SOW §6.01 / §8.
- **In Scope:** User lifecycle; role & permission matrix; optional SSO; MFA; access audit trail.
- **Out of Scope:** Citizen/public self-registration portal; full enterprise IAM product replacement beyond AMT needs.
- **Key Actors:** DIPR Administrator; all authenticated roles.
- **Dependencies:** None (foundational). Consumed by all modules.
- **Notes:** Access model is User → Role → Permissions. District/org scoping only if DIPR confirms later.

### 02. Master Data & System Configuration

- **Type:** Business
- **Slug:** `master-data-system-configuration`
- **Summary:** Controlled reference data and parameters for campaigns, assets, PoD, notifications, and reporting.
- **Source:** Derived from SOW (required to operate explicit modules).
- **In Scope:** Media/campaign masters; vendor/agency master; location/geography; notification templates & parameters; master search/filter/audit.
- **Out of Scope:** Free-form CMS content management; GIS base-map product.
- **Key Actors:** DIPR Administrator; Campaign Officer (read).
- **Dependencies:** 01 User & Access Management.
- **Notes:** GPS accuracy thresholds and retention parameters are configuration once DIPR finalizes rules.

### 03. Campaign Management

- **Type:** Business
- **Slug:** `campaign-management`
- **Summary:** End-to-end campaign lifecycle for print, digital, and outdoor including embedded approvals and vendor assignment.
- **Source:** Explicit — Campaign Management.
- **In Scope:** Create/maintain; approval workflow; scheduling; budget/spend; vendor assignment; version control; campaign–PoD linkage.
- **Out of Scope:** Media buying / creative production agency work; payment gateway for media invoices (unless later added).
- **Key Actors:** Campaign Officer; Approver/Manager; Vendor User (optional); Administrator.
- **Dependencies:** 01, 02; links to 04, 05, 08.
- **Notes:** Approval workflow and campaign documents are **embedded** (not separate Workflow/DMS modules).

### 04. Creative Asset Inventory

- **Type:** Business
- **Slug:** `creative-asset-inventory`
- **Summary:** Central creative/outdoor asset repository with metadata, versions, geotags, and role-based preview.
- **Source:** Explicit — Asset Inventory.
- **In Scope:** Upload & metadata; versioning; outdoor geotagging; search/filter; access & preview with logging.
- **Out of Scope:** Full digital asset management (DAM) for non-advertisement enterprise content.
- **Key Actors:** Asset Manager; Campaign Officer; Viewer roles.
- **Dependencies:** 01, 02, 03.
- **Notes:** File storage is embedded here; no separate File Store module.

### 05. Proof-of-Display Capture & Verification

- **Type:** Business
- **Slug:** `proof-of-display-verification`
- **Summary:** Capture and verify PoD evidence with metadata, batch handling, validation rules, and optional third-party verification.
- **Source:** Explicit — Proof-of-Display (PoD).
- **In Scope:** Capture & metadata stamp; batch upload; manual verification; validation rules engine; third-party provision; evidence register.
- **Out of Scope:** Physical media installation labour; unnamed third-party license purchase.
- **Key Actors:** Field Personnel (via 06); PoD Verifier; Campaign Officer; Auditor.
- **Dependencies:** 01, 02, 03, 04; mobile capture via 06; notifications via 08; third-party via 09.
- **Notes:** Tamper detection / GPS rules parameterized after DIPR Phase 1 clarification.

### 06. Mobile Field Application

- **Type:** Business
- **Slug:** `mobile-field-application`
- **Summary:** Secure field mobile experience for tasks, checklists, PoD capture, offline queue, and sync.
- **Source:** Explicit — Mobile Application.
- **In Scope:** Task/checklist inbox; mobile PoD capture; offline queue; sync & conflict resolution; secure session.
- **Out of Scope:** Separate public-facing citizen app; full native dual-codebase if PWA accepted (assumption).
- **Key Actors:** Field Personnel; Verifier (outcomes); Administrator (device policy).
- **Dependencies:** 01, 03, 05, 08.
- **Notes:** Estimate assumes cross-platform/PWA-capable app unless DIPR mandates separate native stacks.

### 07. Reporting & Analytics

- **Type:** Business
- **Slug:** `reporting-analytics`
- **Summary:** Role-based KPI dashboards, spend and compliance reports, audit exports, and scheduled PDF/CSV delivery.
- **Source:** Explicit — Reporting & Analytics.
- **In Scope:** Campaign KPI dashboards; channel-wise spend; compliance/PoD reports; audit export; scheduled exports; role-based views.
- **Out of Scope:** External BI platform licensing; ad-hoc SQL access for end users.
- **Key Actors:** Managers; Auditor/Viewer; Administrator.
- **Dependencies:** 01, 03, 04, 05; optional analytics via 09.
- **Notes:** KPI dictionary finalized in Phase 1 with DIPR.

### 08. Notifications & Alerts

- **Type:** Shared
- **Slug:** `notifications-alerts`
- **Summary:** In-app, email, and optional SMS alerts for workflow and operational events.
- **Source:** Added for implementation (approvals, assignments, PoD outcomes require alerts).
- **In Scope:** In-app centre; email dispatch; SMS provision; preferences & delivery log.
- **Out of Scope:** Marketing blast campaigns; WhatsApp unless later added.
- **Key Actors:** All operational roles (recipients); Administrator (templates via 02).
- **Dependencies:** 01, 02; triggered by 03, 05, 06.
- **Notes:** SMS optional pending gateway credentials from DIPR.

### 09. Integration Hub

- **Type:** Technical
- **Slug:** `integration-hub`
- **Summary:** Secure REST APIs and connectors for DIPR systems, third-party analytics, and verification services.
- **Source:** Explicit — APIs & Integrations.
- **In Scope:** API gateway; DIPR connectors; third-party analytics provision; auth/failure/reconciliation.
- **Out of Scope:** Building or hosting third-party vendor products; inventing DIPR APIs not provided.
- **Key Actors:** Administrator; integration support; external systems.
- **Dependencies:** 01; data from 02–07 as exposed.
- **Notes:** DIPR system list is an open pre-bid item — connectors sized as configurable capacity.

### 10. Platform Security & Compliance Controls

- **Type:** Technical
- **Slug:** `platform-security-compliance`
- **Summary:** Cross-cutting encryption, retention, OWASP hardening, accessibility/multilingual framework, and VAPT remediation support.
- **Source:** Explicit — Security & Compliance; WCAG; multilingual; data sovereignty.
- **In Scope:** Encryption & secure storage; retention/archival; OWASP/Government guideline controls; WCAG & multilingual framework; VAPT remediation support.
- **Out of Scope:** CERT-In empaneled audit fees if DIPR separately procures auditor (unless contract assigns to bidder); physical SOC staffing.
- **Key Actors:** Administrator; security reviewer; all modules consume controls.
- **Dependencies:** Cross-cutting; coordinates with 01 and deployment.
- **Notes:** Exact Government guideline names pending DIPR; OWASP + encryption baseline assumed.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
| ---------- | --------- |
| Document management | Embedded in Campaign, Asset, and PoD processes |
| Workflow / approval engine | Embedded in Campaign Management and PoD verification |
| Testing & QA | Delivery process / deliverables — not a software module |
| Documentation & Training | Engagement deliverables — not a software module |
| File storage / media blob store | Embedded under Asset Inventory and PoD |
| Job scheduler for reports | Embedded under Reporting & Analytics (scheduled reports) |
| Audit logging (access) | Feature under Module 01; operational audit export under 07; platform controls under 10 |
| Hosting / infrastructure | Deployment dependency; not a functional module |

---

## Assumptions

1. Module numbers and names match `SoW_AMT_Detailed.md` Appendix A — do not renumber without user request.
2. Notifications module added though not named separately in tender Section II list.
3. Master Data module added as implementation necessity.
4. Security & Compliance kept as a technical module because tender lists it as a distinct deliverable stream (encryption, retention, OWASP, accessibility).
5. Mobile estimated as one field application module (PWA/cross-platform assumption).
6. Open pre-bid items do not create extra modules; they widen Assumptions inside existing modules.

---

## Risks

1. **Unknown DIPR integrations** may expand Module 09 beyond provisional connector effort.
2. **Native dual-app mandate** (if issued) would expand Module 06 significantly.
3. **Third-party PoD verification** licensing/API delays block F05-005 / related integration.
4. **Unclear PoD validation / tamper rules** may increase Module 05 complexity after Phase 1.
5. **Government hosting constraints** may affect deployment timeline (Phases 4–5) more than module scope.
6. **KPI dictionary delay** risks rework in Module 07 dashboards.
