import { useEffect, useState } from "react";

import {
  getAsset,
  type Asset,
} from "../services/assetService";

export function useAsset(id: string) {
  const [asset, setAsset] =
    useState<Asset | null>(null);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {
    async function load() {
      try {
        const data = await getAsset(id);

        setAsset(data);

        setError("");
      } catch {
        setError("Failed to load asset");
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [id]);

  return {
    asset,
    loading,
    error,
  };
}