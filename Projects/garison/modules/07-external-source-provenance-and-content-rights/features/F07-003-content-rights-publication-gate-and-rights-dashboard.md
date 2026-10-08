# F07-003 — Content Rights Publication Gate & Rights Dashboard

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-003 |
| Feature Name | Content Rights Publication Gate & Rights Dashboard |
| Module | 07 — External Source, Provenance & Content Rights |
| Module Type | Business |
| Release | Go-live |

### Description
Rules engine that blocks publication of third-party media or text when rights are 'To be confirmed' or usage is 'Restricted'; supports publishing with Garrison-owned content only (third-party media suppressed); flags third-party media; rights status dashboard with re-verification worklist and reminders.

### Business Objective
Protect Garrison from publishing content it has no right to reproduce, while still allowing external profiles to appear with Garrison-owned content where permissible.

### Actors
- Catalogue Administrator
- Super Administrator
- Catalogue Reviewer (view)

### User Journey
1. **Who creates:** Gate results are generated automatically by the system at preview, submission and publish; media flags are set by administrators in the media manager.
2. **How they create:** Administrators flag media and text sections as third-party; the gate panel lists blocking reasons and affected media.
3. **How they edit:** They resolve blocks by confirming rights (F07-002), replacing media with Garrison-owned content, or choosing 'Publish with Garrison-owned content only'.
4. **How they send for approval:** The gate is evaluated automatically; it is not an approval but a hard rule applied before publish (F06-004).
5. **How the approver sees pending items:** There is no approver inbox; the rights dashboard lists products blocked by the gate and those due for re-verification.
6. **How the approver decides:** No human decision overrides the gate; only a change in rights status or content removes the block.
7. **How the maker sees history:** Makers see gate results in the workspace and preview.
8. **How the approver / auditor sees history:** Auditors see gate evaluations at publish and rights changes in the audit log; the dashboard gives the current position.

### Functional Capabilities
- Gate decision matrix (rights status × usage status × media/text ownership)
- Third-party flag on media and descriptive text
- Publish with Garrison-owned content only (suppress third-party media and text publicly)
- Rights dashboard: counts by status, blocked products, due for re-verification
- Re-verification interval setting (default 12 months) and reminder emails
- Gate result panel in workspace, preview and publish dialogs

### UI Screens
- Rights gate result panel
- Third-party media flagging in media manager
- Rights status dashboard
- Re-verification worklist

### Logical API Operations
- Evaluate rights gate
- Flag or unflag third-party media and text
- Get rights dashboard aggregates
- Get re-verification due list
- Apply Garrison-owned-content-only publication mode
- Send re-verification reminders

### Inputs
- Provenance statuses
- Media/text third-party flags
- Publication mode
- Re-verification interval

### Outputs
- Gate pass/fail with reasons
- Suppressed public content where applicable
- Dashboard and reminders

### Business Rules
- Rights 'To be confirmed' or usage 'Restricted' blocks publication of any third-party flagged media or text
- Garrison-owned-content-only mode publishes attributes and Garrison media only
- Usage 'Restricted' with no Garrison-owned content results in 'Reference only' (not publishable)

### Validations
- Re-verification interval 1–36 months

### Calculations
- Next verification due = date verified + interval

### Workflow
Evaluated at preview, submission and publish

### Search Requirements
- Dashboard filters: source, rights status, usage status, due date

### Documents
- None

### Reports
- Rights status dashboard
- Blocked products export

### Notifications
- Re-verification reminders via F06-005

### Security
- Gate enforced server-side; cannot be bypassed by any role

### Integrations
- None

### Dependencies
- F07-002
- F04-004
- F06-004
- F06-005
- F08-003

### Assumptions
- Garrison-owned content alternatives are prepared in the population workstream

### Risks
- Many external products blocked if rights confirmation is slow; dashboard makes the backlog visible

### Non Functional Requirements
- Gate evaluation under 200 ms per item

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Rights gate result panel | Medium | 6 |
| UI | Third-party media flagging in media manager | Easy | 4 |
| UI | Rights status dashboard | Very High | 16 |
| UI | Re-verification worklist | Medium | 6 |
| API | Evaluate rights gate | Complex | 8 |
| API | Flag or unflag third-party media and text | Easy | 4 |
| API | Get rights dashboard aggregates | Medium | 6 |
| API | Get re-verification due list | Medium | 6 |
| API | Apply Garrison-owned-content-only publication mode | Complex | 8 |
| API | Send re-verification reminders | Easy | 4 |
| Database | Media and text rights flags | Easy | 2 |
| Database | Re-verification schedule | Simple | 1 |
| Testing | Gate decision matrix | Complex | 8 |
| Testing | Suppression of third-party media on public pages | Medium | 6 |
| Documentation | Content rights governance procedure | Medium | 3 |

**Feature Total: 88 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 36 | 3 | 0 | 14 | 3 | **88** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Dashboard is a Very High UI
- Gate matrix and suppression mode drive Complex rows
- No external integration channel in this feature; Integration row omitted.
