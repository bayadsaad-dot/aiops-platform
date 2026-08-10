import { useEffect, useState, useCallback } from "react";
import { getWebsites } from "../services/websiteService";
import type { Website } from "../types/website";

export function useWebsites() {
  const [websites, setWebsites] = useState<Website[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const refresh = useCallback(async () => {
    try {
      const data = await getWebsites();
      setWebsites(data);
      setError("");
    } catch (err) {
      console.error(err);
      setError("Failed to load websites.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    refresh();

    const interval = setInterval(() => {
      refresh();
    }, 10000);

    return () => clearInterval(interval);
  }, [refresh]);

  return {
    websites,
    loading,
    error,
    refresh,
  };
}