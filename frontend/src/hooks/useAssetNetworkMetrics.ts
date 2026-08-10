import { useEffect, useState } from "react";

import {
  getAssetNetworkMetrics,
  type NetworkMetric,
} from "../services/networkMetricService";

export function useAssetNetworkMetrics(
  assetId: string
) {
  const [metrics, setMetrics] = useState<
    NetworkMetric[]
  >([]);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const data =
          await getAssetNetworkMetrics(assetId);

        setMetrics(data);
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [assetId]);

  return {
    metrics,
    loading,
  };
}