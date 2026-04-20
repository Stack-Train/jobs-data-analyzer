# Design

## User Flows

### Authentication
```
/ → redirect → /login (GET)
/login (POST) → validate credentials → /homepage
/logout → /login
```

### Dashboard browsing
```
/homepage → tile grid of available dashboards
tile click → /dashboard?dashboardName=<name>
/dashboard → full-page ECharts view for that dashboard
```

### Job search (v1 / future Flask-Meld)
```
Search input → live filter → chart re-render
Two-query mode → side-by-side comparison of two job roles
```

---

## Pages

### Login (`/login`)
Simple username/password form. Error message displayed inline on failure.

### Homepage (`/homepage`)
Grid of clickable dashboard tiles. Each tile shows a title, description, and thumbnail image. Tiles are populated via `createTiles()` in `mainScript.js` from a data array.

### Dashboard (`/dashboard`)
Full-page chart view. A `chartContainer` div (700px tall) is the target for ECharts. Charts are fetched from the data-API on page load. Currently renders four charts:

| Chart | Data source | Type |
|---|---|---|
| Skill market share | `/api/data` | Pie |
| Job demand by role | `/api/data` | Bar |
| Experience distribution | `/api/jobs` | Bar |
| Remote vs hybrid vs onsite | `/api/jobs` | Pie |

### v1 Visualization (`localhost:3000`)
Standalone Node.js app. Two text inputs let the user compare two job roles side-by-side. Sends XHR to `localhost:4000/api/data` and renders results into four ECharts containers.

---

## Chart Data Contract

The data-API returns ECharts-compatible option objects. Each endpoint returns an array of four option objects, one per chart container.

**`GET /api/data`** — demand and skill data  
**`GET /api/jobs`** — seniority, experience, and remote data

The frontend maps `response[index]` directly to `chart[index].setOption(...)`.

---

## Admin Interface

Flask-Admin (at `/admin`) provides CRUD views for `User` and `Job` models. Access should be restricted to users with the `Admin` role once database-backed auth is implemented.

---

## Auth Design

Current: in-memory list in `secret.py`.  
Target: `User` rows in PostgreSQL with hashed passwords. Session managed by Flask-Login. `Admin` subclass grants access to `/admin`.
