import { useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
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

import { useIncidents } from "../hooks/useIncidents";

export default function Incidents() {
  const [page, setPage] = useState(0);
  const [pageSize, setPageSize] = useState(10);
  const [search, setSearch] = useState("");
  const navigate = useNavigate();
  const {
    incidents,
    total,
    loading,
  } = useIncidents(page + 1, pageSize);

  const filteredIncidents = useMemo(() => {
    if (!search.trim()) return incidents;

    const value = search.toLowerCase();

    return incidents.filter(
      (incident) =>
        incident.title.toLowerCase().includes(value) ||
        incident.description.toLowerCase().includes(value)
    );
  }, [incidents, search]);

  const columns: GridColDef[] = [
    {
      field: "priority",
      headerName: "Priority",
      width: 140,
      renderCell: (params) => (
        <Chip
          label={params.value}
          color={
            params.value === "CRITICAL"
              ? "error"
              : params.value === "HIGH"
              ? "warning"
              : params.value === "MEDIUM"
              ? "info"
              : "success"
          }
          size="small"
        />
      ),
    },
    {
      field: "title",
      headerName: "Title",
      flex: 1,
    },
    {
      field: "description",
      headerName: "Description",
      flex: 1.5,
    },
    {
      field: "status",
      headerName: "Status",
      width: 160,
      renderCell: (params) => (
        <Chip
          label={params.value}
          color={
            params.value === "OPEN"
              ? "error"
              : params.value === "IN_PROGRESS"
              ? "warning"
              : "success"
          }
          size="small"
        />
      ),
    },
    {
      field: "assigned_to",
      headerName: "Assigned To",
      width: 180,
      valueGetter: (value) => value || "-",
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
        Incidents
      </Typography>

      <TextField
        fullWidth
        placeholder="Search incidents..."
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
        sx={{ mb: 3 }}
      />

      <Paper elevation={3}>
        <DataGrid
          rows={filteredIncidents}
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
            onRowClick={(params) => 
                 navigate(`/incidents/${params.id}`)
            }
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