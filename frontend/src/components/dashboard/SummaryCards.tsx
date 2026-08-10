import Grid from "@mui/material/Grid";
import ComputerIcon from "@mui/icons-material/Computer";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";
import WarningIcon from "@mui/icons-material/Warning";

import StatCard from "./StatCard";

interface SummaryCardsProps {
  dashboard: {
    total_assets: number;
    online_assets: number;
    offline_assets: number;
    open_alerts: number;
  };
}

export default function SummaryCards({
  dashboard,
}: SummaryCardsProps) {
  return (
    <Grid container spacing={3}>
      <Grid size={{ xs: 12, sm: 6, md: 3 }}>
        <StatCard
          title="Online Assets"
          value={dashboard.online_assets}
          icon={<CheckCircleIcon />}
          color="#2e7d32"
        />
      </Grid>

      <Grid size={{ xs: 12, sm: 6, md: 3 }}>
        <StatCard
          title="Offline Assets"
          value={dashboard.offline_assets}
          icon={<CancelIcon />}
          color="#d32f2f"
        />
      </Grid>

      <Grid size={{ xs: 12, sm: 6, md: 3 }}>
        <StatCard
          title="Total Assets"
          value={dashboard.total_assets}
          icon={<ComputerIcon />}
          color="#1976d2"
        />
      </Grid>

      <Grid size={{ xs: 12, sm: 6, md: 3 }}>
        <StatCard
          title="Open Alerts"
          value={dashboard.open_alerts}
          icon={<WarningIcon />}
          color="#ed6c02"
        />
      </Grid>
    </Grid>
  );
}