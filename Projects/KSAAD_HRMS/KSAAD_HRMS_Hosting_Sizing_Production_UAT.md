# KSAAD Digital Platform — KSDC Resource Request

**Load:** 7,000 institutions × 2 users + 5,000 employees = **19,000** named users · **1,500 / 2,000** concurrent  
**Data:** 7,000 × 500 MB/year = **3.5 TB/year** · **30 TB** object quota for 5 years  
**Stack:** Nginx (UI) · Redis · Node.js + PM2 cluster · MySQL · KSDC object store (bucket)

Each environment: **1 app VM** (Nginx + Redis + PM2) + **1 MySQL VM** + **object-store quota**.

---

## Production

| Resource | Qty | Specification |
|----------|----:|---------------|
| App VM | 1 | **32 vCPU · 64 GB RAM · 500 GB SSD** · Nginx + Redis + Node.js / PM2 cluster (`pm2 -i max`) |
| MySQL VM | 1 | **16 vCPU · 64 GB RAM · 2 TB NVMe** · MySQL 8 |
| Object store | 1 bucket | **30 TB usable** · S3 endpoint + credentials |
| Network | — | Access to object-store endpoint; 10 Gbps between VMs and object store preferred |

| Year | Object data (cumulative) |
|-----:|-------------------------:|
| 1 | 3.5 TB |
| 2 | 7.0 TB |
| 3 | 10.5 TB |
| 4 | 14.0 TB |
| 5 | 17.5 TB |
| **Quota requested** | **30 TB** (5 years + versioning + headroom) |

Thereafter: about **3.5 TB additional quota per year**.

---

## UAT

| Resource | Qty | Specification |
|----------|----:|---------------|
| App VM | 1 | **8 vCPU · 16 GB RAM · 300 GB SSD** · Nginx + Redis + Node.js / PM2 cluster |
| MySQL VM | 1 | **8 vCPU · 32 GB RAM · 500 GB SSD** · MySQL 8 |
| Object store | 1 bucket | **2–4 TB usable** · separate UAT bucket |

---

## Request checklist

| Environment | App VM | MySQL VM | Object-store quota |
|-------------|--------|----------|--------------------|
| Production | 32 vCPU / 64 GB / 500 GB SSD | 16 vCPU / 64 GB / 2 TB NVMe | 30 TB |
| UAT | 8 vCPU / 16 GB / 300 GB SSD | 8 vCPU / 32 GB / 500 GB SSD | 2–4 TB |
