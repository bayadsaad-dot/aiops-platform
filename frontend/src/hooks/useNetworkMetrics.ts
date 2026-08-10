import { useEffect, useState } from "react";

import {
  getLatestNetworkMetrics,
  type NetworkMetric,
} from "../services/networkMetricService";

export function useNetworkMetrics() {
  const [metrics, setMetrics] = useState<NetworkMetric[]>([]);
  const [loading, setLoading] = useState(true);

  async function load() {
    try {
      const data = await getLatestNetworkMetrics();
      setMetrics(data);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();

    const interval = setInterval(load, 10000);

    return () => clearInterval(interval);
  }, []);

  return {
    metrics,
    loading,
  };
}