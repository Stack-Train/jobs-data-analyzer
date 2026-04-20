# Architecture

## Services

```
┌──────────────────────────────────────────────────────────┐
│  docker compose                                          │
│                                                          │
│  ┌───────────────┐        ┌──────────────────────────┐  │
│  │  flask  :5000 │        │  data-api          :4000 │  │
│  │  (Python)     │        │  (Node.js/Express)       │  │
│  └──────┬────────┘        └──────────────┬───────────┘  │
│         │                                │              │
│         └──────────────┬─────────────────┘              │
│                        ▼                                 │
│               ┌────────────────┐                        │
│               │  db      :5432 │                        │
│               │  (PostgreSQL)  │                        │
│               └────────────────┘                        │
└──────────────────────────────────────────────────────────┘
         ▲                        ▲
         │ browser                │ external clients
         │ (HTML + auth)          │ (JSON API)
```

| Service | Image | Port | Entry point |
|---|---|---|---|
| `flask` | python:3.11-slim | 5000 | `flask run` → `JDA-12/main.py` |
| `data-api` | node:18-alpine | 4000 | `JDA-12/data-API/bin/www` |
| `db` | postgres:15-alpine | 5432 | — |

---

## Flask Application (`JDA-12/`)

Two app definitions exist today (known issue — to be consolidated):

| File | App variable | Used by |
|---|---|---|
| `main.py` | `app` | `flask run`, direct execution |
| `__init__.py` | `jda` | `FLASK_APP=JDA-12` (Docker) |

### `__init__.py` initialization order
1. Create `jda = Flask(__name__)`
2. Import models (`db = SQLAlchemy()` defined there)
3. Configure `SQLALCHEMY_DATABASE_URI`, call `db.init_app(jda)`
4. Initialize `Api`, `Admin`, `LoginManager` with `jda`
5. Define `Search` Flask-Meld component
6. Import and register `views.bp` blueprint

### Request lifecycle
```
Request → Flask router → views.bp route handler
                       → renders Jinja2 template
                         (templates/ directory)
```

### Module responsibilities

| Module | Responsibility |
|---|---|
| `main.py` | Standalone app: login, homepage, dashboard routes + in-memory auth |
| `__init__.py` | App factory: extension setup, blueprint registration |
| `views.py` | Blueprint routes: `/`, `/dashboard`, `/hello` |
| `models.py` | SQLAlchemy models + `db` instance |
| `config.py` | Reads env vars into Flask config keys |
| `secret.py` | Hardcoded `SECRET_KEY`, `USERS_LIST`, `PASSWORD_LOGIN` (temporary) |

---

## Data API (`JDA-12/data-API/`)

Stateless Express app. Currently returns static sample data; target is to query PostgreSQL.

```
GET /api/data  →  demand + skills data (array of 4 ECharts option objects)
GET /api/jobs  →  seniority, experience, remote breakdown
```

Configuration via `config/project.js` (reads `DB_HOST`, `DB_USER`, `PG_LOCAL_URI` from env).

---

## Database Schema

Defined in `models.py` via SQLAlchemy:

```
User
  id          INTEGER PK
  username    VARCHAR(80) UNIQUE NOT NULL
  email       VARCHAR(120) UNIQUE NOT NULL

Admin (inherits User)

Job
  id            INTEGER PK
  title         VARCHAR(250)
  desc          VARCHAR(250)
  position      VARCHAR(250)
  skill_lvl     VARCHAR(250)
  yrs_exp       INTEGER
  company       FLOAT UNIQUE
  num_applied   FLOAT
  date_posted   DATE
```

---

## Data Ingestion

`spider.py` at the project root is a Scrapy spider intended to crawl job postings and populate the `Job` table. Not yet wired into a pipeline.

---

## Environment Variables

| Variable | Used by | Purpose |
|---|---|---|
| `SECRET_KEY` | Flask | Session signing |
| `PG_LOCAL_URI` | Flask, data-API | PostgreSQL connection (local/Docker) |
| `PG_REMOTE_URI` | Flask | PostgreSQL connection (remote) |
| `PORT` | data-api | Listening port (default 4000) |
| `DATA_API_URL` | Flask (passed to browser) | Base URL the browser uses to reach the data-api |
