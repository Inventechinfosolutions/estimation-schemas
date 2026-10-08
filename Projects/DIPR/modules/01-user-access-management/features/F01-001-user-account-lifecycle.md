# F01-001 — User account lifecycle

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-001 |
| Feature Name | User account lifecycle |
| Module | 01 — User & Access Management |
| Description | Create, update, activate/deactivate staff, vendor, and field user accounts for the Advertisement Monitoring Tool. |
| Business Objective | Maintain a trusted user register so DIPR staff, vendors, and field personnel access AMT only through governed accounts tied to roles. |
| Actors | DIPR Administrator |

### User Journey

- Administrator opens the AMT User register → filters by user type (staff / vendor / field) and status → creates or edits a profile → assigns one or more roles → activates or deactivates without deleting history.

### Functional Capabilities

- User register with search and filters (name, email, mobile, user type, role, status)
- Create/edit user profile with staff ID, vendor linkage, and contact details
- Assign roles at save (User → Role → Permissions enforced elsewhere)
- Activate/deactivate with reason capture
- Password / credential reset initiation for local accounts (when SSO disabled for user)

### Inputs

- Full name, email, mobile, user type, optional vendor reference, staff/employee ID, role assignments, status, deactivation reason

### Outputs

- Persisted user record with role links
- Updated register reflecting lifecycle state

### Business Rules

- Only Administrator manages user accounts
- Deactivated users cannot authenticate to web, mobile, or APIs
- Vendor users must reference an active vendor master record when user type is vendor
- Field users are flagged for mobile channel eligibility

### Validations

- Mandatory name, email, user type, and at least one role for active users
- Unique email among active users; valid email and mobile formats

### Calculations

- None

### Workflow

- Create → Active (pending first login) → Active → Deactivated; reactivation restores prior role assignments unless changed

### Search Requirements

- Search by name, email, mobile, staff ID, user type, role, status

### Documents

- None

### Reports

- None

### Notifications

- Optional welcome / credential notification when local account created (template from Module 02)

### Security

- Administrator-only; audit create, update, activate, deactivate, and role assignment changes

### Integrations

- None (SSO provisioning handled in F01-003)

### Dependencies

- F01-002 Role & permission matrix (roles must exist)
- Vendor master (F02-002) for vendor user type

### Assumptions

- Initial user load provided by DIPR during cutover
- District/org scoping on users deferred unless DIPR confirms

### Risks

- Duplicate emails in legacy vendor lists require merge before go-live

### Non Functional Requirements

- Responsive web UI; sub-second register search for typical volumes; immutable audit of lifecycle events

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | AMT User register with type/status/role filters | Medium | 6 |
| UI | User create profile form (staff/vendor/field) | Medium | 6 |
| UI | User edit profile with vendor master linkage picker | Medium | 6 |
| UI | Role multi-select panel at save | Easy | 4 |
| UI | Activate/deactivate modal with reason capture | Simple | 2 |
| UI | Local account credential reset initiation dialog | Simple | 2 |
| API | List users with search filters and pagination | Medium | 6 |
| API | Get user profile by identifier | Simple | 2 |
| API | Create user with role assignments | Medium | 6 |
| API | Update user profile and role links | Medium | 6 |
| API | Activate user lifecycle transition | Easy | 4 |
| API | Deactivate user with reason | Easy | 4 |
| API | Initiate password/credential reset | Easy | 4 |
| API | Active email uniqueness validation | Simple | 2 |
| Database | User core entity columns | Easy | 2 |
| Database | User–role junction with FK constraints | Easy | 2 |
| Database | Unique active email index | Easy | 2 |
| Database | Vendor FK for vendor user type | Simple | 1 |
| Testing | Create staff/vendor/field happy paths | Medium | 6 |
| Testing | Validation: missing role, duplicate email | Medium | 6 |
| Testing | Deactivate blocks auth; reactivation restore | Easy | 4 |
| Testing | Administrator-only access for other roles | Easy | 4 |
| Documentation | User administration guide (register/lifecycle) | Easy | 2 |
| Documentation | UAT script: vendor user with master linkage | Easy | 2 |

**Feature Total: 91 hours**

### Estimation Assumptions

- Hours from Estimation Master only; enterprise validation, logging, and security included.
- No API endpoint or table design artefacts in this estimate.
- SSO-only users may skip local password flows when F01-003 is enabled.
