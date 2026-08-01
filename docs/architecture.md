<!-- SafeSwipe/docs/architecture.md -->

# SafeSwipe — Architecture Documentation

## Purpose of this Document
This file is the single source of truth for how SafeSwipe is designed. It will be updated continuously as we make architectural decisions. Nothing goes into the codebase without first being reasoned about here.

## Status
Initialized — no architectural decisions made yet.

## Table of Contents (to be filled in as we go)
- [ ] System Overview
- [ ] High-Level Components
- [ ] Data Flow
- [x] Tech Stack Decisions
- [ ] Deployment Strategy


## Tech Stack Decisions

### Backend
- **FastAPI** (Python) — serves the API and, later, the ML model directly from the same backend.

### Frontend
- **React** — consumes the backend via REST API calls.

### ML / Data Pipeline
- **Python** (pandas, scikit-learn to start).
- Initial training data: a public Kaggle credit card fraud dataset (exact dataset to be confirmed when Umar's pipeline work begins). This is a static file used to train/evaluate the model — separate from the live application's database.

### Database
- **SQLite** for now, while the project is small and local.
- **PostgreSQL** planned once we're closer to a deployable version — decision to be revisited in `docs/architecture.md` when that time comes, not assumed today.

### Data Flow (high-level)

```text
Kaggle dataset (CSV) --> trains ML model (offline)
                                |
                                v
Live transaction --> FastAPI --> ML model predicts --> result + transaction stored in DB
                                |
                                v
                        React frontend displays result
```

## Change Log
| Date | Change | Author |
|---|---|---|
| _(01/08/2026)_ | Initial document created | Mohammad Sabihul Haque |
| _(01/08/2026)_ | Locked in tech stack: FastAPI, React, Python/Kaggle for ML, SQLite→Postgres | Mohammad Sabihul Haque |
