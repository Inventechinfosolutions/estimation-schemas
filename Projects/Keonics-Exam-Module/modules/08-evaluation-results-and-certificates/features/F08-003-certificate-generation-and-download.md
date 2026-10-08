# F08-003 — Certificate Generation and Download

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-003 |
| **Feature Name** | Certificate Generation and Download |
| **Module** | 08 — Evaluation, Results and Certificates |

### Description
Issue certificates only for eligible/pass candidates (per examination and publication rules), assign unique certificate numbers, render certificate content, allow candidate portal download, maintain issue/cancellation status, and support administrator issue console and eligibility register.

### Business Objective
Provide authentic, downloadable certificates to successful candidates while preventing issue to ineligible candidates.

### Actors
- Examination Administrator (issue, cancel/revoke)
- Candidate (download from portal)
- Auditor (issue and cancellation history)
- Public verifier uses F08-004, not this download UI

### User Journey
1. Who creates: Examination Administrators create certificate issues for eligible candidates (individually or batch); the system may auto-queue eligibles after publish if configured. Each issue creates a certificate record with unique number.
2. How they create: Eligibility register → select candidates → preview certificate → issue → candidate downloads from portal. Cancellation/revocation sets status and blocks download/verification accordingly.
3. How they edit: Certificate content fields are driven from master data and results — not free-text edited per candidate. Status changes (issue → cancelled/revoked) are the allowed edits; re-issue may create a new number under policy.
4. How they send for approval: Issue is an administrator operational action in the current SOW, not a multi-level approval package. Cancellation requires reason and is attributable.
5. How the approver sees pending items: No Department approver inbox. Eligibility register and issue console are the administrator worklists.
6. How the approver decides: No separate checker; administrator decides issue/cancel within role. Ineligible candidates never receive a certificate (system rule).
7. How the applicant / maker sees history: Candidates see issued certificates available for download and cancelled status if applicable. Administrators see issue history.
8. How the approver / auditor sees history: Auditors view certificate number, candidate/examination references, issue date, status, cancellation reason and actor.

### Functional Capabilities
- Evaluate certificate eligibility (pass + published + other approved rules)
- Generate unique certificate number and certificate record
- Render certificate document for preview and download
- Candidate portal download of issued certificates
- Maintain certificate number, candidate and examination references, dates, result status, issue date, certificate status, verification token link point
- Cancellation/revocation when required by Department
- Block download for cancelled/revoked or never-issued
- Administrator eligibility register and issue console
- Issue history search

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Certificate eligibility register | Medium |
| Certificate issue console | Complex |
| Certificate preview | Complex |
| Candidate certificate download | Medium |
| Certificate status and cancellation list | Medium |
| Certificate issue history | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Evaluate certificate eligibility | Complex |
| Generate certificate number and record | Complex |
| Render certificate document | Very High |
| Issue certificate to candidate | Complex |
| Download certificate for candidate | Medium |
| Cancel or revoke certificate | Complex |
| Search certificate register | Medium |
| Load certificate status for portal | Easy |

### Inputs
Published pass result, candidate and examination references, issue action, cancellation reason, download request by authenticated candidate.

### Outputs
Certificate record, rendered certificate file, download entitlement, cancellation status, history entries; token/QR creation handoff to F08-004.

### Business Rules
- Ineligible candidates do not receive a certificate.
- Unique certificate number per issued certificate.
- Download only for owning candidate’s issued, non-cancelled certificate.
- Cancellation/revocation immediately blocks download and drives verification status in F08-004.
- Certificate status values include at least issued and cancelled/revoked when cancellation is enabled.

### Validations
- Eligibility checks before issue
- Unique certificate number allocation
- Cancel requires reason
- Portal download ownership enforced

### Calculations
None beyond eligibility boolean from pass/publication rules.

### Workflow
Eligible → preview → issue → download available. Cancel → status cancelled → download blocked → verification reflects cancelled.

### Search Requirements
By certificate number, registration, examination, issue date, status.

### Documents
Certificate PDF (or approved format) for preview and download.

### Reports
Certificate generation status feeds Module 09 dashboard and certificate reports.

### Notifications
Certificate-ready notifications via F09-003.

### Security
Portal ownership isolation; admin issue/cancel attributable; template/access controlled.

### Integrations
None (document render is internal). QR/public verification is F08-004.

### Dependencies
F08-001, F08-002; Module 02 portal; F08-004 for QR/token binding.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Certificate render API is Very High (layout, numbering, secure file generation).
- Generative AI certificate content is out of scope.

### Risks
Issuing before result finalisation — mitigated by eligibility on published pass.
Template legal wording changes requiring re-issue policy.

### Non Functional Requirements
Download available under post-result concurrency; certificate numbers unique under concurrent issue batches.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Certificate eligibility register | UI | Medium | 6 |
| Certificate issue console | UI | Complex | 12 |
| Certificate preview | UI | Complex | 12 |
| Candidate certificate download | UI | Medium | 6 |
| Certificate status and cancellation list | UI | Medium | 6 |
| Certificate issue history | UI | Easy | 4 |
| Evaluate certificate eligibility | API | Complex | 8 |
| Generate certificate number and record | API | Complex | 8 |
| Render certificate document | API | Very High | 16 |
| Issue certificate to candidate | API | Complex | 8 |
| Download certificate for candidate | API | Medium | 6 |
| Cancel or revoke certificate | API | Complex | 8 |
| Search certificate register | API | Medium | 6 |
| Load certificate status for portal | API | Easy | 4 |
| Certificate master entities | DB | Complex | 6 |
| Certificate generation and download tests | Testing | Complex | 8 |
| Certificate generation and download implementation documentation | Documentation | Medium | 3 |

**Feature total: 127 hours**
