# F01-004 — Officer DSC Registration & Signing Authority

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-004 |
| Feature Name | Officer DSC Registration & Signing Authority |
| Module | 01 — User, Role & Access Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Registration of the Digital Signature Certificates (DSC) of approving officers and Deputy Secretaries, verification of certificate validity and class, and configuration of signing authority defining which document types and approval levels each officer may sign.

### Business Objective
Ensure every signed approval, intimation letter and draft sale deed is signed only by an authorised officer with a valid, registered DSC.

### Actors
- Approving Authority
- Deputy Secretary
- Super Admin

### User Journey
1. **Who creates:** The officer (or the Super Admin on their behalf) registers a DSC; the Super Admin defines signing authority.
2. **How they create:** The officer opens My DSC, inserts the token, and the signer utility reads the certificate; the system verifies issuer chain, validity, class and name match and saves it as Pending Verification.
3. **How they edit:** The officer can replace an expiring certificate by registering a new one; the Super Admin edits signing authority (document types, levels, value limits).
4. **How they send for approval:** The registered DSC is submitted to the Super Admin for verification against the officer's identity.
5. **How the approver sees pending items:** The Super Admin sees pending DSC registrations with certificate details and officer profile.
6. **How the approver decides:** The Super Admin approves (DSC becomes active for signing) or rejects with reason.
7. **How the applicant / maker sees history:** The officer sees registered certificates, status, expiry and signing authority on My DSC.
8. **How the approver / auditor sees history:** The Super Admin and auditors see registration, verification, revocation and every signing event in the audit trail.

### Functional Capabilities
- Register DSC through the signer utility (Class 3 individual signing certificates)
- Certificate checks: issuer chain to a CCA-licensed CA, validity, key usage, name match with officer profile
- Super Admin verification of registered certificates
- Signing authority per officer: document types (approval, proceedings, intimation letter, notice, draft sale deed, completion record), approval levels and bid value limits
- Expiry alerts 30 and 7 days before expiry; expired certificate blocks signing
- Revocation and replacement of certificates
- Pre-sign check used by all signing actions

### UI Screens
- My DSC: register and view certificates
- DSC verification queue (Super Admin)
- Signing authority configuration per officer
- Expiring certificates list
- Certificate detail view

### Logical API Operations
- Read certificate from signer utility and validate
- Register DSC
- Verify / reject DSC registration
- Configure signing authority
- Pre-sign authority and validity check
- Revoke / replace DSC
- Expiry alert job

### Inputs
- Certificate read from token
- Document types and levels authorised
- Value limits
- Verification remarks

### Outputs
- Active certificate linked to officer
- Signing authority rules
- Expiry alerts

### Business Rules
- Only Class 3 signing certificates are accepted
- Certificate subject name must match the officer name (configurable tolerance)
- An officer may sign only document types and levels in their authority
- Expired or revoked certificates cannot sign
- Signing authority changes are audited

### Validations
- Certificate chain valid
- Not expired; not revoked where CRL / OCSP reachable
- Officer has a signing role

### Calculations
- Days to expiry = certificate valid-to − today

### Workflow
Registered → Pending Verification → Active → (expiry / revocation) Inactive

### Search Requirements
- Certificates by officer, status and expiry date

### Documents
- Certificate public details only; private keys never leave the token

### Reports
- Officer DSC status and expiry report

### Notifications
- Expiry alerts to officer and Super Admin
- Verification result to officer

### Security
- Private keys remain on the officer's token
- Only Super Admin verifies certificates

### Integrations
- Signer utility and signing service (F13-003)

### Dependencies
- F13-003
- F01-002
- F14-001

### Assumptions
- BDA procures DSC tokens for officers
- Signer utility can be installed on officer machines

### Risks
- Browser and token driver incompatibilities on officer machines

### Non Functional Requirements
- Certificate validation within 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | My DSC: register and view certificates | Medium | 6 |
| UI | DSC verification queue (Super Admin) | Easy | 4 |
| UI | Signing authority configuration per officer | Medium | 6 |
| UI | Expiring certificates list | Easy | 4 |
| UI | Certificate detail view | Simple | 2 |
| API | Read certificate from signer utility and validate | Complex | 8 |
| API | Register DSC | Medium | 6 |
| API | Verify / reject DSC registration | Easy | 4 |
| API | Configure signing authority | Medium | 6 |
| API | Pre-sign authority and validity check | Complex | 8 |
| API | Revoke / replace DSC | Easy | 4 |
| API | Expiry alert job | Easy | 4 |
| Database | Officer certificate register | Easy | 2 |
| Database | Signing authority rules | Easy | 2 |
| Integration | Signer utility interaction for certificate read (through F13-003) | Easy | 8 |
| Testing | DSC registration and validation tests (expired, wrong class, name mismatch) | Medium | 6 |
| Testing | Signing authority enforcement tests | Medium | 6 |
| Documentation | Officer DSC registration guide | Easy | 2 |
| Documentation | Signer utility installation note | Easy | 2 |

**Feature Total: 90 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 40 | 4 | 8 | 12 | 4 | **90** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Signing itself is in F13-003; this feature covers registration and authority only
