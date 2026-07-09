// This file is the ONLY place in the frontend that knows the backend URL.
// Every API call in the app should go through functions defined here
// (or in files that import this base URL) instead of hardcoding URLs
// in components. This makes it easy to change the backend URL later.

export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";

// Example generic fetch wrapper - we will expand this when we build
// real features (tools list, categories, search, etc.)
export async function apiFetch<T>(
  endpoint: string,
  options?: RequestInit
): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
      ...options?.headers,
    },
    ...options,
  });

  if (!res.ok) {
    throw new Error(`API error: ${res.status} ${res.statusText}`);
  }

  return res.json() as Promise<T>;
}
