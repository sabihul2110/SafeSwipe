<!-- SafeSwipe/backend/README.md -->

# SafeSwipe Backend

This is the FastAPI backend for SafeSwipe. It exposes the API that the frontend talks to, and will eventually serve the ML model's predictions.

## Status
Basic structure in place: a health-check endpoint, config module, and router pattern for future endpoints.

## Structure
```text
backend/
├── main.py           # App entry point — wires everything together
├── core/             # App-wide config/settings
└── routers/          # API endpoints, grouped by feature
```

## Stack
- Python 3
- FastAPI
- Uvicorn (dev server)

## Setup (placeholder — will be filled in once real code exists)
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```