# F13-003 — DSC & e-Sign Signing Service

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F13-003 |
| Feature Name | DSC & e-Sign Signing Service |
| Module | 13 — Integration Hub |
| Module Type | Technical |
| Release | Go-live |

### Description
Shared signing service for intimation letters, approvals, proceedings, notices, orders, draft sale deeds and completion records: PDF signing with officer DSC via signer utility (and Aadhaar e-Sign through an ESP where BDA opts), bulk signing, signature verification, signed hash storage and verification page.

### Business Objective
Provide legally valid digital signatures consistently across the Module.

### Actors
- Approving Authority
- Deputy Secretary
- System

### User Journey
1. **Who creates:** Signing requests are created by business features.
2. **How they create:** The officer clicks Sign; the signer utility signs the document hash with the token.
3. **How they edit:** Not editable after signing.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Officers see pending signatures in the relevant queues.
6. **How the approver decides:** Officers sign or return.
7. **How the applicant / maker sees history:** Users see signature details on documents.
8. **How the approver / auditor sees history:** Auditors verify signatures.

### Functional Capabilities
- PDF signing (PAdES)
- Signer utility for USB tokens
- Optional e-Sign through ESP
- Bulk signing
- Signature verification
- Signed hash storage

### UI Screens
- Signing dialog
- Bulk signing progress
- Signature verification page

### Logical API Operations
- Prepare document hash
- Apply signature to PDF
- Bulk signing orchestration
- Verify signature
- Store signed hash

### Inputs
- Documents
- Token signature

### Outputs
- Signed PDFs

### Business Rules
- Pre-sign authority check (F01-004)

### Validations
- Certificate valid

### Calculations
- SHA-256 hash

### Workflow
Prepared → Signed → Verified

### Search Requirements
- Signatures by document

### Documents
- Signed documents

### Reports
- Signing log

### Notifications
- None

### Security
- Keys never leave token

### Integrations
- Signer utility / ESP

### Dependencies
- F01-004

### Assumptions
- Officers use Windows machines with token drivers

### Risks
- Browser / driver compatibility

### Non Functional Requirements
- Single signature within 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Signing dialog | Medium | 6 |
| UI | Bulk signing progress | Easy | 4 |
| UI | Signature verification page | Easy | 4 |
| API | Prepare document hash | Medium | 6 |
| API | Apply signature to PDF | Complex | 8 |
| API | Bulk signing orchestration | Complex | 8 |
| API | Verify signature | Medium | 6 |
| API | Store signed hash | Easy | 4 |
| Database | Signature register | Easy | 2 |
| Integration | DSC signer utility / e-Sign ESP integration | Complex | 24 |
| Testing | Signing and verification tests across tokens | Complex | 8 |
| Documentation | Signing setup guide | Easy | 2 |

**Feature Total: 82 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 32 | 2 | 24 | 8 | 2 | **82** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- One Complex integration row
