<!-- SafeSwipe/docs/architecture.md -->

# SafeSwipe — Architecture Documentation

## Purpose of this Document
This file is the single source of truth for how SafeSwipe is designed. It will be updated continuously as we make architectural decisions. Nothing goes into the codebase without first being reasoned about here.

## Status
Initialized — no architectural decisions made yet.

## Table of Contents (to be filled in as we go)
- [x] System Overview
- [x] High-Level Components
- [x] Data Flow
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


## System Overview
SafeSwipe is split into three independent parts that talk to each other, not one big tangled app:
- **backend/** — the API layer. Everything else goes through this.
- **frontend/** — what the user actually sees and interacts with.
- **ml/** — trains the model that the backend uses to make predictions.

## High-Level Components
- **FastAPI backend** — receives transaction data, asks the ML model for a prediction, stores the result, sends it back.
- **React frontend** — sends transactions (real or simulated) to the backend, displays results.
- **ML pipeline** — offline process; trains a model on the Kaggle dataset, produces a model file the backend can load.


## Repository Structure

```text
SafeSwipe/
├── backend/        # FastAPI app — API and eventually the ML model serving
│   ├── core/        # App-wide config/settings
│   └── routers/     # API endpoints, grouped by feature
├── frontend/        # React app
├── ml/              # Data pipeline, training scripts, Kaggle dataset handling
├── docs/            # All documentation (this folder)
└── docs/private/    # Git-ignored, local-only notes
```

Each of these folders (`backend/`, `frontend/`, `ml/`) will get its own README once real work starts inside it, explaining what's there and how to run it.


## Deployment Strategy
Not decided yet. To be filled in once the app is functional end-to-end locally. Will cover hosting for backend, frontend, and how the trained model gets deployed alongside the API.


## Change Log
Detailed history moved to `docs/private/changelog.md` (git-ignored). Last updated: 2026-08-02.
