import { useEffect, useState } from "react";
import {
  getRecentAssets,
  type Asset,
} from "../services/assetService";

export function useAssets() {
  const [assets, setAssets] = useState<Asset[]>([]);
  const [loading, setLoading] = useState(true);

  async function loadAssets() {
    try {
      const data = await getRecentAssets();
      console.log("Assets API:", data);
      setAssets(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadAssets();
  }, []);

  return {
    assets,
    loading,
  };
}