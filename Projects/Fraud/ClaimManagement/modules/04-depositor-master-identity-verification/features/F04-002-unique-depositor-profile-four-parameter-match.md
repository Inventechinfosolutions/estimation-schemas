# F04-002 — Unique depositor profile (four-parameter match)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Unique depositor profile (four-parameter match) |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
When the Officer saves a new depositor or claim identity, the system matches on the four Authority-defined parameters. If a match exists, the Officer is shown the existing profile and continues on that record (including additional FEs). If not, the Officer confirms creation of a new unique profile used across all FEs.

### Business Objective
Keep one depositor identity across FEs, schemes, branches and investments using four matching parameters.

### Actors
Officer; assisting staff.

### User Journey
1. Who creates: Officer
2. How they create: Officer enters identity particulars and saves a new depositor or claim identity.
3. How they edit: The system matches on the four Authority-defined parameters.
4. How they send for approval: If a match exists, Officer is shown the existing profile and continues on that record, including additional FEs. Enter identity → match → continue existing or confirm new. No generative identity inventing.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. If not, Officer confirms creation of a new unique profile used across all FEs.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Four-parameter match on save.
- Present existing profile and block silent duplicates.
- Allow the same profile to be used across additional imported FEs.
- Create a new unique profile only on Officer confirmation when no match exists.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Match-result and existing-profile screen | Complex |
| New-profile confirmation (match gate) | Medium |
| Unique depositor profile history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Four-parameter match operations | Very High |
| Update unique depositor profile | Medium |
| Search unique depositor profile | Medium |
| Read unique depositor profile history | Easy |

### Inputs
Four Authority-defined match parameters and related identity fields; imported FE when associating.

### Outputs
Existing or newly confirmed unique depositor profile.

### Business Rules
- A single depositor profile exists across FEs.
- The four parameters are Authority-confirmed (source requires four but does not name them).
- Officer continues on the matched record rather than creating a parallel profile.

### Validations
- Match parameters required on save.
- Unconfirmed create is refused when a match is presented.

### Calculations
Match score / exact match on the four parameters as the Authority defines.

### Workflow
Enter identity → match → continue existing or confirm new. No generative identity inventing.

### Search Requirements
The four parameters, unique profile ID, name, imported FE associations.

### Documents
Identity papers sit on F04-010 / claim pack; this feature is the profile identity.

### Reports
Potential-duplicate match log for Officers.

### Notifications
On-screen match result.

### Security
Profile search is need-to-know. Creating a profile is attributable to Person in Post.

### Integrations
None (internal match).

### Dependencies
F02-001 when associating FE; F04-003 KYC fields feed the profile.

### Assumptions
- Authority will name the four matching parameters during implementation.

### Risks
- Unconfirmed parameters would delay unique-profile behaviour.
- Weak match rules would allow duplicate profiles and collusive claims.

### Non Functional Requirements
Keyword, unique ID and depositor-parameter queries are supported.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Match-result and existing-profile screen | UI | Complex | 12 |
| New-profile confirmation (match gate) | UI | Medium | 6 |
| Unique depositor profile history | UI | Medium | 6 |
| Four-parameter match operations | API | Very High | 16 |
| Update unique depositor profile | API | Medium | 6 |
| Search unique depositor profile | API | Medium | 6 |
| Read unique depositor profile history | API | Easy | 4 |
| Unique profile persistence | DB | Complex | 6 |
| Unique depositor profile (four-parameter match) feature tests | Testing | Very High | 12 |
| Unique depositor profile (four-parameter match) implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **77** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
