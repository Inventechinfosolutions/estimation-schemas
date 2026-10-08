# F10-001 — Product Enquiry Form

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-001 |
| Feature Name | Product Enquiry Form |
| Module | 10 — Product Enquiry |
| Module Type | Business |
| Release | Go-live |

### Description
Request Information form opened from product and combination pages (product context captured automatically) and available as a general catalogue enquiry: name, email, phone (optional), company, role (Homeowner, Contractor, Architect/Designer, Dealer, Other), location, quantity/length needed (optional), message, consent; spam protection and rate limiting.

### Business Objective
Convert catalogue interest into qualified enquiries with full product context for Garrison's team.

### Actors
- Visitor

### User Journey
1. **Who creates:** Visitors create enquiries.
2. **How they create:** From a product or combination page the visitor clicks Request Information, completes the form (product pre-filled), passes spam protection and submits.
3. **How they edit:** Visitors cannot edit an enquiry after submission; they may submit another.
4. **How they send for approval:** No approval applies; submission routes the enquiry to Garrison (F10-002).
5. **How the approver sees pending items:** There is no approver inbox; Garrison staff see enquiries in the register (F10-003) and mailbox.
6. **How the approver decides:** No decision applies on this feature.
7. **How the maker sees history:** Visitors receive an acknowledgement email containing a copy of their enquiry.
8. **How the approver / auditor sees history:** Administrators see enquiries in the register; enquiry status changes are audited.

### Functional Capabilities
- Modal form on product/combination pages and standalone general enquiry page
- Automatic capture of product/combination code, name, URL and page context
- Configurable enquiry fields (required/optional) and role list
- Consent and privacy notice
- Spam protection (CAPTCHA / invisible challenge) and rate limiting
- Success confirmation

### UI Screens
- Enquiry form (modal and standalone)
- Enquiry success confirmation
- Consent and privacy notice block

### Logical API Operations
- Submit enquiry with validation and spam check
- Get enquiry form configuration

### Inputs
- Name, email, phone, company, role, location, quantity/length, message, consent, product context

### Outputs
- Enquiry record
- Routing trigger (F10-002)

### Business Rules
- Consent required to submit
- Maximum 5 enquiries per IP per hour
- Enquiries are not shown publicly

### Validations
- Name, email, message mandatory
- Email format
- Message 10–2,000 characters
- Spam check passed

### Calculations
- None

### Workflow
Submitted → Routed (F10-002) → New (F10-003)

### Search Requirements
- None

### Documents
- None (no file attachments in this phase)

### Reports
- Enquiries by product/category (F10-003, F11-004)

### Notifications
- Triggers F10-002 emails

### Security
- Minimal personal data; HTTPS; spam protection; data retention per F10-003

### Integrations
- Spam protection service (for example reCAPTCHA or Turnstile, Garrison keys)

### Dependencies
- F08-003
- F08-004
- F10-002
- F10-003
- F13-002

### Assumptions
- No file attachments on enquiries in this phase

### Risks
- Spam volume if protection is misconfigured

### Non Functional Requirements
- Submission under 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Enquiry form (modal and standalone) | Complex | 12 |
| UI | Enquiry success confirmation | Simple | 2 |
| UI | Consent and privacy notice block | Simple | 2 |
| API | Submit enquiry with validation and spam check | Complex | 8 |
| API | Get enquiry form configuration | Easy | 4 |
| Database | Enquiry record with product context | Easy | 2 |
| Integration | Spam protection service | Easy | 8 |
| Testing | Form validation and context capture | Medium | 6 |
| Testing | Spam and rate-limit protection | Medium | 6 |
| Documentation | Enquiry form configuration note | Simple | 1 |

**Feature Total: 51 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 12 | 2 | 8 | 12 | 1 | **51** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Spam protection integration estimated as Easy (REST)
