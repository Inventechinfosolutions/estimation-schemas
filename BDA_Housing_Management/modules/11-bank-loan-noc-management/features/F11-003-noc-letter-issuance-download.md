# F11-003 — NOC Letter Issuance & Download

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F11-003 |
| **Feature Name** | NOC Letter Issuance & Download |
| **Module** | 11 — Bank / Loan NOC Management |

### Description
Generate, issue, retrieve, and authorize download of a bank/loan NOC from the approved NOC case using the BDA-configured letter template.
### Business Objective
Provide a controlled official NOC artefact to the eligible citizen and BDA officers after approval.
### Actors
- NOC Desk officer, authorized signatory, Citizen
### User Journey
1. NOC Desk opens an approved case and checks the generated letter particulars.
2. An authorized officer issues the NOC.
3. BHMS records the issuance and makes the issued copy available to permitted users.
### Functional Capabilities
- Template-based NOC preparation; review; issue control; numbered issued copy; citizen/officer download; issuance history.
### Inputs
- Approved NOC case, configured NOC template, signatory/issue details.
### Outputs
- Issued NOC document, issue reference/date, download availability, and history record.
### Business Rules
- Issuance is allowed only for an approved, non-withdrawn case.
- Only the issued version is available for citizen download.
### Validations
- Approved status, complete required particulars, authorized issuer, and configured template availability.
### Calculations
- None.
### Workflow
- Approved → Prepared → Issued → Downloaded/Archived.
### Search Requirements
- Search by NOC number, issue date, applicant, bank, project, and issuance status.
### Documents
- Generated NOC letter and its source approved request evidence.
### Reports
- Issued-NOC register and download history.
### Notifications
- Issuance and download-availability alerts through Module 12.
### Security
- Controlled issue permission, citizen ownership isolation, watermarked/traceable downloads where configured.
### Integrations
- Internal template and document capabilities.
### Dependencies
- Modules 01–02 and 12; F11-002 and F11-004.
### Assumptions
- BDA provides the approved NOC template and signatory content before UAT.
### Risks
- Late legal/template changes can affect issued-letter acceptance.
### Non Functional Requirements
- Reliable document generation, authorized retrieval, and durable issuance history.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| NOC letter review, issuance, and download UI | UI | Complex | 8 |
| Letter generation and issue-control operations | API | Complex | 8 |
| Issuance and document-version state | Database | Medium | 4 |
| NOC letter issuance tests | Testing | Complex | 8 |
| NOC issuance guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- The provided template is maintained through Module 02; no independent legal-document authoring product is included.
