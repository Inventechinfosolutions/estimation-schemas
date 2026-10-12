# Auction Management System — Estimation Summary

Internal roll-up of feature totals. Hours are person-hours.

- Modules: **15**
- Features: **46**
- Grand total: **2171 hours**
- Recommended go-live: **2171 hours**
- Optional / conditional: **0 hours**

Both Evaluation = Yes and Evaluation = No are in the go-live total. Auctions that do not use evaluation still need the product to contain the evaluation path, because the creation flag is part of the confirmed scope.

## Per-module totals

| # | Module | Type | Features | Hours |
|---|--------|------|--------:|------:|
| 01 | Staff Access and Role Management | Shared | 4 | 165 |
| 02 | Category and Catalogue Management | Business | 5 | 246 |
| 03 | Bidder Registration and Profile | Business | 4 | 183 |
| 04 | Auction Creation | Business | 6 | 275 |
| 05 | Auction Review, Approval and Publication | Business | 2 | 104 |
| 06 | Corrigendum Management | Business | 2 | 95 |
| 07 | Auction Discovery and Participation | Business | 4 | 187 |
| 08 | Pre-Auction Query and Clarification | Business | 1 | 59 |
| 09 | Pre-Live Participation Evaluation | Business | 2 | 111 |
| 10 | Live Auction Bidding and Extension | Business | 3 | 175 |
| 11 | Live Auction Monitoring and Closure | Business | 3 | 107 |
| 12 | Results, Finalisation and Approval | Business | 3 | 164 |
| 13 | Award and Letter of Intent | Business | 3 | 129 |
| 14 | Notifications | Technical | 2 | 90 |
| 15 | Auction Status and History | Business | 2 | 81 |
|  | **Total** |  | **46** | **2171** |

## Hours by module type

- Shared: 165 hours
- Business: 1916 hours
- Technical: 90 hours

## Assumptions and risks carried forward

- EMD is fulfilment with a reference and proof. No payment gateway, refund, or forfeiture hours are included.
- Email is included. SMS, mobile applications, and post-letter contract or payment are not.
- Reserve price is stored and displayed. It does not auto-reject a bid.
- GST is a pricing-format flag. No tax engine is included.
- Bid-change price is an auction parameter because live validation needs it.
- Delta near-close window equals the delta length (15 or 30 minutes).
- Tied H1 or L1 is an explicit finalisation choice. Timestamp does not break the tie.
- Corrigendum, evaluation-list, and finalisation approvals are in the go-live scope.
- Concurrent live bidding is a delivery risk inside Module 10. Volumes were not in the source.
- Letter wording is an organisation dependency.

## Suggested next actions

1. Review module boundaries and the assumptions above.
2. Adjust any feature whose business rule should differ, then regenerate the roll-up and the client export.
3. Use the client Word export for commercial discussion. Keep this file internal.
