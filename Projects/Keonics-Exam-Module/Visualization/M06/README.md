# Module 06 — Feature-wise Visualization Briefs

ChatGPT / LLM prompt briefs **per feature** for Examination Scheduling & Allocation.

**Parent module brief:** [`../M06_06-examination-scheduling-and-allocation_ChatGPT_Brief.md`](../M06_06-examination-scheduling-and-allocation_ChatGPT_Brief.md)  
**Source feature pack:** [`../../Feature_Specs/M06_examination-scheduling-and-allocation.md`](../../Feature_Specs/M06_examination-scheduling-and-allocation.md)

## How to use

1. Open the feature file you need.
2. Copy from `PROMPT START` to `PROMPT END`.
3. Paste into ChatGPT and ask for Mermaid diagrams.
4. If length-limited, use **Quick paste** at the bottom of the file.

## Features

| ID | Feature | File | Primary table |
|----|---------|------|---------------|
| F06-001 | Examination Schedule Creation and Maintenance | [`F06-001_examination-schedule-creation-and-maintenance_ChatGPT_Brief.md`](./F06-001_examination-schedule-creation-and-maintenance_ChatGPT_Brief.md) | `exam_session` |
| F06-002 | Candidate Centre and Session Allocation | [`F06-002_candidate-centre-and-session-allocation_ChatGPT_Brief.md`](./F06-002_candidate-centre-and-session-allocation_ChatGPT_Brief.md) | `candidate_allocation` |
| F06-003 | Candidate Seat and Computer Assignment | [`F06-003_candidate-seat-and-computer-assignment_ChatGPT_Brief.md`](./F06-003_candidate-seat-and-computer-assignment_ChatGPT_Brief.md) | `seat_assignment` |
| F06-004 | Digital Hall Ticket Generation and Candidate Access | [`F06-004_digital-hall-ticket-generation-and-candidate-access_ChatGPT_Brief.md`](./F06-004_digital-hall-ticket-generation-and-candidate-access_ChatGPT_Brief.md) | `hall_ticket` |
| F06-005 | Examination Credential Generation and Secure Distribution Handoff | [`F06-005_examination-credential-generation-and-secure-distribution-handoff_ChatGPT_Brief.md`](./F06-005_examination-credential-generation-and-secure-distribution-handoff_ChatGPT_Brief.md) | `exam_credential` |

## Pipeline (for orientation)

```text
F06-001 Schedule → F06-002 Allocation → F06-003 Seat → F06-004 Hall Ticket
                              ↘ F06-005 Credentials → Module 07 Notify
```
