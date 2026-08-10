import api from "../api/axios";


export interface Incident {
  id: string;

  asset_id: string;
  alert_id: string;

  title: string;
  description: string;

  priority: string;
  status: string;

  assigned_to?: string | null;

  created_at: string;
  updated_at: string;
}

export interface IncidentResponse {
  items: Incident[];
  total: number;
  page: number;
  size: number;
}

export interface IncidentAnalysis {
  summary: string;
  root_cause: {
    type: string;
    description: string;
  };
  impact: string[];
  confidence: number;
  recommendations: string[];
}

export interface AnalyzeIncidentResponse {
  incident_id: string;
  analysis: IncidentAnalysis;
}

export async function getIncidents(
  page = 1,
  size = 10,
): Promise<IncidentResponse> {
  const response = await api.get("/api/v1/incidents/", {
    params: {
      page,
      size,
    },
  });

  return response.data;
}

export async function getIncident(
  id: string
): Promise<Incident> {
  const response = await api.get(
    `/api/v1/incidents/${id}`
  );

  return response.data;
}

export async function analyzeIncident(
  incidentId: string
): Promise<AnalyzeIncidentResponse> {
  const response = await api.post(
    `/api/v1/incidents/${incidentId}/analyze`
  );

  return response.data;
}