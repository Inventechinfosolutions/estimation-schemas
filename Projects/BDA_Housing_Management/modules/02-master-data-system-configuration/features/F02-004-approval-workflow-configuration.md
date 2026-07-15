# F02-004 — Approval Workflow Configuration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-004 |
| **Feature Name** | Approval Workflow Configuration |
| **Module** | 02 — Master Data & System Configuration |

### Description
Configure multi-level approval definitions by housing process type. Each approval level maps to one or more **Posts** (not directly to persons). At runtime, the incumbent Person on the mapped Post acts on the work item.

### Business Objective
Enable BDA to adapt approval routes while preserving post-based accountability.

### Actors
Super Administrator; section administrator; Auditor.

### User Journey
Administrator selects a process type, adds and orders any number of levels, maps eligible **Posts** (from F01-003) to each level, defines allowed actions, and activates the configuration.

### Functional Capabilities
- Process workflow definition; level ordering/rearrangement  
- **Post mapping per approval level** (one or more Posts per level)  
- Actions: Approve, Reject, Send Back, Hold, Reassign, Delegate, Request Clarification  
- Version history of configuration  
- Runtime worklist resolves to incumbent Person on the target Post  

### Inputs
Process type, levels, sequence, eligible Post(s), action set, status.

### Outputs
Active approval definition and configuration history.

### Business Rules
- Only one active definition per process type/version.  
- Level sequence must be complete.  
- Approver identity is the Person currently mapped to the Post (F01-001); vacant Posts produce routing exception/pending queue.  
- Runtime approvals occur in owning business modules.  
- Reassign/Delegate may target another eligible Post where configured.

### Validations
Process and level required; active Posts only; no duplicate sequence; action set required.

### Calculations
None.

### Workflow
Draft workflow → map Posts to levels → validate → activate → business feature invokes configured Post route.

### Search Requirements
Process type, status, level count, mapped Post, effective date.

### Documents
None.

### Reports
Approval Workflow Configuration Register (with Post mappings).

### Notifications
Optional notice to Posts/incumbents on significant route change.

### Security
Administrator-only changes; configuration audit; SoD checks apply via F01-007.

### Integrations
Internal workflow routing handoff — Post-based (Simple).

### Dependencies
F01-002; F01-003; F01-001; F01-007.

### Assumptions
This is configuration, not a standalone BPM product. Person↔Post occupancy is maintained in Module 01.

### Risks
Mapping approvals to vacant Posts delays turnaround until occupancy is fixed.

### Non Functional Requirements
Predictable Post-based routing; configuration version auditability.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Workflow configuration register | UI | Complex | 8 |
| Multi-level workflow builder | UI | Very High | 16 |
| Post-to-level mapping editor | UI | Complex | 8 |
| Workflow definition + Post routing ops | API | Very High | 16 |
| Workflow definition persistence | Database | Complex | 6 |
| Workflow routing handoff (Post-based) | Integration | Simple | 4 |
| Workflow configuration tests | Testing | Very High | 12 |
| Workflow configuration guide | Documentation | Complex | 4 |
| **Total** | | | **74** |

### Estimation Assumptions
- Uses Estimation Master values only.  
- Person–Post occupancy UI remains in F01-001.  
