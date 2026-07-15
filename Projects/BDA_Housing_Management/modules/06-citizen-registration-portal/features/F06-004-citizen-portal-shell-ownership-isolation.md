# F06-004 — Citizen Portal Shell & Ownership Isolation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-004 |
| **Feature Name** | Citizen Portal Shell & Ownership Isolation |
| **Module** | 06 — Citizen Registration Portal |

### Description
Provide the citizen portal landing experience, navigation to enabled self-service processes, personal notification entry points, and a consistent ownership boundary across citizen records.

### Business Objective
Give each citizen a coherent self-service entry point while preventing exposure of another citizen’s applications, payments, documents, or status.

### Actors
Citizen; BDA Portal Administrator; Auditor.

### User Journey
After sign-in, a citizen sees a personal landing page and navigates to authorised application, payment, tracking, download, and notification views; every linked record is checked against the logged-in citizen.

### Functional Capabilities
- Portal dashboard shell, navigation, session-aware header, and contextual action links.
- Personal summary cards for active applications, payments due, document downloads, and notifications.
- Common ownership enforcement for citizen-facing transaction lookup and deep links.

### Inputs
Authenticated citizen identity, enabled modules, own transaction summaries, and notification indicators.

### Outputs
Personal portal landing view, permitted navigation, and ownership-denied response for unauthorised record requests.

### Business Rules
A citizen can access only records linked to that citizen identity; shared household or representative access is not included unless explicitly configured; portal links respect process state and role permissions.

### Validations
Authenticated session, valid record ownership, active citizen account, and permitted destination state.

### Calculations
Personal counts of active applications, pending dues, unread notifications, and available downloads.

### Workflow
Sign in → personal landing → permitted process area → own record view/download → sign out/session expiry.

### Search Requirements
Personal application number, booking number, payment reference, and document reference searches restricted to owned records.

### Documents
Portal does not own documents; it provides controlled routes to process documents in Modules 07–10.

### Reports
Citizen portal access and ownership-denial audit register.

### Notifications
Unread notification indicator and links to Module 12 in-app notices.

### Security
Citizen ownership isolation on every portal route, session timeout, anti-enumeration handling, and audit logging of sensitive downloads.

### Integrations
Personal summary and notification consumption from process modules and Module 12 (Medium).

### Dependencies
Module 01 authentication/RBAC; Modules 07–12; F06-001 and F06-002.

### Assumptions
Officer operational navigation is outside this feature; representative/agent access is excluded.

### Risks
An inconsistent ownership check in any downstream portal view could disclose citizen data.

### Non Functional Requirements
Responsive navigation, accessible keyboard paths, secure deep-link handling, and consistent session behaviour.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Portal landing, navigation, and personal summary | UI | Very High | 16 |
| Ownership-enforced portal routing | API | Very High | 16 |
| Portal preferences and access audit persistence | Database | Medium | 4 |
| Process-summary and notification consumption | Integration | Medium | 16 |
| Ownership isolation tests | Testing | Very High | 12 |
| Citizen portal navigation guide | Documentation | Complex | 4 |
| **Total** | | | **68** |

### Estimation Assumptions
Process-specific screens and their business operations are estimated in their owning modules; this is the shared citizen portal shell.
