# BDAIT — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 541 hours · **Go-live:** 541 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | User Account and Access Management | Shared | 4 | 188 | 34.8% |
| 02 | Dropdown Values | Business | 1 | 16 | 3.0% |
| 03 | Asset Request Management | Business | 3 | 122 | 22.6% |
| 04 | Ticket Management | Business | 3 | 120 | 22.2% |
| 05 | Admin Dashboard | Business | 2 | 95 | 17.6% |
| | **Total** | | **13** | **541** | **100%** |

## Effort profile

| Type | Hours | % |
|------|------:|---:|
| Shared | 188 | 34.8% |
| Business | 353 | 65.2% |
| Technical | 0 | 0% |

Largest features: F01-001 (58), F05-001 (55), F01-003 (48), F03-003 (46), F01-002 (44), F04-003 (44).

## Indicative phasing

Aligned to the SOW single Phase 1, split only for build order:

| Phase | Modules |
|-------|---------|
| P1 — Access and dropdown values | 01, 02 |
| P2 — Asset requests and tickets | 03, 04 |
| P3 — Admin dashboard | 05 |

## Exclusions (not in feature hours)

- Hosting, SSL, backup operations, and BDA network access.
- Classroom training and change-management programmes.
- Email, SMS, SSO/AD, HR employee-number validation.
- IT asset inventory, stock, barcode, purchase/tender.
- Item / catalogue master (edit, deactivate, history).
- Legacy data migration.
- AMC of IT hardware.

## Optional commercial line items

None in this baseline.


## 01 — User Account and Access Management (188 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Employee and Contractor Accounts | 58 | Admin creates employees (with employee number) and contractors |
| F01-002 | Username and Password Administration | 44 | Admin-only set, reset, and change of credentials |
| F01-003 | Login and Role Session | 48 | Username/password login; User vs Admin session |
| F01-004 | Account Enable and Disable | 38 | Withdraw access without deleting history |

## 02 — Dropdown Values (16 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Create Dropdown Values | 16 | Admin adds values that appear in request and ticket dropdowns |

## 03 — Asset Request Management (122 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Raise Asset Request | 40 | User submits request using the asset-type dropdown |
| F03-002 | User Status Tracking for Asset Requests | 36 | User sees own requests and status |
| F03-003 | Admin Processing of Asset Requests | 46 | Admin remarks and status including Rejected |

## 04 — Ticket Management (120 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | Raise Ticket | 40 | User submits IT ticket using the ticket-category dropdown |
| F04-002 | User Status Tracking for Tickets | 36 | User sees own tickets and status |
| F04-003 | Admin Processing of Tickets | 44 | Admin remarks and status (Open / In progress / Closed) |

## 05 — Admin Dashboard (95 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Request and Ticket Snapshot | 55 | Admin counts and recent/open list |
| F05-002 | Dashboard Filters | 40 | Filter by type, status, and date |
