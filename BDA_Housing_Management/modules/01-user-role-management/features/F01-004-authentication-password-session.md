# F01-004 — Authentication, Password & Session Security

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-004 |
| **Feature Name** | Authentication, Password & Session Security |
| **Module** | 01 — User & Role Management |

### Description
Provide secure officer authentication, password policy, reset, logout, and session timeout. After login, the session resolves authority from the Person’s active **Post** → Post’s **Role** → **Permissions**.

### Business Objective
Protect BHMS access and bind the session to the correct organisational post.

### Actors
All officers (via Post); Super Administrator.

### User Journey
1. Person signs in with credentials.  
2. System validates Person is active and has at least one active Person–Post mapping.  
3. Session selects primary/active Post (or offers post switch when multiple Posts are allowed).  
4. Permissions load from the Post’s Role; officer works under that Post context until logout/timeout.

### Functional Capabilities
- Login/logout; password change/reset; password policy; timeout; failed-login handling  
- Active Post resolution and optional post switcher  
- Session carries Person, Post, Role, and permission set  
- Session invalidation on Person/Post deactivation where configured  

### Inputs
Login ID, password, reset request, selected Post (when multiple).

### Outputs
Authenticated session with Post context, password reset outcome, access event.

### Business Rules
- Inactive Person cannot authenticate.  
- Login requires at least one active Person–Post mapping to an active Post with an active Role.  
- Authorisation checks use the session Post’s Role permissions, not ad-hoc person roles.  
- Password policy and timeout apply to officer Persons.

### Validations
Credential presence; password policy; active mapping/Post/Role chain; reset identity checks.

### Calculations
None.

### Workflow
Credential validation → resolve active Post → load Role permissions → session → access audit.

### Search Requirements
Login ID, Person, Post, authentication outcome, date range (administrators/auditors).

### Documents
None.

### Reports
Authentication Activity extract (with Post context).

### Notifications
Password reset and account-security notices as configured.

### Security
Secure credential handling; Post-scoped RBAC after login; session expiry; audit.

### Integrations
None.

### Dependencies
F01-001; F01-002; F01-003.

### Assumptions
Citizen login UX is owned by Module 06; this feature covers officer Person sessions.

### Risks
Ambiguous multi-post selection can cause officers to act under the wrong Post.

### Non Functional Requirements
HTTPS; agreed response time; secure error messages; session reliability.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Officer sign-in and password screens | UI | Complex | 8 |
| Password reset and policy administration | UI | Medium | 6 |
| Active Post selection / switcher | UI | Easy | 4 |
| Authentication, session, Post resolution | API | Very High | 16 |
| Credential and session persistence | Database | Complex | 6 |
| Authentication security tests (incl. Post context) | Testing | Very High | 12 |
| Access-security guide | Documentation | Medium | 3 |
| **Total** | | | **55** |

### Estimation Assumptions
- Uses Estimation Master values only.  
- Permission matrix maintenance remains in F01-002.  
