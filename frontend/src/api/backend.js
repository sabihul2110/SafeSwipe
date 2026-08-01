// SafeSwipe/frontend/src/api/backend.js

const BASE_URL = "http://localhost:8000";

export async function checkBackendHealth() {
  const response = await fetch(`${BASE_URL}/health`);
  return response.json();
}