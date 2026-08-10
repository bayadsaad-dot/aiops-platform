import api from "../api/axios";

export interface DashboardSummary {
  total_assets: number;
  online_assets: number;
  offline_assets: number;
  open_alerts: number;
  avg_cpu: number;
  avg_memory: number;
  avg_disk: number;
}

export async function getDashboardSummary(): Promise<DashboardSummary> {
  const response = await api.get("/api/v1/dashboard/overview");
  return response.data;
}