import { useEffect, useState } from "react";

import {
  getIncidents,
  type Incident,
} from "../services/incidentService";

export function useIncidents(
  page: number,
  size: number,
) {
  const [incidents, setIncidents] = useState<Incident[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadIncidents();
  }, [page, size]);

  async function loadIncidents() {
    setLoading(true);

    try {
      const data = await getIncidents(page, size);

      setIncidents(data.items);
      setTotal(data.total);
    } finally {
      setLoading(false);
    }
  }

  return {
    incidents,
    total,
    loading,
  };
}