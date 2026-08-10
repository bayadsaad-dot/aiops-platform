import { useParams } from "react-router-dom";

import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import TopCpuChart from "../components/charts/TopCpuChart";
import { useTopCpuProcesses } from "../hooks/useTopCpuProcesses";
import { useAsset } from "../hooks/useAsset";
import { useAssetSummary } from "../hooks/useAssetSummary";
import { useMetrics } from "../hooks/useMetrics";
import { useAssetNetworkMetrics } from "../hooks/useAssetNetworkMetrics";
import WarningAmberIcon from "@mui/icons-material/WarningAmber";
import TopMemoryChart from "../components/charts/TopMemoryChart";
import { useTopMemoryProcesses } from "../hooks/useTopMemoryProcesses";
import MetricCard from "../components/dashboard/MetricCard";
import ProcessTable from "../components/processes/ProcessTable";
import { useProcesses } from "../hooks/useProcesses";
import CpuHistoryChart from "../components/charts/CpuHistoryChart";
import MemoryHistoryChart from "../components/charts/MemoryHistoryChart";
import DiskHistoryChart from "../components/charts/DiskHistoryChart";
import SaveIcon from "@mui/icons-material/Save";
import StorageIcon from "@mui/icons-material/Storage";
import MemoryIcon from "@mui/icons-material/Memory";
import NetworkSpeedChart from "../components/charts/NetworkSpeedChart";
import BytesHistoryChart from "../components/charts/BytesHistoryChart";
import PacketsHistoryChart from "../components/charts/PacketsHistoryChart";

export default function AssetDetails() {
  const { id } = useParams();
  const {
     processes: topCpuProcesses, 
     loading: topCpuLoading,
  } = useTopCpuProcesses(id!);
  const { asset } = useAsset(id!);

  const {
    summary,
    loading,
    error,
  } = useAssetSummary(id!);

  const {
    metrics,
    loading: metricsLoading,
  } = useMetrics(id!);

  const {
    processes,
    loading: processesLoading,
    } = useProcesses(id!);
  
  const {
    processes: topMemoryProcesses,
    loading: topMemoryLoading,
  } = useTopMemoryProcesses(id!);   


  const {
    metrics: networkMetrics,
    loading: networkLoading,
  } = useAssetNetworkMetrics(id!);

  if (loading) {
    return (
      <Container sx={{ mt: 3 }}>
        Loading...
      </Container>
    );
  }

  if (error) {
    return (
      <Container sx={{ mt: 3 }}>
        {error}
      </Container>
    );
  }

  return (
    <Container maxWidth="xl" sx={{ mt: 3 }}>
      <Box sx={{ mb: 4 }}>
        <Typography variant="h4" fontWeight="bold">
          {asset?.hostname}
        </Typography>

        <Typography color="text.secondary">
          {asset?.ip_address}
        </Typography>

        <Typography sx={{ mt: 1 }}>
          Status:
          <strong> {asset?.status}</strong>
        </Typography>

        <Typography color="text.secondary">
          Type: {asset?.asset_type}
        </Typography>
      </Box>

      <Grid container spacing={3}>
        <Grid size={{ xs: 12, md: 3 }}>
          <MetricCard
            title="CPU"
            value={`${summary.current_cpu}%`}
            icon={<MemoryIcon color="primary" />}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <MetricCard
            title="Memory"
            value={`${summary.current_memory}%`}
            icon={<StorageIcon color="success" />}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <MetricCard
            title="Disk"
            value={`${summary.current_disk}%`}
            icon={<SaveIcon color="warning" />}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <MetricCard
            title="Alerts"
            value={summary.alerts}
            icon={<WarningAmberIcon color="warning" />}
          />
        </Grid>
      </Grid>

      <Box
        sx={{
          mt: 5,
          p: 3,
          border: "1px solid #ddd",
          borderRadius: 2,
          bgcolor: "background.paper",
        }}
      >
        <Typography variant="h6" sx={{ mb: 2 }}>
          CPU History
        </Typography>

        {metricsLoading ? (
          "Loading..."
        ) : (
          <CpuHistoryChart data={metrics} />
        )}
      </Box>

      <Box
        sx={{
          mt: 3,
          p: 3,
          border: "1px solid #ddd",
          borderRadius: 2,
          bgcolor: "background.paper",
        }}
      >
        <Typography variant="h6" sx={{ mb: 2 }}>
          Memory History
        </Typography>

        {metricsLoading ? (
          "Loading..."
        ) : (
          <MemoryHistoryChart data={metrics} />
        )}
      </Box>

      <Box
        sx={{
          mt: 3,
          p: 3,
          border: "1px solid #ddd",
          borderRadius: 2,
          bgcolor: "background.paper",
        }}
      >
        <Typography variant="h6" sx={{ mb: 2 }}>
          Disk History
        </Typography>

        {metricsLoading ? (
          "Loading..."
        ) : (
          <DiskHistoryChart data={metrics} />
        )}
      </Box>

            <Box
        sx={{
          mt: 3,
          p: 3,
          border: "1px solid #ddd",
          borderRadius: 2,
          bgcolor: "background.paper",
        }}
      >
        <Typography variant="h6" sx={{ mb: 2 }}>
          Network Speed
        </Typography>

        {networkLoading ? (
          "Loading..."
        ) : (
          <NetworkSpeedChart data={networkMetrics} />
        )}
      </Box>

      <Box
        sx={{
          mt: 3,
          p: 3,
          border: "1px solid #ddd",
          borderRadius: 2,
          bgcolor: "background.paper",
        }}
      >
        <Typography variant="h6" sx={{ mb: 2 }}>
          Network Bytes
        </Typography>

        {networkLoading ? (
          "Loading..."
        ) : (
          <BytesHistoryChart data={networkMetrics} />
        )}
      </Box>

      <Box
        sx={{
          mt: 3,
          p: 3,
          border: "1px solid #ddd",
          borderRadius: 2,
          bgcolor: "background.paper",
        }}
      >
        <Typography variant="h6" sx={{ mb: 2 }}>
          Network Packets
        </Typography>

        {networkLoading ? (
          "Loading..."
        ) : (
          <PacketsHistoryChart data={networkMetrics} />
        )}
      </Box>

       <Box
          sx={{
            mt: 3,
            p: 3,
            border: "1px solid #ddd",
            borderRadius: 2,
            bgcolor: "background.paper",
         }}
        >
       {topCpuLoading ? (
         "Loading..."
       ) : (
        <TopCpuChart data={topCpuProcesses} />
      )}
     </Box>

     <Box
        sx={{
          mt: 3,
          p: 3,
          border: "1px solid #ddd",
          borderRadius: 2,
          bgcolor: "background.paper",
        }}
      >
        

        {topMemoryLoading ? (
          "Loading..."
        ) : (
          <TopMemoryChart data={topMemoryProcesses} />
        )}
      </Box>

     <ProcessTable
       processes={processes}
       loading={processesLoading}
     />
     </Container>
     );
     }