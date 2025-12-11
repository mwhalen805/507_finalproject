const API_BASE = "http://127.0.0.1:5000";

export async function fetchPartners(country: string): Promise<{ partners: string[] }> {
  const res = await fetch(`${API_BASE}/partners/${encodeURIComponent(country)}`);
  if (!res.ok) throw new Error("Failed to fetch partners");
  return res.json();
}

export async function fetchTopCountries(limit = 15): Promise<{ code: string, name: string, num_partners: number }[]> {
  const res = await fetch(`${API_BASE}/top-countries?limit=${limit}`);
  if (!res.ok) throw new Error("Failed to fetch top countries");
  return res.json();
}
