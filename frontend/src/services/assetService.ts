import api from "../api/axios";

export interface Asset {
  id: string;
  asset_code: string;
  hostname: string;
  ip_address: string;
  asset_type: string;
  status: string;
}

export interface AssetSummary {
  online: boolean;
  last_seen: string | null;
  current_cpu: number | null;
  avg_cpu_24h: number | null;
  max_cpu_24h: number | null;
  min_cpu_24h: number | null;
  current_memory: number | null;
  avg_memory_24h: number | null;
  current_disk: number | null;
  alerts: number;
}

interface AssetResponse {
  items: Asset[];
}

export async function getRecentAssets(): Promise<Asset[]> {
  const response = await api.get("/assets/", {
    params: {
      page: 1,
      size: 5,
    },
  });

  return response.data.items;
}

export async function getAssetSummary(
  id: string
): Promise<AssetSummary> {
  const response = await api.get(
    `/assets/${id}/summary`
  );

  return response.data;
}

export async function getAsset(
  id: string
): Promise<Asset> {
  const response = await api.get(`/assets/${id}`);
  return response.data;
}