import api from "../api/axios";

export interface Alert {
  id: string;
  asset_id: string;
  asset_hostname: string;

  title: string;
  message: string;

  severity: string;
  status: string;

  created_at: string;
  resolved_at?: string | null;
}

export interface AlertResponse {
  items: Alert[];
  total: number;
  page: number;
  size: number;
}

export async function getAlerts(
  page = 1,
  size = 10,
): Promise<AlertResponse> {
  const response = await api.get("/api/v1/alerts/", {
    params: {
      page,
      size,
    },
  });

  return response.data;
}

export async function getRecentAlerts(): Promise<Alert[]> {
  const response = await api.get("/api/v1/alerts/", {
    params: {
      page: 1,
      size: 5,
    },
  });

  return response.data.items;
}