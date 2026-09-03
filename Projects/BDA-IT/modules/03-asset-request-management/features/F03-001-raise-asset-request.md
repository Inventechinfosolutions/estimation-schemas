# F03-001 — Raise Asset Request

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Raise Asset Request |
| **Module** | 03 — Asset Request Management |

### Description
A logged-in User submits an asset request by selecting an **asset type from the dropdown** (values created by Admin in F02-001), entering a short description, and optionally attaching one supporting file. The request is stored as **Open**.

### Business Objective
Give BDA employees and contractors one controlled place to ask IT for an asset.

### Actors
Maker: User. Approver: none (Admin processing is F03-003).

### User Journey
1. Who creates: User (employee or contractor with User role). Admin may also raise as a User function.
2. How they create: Raise asset request form → select asset type from the dropdown → enter description → optional attachment → submit. Request is saved as Open and shown in the user’s list (F03-002).
3. How they edit: After submit, the User cannot edit the request in this phase. Correction is a new request or an Admin remark on processing.
4. How they send for approval: Submit/approval does not apply. Submit is not a maker–checker step; it only opens the request for Admin.
5. How the approver sees pending items: There is no approver inbox on this feature. Admin sees Open requests under F03-003 / Module 05.
6. How the approver decides: There is no approval decision on this feature.
7. How the applicant / maker sees history: After submit, the User sees the new Open request in their status list (F03-002).
8. How the approver / auditor sees history: Admin sees the submitted request in the all-requests register (F03-003).

### Functional Capabilities
- Raise request using the asset-type dropdown only
- Capture description and optional single attachment
- Set initial status Open with requester and date/time
- Refuse submit without type and description

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Raise asset request form | Medium |
| Request submit confirmation | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Submit asset request | Complex |
| Validate asset request | Medium |
| Store supporting attachment | Medium |

### Inputs
Asset type (dropdown), description, optional file.

### Outputs
Open asset request attributed to the signed-in user; confirmation to the user.

### Business Rules
- Asset type must be a value Admin created in F02-001.
- Requester is the signed-in account; User cannot raise in another user’s name.
- One optional supporting file, not a document library.
- Initial status is Open. User cannot set status.

### Validations
- Asset type mandatory and from the dropdown.
- Description mandatory.
- Attachment type/size within a simple office-file limit.

### Calculations
None.

### Workflow
Submit creates Open. No maker–checker. Status changes are F03-003.

### Search Requirements
None on the raise form (list/search is F03-002).

### Documents
Optional single supporting attachment, embedded on the request.

### Reports
None.

### Notifications
None.

### Security
Signed-in User or Admin. Attachment visible to requester and Admin only.

### Integrations
None.

### Dependencies
F01-003; F02-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Dropdown list API is billed under F02-001, not repeated here.
- User list/detail is F03-002.

### Risks
Users may attach inappropriate files; a simple type/size check is in scope, not content scanning.

### Non Functional Requirements
Form usable by non-technical staff; submit attributable to the signed-in account.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Raise asset request form | UI | Medium | 6 |
| Request submit confirmation | UI | Simple | 2 |
| Submit asset request | API | Complex | 8 |
| Validate asset request | API | Medium | 6 |
| Store supporting attachment | API | Medium | 6 |
| Asset request records | DB | Medium | 4 |
| Raise asset request tests | Testing | Medium | 6 |
| Raise asset request implementation documentation | Documentation | Easy | 2 |

**Feature total: 40 hours**
