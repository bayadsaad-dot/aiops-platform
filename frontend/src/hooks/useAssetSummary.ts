import { useEffect, useState } from "react";
import { getAssetSummary } from "../services/assetService";

export function useAssetSummary(id: string) {
  const [summary, setSummary] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      try {
        const data = await getAssetSummary(id);
        setSummary(data);
      } catch {
        setError("Failed to load asset summary");
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [id]);

  return { summary, loading, error };
}