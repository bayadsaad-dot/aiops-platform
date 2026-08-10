import api from "./axios";

export const getIncidents = async () => {
  const res = await api.get("/incidents");
  return res.data;
};

export const getIncident = async (id: string) => {
  const res = await api.get(`/incidents/${id}`);
  return res.data;
};

export const analyzeIncident = async (id: string) => {
  const res = await api.post(`/incidents/${id}/analyze`);
  return res.data;
};

export const generateIncidentReport = async (id: string) => {
  const res = await api.post(`/incidents/${id}/report`);
  return res.data;
};