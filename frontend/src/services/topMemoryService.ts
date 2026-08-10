import api from "../api/axios";

export async function getTopMemoryProcesses(
  assetId: string,
  limit = 10,
) {
  const response = await api.get(
    `/api/v1/processes/${assetId}/top/memory`,
    {
      params: {
        limit,
      },
    }
  );

  return response.data;
}