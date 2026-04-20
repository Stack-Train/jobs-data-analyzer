# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Jobs Data Analyzer (JDA) is a Flask web platform for visualizing jobs market data. It provides a Node.js REST API for job statistics served as ECharts-compatible JSON.

## Running the Application

**Docker (recommended):**
```bash
cp .env.example .env   # fill in secrets
docker compose up --build
```

**Flask app (primary):**
```bash
flask run --debug
# or specify the app module explicitly
flask run --app JDA-12:jda
# production
gunicorn JDA-12:jda
waitress-serve --host 127.0.0.1 JDA-12:jda
```

**Node.js data API (port 4000):**
```bash
cd JDA-12/data-API && npm start
```

**Node.js v1 visualization:**
```bash
cd JDA-12/v1 && npm start
```

## Running Tests

```bash
python tests/__init__.py
```

Tests live in `tests/backend/`, `tests/frontend/`, and `tests/unit/`. Many are incomplete (marked TODO).

## Architecture

### Flask Application (`JDA-12/`)

- **`main.py`** — standalone Flask app with login/logout/dashboard routes and in-memory auth via `secret.py`. Used when running directly.
- **`__init__.py`** — alternative app factory that uses Flask-RESTx, Flask-Admin, Flask-Meld, and SQLAlchemy. Exports `jda`. Used by `docker compose` (`FLASK_APP=JDA-12`).
- **`views.py`** — Blueprint with routes registered into the `__init__.py` app factory.
- **`models.py`** — SQLAlchemy models: `User`, `Admin`, `Job`. Defines `db = SQLAlchemy()` initialized via `db.init_app(jda)` in `__init__.py`.
- **`config.py`** — loads environment variables for Flask config (`SECRET_KEY`, `PG_LOCAL_URI`, `PG_REMOTE_URI`).
- **`secret.py`** — hardcoded in-memory user list and password (should migrate to env vars).

### Data Flow

1. User authenticates via the login form (credentials checked against `secret.py`'s `USERS_LIST`).
2. `/homepage` lists available dashboards.
3. `/dashboard` renders the dashboard page with an ECharts container.
4. The Node.js data API (`data-API/app.js`) serves `/api/data` and `/api/jobs` with job market statistics.

### Node.js Components

- **`JDA-12/data-API/`** — Express API returning sample job stats (demand, seniority, experience data) formatted for ECharts.
- **`JDA-12/v1/`** — Standalone Express app that renders ECharts visualizations directly.

## Configuration

Environment variables (set in `.env`, loaded by `config.py`):
- `SECRET_KEY` — Flask session secret
- `PG_LOCAL_URI` — local PostgreSQL connection string
- `PG_REMOTE_URI` — remote PostgreSQL connection string

## Key Dependencies

**Python:** Flask, Flask-Login, Flask-Admin, Flask-RESTx, Flask-SQLAlchemy, Flask-Meld, Scrapy, pendulum, boto3, gunicorn, waitress  
**Node.js:** Express, ECharts, morgan, dotenv  
**Database:** PostgreSQL via SQLAlchemy

## CI/CD

GitHub Actions at `.github/workflows/main.yml` triggers on push to `dev`, `JDA-11`, `JDA-12` branches and on a weekly schedule (Monday 9 AM UTC). The workflow is incomplete.

## Known Issues

- `JDA-12/README.md` contains an unresolved merge conflict (`<<<<<<< HEAD`).
- `main.py` and `__init__.py` both define the Flask app — inconsistent entry points.
- Credentials in `secret.py` are hardcoded instead of using environment variables.
