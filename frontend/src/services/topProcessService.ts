import api from "../api/axios";

export async function getTopCpuProcesses(
  assetId: string,
  limit = 10,
) {
  const response = await api.get(
    `/api/v1/processes/${assetId}/top/cpu`,
    {
      params: {
        limit,
      },
    }
  );

  return response.data;
}