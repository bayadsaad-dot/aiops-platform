import { useMemo, useState } from "react";

import {
  Box,
  Chip,
  CircularProgress,
  Paper,
  Stack,
  TextField,
  Typography,
} from "@mui/material";

import {
  DataGrid,
  type GridColDef,
} from "@mui/x-data-grid";

import { useAlerts } from "../hooks/useAlerts";

export default function Alerts() {
  const [page, setPage] = useState(0);
  const [pageSize, setPageSize] = useState(10);
  const [search, setSearch] = useState("");

  const {
    alerts,
    total,
    loading,
  } = useAlerts(page + 1, pageSize);

  const filteredAlerts = useMemo(() => {
    if (!search.trim()) return alerts;

    const value = search.toLowerCase();

    return alerts.filter(
      (alert) =>
        alert.title.toLowerCase().includes(value) ||
        alert.message.toLowerCase().includes(value) ||
        alert.asset_hostname.toLowerCase().includes(value),
    );
  }, [alerts, search]);

  const columns: GridColDef[] = [
    {
      field: "severity",
      headerName: "Severity",
      width: 140,
      renderCell: (params) => (
        <Chip
          label={params.value}
          color={
            params.value === "CRITICAL"
              ? "error"
              : params.value === "WARNING"
              ? "warning"
              : "success"
          }
          size="small"
        />
      ),
    },
    {
      field: "asset_hostname",
      headerName: "Asset",
      width: 160,
    },
    {
      field: "title",
      headerName: "Title",
      flex: 1,
    },
    {
      field: "message",
      headerName: "Message",
      flex: 1.4,
    },
    {
      field: "status",
      headerName: "Status",
      width: 140,
      renderCell: (params) => (
        <Chip
          label={params.value}
          color={
            params.value === "OPEN"
              ? "error"
              : "success"
          }
          size="small"
        />
      ),
    },
    {
      field: "created_at",
      headerName: "Created",
      width: 190,
      valueFormatter: (value) =>
        value
          ? new Date(value as string).toLocaleString()
          : "-",
    },
    {
      field: "resolved_at",
      headerName: "Resolved",
      width: 190,
      valueFormatter: (value) =>
        value
          ? new Date(value as string).toLocaleString()
          : "-",
    },
  ];

  if (loading) {
    return (
      <Stack
        height="70vh"
        justifyContent="center"
        alignItems="center"
      >
        <CircularProgress />
      </Stack>
    );
  }

  return (
    <Box p={4}>
      <Typography
        variant="h3"
        fontWeight={700}
        mb={3}
      >
        Alerts
      </Typography>

      <TextField
        fullWidth
        placeholder="Search alerts..."
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
        sx={{ mb: 3 }}
      />

      <Paper elevation={3}>
      <DataGrid
         rows={filteredAlerts}
         columns={columns}
         loading={loading}
         rowCount={total}
         paginationMode="server"
         paginationModel={{
           page,
           pageSize,
        }}
         onPaginationModelChange={(model) => {
           setPage(model.page);
           setPageSize(model.pageSize);
       }} 
        pageSizeOptions={[5, 10, 20, 50]}
        disableRowSelectionOnClick
        autoHeight
        sx={{
         border: 0,
         "& .MuiDataGrid-columnHeaders": {
           backgroundColor: "#f5f5f5",
           fontWeight: "bold",
       },
     }}
     />
        </Paper>
    </Box>
  );
}   