import { useEffect, useState } from "react";

import {
  getAssetProcesses,
  type Process,
} from "../services/processService";

export function useProcesses(
  assetId: string,
  page = 1,
  size = 50,
) {
  const [processes, setProcesses] = useState<Process[]>([]);
  const [total, setTotal] = useState(0);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!assetId) return;

    async function load() {
      try {
        const data = await getAssetProcesses(
          assetId,
          page,
          size,
        );

        setProcesses(data.items);
        setTotal(data.total);
        setError("");
      } catch {
        setError("Failed to load processes.");
      } finally {
        setLoading(false);
      }
    }

    load();

    const interval = setInterval(() => {
      load();
    }, 5000);

    return () => clearInterval(interval);

  }, [assetId, page, size]);

  return {
    processes,
    total,
    loading,
    error,
  };
}