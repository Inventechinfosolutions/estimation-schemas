# F10-005 — VAPT remediation support

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F10-005 |
| Feature Name | VAPT remediation support |
| Module | 10 — Platform Security & Compliance Controls |
| Description | Remediate findings from agreed VAPT / security assessment cycles |
| Business Objective | Close or risk-accept VAPT findings within the engagement scope. |
| Actors | Security Officer; Developer; DIPR Auditor |

### User Journey

- VAPT report received → findings triaged → fixes implemented → retest → closure evidence submitted to DIPR.

### Functional Capabilities

- Finding intake and severity tracking
- Remediation tasks linked to affected modules
- Evidence capture for retest
- Risk acceptance workflow with DIPR sign-off

### Inputs

VAPT report; severity; affected component

### Outputs

Closed findings; retest evidence pack

### Business Rules

Critical/high findings prioritized within sprint capacity agreed with DIPR
No silent deferral without documented acceptance

### Validations

- N/A

### Calculations

- None

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

- None

### Dependencies

F10-003; F10-001; all modules in assessment scope

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

Out-of-scope findings or repeated assessment cycles add effort

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | VAPT finding register list | Medium | 6 |
| UI | Finding detail with severity and CVE refs | Medium | 6 |
| UI | Evidence attachment upload panel | Easy | 4 |
| API | Create/update finding status workflow | Complex | 8 |
| API | Attach remediation evidence metadata | Easy | 4 |
| API | Export finding closure pack | Medium | 6 |
| Integration | VAPT tooling import/handoff file ingest | Easy | 8 |
| Database | VAPT finding register | Simple | 1 |
| Testing | Retest pass on remediated finding | Very High | 12 |
| Testing | Reopen on regression | Medium | 6 |
| Testing | Evidence access RBAC | Easy | 4 |
| Documentation | VAPT closure evidence template | Medium | 3 |
| Documentation | Retest request checklist | Easy | 2 |

**Feature Total: 70 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
