# F06-006 — Possession & Handover
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F06-006 |
| **Feature Name** | Possession & Handover |
| **Module** | 06 — Allotment Management |
### Description
Record possession of an accepted allotment, including handover date, condition notes, certificate, and resulting site status.
### Business Objective
Close the allotment journey with a factual, retrievable record of site handover.
### Actors
Revenue/Allotment Officer; field/section officer; Allottee; Auditor.
### User Journey
Officer opens an accepted order, schedules or records the handover, captures possession date and condition remarks, uploads the signed certificate, confirms completion, and the site status changes to possessed/allotted.
### Functional Capabilities
- Possession-pending worklist, handover form, condition-note panel, certificate upload/view, and possession register.
- Link possession to a single accepted allotment and retain corrections through audit.
### Inputs
Accepted order, site, possession date, condition notes, attendees, and signed possession certificate.
### Outputs
Possession record, certificate, updated site/allotment status, and register export.
### Business Rules
Possession is recorded only for an accepted active order; one current possession record per allotment; cancellation/surrender handling occurs in F06-007.
### Validations
Order acceptance, required possession date, certificate where configured, and no duplicate completed handover.
### Calculations
Days between order acceptance and possession; possession count by scheme.
### Workflow
Accepted → possession pending → handover recorded → possession complete.
### Search Requirements
Order reference, site, allottee, possession date, scheme, and completion status.
### Documents
Possession certificate, site condition note, and handover correspondence.
### Reports
Possession register and pending-handover aging.
### Notifications
Handover completion acknowledgement through Module 11.
### Security
Allotment role and site scope; certificates restricted to authorised staff and allottee.
### Integrations
Internal site-status reflection (Simple).
### Dependencies
F06-005, Module 04 site master, Module 11.
### Assumptions
Field inspection scheduling is not a separate feature.
### Risks
Missing signed certificates may delay completion or create disputes.
### Non Functional Requirements
Responsive field-reference UI, auditable completion, secure document retrieval.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Possession-pending register | UI | Complex | 8 |
| Handover and condition recording form | UI | Complex | 8 |
| Certificate view and completion screen | UI | Medium | 6 |
| Possession validation and status processing | API | Complex | 8 |
| Possession record persistence | Database | Medium | 4 |
| Site-status reflection | Integration | Simple | 4 |
| Possession tests | Testing | Complex | 8 |
| Possession guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
The certificate is uploaded as a BDA-supplied digital file; physical scanning is outside scope.
