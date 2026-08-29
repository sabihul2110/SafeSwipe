// SafeSwipe/frontend/src/api/backend.js

import { BASE_URL } from "../config/api";

async function handleResponse(response) {
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response.json();
}

export async function checkBackendHealth() {
  const response = await fetch(`${BASE_URL}/health`);
  return handleResponse(response);
}

export async function checkTransaction(amount, merchant) {
  const response = await fetch(`${BASE_URL}/transactions/check`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount, merchant }),
  });
  return handleResponse(response);
}

export async function getTransactionHistory() {
  const response = await fetch(`${BASE_URL}/transactions`);
  return handleResponse(response);
}


export async function clearTransactionHistory() {
  const response = await fetch(`${BASE_URL}/transactions`, {
    method: "DELETE",
  });
  return handleResponse(response);
}

export async function getSamples() {
  const response = await fetch(`${BASE_URL}/samples`);
  return handleResponse(response);
}

export async function predictSample(sampleId) {
  const response = await fetch(`${BASE_URL}/samples/${sampleId}/predict`, {
    method: "POST",
  });
  return handleResponse(response);
}


export async function getModelInfo() {
  const response = await fetch(`${BASE_URL}/model-info`);
  return handleResponse(response);
}
