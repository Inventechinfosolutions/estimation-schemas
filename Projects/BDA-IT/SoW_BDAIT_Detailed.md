# Statement of Work (SOW)

# Bangalore Development Authority (BDA)

# IT Asset Request and Helpdesk

**Document Type:** Statement of Work – Business Requirements  
**Version:** 1.0  
**Status:** Draft  
**Prepared by:** Bangalore Development Authority  

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Project Objectives](#3-project-objectives)
4. [In Scope / Out of Scope](#4-in-scope--out-of-scope)
5. [Solution Expectations](#5-solution-expectations)
6. [Consolidated Functional Modules](#6-consolidated-functional-modules)
7. [End-to-End Workflows](#7-end-to-end-workflows)
8. [Access Control](#8-access-control)
9. [Channels](#9-channels)
10. [Integrations](#10-integrations)
11. [Audit, Compliance & Security](#11-audit-compliance--security)
12. [Non-Functional Requirements](#12-non-functional-requirements)
13. [Data Migration](#13-data-migration)
14. [Phased Delivery](#14-phased-delivery)
15. [Deliverables](#15-deliverables)
16. [Acceptance Criteria](#16-acceptance-criteria)
17. [Expected Benefits](#17-expected-benefits)
18. [Assumptions & Dependencies](#18-assumptions--dependencies)
19. [Vendor Response Expectations](#19-vendor-response-expectations)
20. [Appendix A — Module & Feature Index](#20-appendix-a--module--feature-index)
21. [Appendix B — Key Entities](#21-appendix-b--key-entities)

---

## 1. Introduction

This Statement of Work (SOW) states the **business requirements** for a simple internal application for the **Bangalore Development Authority (BDA) IT function**. The application shall allow BDA users to **raise an asset request**, **raise a support ticket**, and **track the status** of both. An **Administrator** shall create all users, create the **dropdown values** used on request and ticket forms, and use a **simple dashboard** to monitor open and closed work.

Document handling (optional supporting attachment on a request or ticket) and status workflow are **embedded** in the business processes. They are not separate product modules.

This document is prepared for RFP discussion and internal estimation. It does not prescribe technology stack, APIs, database design, or screen layouts.

---

## 2. Project Overview

BDA IT needs a lightweight system of record for two everyday activities:

1. **Asset request** — a user asks IT for an asset (for example a laptop, desktop, printer, or similar item chosen from a dropdown).
2. **Support ticket** — a user reports an IT issue or service need.

Today these are typically handled through informal channels (email, phone, walk-in), which makes it hard to know what is open, what is closed, and who raised it.

The application shall be used only by **BDA employees** and **contract users**. There is **no person directory, post, or organisational-position model**. Each login is a **plain user account** with one of two roles: **User** or **Admin**.

### 2.1 Business Context

| Aspect | Description |
| ------ | ----------- |
| Organisation | Bangalore Development Authority (BDA) |
| Primary users | BDA employees and contract users (plain User role) |
| Administrator | BDA IT Admin who creates users, dropdown values, and tracks work |
| Primary outcomes | Logged asset requests and tickets with visible status |
| Access foundation | Username and password created and managed by Admin only |

### 2.2 Guiding Principles

1. Keep the product small: raise, track, and administer — nothing more in this phase.
2. Admin is the only party that creates accounts and sets or resets usernames and passwords.
3. Employee number is captured **only for employees**, never for contractors.
4. Admin-created dropdown values are the only choices on request and ticket forms (asset type and ticket category).
5. Users see **their own** requests and tickets. Admin sees **all**.
6. Status change by Admin is the operational workflow; there is no multi-level approval chain in this phase.

---

## 3. Project Objectives

1. Provide one internal place for BDA users to raise asset requests and IT tickets.
2. Let users see the current status of each request and ticket they have raised.
3. Enable Admin to create and maintain all BDA user accounts (employee and contractor).
4. Capture employee number for employees and omit it for contractors.
5. Enable Admin to create the dropdown values used while raising requests and tickets.
6. Give Admin a simple dashboard to see volumes and status of requests and tickets.
7. Keep access simple: User and Admin only; username and password managed solely by Admin.

---

## 4. In Scope / Out of Scope

### In Scope

- Internal web application covering the modules in Section 6.
- Two roles: **User** and **Admin**.
- Admin-managed user accounts for employees and contractors, including username and password.
- Admin option to create the values shown in asset-type and ticket-category dropdowns.
- Raise, view, and status-track for **asset requests** and **tickets**.
- Admin update of request and ticket status (so tracking is meaningful).
- Simple Admin dashboard for request and ticket tracking.
- Optional supporting attachment on a request or ticket (embedded; not a standalone document-management product).
- Basic audit of who created or changed a user, request, ticket, dropdown value, or status.

### Out of Scope

- Person master, post / position master, person-to-post mapping, or any organisational-hierarchy access model.
- User self-registration, self-service password change, or forgot-password / OTP login.
- Full IT asset inventory, stock, barcode/QR asset tagging, allocation register, or return / scrap lifecycle.
- Item / catalogue master product (edit, deactivate, history, nested catalogues).
- Purchase, tender, vendor management, or invoice processing for assets.
- Citizen / public portal, mobile native apps, or kiosk channel.
- Email, SMS, WhatsApp, or other outbound notifications (status is visible in the application).
- Active Directory / LDAP / single sign-on.
- Multi-level approval (maker–checker) of requests or tickets.
- Knowledge base, SLA clocks, escalation matrix, or call-centre telephony.
- Legacy data migration.
- Hosting, hardware, network, and AMC of IT assets themselves.
- Detailed technical architecture, API contracts, database schemas, class diagrams, and UI wireframes (design stage).

---

## 5. Solution Expectations

- Admin creates every login before a user can work.
- Users work with a short, guided form to raise a request or ticket, then a list/detail view to see status.
- Admin works from a dashboard and registers to filter, open, and update status.
- Asset type and ticket category on raise forms are dropdowns whose values Admin has created.
- The application is the system of record for asset requests and tickets raised through it.
- Language and labels remain simple and suitable for non-technical BDA staff.

---

## 6. Consolidated Functional Modules

### 01. User Account and Access Management

**Purpose:** Let Admin create and control every BDA login as a plain User or Admin account, without person or post records.

**Type:** Shared

**Functional requirements:**

- Admin creates accounts for **employees** and **contract users**.
- For an **employee**, Admin captures **employee number** (mandatory and unique among employees).
- For a **contractor**, employee number is **not captured**.
- Admin sets **username** and **password** at creation and may reset or change them later. Users cannot create, change, or recover credentials themselves.
- Admin assigns exactly one role: **User** or **Admin**.
- Admin can activate, disable, and edit account profile fields (name, user type, contact as captured).
- A valid username and password grants access to the functions of that role.

**Acceptance criteria:**

- An employee account cannot be saved without employee number; a contractor account cannot store an employee number.
- A user cannot log in until Admin has created the account and set credentials.
- A disabled account cannot log in.
- Users have no screen or action to change username or password.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Employee and contractor accounts | Admin creates and maintains BDA users; employee number only for employees |
| F01-002 | Username and password administration | Admin sets, resets, and changes credentials; users have no self-service |
| F01-003 | Login and role session | User or Admin signs in with Admin-issued credentials and sees only their role’s functions |
| F01-004 | Account enable and disable | Admin activates or disables an account so access can be withdrawn without deleting history |

---

### 02. Dropdown Values

**Purpose:** Let Admin create the values that appear in the asset-type and ticket-category dropdowns. Nothing more.

**Type:** Business

**Functional requirements:**

- Admin adds values for the **Asset type** dropdown used on the raise-asset-request form.
- Admin adds values for the **Ticket category** dropdown used on the raise-ticket form.
- Users only select from those dropdowns; they cannot create values.
- There is no item catalogue, inventory, edit/deactivate workflow, or master-history product in this module.

**Acceptance criteria:**

- After Admin adds a value, it appears in the matching dropdown on the raise form.
- A request or ticket cannot be raised without selecting a dropdown value.
- Users have no screen to create dropdown values.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Create dropdown values | Admin adds the values shown in asset-type and ticket-category dropdowns |

---

### 03. Asset Request Management

**Purpose:** Let a User raise an asset request and track its status; let Admin process and update that status.

**Type:** Business

**Functional requirements:**

- A logged-in User raises an asset request by selecting an asset type from the Admin-created dropdown, plus a short business description and optional supporting attachment.
- The system records requester, date/time, selected asset type, description, and initial status (for example **Open**).
- The User can view a list and detail of **their own** asset requests and the current status of each.
- Admin can view **all** asset requests, filter by status and date, open a request, add an internal remark, and change status (for example **Open**, **In progress**, **Closed**, **Rejected**).
- A User cannot change status; they only raise and track.

**Acceptance criteria:**

- A User never sees another user’s asset requests.
- Status is visible to the requester after Admin updates it.
- A request cannot be raised without the mandatory dropdown selection and description.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Raise asset request | User submits an asset request using the asset-type dropdown |
| F03-002 | User status tracking for asset requests | User lists and opens own requests and sees current status |
| F03-003 | Admin processing of asset requests | Admin reviews all requests, adds a remark, and updates status |

---

### 04. Ticket Management

**Purpose:** Let a User raise an IT support ticket and track its status; let Admin process and update that status.

**Type:** Business

**Functional requirements:**

- A logged-in User raises a ticket by selecting a ticket category from the Admin-created dropdown, plus a short problem description and optional supporting attachment.
- The system records requester, date/time, category, description, and initial status (for example **Open**).
- The User can view a list and detail of **their own** tickets and the current status of each.
- Admin can view **all** tickets, filter by status and date, open a ticket, add an internal remark, and change status (for example **Open**, **In progress**, **Closed**).
- A User cannot change status; they only raise and track.

**Acceptance criteria:**

- A User never sees another user’s tickets.
- Status is visible to the requester after Admin updates it.
- A ticket cannot be raised without the mandatory dropdown selection and description.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Raise ticket | User submits an IT ticket using the ticket-category dropdown |
| F04-002 | User status tracking for tickets | User lists and opens own tickets and sees current status |
| F04-003 | Admin processing of tickets | Admin reviews all tickets, adds a remark, and updates status |

---

### 05. Admin Dashboard

**Purpose:** Give Admin a simple operational view of asset requests and tickets so open work is visible without opening each register blindly.

**Type:** Business

**Functional requirements:**

- After Admin login, a dashboard shows counts of asset requests and tickets by status (at least Open, In progress, Closed; plus Rejected for requests if used).
- Dashboard provides a short list of recent or open items with a path to the full request or ticket.
- Admin can filter the dashboard (or linked registers) by type (request vs ticket), status, and date range.
- Users do **not** receive this dashboard; they use their own request and ticket lists only.

**Acceptance criteria:**

- Counts match the underlying request and ticket records for the same filters.
- Admin can move from a dashboard figure or row to the related record.
- A User login does not show Admin dashboard widgets or all-user data.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Request and ticket snapshot | Admin sees counts and a simple list of requests and tickets by status |
| F05-002 | Dashboard filters | Admin filters the operational view by type, status, and date |

---

## 7. End-to-End Workflows

### 7.1 Admin creates a user

1. Admin opens user administration.
2. Admin chooses **Employee** or **Contractor**.
3. For Employee, Admin enters employee number and profile details; for Contractor, Admin enters profile details without employee number.
4. Admin assigns role (User or Admin), sets username and password, and saves.
5. The person can sign in with those credentials. They cannot change them.

### 7.2 User raises an asset request

1. User signs in.
2. User opens **Raise asset request**, selects an asset type from the dropdown, enters description, optionally attaches a file, and submits.
3. The request is stored as **Open** and appears in the user’s status list.
4. Admin sees it on the dashboard / request register, acts, and updates status.
5. User opens the same request and sees the new status.

### 7.3 User raises a ticket

1. User signs in.
2. User opens **Raise ticket**, selects a ticket category from the dropdown, enters description, optionally attaches a file, and submits.
3. The ticket is stored as **Open** and appears in the user’s status list.
4. Admin sees it on the dashboard / ticket register, acts, and updates status.
5. User opens the same ticket and sees the new status.

### 7.4 Admin monitors work

1. Admin signs in and lands on (or opens) the dashboard.
2. Admin reviews counts and open items.
3. Admin opens a request or ticket, adds a remark if needed, and sets status to In progress or Closed (or Rejected for an asset request).

There is **no** separate document-management workflow and **no** multi-step approval in these paths.

---

## 8. Access Control

Access is **user → role**. There is no person, post, or unit hierarchy.

| Role | Who | What they can do |
| ---- | --- | ---------------- |
| User | BDA employee or contractor with a User account | Raise asset request; raise ticket; view status of own requests and tickets |
| Admin | BDA IT administrator | All User functions plus: create/edit/disable users; set and reset username and password; create dropdown values; view and update all requests and tickets; use the dashboard |

Rules:

- Permissions are granted only through the role on the account.
- A user has one role at a time.
- Username and password are never editable by the User role.
- Cross-user visibility of requests and tickets is Admin-only.

---

## 9. Channels

| Channel | In scope | Notes |
| ------- | -------- | ----- |
| Internal web application | Yes | Responsive enough for common office browsers; used by User and Admin |
| Citizen / public portal | No | BDA staff and contractors only |
| Native mobile application | No | Not in this phase |
| Email / SMS as a working channel | No | Tracking is in-application |

---

## 10. Integrations

No external system integrations are in scope for this phase.

| System | Status |
| ------ | ------ |
| HR / payroll (employee number validation) | Out of scope — Admin enters employee number; no live HR feed |
| Active Directory / email / SMS gateways | Out of scope |
| Asset / inventory / procurement systems | Out of scope |

If BDA later requires HR validation or notifications, that is a separate change.

---

## 11. Audit, Compliance & Security

- Record who created and last changed users, dropdown values, requests, tickets, and status, with date and time.
- Do not allow Users to alter credentials or other users’ records.
- Store passwords in a protected form (not recoverable as plain text by other Users). Admin reset is the recovery path.
- Optional attachments are stored against the request or ticket and are visible to the requester and to Admin only.
- The application is for internal BDA use; internet exposure, if any, must follow BDA IT security practice (hosting detail is outside this SOW).

---

## 12. Non-Functional Requirements

- Usable by non-technical staff with short, labelled forms and clear status words.
- Typical office concurrent use (BDA IT scale — tens to low hundreds of users, not a public portal).
- Reasonable page response for list, form, and dashboard views on BDA office network.
- Availability aligned to normal office hours unless BDA specifies otherwise at hosting time.
- Browser-based; no thick client.
- Simple operational backup and restore as part of hosting (hosting itself is out of feature scope).

---

## 13. Data Migration

**Out of scope.** The application starts empty except for Admin-created users and dropdown values. Historical email or paper requests and tickets are not loaded.

---

## 14. Phased Delivery

**Single phase (Phase 1)** covering all modules in Section 6.

There is no Phase 2 in this SOW. Items listed as out of scope (notifications, SSO, inventory, approvals, migration) are not implied as a later phase unless BDA issues a separate instruction.

---

## 15. Deliverables

1. Internal web application implementing modules 01–05.
2. Admin ability to create initial Admin and User accounts and dropdown values.
3. User and Admin operating guidance (short how-to, not a training programme).
4. This SOW as the functional baseline for acceptance of Phase 1 scope.

---

## 16. Acceptance Criteria

Program-level acceptance is met when:

1. Admin can create employee and contractor users; employee number is mandatory only for employees.
2. Only Admin can set or reset username and password; a User cannot change credentials.
3. Admin can create asset-type and ticket-category dropdown values; Users pick only from those dropdowns.
4. A User can raise an asset request and a ticket and see status of their own records only.
5. Admin can see all requests and tickets, update status, and use the dashboard counts and lists.
6. Disabled users cannot log in; audit of create/change on core records is available to Admin.

---

## 17. Expected Benefits

- One place to raise and see IT asset requests and tickets.
- Admin visibility of open versus closed work.
- Controlled access without a heavy HR/post model.
- Dropdown values that IT can add as asset types and issue categories change.

---

## 18. Assumptions & Dependencies

1. Organisation is Bangalore Development Authority; users are BDA employees and contractors only.
2. Project code for artefacts is **BDAIT**; display name is **IT Asset Request and Helpdesk**.
3. Access model is User / Admin only — no person or post — as instructed.
4. Admin will update request and ticket status; without that, user status tracking cannot change after submit.
5. Status set is simple (Open / In progress / Closed, plus Rejected for asset requests). BDA may rename labels at configuration time without changing the model.
6. No email/SMS, SSO, HR integration, or data migration in Phase 1.
7. Optional attachment is a single supporting file per request or ticket, not a full DMS.
8. Hosting, SSL, backup operations, and BDA network access are provided by BDA / nominated host; they are not estimated as application features.
9. “Asset request” means a request **to IT for an asset**, not an enterprise fixed-asset register.
10. One Admin role is sufficient; there is no separate helpdesk-agent role distinct from Admin in this phase.

---

## 19. Vendor Response Expectations

Vendors / implementing partners should:

1. Confirm understanding of the two-role model and Admin-only credential management.
2. Confirm in-scope versus out-of-scope boundaries in Section 4 without adding inventory, SSO, or notification scope unless priced separately.
3. Describe, in business terms, how users will raise and track requests and tickets and how Admin will use the dashboard.
4. Identify any dependency on BDA (initial Admin user, hosting, employee-number format) that would block go-live.
5. Not treat this SOW as a technical design; detailed design follows after scope confirmation.

---

## 20. Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | User Account and Access Management | Shared | F01-001 … F01-004 (4) |
| 02 | Dropdown Values | Business | F02-001 (1) |
| 03 | Asset Request Management | Business | F03-001 … F03-003 (3) |
| 04 | Ticket Management | Business | F04-001 … F04-003 (3) |
| 05 | Admin Dashboard | Business | F05-001 … F05-002 (2) |

**Total:** 5 modules, 13 feature outlines.

Slugs (for later folder naming): `user-account-and-access-management`, `dropdown-values`, `asset-request-management`, `ticket-management`, `admin-dashboard`.

---

## 21. Appendix B — Key Entities

| Entity | Meaning |
| ------ | ------- |
| User account | Login for an employee or contractor; role User or Admin |
| Employee number | Identifier captured only when user type is Employee |
| Asset request | User-submitted request for an IT asset, with status |
| Ticket | User-submitted IT support ticket, with status |
| Dropdown value | Text Admin created for the Asset type or Ticket category dropdown |

---

**End of Statement of Work**
