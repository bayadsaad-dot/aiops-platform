import { useEffect, useState } from "react";
import { getAssetMetrics } from "../services/metricService";

export function useMetrics(assetId: string) {
  const [metrics, setMetrics] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!assetId) return;

    async function load() {
      try {
        const data = await getAssetMetrics(assetId);
        setMetrics(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    load();

    const interval = setInterval(() => {
      load();
    }, 5000);

    return () => clearInterval(interval);

  }, [assetId]);

  return {
    metrics,
    loading,
  };
}