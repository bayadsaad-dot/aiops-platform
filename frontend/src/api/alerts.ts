import api from "./axios";

export const getAlerts = async () => {
  const res = await api.get("/alerts");
  return res.data;
};

export const acknowledgeAlert = async (id: string) => {
  const res = await api.post(`/alerts/${id}/acknowledge`);
  return res.data;
};

export const resolveAlert = async (id: string) => {
  const res = await api.post(`/alerts/${id}/resolve`);
  return res.data;
};