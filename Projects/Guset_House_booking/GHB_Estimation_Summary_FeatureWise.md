# GHB — Feature-wise Estimation Summary (Internal)

**Project:** Guest House Booking and Access Management Platform  
**Project code:** GHB  
**As of:** 2026-09-22

## Grand totals

| Bucket | Hours |
|--------|------:|
| Recommended go-live | 1601 |
| Optional / conditional | 158 |
| All-in | 1759 |
| Features | 30 |
| Modules | 8 |

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | User Registration & Authentication | Shared | 4 | 226 | 14.1% |
| 02 | Site, Building & Room Configuration | Business | 4 | 240 | 15.0% |
| 03 | Booking & Room Allocation | Business | 5 | 256 | 16.0% |
| 04 | Online Payment Processing | Business | 3 | 152 | 9.5% |
| 05 | Access Credentials & Guest Check-in | Business | 5 | 254 | 15.9% |
| 06 | Administration, Monitoring & Reports | Business | 4 | 217 | 13.6% |
| 07 | Notification Service | Technical | 2 | 111 | 6.9% |
| 08 | Integration Hub | Technical | 3 | 303 | 18.9% |

## Feature-wise detail

### 01 — User Registration & Authentication

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F01-001 | Mobile OTP Registration | 40 | Go-live |
| F01-002 | Government Identity Submission | 77 | Go-live |
| F01-003 | Secure Login and Session Management | 46 | Go-live |
| F01-004 | Role and Permission Assignment | 63 | Go-live |

**Module subtotal: 226 hours**

### 02 — Site, Building & Room Configuration

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F02-001 | Site and Location Master | 54 | Go-live |
| F02-002 | Building and Floor Setup | 60 | Go-live |
| F02-003 | Room Catalogue and Pricing | 75 | Go-live |
| F02-004 | Heterogeneous Property Structures | 51 | Go-live |

**Module subtotal: 240 hours**

### 03 — Booking & Room Allocation

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F03-001 | Inventory Browse and Availability Search | 62 | Go-live |
| F03-002 | Booking Request with Conflict Prevention | 75 | Go-live |
| F03-003 | Booking Summary and Pricing Preview | 34 | Go-live |
| F03-004 | Automatic Room Allocation | 45 | Go-live |
| F03-005 | Booking Confirmation Record | 40 | Go-live |

**Module subtotal: 256 hours**

### 04 — Online Payment Processing

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F04-001 | Payment Checkout Initiation | 41 | Go-live |
| F04-002 | Payment Success Handling | 55 | Go-live |
| F04-003 | Payment Failure Retry and Status | 56 | Go-live |

**Module subtotal: 152 hours**

### 05 — Access Credentials & Guest Check-in

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F05-001 | Access Credential Generation | 44 | Go-live |
| F05-002 | Credential Delivery | 38 | Go-live |
| F05-003 | Self Check-in and Occupancy Tracking | 79 | Go-live |
| F05-004 | Optional Hardware Access Handoff | 62 | OPTIONAL / conditional |
| F05-005 | Manual Key Override Recording | 31 | Go-live |

**Module subtotal: 254 hours**

### 06 — Administration, Monitoring & Reports

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F06-001 | Operations Dashboard | 54 | Go-live |
| F06-002 | Administrative Master and User Controls | 31 | Go-live |
| F06-003 | Exceptional Booking Override | 67 | Go-live |
| F06-004 | Activity Revenue and Utilization Reports | 65 | Go-live |

**Module subtotal: 217 hours**

### 07 — Notification Service

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F07-001 | Notification Template Catalogue | 56 | Go-live |
| F07-002 | Notification Dispatch and Status | 55 | Go-live |

**Module subtotal: 111 hours**

### 08 — Integration Hub

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F08-001 | Payment Gateway Adapter | 130 | Go-live |
| F08-002 | Communication Service Adapter | 77 | Go-live |
| F08-003 | Access-Control Hardware Adapter | 96 | OPTIONAL / conditional |

**Module subtotal: 303 hours**


## Optional commercial line items

| Item | Hours | Notes |
|------|------:|-------|
| Access-control hardware enablement (F05-004 + F08-003) | 158 | Quote separately when sites have hardware |

## Effort profile — top features by hours

| Rank | Feature ID | Feature Name | Module | Hours |
|-----:|------------|--------------|--------|------:|
| 1 | F08-001 | Payment Gateway Adapter | Integration Hub | 130 |
| 2 | F08-003 | Access-Control Hardware Adapter | Integration Hub | 96 |
| 3 | F05-003 | Self Check-in and Occupancy Tracking | Access Credentials & Guest Check-in | 79 |
| 4 | F08-002 | Communication Service Adapter | Integration Hub | 77 |
| 5 | F01-002 | Government Identity Submission | User Registration & Authentication | 77 |
| 6 | F03-002 | Booking Request with Conflict Prevention | Booking & Room Allocation | 75 |
| 7 | F02-003 | Room Catalogue and Pricing | Site, Building & Room Configuration | 75 |
| 8 | F06-003 | Exceptional Booking Override | Administration, Monitoring & Reports | 67 |
| 9 | F06-004 | Activity Revenue and Utilization Reports | Administration, Monitoring & Reports | 65 |
| 10 | F01-004 | Role and Permission Assignment | User Registration & Authentication | 63 |

## Hours by type

| Type | Hours |
|------|------:|
| Business | 1119 |
| Shared | 226 |
| Technical | 414 |

## Indicative phasing

1. **Foundation:** Modules 01, 02, 07, 08 (partial — payment + comms adapters)  
2. **Booking core:** Modules 03, 04  
3. **Arrival & ops:** Modules 05 (core), 06  
4. **Optional:** F05-004, F08-003 hardware path  

## Exclusions (not in feature hours)

- Payment gateway merchant fees / SMS commercial costs  
- Access-control hardware supply and installation  
- Hosting, AMC, training delivery beyond basic documentation  
- Native mobile apps and central employee directory (future)  
- Legacy data migration  

## Reconciliation note (internal)

Hours rolled up from module `features/_index.md` totals and `GHB_Registry.json`.
