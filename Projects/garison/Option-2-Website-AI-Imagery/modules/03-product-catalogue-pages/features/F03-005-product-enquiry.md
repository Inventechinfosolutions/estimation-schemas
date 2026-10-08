# F03-005 — Product Enquiry

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-005 |
| Feature Name | Product Enquiry |
| Module | 03 — Product Catalogue Pages |
| Module Type | Business |
| Release | Go-live |

### Description
Request Information action on product pages that opens the enquiry form (F02-004) with the product code, category, dimensions and page link pre-filled, so enquiries reach Garrison with product context.

### Business Objective
Convert product views into enquiries that name the product.

### Actors
- Visitor
- Garrison staff (recipients)

### User Journey
1. **Who creates:** Visitors create product enquiries.
2. **How they create:** From a product page the visitor clicks Request Information; the form opens pre-filled.
3. **How they edit:** The visitor can edit the message before sending.
4. **How they send for approval:** No approval applies; the enquiry is emailed to Garrison.
5. **How the approver sees pending items:** Garrison staff see enquiries in their existing mailbox.
6. **How the approver decides:** Garrison staff reply by email; no in-system decision.
7. **How the maker sees history:** Visitors receive the acknowledgement email.
8. **How the approver / auditor sees history:** Garrison keeps enquiries in its mailbox.

### Functional Capabilities
- Product context pre-fill
- Product details included in email
- Return link to product

### UI Screens
- Request Information button
- Pre-filled enquiry form state

### Logical API Operations
- Pass product context to enquiry handler

### Inputs
- Product context
- Visitor details and message

### Outputs
- Enquiry email including product code, dimensions and link

### Business Rules
- Product code and link always included

### Validations
- Same validation as F02-004

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
- Enquiry email and acknowledgement (F02-004)

### Security
- Product parameters escaped

### Integrations
- None

### Dependencies
- F02-004
- F03-003

### Assumptions
- Single enquiry form serves general and product enquiries

### Risks
- None significant

### Non Functional Requirements
- No extra page load

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Request Information button | Simple | 2 |
| UI | Pre-filled enquiry form state | Medium | 6 |
| API | Pass product context to enquiry handler | Easy | 4 |
| Testing | Product enquiry delivery with context | Easy | 4 |
| Documentation | Product enquiry note | Simple | 1 |

**Feature Total: 17 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4 | 0 | 0 | 4 | 1 | **17** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Reuses F02-004 handler
- No external integration channel in this feature; Integration row omitted.
