import api from "./axios";

export const getAssetMetrics = async (
  assetId: string,
  period = "24h"
) => {
  const res = await api.get(`/metrics/asset/${assetId}`, {
    params: {
      page: 1,
      size: 100,
      period,
    },
  });

  return res.data;
};