import api from "./axios";

export const getAssets = async () => {
  const res = await api.get("/assets");
  return res.data;
};

export const getAsset = async (id: string) => {
  const res = await api.get(`/assets/${id}`);
  return res.data;
};