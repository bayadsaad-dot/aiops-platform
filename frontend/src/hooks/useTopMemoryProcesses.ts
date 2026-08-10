import { useEffect, useState } from "react";

import { getTopMemoryProcesses } from "../services/topMemoryService";

export function useTopMemoryProcesses(
  assetId: string,
) {
  const [processes, setProcesses] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!assetId) return;

    loadProcesses();
  }, [assetId]);

  async function loadProcesses() {
    try {
      const data = await getTopMemoryProcesses(
        assetId,
      );

      setProcesses(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  return {
    processes,
    loading,
  };
}