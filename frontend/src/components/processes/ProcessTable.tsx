import {
  Paper,
  Typography,
} from "@mui/material";

import {
  DataGrid,
  type GridColDef,
} from "@mui/x-data-grid";

import type { Process } from "../../services/processService";

interface Props {
  processes: Process[];
  loading: boolean;
}

const columns: GridColDef[] = [
  {
    field: "pid",
    headerName: "PID",
    width: 100,
  },
  {
    field: "name",
    headerName: "Process",
    flex: 1,
    minWidth: 220,
  },
  {
    field: "cpu_percent",
    headerName: "CPU %",
    width: 120,
  },
  {
    field: "memory_percent",
    headerName: "Memory %",
    width: 130,
  },
  {
    field: "username",
    headerName: "User",
    flex: 1,
    minWidth: 180,
  },
  {
    field: "is_running",
    headerName: "Running",
    width: 120,
    renderCell: (params) =>
      params.value ? "🟢 Yes" : "🔴 No",
  },
];

export default function ProcessTable({
  processes,
  loading,
}: Props) {
  return (
    <Paper sx={{ mt: 3, p: 2 }}>
      <Typography
        variant="h6"
        sx={{ mb: 2 }}
      >
        Running Processes
      </Typography>

      <DataGrid
        autoHeight
        rows={processes}
        columns={columns}
        loading={loading}
        pageSizeOptions={[10, 25, 50]}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 10,
            },
          },
        }}
      />
    </Paper>
  );
}