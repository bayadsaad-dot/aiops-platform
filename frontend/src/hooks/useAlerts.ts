import { useEffect, useState } from "react";
import {
  getAlerts,
  type Alert,
} from "../services/alertService";

export function useAlerts(
  page = 1,
  size = 10,
) {
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [total, setTotal] = useState(0);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadAlerts();
  }, [page, size]);

  async function loadAlerts() {
    try {
      setLoading(true);

      const data = await getAlerts(
        page,
        size,
      );

      setAlerts(data.items);
      setTotal(data.total);
    } finally {
      setLoading(false);
    }
  }

  return {
    alerts,
    total,
    loading,
  };
}