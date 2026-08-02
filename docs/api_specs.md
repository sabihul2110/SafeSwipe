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

**Note:** This endpoint uses a placeholder rule (flags amounts over 50000), not the real ML model. Kept as a simple demo. See `/samples` and `/samples/{id}/predict` below for the real model.

Every checked transaction is now saved to the database (SQLite for now), including the amount, merchant, verdict, reason, and timestamp.

### `GET /transactions`
Returns all saved transactions, most recent first.

**Response:**
```json
[
  {
    "id": 1,
    "amount": 100.0,
    "merchant": "Some Store",
    "is_fraud": false,
    "reason": "No issues detected (placeholder rule, not real ML)"
  }
]
```

### `GET /samples`
Returns a small set of real transactions (mix of fraud and legitimate) sampled from the training dataset.

### `POST /samples/{sample_id}/predict`
Runs the real trained model against one sample transaction.

**Response:**
```json
{
  "sample_id": 6,
  "amount": 0.76,
  "actual_label": 0,
  "predicted_fraud": false,
  "fraud_probability": 0.16
}
```

`actual_label` is the real, known outcome from the dataset (0 = legitimate, 1 = fraud) — used to compare against the model's prediction.

## Conventions
- All new endpoints go in `backend/routers/`, grouped by feature (e.g. `transactions.py`, `predictions.py`).
- This document should be updated in the same commit/PR that adds or changes an endpoint.