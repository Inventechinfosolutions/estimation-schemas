# F01-004 — User Lifecycle Management

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-004 |
| **Feature Name** | User Lifecycle Management |
| **Module** | 01 — User & Role Management |

### Description
Allow authorized administrators to create, update, search, activate, deactivate, and unlock CPMS users (officer and tenant-linked accounts) with complete auditability.

### Business Objective
Maintain an accurate, controlled user directory so only authorized personnel and tenants can access CPMS.

### Actors
- Super Administrator
- Delegated admin (if permitted by permission set)
- Auditor (read-only)
- User (self-profile view limited fields)

### User Journey
1. Admin opens User Management.
2. Searches/filters existing users.
3. Creates a new user with identity, contact, account type, and initial role(s).
4. Edits profile details as needed.
5. Activates/deactivates or unlocks after lockout.
6. System records changes for audit.

### Functional Capabilities
- Create / update user profiles
- Account types: Officer, Tenant Portal, System/Admin
- Link tenant portal user to tenant master (when tenant exists — Module 04)
- Activate / deactivate without deleting historical references
- Unlock after failed-attempt lockout
- Assign one or more roles (role definition in F01-005)
- Export user register (Excel) for admin use

### Inputs
- Name, login ID, email, mobile
- Account type, status
- Organization attributes (designation/department — as available)
- Role assignment (reference)
- Tenant reference (for portal users)

### Outputs
- Saved user record
- Status change confirmation
- User list / export

### Business Rules
- Login ID unique across system.
- Deactivated users cannot authenticate but remain visible historically.
- Cannot deactivate the last active Super Administrator.
- Tenant portal users require tenant linkage before activation (when tenant module data exists).
- Soft delete only; no hard delete of users with transactional history.

### Validations
- Mandatory identity and contact fields by account type
- Email/mobile format
- Unique login ID
- Role required before activation for officer accounts

### Calculations
None significant.

### Workflow
Optional maker-checker for creating privileged roles (if configured in Module 02). Baseline: Super Admin direct save with audit.

### Search Requirements
- Search by name, login ID, email, mobile, role, status, account type, location scope
- Filters and pagination
- Export filtered results

### Documents
None mandatory (profile photo optional — out unless requested).

### Reports
User Register export (Excel).

### Notifications
Optional email on account creation / activation with credentials flow deferred to F01-008 for tenants and password setup for officers.

### Security
- Only users with User Admin permission can mutate users
- Masking of sensitive fields for non-admin viewers
- All changes audited

### Integrations
None directly.

### Dependencies
- F01-005 (roles)
- F01-006 (scopes — may be assigned in same or follow-up step)
- Module 04 Tenant master for portal linkage
- F01-001 for authentication impact of status

### Assumptions
- Indicative BDA roles seeded via F01-005/F01-010.
- Bulk HR LDAP sync out of scope.
- Enterprise CRUD quality with validation and logging included.

### Risks
- Orphan tenant portal users if tenant master not ready; activation rule must be enforced.
- Duplicate persons with multiple logins without identity uniqueness beyond login ID.

### Non Functional Requirements
- List page under 3s for typical admin datasets
- Responsive admin UI
- Excel export supported

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: account types, status lifecycle, unique identity, search/export, last-admin protection.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| User list with search/filter | UI | Medium | 6 |
| User create / edit form | UI | Medium | 6 |
| Activate / deactivate confirmation | UI | Simple | 2 |
| User CRUD + search operations | API | Medium | 6 |
| Activate / deactivate / unlock operations | API | Easy | 4 |
| User profile entities & indexes | Database | Medium | 4 |
| User lifecycle tests | Testing | Complex | 8 |
| User admin guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Role matrix UI not included (F01-005); only role multi-select reference on user form.
- Data scope mapping detailed UI estimated in F01-006.
