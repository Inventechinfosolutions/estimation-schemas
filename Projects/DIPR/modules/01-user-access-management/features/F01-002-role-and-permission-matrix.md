# F01-002 — Role & permission matrix

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-002 |
| Feature Name | Role & permission matrix |
| Module | 01 — User & Access Management |
| Description | Define roles and map create/read/update/approve/verify permissions by AMT module for RBAC enforcement. |
| Business Objective | Ensure campaign officers, approvers, verifiers, vendors, and auditors see only permitted modules and actions across web and mobile. |
| Actors | DIPR Administrator |

### User Journey

- Administrator opens Role register → creates or edits a role → opens Permission matrix → toggles module-level actions (create, read, update, approve, verify) → saves → users with that role receive updated entitlements on next session.

### Functional Capabilities

- Role CRUD with description and active flag
- Permission matrix grid by module (01–10 capability areas as applicable)
- Standard action verbs: create, read, update, approve, verify (plus admin configure where needed)
- Clone role as starting point for new roles
- Effective permission preview for a sample user

### Inputs

- Role name, description, status, matrix of module × permission flags

### Outputs

- Role definition and permission map consumed by authorization layer
- Audit of matrix changes

### Business Rules

- At least one system Administrator role cannot be deleted or stripped of full access
- Approve and verify are distinct for Campaign Management and PoD modules
- Vendor role defaults exclude master configuration and platform security modules

### Validations

- Unique role name; matrix must be complete for all in-scope modules before activation

### Calculations

- None

### Workflow

- Draft role → Active; changes apply without redeploy

### Search Requirements

- Search roles by name and status

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Administrator-only; all matrix edits audited

### Integrations

- None

### Dependencies

- None (foundational for all modules)

### Assumptions

- Module list aligns with SOW consolidated modules 01–10

### Risks

- Over-permissive vendor roles if DIPR does not validate matrix in UAT

### Non Functional Requirements

- Authorization checks on every module entry point; matrix changes effective within same session refresh policy

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Role register list with search | Easy | 4 |
| UI | Role create/edit metadata form | Easy | 4 |
| UI | Module permission matrix grid (CRUD/approve/verify) | Complex | 12 |
| UI | Copy permissions from existing role dialog | Medium | 6 |
| UI | Role deactivate confirmation with assigned-user warning | Simple | 2 |
| UI | Read-only permission preview for auditors | Easy | 4 |
| API | List roles with filters | Simple | 2 |
| API | Create and update role metadata | Easy | 4 |
| API | Get permission matrix for role | Easy | 4 |
| API | Persist bulk permission map replace | Complex | 8 |
| API | Clone role permissions from source role | Medium | 6 |
| API | Deactivate role with dependency check | Medium | 6 |
| API | Resolve effective permissions for session | Medium | 6 |
| Database | Role entity | Simple | 1 |
| Database | Permission catalogue seed storage | Easy | 2 |
| Database | Role–permission assignment storage | Medium | 4 |
| Database | Module-scoped permission uniqueness constraints | Easy | 2 |
| Testing | Matrix: campaign approver vs PoD verifier roles | Complex | 8 |
| Testing | Unauthorized module entry denied | Medium | 6 |
| Testing | Role clone and deactivate with assigned users | Medium | 6 |
| Documentation | RBAC configuration handbook | Easy | 2 |
| Documentation | UAT: approver cannot verify PoD | Easy | 2 |

**Feature Total: 101 hours**

### Estimation Assumptions

- Matrix covers discrete modules, not row-level data scoping unless later confirmed by DIPR.
- Mobile and API enforcement share the same permission model.
