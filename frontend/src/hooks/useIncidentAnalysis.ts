import { useState } from "react";
import { analyzeIncident } from "../services/aiService";

export function useIncidentAnalysis() {
  const [loading, setLoading] = useState(false);

  async function analyze(id: string) {
    setLoading(true);

    try {
      return await analyzeIncident(id);
    } finally {
      setLoading(false);
    }
  }

  return {
    analyze,
    loading,
  };
}