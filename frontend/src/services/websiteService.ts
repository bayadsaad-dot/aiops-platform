import api from "../api/axios";
import type {
  Website,
  WebsiteCreate,
} from "../types/website";

export async function getWebsites(): Promise<Website[]> {
  const response = await api.get("/api/v1/websites");
  return response.data;
}

export async function createWebsite(
  data: WebsiteCreate
): Promise<Website> {
  const response = await api.post(
    "/api/v1/websites",
    data
  );

  return response.data;
}

export async function deleteWebsite(
  id: string
): Promise<void> {
  await api.delete(`/api/v1/websites/${id}`);
}