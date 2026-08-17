# F01-002 — Valuation Posts on the shared component

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Valuation Posts on the shared component |
| **Module** | 01 — Shared User & Access Control (consumed) |

### Description
An Administrator configures Posts such as Office user, Approved Valuer and Competent Authority on the shared Claim Module 01 component and maps Persons. A contract staff or security-guard Person used on a valuation site is likewise a shared Person, not a local account. Changing the Post mapping changes which valuation menus the Person sees on next login.

### Business Objective
Expose the correct valuation menus from shared Posts, without a second Post directory.

### Actors
Administrator (shared IAM); Office user; Approved Valuer; Competent Authority; contract staff / security-guard Persons as configured.

### User Journey
1. Administrator creates or selects Posts (Office user, Approved Valuer, Competent Authority, others named by the Authority) on the shared component.
2. Administrator maps Persons, including contract staff or security guards used on a valuation site, to those Posts.
3. On next valuation login the Person sees only menus allowed for the mapped Post.
4. Changing the mapping changes menus on the subsequent session; no local account is created.

### Functional Capabilities
- Map valuation menu sets to shared Posts (Office user, Approved Valuer, CA, others named by SPLOCA)
- Treat contract staff and security-guard Persons as shared Persons, not local accounts
- Refresh menu visibility from the current Post mapping at login

### Inputs
Shared Post identifier; Person–Post mapping; valuation menu-set selection.

### Outputs
Post-to-valuation-menu configuration; next-login menu set for the Person.

### Business Rules
- Posts are configured on the shared component, not a valuation-only Post master
- Approved Valuer professional master (rates, order, category) is Module 02, not this feature
- Menu changes take effect on next login

### Validations
- Post exists on the shared component
- Person–Post mapping is active
- Menu set is one of the Authority-named valuation sets

### Calculations
None.

### Workflow
Configure Post on shared component → map Person → valuation reads mapping at login → menus.

### Search Requirements
Post name, Person, menu set, last mapping change.

### Documents
None.

### Reports
Valuation Post mapping list.

### Notifications
None beyond in-app confirmation of mapping save.

### Security
Only shared-IAM Administrators change Post mapping. Valuation cannot invent Posts.

### Integrations
Read/configure Posts and Person–Post maps on Claim Module 01 (REST consume).

### Dependencies
F01-001; Claim F01-002 Post/Role mapping.

### Assumptions
- SPLOCA confirms the named valuation Posts before configuration
- Hours do not rebuild the shared Post master

### Risks
Incorrect Post mapping exposes CA or assignment menus to the wrong Person.

### Non Functional Requirements
Mapping changes are attributable to the Administrator Person; next-login consistency.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Valuation Post-to-menu mapping | UI | Medium | 6 |
| Post-to-menu resolution at login | API | Medium | 6 |
| Valuation menu-set configuration | Database | Easy | 2 |
| Shared Post/Role consume | Integration | Easy | 8 |
| Post menu-visibility tests | Testing | Medium | 6 |
| Valuation Posts configuration note | Documentation | Easy | 2 |
| **Total** | | | **30** |

### Estimation Assumptions
- Person/Post CRUD remains Claim Module 01
- Professional valuer rates are F02-001, not this feature
