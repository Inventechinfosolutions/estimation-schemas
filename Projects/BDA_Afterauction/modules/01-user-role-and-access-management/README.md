# 01. User, Role & Access Management

Type: Shared
Summary: Staff login and sessions, user and role management, configurable permissions with DS-wise isolation, officer DSC registration.

- **Source:** Explicit (SOW §4.10, §4.12)
- **In Scope:** Staff authentication with OTP and lockout; user register; role assignment with DS office; permission matrix; DS-wise record isolation; DSC certificate registration and signing authority
- **Out of Scope:** Bidder login (Module 05); single sign-on with other BDA systems
- **Key Actors:** Super Admin; Auction Admin; all BDA roles
- **Dependencies:** F12-003 (OTP SMS / e-mail); F13-003 (DSC verification); F14-001 (audit)
- **Notes:** Access model User → Role → Permissions with DS-wise data isolation; bidders use a separate OTP login

Features: 4 · **515 hours** (see `features/_index.md`)
