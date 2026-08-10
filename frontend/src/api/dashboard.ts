import api from "./axios";

export const getOverview = async () => {
    const res = await api.get("/dashboard/overview");
    return res.data;
};