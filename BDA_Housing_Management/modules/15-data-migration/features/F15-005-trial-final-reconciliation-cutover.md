# F15-005 — Trial, Final Reconciliation & Cutover

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F15-005 |
| **Feature Name** | Trial, Final Reconciliation & Cutover |
| **Module** | 15 — Data Migration |

### Description
Run trial and final migration loads with source-target count/sample reconciliation, exception closure tracking, cutover status, and sign-off evidence.
### Business Objective
Achieve controlled migration acceptance before BHMS production go-live.
### Actors
- Vendor migration team; BDA data owners/SMEs; project authority
### User Journey
1. Trial load is run and reconciled. 2. BDA resolves agreed exceptions and verifies samples. 3. Final load is executed during cutover and acceptance evidence is recorded.
### Functional Capabilities
- Trial/final run control, count and sample reconciliation, exception closure, cutover checklist/status, and sign-off evidence.
### Inputs
- Import outcomes, source counts, sample checks, exception decisions, and cutover approvals.
### Outputs
- Reconciliation result, cutover status, unresolved-exception list, and sign-off evidence.
### Business Rules
- Final cutover proceeds only after agreed reconciliation criteria and BDA approvals are met.
### Validations
- Run state, reconciliation tolerance, authorized sign-off, unresolved critical exceptions, and cutover-window controls.
### Calculations
- Source-target counts, reconciliation variances, and closure rates.
### Workflow
- Trial load → reconcile → resolve → final load → validate → sign off.
### Search Requirements
- By dataset, batch/run, exception, reconciliation status, owner, and sign-off date.
### Documents
- Reconciliation reports, exception register, and BDA sign-off evidence.
### Reports
- Trial/final migration reconciliation and cutover report.
### Notifications
- Cutover status/escalation alerts through Module 12 where configured.
### Security
- Restricted migration access, protected data, auditable approvals, and retained acceptance evidence.
### Integrations
- Internal BHMS migration capabilities.
### Dependencies
- F15-001–F15-004; Modules 02–11; BDA data owners.
### Assumptions
- BDA provides extracts, cleansing decisions, timely verification, and an agreed cutover window.
### Risks
- Late source changes or unresolved exceptions can delay go-live.
### Non Functional Requirements
- Restart/recovery controls, traceable acceptance evidence, and cutover-window performance.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Trial/final reconciliation and cutover workspace | UI | Very High | 16 |
| Reconciliation and cutover-control operations | API | Very High | 16 |
| Run, exception, and sign-off state | Database | Complex | 6 |
| Cutover coordination handoff | Integration | Easy | 8 |
| Trial/final cutover tests | Testing | Very High | 12 |
| Cutover guide | Documentation | Very High | 6 |
| **Total** | | | **64** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. BDA provides extracts, cleansing decisions, timely verification, and an agreed cutover window.
