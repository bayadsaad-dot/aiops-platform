import api from "../api/axios";

export async function analyzeIncident(id: string) {
  const response = await api.post(
    `/api/v1/incidents/${id}/analyze`
  );

  return response.data;
}