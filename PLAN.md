# Project Plan

## Current State

The app runs in Docker with four services: Flask (port 5000), data-API (port 4000), v1 visualization (port 3000), and PostgreSQL. Tableau has been removed; ECharts is the target visualization library. Authentication is functional but uses hardcoded credentials in `secret.py`. The database schema exists but is not connected to live data.

---

## Phase 1 — Stabilize (immediate)

- [ ] Resolve the dual app-factory problem: consolidate `main.py` and `__init__.py` into one entry point
- [ ] Move credentials out of `secret.py` into environment variables (`.env`)
- [ ] Connect `db.init_app` to a live PostgreSQL instance; run `db.create_all()` on startup
- [ ] Wire the data-API to the PostgreSQL database instead of returning hardcoded sample data
- [ ] Confirm all three services start cleanly with `docker compose up`

---

## Phase 2 — Core Features

- [ ] Replace the hardcoded `USERS_LIST` auth with database-backed user accounts (use `User` model + password hashing via Flask-Praetorian or Werkzeug)
- [ ] Build a Scrapy pipeline that ingests job postings into the `Job` table
- [ ] Expose real job data through `/api/data` and `/api/jobs` (counts by seniority, role, experience, remote status)
- [ ] Embed ECharts charts into the Flask `dashboard.html` template, fetching from the data-API
- [ ] Add Flask-Admin views for `User` and `Job` models so data can be inspected without raw SQL

---

## Phase 3 — Search & Exploration

- [ ] Implement the `Search` Flask-Meld component (`__init__.py`) — live search across `Job.title` and `Job.desc`
- [ ] Connect the v1 search UI (two-query compare input) to the data-API
- [ ] Add filtering to the data-API: by role, seniority, country, remote
- [ ] Surface results as side-by-side ECharts comparisons (demand, skills overlap, experience distribution)

---

## Phase 4 — Polish

- [ ] Add pagination and date-range filtering to the dashboard
- [ ] Write integration tests for the data-API routes
- [ ] Complete the GitHub Actions CI workflow (install, lint, test)
- [ ] Harden Docker setup for production (non-root user, gunicorn workers, health checks)
