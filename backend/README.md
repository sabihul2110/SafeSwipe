<!-- SafeSwipe/backend/README.md -->

# SafeSwipe Backend

This is the FastAPI backend for SafeSwipe. It exposes the API that the frontend talks to, and will eventually serve the ML model's predictions.

## Status
Basic structure in place: a health-check endpoint, config module, and router pattern for future endpoints.

## Structure
```text
backend/
├── main.py           # App entry point — wires everything together
├── core/              # App-wide config/settings, database connection
├── routers/           # HTTP layer — receives requests, calls services
├── services/          # Business logic (e.g. fraud rules)
├── repositories/       # Database queries only, no business logic
├── models/             # SQLAlchemy database table definitions
└── schemas/            # Pydantic request/response shapes
```

## Layering convention
Each layer only talks to the one directly below it:
`routers` → `services` → `repositories` → `models`

Routers never touch the database directly. Services never know about HTTP. Repositories never make business decisions. This keeps each piece easy to test and replace on its own — e.g. swapping the placeholder fraud rule for a real ML model only touches `services/`.

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