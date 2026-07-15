# F10-008 — DigiLocker Connector (Optional)

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F10-008 |
| **Feature Name** | DigiLocker Connector (Optional) |
| **Module** | 10 — API / Integration Hub |

### Description
Optional DigiLocker integration subject to BDA/legal approval for pulling/pushing issued documents related to KYC or certificates into Module 08.

### Business Objective
Reduce manual KYC document handling when digitally available.

### Actors
- Tech admin, Estate/Accounts officers, Tenant (consent UX)

### User Journey
1. User consents and authorizes DigiLocker.
2. Hub fetches allowed documents.
3. Files archived in Module 08 linked to tenant.

### Functional Capabilities
- OAuth/consent flow support
- Document fetch APIs
- Map to DMS categories
- Consent/audit trail

### Inputs
- Auth codes; document type requests

### Outputs
- Retrieved docs in DMS

### Business Rules
- Subject to approval; optional commercial line.
- Manual KYC upload remains baseline.

### Validations
- Consent valid; document type allowed

### Calculations
None.

### Workflow
Consent → Fetch → Archive.

### Search Requirements
Via DMS.

### Documents
Consent logs.

### Reports
DigiLocker fetch register.

### Notifications
Fetch success/fail to user.

### Security
Consent-first; minimize retained tokens; audit.

### Integrations
DigiLocker — **Medium (16)** Auth+Mapping+Retry.

### Dependencies
F10-001; Modules 04, 08

### Assumptions
- API specs as published; changes may revise estimate.

### Risks
- Approval delays; scope of allowed docs uncertain.

### Non Functional Requirements
- Secure redirect handling

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| DigiLocker link UX hooks config | UI | Medium | 6 |
| DigiLocker facade APIs | API | Complex | 8 |
| DigiLocker link entities | Database | Easy | 2 |
| DigiLocker integration | Integration | Medium | 16 |
| DigiLocker connector tests | Testing | Complex | 8 |
| DigiLocker guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Optional Phase 3 line item.
