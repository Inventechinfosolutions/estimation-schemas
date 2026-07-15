# F04-001 — Tenant Registration & KYC Profile

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F04-001 |
| **Feature Name** | Tenant Registration & KYC Profile |
| **Module** | 04 — Tenant & Lease Lifecycle |

### Description
Register and maintain tenants of types Individual, Partnership, Company, Trust, and Society with identity, tax, contact, bank, and KYC document details, including configurable duplicate detection on PAN/GSTIN/Aadhaar.

### Business Objective
Create a reliable tenant master for allotment, leasing, billing, and portal access with adequate KYC for government compliance.

### Actors
- Estate Officer, Property Manager, Data Entry Operator
- Accounts Officer (bank/GST fields)
- Auditor (read-only)

### User Journey
1. Officer opens Tenant Register → Create Tenant.
2. Selects tenant type and captures profile, IDs, contacts, business type, emergency contact, bank details.
3. Uploads/links KYC documents.
4. System runs duplicate check; officer confirms/overrides with reason if allowed.
5. Saves tenant; optionally triggers portal credential issuance (F01-008).

### Functional Capabilities
- CRUD for all SOW tenant types
- Fields: Tenant ID, Aadhaar/PAN, GSTIN, contacts, business type, emergency contact, bank details
- KYC document linkage (Module 08)
- Configurable duplicate detection on PAN/GSTIN/Aadhaar
- Activate/deactivate tenant for new leases
- Search, filter, Excel export
- Mask Aadhaar/PAN in UI per role

### Inputs
- Tenant type and profile attributes, ID numbers, KYC files/refs

### Outputs
- Tenant master record
- Duplicate match warnings
- Tenant register export

### Business Rules
- Tenant ID system-generated (plus optional BDA reference).
- Duplicate detection configurable (block vs warn).
- Lease activation requires required KYC complete (M3-AC1) — enforced with F04-003.
- Portal credentials are F01-008; this feature only links tenant identity.
- Aadhaar eKYC / DigiLocker automation out of scope (optional Module 10).

### Validations
- Type-specific mandatory fields
- PAN/GSTIN/Aadhaar format checks
- Unique Tenant ID; soft uniqueness on ID numbers per config

### Calculations
None.

### Workflow
Optional maker-checker for tenant create (F02-009). Baseline: direct save with audit.

### Search Requirements
By name, Tenant ID, PAN/GSTIN, mobile, type, status; duplicate candidate search.

### Documents
KYC set via Module 08.

### Reports
Tenant Register (Excel).

### Notifications
Optional notify on tenant activation.

### Security
RBAC; PII masking; audit; document ACL.

### Integrations
Internal DMS (Simple). Optional eKYC later in Module 10.

### Dependencies
Modules 01–02, 08; F01-008 for portal users.

### Assumptions
- Manual KYC upload baseline; no DigiLocker in this estimate.
- Very High UI for multi-type tabbed profile.

### Risks
- Poor ID data quality causes false duplicate matches.
- PII handling must meet security policy.

### Non Functional Requirements
- Responsive admin UI; Excel export; PII masking

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Tenant register list + search | UI | Complex | 8 |
| Tenant create/edit (multi-type, KYC tabs) | UI | Very High | 16 |
| Duplicate match review dialog | UI | Medium | 6 |
| Tenant CRUD + search + duplicate check | API | Complex | 8 |
| Tenant & KYC entities | Database | Complex | 6 |
| DMS KYC handoff (internal) | Integration | Simple | 4 |
| Tenant registration tests | Testing | Very High | 12 |
| Tenant registration guide | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Duplicate detection included here (not a separate feature).
- DigiLocker/eKYC connectors excluded.
