# 01. Administrator Access & Role Management

Type: Shared
Summary: Admin sign-in and session security, user management, configurable role permissions, audit log.

- **Source:** Explicit (Proposal §20, §22; FR-14, FR-20)
- **In Scope:** Admin authentication, password policy, lockout, reset; user invite and lifecycle; role-permission matrix; audit log with field-level diff
- **Out of Scope:** Public visitor accounts; SSO; MFA (future option)
- **Key Actors:** Super Administrator; Catalogue Administrator; Catalogue Reviewer; Content Administrator
- **Dependencies:** F06-005 (email connector); F13-002 (rate limiting)
- **Notes:** Access model User → Role → Permissions; four default roles seeded

Features: 4 · **397 hours** (see `features/_index.md`)
