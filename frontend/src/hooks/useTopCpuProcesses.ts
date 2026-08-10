import { useEffect, useState } from "react";

import { getTopCpuProcesses } from "../services/topProcessService";

export function useTopCpuProcesses(
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
      const data = await getTopCpuProcesses(
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