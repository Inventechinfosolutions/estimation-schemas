# 03. KPPP Result Intake & Site Package

Type: Business
Summary: KPPP API receipt, controlled report upload, matching and exceptions, CDRMS site package, locking and versioned re-import.

- **Source:** Explicit (SOW §4.1)
- **In Scope:** Result intake by API or upload; site matching; exception queue; read-only site package; integrity lock; re-import with approval
- **Out of Scope:** Any live bidding or pre-auction activity on KPPP
- **Key Actors:** System; Auction Admin; Result Verifier
- **Dependencies:** F13-001; F02-006; KPPP and CDRMS access
- **Notes:** Upload route ensures scope is not blocked if the KPPP API is unavailable

Features: 5 · **502 hours** (see `features/_index.md`)
