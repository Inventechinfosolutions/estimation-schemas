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
1. Officer enters identity particulars and saves a new depositor or claim identity.
2. The system matches on the four Authority-defined parameters.
3. If a match exists, Officer is shown the existing profile and continues on that record, including additional FEs.
4. If not, Officer confirms creation of a new unique profile used across all FEs.

### Functional Capabilities
- Four-parameter match on save.
- Present existing profile and block silent duplicates.
- Allow the same profile to be used across additional imported FEs.
- Create a new unique profile only on Officer confirmation when no match exists.

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
| Four-parameter match operations | API | Very High | 16 |
| Unique profile persistence | DB | Complex | 6 |
| Unique-profile match tests | Testing | Very High | 12 |
| Four-parameter match note | Documentation | Medium | 3 |
| **Total** | | | **55** |

### Estimation Assumptions
- Uses Estimation Master values only.
- KYC field capture screens are estimated in F04-003.
