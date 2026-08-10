import api from "../api/axios";

export interface NetworkMetric {
  id: string;
  asset_id: string;
  interface_id: string;

  bytes_sent: number;
  bytes_received: number;

  packets_sent: number;
  packets_received: number;

  upload_speed: number;
  download_speed: number;

  created_at: string;
}

interface NetworkMetricResponse {
  items: NetworkMetric[];
  total: number;
  page: number;
  size: number;
}

export async function getLatestNetworkMetrics(
  limit = 20
): Promise<NetworkMetric[]> {
  const response = await api.get(
    "/api/v1/network/metrics/latest",
    {
      params: { limit },
    }
  );

  return response.data.items;
}

export async function getAssetNetworkMetrics(
  assetId: string
): Promise<NetworkMetric[]> {
  const response = await api.get(
    `/api/v1/network/metrics/${assetId}`,
    {
      params: {
        page: 1,
        size: 100,
      },
    }
  );

  return response.data.items;
}