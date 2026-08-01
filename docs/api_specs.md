<!-- SafeSwipe/docs/api_specs.md -->

# SafeSwipe — API Specifications

## Status
Early — only basic endpoints exist so far. This will grow as real features are added.

## Base URL (development)
`http://localhost:8000`

## Endpoints

### `GET /`
Returns a basic status message confirming the backend is running.

### `GET /health`
Returns `{ "status": "ok" }`. Used to confirm the backend is reachable — e.g. by the frontend or monitoring later.

## Conventions
- All new endpoints go in `backend/routers/`, grouped by feature (e.g. `transactions.py`, `predictions.py`).
- This document should be updated in the same commit/PR that adds or changes an endpoint.