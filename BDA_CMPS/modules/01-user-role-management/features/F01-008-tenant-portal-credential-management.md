# F01-008 — Tenant Portal Credential Management

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-008 |
| **Feature Name** | Tenant Portal Credential Management |
| **Module** | 01 — User & Role Management |

### Description
Issue, activate, revoke, and reset tenant self-service portal credentials linked to tenant records, including first-login password change and notification of access details.

### Business Objective
Enable tenants to securely access dues, payments, complaints, and documents through the portal as required by the SOW, without sharing officer accounts.

### Actors
- Super Administrator / Estate or Accounts officer with permission
- Tenant (Portal)
- System

### User Journey
1. Officer selects a tenant and chooses **Issue Portal Access**.
2. System creates/links a tenant user with Tenant (Portal) role and temporary credentials.
3. Tenant receives notification (email/SMS) with activation instructions.
4. Tenant logs in, forced to change password (F01-002), then accesses portal features owned by other modules.
5. Officer may reset or revoke access on request or lease closure.

### Functional Capabilities
- Issue portal credentials to a tenant
- Resend activation/notification
- Reset portal password
- Revoke/deactivate portal access
- Show portal access status on tenant/user screens
- Enforce one active portal login per tenant (configurable)

### Inputs
- Tenant ID
- Registered email/mobile
- Issue / reset / revoke action

### Outputs
- Portal user linkage
- Notification dispatch
- Status on tenant/user profile

### Business Rules
- Portal role is Tenant (Portal) with self-data permissions only.
- Credentials cannot be issued without contact channel (email or mobile).
- On lease termination, access may auto-revoke or remain read-only per BDA policy (configurable).
- Officer users cannot be converted to tenant type without controlled migration (out of baseline).

### Validations
- Tenant exists and is eligible
- Contact present
- No duplicate active portal user if single-account rule enabled

### Calculations
None.

### Workflow
Issue → notify → first login → force password change → active portal use.

### Search Requirements
- Filter tenants/users by portal status (Issued/Active/Revoked)

### Documents
None.

### Reports
Portal Access Register (Excel).

### Notifications
Credential issuance, reset, and revocation notices via Module 09.

### Security
- Temporary passwords/OTPs time-bound
- Tenant authorization scoped to own tenant/leases only
- Revoke immediate session invalidation

### Integrations
- Internal Notification Service (Simple)

### Dependencies
- F01-001, F01-002, F01-004, F01-005
- Module 04 Tenant master
- Module 09 notifications

### Assumptions
- Portal functional pages (dues/pay/complaints) estimated under Modules 04/05/07; this feature covers identity/credential only.
- Temporary secret delivery via email/SMS only.
- Enterprise controls included.

### Risks
- Incorrect tenant linkage could expose another tenant’s data — requires strict scope tests.
- Contact data quality blocks issuance.

### Non Functional Requirements
- Mobile-friendly first-login screens
- Immediate revoke propagation to active sessions

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: tenant–user linkage, issuance/revoke lifecycle, notification handoff, forced first login.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Admin issue / reset tenant credentials actions | UI | Easy | 4 |
| Tenant first-login / force password change screens | UI | Medium | 6 |
| Issue / revoke / reset portal credentials operations | API | Complex | 8 |
| Tenant–user linkage attributes | Database | Easy | 2 |
| Credential notification handoff | Integration | Simple | 4 |
| Tenant credential tests | Testing | Complex | 8 |
| Tenant portal access guide | Documentation | Easy | 2 |
| **Total** | | | **34** |

### Estimation Assumptions
- Does not include payment or complaint portal pages.
- Gateway costs remain under Modules 09/10.
