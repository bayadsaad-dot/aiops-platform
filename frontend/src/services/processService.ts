import api from "../api/axios";

export interface Process {
  id: string;
  asset_id: string;
  pid: number;
  name: string;
  cpu_percent: number;
  memory_percent: number;
  executable: string | null;
  username: string | null;
  is_running: boolean;
  created_at: string;
}

export interface ProcessResponse {
  items: Process[];
  total: number;
  page: number;
  size: number;
}

export async function getAssetProcesses(
  assetId: string,
  page = 1,
  size = 50,
): Promise<ProcessResponse> {

  const response = await api.get(
    `/api/v1/processes/${assetId}`,
    {
      params: {
        page,
        size,
      },
    }
  );

  return response.data;
}