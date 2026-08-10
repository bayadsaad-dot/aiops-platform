import api from "../api/axios";

export async function getAssetMetrics(assetId: string) {
  const response = await api.get(
    `/api/v1/metrics/asset/${assetId}`
  );

  return response.data.items;
}