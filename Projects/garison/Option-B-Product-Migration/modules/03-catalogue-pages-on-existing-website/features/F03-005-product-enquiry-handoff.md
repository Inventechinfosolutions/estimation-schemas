# F03-005 — Product Enquiry Handoff

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-005 |
| Feature Name | Product Enquiry Handoff |
| Module | 03 — Catalogue Pages on Existing Website |
| Module Type | Business |
| Release | Go-live |

### Description
Request Information action that opens the existing Garrison contact form (or email) with the product code, category, dimensions and page link pre-filled, so enquiries reach Garrison with product context.

### Business Objective
Turn product views into enquiries using Garrison's existing contact channel.

### Actors
- Visitor
- Garrison staff (recipients)

### User Journey
1. **Who creates:** Visitors create enquiries.
2. **How they create:** From a product page the visitor clicks Request Information; the existing form opens with product details pre-filled.
3. **How they edit:** The visitor can edit the message before sending.
4. **How they send for approval:** No approval applies; the existing form sends the enquiry as it does today.
5. **How the approver sees pending items:** Garrison staff receive enquiries in their existing mailbox; no new inbox.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Visitors receive whatever confirmation the existing form provides.
8. **How the approver / auditor sees history:** Garrison sees enquiries in its existing email records.

### Functional Capabilities
- Product context pre-fill
- Fallback mailto link with subject and body
- Confirmation via existing form behaviour

### UI Screens
- Pre-filled enquiry form integration
- Enquiry confirmation

### Logical API Operations
- Pass product context to existing form handler

### Inputs
- Product context
- Visitor message and contact details

### Outputs
- Enquiry email to Garrison including product details

### Business Rules
- Product code and link always included

### Validations
- Existing form validation applies

### Calculations
- None

### Workflow
Product page → Pre-filled form → Sent

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- Existing form email

### Security
- Existing form spam protection reused; product parameters escaped

### Integrations
- Existing contact form / email

### Dependencies
- F03-003
- F04-001

### Assumptions
- Existing site has a working contact form

### Risks
- If no working form exists, a simple form is needed (small change request)

### Non Functional Requirements
- No change to existing form performance

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Pre-filled enquiry form integration | Medium | 6 |
| UI | Enquiry confirmation | Simple | 2 |
| API | Pass product context to existing form handler | Medium | 6 |
| Integration | Existing website contact form and email handler | Simple | 4 |
| Testing | Enquiry delivery with product context | Easy | 4 |
| Documentation | Enquiry handoff note | Simple | 1 |

**Feature Total: 23 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 6 | 0 | 4 | 4 | 1 | **23** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Reuses existing form; no new enquiry storage
