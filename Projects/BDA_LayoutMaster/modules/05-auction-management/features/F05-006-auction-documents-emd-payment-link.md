# F05-006 — Auction Documents, EMD & Payment Link
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F05-006 |
| **Feature Name** | Auction Documents, EMD & Payment Link |
| **Module** | 05 — Auction Management |
### Description
Maintain embedded auction documents and record/link EMD and balance-due payment references for auction cases.
### Business Objective
Keep auction evidence and payment status visible without implementing the payment gateway in this module.
### Actors
Auction Section; Accounts user; participant; Auditor.
### User Journey
Officer uploads notices/proceedings/challans, records or receives payment reference/status, and reviews payment linkage in the case.
### Functional Capabilities
Typed auction attachments, payment/EMD reference recording, status display, reconciliation reference, audit.
### Inputs
Case, document type/file, EMD/payment reference, amount/status, remarks.
### Outputs
Embedded document set and payment-link status.
### Business Rules
Payment execution is Module 12; this feature records business linkage only and does not implement accounting/GL.
### Validations
Valid case/type; required reference/status; authorised update.
### Calculations
No financial engine; amounts/status are recorded or received from the hub.
### Workflow
Attach evidence and record/link payment status during auction lifecycle.
### Search Requirements
Case, document type, payment reference, status.
### Documents
Notices, proceedings, bid sheets, winner confirmation, challans, GOs/approvals.
### Reports
Auction document/payment-link register.
### Notifications
Payment-status notification where enabled.
### Security
Document ACL, payment-reference access control, audit.
### Integrations
Payment hub consumption stub (Easy); internal document storage (Simple).
### Dependencies
F02-003, F05-002–005, Module 12, Module 11.
### Assumptions
Gateway authentication, callbacks, reconciliation, and execution are Module 12 scope.
### Risks
Conditional payment-gateway inclusion depends on RFP commercial scope.
### Non Functional Requirements
Secure references, auditable attachments, status visibility.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Document/payment-link register | UI | Complex | 8 |
| Upload and payment-reference editor | UI | Complex | 8 |
| Document/payment-link operations | API | Complex | 8 |
| Attachment/payment-link persistence | Database | Complex | 6 |
| Payment hub consumption stub | Integration | Easy | 8 |
| Document/payment-link tests | Testing | Very High | 12 |
| Payment-link guide | Documentation | Medium | 3 |
| **Total** | | | **53** |
### Estimation Assumptions
Payment gateway implementation is explicitly deferred to Module 12.
