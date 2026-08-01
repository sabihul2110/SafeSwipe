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

### `POST /transactions/check`
Accepts a transaction and returns a fraud verdict.

**Request body:**
```json
{
  "amount": 100.0,
  "merchant": "Some Store"
}
```

**Response:**
```json
{
  "is_fraud": false,
  "reason": "No issues detected (placeholder rule, not real ML)"
}
```

**Note:** The fraud check is currently a placeholder rule (flags amounts over 50000), not a real ML model. This will be replaced once Umar's pipeline produces a trained model.

## Conventions
- All new endpoints go in `backend/routers/`, grouped by feature (e.g. `transactions.py`, `predictions.py`).
- This document should be updated in the same commit/PR that adds or changes an endpoint.