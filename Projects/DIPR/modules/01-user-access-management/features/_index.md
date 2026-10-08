# Feature Index — Ultra Detailed
## 01 — User & Access Management

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Line items | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|-----------:|-------|
| F01-001 | User account lifecycle | 26 | 34 | 7 | 0 | 20 | 4 | 91 | 24 |  |
| F01-002 | Role & permission matrix | 32 | 36 | 9 | 0 | 20 | 4 | 101 | 22 |  |
| F01-003 | Optional SSO integration | 24 | 32 | 3 | 16 | 22 | 4 | 101 | 19 | OPTIONAL |
| F01-004 | Multi-factor authentication | 26 | 34 | 8 | 8 | 24 | 5 | 105 | 23 |  |
| F01-005 | Access audit trail | 18 | 22 | 6 | 0 | 14 | 3 | 63 | 16 |  |

**Module Total:** **461 hours** · **104 artefact line items**

### Module estimation line-item roll-up

| Area | Hours |
|------|------:|
| UI | 126 |
| API | 158 |
| Database | 33 |
| Integration | 24 |
| Testing | 100 |
| Documentation | 20 |

### Ultra-detailed artefact catalogue

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F01-001 | UI | AMT User register with type/status/role filters | Medium | 6 |
| F01-001 | UI | User create profile form (staff/vendor/field) | Medium | 6 |
| F01-001 | UI | User edit profile with vendor master linkage picker | Medium | 6 |
| F01-001 | UI | Role multi-select panel at save | Easy | 4 |
| F01-001 | UI | Activate/deactivate modal with reason capture | Simple | 2 |
| F01-001 | UI | Local account credential reset initiation dialog | Simple | 2 |
| F01-001 | API | List users with search filters and pagination | Medium | 6 |
| F01-001 | API | Get user profile by identifier | Simple | 2 |
| F01-001 | API | Create user with role assignments | Medium | 6 |
| F01-001 | API | Update user profile and role links | Medium | 6 |
| F01-001 | API | Activate user lifecycle transition | Easy | 4 |
| F01-001 | API | Deactivate user with reason | Easy | 4 |
| F01-001 | API | Initiate password/credential reset | Easy | 4 |
| F01-001 | API | Active email uniqueness validation | Simple | 2 |
| F01-001 | Database | User core entity columns | Easy | 2 |
| F01-001 | Database | User–role junction with FK constraints | Easy | 2 |
| F01-001 | Database | Unique active email index | Easy | 2 |
| F01-001 | Database | Vendor FK for vendor user type | Simple | 1 |
| F01-001 | Testing | Create staff/vendor/field happy paths | Medium | 6 |
| F01-001 | Testing | Validation: missing role, duplicate email | Medium | 6 |
| F01-001 | Testing | Deactivate blocks auth; reactivation restore | Easy | 4 |
| F01-001 | Testing | Administrator-only access for other roles | Easy | 4 |
| F01-001 | Documentation | User administration guide (register/lifecycle) | Easy | 2 |
| F01-001 | Documentation | UAT script: vendor user with master linkage | Easy | 2 |
| F01-002 | UI | Role register list with search | Easy | 4 |
| F01-002 | UI | Role create/edit metadata form | Easy | 4 |
| F01-002 | UI | Module permission matrix grid (CRUD/approve/verify) | Complex | 12 |
| F01-002 | UI | Copy permissions from existing role dialog | Medium | 6 |
| F01-002 | UI | Role deactivate confirmation with assigned-user warning | Simple | 2 |
| F01-002 | UI | Read-only permission preview for auditors | Easy | 4 |
| F01-002 | API | List roles with filters | Simple | 2 |
| F01-002 | API | Create and update role metadata | Easy | 4 |
| F01-002 | API | Get permission matrix for role | Easy | 4 |
| F01-002 | API | Persist bulk permission map replace | Complex | 8 |
| F01-002 | API | Clone role permissions from source role | Medium | 6 |
| F01-002 | API | Deactivate role with dependency check | Medium | 6 |
| F01-002 | API | Resolve effective permissions for session | Medium | 6 |
| F01-002 | Database | Role entity | Simple | 1 |
| F01-002 | Database | Permission catalogue seed storage | Easy | 2 |
| F01-002 | Database | Role–permission assignment storage | Medium | 4 |
| F01-002 | Database | Module-scoped permission uniqueness constraints | Easy | 2 |
| F01-002 | Testing | Matrix: campaign approver vs PoD verifier roles | Complex | 8 |
| F01-002 | Testing | Unauthorized module entry denied | Medium | 6 |
| F01-002 | Testing | Role clone and deactivate with assigned users | Medium | 6 |
| F01-002 | Documentation | RBAC configuration handbook | Easy | 2 |
| F01-002 | Documentation | UAT: approver cannot verify PoD | Easy | 2 |
| F01-003 | UI | SSO IdP configuration screen (metadata, certificates) | Medium | 6 |
| F01-003 | UI | IdP attribute-to-AMT field mapping grid | Medium | 6 |
| F01-003 | UI | Login page SSO entry and federation error states | Easy | 4 |
| F01-003 | UI | SSO link status panel on user profile | Simple | 2 |
| F01-003 | UI | JIT provision dry-run test panel | Medium | 6 |
| F01-003 | API | Initiate federated login (auth request) | Complex | 8 |
| F01-003 | API | Consume IdP callback and issue AMT session | Complex | 8 |
| F01-003 | API | JIT create or link user from IdP attributes | Medium | 6 |
| F01-003 | API | SSO configuration CRUD | Medium | 6 |
| F01-003 | API | Apply default role on first SSO login | Easy | 4 |
| F01-003 | Integration | IdP protocol adapter (auth, mapping, retry) | Medium | 16 |
| F01-003 | Database | SSO external identity link on user | Easy | 2 |
| F01-003 | Database | SSO configuration store | Simple | 1 |
| F01-003 | Testing | SSO happy-path login | Medium | 6 |
| F01-003 | Testing | Certificate expiry and invalid signature | Medium | 6 |
| F01-003 | Testing | Deactivated user blocked at SSO | Easy | 4 |
| F01-003 | Testing | JIT role assignment edge cases | Medium | 6 |
| F01-003 | Documentation | SSO setup runbook for DIPR IT | Easy | 2 |
| F01-003 | Documentation | UAT federation sign-off checklist | Easy | 2 |
| F01-004 | UI | MFA enrollment wizard with TOTP QR | Medium | 6 |
| F01-004 | UI | Login MFA TOTP challenge screen | Easy | 4 |
| F01-004 | UI | Login MFA SMS OTP challenge screen | Easy | 4 |
| F01-004 | UI | Admin MFA policy toggles by role | Medium | 6 |
| F01-004 | UI | Backup codes generate and confirm modal | Simple | 2 |
| F01-004 | UI | Admin force-reset MFA for user dialog | Simple | 2 |
| F01-004 | UI | MFA lockout user messaging panel | Simple | 2 |
| F01-004 | API | Enroll TOTP secret and confirm enrollment | Complex | 8 |
| F01-004 | API | Verify MFA challenge at login | Medium | 6 |
| F01-004 | API | Send and verify SMS OTP | Medium | 6 |
| F01-004 | API | Admin read/update MFA policy by role | Medium | 6 |
| F01-004 | API | Generate and invalidate backup codes | Easy | 4 |
| F01-004 | API | Admin reset MFA enrollment for user | Easy | 4 |
| F01-004 | Integration | SMS gateway OTP dispatch (provision) | Easy | 8 |
| F01-004 | Database | MFA enrollment secrets (encrypted) | Medium | 4 |
| F01-004 | Database | MFA policy flags per role | Easy | 2 |
| F01-004 | Database | Backup codes hash storage | Easy | 2 |
| F01-004 | Testing | MFA policy enforced per role | Complex | 8 |
| F01-004 | Testing | Lockout after failed attempts | Medium | 6 |
| F01-004 | Testing | Backup code one-time use | Medium | 6 |
| F01-004 | Testing | TOTP clock skew tolerance | Easy | 4 |
| F01-004 | Documentation | MFA operations guide for administrators | Medium | 3 |
| F01-004 | Documentation | UAT MFA enrollment and recovery scripts | Easy | 2 |
| F01-005 | UI | Access audit register with actor/action filters | Medium | 6 |
| F01-005 | UI | Audit event detail drawer (before/after snapshot) | Easy | 4 |
| F01-005 | UI | Quick date-range presets (today/7d/30d) | Simple | 2 |
| F01-005 | UI | Export filtered audit slice to CSV dialog | Easy | 4 |
| F01-005 | UI | Login failure spike filter chip | Simple | 2 |
| F01-005 | API | Ingest authentication login/logout/failure events | Medium | 6 |
| F01-005 | API | Ingest privilege change events (users/roles) | Medium | 6 |
| F01-005 | API | Query audit register with filters and pagination | Medium | 6 |
| F01-005 | API | Export filtered audit register | Easy | 4 |
| F01-005 | Database | Append-only access audit event storage | Medium | 4 |
| F01-005 | Database | Time-series indexes on actor and timestamp | Easy | 2 |
| F01-005 | Testing | Events on login and permission matrix change | Medium | 6 |
| F01-005 | Testing | Filter combinations and export correctness | Easy | 4 |
| F01-005 | Testing | Append-only immutability enforcement | Easy | 4 |
| F01-005 | Documentation | Access audit register user guide | Easy | 2 |
| F01-005 | Documentation | UAT: trace administrator role change | Simple | 1 |
