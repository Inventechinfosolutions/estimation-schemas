# F02-001 — Create Dropdown Values

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Create Dropdown Values |
| **Module** | 02 — Dropdown Values |

### Description
Admin creates the text values that appear in two dropdowns: **asset type** on the raise-asset-request form, and **ticket category** on the raise-ticket form. There is no catalogue, inventory, or deactivate workflow — Admin adds a value and it shows in the matching dropdown.

### Business Objective
IT can put the right choices on the request and ticket forms without a software change.

### Actors
Maker: Admin. Applicant: User (selects a value on a form only). Approver: none.

### User Journey
1. Who creates: Admin.
2. How they create: Dropdown values screen → choose which dropdown (Asset type or Ticket category) → type the value → Add. The value is immediately available in that dropdown for users raising a request or ticket.
3. How they edit: This feature is create-only. Admin does not edit, deactivate, or maintain a catalogue of historical values.
4. How they send for approval: Submit/approval does not apply. Adding the value is the complete action.
5. How the approver sees pending items: There is no approver inbox.
6. How the approver decides: There is no approval decision on this feature.
7. How the maker sees history: Admin sees the current list of values on the same screen (what will appear in the dropdown). There is no separate history screen.
8. How the approver / auditor sees history: Same current list. There is no separate auditor role.

### Functional Capabilities
- Add a value to the Asset type dropdown
- Add a value to the Ticket category dropdown
- List current values so the Admin screen and the user dropdowns show the same set
- Users cannot add values

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Dropdown values screen | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create dropdown value | Easy |
| List dropdown values | Simple |

### Inputs
Which dropdown (Asset type / Ticket category), value text.

### Outputs
Value appears in the chosen dropdown on the raise form.

### Business Rules
- Empty value is refused.
- Duplicate value in the same dropdown is refused.
- User role cannot open this screen.
- Existing requests/tickets keep the value they stored at raise time even if Admin later adds more values.

### Validations
- Dropdown kind and value text mandatory.
- Duplicate in the same dropdown refused.

### Calculations
None.

### Workflow
No approval. Add is final.

### Search Requirements
None. The screen shows the current list for the selected dropdown.

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
Admin only for create. Users only see the values inside the raise-form dropdowns (F03-001, F04-001).

### Integrations
None.

### Dependencies
Module 01 (Admin role).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Create and list only — no edit, deactivate, history, or item-master catalogue.
- List dropdown values is billed here and reused by the raise forms; F03-001 and F04-001 do not rebill the lookup.

### Risks
A mistyped value stays in the dropdown until a later change; correction is out of this feature’s create-only scope.

### Non Functional Requirements
Add is attributable to the Admin account; user forms show new values without a software release.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Dropdown values screen | UI | Easy | 4 |
| Create dropdown value | API | Easy | 4 |
| List dropdown values | API | Simple | 2 |
| Dropdown value records | DB | Simple | 1 |
| Create dropdown values tests | Testing | Easy | 4 |
| Create dropdown values implementation documentation | Documentation | Simple | 1 |

**Feature total: 16 hours**
