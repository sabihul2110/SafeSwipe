// SafeSwipe/frontend/src/api/backend.js

const BASE_URL = "http://localhost:8000";

export async function checkBackendHealth() {
  const response = await fetch(`${BASE_URL}/health`);
  return response.json();
}

export async function checkTransaction(amount, merchant) {
  const response = await fetch(`${BASE_URL}/transactions/check`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount, merchant }),
  });
  return response.json();
}