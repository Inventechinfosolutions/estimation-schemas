# F08-003 — Document Category Access Control

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F08-003 |
| **Feature Name** | Document Category Access Control |
| **Module** | 08 — Document Management |

### Description
Enforce role-based access so unauthorized roles cannot download (or preview) restricted document categories (M7-AC2), including tenant self-scope for own documents.

### Business Objective
Protect PII, KYC, legal, and financial artefacts per least privilege.

### Actors
- Super Administrator (ACL config)
- All roles as subjects
- Auditor (typically broad read)

### User Journey
1. Admin maps document categories to view/download permissions by role.
2. User attempts preview/download.
3. System allows or denies; denial logged.

### Functional Capabilities
- Category permission matrix (View / Download / Upload / Delete)
- Integrate with Module 01 roles
- Tenant scope: only documents linked to own tenant/leases
- Officer scope: property data scope intersection
- Access denial UX and audit of denied attempts

### Inputs
- Category–role permission grants

### Outputs
- Allow/deny decisions; audit events

### Business Rules
- Unauthorized roles cannot download restricted categories (M7-AC2).
- Server-side enforcement mandatory (UI hide insufficient).
- Legal/KYC categories default restricted.

### Validations
- Role and category exist
- Cannot strip Super Admin from ACL admin capability

### Calculations
None.

### Workflow
Optional dual control for ACL matrix changes.

### Search Requirements
Admin search ACL by category/role.

### Documents
ACL matrix export for sign-off.

### Reports
Denied access report (security).

### Notifications
Optional alert on repeated denials.

### Security
Core of DMS trust model; full audit of ACL changes and denials.

### Integrations
None (Module 01 role catalog).

### Dependencies
F01-005; F08-001/002

### Assumptions
- Testing Very High: role × category × scope matrix.
- Complements module permissions—document ACL is category-specific.

### Risks
- Over-permissive defaults — ship least privilege baseline.

### Non Functional Requirements
- ACL evaluation overhead negligible on download path

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Category ACL configuration UI | UI | Complex | 8 |
| Access denied / restricted UX | UI | Simple | 2 |
| ACL evaluate & enforce ops | API | Complex | 8 |
| Category permission entities | Database | Medium | 4 |
| Document ACL tests | Testing | Very High | 12 |
| Document access control guide | Documentation | Medium | 3 |
| **Total** | | | **37** |

### Estimation Assumptions
- Property scope from Module 01 applied in evaluate API.
