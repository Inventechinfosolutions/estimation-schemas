# F05-002 — Hosting, Domain, SSL & DNS Cutover

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-002 |
| Feature Name | Hosting, Domain, SSL & DNS Cutover |
| Module | 05 — Hosting, SEO & Launch |
| Module Type | Shared |
| Release | Go-live |

### Description
Provision staging and production hosting for the new static site and form handler, set up automated build and deployment, install SSL with automatic renewal, and switch the garrisonindustries.ky DNS to the new site while keeping the existing Google Workspace email (MX, SPF, DKIM, DMARC) records unchanged.

### Business Objective
Launch the new website securely on Garrison's domain without disrupting company email.

### Actors
- Delivery developer
- Garrison domain/registrar contact

### User Journey
1. **Who creates:** The delivery developer prepares hosting and the cutover plan with Garrison's domain contact.
2. **How they create:** They provision hosting, configure deployment and SSL, and document the DNS changes.
3. **How they edit:** The plan is revised if registrar or email settings differ from expectations.
4. **How they send for approval:** The cutover plan is emailed to Garrison for approval of the cutover window.
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's approval email confirms the cutover window.
7. **How the maker sees history:** Garrison receives the hosting and DNS runbook.
8. **How the approver / auditor sees history:** The delivery lead keeps the DNS before/after record and runbook.

### Functional Capabilities
- Staging and production hosting
- Automated build and deployment
- SSL with auto-renewal
- DNS cutover plan and execution
- Email record preservation and verification
- Rollback by reverting DNS

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Automated build and deployment

### Inputs
- Registrar/DNS access
- Hosting account

### Outputs
- Live site on garrisonindustries.ky with valid SSL
- Runbook

### Business Rules
- MX and email authentication records copied exactly before cutover
- Old server kept running until the new site is verified

### Validations
- SSL valid on www and apex domains
- Test email delivered after cutover

### Calculations
- None

### Workflow
Provision → Staging → Cutover plan approved → DNS switch → Verify

### Search Requirements
- None

### Documents
- Runbook

### Reports
- None

### Notifications
- None

### Security
- HTTPS everywhere with HSTS
- Access credentials handed over at the end

### Integrations
- Hosting provider
- Domain registrar / DNS

### Dependencies
- Garrison provides domain/DNS access

### Assumptions
- Hosting fees are paid by Garrison (static hosting is low cost)
- The current site's SSL certificate did not validate during our review; the new site replaces it

### Risks
- Registrar access unavailable; Garrison must recover it before cutover

### Non Functional Requirements
- Cutover downtime under 15 minutes; DNS propagation monitored

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Automated build and deployment | Medium | 6 |
| Integration | Hosting environment provisioning (staging and production) | Medium | 16 |
| Integration | Domain DNS cutover preserving Google Workspace email records | Easy | 8 |
| Integration | SSL certificate setup and auto-renewal | Simple | 4 |
| Testing | Pre- and post-cutover website and email checks | Easy | 4 |
| Documentation | Hosting and DNS runbook | Medium | 3 |

**Feature Total: 41 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 0 | 28 | 4 | 3 | **41** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Infrastructure tasks sized on the Integration scale
