// SafeSwipe/frontend/src/api/backend.js

import { BASE_URL } from "../config/api";

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


export async function getTransactionHistory() {
  const response = await fetch(`${BASE_URL}/transactions`);
  return response.json();
}